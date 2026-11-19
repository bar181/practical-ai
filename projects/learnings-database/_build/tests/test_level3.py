"""test_level3.py: checks the level 3 database and MCP server against a real Postgres with pgvector.

Needs a local Postgres 15+ with the vector extension, and a superuser login to create a scratch
database (LT_ADMIN_URL, default postgresql://lt_admin:lt_admin_pw@127.0.0.1:5432/postgres).
It creates the database lt_test, applies schema.sql twice, imports the template sheet, then
checks what an agent's role and the owner's role can and cannot do, through SQL and through the
MCP server's tools, both called directly and over the MCP protocol (stdio).
Run: python3 projects/learnings-database/_build/tests/test_level3.py
"""
import asyncio, csv, importlib.util, json, os, subprocess, sys

import psycopg

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(here))
L3 = os.path.join(root, "level-3-files")
ADMIN = os.environ.get("LT_ADMIN_URL", "postgresql://lt_admin:lt_admin_pw@127.0.0.1:5432/postgres")
TEST = ADMIN.rsplit("/", 1)[0] + "/lt_test"
AGENT = "postgresql://lt_agent:lt_agent_pw@127.0.0.1:5432/lt_test"
OWNER = "postgresql://lt_owner:lt_owner_pw@127.0.0.1:5432/lt_test"
passed = failed = 0


def check(name, ok, detail=""):
    global passed, failed
    if ok: passed += 1; print("PASS", name)
    else: failed += 1; print("FAIL", name, "::", str(detail)[:300])


def q(url, sql, args=()):
    with psycopg.connect(url, autocommit=True) as c, c.cursor() as cur:
        cur.execute(sql, args)
        return cur.fetchall() if cur.description else None


def err(url, sql, args=()):
    try: q(url, sql, args); return ""
    except Exception as e: return str(e).splitlines()[0]


# 1. a scratch database, the schema twice, and two logins
with psycopg.connect(ADMIN, autocommit=True) as c:
    c.execute("drop database if exists lt_test with (force)"); c.execute("create database lt_test")
for i in (1, 2):
    r = subprocess.run(["psql", TEST, "-v", "ON_ERROR_STOP=1", "-q", "-f", os.path.join(L3, "supabase", "schema.sql")],
                       capture_output=True, text=True)
    check(f"schema.sql applies cleanly (run {i})", r.returncode == 0, r.stderr)
q(TEST, """do $$ begin
  if not exists (select 1 from pg_roles where rolname='lt_agent') then create role lt_agent login password 'lt_agent_pw'; end if;
  if not exists (select 1 from pg_roles where rolname='lt_owner') then create role lt_owner login password 'lt_owner_pw'; end if;
end $$; grant learnings_agent to lt_agent; grant learnings_owner to lt_owner; grant connect on database lt_test to lt_agent, lt_owner;""")

# 2. import the template sheet as the owner
csv_path = os.path.join(root, "base", "template", "learnings.csv")
rows = list(csv.DictReader(open(csv_path)))
env = dict(os.environ, LEARNINGS_DATABASE_URL=OWNER)
r = subprocess.run([sys.executable, os.path.join(L3, "import_csv.py"), csv_path], capture_output=True, text=True, env=env)
check("import: the 12 template rows load unchanged", "loaded 12, skipped 0, not loaded 0" in r.stdout, r.stdout + r.stderr)
r = subprocess.run([sys.executable, os.path.join(L3, "import_csv.py"), csv_path], capture_output=True, text=True, env=env)
check("import: running it again changes nothing", "loaded 0, skipped 12" in r.stdout, r.stdout)
same = q(OWNER, "select id, area, status, seen, sensitive from learnings.learnings order by id")
want = sorted((x["id"], x["area"], x["status"], int(x["seen"]), x["sensitive"] == "yes") for x in rows)
check("import: ids, areas, statuses, counts and sensitive flags match the sheet", sorted(same) == want, same)

