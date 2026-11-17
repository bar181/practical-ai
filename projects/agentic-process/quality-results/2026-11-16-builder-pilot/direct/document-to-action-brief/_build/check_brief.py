"""check_brief.py BRIEF DOCUMENT [KEY]: check an action brief against the document it came from.

1. Quotes. Every run of words inside quotation marks in the brief must appear word for word in
   the document. Curly and straight quotation marks, spacing, line breaks and Markdown bold are
   ignored; case, numbers and every other character count.
2. Acceptance (only with KEY, a JSON answer key). Each expected item must be on one row of the
   section the key names, and nothing the key forbids may appear in a section.

Only the part of BRIEF between <!-- brief:start --> and <!-- brief:end --> is read when those
markers are present, so a worked example can be checked in place.
This is for testing the instructions. It does not replace the person's check against the page.
Exit code 1 if any check fails. Standard library only.
"""
import json, re, sys

SECTIONS = {"facts": "key facts", "obligations": "what you must do", "dates": "dates", "questions": "open questions"}


def norm(s):
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = s.replace("**", "").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def brief_text(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"<!-- brief:start -->(.*?)<!-- brief:end -->", text, re.S)
    return m.group(1) if m else text


def sections(text):
    """Map each known section to its rows (table rows or list lines)."""
    out, current = {k: [] for k in SECTIONS}, None
    for line in text.splitlines():
        h = re.match(r"^#{1,3}\s+(.+)$", line)
        if h:
            title = h.group(1).strip().lower()
            current = next((k for k, v in SECTIONS.items() if title.startswith(v)), None)
            continue
        if current and line.strip() and not re.match(r"^\|\s*-", line) and not line.lower().startswith("| #"):
            out[current].append(norm(line).lower())
    return out


def quotes(text):
    body = re.sub(r"<!--.*?-->", "", norm(text), flags=re.S)
    return [q.strip().rstrip(",;:") for q in re.findall(r'"([^"]{3,})"', body)]


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    brief, doc = brief_text(argv[1]), norm(open(argv[2], encoding="utf-8").read())
    failures = 0
    qs = quotes(brief)
    missing = [q for q in qs if q not in doc]
    print(f"Quotes: {len(qs)} found, {len(qs) - len(missing)} match the document word for word, {len(missing)} do not")
    for q in missing:
        print(f'  NOT IN DOCUMENT: "{q}"')
    failures += len(missing)
    if len(argv) > 3:
        key, secs = json.load(open(argv[3], encoding="utf-8")), sections(brief)
        everything = [r for rows in secs.values() for r in rows]
        for item in key.get("expect", []):
            rows = everything if item["section"] == "any" else secs[item["section"]]
            ok = any(all(a.lower() in r for a in item.get("all", [])) and
                     (not item.get("any") or any(a.lower() in r for a in item["any"])) for r in rows)
            print(f"  {'pass' if ok else 'FAIL'}  {item['id']}: {item['test']}")
            failures += not ok
        for item in key.get("forbid", []):
            hit = [r for r in secs[item["section"]] if any(a.lower() in r for a in item["any"])]
            print(f"  {'FAIL' if hit else 'pass'}  {item['id']}: {item['test']}")
            failures += bool(hit)
    print("RESULT:", "pass" if not failures else f"{failures} problem(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
