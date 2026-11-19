"""import_csv.py: loads a level 1 or level 2 learnings sheet into the level 3 database, unchanged.

Export your sheet's Learnings tab as CSV (File > Download > CSV in Google Sheets; Save As > CSV
in Excel), then run, with an owner connection:
  LEARNINGS_DATABASE_URL=postgresql://... python3 import_csv.py learnings.csv
Rows keep their id, status, seen and source. A row whose id is already in the database is
skipped and reported, so running it twice changes nothing. Any value that breaks the schema's
rules (an area not on the list, a bad status) stops that row with the reason, and the rest load.
Projects in the sheet that are not on the Projects list are added to it.
"""
import csv, os, re, sys

import psycopg

COLUMNS = ["id", "date", "kind", "area", "project", "lesson_type", "rule", "what_happened", "expected", "why",
           "tags", "severity", "status", "seen", "source", "sensitive", "confidence", "review_by"]


def main(path: str, url: str) -> int:
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8-sig")))
    missing = [c for c in COLUMNS[:16] if rows and c not in rows[0]]
    if missing:
        print("The sheet is missing columns:", ", ".join(missing)); return 1
    loaded = skipped = failed = 0
    with psycopg.connect(url, autocommit=True) as c, c.cursor() as cur:
        for p in sorted({r["project"].strip() for r in rows if r.get("project", "").strip() and not r["project"].startswith("new:")}):
            cur.execute("insert into learnings.lists (list, value, means) values ('project', %s, 'Imported') on conflict do nothing", (p,))
        for r in rows:
            v = {k: (r.get(k) or "").strip() for k in COLUMNS}
            cur.execute("select 1 from learnings.learnings where id = %s", (v["id"],))
            if cur.fetchone():
                skipped += 1; print(f"{v['id']}: already in the database, skipped"); continue
            try:
                with c.transaction():
                    cur.execute("""insert into learnings.learnings (id, date, kind, area, project, lesson_type, rule, what_happened,
                                     expected, why, tags, severity, status, seen, source, sensitive, confidence, review_by)
                                   values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                (v["id"], v["date"] or None, v["kind"], v["area"], v["project"] or None, v["lesson_type"] or None,
                                 v["rule"], v["what_happened"] or None, v["expected"] or None, v["why"] or None,
                                 [t.strip() for t in v["tags"].split(";") if t.strip()], v["severity"] or None,
                                 v["status"] or "proposed", int(v["seen"] or 1), v["source"] or "import",
                                 v["sensitive"].lower() != "no", v["confidence"] or None, v["review_by"] or None))
                loaded += 1
            except Exception as e:
                failed += 1; print(f"{v['id']}: not loaded: {str(e).splitlines()[0]}")
        nums = [int(m.group(1)) for r in rows if (m := re.fullmatch(r"L-(\d+)", (r.get("id") or "").strip()))]
        if nums:  # new rows written later continue after the highest imported number
            cur.execute("select setval('learnings.id_seq', greatest(%s, (select last_value from learnings.id_seq)))", (max(nums),))
    print(f"loaded {loaded}, skipped {skipped}, not loaded {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) != 2 or not os.environ.get("LEARNINGS_DATABASE_URL"):
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1], os.environ["LEARNINGS_DATABASE_URL"]))
