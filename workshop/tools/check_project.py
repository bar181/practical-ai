"""check_project.py PROJECT_FOLDER: does this folder follow the repository's layout?

The showcase layout, used by everything in projects/. base/ is enough to try the tool.
  README.md        the hook, a "Try it" quick start, the North Star and a Status section
  AGENTS.md        instructions for AI agents
  LICENSE
  base/            the few files a beginner needs: six things at most, counting an optional examples/ folder of worked examples (files only)
  level-2-files/   optional. What an advanced user adds, with a README.md
  level-3-files/   optional. Connections for agents, with a README.md
  _build/          optional. What the project is built from
Nothing else sits beside them.

The earlier layout, still used by drafts/project-method and its scaffold: README.md, AGENTS.md, gates.json,
base/ with a README.md, and level-1/ to level-3/ folders each with a README.md.
Exit code 1 if any rule is broken.
"""
import json, os, re, sys

if len(sys.argv) < 2:
    sys.exit(__doc__)
root = os.path.abspath(sys.argv[1]); problems = []; name = os.path.basename(root)
exists = lambda *p: os.path.exists(os.path.join(root, *p))
text = open(os.path.join(root, "README.md"), encoding="utf-8").read() if exists("README.md") else ""
folders = sorted(int(m.group(1)) for d in os.listdir(root) if (m := re.fullmatch(r"level-(\d+)", d)))
if folders or exists("gates.json"):                                  # the earlier layout
    for need in ("README.md", "AGENTS.md", "gates.json", "base/README.md", "level-1/README.md"):
        if not exists(need): problems.append(f"missing {need}")
    for mark in ("**Think of it as**", "**North Star:**", "## Use it today", "## How it is laid out", "## Status"):
        if mark not in text: problems.append(f"README.md has no '{mark}'")
    if folders != list(range(1, len(folders) + 1)) or len(folders) > 3: problems.append(f"levels must be numbered 1 to 3 in order. Found {folders}")
    for n in folders:
        if not exists(f"level-{n}", "README.md"): problems.append(f"level-{n} has no README.md")
    if exists("gates.json"):
        try:
            for g in json.load(open(os.path.join(root, "gates.json"), encoding="utf-8")):
                if not all(g.get(k) for k in ("name", "proves", "run")): problems.append(f"gate {g.get('name', '?')} needs a name, what it proves and a command")
        except ValueError as e:
            problems.append(f"gates.json does not parse: {e}")
else:                                                                # the showcase layout
    for need in ("README.md", "AGENTS.md", "LICENSE", "base"):
        if not exists(need): problems.append(f"missing {need}")
    for mark, why in (("**North Star:**", "one sentence saying what success is"), ("## Status", "who has and has not tried it")):
        if mark not in text: problems.append(f"README.md has no '{mark}' ({why})")
    if not re.search(r"^## Try it", text, re.M): problems.append("README.md has no section starting '## Try it' (the quick start)")
    first = [h for h in re.findall(r"^## (.+)$", text, re.M)]
    if first and not first[0].startswith("Try it"): problems.append(f"the quick start must be the first section of the README. Found '{first[0]}' first")
    if exists("base"):
        inside = os.listdir(os.path.join(root, "base"))
        if not inside: problems.append("base/ is empty")
        if len(inside) > 6: problems.append(f"base/ holds {len(inside)} things. Six at most: it is what a beginner opens")
        sub = [d for d in inside if os.path.isdir(os.path.join(root, "base", d)) and d != "examples"]
        if sub: problems.append("base/ may hold one folder, examples/. Found: " + ", ".join(sorted(sub)))
        if exists("base", "examples"):
            ex = os.listdir(os.path.join(root, "base", "examples"))
            if not ex: problems.append("base/examples/ is empty")
            if any(os.path.isdir(os.path.join(root, "base", "examples", d)) for d in ex): problems.append("base/examples/ should hold files only")
    for lv in ("level-2-files", "level-3-files"):
        if exists(lv) and not exists(lv, "README.md"): problems.append(f"{lv}/ has no README.md")
    if exists("level-3-files") and not exists("level-2-files"): problems.append("level-3-files/ without level-2-files/")
    allowed = {"README.md", "AGENTS.md", "LICENSE", "base", "level-2-files", "level-3-files", "_build"}
    extra = sorted(d for d in os.listdir(root) if d not in allowed and not d.startswith("."))
    if extra: problems.append("found beside base/, and not part of the layout: " + ", ".join(extra))
if problems:
    print(f"{name}: {len(problems)} problem(s)"); [print("  " + p) for p in problems]; sys.exit(1)
print(f"{name}: layout ok")
