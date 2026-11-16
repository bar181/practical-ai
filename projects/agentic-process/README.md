# Agentic Process: from an idea to a tool people can try, in nine steps

<p align="center">
  <img src="_build/img/nine-steps.svg" width="800" alt="Animation: nine steps in a row, from scope to grow. A marker moves along them and stops at a gate after each step. The eighth step, build and test, is highlighted.">
</p>

<h3 align="center">Your AI can build almost anything. That is the problem.</h3>

**An AI agent will happily build the wrong thing three times.** Agentic Process is the order of
work that stops it: nine steps, a gate after each, and a test in a fresh chat, run before anyone
else sees the result. It is free. Use it in any chatbot (so far tested in Claude only),
hand it to your coding agent, or give the agent a spec and let it build the tool on its own.

**North Star:** a person, or an agent working alone, can take an idea or a spec to a tool that someone
else can use, without rebuilding it three times on the way.
**The spec:** [`workshop/plans/agentic-process/SPEC.md`](../../workshop/plans/agentic-process/SPEC.md) says what this
project is for, who it serves, and when version 1 is done. Everything here follows it.

## Try it in five minutes

### 1. Ask the coach about your own idea

Paste this into the chatbot you already use. Change the last line to a job you repeat.

<!-- prompt:start (written by _build/build.py) -->
```
Read the build coach at https://raw.githubusercontent.com/bar181/practical-ai/main/projects/agentic-process/base/AI-INSTRUCTIONS.md and follow it. If you cannot open it, say so and stop: do not make up a coach of your own.

My idea: every Monday I turn last week's sales notes into an email for my team. I want an AI to draft it.
```
<!-- prompt:end -->

It walks you through the steps one at a time, asks at most two questions in each, and ends with a
one-page plan and a first version you can test. For a small job like this one it offers a short
path: steps 1, 6 and 8 in full, steps 2 to 5 in a line each, step 7 folded into the test, and step 9 left open. You can start in five minutes; a full first run takes about an hour.

- **It cannot open the link?** Open [`base/AI-INSTRUCTIONS.md`](base/AI-INSTRUCTIONS.md), press
  **Raw**, select all, copy, and paste it into the chat. Then type: *Follow the build coach pasted
  above. My idea:* and your job.
- **Rather go one step at a time?** [The nine steps in detail](base/PROCESS.md) give each step a
  purpose, user stories, what to expect, proof you are done, and a prompt to paste.

### 2. Use it at your level

| You are | You use | You get |
| --- | --- | --- |
| **New to this** (Beginner) | The coach, pasted into any chatbot | A one-page plan and a first prompt you can test today |
| **Building with an agent** (Advanced) | [One skill folder](level-2-files/) to copy into your agent's skills. Works in any repository | A project folder with its own checks, the front page and the first version in place |
| **Running agents unattended** (Expert) | [Gates, the fresh-run test and the score sheet](level-3-files/) | Proof of what works, before a person spends time on it |
| **Building from a spec you already have** (Autopilot) | [One prompt](level-2-files/AUTOPILOT.md) for a coding agent or a scheduled task: your spec, guidance and where it should end up | A tested tool with a demo, gate results and what the agent assumed: a draft pull request, or a package for your chatbot project or Drive folder |

### 3. See it used

| Example | Level | What it is |
| --- | --- | --- |
| [A Monday email from sales notes](base/examples/monday-email.md) | Beginner, short path | The plan, the prompt and the note a new AI session made from one paragraph, unedited |
| [Deal updates for a sales team](base/examples/shared-tracker.md) | Beginner, all nine steps | The same for a team job, where the coach takes every step |
| [An agent working unattended](base/examples/unattended-run.md) | Advanced and Expert | A coding agent with only the skill folder, in a repository it had never seen: the plan, the tool it built, two fresh-session tests and its hand-back |

The people are invented. Each result was made by a session that had only this project's
instructions. Nobody has used what they made.

**If you are an AI agent:** follow [`AGENTS.md`](AGENTS.md).

## What you save

Every figure here is an estimate. Nobody outside the author has yet been timed.

| Who | Without the process | With it | You leave with |
| --- | --- | --- | --- |
| **Beginner** turning a repeated job into a reusable prompt | Trial and error in a chat until something works on the day. Next week you start again | About an hour the first time: the step times added up | A one-page plan, a prompt you can reuse and a test that tells you when it breaks |
| **Advanced** building a small tool with an agent | The agent builds fast and you find the shape by rebuilding. Folders move and links break | The layout is fixed before the first file, and the front page is written before the tool | A project folder that passes its own checks, with a front page a stranger can follow |
| **Expert** finding faults before users do | The author reviews their own work and passes it, because they know what they meant | Fresh sessions side by side, about ten minutes each | A numbered list of every place a stranger had to guess, and which ones change the result |

The larger gain is quality, not speed: a stranger's test finds the faults the author cannot see.

## The nine steps

