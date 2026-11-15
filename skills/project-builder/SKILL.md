---
name: project-builder
description: Takes a tool in the practical-ai repository from an idea to something another person can use, through seven stages with a gate after each. Use when asked to start a new tool, to continue or finish one in drafts/, to convert an older draft to the base-plus-levels layout, or to say what stage a tool is at and what to do next.
---

# Project builder

You build a tool the way this repository builds tools: in seven stages, with a gate after each.
The gates decide when a stage is done. You do not.

**Think of it as** a relay. You carry one stage, pass its gate, and hand over. Three of the
handovers are to a person.

## Before you start

- The stages are in `drafts/project-method/base/METHOD.md`. Read the stage you are on, not all seven.
- The lessons behind them are in `drafts/project-method/base/LESSONS.md`. Read it once.
- Run every command from the repository root.

## Steps

1. **Find the stage.** If `drafts/<tool>/` does not exist, the tool is at stage 1: run
   `python3 drafts/project-method/base/new_project.py <slug> "<Title>"`. Otherwise read the status
   table in its `README.md` and run `python3 tools/gates.py drafts/<tool>`.
2. **Do that stage's work, and only that.** The table below says what it is and which skill helps.
3. **Run the gate.** If it fails, read what it printed, fix the cause and run it again. Three tries
   at most. Then stop and report.
4. **Stop at a person's decision.** After stages 1, 4 and 7, set out the decision and wait.
5. **Update the status table** in the tool's `README.md` before you report.

| Stage | Work | Skill | Gate |
| --- | --- | --- | --- |
| 1. Purpose | Fill in `docs/purpose.md` | none | A person approves it. **Stop** |
| 2. Reuse check | What exists, with dated sources, and a decision | `landscape-review` | Every source dated. Decision written in `docs/purpose.md` |
| 3. Skeleton | `README.md`, `AGENTS.md`, and the gates the tool must pass | `plan-writer` for the plan | `python3 tools/check_project.py drafts/<tool>` |
| 4. One real example | One request to one finished output | the tool's own | A person says it is what they wanted. **Stop** |
| 5. One source, then breadth | One source file. Generate what repeats it. Then add content | none | `python3 tools/gates.py drafts/<tool>` |
| 6. Play the user and the agent | Worked examples. A script that uses only the public surface | none | The example and agent gates pass |
| 7. Ship honestly | Status table, scored self-review, short report | none | `python3 tools/gates.py drafts/<tool> --all`. A person approves. **Stop** |

## Rules that never bend

- Never change a gate to make it pass. If a gate is wrong, say so and ask.
- Never mark a stage done without running its gate in this session.
- `base/` holds everything. A level holds only what it adds. If you are copying, it belongs in the base.
- One fact lives in one file. What repeats it is generated.
- A number in a document is counted by a script, or carries the date a person checked it.
- Retired work moves to `plans/archive/` with a line saying what replaced it. Do not delete it.
- Every status line says who has and has not tried the thing. "Built" is not "used".

## Converting an older draft

Run `python3 tools/check_project.py drafts/<tool>`. It lists what is left. Follow the table at the
end of `drafts/project-method/base/LESSONS.md`, and start from stage 1: write the purpose page
first, because the older drafts were written as course material and this repository holds products.

## What you return

A note with four headings: the stage the tool is now at, which gates pass, what you assumed, and
the one decision you need from a person.
