# Loop 7: second blind review, after the bigger Gem

**18 November 2026.** A second fresh reviewer agent, with no access to the repository, played two
builds named A and B. It was not told which was newer. This time the labels were swapped: **B was
the new build** (with the bigger Gem from loop 6), **A was the build on `main`**. It used the same
five prompts and answers, the game-review rubric, video frames every 50 ms to judge feel, and a
mock of Claude. Nobody played it in the real Claude artifact runtime.

| Build | Score | Verdict |
| --- | --- | --- |
| B, new | 86 | Ready to share, just |
| A, before | 82 | Ready for friendly testers |

**Which would you replay?** B, the new build: the dots show how each round went, Next is ready four
times sooner, and the share grid gives you something to post.

**Which result do you remember?** B's Gem, from the new build: "the diamond, then '+100' flying up
into the score total. A's confetti is the bigger party on a shared screen, but it is generic."

**Fixed after this review, checked by the playtest, not re-scored:** the points counter could show
"-1" for one frame (a frame time just before the start; now clamped, with a playtest check), and
"Claude could not be reached" no longer appears twice.

**Left as they are, for the owner to decide:** a room-allowed answer shows as a plain Good find in
the share grid and the scorecard (the end screen says "Allowed 80"); the flying +100 briefly
overlaps "pts" as it lands; reaching "We allow it" by keyboard takes several Tab presses.

## The reviewer's report, unedited

| Item | A, before | B, new |
|---|---|---|
| First ten seconds | 13: one line and a big "Play today's game" button | 13: identical home |
| Core loop | 12: the 30 s ring and "5 Gems are hidden" create tension; the reveal pays off | 12: same loop, plus the top-ten row tagged "Yours 25" |
| Feedback and feel | 11: result in 8 to 24 ms, points count up in about 330 ms, full-screen confetti; Next locked about 450 ms; dots all yellow; a late verdict changes the score silently | 13: result in 16 to 18 ms, Next locked about 120 ms, tier dots, a staged Gem of about 1 s; points off for the "-1" glitch and the overlap at the total |
| Fair scoring | 12: totals match; one "We allow it" gives 80, labelled "Allowed 80"; the late judge moved the score with no notice | 13: same rules; a late verdict shows a toast; but the share grid and scorecard list the room-allowed answer as a plain Good find |
| Usable by everyone | 8: keyboard works, results announced, reduced motion instant, contrast 9.1:1 or better; dots have no aria-label | 9: same, and dots are labelled "Round results: 1, Gem; 2, Gem; 3, now playing…" |
| Others feel present | 8 | 8: plus the share grid |
| Commentary | 4 | 4 |
| Robust | 9: no console errors, clean fallbacks | 9: the same |
| Honest and safe | 5 | 5 |
| **Total** | **82** | **86** |

| Moment | Before | New | Better |
|---|---|---|---|
| Popular | Points count up, Eagle row outlined | Same, plus "Yours 25", but "-1" shows for a frame | Tie |
| Good find | "80" | "Good find · 80", purple dot | New |
| Unlisted plus check | "We allow it" inside the card | "We allow it" beside Next; dashed row | New |
| Gem | Confetti for about 900 ms | The gem drops in, "GEM! +100", sparkles, +100 flies to the total | New, more crafted; before is louder |
| Miss | Red "Miss" | The same, plus a red dot | Tie |

Bugs it reported: the "-1" frame and the +100 overlap (new build, both fixed or noted above); a
late verdict with no notice (before); in both builds, one "We allow it" turns nonsense into 80,
"Claude could not be reached" shows twice when the judge fails, and "We allow it" is five Tab
presses away. The console was empty for both builds in every run.

Not tested: real Claude, true offline, a spoken screen reader, the commentary-off switch, party
mode, a friend's code coming back, and touch on a real phone.
