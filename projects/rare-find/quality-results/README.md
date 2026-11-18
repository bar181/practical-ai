# Quality results: Rare Find

**Built and machine-tested. As of 18 November 2026, users are testing it; their results are not in yet.**

## How it was tested

- **The automated playtest**, [`../_build/playtest.py`](../_build/playtest.py). It plays the built
  page in Chromium at 390 px (phone) and 1280 px, keyboard only, with reduced motion, with no Claude,
  and with a mock of Claude's answer check (`sample`). Last run, 18 November 2026: **82 of 82 checks
  passed**. They cover 60 spelling cases, the per-category points, hidden Gems, the daily calendar
  over 240 days, practice limits, Check with Claude and Check again, an unreachable Claude, the
  hosts, settings, the scorecard, challenge links, Back to start, the timer and phone width.
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

**Version 3, the simple version** (17 November 2026, after loop 5): a JSON bank of 125 prompts and a
JSON calendar, up to 100 practice prompts a day, one share link to the public web copy, and the
shared scoreboard, friends groups and live rooms removed at the owner's request. Checked by the
playtest (82 of 82); not re-scored by a reviewer. The 100 new prompts were drafted by Claude and
passed `check_packs.py`. Claude spot-checked a sample of them; no person has read every list yet.

## Who has and has not tried it

| Who or what | Tried? |
| --- | --- |
| The author, with Claude, building it | Yes |
| The automated playtest, with a mock of Claude | Yes |
| Fresh reviewer agents, with a mock of Claude | Yes, six loops |
| Users, in the Claude artifact or the web copy | **In progress** since 18 November 2026. No results yet |
| A screen reader, ChatGPT | **No** |

The answer lists are Claude's estimates, not a survey. The research behind the rules is in
[`../_build/PLAN.md`](../_build/PLAN.md).
