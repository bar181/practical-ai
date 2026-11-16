# Autopilot: from a spec to a finished tool

You write the spec and the guidance, and say where the tool should end up. A coding agent with
the `agentic-process` skill runs the nine steps, builds the tool and a demo, tests it with fresh
sessions, and hands it back. You review it and decide. You do not guide each step.

It builds any tool that can be written as a workflow of steps: a script in a repository, or a
chatbot tool such as one that researches a decision and writes a SWOT.

**Think of it as** handing a drawing and a note to a builder you trust, and coming back to an
inspected first floor and a list of what they assumed.

**Status:** written on 16 November 2026. Not yet run end to end. The skill it uses has been run
once unattended, from an idea rather than a spec.

## The prompt

Paste this into a coding agent that has the skill (see [the Advanced level](README.md)), or save
it as the prompt of a scheduled task. Change the lines in brackets.

```
Use the agentic-process skill on autopilot.
Spec: [workshop/plans/learning-system/README.md and the draft it links to]
Guidance: [who it is for, what the demo must show, anything to avoid]
Deliver to: [repository | chatbot | folder: the path or the Drive folder]
Never merge, post or send anything.
```

| Deliver to | You get |
| --- | --- |
| `repository` | A draft pull request on a branch named `build/<slug>`. You review and merge |
| `chatbot` | A folder, plus what to paste where: the instructions into a Claude Project, a ChatGPT Project or a Gemini Gem, and the skills and the example as project files |
| `folder` | The same folder, written to the place you named, such as a Drive folder your chatbot is connected to |

## Where to run it

| Runner | How |
| --- | --- |
| Claude Code, now | Paste the prompt in a session in your repository |
| Claude Code, on a schedule or a GitHub event | Save the prompt as a routine at claude.ai/code/routines, with this repository attached |
| ChatGPT or Codex | Save the prompt as a scheduled task on a local project, or run it as a Codex task; the skill folder must be readable in the repository |
| Any agent that takes GitHub issues | Put the prompt in an issue and assign it to the agent |

## What comes back

Whatever the target, the same parts:

- the project folder, made from the template, with its plan filled from your spec;
- the instructions the tool runs on, any skills, and how to install and run it;
- a demo: for a chatbot tool, a worked example a fresh chat made; for code, one command that
  runs it on invented data;
- optionally, results laid out by Artifact Studio, if your spec or guidance asks for it;
- the gate results, each pass or open with the reason;
- two fresh-session test logs, unedited;
- a note: Decided. Assumed. Not checked. Test this next.

The hand-back is in `_build/HANDBACK.md`, and in the pull request's description for a repository.
Read "Assumed" first. That is where the agent made a choice your spec did not.

## Write a spec it can use

The more of these your spec answers, the fewer assumptions come back:

1. Who it is for, and the one job, in one sentence.
2. What is out of the first version.
3. One test: a specific input and what a good result looks like.
4. Where it runs, and where it should be delivered: a repository, a chatbot project or a folder.
5. What the demo must show.
