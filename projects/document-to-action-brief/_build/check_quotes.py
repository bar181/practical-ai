"""check_quotes.py: checks that every quote in a brief appears word for word in its document.

This is the person's Ctrl+F check, done by a script, for testing the tool. It takes every run of
text in double quotes ("..." or curly quotes) with four or more words, and looks for it in the
document. Spaces and line breaks count as one space, because a search in a browser treats them
alike. Nothing else is forgiven: case, punctuation and spelling must match. The brief's own
closing line, "I will ... by ...", is skipped.

Run: python3 check_quotes.py BRIEF.md DOCUMENT.txt
Prints each quote that is not found, then a count. Exits 1 if any quote is missing.
"""
import re
import sys


def squash(text):
    return re.sub(r"\s+", " ", text).strip()


def quotes(brief):
    found = re.findall(r'"([^"\n]+)"|“([^”\n]+)”', brief)
    out = []
    for a, b in found:
        q = squash(a or b)
        if len(q.split()) >= 4 and not q.startswith("I will"):  # the brief's own "I will ... by ..." line
            out.append(q)
    return out


def main():
    brief = open(sys.argv[1], encoding="utf-8").read().split("=====NOTE=====")[0]
    doc = squash(open(sys.argv[2], encoding="utf-8").read())
    qs = quotes(brief)
    missing = [q for q in qs if q not in doc]
    for q in missing:
        print("NOT FOUND:", q)
    print(f"{len(qs) - len(missing)} of {len(qs)} quotes found word for word")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
