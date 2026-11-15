"""check_project.py PROJECT_FOLDER: does this folder follow the repository's layout for a tool?

The layout, in one rule: base/ holds everything, and a level holds only what it adds.
  README.md      the front door for people: an analogy, a North Star, how to use it today, the layout, the status
  AGENTS.md      the front door for agents
  gates.json     the checks that must pass, each with what it proves
  base/          with a README.md
  level-1/       with a README.md. Levels 2 and 3 are optional and must be numbered in order
Exit code 1 if any rule is broken.
"""
import json, os, re, sys

if len(sys.argv) < 2:
    sys.exit(__doc__)
root = sys.argv[1]; problems = []
MAX_LEVELS = 3                                                       # more than three levels means the tool should be split
OLD = ("level-demo", "level-simple", "level-working", "level-automated", "student-projects")   # the earlier layout
exists = lambda *p: os.path.exists(os.path.join(root, *p))
for need in ("README.md", "AGENTS.md", "gates.json", "base/README.md", "level-1/README.md"):
    if not exists(need): problems.append(f"missing {need}")
if exists("README.md"):
    text = open(os.path.join(root, "README.md"), encoding="utf-8").read()
    for mark, why in (("**Think of it as**", "an analogy near the top"), ("**North Star:**", "one sentence saying what success is"),
                      ("## Use it today", "what a person can do with it now"), ("## How it is laid out", "the folders, explained"), ("## Status", "who has and has not tried it")):
        if mark not in text: problems.append(f"README.md has no '{mark}' ({why})")
if exists("gates.json"):
    try:
        gates = json.load(open(os.path.join(root, "gates.json"), encoding="utf-8"))
        if not gates: problems.append("gates.json lists no gates")
        for g in gates:
            if not all(g.get(k) for k in ("name", "proves", "run")): problems.append(f"gate {g.get('name', '?')} needs a name, what it proves and a command")
    except ValueError as e:
        problems.append(f"gates.json does not parse: {e}")
levels = sorted(int(m.group(1)) for d in os.listdir(root) if (m := re.fullmatch(r"level-(\d+)", d)))
if levels != list(range(1, len(levels) + 1)): problems.append(f"levels must be numbered 1, 2, 3 in order. Found {levels}")
if len(levels) > MAX_LEVELS: problems.append(f"{len(levels)} levels. Use {MAX_LEVELS} or fewer")
for n in levels:
    if not exists(f"level-{n}", "README.md"): problems.append(f"level-{n} has no README.md")
for d in OLD:
    if exists(d): problems.append(f"'{d}' is from the earlier layout. Move its contents into base/ or a numbered level")
print(f"{os.path.basename(os.path.abspath(root))}: " + ("layout ok" if not problems else f"{len(problems)} layout problems"))
for p in problems: print("  PROBLEM", p)
sys.exit(1 if problems else 0)
