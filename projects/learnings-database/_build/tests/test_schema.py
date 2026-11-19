"""test_schema.py: checks level-3-files/schema.sql on a real Postgres, the way Supabase runs it.

Needs a local Postgres 14+ and a superuser login (LT_ADMIN_URL, default
postgresql://lt_admin:lt_admin_pw@127.0.0.1:5432/postgres). It creates a scratch database, makes the
two roles Supabase has (anon, authenticated) if missing, applies the schema twice, imports the template
sheet as Supabase's CSV import would (plain inserts of every column), then calls each function the
way an assistant does through a Supabase connection: plain SQL.
Run: python3 projects/learnings-database/_build/tests/test_schema.py
"""
import csv, os, subprocess, sys

import psycopg

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(here))
SCHEMA = os.path.join(root, "level-3-files", "schema.sql")
ADMIN = os.environ.get("LT_ADMIN_URL", "postgresql://lt_admin:lt_admin_pw@127.0.0.1:5432/postgres")
DB = ADMIN.rsplit("/", 1)[0] + "/lt_test"
passed = failed = 0


def check(name, ok, detail=""):
    global passed, failed
    if ok: passed += 1; print("PASS", name)
    else: failed += 1; print("FAIL", name, "::", str(detail)[:300])


def q(sql, args=(), url=DB):
    with psycopg.connect(url, autocommit=True) as c, c.cursor() as cur:
        cur.execute(sql, args)
        return cur.fetchall() if cur.description else None


def err(sql, args=(), url=DB):
    try: q(sql, args, url); return ""
    except Exception as e: return str(e).splitlines()[0]


with psycopg.connect(ADMIN, autocommit=True) as c:
    c.execute("drop database if exists lt_test with (force)"); c.execute("create database lt_test")
    c.execute("""do $$ begin
      if not exists (select 1 from pg_roles where rolname = 'anon') then create role anon nologin; end if;
      if not exists (select 1 from pg_roles where rolname = 'authenticated') then create role authenticated nologin; end if;
      if not exists (select 1 from pg_roles where rolname = 'lt_anon') then create role lt_anon login password 'lt_anon_pw'; end if;
    end $$; grant anon to lt_anon""")

# 1. setup: paste the file, twice
for i in (1, 2):
    r = subprocess.run(["psql", DB, "-v", "ON_ERROR_STOP=1", "-q", "-f", SCHEMA], capture_output=True, text=True)
    check(f"setup: schema.sql runs cleanly (run {i})", r.returncode == 0, r.stderr)

# 2. bring in the spreadsheet: every column, as the CSV import does
rows = list(csv.DictReader(open(os.path.join(root, "base", "template", "learnings.csv"))))
cols = list(rows[0].keys())
q("insert into learnings.lists values " + ",".join(["('project', %s, 'invented')"] * len({r['project'] for r in rows} - {''})),
  sorted({r["project"] for r in rows} - {""}))
for r in rows:
    q(f"insert into learnings.learnings ({', '.join(cols)}) values ({', '.join(['%s'] * len(cols))})",
      [None if r[c] == "" else r[c] for c in cols])
back = q("select id, area, status, seen, sensitive, rule from learnings.learnings order by substr(id, 3)::int")
check("import: the 12 sheet rows load with their values", [(b[0], b[1], b[2], str(b[3]), "yes" if b[4] else "no", b[5]) for b in back]
      == [(r["id"], r["area"], r["status"], r["seen"], r["sensitive"], r["rule"]) for r in rows], back[:2])

# 3. logging
sim = q("select id, rule from learnings.similar_rows('working-with-ai', null, 'price table on request')")
check("similar_rows: a likely repeat comes first", sim and sim[0][0] == "L-9", sim)
sim = q("select id, rule from learnings.similar_rows('customers', 'kitchen-renovations', 'job delayed customer')")
check("similar_rows: a sensitive row is found, with its rule", any(s[0] == "L-7" and s[1].startswith("When ") for s in sim), sim)
check("mark_seen: raises seen on a repeat", q("select learnings.mark_seen('L-9')")[0][0] == 2)
new = q("""select learnings.log_learning(p_kind => 'worked', p_area => 'customers',
           p_rule => 'When a new customer signs, send the two-minute welcome video.',
           p_what_happened => 'Login questions stopped after the welcome video.', p_expected => 'The written guide would do.',
           p_tags => 'welcome video; onboarding', p_sensitive => false)""")[0][0]