# 3. what an agent can and cannot do
check("agent: cannot read the table itself", "permission denied" in err(AGENT, "select * from learnings.learnings"))
served = {r[0] for r in q(AGENT, "select id from learnings.served_rules")}
expect = {x["id"] for x in rows if x["status"] == "accepted" and x["sensitive"] == "no"}
check("agent: the served view holds exactly the accepted, non-sensitive rows", served == expect, (served, expect))
check("agent: cannot insert into the table directly", "permission denied" in err(AGENT,
      "insert into learnings.learnings (kind, area, rule, status) values ('error','sales','When testing, do nothing at all.','accepted')"))
nid = q(AGENT, "select learnings.log_learning(p_kind=>'error', p_area=>'sales', p_rule=>'When a quote goes out, attach the terms.', p_sensitive=>false)")[0][0]
st = q(OWNER, "select status, seen, source from learnings.learnings where id=%s", (nid,))[0]
check("agent: a logged row is 'proposed', seen 1, source agent, and its id follows the imported ones",
      nid == "L-13" and st == ("proposed", 1, "agent"), (nid, st))
check("agent: cannot set a status", "permission denied" in err(AGENT, "select learnings.set_status('L-13','accepted','me')"))
check("agent: cannot open the review queue", "permission denied" in err(AGENT, "select * from learnings.review_queue()"))
check("agent: cannot read the history", "permission denied" in err(AGENT, "select * from learnings.history"))
check("lists: an area not on the list is refused", "not on the Areas list" in err(AGENT,
      "select learnings.log_learning(p_kind=>'error', p_area=>'astrology', p_rule=>'When testing, refuse this row.')"))
check("lists: a new area is accepted when written new:<word>", not err(AGENT,
      "select learnings.log_learning(p_kind=>'error', p_area=>'new:permits', p_rule=>'When repainting a sign, ask the council about a permit.')"))

# 4. the owner's decisions, with a name, kept in history
check("owner: set_status refuses without the approver's name", "needs the name" in err(OWNER, "select learnings.set_status('L-9','accepted','')"))
q(OWNER, "select learnings.set_status('L-9','accepted','Owner (test)')")
h = q(OWNER, "select approved_by, before->>'status', after->>'status' from learnings.history where id='L-9' and action='UPDATE' order by at desc limit 1")
check("owner: an accepted row's change is in history with who approved it", h == [("Owner (test)", "proposed", "accepted")], h)
check("owner: a merge needs merged_into", "needs merged_into" in err(OWNER, "select learnings.set_status('L-10','merged','Owner (test)')"))
q(OWNER, "select learnings.set_status('L-7','accepted','Owner (test)')")  # L-7 is sensitive
served = {r[0] for r in q(AGENT, "select id from learnings.find_rules(p_limit=>10)")}
check("serving: a sensitive row is never served, even once accepted", "L-7" not in served and "L-9" in served, served)

# 5. finding
got = [r[0] for r in q(AGENT, "select id from learnings.find_rules(p_project=>'company-website', p_for_work=>'price update')")]
check("find: project company-website returns its accepted rules and those with no project", set(got) == {"L-5", "L-11"}, got)
n = q(OWNER, "select count(*) from learnings.served_log where for_work='price update'")[0][0]
check("find: each served rule is recorded, so reuse can be measured", n == 2, n)
got = [r[0] for r in q(AGENT, "select id from learnings.find_rules(p_words=>'price table on request')")]
check("find: words rank the matching rule first", got[:1] == ["L-9"], got)
got = q(AGENT, "select id from learnings.find_rules(p_limit=>50)")
check("find: never more than 10 rules", len(got) <= 10, len(got))
sim = q(AGENT, "select id, rule from learnings.similar_rows('customers', 'kitchen-renovations', 'customer or delay')")
check("search before write: a similar sensitive row shows its id but not its text",
      any(i == "L-7" and r.startswith("(sensitive") for i, r in sim), sim)

