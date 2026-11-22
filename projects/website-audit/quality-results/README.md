# Quality results: Website audit

**Who has tried it:** its author, Claude, on one real site, 22 November 2026. **Not yet tried:** a
live address, anyone else, ChatGPT, Gemini, and the Level 2 guide.

## 22 November 2026: Bradley Academy, served from a laptop copy

The live site could not be reached from the session, so the build was served locally with Python's
web server (no compression, no caching). Speed figures from that first run are a floor. The
later runs used a server with compression, as GitHub Pages serves the site.

| Check | Result |
| --- | --- |
| `check_site.py`, 16 pages, 80 links | Ran cleanly. Found 14 titles over 65 characters, no structured data, a robots.txt in a sub-folder, five missing security headers, images without sizes, 0 broken links, and 4 outside links it could not reach from the session. [Report](2026-11-22-check-before.md) |
| `check_site.py` on 40 pages | Ran cleanly; also crawled the static example pages, which lack canonical links and social previews by design |
| Lighthouse 12.8, home, Research, Practical AI | Performance 68, 76, 67 (local copy); accessibility, best practices and SEO 100 on all three |
| The skill's scorecard | 71 of 100, with five fixes. [Worked example](../base/examples/bradley-academy-audit.md) |
| Two fixes applied, checker run again | Long titles 14 to 0; structured data on 2 pages, up from 0 |
| All fixes applied (photos final, WebP copies, fonts preloaded, still motion on phones, privacy page, consent analytics ready), checker run on 30 pages | No new findings on the site's own pages; four GitHub links to this project return 404 until it is merged. [Report](2026-11-22-check-after.md) |
| Lighthouse 12.8.2 on both builds, served with compression | Performance 88 to 91, 94 to 94, 87 to 90; home 667 to 409 KB; home layout shift 0.035 to 0.001. [Table](2026-11-22-lighthouse.md) |
| The scorecard again | 81 of 100. Like for like (compressed), the site before the fixes was 73, not 71 |
| The report page, from `report-template.html` | Drawn without errors; no sideways scrolling at 390 or 1280 pixels after one fix (the bars and rings were too wide on phones). [Report](../base/examples/bradley-academy-report.html) |

## Found while testing, and fixed

- The first audit measured speed without compression, which understated it by about 20
  performance points. Speed is now measured with compression on.
- The report's bars and Lighthouse rings ran off a phone screen (443 pixels in a 390 window). They
  now stack below 600 pixels.
- The first version counted links it could not reach (no response, or 403 from sites that refuse
  automated checks) as broken. They are now listed separately as "could not be checked from here".

## Not checked

- PageSpeed Insights field data and the Observatory grade: they need the live address.
- A fresh agent following the Level 3 runbook without context.
- The skill in ChatGPT or Gemini, and on a site built in a chatbot.
