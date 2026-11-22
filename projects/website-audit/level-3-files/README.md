# Level 3: the full audit, run by a coding agent

**The core idea:** a coding agent runs every free check on every page, scores the site with the
same scorecard, and writes an improvement plan you can hand to whoever builds the site.

**Think of it as** the full inspection with the instruments out, room by room, with a written
report and a repair schedule.

**Status, 22 November 2026:** `check_site.py`, Lighthouse and the report page were run on Bradley
Academy, served from a laptop copy, before and after its fixes. The rest of this runbook has not been followed end to end by a fresh agent.

## What you need

- A coding agent that can run commands (Claude Code, for example).
- Python 3.9 or later; Node.js for Lighthouse; Chrome.
- The site's address. For a site you own, Search Console access helps (you check it, not the agent).

## The runbook, for the agent

1. **Read** [`../base/SKILL.md`](../base/SKILL.md). Its scorecard and report shape are the output.
2. **Crawl:** `python3 check_site.py https://your-site/ --pages 50 --out audit/check.md`
3. **Speed and basics,** for the home page and the two or three most important pages, on mobile:
   `npx lighthouse https://your-site/PAGE --output=json --output-path=audit/lh-PAGE.json --only-categories=performance,accessibility,best-practices,seo`
4. **Security:** the MDN HTTP Observatory for the domain, on its website or its API.
5. **Real users:** if the site has traffic, the person runs PageSpeed Insights and pastes the field
   data (Core Web Vitals for real visitors).
6. **Message:** read the home page and the main landing pages, then fill the core context card.
   Mark each line "from the site" or "needs you".
7. **Score** with the scorecard. Full points only with evidence in the files above.
8. **Plan the fixes** with [Agentic Process](../../agentic-process/README.md): one change per item,
   with where, the fix, how to check it, and what it should move on the scorecard. Order by points
   gained per hour of work.
9. **Report page:** copy [`../base/report-template.html`](../base/report-template.html) to
   `audit/report.html` and replace its JSON data block with the audit: areas, issues by severity,
   Core Web Vitals, Lighthouse by page, before and after (if any), fixes, could not check and the
   core context card. Leave out what you did not measure; the page skips empty parts. Open it at
   390 and 1280 pixels wide.
10. **Stop.** Report and plan only. The person approves every change and every publish.

## What check_site.py checks

Read-only, standard library only. It fetches pages as a crawler first sees them, without
JavaScript.

| Check | Why |
| --- | --- |
| robots.txt at the domain root, and which AI crawlers it blocks | Blocking OAI-SearchBot or Claude-SearchBot can drop you from AI search answers; blocking training crawlers does not |
| A robots.txt in a sub-folder | Crawlers ignore it there |
| Sitemap and llms.txt | Faster discovery by search engines and AI agents |
| Security headers on the start page | Missing headers lower the Observatory grade |
| Per page: title length and repeats, description, one h1, canonical, lang, viewport, social preview | What search results and link previews show |
| Per page: words visible without JavaScript | A page that is empty without scripts can look empty to crawlers |
| Per page: images without alt text or size, lazy loading after the first screen, and a lazy first image | Accessibility, layout shift and speed |
| Structured data (JSON-LD) | How search engines and assistants understand the business or person |
| Every link | Broken links, and links that could not be checked from where it ran |

## Sources

Checked 22 November 2026.

- [Core Web Vitals thresholds](https://web.dev/articles/defining-core-web-vitals-thresholds), web.dev
- [The performance effects of too much lazy loading](https://web.dev/articles/lcp-lazy-loading), web.dev
- [Introduction to robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro), Google Search Central
- [Overview of OpenAI crawlers](https://developers.openai.com/api/docs/bots), OpenAI
- [Does Anthropic crawl data from the web?](https://support.claude.com/en/articles/8896518), Anthropic
- [Lighthouse performance scoring](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring) (the 0 to 49, 50 to 89, 90 to 100 bands), Chrome for Developers
- [How is Site Health Score calculated?](https://www.semrush.com/kb/114-total-score) (errors weigh more than warnings), Semrush
- [What is Health Score?](https://help.ahrefs.com/en/articles/1424673-what-is-health-score-and-how-is-it-calculated-in-ahrefs-site-audit) (only errors lower it; warnings and notices do not), Ahrefs
- [HTTP Observatory scoring](https://developer.mozilla.org/en-US/observatory/docs/tests_and_scoring), MDN

Part of the [Website audit](../README.md).
