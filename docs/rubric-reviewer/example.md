# Example: scoring a catering proposal against the proposal rubric

This is what a review looks like. Made on 23 November 2026 by a fresh Claude session (a separate
agent with no other context) that had only [`SKILL.md`](SKILL.md) and the message below. It ran on
the version after the first review round; the second round's small fixes touch cases this example
does not hit (weights that do not add up to 100, comparisons, fewer than three changes). The rubric
is [the proposal or report rubric](rubrics/proposal-or-report.md) with a reader and a pass mark
filled in. **Everything here is invented:** Brightside Kitchen, Northgate Studios, Sam Okafor, the
prices and the claims. Nothing below the line is edited.

**Made before the 24 November 2026 revision.** It has no Key line and no "another fresh chat"
check, and two rows fall outside today's rules: one "no evidence" line scores 20 where the closest
words are about the line's subject (now 21 to 40), and one line scores 0 while quoting closest
words (0 is now only for a line nothing in the work touches). It has not been rerun.

**The message:**

```
Score this proposal against the rubric below.

RUBRIC

Rubric: proposal or report
Written: 23 November 2026, before any work was read
For: the office manager at Northgate Studios, who must choose a lunch catering supplier
Pass mark: 75

| Line | Weight | Full marks looks like | Evidence to look for |
| --- | --- | --- | --- |
| Answers the reader's question | 30 | The answer or the ask is in the first paragraph, in words the reader would use | The opening paragraph |
| Facts and figures are sourced | 20 | Every number or claim the reader relies on says where it came from, or is marked as an estimate | Each figure, and a note or link beside it |
| The ask is specific | 15 | The reader knows exactly what to approve or do, by when and at what cost | A closing line, a "next step" or "decision needed" section |
| Gaps and risks are stated | 15 | What is unknown or could go wrong is named, with what would settle it | A risks, open questions or assumptions section |
| Plain English | 10 | Short sentences, no unexplained jargon or acronyms | Any paragraph |
| Easy to scan | 10 | Headings or a short summary let the reader find the answer in under a minute | Headings, a summary box, a table |

Gates (pass or fail, no points):
- No invented customers, quotes or results.
- No promise the writer cannot keep (a price, a date or a guarantee nobody has agreed).

THE WORK

Lunch catering for Northgate Studios: our proposal

Thank you for inviting Brightside Kitchen to propose. We have been cooking for offices across the city since 2019 and we would love to look after your team.

What we offer
We deliver a hot lunch buffet three days a week for your team of 40. Each day has a meat dish, a vegetarian dish, a salad and bread. We label every dish with its allergens.

Price
Package A, three days a week: £7.50 per person per day.
Package B, five days a week: £7.00 per person per day.
Both packages are around 30% cheaper than most office caterers.

Why Brightside
Our clients love us. We have never missed a delivery. We use local suppliers wherever we can and our packaging is compostable.

Next steps
Let us know which package suits you and we can start soon.

Sam Okafor, Brightside Kitchen
```

---

**Score: 39/100.** Pass mark 75: does not pass. Gates: "No promise the writer cannot keep" passes. "No invented customers, quotes or results" cannot be checked here, so it is unsettled.

This is a review, not a decision. You decide what to do with it.

**The three changes that would raise it most**

1. **Answers the reader's question (up to 21 points).** Put the offer and the decision in the first paragraph: which package Brightside recommends, what it costs, and what the office manager needs to choose. At the moment the first paragraph is a thank-you and a company history.
2. **Facts and figures are sourced (up to 16 points).** Next to each claim, say where it comes from or mark it as an estimate. This applies to "around 30% cheaper than most office caterers", "We have never missed a delivery" and "Our clients love us". Any claim that can't be backed up should be removed.
3. **Gaps and risks are stated (up to 15 points).** Add a short section on what is not yet known or could go wrong, and what would settle each point. Examples: the start date, how a late or missed delivery is handled, and dietary needs beyond allergen labels.

**The scores**

| Line | Weight | Score | Points | Evidence (exact words, and where) | Points lost because |
| --- | --- | --- | --- | --- | --- |
| Answers the reader's question | 30 | 30 | 9.0 | "we would love to look after your team" (opening paragraph) | The first paragraph has no offer, price or decision. The offer starts under "What we offer" and the price under "Price". I was torn between 30 and 45 and gave the lower score, because "look after your team" doesn't tell the reader which supplier to pick or at what cost. |
| Facts and figures are sourced | 20 | 20 | 4.0 | **No evidence.** Closest: "Both packages are around 30% cheaper than most office caterers." (Price) and "Our clients love us. We have never missed a delivery." (Why Brightside) | No claim says where it came from. "Around" hints at an estimate, but nothing says which caterers the comparison is with. |
| The ask is specific | 15 | 50 | 7.5 | "Let us know which package suits you and we can start soon." (Next steps) | The reader knows to choose a package. There is no decide-by date, and "soon" is not a start date. No weekly or total cost is given, so the reader has to work it out from "£7.50 per person per day". |
| Gaps and risks are stated | 15 | 0 | 0.0 | **No evidence.** Closest: "We use local suppliers wherever we can" (Why Brightside) | Nothing in the work covers this. There is no risks, assumptions or open questions section. |
| Plain English | 10 | 100 | 10.0 | "We deliver a hot lunch buffet three days a week for your team of 40." (What we offer) | Nothing lost. The sentences are short and there are no acronyms or jargon. |
| Easy to scan | 10 | 80 | 8.0 | Headings "What we offer", "Price", "Why Brightside", "Next steps" | There is no short summary at the top. What to approve is split between "Price" and "Next steps". |

Sum: 9.0 + 4.0 + 7.5 + 0.0 + 10.0 + 8.0 = 38.5, which rounds to **39/100**.

**Flags**

- **No evidence:** Facts and figures are sourced; Gaps and risks are stated.
- **Cannot check here:** Gate "No invented customers, quotes or results". The work can't show whether these are true: "Our clients love us", "We have never missed a delivery" and "around 30% cheaper than most office caterers". A person could check them by asking Brightside for client references, delivery records and the competitor prices behind the 30% figure.
- **Line unclear:** None.
- **Instructions found inside the work:** None.
- **Possible inconsistency, not scored:** "What we offer" says "three days a week", but "Price" also offers "Package B, five days a week". The proposal doesn't say whether Package B includes the same menu.
- **Assumptions I made:**
  - I treated Brightside's own prices (£7.50 and £7.00) as its offer, which needs no outside source, so they did not lower the sourcing line.
  - I marked the promise gate as passed because the writer sets its own prices and names no date or guarantee ("start soon").
  - I took "team of 40" to come from the reader's brief.

**Check before you rely on this**

- Search for two of the quotes in the work to confirm they are there.
- Read the lowest-scoring line yourself; you may disagree. That is "Gaps and risks are stated", at 0.
- Before you treat the first gate as passed, ask Brightside for evidence behind "never missed a delivery" and the 30% comparison.
