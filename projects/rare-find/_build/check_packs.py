"""check_packs.py: checks pack files before they join packs.json.

Run: python3 _build/check_packs.py _build/packs-new/a.json [more files]
Checks every pack's shape, the 10th-place points, that no answer form appears twice in a pack,
that no tempting wrong answer is also a right one, and that ids and prompts are new.
"""
import json, os, re, sys, unicodedata

here = os.path.dirname(os.path.abspath(__file__))
CATS = {"General", "Food", "Animals", "Pop culture", "Geography", "Games", "Office", "Sport", "Nature", "Places", "Home", "Hobbies"}

def norm(s):
    s = unicodedata.normalize("NFD", str(s)).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"&", " and ", s)
    s = re.sub(r"^(the|a|an)\s+", "", s.strip())
    return re.sub(r"[^a-z0-9]", "", s)

existing = json.load(open(os.path.join(here, "packs.json"), encoding="utf-8"))["packs"]
seen_ids = {p["id"] for p in existing}
seen_prompts = {norm(p["prompt"]) for p in existing}
errors = 0
for path in sys.argv[1:]:
    packs = json.load(open(path, encoding="utf-8"))["packs"]
    for p in packs:
        where = f"{os.path.basename(path)}:{p.get('id')}"
        def bad(msg):
            global errors
            errors += 1; print("FAIL", where, msg)
        for k in ("id", "prompt", "cat", "top", "ranked", "gems", "good", "wrong"):
            if k not in p: bad("missing " + k)
        if p.get("id") in seen_ids: bad("id already used")
        if norm(p.get("prompt", "")) in seen_prompts: bad("prompt already used")
        seen_ids.add(p.get("id")); seen_prompts.add(norm(p.get("prompt", "")))
        if not re.fullmatch(r"[a-z0-9-]+", str(p.get("id", ""))): bad("id must be lowercase letters, digits and hyphens")
        if p.get("cat") not in CATS: bad(f"cat must be one of {sorted(CATS)}")
        if not (isinstance(p.get("top"), int) and 40 <= p["top"] <= 60 and p["top"] % 5 == 0): bad("top must be 40, 45, 50, 55 or 60")
        if len(p.get("ranked", [])) != 10: bad("ranked needs exactly 10")
        if len(p.get("gems", [])) != 5: bad("gems needs exactly 5")
        if len(p.get("good", [])) < 20: bad("good needs 20 or more")
        if not (2 <= len(p.get("wrong", [])) <= 5): bad("wrong needs 2 to 5")
        forms = {}
        for group in ("ranked", "gems", "good"):
            for e in p.get(group, []):
                if not isinstance(e, dict) or "a" not in e: bad(f"{group} entries must be {{a, aka}}"); continue
                for f in [e["a"]] + list(e.get("aka", [])):
                    n = norm(f)
                    if not n: bad(f"empty answer in {group}"); continue
                    if n in forms and forms[n] != e["a"]: bad(f"'{f}' appears under '{forms[n]}' and '{e['a']}'")
                    forms[n] = e["a"]
        for w in p.get("wrong", []):
            if norm(w) in forms: bad(f"wrong answer '{w}' is also a right answer")
print("all packs pass" if not errors else f"{errors} problems")
sys.exit(1 if errors else 0)
