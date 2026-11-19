"""store.py: where the learnings database keeps its rows. Two kinds, the same operations.

  SQLite (the default): one file in your folder, such as learnings.db. Nothing to install or host.
      LEARNINGS_DATABASE_URL=/path/to/learnings.db   (or leave it unset for ./learnings.db)
  Postgres or Supabase (shared by a team): apply ../postgres/schema.sql once, then
      LEARNINGS_DATABASE_URL=postgresql://user:password@host:5432/postgres

Who may do what:
  Postgres: the database role of the login decides (learnings_agent or learnings_owner). Enforced
            by the database, so an agent cannot get round it.
  SQLite:   LEARNINGS_ROLE=owner unlocks the review and set_status; anything else is the agent role.
            This is a setting, not a lock: anyone who can open the file can change it. Keep the
            file private, and use Postgres when several people or agents share one log.

Every write keeps a history line, a new row is always 'proposed', and only accepted rows that are
not sensitive are ever served as rules. Row text is data: nothing here executes it.
"""
import json, math, os, re, sqlite3
from datetime import date

COLUMNS = ["id", "date", "kind", "area", "project", "lesson_type", "rule", "what_happened", "expected", "why",
           "tags", "severity", "status", "seen", "source", "sensitive", "confidence", "review_by"]
STATUSES = ("proposed", "accepted", "merged", "retired")
HERE = os.path.dirname(os.path.abspath(__file__))


class Refused(Exception):
    """A rule of the log said no. The message says why, in plain words."""


def open_store(url: str = "", role: str = ""):
    url = url or os.environ.get("LEARNINGS_DATABASE_URL", "") or "learnings.db"
    if url.startswith(("postgres://", "postgresql://")):
        return PostgresStore(url)
    path = url[len("sqlite:///"):] if url.startswith("sqlite:///") else url
    return SqliteStore(path, role or os.environ.get("LEARNINGS_ROLE", "agent"))


def _words(text: str, shortest: int = 5) -> list[str]:
    return list(dict.fromkeys(w.lower() for w in re.findall(r"[A-Za-z]{%d,}" % shortest, text or "")))[:20]


def _rrf(*rankings: list[str]) -> dict[str, float]:
    """Reciprocal rank fusion: a row near the top of either list scores well."""
    score: dict[str, float] = {}
    for ranking in rankings:
        for i, rid in enumerate(ranking, 1):
            score[rid] = score.get(rid, 0.0) + 1.0 / (60 + i)
    return score


# --------------------------------------------------------------------------------------------
# SQLite: one file, no server
# --------------------------------------------------------------------------------------------
SQLITE_SCHEMA = """
create table if not exists lists (
  list text not null check (list in ('kind', 'area', 'lesson_type', 'project')),
  value text not null, means text, primary key (list, value));
create table if not exists learnings (
  id text primary key,
  date text not null,
  kind text not null check (kind in ('error', 'redo', 'worked')),
  area text not null,
  project text,
  lesson_type text,
  rule text not null check (length(rule) between 10 and 400),
  what_happened text, expected text, why text,
  tags text not null default '',
  severity text check (severity in ('low', 'medium', 'high')),
  status text not null default 'proposed' check (status in ('proposed', 'accepted', 'merged', 'retired')),
  merged_into text references learnings (id),
  seen integer not null default 1 check (seen >= 1),
  source text not null default 'agent' check (source in ('chat', 'review', 'person', 'agent', 'import')),
  sensitive integer not null default 1,
  confidence text check (confidence in ('high', 'medium', 'low')),
  review_by text,
  created_at text not null default (datetime('now')),
  updated_at text not null default (datetime('now')),
  embedding text);
create virtual table if not exists learnings_fts using fts5(id unindexed, body, tokenize = 'porter');
create table if not exists history (
  at text not null default (datetime('now')), id text not null, action text not null,
  by_role text not null, approved_by text, before text, after text);
create table if not exists served_log (
  at text not null default (datetime('now')), id text not null, for_work text, by_role text not null);
"""