check("log_learning: an imported sheet's ids continue (the new row is L-13)", new == "L-13", new)
st = q("select status, seen, source, sensitive from learnings.learnings where id = 'L-13'")[0]
check("log_learning: the new row is proposed, seen 1, from chat", st == ("proposed", 1, "chat", False), st)
dflt = q("select learnings.log_learning('error', 'finance', 'When an invoice goes out, confirm the billing email first.', 'x', 'y')")[0][0]
check("log_learning: sensitive is yes unless said otherwise", q("select sensitive from learnings.learnings where id = %s", (dflt,))[0][0] is True)
check("lists: an area not on the list is refused, with the reason",
      "not on the Areas list" in err("select learnings.log_learning('error', 'astrology', 'When testing, refuse this row.', 'x', 'y')"))
permit = q("select learnings.log_learning('error', 'new:permits', 'When repainting a sign, ask about a permit.', 'x', 'y')")[0][0]
check("lists: a new area is accepted as new:<word>", permit and permit.startswith("L-"), permit)

# 4. the person's decisions
check("set_status: refused without the approver's name", "needs the name" in err("select learnings.set_status('L-9', 'accepted', ' ')"))
q("select learnings.set_status('L-9', 'accepted', 'Owner (test)')")
h = q("select approved_by, before->>'status', after->>'status' from learnings.history where id = 'L-9' order by at desc limit 1")[0]
check("set_status: the change is in the history with who approved it", h == ("Owner (test)", "proposed", "accepted"), h)
check("set_status: a merge needs merged_into", "merged_into" in err("select learnings.set_status('L-10', 'merged', 'Owner (test)')"))
q("select learnings.set_status('L-13', 'accepted', 'Owner (test)')")
q("select learnings.set_status('L-7', 'accepted', 'Owner (test)')")
check("history: every insert is recorded", q("select count(*) from learnings.history where action = 'INSERT'")[0][0] == 15)
rq = {r[0] for r in q("select id from learnings.review_queue()")}
check("review_queue: the rows still proposed, and not the accepted ones", {"L-10", dflt, permit} <= rq and "L-9" not in rq, rq)

# 5. finding
allr = {r[0] for r in q("select id from learnings.find_rules(p_limit => 10)")}
check("find_rules: an accepted sensitive row's rule is served", "L-7" in allr and "L-9" in allr, allr)
cols = [d.name for d in psycopg.connect(DB).execute("select * from learnings.find_rules()").description]
check("find_rules: returns rules only, never the details", not {"what_happened", "expected", "why", "tags"} & set(cols), cols)
got = q("select id, project from learnings.find_rules(p_project => 'company-website')")
check("find_rules: a project's rules plus those with no project", {g[0] for g in got} >= {"L-5", "L-11"}
      and all(g[1] in ("company-website", None) for g in got), got)
got = q("select id from learnings.find_rules(p_words => 'welcome video')")
check("find_rules: words find the matching rule", got and got[0][0] == "L-13", got)
check("find_rules: never more than 10", len(q("select * from learnings.find_rules(p_limit => 50)")) <= 10)
check("find_rules: proposed rows are not served", "L-10" not in {r[0] for r in q("select id from learnings.find_rules(p_limit => 10)")})

# 6. privacy: the public API roles get nothing
anon = DB.replace("lt_admin:lt_admin_pw", "lt_anon:lt_anon_pw")
e = err("set role anon; select * from learnings.learnings", url=anon)
check("privacy: Supabase's public role cannot read the log", "permission denied" in e, e)
e = err("set role anon; select learnings.log_learning('error', 'finance', 'When testing, this must fail.', 'x', 'y')", url=anon)
check("privacy: Supabase's public role cannot add a row", "permission denied" in e, e)

print(f"\n{passed}/{passed + failed} checks passed")
sys.exit(1 if failed else 0)