# 6. the MCP server's tools, called directly as the agent and the owner
spec = importlib.util.spec_from_file_location("lt_server", os.path.join(L3, "mcp-server", "server.py"))
os.environ["LEARNINGS_DATABASE_URL"] = AGENT; os.environ["LEARNINGS_EMBED_URL"] = "test:hash"
srv = importlib.util.module_from_spec(spec); spec.loader.exec_module(srv)
res = srv.log_learning(kind="error", area="working-with-ai", rule="When an AI builds a price table, check items priced on request are listed.",
                       what_happened="The January price table lost the items priced on request.", expected="Every item listed.",
                       project="december-price-list", sensitive=False)
check("mcp log_learning: a likely repeat is returned for a decision, not written",
      res.get("written") is False and any(s["id"] == "L-9" for s in res.get("similar", [])), res)
res2 = srv.mark_seen("L-9")
check("mcp mark_seen: raises seen on the repeat", res2.get("seen") == 2, res2)
res3 = srv.log_learning(kind="worked", area="customers", rule="When a new customer signs, send the two-minute welcome video.",
                        what_happened="Login questions stopped after the welcome video.", expected="The written guide would do.",
                        force_new=True, sensitive=False)
check("mcp log_learning: force_new writes a proposed row with an embedding", res3.get("written") and res3.get("status") == "proposed", res3)
emb = q(OWNER, "select embedding is not null from learnings.learnings where id=%s", (res3.get("id"),))
check("mcp log_learning: the embedding is stored when an embedding service is set", emb == [(True,)], emb)
res4 = srv.review_queue()
check("mcp review_queue: refused on the agent's connection, with a clear reason", res4.get("ok") is False and "owner" in res4.get("error", ""), res4)
os.environ["LEARNINGS_DATABASE_URL"] = OWNER
res5 = srv.set_status(id=res3["id"], status="accepted", approved_by="Owner (test)")
check("mcp set_status: the owner accepts a row, naming the approver", res5.get("status") == "accepted", res5)
os.environ["LEARNINGS_DATABASE_URL"] = AGENT
res6 = srv.find_learnings(words="welcome video for new customers")
check("mcp find_learnings: finds the accepted rule and gives a block to paste",
      res6.get("rules") and res6["rules"][0]["id"] == res3["id"] and res6["paste"].startswith("Rules from the log"), res6)
emb_only = srv.find_learnings(words="")  # plain filters
check("mcp find_learnings: with no words, rules come back most seen first", emb_only.get("ok") and emb_only["count"] >= 1, emb_only)
lists = srv.find_learnings(list_values=True)
check("mcp find_learnings: list_values returns the Areas list", any(x["value"] == "working-with-ai" for x in lists.get("lists", [])), lists)

# 7. the same server over the MCP protocol (stdio), as a client would use it
async def over_stdio():
    from mcp import ClientSession
    from mcp.client.stdio import stdio_client, StdioServerParameters
    p = StdioServerParameters(command=sys.executable, args=[os.path.join(L3, "mcp-server", "server.py")],
                              env={**os.environ, "LEARNINGS_DATABASE_URL": AGENT})
    async with stdio_client(p) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            tools = sorted(t.name for t in (await s.list_tools()).tools)
            out = await s.call_tool("find_learnings", {"project": "company-website"})
            text = "".join(getattr(c, "text", "") for c in out.content)
            return tools, text
try:
    tools, text = asyncio.run(over_stdio())
    check("protocol: the server lists its five tools", tools == ["find_learnings", "log_learning", "mark_seen", "review_queue", "set_status"], tools)
    check("protocol: a client call returns the rules", "L-5" in text and "Rules from the log" in text, text[:300])
except Exception as e:
    check("protocol: the server runs over stdio", False, repr(e))

print(f"\n{passed}/{passed + failed} checks passed")
sys.exit(1 if failed else 0)
