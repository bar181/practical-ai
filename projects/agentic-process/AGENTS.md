# Agentic Process: instructions for agents

You are here because a person wants to turn an idea into a small tool, or to know what to do
next on one. This file is written for you. People start at the [README](README.md).

## The path

Take the first of these that you can do.

| You can | Do this |
| --- | --- |
| Load skills | Load [`level-2-files/agentic-process/SKILL.md`](level-2-files/agentic-process/SKILL.md) and follow it |
| Read one file | Read [`base/AI-INSTRUCTIONS.md`](base/AI-INSTRUCTIONS.md). It is the same process, as a coach |

## Where things are

| You need | Read |
| --- | --- |
| Why the project exists: the North Star, purpose and value | [`base/north-star.html`](base/north-star.html) |
| The course: modules, lessons, lecture decks with instructor notes | [`base/course.html`](base/course.html), written from `_build/course.py` |
| The nine steps, with a purpose, proof and prompt for each | [`base/PROCESS.md`](base/PROCESS.md). It is written by `_build/build.py` from `_build/steps.py`: change the source |
| The plan to fill in | The end of [`base/PROCESS.md`](base/PROCESS.md), and `base/plan.md` in every new project folder |
| A new project folder | Run `python3 projects/agentic-process/level-2-files/agentic-process/new_project.py <slug> "<Title>"` from the repository root. It makes `projects/<slug>/` from [the template](level-2-files/agentic-process/template/), with its own checks |
| How to test what you built | [`level-3-files/fresh-run/`](level-3-files/fresh-run/) |
| Checks to run from step 5 on | `python3 projects/<slug>/_build/checks/gates.py projects/<slug>`. It runs the new project's `_build/gates.json`. This project's own gates are in [`level-3-files/gates.json`](level-3-files/gates.json) |
| How to score the result | [`level-3-files/scorecard.md`](level-3-files/scorecard.md) |
| Three worked examples | [`base/examples/`](base/examples/): the unedited results of fresh sessions, one of them an agent working unattended |

## Output contract

After each step, three lines: what was decided, what you assumed, and the gate with pass, fail or open.
At the end: the plan on one page, the first version, and a note with four headings: Decided.
Assumed. Not checked. Test this next.

## Rules that never bend

1. One user and one job. A second job goes under "Next".
2. Stop at a failed gate. Fix the step before you go on. A gate you cannot answer without a person is open, not failed. `filled` fails by design until step 6.
3. Fix the folder layout at step 5 and do not change it.
4. Say what a result is: one you wrote yourself is a reference, one a fresh session made from the prompt is an example.
5. A person approves anything that is merged, posted, sent, paid or published.

## Known limits

- The skill has been run end to end by one agent working unattended. Treat the next runs as tests: see the status table in the README.
- Every time in the README and the guide is an estimate.
