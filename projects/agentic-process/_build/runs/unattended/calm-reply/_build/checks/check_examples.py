"""check_examples.py [FOLDER]: every worked example in base/examples/ has the shape the instructions promise.

For each example: the answer block has WHAT THEY WANT, REPLY DRAFT and the four-part NOTE; the reply body
(after the greeting, before "Kind regards,") is 120 words or fewer and has no exclamation mark.
Prints the word counts. Exit code 1 if any rule is broken.
"""
import glob, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
LIMIT, bad, files = 120, [], sorted(glob.glob(os.path.join(root, "base", "examples", "*.md")))
if not files:
    bad.append("no worked examples in base/examples/")
for path in files:
    name = os.path.basename(path)
    blocks = re.findall(r"```\n(.*?)```", open(path, encoding="utf-8").read(), flags=re.S)
    answer = next((b for b in blocks if "REPLY DRAFT:" in b), None)
    if answer is None:
        bad.append(f"{name}: no answer block with 'REPLY DRAFT:'"); continue
    for mark in ("WHAT THEY WANT:", "REPLY DRAFT:", "\nNOTE\n", "Chose:", "Assumed:", "Missing:", "Check before sharing:"):
        if mark not in answer:
            bad.append(f"{name}: answer has no '{mark.strip()}'")
    reply = answer.split("REPLY DRAFT:", 1)[1].split("\nNOTE\n", 1)[0]
    lines = [l for l in reply.strip().splitlines() if l.strip()]
    if not lines or "Kind regards," not in lines:
        bad.append(f"{name}: reply has no 'Kind regards,' sign-off"); continue
    body = lines[1:lines.index("Kind regards,")]                  # greeting is the first line
    words = len(" ".join(body).split())
    if "!" in reply:
        bad.append(f"{name}: reply has an exclamation mark")
    if words > LIMIT:
        bad.append(f"{name}: reply body is {words} words, more than {LIMIT}")
    print(f"{name}: reply body {words} words (limit {LIMIT})")
print(f"{len(files)} worked examples, {len(bad)} problems")
for b in bad:
    print("  PROBLEM", b)
sys.exit(1 if bad else 0)
