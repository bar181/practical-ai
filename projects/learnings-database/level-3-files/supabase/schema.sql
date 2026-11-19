-- Learnings database, level 3: one table in Postgres (Supabase or any Postgres 15+ with pgvector).
--
-- What this gives you:
--   learnings.learnings      the log: the same 18 columns as the spreadsheet, plus what a database adds
--   learnings.lists          the Areas, Lesson types and Projects lists, editable
--   learnings.history        every insert and change, with who made it: nothing is lost
--   learnings.served_log     every time a rule was handed to someone, so reuse can be measured
--   learnings.served_rules   the only view agents may read: accepted and not sensitive
--   functions                log_learning, mark_seen, find_rules, review_queue, set_status
--   roles                    learnings_agent (log and read rules only) and learnings_owner (everything)
--
-- The two safety rules, enforced here rather than trusted to the assistant:
--   1. Anything written by an agent arrives as 'proposed'. Only the owner's role can accept it.
--   2. Agents never read the table itself: only accepted, non-sensitive rules, through the view or
--      find_rules. A row's text is data; nothing here executes it.
--
-- Run once on an empty project:  psql "$DATABASE_URL" -f schema.sql
-- In Supabase, paste it into the SQL editor, or apply it as a migration.

create extension if not exists vector;
create schema if not exists learnings;

-- Roles. In Supabase, give a database user one of these roles for the MCP server's connection.
do $$ begin
  if not exists (select 1 from pg_roles where rolname = 'learnings_agent') then create role learnings_agent nologin; end if;
  if not exists (select 1 from pg_roles where rolname = 'learnings_owner') then create role learnings_owner nologin; end if;
end $$;

create table if not exists learnings.lists (
  list        text not null check (list in ('kind', 'area', 'lesson_type', 'project')),
  value       text not null,
  means       text,
  primary key (list, value)
);

create sequence if not exists learnings.id_seq;

create table if not exists learnings.learnings (
  id            text primary key default 'L-' || nextval('learnings.id_seq'),
  date          date not null default current_date,
  kind          text not null check (kind in ('error', 'redo', 'worked')),
  area          text not null,
  project       text,
  lesson_type   text,
  rule          text not null check (length(rule) between 10 and 400),
  what_happened text,
  expected      text,
  why           text,
  tags          text[] not null default '{}',
  severity      text check (severity in ('low', 'medium', 'high')),
  status        text not null default 'proposed' check (status in ('proposed', 'accepted', 'merged', 'retired')),
  merged_into   text references learnings.learnings (id),
  seen          integer not null default 1 check (seen >= 1),
  source        text not null default 'agent' check (source in ('chat', 'review', 'person', 'agent', 'import')),
  sensitive     boolean not null default true,          -- unknown counts as sensitive
  confidence    text check (confidence in ('high', 'medium', 'low')),
  review_by     date,
  owner         text,
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now(),
  fts           tsvector,
  embedding     vector(384)                             -- 384 dimensions, as Supabase's gte-small; change to match your model
);

create index if not exists learnings_fts_idx on learnings.learnings using gin (fts);
create index if not exists learnings_filter_idx on learnings.learnings (status, area, project);
create index if not exists learnings_embedding_idx on learnings.learnings using hnsw (embedding vector_cosine_ops);

create table if not exists learnings.history (
  at         timestamptz not null default now(),
  id         text not null,
  action     text not null,
  by_role    text not null default current_user,
  approved_by text,
  before     jsonb,
  after      jsonb
);

create table if not exists learnings.served_log (
  at        timestamptz not null default now(),
  id        text not null,
  for_work  text,
  by_role   text not null default current_user
);

-- Keep the search text, the time stamp and the lists in step on every write.
create or replace function learnings.before_write() returns trigger language plpgsql as $$
begin
  new.fts := to_tsvector('english', coalesce(new.rule, '') || ' ' || coalesce(new.what_happened, '') || ' ' ||
             coalesce(new.expected, '') || ' ' || coalesce(new.why, '') || ' ' || array_to_string(new.tags, ' '));
  new.updated_at := now();
  if new.area not like 'new:%' and not exists (select 1 from learnings.lists where list = 'area' and value = new.area) then
    raise exception 'area % is not on the Areas list (a new one is written new:<word>)', new.area;
  end if;
  if new.lesson_type is not null and new.lesson_type not like 'new:%'
     and not exists (select 1 from learnings.lists where list = 'lesson_type' and value = new.lesson_type) then
    raise exception 'lesson type % is not on the Lesson types list', new.lesson_type;
  end if;
  if new.status = 'merged' and new.merged_into is null then
    raise exception 'a merged row needs merged_into';
  end if;
  return new;
end $$;

