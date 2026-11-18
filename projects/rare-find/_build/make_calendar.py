"""make_calendar.py: extends calendar.json, which fixes the five prompts for each date.

Days already in the calendar never change, because people may have played them. New days use
prompts the calendar has not used yet, five different topics a day where possible, until every
prompt in packs.json has had a day. After the calendar ends the game deals from the whole bank.
Run after adding packs: python3 _build/make_calendar.py && python3 _build/build.py
"""
import json, os, random, datetime

here = os.path.dirname(os.path.abspath(__file__))
packs = json.load(open(os.path.join(here, "packs.json"), encoding="utf-8"))["packs"]
path = os.path.join(here, "calendar.json")
# The first day is the one already played on 17 November 2026, kept exactly as it was dealt.
cal = json.load(open(path)) if os.path.exists(path) else {"start": "2026-11-17", "days": [["bird", "breakfast", "superhero", "sport", "animated-film"]]}
ids = {p["id"] for p in packs}
for d in cal["days"]:
    assert all(i in ids for i in d), f"calendar names a missing pack: {d}"
used = {i for d in cal["days"] for i in d}
cat = {p["id"]: p["cat"] for p in packs}
rng = random.Random(len(cal["days"]) * 7919 + len(packs))
todo = [p["id"] for p in packs if p["id"] not in used]
rng.shuffle(todo)
added = 0
while len(todo) >= 5:
    day = []
    for i in list(todo):  # five different topics where possible
        if cat[i] not in {cat[x] for x in day}:
            day.append(i); todo.remove(i)
        if len(day) == 5: break
    while len(day) < 5: day.append(todo.pop(0))
    cal["days"].append(day); added += 1
json.dump(cal, open(path, "w"), indent=1)
start = datetime.date.fromisoformat(cal["start"])
end = start + datetime.timedelta(days=len(cal["days"]) - 1)
print(f"calendar: {len(cal['days'])} days, {cal['start']} to {end}; added {added}; {len(todo)} prompts wait for the next batch")