| # | Step | Why it exists | The gate |
| --- | --- | --- | --- |
| 1 | [Scope](base/PROCESS.md#1-scope) | A tool that does one job gets finished | Can you say the job in one sentence? |
| 2 | [Reuse check](base/PROCESS.md#2-reuse-check) | The cheapest tool is the one you do not build | After what already exists, is there still something to build? If not, stop and write a guide to that thing |
| 3 | [Outside help](base/PROCESS.md#3-outside-help) | Build or buy is decided on purpose | Do you know what you would build and what you would buy? |
| 4 | [Cost](base/PROCESS.md#4-cost) | A tool people cannot afford to run is not finished | Does the first version cost nothing, or an amount you accept? |
| 5 | [Simplest design](base/PROCESS.md#5-simplest-design) | Moving files later breaks every link | Could a beginner draw it? |
| 6 | [Plan and front door](base/PROCESS.md#6-plan-and-front-door) | If the first screen cannot be written, the tool is not understood | Is the beginner version fully described? |
| 7 | [Review](base/PROCESS.md#7-review) | You cannot see your own gaps | Can someone else explain it back to you? |
| 8 | [Build and test](base/PROCESS.md#8-build-and-test) | A stranger finds what you cannot | Did a fresh session finish the job, and have you read what it tripped on? |
| 9 | [Grow](base/PROCESS.md#9-grow) | Small additions get reviewed. Big ones get waved through | Is the level below in use before you build the next? |

Each step in [the detailed page](base/PROCESS.md) also has a user story for each level, what to
expect, proof you are done, and a prompt to paste.

**Think of it as** building a deck in the garden: decide what it is for, check for a kit, price
the wood, draw it, have someone check the drawing, build the smallest platform you can stand on.

## What the AI does and what stays with you

| The AI does | You do |
| --- | --- |
| Asks the questions, searches for what exists, drafts the plan | Say no to anything outside the one job |
| Builds the first version and tests it in a fresh session | Read what the test tripped on and decide what to fix |
| Makes each addition | Approve each one, and use the tool yourself |

## Autopilot: a spec in, a finished tool out

The same nine steps, run by a coding agent without you guiding each one. You give it a spec, a few
lines of guidance, and where the tool should end up. It fills the plan from the spec and marks
every choice the spec did not make as assumed, checks what already exists, builds the tool and a
demo, tests them with fresh sessions, and hands back a note of what it decided and assumed. You
decide twice: when you write the spec, and when you review the result.

It builds any tool written as a workflow of steps. For a project on GitHub, the result is a draft
pull request. For someone who works in a chatbot, it is a package to save in a chatbot project or
a Drive folder: the instructions, any skills, a worked example and how to run it. For example, a
decision-support tool that researches a decision and writes a SWOT, laid out by
[Artifact Studio](../artifact-studio/) if you ask.

```
Use the agentic-process skill on autopilot.
Spec: workshop/plans/learning-system/README.md and the draft it links to
Guidance: a demo for developers first; invented data only; one command runs it
Deliver to: repository
Never merge, post or send anything.
```

[How to run it, and what comes back for each target](level-2-files/AUTOPILOT.md).

## Status

**Built on 16 November 2026, by its author.** Nobody else has used it yet.

| Part | Who has tried it |
| --- | --- |
| The coach | Fresh AI sessions, six runs in Claude. **Not yet run in ChatGPT, Gemini or Copilot, or by a person** |
| The skill folder | One agent working unattended, in an empty repository: it built and tested a first tool |
| Autopilot | **Not yet run end to end.** Written on 16 November 2026 |
| The links in this page | Open once this project is merged into the main branch |

Every round of testing, with the logs, is in [`_build/runs/`](_build/runs/README.md).

**Built a tool with it?** [Tell us in two minutes](https://github.com/bar181/practical-ai/issues/new?template=i-built-one.yml): the form records the three numbers the North Star is measured by.

## How it is laid out

```
agentic-process/
  README.md               this page
  AGENTS.md               the path for an AI agent
  base/                   Beginner: everything you need
    AI-INSTRUCTIONS.md    the build coach: paste into your chatbot
    PROCESS.md            the nine steps in detail, and the one-page plan to fill in
    examples/             unedited runs: two of the coach, one of an agent working unattended
  level-2-files/          Advanced: one skill folder, with the project template and its checks inside, and AUTOPILOT.md
  level-3-files/          Expert: gates, the fresh-run test and a score sheet
  _build/                 steps.py, the one source of the nine steps; build.py, which writes every generated file from it; runs/, the test logs; deferred/, end-user pages parked until version 1
```

## About the creator

<img src="../artifact-studio/_build/img/bradley-ross.jpg" width="130" alt="Bradley Ross, creator of Practical AI">

**Bradley Ross** is an agentic AI architect and developer for businesses of every size, from
start-up to enterprise. He builds and teaches practical AI.

**Training, questions or feedback:** [linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)

Free to use, change and share under Apache-2.0. See [`LICENSE`](LICENSE).
