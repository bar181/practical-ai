# Worked example: Bradley Academy, before going live on its own domain

Made by Claude on 22 November 2026 by following [`../SKILL.md`](../SKILL.md) on the Bradley Academy
site (the website in this repository), with two free tools run on a copy served from a laptop:
Lighthouse 12.8 on three pages and [`check_site.py`](../../level-3-files/check_site.py) on 16 pages.
The live site could not be reached from the session, so speed figures are lab estimates from the
local copy, which had no compression or caching. Treat them as a floor, not a measurement.

## Score: 71 out of 100

The message, phones and accessibility are strong. Placeholder photos on the tool pages, the speed of the large
pictures, and running on a sub-folder of GitHub Pages hold it back.

## Fix first

| # | Where | Why a visitor cares | The fix | Helps |
| --- | --- | --- | --- | --- |
| 1 | Tool pages, and the home page's closing band | A research lab judging rigour meets placeholder photos (a puppy in a tweed jacket, a paint-splashed light bulb, a sunset). They undercut the credibility the words build | Replace the pictures listed on the Image brief page, starting with the home page and the most visited tools | Image brief, Artifact Studio |
| 2 | The whole site | On `bar181.github.io/practical-ai/`, `robots.txt` and `llms.txt` sit in a sub-folder, where crawlers do not look | Move to Bradley.academy, so both files sit at the root | Site Studio, Level 2 |
| 3 | Home: the large photos | Lighthouse estimates 181 KB could be saved by sizing pictures to the screen and 85 KB more by modern formats. Largest Contentful Paint was 5.7 s on the local copy, against a 2.5 s target | Serve each photo as WebP or AVIF at the widths it is shown, and keep the first one eager | Site Studio, Level 3 |
| 4 | Every page | Security headers (HSTS, a content security policy) cannot be set on GitHub Pages | Put Cloudflare in front of the custom domain, or host where headers can be set | Site Studio, Level 3 |
| 5 | Measurement | Nothing shows who visits or which pages work | Add Google Search Console for the domain, and analytics with consent where required | Website audit, Level 2 |

## The scorecard

| Area | Points | Evidence |
| --- | --- | --- |
| 1. Message | 16 of 20 | First screen: name, title, "Agentic systems that behave the same way every time", and two clear next steps. Who it is for is in the lead line. Loses points because the headline names a quality, not a result for the reader |
| 2. Found in search and AI | 10 of 15 | Every page pre-rendered, so text is there without JavaScript; one h1; canonical links; a sitemap of 16 pages. But 14 of 16 titles ran past 65 characters (up to 134), no structured data, and robots.txt in a sub-folder |
| 3. Speed | 8 of 15 | Estimate. Lighthouse performance 68, 76 and 67 on home, Research and Practical AI. Unused JavaScript about 240 KB (the motion libraries). Cumulative Layout Shift good at 0.035 or less. Field data needs the live site in PageSpeed Insights |
| 4. Phones and access | 15 of 15 | Lighthouse accessibility 100 on all three pages; no sideways scrolling at 390 pixels; tap targets at least 44 pixels |
| 5. Trust and contact | 9 of 10 | Who runs it: "operated by WiseGeo Inc., a federally incorporated Canadian company". Credentials and research results, all from Bradley. Contact is LinkedIn only |
| 6. Security | 6 of 10 | HTTPS on GitHub Pages; no keys or private data in the page source; no forms. Five security headers missing, which GitHub Pages cannot set. Observatory grade not run |
| 7. Links and content | 6 of 10 | 0 broken links of 80. Four outside links could not be reached from the session (open them in a browser). Placeholder photos on the tool pages and the home page's closing band |
| 8. Measured | 1 of 5 | A sitemap is ready for Search Console. No analytics |

## Could not check

- Real-user speed: PageSpeed Insights on the live address.
- Security grade: MDN HTTP Observatory on the live address.
- What Google has indexed: Search Console's URL Inspection, once the domain is verified.
- Four outside links: LinkedIn, agentics.org and two GitHub repositories, which refused automated
  checks from the session.

## Fixed on the same day

Titles now fit (for example "Research brief with checked sources | Bradley Academy", 53
characters), the home and About pages carry `Person` structured data, and the home description was
reworded. A rerun of the checker found 0 long titles, down from 14, and structured data on 2 pages,
up from 0. Evidence: [before](../../quality-results/2026-11-22-check-before.md) and
[after](../../quality-results/2026-11-22-check-after.md).

## Core context card: Bradley Academy

```
Core context card: Bradley Academy
One line:            Needs you. Draft: "Research and teaching that make AI agents behave the same way every time."
Who it is for:       Research labs and partners; engineering teams; small businesses learning practical AI   (from the site)
The problem:         Most AI solves the same problem from scratch every time   (from the site)
Value proposition:   Deterministic AI that keeps what it learns, built on AISP   (from the site)
Unique selling points: AISP, a mathematical specification language; research milestones from
                     pre-registered studies; teaching from ten-person teams to frontier labs   (from the site)
Proof:               Under 2% ambiguity against 40 to 60% in prose; 17 vs 62 failures (Milestone 1);
                     Claude Certified Architect; CS50 Teaching Fellow   (from the site)
Core messages:       Systems that behave the same way every time; machines that keep what they learn;
                     grounded in small business, trusted by advanced teams   (from the site)
Call to action:      Early access by invitation; connect on LinkedIn   (from the site)
Tone:                Needs you. Draft: confident, precise, plain
Never say:           Needs you
```
