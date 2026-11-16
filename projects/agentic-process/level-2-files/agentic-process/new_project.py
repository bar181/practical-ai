#!/usr/bin/env python3
"""Make a new project folder from the template beside this script. Works in any repository.

    python3 new_project.py my-tool "My tool"              makes projects/my-tool/ if there is a projects/ folder here,
                                                          otherwise my-tool/ in the current folder
    python3 new_project.py my-tool "My tool" tools        makes tools/my-tool/

Copies template/ and replaces {{SLUG}} and {{TITLE}} in every text file. The new folder carries its own
checks in _build/checks/, so it needs nothing else from this repository. Check it with:

    python3 <the new folder>/_build/checks/gates.py <the new folder>
"""
import os, re, shutil, sys

if len(sys.argv) < 3:
    sys.exit(__doc__)
slug, title = sys.argv[1], sys.argv[2]
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
    sys.exit("The slug is lower-case words joined by hyphens, such as meeting-notes.")
here = os.path.dirname(os.path.abspath(__file__))
parent = sys.argv[3] if len(sys.argv) > 3 else ("projects" if os.path.isdir("projects") else ".")
dest = os.path.abspath(os.path.join(parent, slug))
if os.path.exists(dest):
    sys.exit(f"{dest} already exists. Nothing was changed.")
shutil.copytree(os.path.join(here, "template"), dest, ignore=shutil.ignore_patterns("__pycache__"))
for folder, _, files in os.walk(dest):
    for name in files:
        if not name.endswith((".md", ".json", ".txt")):
            continue                                              # the checks are copied as they are
        path = os.path.join(folder, name)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        with open(path, "w", encoding="utf-8") as f:
            f.write(text.replace("{{SLUG}}", slug).replace("{{TITLE}}", title))
blanks = set()                                                    # every template line with a blank, for check_filled.py
for name in ("README.md", "AGENTS.md", os.path.join("base", "plan.md"), os.path.join("base", "AI-INSTRUCTIONS.md")):
    path = os.path.join(dest, name)
    if os.path.exists(path):
        blanks |= {l.strip() for l in open(path, encoding="utf-8") if "[" in l and l.strip()}
with open(os.path.join(dest, "_build", "checks", "blanks.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(blanks)) + "\n")
rel = os.path.relpath(dest)
print(f"Made {rel}")
print(f"Check it now:  python3 {rel}/_build/checks/gates.py {rel}")
print("Next: fill in base/plan.md, then write the README's first screen.")
