#!/usr/bin/env python3
"""Make a new project folder from the template.

    python3 projects/agentic-process/level-2-files/new_project.py my-tool "My tool"   from the repository root: makes projects/my-tool/
    python3 new_project.py my-tool "My tool" /some/dir  makes /some/dir/my-tool/

Copies template/ and replaces {{SLUG}} and {{TITLE}} in every file.
"""
import os, re, shutil, sys

if len(sys.argv) < 3:
    sys.exit(__doc__)
slug, title = sys.argv[1], sys.argv[2]
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
    sys.exit("The slug is lower-case words joined by hyphens, such as meeting-notes.")
here = os.path.dirname(os.path.abspath(__file__))
parent = sys.argv[3] if len(sys.argv) > 3 else os.path.normpath(os.path.join(here, "..", ".."))
dest = os.path.join(parent, slug)
if os.path.exists(dest):
    sys.exit(f"{dest} already exists. Nothing was changed.")
shutil.copytree(os.path.join(here, "template"), dest)
for folder, _, files in os.walk(dest):
    for name in files:
        path = os.path.join(folder, name)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        with open(path, "w", encoding="utf-8") as f:
            f.write(text.replace("{{SLUG}}", slug).replace("{{TITLE}}", title))
print(f"Made {dest}")
print("Next: fill in base/plan.md, then write the README's first screen.")
