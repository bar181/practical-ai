"""check_site.py: the basic checks a search engine, an AI assistant and a visitor's browser make, in one run.

Fetches a site the way a crawler does (no JavaScript), follows its own links up to a limit, and
writes a findings report in Markdown. It reads public pages only and changes nothing.

  python3 check_site.py https://example.com/              print the report
  python3 check_site.py https://example.com/ --pages 40   check up to 40 pages (default 25)
  python3 check_site.py https://example.com/ --out report.md

Python 3.9 or later, standard library only. Speed, accessibility and security grades come from the
free tools named at the end of the report; this script checks what they do not.
"""
import argparse, html.parser, re, sys, time, urllib.error, urllib.parse, urllib.request
from collections import Counter

AGENT = "practical-ai-website-audit/1.0 (+https://github.com/bar181/practical-ai)"
AI_BOTS = ["OAI-SearchBot", "GPTBot", "ChatGPT-User", "Claude-SearchBot", "ClaudeBot", "Claude-User",
           "Google-Extended", "PerplexityBot"]
SEARCH_BOTS = ["OAI-SearchBot", "Claude-SearchBot", "Claude-User", "PerplexityBot"]  # these affect AI search answers
SECURITY_HEADERS = ["strict-transport-security", "content-security-policy", "x-content-type-options",
                    "referrer-policy", "permissions-policy"]


def fetch(url, method="GET", limit=3_000_000):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": AGENT, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read(limit) if method == "GET" else b""
            return r.status, {k.lower(): v for k, v in r.headers.items()}, body, r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, {k.lower(): v for k, v in e.headers.items()}, b"", url
    except Exception as e:  # DNS, TLS, timeout
        return 0, {"error": str(e)}, b"", url


class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.meta, self.links, self.imgs, self.h1 = "", {}, [], [], 0
        self.canonical, self.lang, self.jsonld, self.text = None, None, 0, []
        self._in, self._skip = None, 0

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "html": self.lang = a.get("lang")
        elif tag == "title": self._in = "title"
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key: self.meta[key] = a.get("content", "")
        elif tag == "link" and "canonical" in a.get("rel", "").lower(): self.canonical = a.get("href")
        elif tag == "a" and a.get("href"): self.links.append(a["href"])
        elif tag == "img": self.imgs.append(a)
        elif tag == "h1": self.h1 += 1
        elif tag == "script":
            self._skip += 1
            if a.get("type") == "application/ld+json": self.jsonld += 1
        elif tag in ("style", "noscript"): self._skip += 1

    def handle_endtag(self, tag):
        if tag == "title": self._in = None
        elif tag in ("script", "style", "noscript") and self._skip: self._skip -= 1

    def handle_data(self, data):
        if self._in == "title": self.title += data
        elif not self._skip: self.text.append(data)


def robots_rules(txt):
    """Return {agent: [(directive, path)]} from a robots.txt body."""
    groups, current, rules = {}, [], None
    for raw in txt.splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line: continue
        key, val = [s.strip() for s in line.split(":", 1)]
        key = key.lower()
        if key == "user-agent":
            if rules is not None: current, rules = [], None
            current.append(val.lower())
            for ag in current: groups.setdefault(ag, [])
        elif key in ("allow", "disallow") and current:
            rules = True
            for ag in current: groups[ag].append((key, val))
    return groups


