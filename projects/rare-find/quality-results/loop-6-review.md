# Loop 6: blind before-and-after review, answer moments

**18 November 2026.** A fresh reviewer agent, with no access to the repository, played two builds
named A and B. It was not told which was newer. **A was the new build** (answer moments, outcome
dots, Gem reveal, first version), **B was the build on `main`**. It used the same five prompts (the
17 November daily game), the same answers, the game-review rubric, and a mock of Claude. Nobody
played it in the real Claude artifact runtime.

| Build | Score | Verdict |
| --- | --- | --- |
| A, new | 91 | Ready to share |
| B, before | 84 | Ready for friendly testers |

**Which would you replay?** A: "Next works about 3x sooner on every prompt", and the coloured dots
and emoji challenge grid make the day readable at a glance.

**Which result do you remember?** B's confetti Gem: "the only moment in either build that feels
like a celebration; A's Gem is polite by comparison."

**What changed because of it:** the Gem reveal was made the event. It now sits right under the
score, drops in, throws a light burst and a gold flash, sheds ten fragments, and sends +100 to the
score, all inside 600 ms. A tab switch now clears an old toast. Loop 7 reviews that build.

## The reviewer's report, unedited

| # | Item | A | B | Evidence |
|---|---|---|---|---|
| 1 | First ten seconds | 14 | 14 | Identical home: one line ("Name a right answer nobody else thinks of…") and one big yellow "Play today's game". |
| 2 | Core loop is fun | 13 | 12 | Both have timer ring, top-ten reveal and secret Gems; A's tier-coloured dots (grey, purple, diamond, red) turn the round into a story, B's are all plain yellow. |
| 3 | Feedback and feel | 13 | 11 | Result appears in 15 to 50 ms in both; A's score counts up in about 210 ms and Next is live at 130 to 160 ms, B's takes about 300 ms and Next is locked until about 460 to 476 ms. B's Gem is the bigger event. |
| 4 | Fair scoring | 14 | 13 | Scores match the table and typos were forgiven, but "Srek" was not; B's Unit 7 says "Correctness: confirmed" when only the room allowed "Zxqv thing". |
| 5 | Usable by everyone | 9 | 8 | Both work keyboard-only, pass a rough contrast check and respect reduced motion; A's dots carry an aria-label, B's are aria-hidden. |
| 6 | Others feel present | 9 | 8 | Four distinct hosts, a saved week and streak, an estimated spread labelled "Not real players"; A's share text adds an emoji grid. |
| 7 | Commentary | 5 | 4 | Short and about the answer; the off switch works; B's "Correctness: confirmed" line is false. |
| 8 | Robust | 9 | 9 | No errors, works offline, the Claude check hides or fails honestly; party mode not tested. |
| 9 | Honest and safe | 5 | 5 | Both say "Popularity is the AI's estimate, not a survey" and use original characters. |
| | **Total** | **91** | **84** | |

| Moment | A | B | Lands better |
|---|---|---|---|
| Popular (Eagle) | Grey badge pops, a "+25" chip by the total, grey dot, "1. Eagle · Yours 25" highlighted; Next at 157 ms | Same badge, gold row with no "Yours", yellow dot; Next at 476 ms | A |
| Good find (Bagel) | Purple badge, "+80" chip, purple dot, row "Good find · 80" | Purple badge, gold row, yellow dot | A |
| Unlisted plus check | Dashed "Not on our list"; "We allow it" beside Next | Same, with a full-width "We allow it"; the host then claims "Correctness: confirmed" | A |
| Gem (Sepak takraw) | Diamond banner "Gem! +100", a floating "+100"; the total holds about 0.6 s | Big "GEM!" banner and full-screen confetti | **B** |
| Miss (time-out) | Red badge, "Out of time", red dot | Same, yellow dot | Even, A slightly |

Bugs it reported: in B, the host line after a room allow claims "Correctness: confirmed", and Next
is locked for about 460 ms and for a whole Claude check. In A, a late verdict changes the total
during the next prompt (a toast says so). In both, one "We allow it" gives 80 to nonsense, the
rules say spelling slips are forgiven yet "Srek" is not, and a copy toast could cover the
scorecard.

Not tested: real Claude, party mode, a real screen reader, a challenge link on another device.
