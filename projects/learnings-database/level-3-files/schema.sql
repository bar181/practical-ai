-- Learnings database, level 3: a shared log in Supabase (or any Postgres 14+).
-- Paste this whole file into Supabase's SQL editor and press Run. Running it again is safe.
--
-- What it makes, in a schema of its own called learnings:
--   learnings.learnings   one row per lesson: the same 18 columns as the spreadsheet
--   learnings.lists       the areas, lesson types, kinds and your projects
--   learnings.history     every insert and change, with who approved it
-- and six functions, the only things an assistant should call:
--   select learnings.log_learning(...)        add a lesson; always 'proposed'
--   select * from learnings.similar_rows(...) look for a repeat before adding
--   select learnings.mark_seen('L-9')         the same lesson again: seen + 1
--   select * from learnings.find_rules(...)   accepted rules for the work (rules only, no details)
-- (and select * from learnings.lists, to see the areas, lesson types and projects)
--   select * from learnings.review_queue()    the weekly review
--   select learnings.set_status('L-9', 'accepted', 'Your Name')   the person's decision
-- Row level security is on with no policies, so the public API cannot read or write the log.

create schema if not exists learnings;

create table if not exists learnings.lists (
  list   text not null check (list in ('kind', 'area', 'lesson_type', 'project')),
  value  text not null,
  means  text,
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
  tags          text,                                   -- separated by ; as in the sheet
  severity      text check (severity in ('low', 'medium', 'high')),
  status        text not null default 'proposed' check (status in ('proposed', 'accepted', 'merged', 'retired')),
  seen          integer not null default 1 check (seen >= 1),
  source        text not null default 'chat' check (source in ('chat', 'review', 'person', 'agent', 'import')),
  sensitive     boolean not null default true,          -- unknown counts as sensitive
  confidence    text check (confidence in ('high', 'medium', 'low')),
  review_by     date,
  merged_into   text references learnings.learnings (id),
  updated_at    timestamptz not null default now(),
  fts           tsvector
);

create index if not exists learnings_fts_idx on learnings.learnings using gin (fts);

create table if not exists learnings.history (
  at          timestamptz not null default now(),
  id          text not null,
  action      text not null,
  approved_by text,
  before      jsonb,
  after       jsonb
);

-- On every write: check the lists, keep the search text and the id counter in step.
create or replace function learnings.before_write() returns trigger language plpgsql as $$
begin
  if new.area not like 'new:%' and not exists (select 1 from learnings.lists where list = 'area' and value = new.area) then
    raise exception 'area "%" is not on the Areas list (a new one is written new:<word>)', new.area;
  end if;
  if new.lesson_type is not null and new.lesson_type not like 'new:%'
     and not exists (select 1 from learnings.lists where list = 'lesson_type' and value = new.lesson_type) then
    raise exception 'lesson type "%" is not on the Lesson types list', new.lesson_type;
  end if;
  if new.status = 'merged' and new.merged_into is null then
    raise exception 'a merged row needs merged_into, the id it was merged into';
  end if;
  new.fts := to_tsvector('english', concat_ws(' ', new.rule, new.what_happened, new.expected, new.why, replace(new.tags, ';', ' ')));
  new.updated_at := now();
  if new.id ~ '^L-[0-9]+$' and substr(new.id, 3)::bigint > (select case when is_called then last_value else 0 end from learnings.id_seq) then
    perform setval('learnings.id_seq', substr(new.id, 3)::bigint);   -- rows imported from the sheet keep their ids
  end if;
  return new;
end $$;

create or replace function learnings.after_write() returns trigger language plpgsql as $$
begin
  insert into learnings.history (id, action, approved_by, before, after)
  values (new.id, tg_op, nullif(current_setting('learnings.approved_by', true), ''),
          case when tg_op = 'UPDATE' then to_jsonb(old) - 'fts' end, to_jsonb(new) - 'fts');
  return new;
end $$;

drop trigger if exists learnings_before on learnings.learnings;
create trigger learnings_before before insert or update on learnings.learnings
  for each row execute function learnings.before_write();
drop trigger if exists learnings_after on learnings.learnings;
create trigger learnings_after after insert or update on learnings.learnings
  for each row execute function learnings.after_write();

-- log_learning: a new lesson, always 'proposed' with seen 1. Returns its id.
create or replace function learnings.log_learning(
  p_kind text, p_area text, p_rule text, p_what_happened text, p_expected text,
  p_project text default null, p_lesson_type text default null, p_why text default null,
  p_tags text default null, p_severity text default null, p_sensitive boolean default true,
  p_confidence text default null, p_review_by date default null, p_date date default current_date
) returns text language sql as $$
  insert into learnings.learnings (date, kind, area, project, lesson_type, rule, what_happened, expected, why,
                                   tags, severity, status, seen, source, sensitive, confidence, review_by)
  values (coalesce(p_date, current_date), p_kind, p_area, nullif(p_project, ''), nullif(p_lesson_type, ''), p_rule,
          p_what_happened, p_expected, nullif(p_why, ''), nullif(p_tags, ''), nullif(p_severity, ''), 'proposed', 1,
          'chat', coalesce(p_sensitive, true), nullif(p_confidence, ''), p_review_by)
  returning id;
