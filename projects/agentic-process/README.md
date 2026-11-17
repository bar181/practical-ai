# Agentic Process: turn work you repeat into an AI tool you can run again

<p align="center">
  <img src="_build/img/nine-steps.svg" width="800" alt="Animation: nine steps in a row, from scope to grow. A marker moves along them and stops at a check after each step.">
</p>

Start with one real job, such as drafting a weekly update or comparing suppliers. Leave with four
files: a **workflow card** (what goes in, the steps, what comes out, what a person checks),
**instructions** your chatbot runs, a **worked example**, and a short **setup guide**. Next time,
bring fresh input and run the same workflow. It is free and works in the chatbot you already use.

**Why bother:** misunderstandings are caught before they become rework. You decide what goes in,
what good looks like and what a person checks, once, instead of explaining it again every week.

**North Star:** someone can try a worked example, adapt it to their own task, and run it again
without needing the original conversation. [The spec](../../workshop/plans/agentic-process/SPEC.md)
says what this project is for and when it is done.

## Try it: a finished tool, in 5 minutes

**Decision support:** describe your business once, ask a business question, and get research
with sources, the options compared, a recommendation, a SWOT and a two-minute brief.

1. Open a new chat in ChatGPT, Claude or Gemini. Web search helps: without it, the tool says so
   and lists what to look up instead of researching.
2. Open the tool's instructions,
   [`decision-support/AI-INSTRUCTIONS.md`](base/examples/decision-support/AI-INSTRUCTIONS.md),
   press **Raw**, and copy all of it into the chat. Do not send yet.
3. Under it, in the same message, paste this sample from an invented bakery, and send:

```
Business profile: Harbour Lane Bakery. We sell bread, pastries and coffee to walk-in customers. Three shops in Hamilton, Ontario, 22 staff, about 1.4 million dollars in sales a year. Goals for the next twelve months: grow sales 10 percent, raise weekday afternoon sales, keep the team from burning out. Limits: up to 25,000 dollars to invest, no new building, the head baker already works six days. Risk: medium. My business partner has a say in big decisions.

My question: should we start a weekday catering service for offices near our shops?
```

**What you get,** in a few minutes: research with sources, the options scored, a recommendation,
a SWOT, a short brief and a list of what to check. Compare it with
[the finished result](base/examples/decision-support/example.md), made by a fresh chat and
unedited. Yours will differ in its sources and numbers. It worked if it has: "not now" among the
options, a source and date for every fact (or "not found"), a score for each option, a
recommendation that follows from those scores, and a check list at the end.