def blocked_at_root(groups, bot):
    rules = groups.get(bot.lower(), groups.get("*", []))
    return any(d == "disallow" and p == "/" for d, p in rules) and not any(d == "allow" and p == "/" for d, p in rules)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("url"); ap.add_argument("--pages", type=int, default=25); ap.add_argument("--out")
    args = ap.parse_args()
    start = args.url if args.url.endswith("/") or urllib.parse.urlparse(args.url).path.count(".") else args.url + "/"
    u = urllib.parse.urlparse(start)
    origin, base = f"{u.scheme}://{u.netloc}", start
    out, problems = [], Counter()

    def say(line=""): out.append(line)

    def flag(area, text):
        problems[area] += 1
        say(f"- **{area}:** {text}")

    say(f"# Website check: {start}")
    say(f"\nRun {time.strftime('%Y-%m-%d %H:%M')} by check_site.py. Read-only. Pages fetched without JavaScript, as a crawler first sees them.\n")

    # 1. Site-level files
    say("## Site files\n")
    status, headers, body, final = fetch(start)
    if status != 200:
        flag("Works", f"the start page returned {status or headers.get('error')}. Nothing else can be checked.")
        return finish(out, args.out)
    if not final.startswith("https://"): flag("Security", "the site is served without HTTPS.")
    rs, _, rb, _ = fetch(origin + "/robots.txt")
    groups = robots_rules(rb.decode("utf-8", "replace")) if rs == 200 else {}
    if rs == 200: say(f"- robots.txt found at the domain root.")
    else: say(f"- No robots.txt at the domain root ({rs}): every crawler may read everything. Fine, but there is nowhere to list the sitemap.")
    if base.rstrip("/") != origin:
        ss, _, _, _ = fetch(urllib.parse.urljoin(base, "robots.txt"))
        if ss == 200: flag("Findable", "a robots.txt sits in a sub-folder. Crawlers read robots.txt only at the domain root, so it is ignored. It starts working on your own domain.")
    for bot in AI_BOTS:
        if groups and blocked_at_root(groups, bot):
            if bot in SEARCH_BOTS: flag("Findable", f"robots.txt blocks {bot}, so the site can drop out of that assistant's search answers.")
            else: say(f"- robots.txt blocks {bot} (a training crawler). This does not remove the site from AI search answers.")
    if groups and blocked_at_root(groups, "*"): flag("Findable", "robots.txt blocks every crawler from the whole site.")
    sm = [l.split(":", 1)[1].strip() for l in rb.decode("utf-8", "replace").splitlines() if l.lower().startswith("sitemap:")]
    sitemap_url = sm[0] if sm else urllib.parse.urljoin(base, "sitemap.xml")
    sms, _, smb, _ = fetch(sitemap_url)
    sitemap_urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", smb.decode("utf-8", "replace")) if sms == 200 else []
    say(f"- Sitemap: {len(sitemap_urls)} URLs at {sitemap_url}." if sitemap_urls else "")
    if not sitemap_urls: flag("Findable", "no sitemap found. Search engines find pages faster with one.")
    ls, _, _, _ = fetch(urllib.parse.urljoin(base, "llms.txt"))
    say("- llms.txt found: an index for AI agents." if ls == 200 else "- No llms.txt. Optional: an index that helps AI agents find your key pages.")
    missing = [h for h in SECURITY_HEADERS if h not in headers]
    if missing: flag("Security", "response headers missing: " + ", ".join(missing) + ". Some hosts, GitHub Pages among them, cannot set these; a host or CDN that can (Cloudflare, Vercel, Netlify) fixes it.")

    # 2. Pages
    say("\n## Pages\n")
    seen, queue, pages, link_status = set(), [start], [], {}
    while queue and len(pages) < args.pages:
        url = queue.pop(0)
        if url in seen: continue
        seen.add(url)
        st, hd, bd, fin = fetch(url) if url != start else (status, headers, body, final)
        link_status[url] = st
        if st != 200 or "html" not in hd.get("content-type", ""): continue
        p = Page(); p.feed(bd.decode("utf-8", "replace"))
        pages.append((url, p, hd))
        for href in p.links:
            absu = urllib.parse.urljoin(url, href.split("#")[0])
            if absu.startswith(base) and absu not in seen and absu not in queue and not re.search(r"\.(pdf|zip|png|jpe?g|webp|svg|gif|mp4)$", absu, re.I):
                queue.append(absu)
    titles = Counter(p.title.strip() for _, p, _ in pages)
    descs = Counter(p.meta.get("description", "").strip() for _, p, _ in pages)
    for url, p, hd in pages:
        path = url[len(origin):] or "/"
        issues = []
        t = p.title.strip()
        if not t: issues.append("no title")
        elif len(t) > 65: issues.append(f"title is {len(t)} characters (search results show about 60)")
        elif titles[t] > 1: issues.append("title repeats on another page")
        d = p.meta.get("description", "").strip()
        if not d: issues.append("no meta description")
        elif descs[d] > 1: issues.append("meta description repeats on another page")
        if p.h1 != 1: issues.append(f"{p.h1} h1 headings (expect 1)")
        if "noindex" in p.meta.get("robots", "").lower() or "noindex" in hd.get("x-robots-tag", "").lower(): issues.append("marked noindex: search engines will drop it")
        if not p.canonical: issues.append("no canonical link")
        if not p.lang: issues.append("no lang on <html>")
        if "viewport" not in p.meta: issues.append("no viewport tag: phones will show the desktop layout")
        if not p.meta.get("og:title") or not p.meta.get("og:image"): issues.append("no social preview (og:title and og:image)")
        words = len(" ".join(p.text).split())
        if words < 80: issues.append(f"only {words} words without JavaScript: crawlers and AI assistants may see an empty page")
        no_alt = sum(1 for i in p.imgs if "alt" not in i)
        no_size = sum(1 for i in p.imgs if not (i.get("width") and i.get("height")))
        eager_late = sum(1 for i in p.imgs[3:] if i.get("loading", "").lower() != "lazy")
        lazy_first = sum(1 for i in p.imgs[:1] if i.get("loading", "").lower() == "lazy")
        if no_alt: issues.append(f"{no_alt} images with no alt text")
        if no_size: issues.append(f"{no_size} images without width and height (the page may jump as they load)")
        if eager_late: issues.append(f"{eager_late} images after the first three are not lazy loaded")
        if lazy_first: issues.append("the first image is lazy loaded: if it is the largest thing on screen, this slows the page")
        if issues: flag("Page", f"`{path}`: " + "; ".join(issues) + ".")
    say(f"\n{len(pages)} pages checked. Structured data (JSON-LD) on {sum(1 for _, p, _ in pages if p.jsonld)} of them.")

    # 3. Links
    say("\n## Links\n")
    targets = set()
    for url, p, _ in pages:
        for href in p.links:
            if href.startswith(("mailto:", "tel:", "javascript:")) or href.startswith("#"): continue
            targets.add(urllib.parse.urljoin(url, href.split("#")[0]))
    broken, unsure = [], []
    for t in sorted(targets):
        if t in link_status: st = link_status[t]
        else:
            st = fetch(t, "HEAD")[0]
            if st in (0, 403, 405, 429): st = fetch(t, "GET", 20000)[0]
            link_status[t] = st
        if st in (0, 401, 403, 429): unsure.append((t, st))  # blocked or unreachable from here, not proof of a broken link
        elif st >= 400: broken.append((t, st))
    say(f"{len(targets)} distinct links checked.")
    for t, st in broken: flag("Links", f"{t} returned {st}.")
    if unsure:
        say(f"\n{len(unsure)} links could not be checked from here (no response, or the site refuses automated checks). Open them in a browser:")
        for t, st in unsure: say(f"- {t} ({st or 'no response'})")

    # 4. Summary
    say("\n## Summary\n")
    say("| Area | Findings |\n| --- | --- |")
    for area in ("Findable", "Page", "Links", "Security", "Works"):
        say(f"| {area} | {problems.get(area, 0)} |")
    say("\nNext: run PageSpeed Insights (speed and Core Web Vitals), the MDN HTTP Observatory (security headers) "
        "and Google Search Console's URL Inspection (what Google indexed), then score the site with the "
        "Website audit scorecard.")
    finish(out, args.out)


def finish(out, path):
    text = "\n".join(l for l in out if l is not None) + "\n"
    if path: open(path, "w", encoding="utf-8").write(text); print(f"wrote {path}")
    else: sys.stdout.write(text)


if __name__ == "__main__":
    main()
