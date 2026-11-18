# Loop 0: baseline review, 17 November 2026

Scored by the builder (Claude) with the [game-review skill](../level-2-files/game-review/SKILL.md), before any
build. There was no game to play, only the plan and a draft prompt, so most items are scored on the
design as written. This is the starting point, not a fair test of a game.

**Score: 37/100. Not ready to show:** nothing can be played.

| # | Item | Score | Evidence |
| --- | --- | --- | --- |
| 1 | First ten seconds | 8/15 | The README says what the game is in one line and shows the scoring table. There is nothing to press |
| 2 | The core loop is fun | 9/15 | The rare-answer bet and the reveal board are designed. Five tiers plus a separate "accepted answers" list is more than a player needs to hold in mind |
| 3 | Feedback and feel | 2/15 | No micro-interactions are specified beyond "the score lands" |
| 4 | Fair scoring | 8/15 | The rules are stated and sensible. Nothing checks them |
| 5 | Usable by everyone | 2/10 | Not specified: keyboard, phone width, reduced motion and screen readers are not mentioned |
| 6 | Opponents feel alive | 0/10 | Not in the design. Level 2 is a shared sheet, which is admin, not play |
| 7 | Trash talk | 0/5 | Not in the design |
| 8 | Robust | 3/10 | "No outside images, fonts or links" is stated. What happens when the AI is unavailable is not |
| 9 | Honest and safe | 5/5 | The estimate is labelled; copyright and trademark care is written down |

## Fix first

1. **Build a playable Level 1 game file** that works offline with built-in packs (items 1, 2, 3, 8).
2. **Specify the feel:** timings, a count-up, tier colours, a Gem moment, a miss shake, reduced motion (item 3).
3. **Make Level 2 play, not admin:** a ladder of AI co-worker opponents with saved progress (item 6).
4. **Level 3 trash talk** after each answer, kind and switchable (item 7).
5. **Test the matcher** with a script: every tier, typos, plurals, aliases, short words (item 4).
6. **Accessibility pass:** keyboard, 390 px, reduced motion, live region (item 5).
7. **Graceful absence:** every AI, saving and party feature hides when unavailable (item 8).
8. **Simplify what the player sees:** five tier names and colours, no separate list to learn (item 2).

## Could not test

Everything: there is no game yet.
