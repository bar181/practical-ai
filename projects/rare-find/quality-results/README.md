# Quality results: Rare Find

**Built and machine-tested; not yet played by people or in the real Claude artifact runtime.** The
status at a glance is in [`status-report.html`](status-report.html), a one-page report.

## How it was tested

Two tools, both in this project:

- **The automated playtest**, [`../_build/playtest.py`](../_build/playtest.py). It plays the built
  page in Chromium at desktop and phone width, keyboard only, with reduced motion, with no Claude,
  and with a mock of Claude's artifact runtime (`sample`, `db`, `user`, `room`). Last run, 17
  November 2026: **51 of 51 checks passed**, including 60 spelling cases, rank points, the Claude
  answer check ("big hero 5" counts as Big Hero 6 for 80), Back to start on every screen, the
  timer, saving, the ladder and a party room.
- **The review skill**, [`../level-2-files/game-review/SKILL.md`](../level-2-files/game-review/SKILL.md).
  At the end of each loop a fresh reviewer agent that had not seen the game played it and scored it
  out of 100.

## Scores by loop

| Loop | Score | Verdict | Review |
| --- | --- | --- | --- |
| 0, the plan only | 37 | Not ready: nothing to play | [loop-0-baseline.md](loop-0-baseline.md) |
| 1 | 68 | Not ready, but close | [loop-1-review.md](loop-1-review.md) |
| 2 | 80 | Ready for friendly testers | [loop-2-review.md](loop-2-review.md) |
| 3 | 84 | Ready for friendly testers | [loop-3-review.md](loop-3-review.md) |
| 4 | {{L4}} | {{L4V}} | [loop-4-review.md](loop-4-review.md) |

Changes between loop 3 and loop 4, at the owner's request: points by rank (25 to 70 down the top
ten, 80 beyond it, 100 for a Gem), "We allow it" asks Claude to check the answer, Back to start on
every screen, 16 prompts, and a stronger spelling rule.

## Who has and has not tried it

| Who or what | Tried? |
| --- | --- |
| The author, with Claude, building it | Yes |
| The automated playtest, with a mock of Claude | Yes, 51 of 51 |
| Fresh reviewer agents, with a mock of Claude | Yes, five loops |
| The real Claude artifact runtime | **No.** The artifact is published and its capabilities declared; nobody has played it there |
| Real players, a real multi-device party, a screen reader, ChatGPT | **No** |

The answer lists are Claude's estimates, not a survey. The research behind the rules is in
[`../_build/PLAN.md`](../_build/PLAN.md).
