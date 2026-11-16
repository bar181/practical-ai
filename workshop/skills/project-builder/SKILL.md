---
name: project-builder
description: Takes a tool in the practical-ai repository from an idea to something another person can use, through nine stages with a gate after each. Use when asked to start a new tool, to continue or finish one in drafts/, to convert an older draft to the base-plus-levels layout, or to say what stage a tool is at and what to do next.
---

# Project builder

You build a tool the way this repository builds tools: in nine stages, with a gate after each.
The gates decide when a stage is done. You do not.

**Think of it as** a relay. You carry one stage, pass its gate, and hand over. Three of the
handovers are to a person.

## Before you start

- The stages are in `workshop/drafts/project-method/base/METHOD.md`. Read the stage you are on, not all nine.
- The lessons behind them are in `workshop/drafts/project-method/base/LESSONS.md`. Read it once.
- Run every command from the repository root.

## Steps

1. **Find the stage.** If `workshop/drafts/<tool>/` does not exist, the tool is at stage 1: run
   `python3 drafts/project-method/base/new_project.py <slug> "<Title>"`. Otherwise read
   `docs/progress.md` and the status table in its `README.md`, and run `python3 workshop/tools/gates.py drafts/<tool>`.
2. **Do that stage's work, and only that.** The table below says what it is and which skill helps.
3. **Run the gate.** If it fails, read what it printed, fix the cause and run it again. Three tries
   at most. Then stop and report.
4. **Stop at a person's decision.** After stages 3, 5 and 9, set out the decision and wait.
5. **Leave a handover.** Update `docs/progress.md` and the status table in the tool's `README.md`
   before you report. The next session starts by reading them and running the gates.

| Stage | Work | Skill | Gate |
| --- | --- | --- | --- |
| 1. Understand | The top of `docs/north-star.md`: who, the one job, a North Star | none | The person who asked says it is true |
| 2. Research | What exists, with links and dates. Three to six influences on the page | `landscape-review` | Every source dated. The decision written down |
| 3. Scope | In, out, the levels, a "done when" line for each item, where data lives | `plan-writer` for a full plan | A person approves the page. **Stop** |
| 4. Plan | `README.md`, `AGENTS.md`, `gates.json` from the "done when" lines, `docs/rubric.md` | none | `python3 workshop/tools/check_project.py drafts/<tool>` |
| 5. Prove | One request to one finished output | the tool's own | A person says it is what they wanted. **Stop** |
| 6. Build | One source file. Generate what repeats it. Then add content, a piece at a time | none | `python3 workshop/tools/gates.py drafts/<tool>` |
| 7. Verify | Worked examples. A script that uses only the public surface. Every request run | none | The example and agent gates pass |
| 8. Score | Score each rubric line out of 100 with one sentence of evidence | none | Every line scored. No evidence means 40 or less |
| 9. Close | The closing checklist: gates, stale documents, leftovers, lessons, the priority list, a report | none | `python3 workshop/tools/gates.py drafts/<tool> --all`. A person says close. **Stop** |

## Rules that never bend

- Never change a gate to make it pass. If a gate is wrong, say so and ask.
- Never change the rubric after stage 4.
- Nothing private goes in the repository. A tool that stores things keeps its store outside it.
- Never mark a stage done without running its gate in this session.
- `base/` holds everything. A level holds only what it adds. If you are copying, it belongs in the base.
- One fact lives in one file. What repeats it is generated.
- A number in a document is counted by a script, or carries the date a person checked it.
- Retired work moves to `workshop/plans/archive/` with a line saying what replaced it. Do not delete it.
- Every status line says who has and has not tried the thing. "Built" is not "used".

## Converting an older draft

Run `python3 workshop/tools/check_project.py drafts/<tool>`. It lists what is left. Follow the table at the
end of `workshop/drafts/project-method/base/LESSONS.md`, and start from stage 1: write the North Star page
first, because the older drafts were written as course material and this repository holds products.

## What you return

A note with four headings: the stage the tool is now at, which gates pass, what you assumed, and
the one decision you need from a person.