**Now your own question:** replace the profile with your business, or leave it out and the tool
asks six questions first. To keep the tool, keep the instructions in a note and paste them at the
start of each chat, or save them once in a free ChatGPT or Claude project or a Gemini Gem:
[how to set it up, step by step](base/examples/decision-support/README.md#set-it-up-once-about-5-minutes).
Use real business figures only if your workplace allows that chatbot for them.

## Make your own (the short path)

Most jobs are one person turning one kind of input into one result. The easiest way is to let the
coach build the four files with you, in about an hour the first time (an estimate). Paste this into
your chatbot and change the last line to a job you repeat:

<!-- prompt:start (written by _build/build.py) -->
```
Read the build coach at https://raw.githubusercontent.com/bar181/practical-ai/main/projects/agentic-process/base/AI-INSTRUCTIONS.md and follow it. If you cannot open it, say so and stop: do not make up a coach of your own.

My idea: every Monday I turn last week's sales notes into an email for my team. I want an AI to draft it.
```
<!-- prompt:end -->

The coach asks at most two questions at a time. It writes the workflow card with you and drafts
the instructions. Then it gives you a test: you paste it into a new chat that remembers nothing,
and bring the whole reply back. It reads what the new chat had to guess, fixes the instructions,
keeps that result as the worked example, and writes how to use the tool. Use invented or
anonymised input for the test; real data is for using the tool, where your workplace allows it.

If the chatbot cannot open the link, open [`base/AI-INSTRUCTIONS.md`](base/AI-INSTRUCTIONS.md),
press **Raw**, copy all of it into the chat, and type: *Follow the build coach pasted above. My
idea:* and your job. Prefer to fill the files in yourself? Copy [the template](base/template/).

**Most readers can stop here.** The rest is for jobs that need more planning, and for people who
build with coding agents.

## When the job needs more planning: the nine checks

Take all nine when the tool is used by more than one person, reads or writes files other people
use, or costs money. Input that arrives by email does not count as shared files. Each check helps you make
one decision and adds to the four files. [Each step in detail](base/PROCESS.md), with a prompt to paste.

| # | Check | The decision it helps you make | Adds to your files |
| --- | --- | --- | --- |
| 1 | [Scope](base/PROCESS.md#1-scope) | Which one job, for whom, and what is out | The card: who, the job, what is out, the acceptance test |
| 2 | [Reuse check](base/PROCESS.md#2-reuse-check) | Build, wrap something that exists, or stop | The card: what already exists |
| 3 | [Outside help](base/PROCESS.md#3-outside-help) | What, if anything, to buy or connect | Setup guide: what it needs |
| 4 | [Cost](base/PROCESS.md#4-cost) | Whether it is worth running | The card: what you will measure |
| 5 | [Simplest design](base/PROCESS.md#5-simplest-design) | Where it runs and where it is saved | The card: where it runs; the setup steps |
| 6 | [Plan](base/PROCESS.md#6-plan-and-front-door) | The steps, the result, and what a person checks | The rest of the card, and draft instructions |
| 7 | [Review](base/PROCESS.md#7-review) | Whether a stranger understands the card | Fixes to the card |
| 8 | [Build and test](base/PROCESS.md#8-build-and-test) | Whether it is ready, or what to fix first | Final instructions, the example, how to use it |
| 9 | [Grow](base/PROCESS.md#9-grow) | What to add next, from real use | The next version |

**Think of it as** a site inspector on a small job: nothing moves to the next stage until the
current one is signed off. The final check is a fresh chat that has only your instructions. It
finds what you cannot see, because you know what you meant.

## Go further

| Level | For | What it adds |
| --- | --- | --- |
| **Base**: the simplest version that works | Anyone, starting in minutes | A useful result today, and the four files to run it again |
| **Level 2**: repeatable | Someone trained on AI, or a coder | A saved, shared workflow in a chatbot project, a skill or a shared folder. For coders: [one skill folder](level-2-files/) that turns an idea into a testable spec and a project folder in any repository |
| **Level 3**: connected and automated | The owner, or a client setup | A folder, a tool server, GitHub or a schedule, connected only when it saves a recurring manual step; [gates, fresh-session tests and every test log](level-3-files/) |

**More examples**, each made by a fresh session from this project's instructions, unedited, with
invented people: [a Monday email from sales notes](base/examples/monday-email.md) (short path),
[deal updates for a sales team](base/examples/shared-tracker.md) (all nine), and
[an agent working unattended](base/examples/unattended-run.md) (Level 2 and 3). These three were
made before the four-file package, so they hand back a plan and a prompt instead.

**If you are an AI agent:** follow [`AGENTS.md`](AGENTS.md).

## Autopilot (Level 2, not yet proven): a spec in, a finished tool out

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

[How to run it, and what comes back for each target](level-2-files/AUTOPILOT.md). Its progress is tracked
separately, in [`AUTOPILOT-PROGRESS.md`](../../workshop/plans/agentic-process/AUTOPILOT-PROGRESS.md).

## Status

**Built on 16 November 2026, by its author.** Nobody else has used it yet.

| Part | Who has tried it |
| --- | --- |
| The coach | Fresh AI sessions, six runs in Claude. **Not yet run in ChatGPT, Gemini or Copilot, or by a person** |
| The skill folder | One agent working unattended, in an empty repository: it built and tested a first tool |
| Autopilot | **Not yet run end to end.** Written on 16 November 2026 |
| The links in this page | Open once this project is merged into the main branch |

Every round of testing, with the logs, is in [`level-3-files/test-runs/`](level-3-files/test-runs/README.md).

**Built a tool with it?** [Tell us in two minutes](https://github.com/bar181/practical-ai/issues/new?template=i-built-one.yml): the form records the three numbers the North Star is measured by.

## How it is laid out

```
agentic-process/
  README.md               this page
  AGENTS.md               the path for an AI agent
  base/                   Base: everything you need
    AI-INSTRUCTIONS.md    the build coach: paste into your chatbot
    PROCESS.md            the nine checks in detail, and the one-page plan to fill in
    template/             the four files to copy: workflow card, instructions, example, how to use
    examples/             a complete tool (decision-support/), and unedited runs of the coach and an agent
  level-2-files/          Level 2: one skill folder, with the project template and its checks inside, and AUTOPILOT.md
  level-3-files/          Level 3: gates, the fresh-run test, a score sheet, and every test log
  _build/                 steps.py, the one source of the nine steps; build.py, which writes every generated file from it; deferred/, pages parked until version 1
```

## About the creator

<img src="../artifact-studio/_build/img/bradley-ross.jpg" width="130" alt="Bradley Ross, creator of Practical AI">

**Bradley Ross** is an agentic AI architect and developer for businesses of every size, from
start-up to enterprise. He builds and teaches practical AI.

**Training, questions or feedback:** [linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)

Free to use, change and share under Apache-2.0. See [`LICENSE`](LICENSE).
