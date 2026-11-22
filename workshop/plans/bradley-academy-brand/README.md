# Bradley Academy as Bradley's own site

**One-line promise:** a research lead or a funded founder leaves the home page knowing what Bradley
Ross builds, why it is advanced, and how to start a conversation.

**Think of it as:** a gallery with three rooms. The research room and the studio are for the people
Bradley wants to work with. The classroom, Practical AI, stays open to everyone.

## Overview

The Bradley Academy site began as a home for the Practical AI tools. This plan turns it into
Bradley's own site at Bradley.academy, aimed at research labs and funded startups in the United
States first and Canada second, with Practical AI kept whole as one section. The full brand plan,
with the review of the old site and the disclosure rules, is a private document owned by Bradley.

## Decisions

| Decision | Choice | Decided |
| --- | --- | --- |
| Domain and name | Bradley.academy; the site stays Bradley Academy and the home page leads with Bradley's name | 22 November 2026 |
| Title | Agentic Architect and Researcher; "agentic engineer" is also allowed. This reverses the earlier decision: the audience is global, and Bradley holds Anthropic's Claude Certified Architect credential. Both words are protected titles in Ontario; Bradley accepts that risk | 22 November 2026, reversed the same day |
| Title risk | Accepted by Bradley. The Ontario Association of Architects says unlicensed use of "Architect" or any derivative is an offence, though its guidance is about buildings; Professional Engineers Ontario enforces "engineer", including against software titles. A certificate from Anthropic is not a provincial licence. A short call with an Ontario regulatory lawyer would settle both | Open, accepted |
| Market | United States first, Canada second: US spelling on Bradley's pages, US dollars, US Eastern hours | 22 November 2026 |
| Practical AI | Kept whole as one section, at `/tools`, with a practical guide added | 22 November 2026 |
| Contact | Early access by invitation, for Bradley's LinkedIn connections and partners only; not open to the general public. Office hours became agentic office hours on the Practical AI page: a prompt that points any assistant at the repository, with an assistant planned in [`practical-ai-guide`](../practical-ai-guide/README.md). Public office hours were dropped: they read as an offer of free help. Set in one place (`contact` in `app/content/brand.ts`) | 22 November 2026 |
| Style | A personal brand, not a catalogue: people browse, so each page shows the vision and a few proof points, then invites a conversation. Details come in conversation | 22 November 2026 |

## Pages

| Page | Address | Holds |
| --- | --- | --- |
| Home | `/` | Who Bradley is, a credentials strip, the vision in one sentence, three results, the range from small teams to labs, open work, the network, early access |
| Research | `/research` | The aim in one line, five milestones built on AISP, the system in five layers, the method, open work, early access |
| Practical AI | `/tools` | The tools, the smart intern idea, the practical guide, levels, the starter prompt, the classroom |
| About | `/about` | Credentials and the research to instruction line |

## Rules for these pages

- Show the question, the shape of the method and the class of evidence. Never the mechanism.
- Only public repositories are linked. No client or partner names without written permission.
- Bradley approves every research claim before the pages are merged.

## Acceptance check

Two independent reviewer agents, one playing a US research lead, a founder and an enterprise
engineering manager, the other reviewing UI, UX and front end, score the site. Target: 80 or more on
every item of the brand rubric (positioning, engineering depth, research signal, credentials,
teaching, calls to action, craft, protection of the research).

## Scores

The old site scored 53 for these audiences. Results of the two review loops are in
[`scores.md`](scores.md).

## Going live on Bradley.academy

Reviewed 22 November 2026, with the [Website audit](../../../projects/website-audit/base/examples/bradley-academy-audit.md)
(71 of 100 before its first two fixes). **Recommendation: yes, once the placeholder photo on the
home page's closing band is replaced.** The domain fixes two audit findings on its own: robots.txt
and llms.txt start counting at the root, and Search Console can verify the whole domain.

| Readiness item | Score | Note |
| --- | --- | --- |
| Content and claims | 90 | Approved by Bradley, 22 November 2026 |
| Search basics | 85 | Titles fixed, structured data added; robots.txt works once at the root |
| Pictures | 55 | Placeholders on the tool pages and the home page's closing band |
| Speed | 65 | Lab estimate; photos not yet resized or converted |
| Security headers | 50 | GitHub Pages cannot set them; a CDN in front can |
| Measurement | 20 | No Search Console or analytics yet |
| **Overall** | **61** | **About 80 after the photos, Search Console and the domain** |

Steps. Bradley does the steps marked "you"; each needs his accounts.

1. **You:** note what Bradley.academy serves today, and keep a copy.
2. **You:** in the repository, Settings, Pages, Custom domain: `bradley.academy`, then Save.
3. **You:** at the registrar, four A records for `bradley.academy` (185.199.108.153,
   185.199.109.153, 185.199.110.153, 185.199.111.153) and a CNAME for `www` to `bar181.github.io`.
4. **Agent, after DNS resolves:** in `.github/workflows/pages.yml`, build with `SITE_BASE=/` and
   `SITE_URL=https://bradley.academy`, so every link, the sitemap, robots.txt and llms.txt use the
   domain. Old `bar181.github.io/practical-ai/` links redirect to the domain.
5. **You:** turn on Enforce HTTPS when GitHub offers it.
6. **You:** Search Console, a domain property, the sitemap submitted (Website audit, Level 2).
7. **Later, optional:** Cloudflare in front of the domain for security headers and caching.

## Further work for the public site

1. Replace the placeholder photos, starting with the home page and the most visited tools (the
   Image brief page lists every one).
2. Resize the photos and serve WebP or AVIF at the widths they are shown.
3. A contact form for companies and people who want a website built or reviewed, saved to Supabase
   with insert-only access (Website audit, Level 2). It complements LinkedIn; decide whether it
   carries early-access requests too.
4. Analytics with consent, and Search Console.
5. Shorter, lighter motion on phones: about 240 KB of unused JavaScript per page, mostly the motion
   libraries.

## Still open

- A request form for early access, if LinkedIn proves too open.
- A real portrait large enough for a full-screen scene, and final pictures for the new image slots.
- Which research findings Bradley approves for publication: under 2% against 40 to 60%, Milestone 1 at 17 against 62 failures, 37 of 40 after eight sessions, the 6 of 6 grammar trial and the 250,000 units of knowledge.
- A measured failure rate for elite prose instructions over eight sessions, to replace the labelled projection (about 43% kept, 0.9 to the power of 8).
- Whether the AISP explainer video is cleared to publish.
