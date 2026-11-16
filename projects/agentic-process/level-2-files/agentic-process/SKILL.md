---
name: agentic-process
description: Takes an idea for a small AI tool from a sentence to a first version someone else can try, in nine steps with a gate after each. Use when asked to "start a new tool", "plan a tool", "build this project", "follow the process", "set up a project folder", "what is the next step on this tool", or to review whether a tool is ready to share.
---

# Agentic process

You take a tool from an idea to a first version someone else can try. You do the drafting and
the building. A person makes the decisions. Nothing moves to the next step until its gate passes.

Think of it as a small building job with an inspector: frame before curtains, and a check at
every stage.

## Before you start

1. Read `PROCESS.md` in this project's `base/` folder if you can reach it. For each step it gives
   the purpose, what to expect, the proof you need before the gate, and a prompt. Use its proof
   list as the evidence for each gate. The table below is the same process, written for you.
2. If the person has a plan already, find which step it has reached. Start there, not at step 1.
3. Find the project folder. If there is none, make one from the template (step 5).

## The nine steps

| # | Step | You do | Gate |
| --- | --- | --- | --- |
| 1 | Scope | One user, one job, what is out, the wow, and one test with a specific input and a good result | The job fits in one sentence |
| 2 | Reuse check | Search for what already does it: built-in features, free tools, common practice. Record links and the date | Nothing existing does the whole job. If something does, stop and write a guide to it |
| 3 | Outside help | List paid options for what is left. Do not choose | Build-or-buy is clear for the first version |
| 4 | Cost | Every dependency of the first version with its price and limit | The first version has a known cost |
| 5 | Simplest design | Which assistant, where files live, what stays manual. From the repository root, make the folder from the template: `python3 projects/agentic-process/level-2-files/new_project.py <slug> "<Title>"`. It makes `projects/<slug>/` | The layout check passes |
| 6 | Plan and front door | Fill `plan-template.md`. Write the README's hook, its "Try it in five minutes" section and one worked example for each kind of request the beginner version handles, and at least one | The beginner version is fully described |
| 7 | Review | A person, or a fresh session that sees only the plan, explains it back | The reviewer's summary matches the plan |
| 8 | Build and test | Build the beginner version. Run the fresh-session test: `level-3-files/fresh-run/` | The fresh session finished the job. Its friction log has been read and the recurring points fixed |
| 9 | Grow | One addition at a time, each its own change request | The level below is in use |

## The folder every project uses

```
README.md          hook, one picture, the value, then "Try it in five minutes" as the first section
AGENTS.md          the path for an agent
LICENSE
base/              what a beginner needs: six things at most, plus examples/
level-2-files/     what a builder adds: a skill, a template. Only if it holds something usable
level-3-files/     what a team adds: checks, a server, a schedule. Only if it holds something usable
_build/            what makes or tests the tool: gates.json, and runs/ for fresh-session tests
```

Fix this layout at step 5. Do not change it later.

## Rules that never bend

- **One user, one job.** A second job goes under "Next" in the plan.
- **Stop at the gate.** If a gate fails, fix the step. Do not carry on and come back.
- **Say what a result is.** Hand-built is a reference. Made by a chat from a prompt is an example.
- **Status lines say who tried it.** "Built" is not "used".
- **Numbers shown to a reader are checked by a script, or not shown.**
- **One addition, one change request.**
- **A person approves anything that is merged, posted, sent, paid or published.**

## What you hand back after each step

Three lines: what was decided, what you assumed, and the gate with pass or fail. After step 8,
also hand back the friction log from the fresh-session test, unedited.

## Checks you can run

From the repository root:

- `python3 workshop/tools/check_project.py projects/<slug>` checks the layout
- `python3 workshop/tools/check_links.py .` checks every Markdown link
- `python3 workshop/tools/gates.py projects/<slug>` runs the project's own gates, listed in the
  project's `_build/gates.json`. The template starts it with two. Add one whenever a step
  produces something a command can check
