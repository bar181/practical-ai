# Every test of Agentic Process, with its logs

All on 16 November 2026, all in Claude. Each test gave a fresh AI session only this project's
files and one request, and asked it to log every place it had to guess: BLOCKING if a different
guess would change the result, MINOR if not. Nothing in these folders has been edited, except
that machine paths were shortened.

## The coach, `base/AI-INSTRUCTIONS.md`

| Round | Folder | People (invented) | Blocking points per run |
| --- | --- | --- | --- |
| 1 | [`round-1/`](round-1/) | A kitchen-fitting owner; a teacher who builds with a coding agent | 4 and 5 |
| 2 | [`round-2/`](round-2/) | The same two, after the round 1 fixes | 4 and 3 |
| 3 | [`round-3/`](round-3/) | The kitchen-fitting owner (short path); a sales team member (all nine steps) | 2 and 3 |

The round 3 points are fixed and have not been tested again. Each round found new, smaller
points: no round repeated the list before it.

## A complete tool: decision support, `base/examples/decision-support/`

| Round | Folder | Message (invented) | Blocking, minor |
| --- | --- | --- | --- |
| 1 | [`decision-support/round-1/`](decision-support/round-1/) | A three-shop bakery asks whether to start office catering | 2, 13 |
| 2 | [`decision-support/round-2/`](decision-support/round-2/) | The same, after the round 1 fixes | 2, 11 |
| 3 | [`decision-support/round-3/`](decision-support/round-3/) | The same, after the round 2 fixes | 1, 11 |
| 4 | [`decision-support/round-4/`](decision-support/round-4/) | The same, after the round 3 fix | 0, 10 |
| 5 | [`decision-support/new-decision/`](decision-support/new-decision/) | A landscaper: rent, buy used or lease a truck | 5, 8 |
| 6 | [`decision-support/round-5/`](decision-support/round-5/) | The bakery, after one general rule | 3, 7 |
| 7 | [`decision-support/new-decision-2/`](decision-support/new-decision-2/) | The truck, after one general rule | 2, 8 |
| 8 | [`decision-support/round-6/`](decision-support/round-6/) | The bakery, judgement calls disclosed | 1, 11 |
| 9 | [`decision-support/new-decision-3/`](decision-support/new-decision-3/) | The truck, judgement calls disclosed | 1, 10 |

From run 8, a judgement call the instructions make the tool disclose counts as minor.

## A beginner reading the README

| Folder | Who (played by an AI session) | Blocking, minor |
| --- | --- | --- |
| [`beginner-walkthrough/`](beginner-walkthrough/friction.md) | An office manager who uses ChatGPT daily, starting at the README, then making a supplier-comparison tool | 3, 24, all three fixed and not re-tested |

## The skill folder, `level-2-files/agentic-process/`

| Run | Folder | What happened |
| --- | --- | --- |
| Inside this repository | [`skill-run/`](skill-run/SKILL-RUN.md) | A second agent took an invented idea to step 8. Two commands failed as written; 8 blocking points. All fixed |
| Unattended, in an empty repository | [`unattended/`](unattended/HANDBACK.md) | An agent with only the skill folder built a tool, prepared two tests, read their logs and fixed the tool. It logged 9 blocking points about the skill, all fixed. The tool's own tests: 3 blocking points each |

## Newcomer audits

A fresh session read the whole project as a beginner, a builder and a teacher, and ran the
builder's commands in an empty repository. The audit files are not kept here; their scores are.

| Audit | Beginner | Builder | Teacher | Blocking, confusing, minor |
| --- | --- | --- | --- | --- |
| First | 64 | 60 | 52 | 4, 16, 23 |
| Second, after the first audit's fixes | 60 | 70 | 58 | 4, 12, 19 |
| Third, after the second audit's fixes, scored as if merged | 72 | 52 | 70 | 1, 12, 16 |
| Fourth, after the third audit's fixes, scored as if merged | 72 | 76 | 74 | 1, 7, 20 |

Each audit found new faults, some introduced by the previous round's fixes: a bug that added four
nonsense headings to every plan (second audit), and a check that a finished project could never
pass (third audit, the cause of the builder's 52). Both are fixed, and a gate now fills a new
project and expects every check to pass. The fourth audit's one blocking point (the copy command
failed when `.claude/skills/` did not exist) and its keyboard points are fixed and not audited again.
