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
(71 of 100 before the fixes, 80 after). **Recommendation: yes.** The photos are Bradley's own and
final (confirmed 22 November 2026). The domain fixes two audit findings on its own: robots.txt and
llms.txt start counting at the root, and Search Console can verify the whole domain.

| Readiness item | Score | Note |
| --- | --- | --- |
| Content and claims | 90 | Approved by Bradley, 22 November 2026 |
| Search basics | 85 | Titles fixed, structured data added; robots.txt works once at the root |
| Pictures | 85 | Bradley's own photos, now light WebP copies sized for phones and laptops |
| Speed | 72 | Lab, local copy: home 72, research 77, tools 69 for performance. Pages are about a third lighter |
| Security headers | 50 | GitHub Pages cannot set them; a CDN in front can |
| Measurement | 40 | Ready: set `SITE_GSC` and `SITE_GA_ID`; analytics waits for consent. Not switched on yet |
| **Overall** | **70** | **The average of the six. About 78 once Search Console and analytics are on (measurement to 85); about 85 with Cloudflare headers too** |

Steps. Bradley does the steps marked "you"; each needs his accounts.

1. **You:** note what Bradley.academy serves today, and keep a copy.
2. **You:** in the repository, Settings, Pages, Custom domain: `bradley.academy`, then Save.
3. **You:** at the registrar, four A records for `bradley.academy` (185.199.108.153,
   185.199.109.153, 185.199.110.153, 185.199.111.153) and a CNAME for `www` to `bar181.github.io`.
4. **Agent, after DNS resolves:** in `.github/workflows/pages.yml`, build with `SITE_BASE=/` and
   `SITE_URL=https://bradley.academy`, so every link, the sitemap, robots.txt and llms.txt use the
   domain. Old `bar181.github.io/practical-ai/` links redirect to the domain.
5. **You:** turn on Enforce HTTPS when GitHub offers it.
6. **You:** Search Console, a domain property, the sitemap submitted (Website audit, Level 2). If
   you choose the HTML-tag method, give the agent the token for `SITE_GSC`.
7. **You, optional:** a Google Analytics 4 property; give the agent its ID for `SITE_GA_ID`. Visitors
   see a consent banner, and nothing loads until they say yes.
8. **Later, optional:** Cloudflare in front of the domain for security headers and caching.

## Further work for the public site

Done on 22 November 2026: the Image brief page removed (the photos are final); light WebP copies
at two widths; a consent banner, analytics and Search Console ready behind build settings; a
privacy page; the fonts preloaded; phones get the still version of the motion.

1. A contact form for companies and people who want a website built or reviewed, saved to Supabase
   with insert-only access (Website audit, Level 2). It complements LinkedIn; decide whether it
   carries early-access requests too.
2. Switch on Search Console and analytics once the domain is live (steps 6 and 7 above).
3. Load the motion libraries only on screens that use them: phones no longer run them, but still
   download them.

## Messaging for a top-tier reader (22 November 2026)

An outside reviewer read the site as decent, not top tier. The diagnosis: it spoke to every
audience at once, led with credentials rather than work, and its numbers could not be checked. The
home and Research pages now lead with the contribution (AISP and BAR Observatory), show only public
evidence with a "Method and limits" link on each number, and end with a five-step "Check it
yourself" path: the paper, the evidence, the validator, the agent guide, and BAR Observatory.
Credentials moved to About. Small business moved below research.

Still weak, and only fixable in the research repositories: the AISP README's "97x" figure does not
follow from its own table (59% to 95% success), the tier distribution and benchmarks have no data
or script behind them, and the paper is a submission draft with LLM judges and no human agreement
score.

## Still open

- A request form for early access, if LinkedIn proves too open.
- A real portrait large enough for a full-screen scene.
- Unpublished results stay off the site (Bradley's decision, 22 November 2026, to protect the
  research): the learning and transfer studies are shared with partners on request, once each is
  verified. The site shows only what is public in aisp-open-core and bar-observatory, each linked
  to its method and limits.
- Whether the AISP explainer video is cleared to publish.
