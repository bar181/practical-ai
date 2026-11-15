"""check_skills.py [SKILLS_FOLDER]: check every skill against the published authoring rules.

Rules checked (source: the Agent Skills authoring best practices, read 2026-11-15):
  name         lowercase letters, numbers and hyphens, 64 characters or fewer, matches its folder
  description  present, 1,024 characters or fewer, no angle brackets, says when to use it, not written as "I" or "you"
  body         under 500 lines
  references   every linked file exists and is linked straight from SKILL.md (one level deep)
  long files   a reference file over 100 lines has a contents list near the top
  evals        reported, not failed: how many test cases the skill carries
Exit code 1 if any rule is broken.
"""
import glob, os, re, sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)                                                # so piping the report into head does not raise

root = sys.argv[1] if len(sys.argv) > 1 else "skills"
MAX_BODY, MAX_DESC, MAX_NAME, TOC_FROM = 500, 1024, 64, 100          # the limits the authoring guide gives
fails, rows = [], []
for skill in sorted(glob.glob(os.path.join(root, "*", "SKILL.md"))):
    folder = os.path.dirname(skill); name_dir = os.path.basename(folder)
    text = open(skill, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        fails.append(f"{name_dir}: no frontmatter"); continue
    front, body = m.group(1), m.group(2)
    get = lambda k: (re.search(rf"^{k}:\s*(.*)$", front, re.M) or [None, ""])[1].strip().strip('"')
    name, desc = get("name"), get("description")
    problems = []
    if not re.fullmatch(r"[a-z0-9-]{1,%d}" % MAX_NAME, name): problems.append("name must be lowercase letters, numbers and hyphens")
    if name != name_dir: problems.append(f"name '{name}' does not match folder '{name_dir}'")
    if not desc: problems.append("no description")
    if len(desc) > MAX_DESC: problems.append(f"description is {len(desc)} characters, over {MAX_DESC}")
    if "<" in desc or ">" in desc: problems.append("description contains angle brackets")
    if not re.search(r"\b[Uu]se (when|for|this|it)\b", desc): problems.append("description does not say when to use the skill")
    if re.match(r"^(I|You|We)\b", desc): problems.append("description should be in the third person")
    lines = body.count("\n") + 1
    if lines > MAX_BODY: problems.append(f"body is {lines} lines, over {MAX_BODY}")
    linked = set(re.findall(r"\]\(((?:references|assets|scripts|evals)/[^)#\s]+)", body)) | set(re.findall(r"`((?:references|assets|scripts|evals)/[^`\s]+)`", body))
    for rel in sorted(linked):
        if not os.path.exists(os.path.join(folder, rel)): problems.append(f"links to missing file {rel}")
    for ref in glob.glob(os.path.join(folder, "references", "*.md")):
        rel = os.path.relpath(ref, folder).replace(os.sep, "/")
        if rel not in linked: problems.append(f"{rel} is not linked from SKILL.md")
        rtext = open(ref, encoding="utf-8").read()
        if rtext.count("\n") > TOC_FROM and not re.search(r"^## Contents", rtext[:1500], re.M): problems.append(f"{rel} is over {TOC_FROM} lines and has no '## Contents' list")
        if re.search(r"\]\((?!https?:)[^)]*references/", rtext): problems.append(f"{rel} links on to another reference file (keep it one level deep)")
    evals = 0
    for ef in glob.glob(os.path.join(folder, "evals", "*.json")):
        data = __import__("json").load(open(ef, encoding="utf-8")); evals += len(data.get("evals", [])) if isinstance(data, dict) else len(data)
    rows.append((name_dir, lines, len(desc), evals, "ok" if not problems else "FAIL"))
    fails += [f"{name_dir}: {p}" for p in problems]
print(f"{'skill':26}{'lines':>6}{'desc':>6}{'evals':>6}  result")
for r in rows: print(f"{r[0]:26}{r[1]:>6}{r[2]:>6}{r[3]:>6}  {r[4]}")
for f in fails: print("  FAIL", f)
sys.exit(1 if fails else 0)
