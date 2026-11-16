"""check_filled.py FILE...: no blanks left over from a template.

Two kinds of blank are found:
  1. Text in square brackets that is not a link, outside code blocks, even across lines, such as
     "[The hook: one sentence a stranger would stop for.]". "[needs: ...]", a gap left on purpose, is fine.
  2. Any line of the template that is still there word for word, inside code blocks too. new_project.py
     writes those lines to _build/checks/blanks.txt when it makes the project. A placeholder the tool's own
     users should fill, such as "[paste your notes]" in a prompt, is fine once the line around it changes.
Exit code 1 if any file still has a blank.
"""
import os, re, sys

if len(sys.argv) < 2:
    sys.exit(__doc__)
BLANK = re.compile(r"(?<!!)\[(?!needs:)(?!x\])(?! \])([^\]\[`]{4,400})\](?![(\[:])", re.S)
here = os.path.dirname(os.path.abspath(__file__))
listed = os.path.join(here, "blanks.txt")
template_lines = set()
if os.path.exists(listed):
    template_lines = {l.strip() for l in open(listed, encoding="utf-8") if l.strip()}
found = 0
def report(msg):
    global found
    found += 1
    if found <= 20: print(msg)
for path in sys.argv[1:]:
    try:
        raw = open(path, encoding="utf-8").read()
    except FileNotFoundError:
        report(f"{path}: missing"); continue
    outside = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), raw, flags=re.S)
    for m in BLANK.finditer(outside):
        line = outside.count("\n", 0, m.start()) + 1
        report(f"{path}:{line}: still a blank: [{' '.join(m.group(1).split())[:60]}]")
    for n, line in enumerate(raw.splitlines(), 1):
        if line.strip() in template_lines and "[" in line and not BLANK.search(outside.splitlines()[n - 1] if n <= len(outside.splitlines()) else ""):
            report(f"{path}:{n}: still the template's line: {line.strip()[:60]}")
print(f"{found} blank(s) left" if found else "no blanks left")
sys.exit(1 if found else 0)
