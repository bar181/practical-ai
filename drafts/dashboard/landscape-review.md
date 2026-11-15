# Dashboard: landscape review

What established practice says about dashboards, checked on 2026-11-15 before building further.

## Summary

- **The advice is consistent across sources.** Few numbers, each with a comparison, laid out for
  the person who acts on them. The simple level follows it.
- **Our cap of six tiles sits inside every range found.** Sources give five to seven, five to
  nine, and five to ten.
- **Nothing new needs building for the simple level.** A spreadsheet, a chat assistant and one
  page of instructions.

## Established practice

| Practice | What the sources say | Source |
| --- | --- | --- |
| Limit the numbers | Five to seven per view before understanding drops. Others say five to nine, or five to ten | [Boundev](https://boundev.ai/blog/dashboard-design-best-practices-guide), [Fiveable](https://fiveable.me/lists/best-practices-for-dashboard-design), [Domo](https://domo-webflow.domo.com/learn/article/kpi-dashboards) |
| Give every number a comparison | A target or the prior period, so a reader can tell at once whether the number is good | [Klipfolio](https://www.klipfolio.com/blog/6-dashboard-design-mistakes), [Databox](https://databox.com/?p=149009) |
| Tie each number to a decision | A metric that does not trigger an action does not belong on the screen | [Boundev](https://boundev.ai/blog/dashboard-design-best-practices-guide) |
| Design for the person who acts | Build for whoever uses the information, not whoever built the page. Picture a new employee on day one | [Klipfolio](https://www.klipfolio.com/blog/6-dashboard-design-mistakes) |
| One dashboard per need | Separate pages for separate purposes | [Klipfolio](https://www.klipfolio.com/blog/6-dashboard-design-mistakes) |
| Keep it simple on small screens | Phones need minimal, focused layouts | [Klipfolio](https://www.klipfolio.com/blog/6-dashboard-design-mistakes) |
| Too many metrics tire people | Overloaded dashboards lead to fatigue and go unread | [TechTarget](https://www.techtarget.com/searchbusinessanalytics/tip/Good-dashboard-design-8-tips-and-best-practices-for-BI-teams) |

The sources are vendor and trade guides, not studies. Several cite a working-memory limit for the
number range without naming the research. Treat the range as agreed practice, not as a finding.

## How the simple level follows it

| Practice | In this tool |
| --- | --- |
| Limit the numbers | Six tiles at most. The assistant proposes them and waits |
| A comparison for every number | Each tile shows the change from the previous period, with a sign and a word |
| Tie to a decision | The guide asks what "good" looks like for each number before it goes on the page |
| Simple on small screens | One column of tiles, one chart, one table |

## Not rechecked for this review

From general knowledge:

- Which assistants can read a live spreadsheet, and on which plans.
- Connections from assistants to sales, accounting and customer systems.
- Hosted dashboard products. Many exist. A review of them, with prices, belongs before the
  automated level is built.

## Build or license

| Level | Lean | Why |
| --- | --- | --- |
| Simple | Build nothing. Instructions and a sheet | The practice is settled and the page is small |
| Working | Reuse the assistant's connection to a live sheet | Rebuilding from the latest rows is the only new part |
| Automated | License. Review hosted dashboard products before building connections to several systems | Keeping connections working is ongoing work that products already do |

## Still to do

- Review hosted dashboard products and their prices for the automated level.
- Check how each assistant connects to a live spreadsheet.
- Test the demo with a real sheet that has gaps and totals mixed in.
