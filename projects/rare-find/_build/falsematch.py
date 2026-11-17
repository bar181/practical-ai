"""falsematch.py: finds real English words that the typo rule would wrongly count as an answer.

It plays every word in a system dictionary (hunspell en_US) against every pack, with the stop list
switched off, and writes the words that typo-match a different answer to stopwords.json. build.py
then bakes that list into the game: those words are never typo-matched (an exact answer still counts).
Run after changing packs.json or the matching rule:
  python3 projects/rare-find/_build/build.py && python3 projects/rare-find/_build/falsematch.py && python3 projects/rare-find/_build/build.py
"""
import json, os, re
from playwright.sync_api import sync_playwright
here = os.path.dirname(os.path.abspath(__file__))
DIC = "/usr/share/hunspell/en_US.dic"
AFF = "/usr/share/hunspell/en_US.aff"
# Expand every stem with the dictionary's own suffix rules, so "talking", "hustling" and "calms" are
# real words too, not only the bare stems.
sfx = {}
for line in open(AFF, encoding="latin-1"):
    f = line.split()
    if len(f) >= 5 and f[0] == "SFX":
        strip = "" if f[2] == "0" else f[2]; add = "" if f[3] == "0" else f[3].split("/")[0]
        sfx.setdefault(f[1], []).append((strip, add, re.compile(f[4] + "$")))
words = set()
for l in open(DIC, encoding="latin-1").read().split("\n")[1:]:
    stem, _, flags = l.strip().partition("/")
    if not stem.isalpha(): continue
    stem = stem.lower(); forms = {stem}
    for fl in flags:
        for strip, add, cond in sfx.get(fl, []):
            if cond.search(stem) and stem.endswith(strip):
                forms.add(stem[:len(stem) - len(strip)] + add)
    words |= {w for w in forms if len(w) >= 5}
words = sorted(words)
print(len(words), "dictionary words and forms")
html = os.path.join(os.path.dirname(here), "base", "game.html")
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(); pg.goto("file://" + html); pg.wait_for_timeout(300)
    hits = pg.evaluate("""(words)=>{ const R=window.__rf; R.STOP.clear(); const out=new Set();
      for(const p of R.packs){ const forms=new Set(); for(const e of [...p.ranked,...p.gems,...p.good]) for(const f of [e.a,...(e.aka||[])]) forms.add(R.norm(f));
        const keys=new Set([...forms].map(f=>f[0]+"|"+f.length));
        for(const w of words){ const n=R.norm(w); if(forms.has(n)) continue; let ok=false; for(let d=-1;d<=1;d++) if(keys.has(n[0]+"|"+(n.length+d))) ok=true; if(!ok) continue;
          const m=R.match(p,w); if(m.how==="typo") out.add(n); } }
      return [...out].sort(); }""", words)
    b.close()
json.dump(hits, open(os.path.join(here, "stopwords.json"), "w"))
print(len(hits), "real words blocked from typo matching, for example:", hits[:12])
