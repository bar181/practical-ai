"""score_filing.py: scores a run of the filing test against filing-cases.csv.

Input: a predictions CSV with columns case,logged,kind,area,lesson_type,project,confidence,asked
(logged is yes, no or repeat:L-n; asked is yes or no). An area or lesson type counts as right if it is the expected
one or the case's also_ok value. A close call also counts as handled if the assistant asked.
Run: python3 score_filing.py predictions.csv
The definition of done (step 2.4): area right on at least 36 of 40, lesson type on at least 32,
every non-learning declined, every close call asked about or filed right.
"""
import csv, os, sys

here = os.path.dirname(os.path.abspath(__file__))
cases = {r["case"]: r for r in csv.DictReader(open(os.path.join(here, "filing-cases.csv")))}
preds = {r["case"].strip(): {k: (v or "").strip().lower() for k, v in r.items()} for r in csv.DictReader(open(sys.argv[1]))}
area = lt = area_strict = lt_strict = declined = kind = 0
nonl = sum(1 for c in cases.values() if c["is_learning"] == "no")
close_ok = closes = 0
misses = []; repeats = []
for cid, c in cases.items():
    p = preds.get(cid)
    if not p:
        misses.append(f"{cid}: no prediction"); continue
    if p["logged"].startswith("repeat"):  # a repeat is a filing too: it is judged by the row it names
        repeats.append(f"{cid} as {p['logged'][7:]}"); p["logged"] = "yes"
    if c["is_learning"] == "no":
        if p["logged"] == "no":
            declined += 1; area += 1; lt += 1; area_strict += 1; lt_strict += 1
        else:
            misses.append(f"{cid}: logged a non-learning")
        continue
    if p["logged"] != "yes":
        misses.append(f"{cid}: declined a real learning"); continue
    a_ok = p["area"] in {c["area"], c["also_ok_area"]} - {""}
    t_ok = p["lesson_type"] in {c["lesson_type"], c["also_ok_lesson_type"]} - {""}
    area += a_ok; lt += t_ok; area_strict += p["area"] == c["area"]; lt_strict += p["lesson_type"] == c["lesson_type"]
    kind += p["kind"] == c["kind"]
    if not a_ok: misses.append(f"{cid}: area {p['area']} (expected {c['area']}{'/' + c['also_ok_area'] if c['also_ok_area'] else ''})")
    if not t_ok: misses.append(f"{cid}: lesson type {p['lesson_type']} (expected {c['lesson_type']}{'/' + c['also_ok_lesson_type'] if c['also_ok_lesson_type'] else ''})")
    if c["close_call"] == "yes":
        closes += 1; close_ok += (p["asked"] == "yes" or (a_ok and p["area"] == c["area"]))
n = len(cases); learnings = n - nonl
if repeats: print("filed as repeats:", ", ".join(repeats))
print(f"area right: {area}/{n} (strict, first choice only: {area_strict}/{n})   target 36")
print(f"lesson type right: {lt}/{n} (strict: {lt_strict}/{n})   target 32")
print(f"kind right: {kind}/{learnings}")
print(f"non-learnings declined: {declined}/{nonl}   target {nonl}")
print(f"close calls asked about or filed right: {close_ok}/{closes}   target {closes}")
ok = area >= 36 and lt >= 32 and declined == nonl and close_ok == closes
print("PASS" if ok else "FAIL")
for m in misses: print(" -", m)
sys.exit(0 if ok else 1)
