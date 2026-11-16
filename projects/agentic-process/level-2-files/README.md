# Advanced: build a tool with an agent

For people who work with a coding agent. You get a skill that knows the nine steps, and a
folder to copy so every project starts in the same shape.

**Think of it as** a job site that is already marked out: the pegs are in, and the crew knows
the order of work.

## Set up, once

| What | Where | What it does |
| --- | --- | --- |
| The skill | [`agentic-process/SKILL.md`](agentic-process/SKILL.md) | Runs the nine steps and stops at each gate |
| The template | [`agentic-process/template/`](agentic-process/template/) | A project folder with the front page, the agent file, a plan, paste-in instructions and its own checks, all with the blanks marked |
| The script | [`agentic-process/new_project.py`](agentic-process/new_project.py) | Copies the template and fills in the name |

All three are in one folder, [`agentic-process/`](agentic-process/). Copy that folder into your
agent's skills (for Claude Code, `.claude/skills/` in your repository) and it works in any
repository: a new project carries its own checks and needs nothing else from here.

## Use it

1. Copy the folder [`agentic-process/`](agentic-process/) into your repository. For Claude Code:
   `git clone --depth 1 https://github.com/bar181/practical-ai /tmp/pai && mkdir -p .claude/skills && cp -r /tmp/pai/projects/agentic-process/level-2-files/agentic-process .claude/skills/`. For any other coding agent, put it anywhere and tell the agent to
   read `SKILL.md` in it first.
2. Say to your agent: "Use the agentic-process skill. The idea: turn a meeting transcript into a
   list of actions, each with an owner and a date. Start at step 1."
3. Answer its two questions for each step. It stops at every gate and waits for you.
4. At step 5 the agent makes the project folder and prints the command that checks it. Run that
   command yourself whenever you want to see where things stand.
5. After step 8, read the friction log from the fresh-session test before you fix anything.

## What changes compared with the Beginner level

| Beginner | Advanced |
| --- | --- |
| You paste the coach into a chat and it writes a plan and a first prompt | The agent makes the folder, the front page and the first version in your repository |
| You test by pasting into a fresh chat yourself | The agent runs the checks. You read the results |
| The plan lives in the chat | The plan lives in `base/plan.md`, beside the tool |

Tested on 16 November 2026: an agent with only this folder, in an empty repository, took an idea
to a tested first version. Its whole hand-back is [a worked example](../base/examples/unattended-run.md).
That run used the version before the `filled` and `built` gates; the current folder is checked
by a gate that makes a project, fills it and expects every check to pass. Nobody but the author
has built a real tool with it.
