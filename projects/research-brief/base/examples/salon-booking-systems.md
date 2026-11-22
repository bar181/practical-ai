# Worked example: three salon booking systems

**Invented.** The salon, the three booking systems, the pages and the links are made up. The
`example.com` links do not open, which is why the pages are pasted in. This is the try-it prompt
from the [README](../../README.md#try-it-now).

This is the reply a fresh Claude session gave on 22 November 2026, unedited. The session saw only
[`../SKILL.md`](../SKILL.md) and the input below, and could not browse the web. It was graded
against the answer key at the end, written before the run, and passed. [The evidence](../../quality-results/README.md).

## The input

```
Read the instructions at this link and follow them for the rest of this chat:
https://raw.githubusercontent.com/bar181/practical-ai/main/projects/research-brief/base/SKILL.md

The choice: which booking system should our hair salon use from January?
The options: Bookwell, SlotPilot, Chairtime.
What matters: monthly price, card fee, no-show deposits, contract length.

My notes to check (from a quick chat with an AI):
- SlotPilot has no contract, cancel any time. Source: https://example.com/slotpilot/pricing
- Chairtime is the one most salons use.
- Bookwell takes no-show deposits. Source: https://example.com/bookwell/features

Page 1, https://example.com/bookwell/pricing (updated 3 November 2026):
"Bookwell Solo is £29 a month for one chair. Each extra chair is £10 a month. Card payments cost 1.9% + 20p. Pay monthly, cancel with 30 days' notice."

Page 2, https://example.com/slotpilot/pricing (no date shown):
"SlotPilot Studio: £35 a month on a 12-month minimum term. Card fee 1.5% per transaction. Take a deposit at booking to cut no-shows."

Page 3, https://example.com/chairtime/plans (updated 20 October 2026):
"Chairtime Free: no monthly fee. Card payments 2.5% + 10p. Deposits and no-show fees on the Plus plan, £19 a month. No contract."
```

## The reply (unedited)

**Count:** 13 claims: 10 checked, 0 partly, 1 does not match, 1 could not open, 1 with no source.

**How I checked:** I read the three pages you pasted and your three notes. I cannot open web pages in this chat, so I did not browse. Dates are as you gave them with each page.

**In short:** Contract length differs most: Bookwell is pay monthly with 30 days' notice [3], SlotPilot has a 12-month minimum term [4], Chairtime says no contract [10].
Monthly price runs from no monthly fee (Chairtime Free [7]) to £35 (SlotPilot [4]); card fees from 1.5% (SlotPilot [5]) to 2.5% + 10p (Chairtime [8]). Chairtime deposits need the Plus plan at £19 a month [9].
Still unknown: whether Bookwell takes no-show deposits, and how current the SlotPilot page is (no date shown).

#### Flags: check these before you share

| Option | Claim | Result | What the source actually says |
| --- | --- | --- | --- |
| SlotPilot | No contract, cancel any time | Does not match | "SlotPilot Studio: £35 a month on a 12-month minimum term." [4] |
| Bookwell | Takes no-show deposits | Could not open | You cited https://example.com/bookwell/features, but its text was not pasted and I cannot open web pages. The Bookwell pricing page you pasted does not mention deposits. |
| Chairtime | The one most salons use | No source | Nothing was cited. None of the three pages mentions how many salons use it. |

#### The comparison

| What matters | Bookwell | SlotPilot | Chairtime |
| --- | --- | --- | --- |
| Monthly price | £29 for one chair, £10 per extra chair [1] | £35, on a 12-month minimum term [4] | Free: no monthly fee [7]; Plus: £19 [9] |
| Card fee | 1.9% + 20p [2] | 1.5% per transaction [5] | 2.5% + 10p [8] |
| No-show deposits | ⚠ see flags | Deposit at booking [6] | On the Plus plan, £19 a month [9] |
| Contract length | Pay monthly, 30 days' notice [3] | ⚠ see flags | No contract [10] |

#### The words behind each number

| # | The exact words | Source | Date on page |
| --- | --- | --- | --- |
| 1 | "Bookwell Solo is £29 a month for one chair. Each extra chair is £10 a month." | Page 1 you pasted, https://example.com/bookwell/pricing | Updated 3 November 2026 |
| 2 | "Card payments cost 1.9% + 20p." | Page 1 you pasted, https://example.com/bookwell/pricing | Updated 3 November 2026 |
| 3 | "Pay monthly, cancel with 30 days' notice." | Page 1 you pasted, https://example.com/bookwell/pricing | Updated 3 November 2026 |
| 4 | "SlotPilot Studio: £35 a month on a 12-month minimum term." | Page 2 you pasted, https://example.com/slotpilot/pricing | No date shown |
| 5 | "Card fee 1.5% per transaction." | Page 2 you pasted, https://example.com/slotpilot/pricing | No date shown |
| 6 | "Take a deposit at booking to cut no-shows." | Page 2 you pasted, https://example.com/slotpilot/pricing | No date shown |
| 7 | "Chairtime Free: no monthly fee." | Page 3 you pasted, https://example.com/chairtime/plans | Updated 20 October 2026 |
| 8 | "Card payments 2.5% + 10p." | Page 3 you pasted, https://example.com/chairtime/plans | Updated 20 October 2026 |
| 9 | "Deposits and no-show fees on the Plus plan, £19 a month." | Page 3 you pasted, https://example.com/chairtime/plans | Updated 20 October 2026 |
| 10 | "No contract." | Page 3 you pasted, https://example.com/chairtime/plans | Updated 20 October 2026 |

#### Not found

None.

**Before you share:** Open the sources of the flagged rows yourself, and find two quoted lines with Ctrl+F (Cmd+F on a Mac). This compares; it does not choose.

## The answer key

Written by the author before the run.

**Flags a correct reply must raise**

| Option | Claim in the notes | Result | What the source says |
| --- | --- | --- | --- |
| SlotPilot | No contract, cancel any time | Does not match | "£35 a month on a 12-month minimum term" |
| Bookwell | Takes no-show deposits | Could not open | The features page was not pasted, and `example.com` links do not open |
| Chairtime | The one most salons use | No source | Nothing was cited |

**The table a correct reply must show** (the wording may differ; the values may not)

| What matters | Bookwell | SlotPilot | Chairtime |
| --- | --- | --- | --- |
| Monthly price | £29 for one chair, £10 per extra chair | £35 | No monthly fee on Free; Plus is £19 |
| Card fee | 1.9% + 20p | 1.5% per transaction | 2.5% + 10p |
| No-show deposits | Flagged (could not open) | Yes, deposit at booking | On the Plus plan, £19 a month |
| Contract length | Monthly, 30 days' notice | 12-month minimum term | No contract |

Every value above has its exact words on pages 1 to 3, with the page's date: 3 November 2026,
"no date shown" and 20 October 2026. There is no recommendation.

**Fail if:** SlotPilot shows "no contract"; Bookwell deposits show "yes"; "most salons use" appears
as a fact; a quote is not word for word; one system is recommended.