class SqliteStore:
    kind = "sqlite"

    def __init__(self, path: str, role: str = "agent"):
        self.path, self.role = path, ("owner" if role == "owner" else "agent")
        folder = os.path.dirname(os.path.abspath(path))
        os.makedirs(folder, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("pragma foreign_keys = on")
        self.db.executescript(SQLITE_SCHEMA)
        if not self.db.execute("select 1 from lists limit 1").fetchone():
            self._seed_lists()

    # ---- helpers
    def _seed_lists(self):
        L = json.load(open(os.path.join(HERE, "lists.json")))
        with self.db:
            for key, name in (("kinds", "kind"), ("areas", "area"), ("lesson_types", "lesson_type")):
                for item in L[key]:
                    self.db.execute("insert or ignore into lists values (?, ?, ?)", (name, item["value"], item["means"]))

    def _owner(self, what: str):
        if self.role != "owner":
            raise Refused(f"{what} is for the log's owner. Start this connection with LEARNINGS_ROLE=owner "
                          "on the owner's own computer; an agent's connection may only log, mark seen and find.")

    def _row(self, rid: str):
        r = self.db.execute("select * from learnings where id = ?", (rid,)).fetchone()
        if not r:
            raise Refused(f"There is no row {rid}.")
        return r

    def _check(self, v: dict):
        on = lambda lst, val: self.db.execute("select 1 from lists where list = ? and value = ?", (lst, val)).fetchone()
        if not v.get("area") or (not v["area"].startswith("new:") and not on("area", v["area"])):
            raise Refused(f"area {v.get('area')!r} is not on the Areas list (a new one is written new:<word>).")
        lt = v.get("lesson_type")
        if lt and not lt.startswith("new:") and not on("lesson_type", lt):
            raise Refused(f"lesson type {lt!r} is not on the Lesson types list (a new one is written new:<word>).")
        if v.get("status") == "merged" and not v.get("merged_into"):
            raise Refused("A merged row needs merged_into: the id it was merged into.")

    def _history(self, rid: str, action: str, before, after, approved_by=None):
        clean = lambda r: None if r is None else json.dumps({k: r[k] for k in r.keys() if k != "embedding"})
        self.db.execute("insert into history (id, action, by_role, approved_by, before, after) values (?, ?, ?, ?, ?, ?)",
                        (rid, action, self.role, approved_by, clean(before), clean(after)))

    def _index(self, rid: str):
        r = self._row(rid)
        body = " ".join(filter(None, [r["rule"], r["what_happened"], r["expected"], r["why"], r["tags"].replace(";", " ")]))
        self.db.execute("delete from learnings_fts where id = ?", (rid,))
        self.db.execute("insert into learnings_fts (id, body) values (?, ?)", (rid, body))

    def _next_id(self) -> str:
        nums = [int(m.group(1)) for (i,) in self.db.execute("select id from learnings") if (m := re.fullmatch(r"L-(\d+)", i))]
        return f"L-{max(nums, default=0) + 1}"

    def _match(self, words: list[str]) -> list[str]:
        """Row ids whose text matches any of the words, best first (BM25)."""
        if not words:
            return []
        q = " OR ".join('"%s"' % w.replace('"', "") for w in words)
        return [r[0] for r in self.db.execute(
            "select id from learnings_fts where learnings_fts match ? order by bm25(learnings_fts)", (q,))]

    # ---- operations
    def lists(self) -> list[dict]:
        return [dict(r) for r in self.db.execute("select list, value, means from lists order by list, value")]

    def similar(self, area: str, project: str | None, rule: str) -> list[dict]:
        hits = self._match(_words(rule))
        rows = self.db.execute("select id, status, seen, rule, sensitive, area, project from learnings where status <> 'retired'").fetchall()
        same = [r for r in rows if r["area"] == area and (r["project"] or "") == (project or "")]
        by_id = {r["id"]: r for r in rows}
        out, seen_ids = [], set()
        for rid, why in [(h, "shares words") for h in hits] + [(r["id"], "same area and project") for r in
                                                                  sorted(same, key=lambda r: -r["seen"])]:
            if rid in by_id and rid not in seen_ids:
                r = by_id[rid]; seen_ids.add(rid)
                out.append({"id": rid, "status": r["status"], "seen": r["seen"], "match": why,
                            "rule": "(sensitive row: ask the owner)" if r["sensitive"] else r["rule"]})
        return out[:5]

    def log(self, *, kind, area, rule, project=None, lesson_type=None, what_happened=None, expected=None, why=None,
            tags=None, severity=None, sensitive=True, confidence=None, review_by=None, happened_on=None,
            source="agent", embedding=None) -> str:
        v = dict(kind=kind, area=area, lesson_type=lesson_type or None, status="proposed")
        self._check(v)
        rid = self._next_id()
        with self.db:
            try:
                self.db.execute(
                    """insert into learnings (id, date, kind, area, project, lesson_type, rule, what_happened, expected, why,
                       tags, severity, status, seen, source, sensitive, confidence, review_by, embedding)
                       values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'proposed', 1, ?, ?, ?, ?, ?)""",
                    (rid, happened_on or date.today().isoformat(), kind, area, project or None, lesson_type or None, rule,
                     what_happened, expected, why or None, ";".join(tags or []), severity or None,
                     source if source in ("chat", "agent") else "agent", 0 if sensitive is False else 1,
                     confidence or None, review_by or None, json.dumps(embedding) if embedding else None))
            except sqlite3.IntegrityError as e:
                raise Refused(f"The row breaks a rule of the log: {e}.")
            self._index(rid)
            self._history(rid, "INSERT", None, self._row(rid))
        return rid

    def mark_seen(self, rid: str) -> int:
        before = self._row(rid)
        with self.db:
            self.db.execute("update learnings set seen = seen + 1, updated_at = datetime('now') where id = ?", (rid,))
            self._history(rid, "UPDATE", before, self._row(rid))
        return self._row(rid)["seen"]

    def find(self, project=None, area=None, kind=None, words=None, embedding=None, limit=5, for_work=None) -> list[dict]:
        sql, args = "select * from learnings where status = 'accepted' and sensitive = 0", []
        if project: sql += " and (project = ? or project is null)"; args.append(project)
        if area: sql += " and area = ?"; args.append(area)
        if kind: sql += " and kind = ?"; args.append(kind)
        base = {r["id"]: r for r in self.db.execute(sql, args)}
        limit = max(1, min(int(limit or 5), 10))
        if not words and not embedding:
            score = {rid: float(r["seen"]) for rid, r in base.items()}
        else:
            kw = [i for i in self._match(_words(words or "", 3)) if i in base]
            sem = []
            if embedding:
                def cos(a, b):
                    d = sum(x * y for x, y in zip(a, b)); n = math.sqrt(sum(x * x for x in a) * sum(y * y for y in b))
                    return d / n if n else 0.0
                vecs = [(rid, json.loads(r["embedding"])) for rid, r in base.items() if r["embedding"]]
                sem = [rid for rid, _ in sorted(vecs, key=lambda t: -cos(embedding, t[1]))][:50]
            score = _rrf(kw, sem)
        chosen = sorted(score, key=lambda i: (score[i], base[i]["seen"], base[i]["date"]), reverse=True)[:limit]
        with self.db:
            for rid in chosen:
                self.db.execute("insert into served_log (id, for_work, by_role) values (?, ?, ?)", (rid, for_work, self.role))
        return [{"id": i, "rule": base[i]["rule"], "area": base[i]["area"], "project": base[i]["project"],
                 "lesson_type": base[i]["lesson_type"], "kind": base[i]["kind"], "seen": base[i]["seen"],
                 "score": round(score[i], 4)} for i in chosen]

    def review_queue(self) -> list[dict]:
        self._owner("The weekly review")
        today = date.today().isoformat()
        rows = self.db.execute("""select id, date, kind, area, project, lesson_type, rule, what_happened, why, seen, status,
                                  sensitive, source, review_by from learnings
                                  where status = 'proposed' or (status = 'accepted' and review_by is not null and review_by <= ?)
                                  order by status, date""", (today,))
        return [dict(r) | {"sensitive": bool(r["sensitive"])} for r in rows]

    def set_status(self, rid: str, status: str, approved_by: str, merged_into: str | None = None) -> str:
        self._owner("Changing a row's status")
        if not (approved_by or "").strip():
            raise Refused("set_status needs the name of the person who approved it.")
        if status not in STATUSES:
            raise Refused(f"status must be one of {', '.join(STATUSES)}.")
        before = self._row(rid)
        v = dict(before) | {"status": status, "merged_into": merged_into or None}
        self._check(v)
        if merged_into:
            self._row(merged_into)
        with self.db:
            self.db.execute("update learnings set status = ?, merged_into = ?, updated_at = datetime('now') where id = ?",
                            (status, merged_into or None, rid))
            self._history(rid, "UPDATE", before, self._row(rid), approved_by.strip())
        return status

    def history(self, rid: str | None = None) -> list[dict]:
        self._owner("Reading the history")
        sql = "select at, id, action, by_role, approved_by from history" + (" where id = ?" if rid else "") + " order by rowid"
        return [dict(r) for r in self.db.execute(sql, (rid,) if rid else ())]

    def import_rows(self, rows: list[dict]) -> tuple[int, int, list[str]]:
        self._owner("Importing a sheet")
        loaded, skipped, failed = 0, 0, []
        with self.db:
            for p in sorted({(r.get("project") or "").strip() for r in rows} - {""}):
                if not p.startswith("new:"):
                    self.db.execute("insert or ignore into lists values ('project', ?, 'Imported')", (p,))
        for r in rows:
            v = {k: (r.get(k) or "").strip() for k in COLUMNS}
            if self.db.execute("select 1 from learnings where id = ?", (v["id"],)).fetchone():
                skipped += 1; continue
            try:
                self._check(v | {"lesson_type": v["lesson_type"] or None})
                with self.db:
                    self.db.execute(
                        """insert into learnings (id, date, kind, area, project, lesson_type, rule, what_happened, expected, why,
                           tags, severity, status, seen, source, sensitive, confidence, review_by)
                           values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (v["id"], v["date"] or date.today().isoformat(), v["kind"], v["area"], v["project"] or None,
                         v["lesson_type"] or None, v["rule"], v["what_happened"] or None, v["expected"] or None,
                         v["why"] or None, ";".join(t.strip() for t in v["tags"].split(";") if t.strip()),
                         v["severity"] or None, v["status"] or "proposed", int(v["seen"] or 1), v["source"] or "import",
                         0 if v["sensitive"].lower() == "no" else 1, v["confidence"] or None, v["review_by"] or None))
                    self._index(v["id"])
                    self._history(v["id"], "IMPORT", None, self._row(v["id"]))
                loaded += 1
            except (Refused, sqlite3.Error, ValueError) as e:
                failed.append(f"{v['id']}: not loaded: {e}")
        return loaded, skipped, failed

    def export_rows(self) -> list[dict]:
        self._owner("Exporting the log")
        out = []
        for r in self.db.execute("select * from learnings order by cast(substr(id, 3) as integer), id"):
            d = {k: r[k] for k in COLUMNS}
            d["sensitive"] = "yes" if r["sensitive"] else "no"
            out.append({k: ("" if d[k] is None else d[k]) for k in COLUMNS})
        return out


# --------------------------------------------------------------------------------------------
# Postgres or Supabase: shared, with the rules enforced by the database (../postgres/schema.sql)
# --------------------------------------------------------------------------------------------
class PostgresStore:
    kind = "postgres"

    def __init__(self, url: str):
        import psycopg  # only needed for a shared database
        self.psycopg, self.url = psycopg, url

    def _q(self, sql, args=(), fetch=True):
        try:
            with self.psycopg.connect(self.url, autocommit=True) as c, c.cursor() as cur:
                cur.execute(sql, args)
                if not fetch:
                    return None
                cols = [d.name for d in cur.description]
                return [{k: (v.isoformat() if isinstance(v, date) else v) for k, v in zip(cols, row)} for row in cur.fetchall()]
        except self.psycopg.Error as e:
            msg = str(e).split("\n")[0]
            if "permission denied" in msg:
                msg += ". This connection's database role may not do this: only the owner's connection can."
            raise Refused(msg)

    @staticmethod
    def _vec(embedding):
        return "[" + ",".join(f"{x:.6f}" for x in embedding) + "]" if embedding else None

    def lists(self):
        return self._q("select list, value, means from learnings.lists order by list, value")

    def similar(self, area, project, rule):
        words = " or ".join(_words(rule))[:300] or None
        return self._q("select * from learnings.similar_rows(%s, %s, %s)", (area, project or None, words))

    def log(self, *, kind, area, rule, project=None, lesson_type=None, what_happened=None, expected=None, why=None,
            tags=None, severity=None, sensitive=True, confidence=None, review_by=None, happened_on=None,
            source="agent", embedding=None):
        r = self._q("""select learnings.log_learning(p_kind => %s, p_area => %s, p_rule => %s, p_project => %s,
                         p_lesson_type => %s, p_what_happened => %s, p_expected => %s, p_why => %s, p_tags => %s,
                         p_severity => %s, p_sensitive => %s, p_confidence => %s, p_review_by => %s,
                         p_date => coalesce(%s::date, current_date), p_source => %s, p_embedding => %s::vector) as id""",
                    (kind, area, rule, project or None, lesson_type or None, what_happened, expected, why or None,
                     tags or [], severity or None, sensitive is not False, confidence or None, review_by or None,
                     happened_on or None, source, self._vec(embedding)))
        return r[0]["id"]

    def mark_seen(self, rid):
        return self._q("select learnings.mark_seen(%s) as seen", (rid,))[0]["seen"]

    def find(self, project=None, area=None, kind=None, words=None, embedding=None, limit=5, for_work=None):
        return self._q("""select * from learnings.find_rules(p_project => %s, p_area => %s, p_kind => %s, p_words => %s,
                            p_embedding => %s::vector, p_limit => %s, p_for_work => %s)""",
                       (project or None, area or None, kind or None, words or None, self._vec(embedding),
                        max(1, min(int(limit or 5), 10)), for_work or None))

    def review_queue(self):
        return self._q("""select id, date, kind, area, project, lesson_type, rule, what_happened, why, seen, status,
                          sensitive, source, review_by from learnings.review_queue()""")

    def set_status(self, rid, status, approved_by, merged_into=None):
        return self._q("select learnings.set_status(%s, %s, %s, %s) as s", (rid, status, approved_by, merged_into or None))[0]["s"]

    def history(self, rid=None):
        return self._q("select at::text, id, action, by_role, approved_by from learnings.history"
                       + (" where id = %s" if rid else "") + " order by at", (rid,) if rid else ())

    def import_rows(self, rows):
        loaded, skipped, failed = 0, 0, []
        with self.psycopg.connect(self.url, autocommit=True) as c, c.cursor() as cur:
            for p in sorted({(r.get("project") or "").strip() for r in rows} - {""}):
                if not p.startswith("new:"):
                    cur.execute("insert into learnings.lists (list, value, means) values ('project', %s, 'Imported') "
                                "on conflict do nothing", (p,))
            for r in rows:
                v = {k: (r.get(k) or "").strip() for k in COLUMNS}
                cur.execute("select 1 from learnings.learnings where id = %s", (v["id"],))
                if cur.fetchone():
                    skipped += 1; continue
                try:
                    with c.transaction():
                        cur.execute("""insert into learnings.learnings (id, date, kind, area, project, lesson_type, rule,
                                         what_happened, expected, why, tags, severity, status, seen, source, sensitive,
                                         confidence, review_by)
                                       values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                    (v["id"], v["date"] or None, v["kind"], v["area"], v["project"] or None,
                                     v["lesson_type"] or None, v["rule"], v["what_happened"] or None, v["expected"] or None,
                                     v["why"] or None, [t.strip() for t in v["tags"].split(";") if t.strip()],
                                     v["severity"] or None, v["status"] or "proposed", int(v["seen"] or 1),
                                     v["source"] or "import", v["sensitive"].lower() != "no", v["confidence"] or None,
                                     v["review_by"] or None))
                    loaded += 1
                except Exception as e:
                    failed.append(f"{v['id']}: not loaded: {str(e).splitlines()[0]}")
            nums = [int(m.group(1)) for r in rows if (m := re.fullmatch(r"L-(\d+)", (r.get("id") or "").strip()))]
            if nums:
                cur.execute("select setval('learnings.id_seq', greatest(%s, (select last_value from learnings.id_seq)))",
                            (max(nums),))
        return loaded, skipped, failed

    def export_rows(self):
        rows = self._q("""select id, date::text, kind, area, project, lesson_type, rule, what_happened, expected, why,
                          array_to_string(tags, ';') as tags, severity, status, seen, source,
                          case when sensitive then 'yes' else 'no' end as sensitive, confidence, review_by::text
                          from learnings.learnings order by created_at, id""")
        return [{k: ("" if r[k] is None else r[k]) for k in COLUMNS} for r in rows]
