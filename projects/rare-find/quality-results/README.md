# Quality results: Rare Find

**Built and machine-tested; not yet played by people or in the real Claude artifact runtime.** The
status at a glance is in [`status-report.html`](status-report.html), a one-page report.

## How it was tested

- **The automated playtest**, [`../_build/playtest.py`](../_build/playtest.py). It plays the built
  page in Chromium at 390 px (phone) and 1280 px, keyboard only, with reduced motion, with no Claude,
  and with a mock of Claude's artifact runtime (`sample`, `db`, `user`, `room`). Last run, 17
  November 2026: **80 of 80 checks passed**. They cover 60 spelling cases, the per-category points,
  hidden Gems, today's prompts over 120 days, Check with Claude and Check again, an unreachable
  Claude, the hosts, settings, the scorecard, the shared scoreboard, friends groups, live play,
  Back to start, the timer and phone width.
- **The review skill**, [`../level-2-files/game-review/SKILL.md`](../level-2-files/game-review/SKILL.md).
  At the end of each loop a fresh reviewer agent that had not seen the game played it and scored it
  out of 100.

## Scores by loop

| Loop | Version | Score | Verdict | Review |
| --- | --- | --- | --- | --- |
| 0 | The plan only | 37 | Not ready: nothing to play | [loop-0-baseline.md](loop-0-baseline.md) |
| 1 | 1, office ladder | 68 | Not ready, but close | [loop-1-review.md](loop-1-review.md) |
| 2 | 1 | 80 | Ready for friendly testers | [loop-2-review.md](loop-2-review.md) |
| 3 | 1 | 84 | Ready for friendly testers | [loop-3-review.md](loop-3-review.md) |
| 4 | Interim: rank points, Claude check | 80 | Ready for friendly testers | [loop-4-review.md](loop-4-review.md) |
| 5 | 2, daily game and scorecard | 71 | Ready for friendly testers, only just | [loop-5-review.md](loop-5-review.md) |

**After loop 5**, at the owner's request: challenge codes, a prompts-per-game setting (5, 10 or party
mode) and an edit-access note. Then all five top problems from the loop 5 review were fixed: totals
that could disagree, a "Check again" that skipped Claude, real words that scored, codes trusted
blindly, and "saved" messages that were not true. The automated playtest checks every fix (80 of
80). No reviewer has re-scored the fixed build yet.

## Who has and has not tried it

| Who or what | Tried? |
| --- | --- |
| The author, with Claude, building it | Yes |
| The automated playtest, with a mock of Claude | Yes |
| Fresh reviewer agents, with a mock of Claude | Yes, six loops |
| The real Claude artifact runtime | **No.** The artifact is published with its capabilities declared; nobody has played it there |
| Real players, friends on other accounts, a multi-device live game, a screen reader, ChatGPT | **No** |

The answer lists are Claude's estimates, not a survey. The research behind the rules is in
[`../_build/PLAN.md`](../_build/PLAN.md).
