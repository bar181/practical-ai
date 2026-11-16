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
| The nine steps and their gates | [`base/PROCESS.md`](base/PROCESS.md) |
| The plan to fill in | [`base/plan-template.md`](base/plan-template.md) |
| A new project folder | From the repository root, run `python3 projects/agentic-process/level-2-files/new_project.py <slug> "<Title>"`. It makes `projects/<slug>/` from [`level-2-files/template/`](level-2-files/template/) |
| How to test what you built | [`level-3-files/fresh-run/`](level-3-files/fresh-run/) |
| Checks to run from step 5 on | The new project's own `_build/gates.json`, with `python3 workshop/tools/gates.py projects/<slug>` from the repository root. This project's gates are in [`level-3-files/gates.json`](level-3-files/gates.json) |
| How to score the result | [`level-3-files/scorecard.md`](level-3-files/scorecard.md) |
| What went wrong last time | [Project one, step by step](base/examples/project-one-through-the-nine-steps.md) |

## Output contract

After each step, three lines: what was decided, what you assumed, and the gate with pass or fail.
At the end: the plan on one page, the first version, and a note with four headings: Decided.
Assumed. Not checked. Test this next.

## Rules that never bend

1. One user and one job. A second job goes under "Next".
2. Stop at a failed gate. Fix the step before you go on.
3. Fix the folder layout at step 5 and do not change it.
4. Say what a result is: hand-built is a reference, made by a chat from a prompt is an example.
5. A person approves anything that is merged, posted, sent, paid or published.

## Known limits

- The skill has not been run by a second agent. Treat the first runs as tests.
- The time comparisons in the README are one author's two projects, not a study.
