# Advanced: build a tool with an agent

For people who work with a coding agent. You get a skill that knows the nine steps, and a
folder to copy so every project starts in the same shape.

**Think of it as** a job site that is already marked out: the pegs are in, and the crew knows
the order of work.

## Set up, once

| What | Where | What it does |
| --- | --- | --- |
| The skill | [`agentic-process/`](agentic-process/) | Add the folder to your agent's skills. It runs the nine steps and stops at each gate |
| The template | [`template/`](template/) | A project folder with the front page, the agent file, a plan and paste-in instructions, all with the blanks marked |
| The script | [`new_project.py`](new_project.py) | Copies the template and fills in the name |

## Use it

1. From the repository root, make the folder: `python3 projects/agentic-process/level-2-files/new_project.py meeting-notes "Meeting notes to actions"`
2. Say to your agent: "Use the agentic-process skill. The idea: turn a meeting transcript into
   decisions, tasks and a follow-up. Start at step 1."
3. Answer its two questions for each step. It stops at every gate and waits for you.
4. After step 8, read the friction log from the fresh-session test before you fix anything.

## What changes compared with the Beginner level

| Beginner | Advanced |
| --- | --- |
| You paste the coach into a chat and it writes a plan and a first prompt | The agent makes the folder, the front page and the first version in your repository |
| You test by pasting into a fresh chat yourself | The agent runs the checks. You read the results |
| The plan lives in the chat | The plan lives in `base/plan.md`, beside the tool |

The template has been used once, to make a trial folder that passes the layout check. No tool has
been built from it yet by anyone but its author.
