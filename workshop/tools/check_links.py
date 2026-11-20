"""check_links.py [FOLDER]: every relative link in every Markdown file must point at something that exists.

Also checks src="..." in Markdown (pictures). Skips links inside code fences, links with a scheme (https:, mailto:),
scaffold folders, installed packages (node_modules), and the copies of instructions inside fresh-run folders (_build/runs/round-N/),
which are inputs to a test and keep the links they had. Exit code 1 if any link is broken.
"""
import glob, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
bad, files = [], 0
for path in glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
    if "/node_modules/" in path.replace(os.sep, "/") or "/scaffold/" in path.replace(os.sep, "/") or re.search(r"/_build/runs/round-\d+/", path.replace(os.sep, "/")):
        continue                                                     # a scaffold's links are right once copied; archived pages keep the links they had
    files += 1
    text = re.sub(r"```.*?```", "", open(path, encoding="utf-8").read(), flags=re.S)
    for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)|\bsrc=\"([^\"#]+)\"", text):
        target = m.group(1) or m.group(3)
        if re.match(r"^[a-z]+:", target):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target))):
            bad.append(f"{os.path.relpath(path, root)} -> {target}")
print(f"{files} Markdown files, {len(bad)} broken links")
for b in bad[:40]:
    print("  BROKEN", b)
sys.exit(1 if bad else 0)
