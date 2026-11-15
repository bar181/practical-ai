# Project method: start here if you are an agent

You were asked to start a tool, or to continue one. This folder tells you the order to work in and
what must be true before you move on.

## The path

1. **Find the stage.** Read the tool's `README.md` status table and run
   `python3 tools/gates.py drafts/<tool>` from the repository root. A tool with no folder is at stage 1.
2. **Read that stage** in [`base/METHOD.md`](base/METHOD.md). Do only its work.
3. **Use the skill the stage names**, if there is one: [`landscape-review`](../../skills/landscape-review/)
   at stage 2, [`plan-writer`](../../skills/plan-writer/) for the plan, and
   [`project-builder`](../../skills/project-builder/) to run the whole sequence.
4. **Pass the gate.** A gate is a command that exits with 0, or a named person saying yes. Never
   mark a stage done because the work feels finished.
5. **Stop where the method says stop.** Stages 1, 4 and 7 end with a person's decision. Prepare
   everything, set out the decision, and wait.

## Rules that never bend

- Copy the scaffold with [`base/new_project.py`](base/new_project.py). Do not invent a layout.
- `base/` holds everything. A level holds only what it adds.
- One fact lives in one file. Anything that repeats it is generated from that file.
- A number in a document is counted by a script, or it carries the date a person checked it.
- Every status line says who has and has not tried the thing.
- Examples use invented data and say so.

## What you return

The files, and a note with four headings: what stage the tool is now at, which gates pass, what
you assumed, and the one decision you need from a person.
