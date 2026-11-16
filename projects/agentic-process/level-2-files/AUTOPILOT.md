# Autopilot: from a spec to a draft pull request

You write the spec and the guidance. A coding agent with the `agentic-process` skill runs the nine
steps, builds a demo you can run, tests it with fresh sessions, and opens a draft pull request.
You review and merge. You do not guide each step.

**Think of it as** handing a drawing and a note to a builder you trust, and coming back to an
inspected first floor and a list of what they assumed.

**Status:** written on 16 November 2026. Not yet run end to end. The skill it uses has been run
once unattended, from an idea rather than a spec.

## The prompt

Paste this into a coding agent that has the skill (see [the Advanced level](README.md)), or save
it as the prompt of a scheduled task. Change the two lines in brackets.

```
Use the agentic-process skill on autopilot.
Spec: [workshop/plans/learning-system/README.md and the draft it links to]
Guidance: [who it is for, what the demo must show, anything to avoid]
Work in this repository. Open a draft pull request. Never merge.
```

## Where to run it

| Runner | How |
| --- | --- |
| Claude Code, now | Paste the prompt in a session in your repository |
| Claude Code, on a schedule or a GitHub event | Save the prompt as a routine at claude.ai/code/routines, with this repository attached |
| ChatGPT or Codex | Save the prompt as a scheduled task on a local project, or run it as a Codex task; the skill folder must be readable in the repository |
| Any agent that takes GitHub issues | Put the prompt in an issue and assign it to the agent |

## What comes back

A draft pull request on a branch named `build/<slug>` with:

- the new project folder, made from the template, with its plan filled from your spec;
- a demo: the beginner version, and if the first version needs code, a small working version
  with one command that runs it on invented data;
- the gate results, each pass or open with the reason;
- two fresh-session test logs, unedited;
- a note: Decided. Assumed. Not checked. Test this next.

Read "Assumed" first. That is where the agent made a choice your spec did not.

## Write a spec it can use

The more of these your spec answers, the fewer assumptions come back:

1. Who it is for, and the one job, in one sentence.
2. What is out of the first version.
3. One test: a specific input and what a good result looks like.
4. Where it runs: a chatbot, a script, or both.
5. What the demo must show.