create or replace function learnings.after_write() returns trigger language plpgsql security definer set search_path = learnings, public as $$
begin
  insert into learnings.history (id, action, approved_by, before, after)
  values (new.id, tg_op, current_setting('learnings.approved_by', true),
          case when tg_op = 'UPDATE' then to_jsonb(old) - 'embedding' - 'fts' end, to_jsonb(new) - 'embedding' - 'fts');
  return new;
end $$;

drop trigger if exists learnings_before on learnings.learnings;
create trigger learnings_before before insert or update on learnings.learnings
  for each row execute function learnings.before_write();
drop trigger if exists learnings_after on learnings.learnings;
create trigger learnings_after after insert or update on learnings.learnings
  for each row execute function learnings.after_write();

-- The only view agents read.
create or replace view learnings.served_rules as
  select id, date, kind, area, project, lesson_type, rule, seen, review_by
  from learnings.learnings
  where status = 'accepted' and sensitive = false;

-- log_learning: write one row. Whoever calls it, the row starts as 'proposed', seen 1.
create or replace function learnings.log_learning(
  p_kind text, p_area text, p_rule text,
  p_project text default null, p_lesson_type text default null,
  p_what_happened text default null, p_expected text default null, p_why text default null,
  p_tags text[] default '{}', p_severity text default null, p_sensitive boolean default true,
  p_confidence text default null, p_review_by date default null, p_date date default current_date,
  p_source text default 'agent', p_embedding vector default null
) returns text language plpgsql security definer set search_path = learnings, public as $$
declare new_id text;
begin
  insert into learnings.learnings (date, kind, area, project, lesson_type, rule, what_happened, expected, why,
                                   tags, severity, status, seen, source, sensitive, confidence, review_by, embedding)
  values (p_date, p_kind, p_area, nullif(p_project, ''), p_lesson_type, p_rule, p_what_happened, p_expected, p_why,
          coalesce(p_tags, '{}'), p_severity, 'proposed', 1,
          case when p_source in ('chat', 'agent') then p_source else 'agent' end,
          coalesce(p_sensitive, true), p_confidence, p_review_by, p_embedding)
  returning id into new_id;
  return new_id;
end $$;

-- mark_seen: the same lesson happened again. Raises seen; changes nothing else.
create or replace function learnings.mark_seen(p_id text) returns integer
language plpgsql security definer set search_path = learnings, public as $$
declare n integer;
begin
  update learnings.learnings set seen = seen + 1 where id = p_id returning seen into n;
  if n is null then raise exception 'no row %', p_id; end if;
  return n;
end $$;

-- find_rules: accepted, non-sensitive rules only. Filters are exact; the words and the embedding,
-- when given, rank what the filters let through (hybrid search: keyword rank and similarity,
-- combined by reciprocal rank fusion). Every row returned is recorded in served_log.
create or replace function learnings.find_rules(
  p_project text default null, p_area text default null, p_kind text default null,
  p_words text default null, p_embedding vector default null, p_limit integer default 5,
  p_for_work text default null
) returns table (id text, rule text, area text, project text, lesson_type text, kind text, seen integer, score double precision)
language plpgsql security definer set search_path = learnings, public as $$
begin
  return query
  with base as (
    select l.* from learnings.learnings l
    where l.status = 'accepted' and l.sensitive = false
      and (p_project is null or l.project = p_project or l.project is null)
      and (p_area is null or l.area = p_area)
      and (p_kind is null or l.kind = p_kind)
  ),
  kw as (
    select b.id, row_number() over (order by ts_rank_cd(b.fts, websearch_to_tsquery('english', p_words)) desc) as r
    from base b where p_words is not null and b.fts @@ websearch_to_tsquery('english', p_words)
  ),
  sem as (
    select b.id, row_number() over (order by b.embedding <=> p_embedding) as r
    from base b where p_embedding is not null and b.embedding is not null
    order by b.embedding <=> p_embedding limit 50
  ),
  ranked as (
    select b.id,
      case when p_words is null and p_embedding is null then b.seen::double precision
           else coalesce(1.0 / (60 + kw.r), 0) + coalesce(1.0 / (60 + sem.r), 0) end as score
    from base b left join kw on kw.id = b.id left join sem on sem.id = b.id
    where (p_words is null and p_embedding is null) or kw.id is not null or sem.id is not null
  ),
  chosen as (
    select r.id, r.score from ranked r join base b on b.id = r.id
    order by r.score desc, b.seen desc, b.date desc
    limit least(greatest(coalesce(p_limit, 5), 1), 10)
  ),
  logged as (
    insert into learnings.served_log (id, for_work) select c.id, p_for_work from chosen c returning 1
  )
  select b.id, b.rule, b.area, b.project, b.lesson_type, b.kind, b.seen, c.score
  from chosen c join base b on b.id = c.id
  where (select count(*) from logged) >= 0
  order by c.score desc, b.seen desc, b.date desc;
end $$;

