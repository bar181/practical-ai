"""check_quotes.py REPLY INPUT: is every quoted phrase in the reply's Sources table word for word in the input?

Used to grade test runs. Takes every "..." phrase in the 'The exact words' column (a row like
'Claim: "..." Page says: "..."' gives two phrases) and looks for it in the input text, ignoring
case, spacing and curly quotes; "..." splits a phrase into parts that must each appear. Exit code 1 if any phrase is not found.
"""
import re, sys

def tidy(s):
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"')):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()

reply, source = (open(p, encoding="utf-8").read() for p in sys.argv[1:3])
text, header, phrases = tidy(source), None, []
for line in reply.splitlines():
    if not line.strip().startswith("|"):
        header = None; continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if header is None:
        header = [c.lower() for c in cells] if any("exact words" in c.lower() for c in cells) else None
        continue
    if set("".join(cells)) <= set("-: "): continue
    i = next(i for i, h in enumerate(header) if "exact words" in h)
    phrases += [(cells[0], p) for p in re.findall(r'"([^"]+)"', tidy(cells[i]))]
# "..." marks words left out: each part must appear, as in level-2-files/check_sources.py
missing = [(n, p) for n, p in phrases
           if any(part.strip(" .") not in text for part in re.split(r"\.\.\.|\u2026", tidy(p)) if len(part.strip(" .")) > 3)]
print(f"{len(phrases)} quoted phrases, {len(phrases) - len(missing)} word for word in the input")
for n, p in missing: print(f"  NOT FOUND [{n}]: {p}")
sys.exit(1 if missing else 0)
