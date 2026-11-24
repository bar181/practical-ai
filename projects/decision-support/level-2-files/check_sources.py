"""check_sources.py BRIEF.md: does every quoted source in a decision brief still say what it is quoted as saying?

Reads every Markdown table in BRIEF.md whose header has a column named "The exact words". For each
row it takes the quoted words and the first http(s) link in the row, opens the link, and looks for
the words on the page (case, spacing, curly quotes and dashes ignored; "..." splits a quote into
parts that must each appear).

Each row gets one of:
  OK              the page opened and the words are on it
  WORDS NOT FOUND the page opened but the words are not on it (changed page, or a misquote)
  COULD NOT OPEN  an error, a block, a paywall or a timeout. Open it yourself in a browser
  NO LINK         the row has no link (their own figures, or a pasted page)

Exit code 1 if a row the brief marks "Checked" is not OK, so a brief resting on a source that does not
hold up cannot pass. Standard library only. It reads pages; it never sends anything anywhere.

  python3 check_sources.py brief.md
  python3 check_sources.py brief.md --timeout 20 --json results.json
"""
import argparse, html, json, re, sys, urllib.request

UA = "Mozilla/5.0 (compatible; practical-ai-check-sources/1.0; +https://github.com/bar181/practical-ai)"
URL = re.compile(r"https?://[^\s)>\]|\"']+")


def tidy(text):
    """Lower case, straight quotes, plain hyphens, single spaces."""
    text = html.unescape(text)
    for a, b in (("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2013", "-"),
                 ("\u2014", "-"), ("\u00a0", " "), ("\u2026", "...")):
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip().lower()


def page_text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return tidy(raw)


def rows(markdown):
    """Yield (number, words, link, result) for each row of each sources table."""
    header = None
    for line in markdown.splitlines():
        if not line.strip().startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            low = [c.lower() for c in cells]
            if any("exact words" in c for c in low):
                header = low
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        get = lambda name: next((cells[i] for i, h in enumerate(header) if name in h and i < len(cells)), "")
        words = get("exact words").strip().strip('"\u201c\u201d').strip()
        link = URL.search(line)
        yield get("#") or "?", words, link.group(0).rstrip(".,;") if link else "", get("result")


def check(words, url, timeout):
    if not url:
        return "NO LINK", ""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(5_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace")
    except Exception as e:  # any failure to read counts as could not open
        return "COULD NOT OPEN", type(e).__name__ + ": " + str(e)[:120]
    text = page_text(body)
    parts = [p for p in (tidy(x).strip(" .") for x in re.split(r"\.\.\.|…", words)) if len(p) > 3]
    if not parts:
        return "WORDS NOT FOUND", "no words to look for"
    missing = [p for p in parts if p not in text]
    return ("OK", "") if not missing else ("WORDS NOT FOUND", "missing: " + missing[0][:80])


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("brief")
    ap.add_argument("--timeout", type=float, default=15)
    ap.add_argument("--json", help="also write the results to this file")
    a = ap.parse_args()
    found = list(rows(open(a.brief, encoding="utf-8").read()))
    if not found:
        sys.exit("No sources table found: it needs a column headed 'The exact words'.")
    results, failed = [], 0
    for num, words, url, claimed in found:
        status, note = check(words, url, a.timeout)
        bad = "checked" in claimed.lower() and status != "OK"
        failed += bad
        results.append({"number": num, "status": status, "brief_says": claimed, "link": url, "note": note})
        print(f"[{num}] {status:<15} brief says: {claimed or '-':<15} {url or '(no link)'}" + (f"  {note}" if note else "")
              + ("  << marked Checked" if bad else ""))
    ok = sum(r["status"] == "OK" for r in results)
    print(f"\n{len(results)} sources: {ok} OK. {failed} marked Checked but not OK.")
    if a.json:
        json.dump(results, open(a.json, "w", encoding="utf-8"), indent=2)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
