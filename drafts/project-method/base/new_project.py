"""new_project.py SLUG "Title" [DESTINATION]: start a tool from the scaffold.

Copies base/scaffold/ to drafts/SLUG/ (or to DESTINATION/SLUG/) and replaces {{SLUG}} and {{TITLE}}.
Refuses to write over a folder that exists. SLUG is lowercase letters, numbers and hyphens.
"""
import os, re, shutil, sys

if len(sys.argv) < 3:
    sys.exit(__doc__)
slug, title = sys.argv[1], sys.argv[2]
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
    sys.exit("SLUG must be lowercase letters, numbers and hyphens, such as weekly-brief")
here = os.path.dirname(os.path.abspath(__file__))
drafts = sys.argv[3] if len(sys.argv) > 3 else os.path.normpath(os.path.join(here, "..", ".."))
dest = os.path.join(drafts, slug)
if os.path.exists(dest):
    sys.exit(f"{dest} already exists. Nothing was changed.")
shutil.copytree(os.path.join(here, "scaffold"), dest)
for folder, _, files in os.walk(dest):
    for name in files:
        path = os.path.join(folder, name)
        text = open(path, encoding="utf-8").read().replace("{{SLUG}}", slug).replace("{{TITLE}}", title)
        open(path, "w", encoding="utf-8").write(text)
print(f"Created {dest}. Next: write the purpose page in docs/purpose.md and get it approved (stage 1).")
