# Worked example: Bradley Academy, before going live on its own domain

Made by Claude on 22 November 2026 by following [`../SKILL.md`](../SKILL.md) on the Bradley Academy
site (the website in this repository), with two free tools run on a copy served from a laptop:
Lighthouse 12.8 on three pages and [`check_site.py`](../../level-3-files/check_site.py) on 16 pages.
The live site could not be reached from the session, so speed figures are lab estimates from the
local copy, which had no compression or caching. Treat them as a floor, not a measurement.

## Score: 81 out of 100 (71 before the fixes)

The message, phones, accessibility and trust are strong. What holds it back now is the address: on a
sub-folder of GitHub Pages, robots.txt is ignored, security headers cannot be set and Search Console
cannot verify the whole domain. Moving to Bradley.academy fixes most of that.

The report with the scorecard and charts: [`bradley-academy-report.html`](bradley-academy-report.html).

## Fix first

| # | Where | Why a visitor cares | The fix | Helps |
| --- | --- | --- | --- | --- |
| 1 | The whole site | On `bar181.github.io/practical-ai/`, `robots.txt` and `llms.txt` sit in a sub-folder, where crawlers do not look | Move to Bradley.academy, so both files sit at the root | Site Studio, Level 2 |
| 2 | Measurement | Nothing shows who visits or what Google has indexed | Switch on what is now built in: the Search Console tag (`SITE_GSC`) and analytics with consent (`SITE_GA_ID`) | Website audit, Level 2 |
| 3 | Home and Practical AI: the opening photo | Largest Contentful Paint is 3.1 s against a 2.5 s target. The photo arrives in time; it waits about 75% of that for the stylesheet (51 KB, 11 KB compressed) and the fonts | Preload the opening photo at its phone size, and split the stylesheet so the first screen needs less of it | Site Studio, Level 3 |
| 4 | Every page | Security headers (HSTS, a content security policy) cannot be set on GitHub Pages | Put Cloudflare in front of the custom domain, or host where headers can be set | Site Studio, Level 3 |
| 5 | Tool pages | Up to 18 example pictures a page have no width and height, and phones still download about 189 KB of motion code they no longer run. Layout shift is measured low (0.017 at most), so this is tidying | Write each picture's size into the page at build time; load the motion libraries only on screens that use them | Site Studio |

## The scorecard

| Area | Points | Evidence |
| --- | --- | --- |
| 1. Message | 16 of 20 | First screen: name, title, "Agentic systems that behave the same way every time", and two clear next steps. Who it is for is in the lead line. Loses points because the headline names a quality, not a result for the reader |
| 2. Found in search and AI | 12 of 15 | Every page pre-rendered, so text is there without JavaScript; one h1; canonical links; a sitemap of 18 pages; titles now fit (0 over 65 characters, down from 14); `Person` structured data on home and About. Loses points for robots.txt in a sub-folder |
| 3. Speed | 11 of 15 | Lab, mobile, compressed as GitHub Pages serves it: Lighthouse performance 91, 94 and 90 on home, Research and Practical AI. Largest Contentful Paint 3.1, 2.5 and 3.1 s; layout shift 0.017 or less; blocking time 10 ms or less. Pages weigh 230 to 409 KB, down from 275 to 667. Field data needs the live site in PageSpeed Insights |
| 4. Phones and access | 15 of 15 | Lighthouse accessibility 100 on all three pages; no sideways scrolling at 390 pixels; tap targets at least 44 pixels. Phones get the still version of the motion |
| 5. Trust and contact | 10 of 10 | Who runs it: "operated by WiseGeo Inc., a federally incorporated Canadian company". Credentials and research results, all from Bradley. Contact is LinkedIn. A privacy page now says what is collected: nothing, until analytics is switched on, and then only after consent |
| 6. Security | 6 of 10 | HTTPS on GitHub Pages; no keys or private data in the page source; no forms; a referrer policy set in the page. Five security headers missing, which GitHub Pages cannot set. Observatory grade not run |
| 7. Links and content | 9 of 10 | No broken links on the site. Four GitHub links to this project return 404 until it is merged. Four outside links could not be reached from the session (open them in a browser). The photos are Bradley's own and final |
| 8. Measured | 2 of 5 | Search Console and analytics with consent are built in but not switched on. A sitemap is ready |

## Could not check

- Real-user speed: PageSpeed Insights on the live address.
- Security grade: MDN HTTP Observatory on the live address.
- What Google has indexed: Search Console's URL Inspection, once the domain is verified.
- Four outside links: LinkedIn, agentics.org and two GitHub repositories, which refused automated
  checks from the session.

## Fixed on 22 November 2026

| Fix | Measured result |
| --- | --- |
| Titles shortened; `Person` structured data on home and About | 0 long titles, down from 14; structured data on 2 pages, up from 0 |
| Photos confirmed final; the Image brief page removed | Links and content 6 to 9 |
| Light WebP copies of every photo at 1600 and 800 pixels, served with `srcset` | Home 667 to 409 KB, Practical AI 528 to 389 KB, Research 275 to 230 KB |
| Fonts preloaded; phones get the still version of the motion | Home layout shift 0.035 to 0.001; largest paint 3.4 to 3.1 s on home and 3.5 to 3.1 s on Practical AI. Performance 88 to 91 and 87 to 90, within what one run can move |
| A privacy page, a referrer policy, a consent banner, and Search Console and analytics behind build settings | Trust 9 to 10; measurement ready to switch on |

Measured with Lighthouse 12.8, mobile, one run per page, on two builds served locally with
compression: the commit before these fixes and the commit after. One run can move a few points, so
treat a change of 3 or less as noise. Research held at 94.

The first pass of this audit scored speed 8 of 15 from a copy served without compression (home
68). GitHub Pages compresses, so that understated the speed. Measured the same way as above, the
site before the fixes would have scored 10 for speed and 73 overall.

Evidence: [checker before](../../quality-results/2026-11-22-check-before.md),
[checker after](../../quality-results/2026-11-22-check-after.md) and the
[Lighthouse numbers](../../quality-results/2026-11-22-lighthouse.md).

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
