"""fill_fixture.py PROJECT: fill every blank a new project starts with, as a builder would, so a gate can
check that a correctly filled project passes all of its own checks. Used only by level-3-files/gates.json."""
import re, sys, os
BLANK = re.compile(r"(?<!!)\[(?!needs:)(?!x\])(?! \])([^\]\[`]{4,400})\](?![(\[:])", re.S)
root = sys.argv[1]
for name in ("README.md", "AGENTS.md", "base/plan.md", "base/AI-INSTRUCTIONS.md"):
    p = os.path.join(root, name); s = open(p, encoding="utf-8").read()
    s = BLANK.sub("Filled in by the builder", s)
    open(p, "w", encoding="utf-8").write(s)
