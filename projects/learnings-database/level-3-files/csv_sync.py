"""csv_sync.py: moves your learnings log between a spreadsheet and the level 3 database.

  python3 csv_sync.py import learnings.csv     load a sheet's rows into the database, unchanged
  python3 csv_sync.py export learnings.csv     write every row back out, to open in any spreadsheet

The database is LEARNINGS_DATABASE_URL: a file such as /path/to/learnings.db (the default is
learnings.db in this folder) or a postgresql:// login with the owner's role. This script acts as the
owner, because it is run by the person at the keyboard.

To get a CSV from your sheet: File > Download > CSV in Google Sheets; Save As > CSV in Excel.
Import keeps each row's id, status, seen and source. A row whose id is already in the database is
skipped, so running it twice changes nothing. A row that breaks a rule (an area not on the list, a
bad status) is reported with the reason, and the rest load. New projects are added to the lists.
Export overwrites the file you name, with the 18 columns of the sheet.
"""
import csv, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "mcp-server"))
from store import COLUMNS, open_store  # noqa: E402


def main(action: str, path: str) -> int:
    st = open_store(os.environ.get("LEARNINGS_DATABASE_URL", ""), role="owner")
    if action == "import":
        rows = list(csv.DictReader(open(path, newline="", encoding="utf-8-sig")))
        missing = [c for c in COLUMNS[:16] if rows and c not in rows[0]]
        if missing:
            print("The sheet is missing columns:", ", ".join(missing)); return 1
        loaded, skipped, failed = st.import_rows(rows)
        for f in failed:
            print(f)
        print(f"loaded {loaded}, skipped {skipped}, not loaded {len(failed)}")
        return 1 if failed else 0
    if action == "export":
        rows = st.export_rows()
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader(); w.writerows(rows)
        print(f"exported {len(rows)} rows to {path}")
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("import", "export"):
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
