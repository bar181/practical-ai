"""check_project.py PROJECT_FOLDER: does this folder follow the repository's layout for a tool?

The layout, in one rule: base/ holds everything, and the rest explains how to use it.
  README.md        the front door for people: an analogy, a North Star, how to use it today, the layout, the status
  base/            everything the tool is made of, with a README.md
  AGENTS.md        the front door for agents, in base/ or beside the README
  gates.json       the checks that must pass, each with what it proves, in base/ or beside the README
  a guide for each level, numbered in order, three at most. Either a file beside the README named
  level-1-NAME.md (the current form), or a folder level-1/ with a README.md (the earlier form).
A project in the current form also has a LICENSE and a north-star.html.
Exit code 1 if any rule is broken.
"""
import glob, json, os, re, sys

if len(sys.argv) < 2:
    sys.exit(__doc__)
root = os.path.abspath(sys.argv[1]); problems = []
MAX_LEVELS = 3                                                       # more than three levels means the tool should be split
OLD = ("level-demo", "level-simple", "level-working", "level-automated", "student-projects")   # the first layout
exists = lambda *p: os.path.exists(os.path.join(root, *p))
either = lambda name: exists("base", name) or exists(name)
for need in ("README.md", "base/README.md"):
    if not exists(need): problems.append(f"missing {need}")
for need in ("AGENTS.md", "gates.json"):
    if not either(need): problems.append(f"missing {need}, in base/ or beside the README")
if exists("README.md"):
    text = open(os.path.join(root, "README.md"), encoding="utf-8").read()
    for mark, why in (("**Think of it as**", "an analogy"), ("**North Star:**", "one sentence saying what success is"),
                      ("## Use it today", "what a person can do with it now"), ("## How it is laid out", "the folders, explained"), ("## Status", "who has and has not tried it")):
        if mark not in text: problems.append(f"README.md has no '{mark}' ({why})")
gates_file = os.path.join(root, "base", "gates.json") if exists("base", "gates.json") else os.path.join(root, "gates.json")
if os.path.exists(gates_file):
    try:
        gates = json.load(open(gates_file, encoding="utf-8"))
        if not gates: problems.append("gates.json lists no gates")
        for g in gates:
            if not all(g.get(k) for k in ("name", "proves", "run")): problems.append(f"gate {g.get('name', '?')} needs a name, what it proves and a command")
    except ValueError as e:
        problems.append(f"gates.json does not parse: {e}")
folders = sorted(int(m.group(1)) for d in os.listdir(root) if (m := re.fullmatch(r"level-(\d+)", d)))
files = sorted(int(m.group(1)) for d in os.listdir(root) if (m := re.fullmatch(r"level-(\d+)-[a-z-]+\.md", d)))
if folders and files: problems.append("level guides are both files and folders. Use one form")
levels = files or folders
if not levels: problems.append("no level guide. Add level-1-NAME.md beside the README")
elif levels != list(range(1, len(levels) + 1)): problems.append(f"levels must be numbered 1, 2, 3 in order. Found {levels}")
if len(levels) > MAX_LEVELS: problems.append(f"{len(levels)} levels. Use {MAX_LEVELS} or fewer")
for n in folders:
    if not exists(f"level-{n}", "README.md"): problems.append(f"level-{n} has no README.md")
if files:
    for need in ("LICENSE", "north-star.html"):
        if not exists(need): problems.append(f"missing {need}")
    allowed = {"README.md", "LICENSE", "north-star.html", "base"} | {os.path.basename(f) for f in glob.glob(os.path.join(root, "level-*-*.md"))}
    extra = sorted(d for d in os.listdir(root) if d not in allowed and not d.startswith("."))
    if extra: problems.append("the project folder should hold only the landing page, the licence, the North Star page, the level guides and base/. Also found: " + ", ".join(extra))
for d in OLD:
    if exists(d): problems.append(f"'{d}' is from the first layout. Move its contents into base/")
name = os.path.basename(root)
if problems:
    print(f"{name}: {len(problems)} problem(s)"); [print("  " + p) for p in problems]; sys.exit(1)
print(f"{name}: layout ok")