$$;

-- Words are matched loosely: a row matching any of them is a candidate, the best matches first.
create or replace function learnings.any_words(p_words text) returns tsquery language sql immutable as $$
  select case when coalesce(trim(p_words), '') = '' then null
         else websearch_to_tsquery('english', regexp_replace(trim(p_words), '\s+', ' or ', 'g')) end;
$$;

-- similar_rows: rows that may be the same lesson: the same area and project, or sharing words, in
-- any area. A sensitive row shows its rule, never its details.
create or replace function learnings.similar_rows(p_area text, p_project text default null, p_words text default null)
returns table (id text, area text, project text, kind text, lesson_type text, status text, seen integer, rule text, tags text)
language sql stable as $$
  select l.id, l.area, l.project, l.kind, l.lesson_type, l.status, l.seen,
         l.rule, case when l.sensitive then null else l.tags end
  from learnings.learnings l
  where l.status <> 'retired'
    and ((l.area = p_area and coalesce(l.project, '') = coalesce(p_project, ''))
         or coalesce(l.fts @@ learnings.any_words(p_words), false))
  order by coalesce(ts_rank_cd(l.fts, learnings.any_words(p_words)), 0) desc, l.seen desc
  limit 5;
$$;

-- mark_seen: the same lesson happened again.
create or replace function learnings.mark_seen(p_id text) returns integer language plpgsql as $$
declare n integer;
begin
  update learnings.learnings set seen = seen + 1 where id = p_id returning seen into n;
  if n is null then raise exception 'there is no row %', p_id; end if;
  return n;
end $$;

-- find_rules: accepted rules. It returns the rule, never the details, so a sensitive row's rule
-- (written to name no one) is served too. A project filter keeps rows with no project (they apply
-- everywhere). Words, if given, rank the rows that match any of them; otherwise the most seen come
-- first. At most 10.
create or replace function learnings.find_rules(
  p_project text default null, p_area text default null, p_words text default null, p_limit integer default 5
) returns table (id text, date date, kind text, area text, project text, lesson_type text, rule text, seen integer)
language sql stable as $$
  select l.id, l.date, l.kind, l.area, l.project, l.lesson_type, l.rule, l.seen
  from learnings.learnings l
  where l.status = 'accepted'
    and (p_project is null or l.project = p_project or l.project is null)
    and (p_area is null or l.area = p_area)
    and (learnings.any_words(p_words) is null or l.fts @@ learnings.any_words(p_words))
  order by coalesce(ts_rank_cd(l.fts, learnings.any_words(p_words)), 0) desc, l.seen desc, l.date desc
  limit least(greatest(coalesce(p_limit, 5), 1), 10);
$$;

-- review_queue: every proposed row, and accepted rows past their review_by date.
create or replace function learnings.review_queue()
returns table (id text, date date, kind text, area text, project text, lesson_type text, rule text,
               what_happened text, seen integer, status text, sensitive boolean, review_by date)
language sql stable as $$
  select l.id, l.date, l.kind, l.area, l.project, l.lesson_type, l.rule, l.what_happened, l.seen, l.status,
         l.sensitive, l.review_by
  from learnings.learnings l
  where l.status = 'proposed' or (l.status = 'accepted' and l.review_by <= current_date)
  order by l.status, l.date;
$$;

-- set_status: the person's decision on a row. Needs their name, which is kept in the history.
create or replace function learnings.set_status(p_id text, p_status text, p_approved_by text, p_merged_into text default null)
returns text language plpgsql as $$
begin
  if coalesce(trim(p_approved_by), '') = '' then
    raise exception 'set_status needs the name of the person who approved it';
  end if;
  perform set_config('learnings.approved_by', trim(p_approved_by), true);
  update learnings.learnings set status = p_status, merged_into = nullif(p_merged_into, '') where id = p_id;
  if not found then raise exception 'there is no row %', p_id; end if;
  return p_status;
end $$;

-- The log is private: the public API gets nothing.
alter table learnings.learnings enable row level security;
alter table learnings.lists enable row level security;
alter table learnings.history enable row level security;
do $$ begin
  if exists (select 1 from pg_roles where rolname = 'anon') then
    revoke all on schema learnings from anon, authenticated;
    revoke all on all functions in schema learnings from anon, authenticated, public;
  end if;
end $$;

-- Starting lists. Add your own projects with:
--   insert into learnings.lists values ('project', 'my-project', 'What it is');
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
