# Website audit

Know what is holding your website back, and what to fix first.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Done, 22 November 2026 | Built: [the project](../../../projects/website-audit/) | Levels 1 to 3 written; run on one real site |

**Think of it as:** a home inspection before a sale. The inspector walks every room, notes what a
buyer would notice, and ranks the repairs.

## Overview

People make pages in Claude or ChatGPT, or own a company site, and do not know whether it is found,
fast, safe or clear. Free tools answer parts of that in their own jargon. The audit runs or reads
them, scores the site out of 100 on one scorecard, adds the part they skip (does a stranger
understand the business?), and lists five fixes in plain words. It also writes the business's core
context card, which students keep and paste into every AI task.

## Who it is for

Owners of small business sites, people who built a page in a chatbot, and students in Bradley's
courses who need a checklist before they publish.

## Scope

- **In:** the message, search and AI search, speed, phones and accessibility, trust and contact,
  security visible from outside, links and content, measurement. The core context card.
- **Out:** changing the site, logging in anywhere, penetration testing, legal advice on privacy.
- **It works when:** given Bradley Academy, it scores the site with evidence for every point, finds
  the long titles and the robots.txt in a sub-folder, and draws a report page with the scorecard and
  charts. Met on 22 November 2026: 71 of 100, then 81 after the fixes. The first run listed the
  photos as placeholders; the owner corrected that, and the photos are final.

## What might be involved at each level

| Level | What it involves | Complexity |
| --- | --- | --- |
| Level 1, Beginner: basic checks | The skill in any chatbot, with the site's address or the page pasted in; PageSpeed Insights and the Observatory results pasted for real speed and security scores | Beginner |
| Level 2, Intermediate: the expected basics | Search Console, a contact form saved to Supabase with insert-only access, analytics with consent, a privacy note | Intermediate |
| Level 3, Advanced: the full audit | A coding agent runs `check_site.py`, Lighthouse and the Observatory, scores every page and writes the improvement plan with Agentic Process | Advanced |
| Commercial grade | Scheduled audits with trend lines, alerts on regressions, client-ready reports | Explained, not built |

## Established best practices

1. **Judge speed by Core Web Vitals at the 75th percentile:** good is Largest Contentful Paint
   2.5 s or less, Interaction to Next Paint 200 ms or less, Cumulative Layout Shift 0.1 or less.
   Source: [How the Core Web Vitals thresholds were defined](https://web.dev/articles/defining-core-web-vitals-thresholds),
   web.dev, checked 22 November 2026.
2. **Prefer field data to lab data, and say which you have.** PageSpeed Insights shows both: real
   users from the Chrome UX Report, and a Lighthouse lab run. Source:
   [About PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/about), Google,
   checked 22 November 2026.
3. **Lazy load below the first screen, never the main image.** Too much lazy loading made the
   Largest Contentful Paint slower in Google's analysis. Source:
   [The performance effects of too much lazy loading](https://web.dev/articles/lcp-lazy-loading),
   web.dev, checked 22 November 2026.
4. **Use noindex, not robots.txt, to keep a page out of Google.** robots.txt manages crawling and is
   read only at the domain root. Source:
   [Introduction to robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro),
   Google Search Central, checked 22 November 2026.
5. **Treat AI crawlers separately:** search crawlers (OAI-SearchBot, Claude-SearchBot) decide
   whether you appear in AI search answers; training crawlers (GPTBot, ClaudeBot) do not. Sources:
   [Overview of OpenAI crawlers](https://developers.openai.com/api/docs/bots) and
   [Anthropic's crawlers](https://support.claude.com/en/articles/8896518), checked 22 November 2026.
6. **Grade security headers with the MDN HTTP Observatory,** and know your host's limits: GitHub
   Pages cannot set custom headers. Sources:
   [HTTP Observatory scoring](https://developer.mozilla.org/en-US/observatory/docs/tests_and_scoring),
   MDN, and [GitHub community discussion 54257](https://github.com/orgs/community/discussions/54257),
   checked 22 November 2026.
7. **Wait for consent before analytics storage where required,** using consent mode. Source:
   [Consent mode overview](https://developers.google.com/tag-platform/security/concepts/consent-mode),
   Google, checked 22 November 2026.
8. **Sort findings by severity and let errors weigh most.** The market's audits split issues into
   errors, warnings and notices. Semrush's Site Health weighs errors more than warnings; Ahrefs'
   Health Score counts only errors. Sources:
   [How is Site Health Score calculated?](https://www.semrush.com/kb/114-total-score), Semrush, and
   [What is Health Score?](https://help.ahrefs.com/en/articles/1424673-what-is-health-score-and-how-is-it-calculated-in-ahrefs-site-audit),
   Ahrefs, checked 22 November 2026.
9. **Band every score in words and colour.** Lighthouse marks 0 to 49 poor, 50 to 89 needs
   improvement and 90 to 100 good. The report uses the same bands and always writes the word, so
   the colour is never the only signal. Source:
   [Lighthouse performance scoring](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring),
   Chrome for Developers, checked 22 November 2026.

## What it reuses

- PageSpeed Insights, Lighthouse, Search Console and the MDN HTTP Observatory: run or read, never
  rebuilt.
- Web Sections, Tone Studio and Site Studio for the fixes; Agentic Process for the improvement plan.
- Supabase, as in Site Studio Level 3 and the Learnings database, for the contact form.

## Decisions to record

- [x] **Reuse check:** the free tools cover speed, security and indexing. Built only the missing
  pieces: one scorecard, the message check, the core context card, and a crawler-eye checker for
  titles, robots.txt, AI crawlers, llms.txt, structured data and links.
- [x] **Build or license:** build; the checker is standard-library Python, read-only.
- [x] **Dependencies and pricing:** Level 1 is free with any chatbot. Level 3 needs Python, Node.js
  and Chrome, all free.
- [ ] **A hosted version:** a web form that runs the checker for a visitor. Not before Level 1 and
  Level 3 have users.

## Open questions

- Should the scorecard weigh areas differently for a shop, a portfolio or a research site?
- Should the core context card become its own small tool, since students need it for every AI task?
- Would a scheduled audit (weekly, with alerts) be worth a Level 3 option?
