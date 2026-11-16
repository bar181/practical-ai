"""check_filled.py FILE...: no blanks left over from a template.

A blank is text in square brackets that is not a link, such as "[The hook: one sentence a stranger
would stop for.]". A visible gap the author left on purpose, "[needs: ...]", is not a blank.
Text inside code fences is skipped. Exit code 1 if any file still has a blank.
"""
import re, sys

if len(sys.argv) < 2:
    sys.exit(__doc__)
BLANK = re.compile(r"(?<!!)\[(?!needs:)(?!x\])(?! \])([^\]\[`\n]{4,})\](?![(\[:])")
found = 0
for path in sys.argv[1:]:
    try:
        text = open(path, encoding="utf-8").read()
    except FileNotFoundError:
        print(f"{path}: missing"); found += 1; continue
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    for n, line in enumerate(text.splitlines(), 1):
        for m in BLANK.finditer(line):
            found += 1
            if found <= 20:
                print(f"{path}:{n}: still a blank: [{m.group(1)[:60]}]")
print(f"{found} blank(s) left" if found else "no blanks left")
sys.exit(1 if found else 0)