-- similar_rows: search before you write. Any row not retired with the same area and project, or
-- sharing words with the new rule. The text of a sensitive row is never returned, only its id.
create or replace function learnings.similar_rows(p_area text, p_project text default null, p_words text default null)
returns table (id text, status text, seen integer, rule text, match text)
language sql security definer set search_path = learnings, public as $$
  select l.id, l.status, l.seen, case when l.sensitive then '(sensitive row: ask the owner)' else l.rule end,
         case when p_words is not null and l.fts @@ websearch_to_tsquery('english', p_words) then 'shares words'
              else 'same area and project' end
  from learnings.learnings l
  where l.status <> 'retired'
    and ((l.area = p_area and coalesce(l.project, '') = coalesce(p_project, ''))
         or (p_words is not null and l.fts @@ websearch_to_tsquery('english', p_words)))
  order by case when p_words is null then 0 else ts_rank_cd(l.fts, websearch_to_tsquery('english', p_words)) end desc,
           l.seen desc
  limit 5;
$$;

-- review_queue: for the owner. Proposed rows, and accepted rows past their review date.
create or replace function learnings.review_queue() returns setof learnings.learnings
language sql security definer set search_path = learnings, public as $$
  select * from learnings.learnings
  where status = 'proposed' or (status = 'accepted' and review_by is not null and review_by <= current_date)
  order by status, date;
$$;

-- set_status: the owner's decision. Needs the name of the person who approved it, kept in history.
create or replace function learnings.set_status(p_id text, p_status text, p_approved_by text, p_merged_into text default null)
returns text language plpgsql security definer set search_path = learnings, public as $$
begin
  if coalesce(trim(p_approved_by), '') = '' then raise exception 'set_status needs the name of the person who approved it'; end if;
  perform set_config('learnings.approved_by', p_approved_by, true);
  update learnings.learnings set status = p_status, merged_into = p_merged_into where id = p_id;
  if not found then raise exception 'no row %', p_id; end if;
  return p_status;
end $$;

-- Permissions: agents call functions and read the view; only the owner touches the table.
alter table learnings.learnings enable row level security;
alter table learnings.history enable row level security;
alter table learnings.served_log enable row level security;
revoke all on all tables in schema learnings from public;
revoke all on all functions in schema learnings from public;
grant usage on schema learnings to learnings_agent, learnings_owner;
grant select on learnings.served_rules, learnings.lists to learnings_agent;
grant execute on function learnings.log_learning, learnings.mark_seen, learnings.find_rules, learnings.similar_rows to learnings_agent;
grant select, insert, update on all tables in schema learnings to learnings_owner;
grant usage, select, update on sequence learnings.id_seq to learnings_owner;
grant execute on all functions in schema learnings to learnings_owner;
drop policy if exists owner_all on learnings.learnings;
create policy owner_all on learnings.learnings for all to learnings_owner using (true) with check (true);
drop policy if exists owner_history on learnings.history;
create policy owner_history on learnings.history for select to learnings_owner using (true);
drop policy if exists owner_served on learnings.served_log;
create policy owner_served on learnings.served_log for select to learnings_owner using (true);

-- Starting lists. Edit them with: insert into learnings.lists values ('project', 'my-project', '...');
insert into learnings.lists (list, value, means) values
  ('kind', 'error', 'Something failed or was wrong'),
  ('kind', 'redo', 'Work had to be rebuilt or rewritten'),
  ('kind', 'worked', 'A departure from the usual way that worked better than expected'),
  ('area', 'marketing', 'Messages, posts, campaigns, the website, brand and audience'),
  ('area', 'sales', 'Leads, quotes, proposals, follow-up and pricing to a customer'),
  ('area', 'customers', 'Service, complaints, onboarding and what customers actually want'),
  ('area', 'decisions', 'How a choice was made: the options, the evidence, and what we would weigh differently'),
  ('area', 'operations', 'Suppliers, scheduling, delivery and the steps of the work itself'),
  ('area', 'finance', 'Invoices, payments, costs, budgets and the numbers behind them'),
  ('area', 'people', 'Hiring, delegating, training and working with a team or contractor'),
  ('area', 'coding', 'Software, scripts, spreadsheets with formulas, and building with agents'),
  ('area', 'working-with-ai', 'Prompts, instructions, checking AI output and what a chatbot gets wrong'),
  ('area', 'other', 'Anything that fits none of the above'),
  ('lesson_type', 'process', 'A step was missing, in the wrong order or done twice'),
  ('lesson_type', 'tool', 'A tool, app or platform behaved in a way we did not expect'),
  ('lesson_type', 'instruction', 'How something was asked, of a person or an AI, decided the result'),
  ('lesson_type', 'check', 'A check would have caught it, or did'),
  ('lesson_type', 'judgement', 'A rule of thumb for a decision'),
  ('lesson_type', 'communication', 'Who was told what, when, and how'),
  ('lesson_type', 'insight', 'Something learned about customers, the market or the work that changes what we do')
on conflict (list, value) do update set means = excluded.means;
