# Agentic Process

<p align="center">
  <img src="_build/img/pilot-score.svg" width="720" alt="Animated chart: in one blind pilot on the same brief, the tool built with Agentic Process scored 93 out of 100 and needed 0 corrections; the direct-build version scored 73 out of 100 and needed 2 corrections.">
</p>

<h3 align="center">AI tools that catch what people miss.</h3>

<p align="center"><b>Turn a job you repeat into a tool that does it well every time.</b><br>
Agentic Process works with your coding agent to build the tool, then tests it before you rely on it.
In a blind pilot, its tool scored 93 out of 100. A tool built the usual way scored 73.</p>

<p align="center">
  <a href="#get-started"><b>Build your first tool</b></a> &nbsp;·&nbsp;
  <a href="#the-proof">The proof</a> &nbsp;·&nbsp;
  <a href="#what-it-has-built">What it has built</a>
</p>

## Why it is better

- **Better results.** Every tool is built around who will use it and the one mistake it must
  catch, then tested on exactly that mistake.
- **Checked before you rely on it.** A fresh AI session tries the tool, as a stranger would. If the
  person could not act on the result as it is, the tool is fixed first.
- **A repeatable process with your AI.** The same four steps for every job, so each new tool starts
  from a method that already works.
- **And faster.** A tested tool in about ten minutes. Times are estimates.

## The proof

<p align="center">
  <img src="_build/img/pilot-brief-direct.webp" width="49%" alt="Screen capture of the reply from the tool built directly: a title, a line counting penalties, actions, dates and questions, then a key facts table where the missing effective date and the account form sit among the facts.">
  <img src="_build/img/pilot-brief.webp" width="49%" alt="Screen capture of a chat reply from a tool built with Agentic Process, run on a supplier notice it had never seen. It sums up that the notice asks for four things, with the earliest deadline 15 December 2026, then warns that three things are missing: the Effective Date is never stated, the Account Update Form was not attached, and the overdue charge points to nothing. Below, a table of what you must do, each row with the exact words from the notice and where they are.">
</p>

**In one blind pilot, a tool built with Agentic Process scored 93/100. The direct-build version
scored 73/100 on the same brief.** Both found all nine key items in a notice neither had seen. Only
the Agentic Process tool put the missing date and form first and said who to ask, and the owner
could act on it with no corrections. The other needed two.

**The two captures, in words:** the same supplier notice, given to two tools built from the same
brief. Left, a tool built the usual way: the facts are there, but the missing effective date is
buried in a table. Right, the tool built with Agentic Process: it warns first that the date and a
form are missing, and says who to ask.

One build task, one notice, one blind reviewer: a strong signal, not a study.
[The full pilot](quality-results/README.md) · [the raw review](quality-results/2026-11-16-builder-pilot/runs/BLIND-REVIEW.md).

## What it has built

| Tool | What it does for you | Quality, checked |
| --- | --- | --- |
| [**Document to action brief**](quality-results/2026-11-16-builder-pilot/agentic-process/document-to-action-brief/) | A supplier notice or report becomes what you must do, by when, and what is missing, each with the exact words | 93/100 in the blind pilot, zero corrections |
| [**Decision brief**](base/examples/decision-support/) | A business question becomes options weighed against your goals and limits, with dated sources and a recommendation | Scored 86 to 89 in blind grading, against 61 to 67 for a plain chatbot answer |
| [**Learning log**](base/examples/learning-log/) | Each lesson recorded once, and brought back before similar work starts | Passed three fresh-session checks |

## How it works

<p align="center">
  <img src="_build/img/builder-flow.svg" width="420" alt="Animation of the builder. A job you repeat goes in at the top. Four steps light up in turn: name the usable result, pick the simplest build, build one SKILL.md, and test it in a fresh session, with a loop back to fix. At the bottom, the package you get: README.md, SKILL.md and example.md, checked before you get it.">
</p>

1. **Name the result:** who uses it, and the one mistake it must catch.
2. **Reuse first:** use what already does the job; build only what is missing.
3. **Build the tool** for the chatbot people already use.
4. **Test it fresh:** does it hold up, and would the person use it as it is? Fix, then hand back.

## Get started

Open a coding agent such as Claude Code or Codex in an empty folder, and paste this:

```
Read the builder skill at
https://raw.githubusercontent.com/bar181/practical-ai/main/projects/agentic-process/level-2-files/agentic-process/SKILL.md
and follow it.

The job: when a supplier sends a notice
that changes our terms, work out what it
makes us do and by when.
Who uses the result: a café owner,
in the chatbot they already use.
Example input: write an invented
one-page supplier notice.
The catch: a notice that leaves out a date
or an attachment it mentions.

Put the tool in document-to-action-brief/.
Hand back what you built, the checks
you ran, and what you assumed.
```

You get the tool, a guide and a real tested example. Then use it on your own job: keep the first
three lines and give the job, who uses the result, an example input, and the mistake it must catch.

**It is ready when** every check ran in a fresh session, the example is a real result, and the
person could act on its first screen as it is. If the builder could not run its tests, it hands you
the messages to paste into fresh chats.

No coding agent? Copy [`base/template/`](base/template/) and follow [the one-page process](base/PROCESS.md) in any chatbot.
To skip the link, install [the builder skill](level-2-files/). AI agents: [`AGENTS.md`](AGENTS.md).

## Status

**16 November 2026.** Built by its author with Claude. All testing so far was in Claude, including
the blind reviews. Not yet tried in other coding agents, or by anyone else. [The evidence](quality-results/README.md).

<img src="_build/img/bradley-ross-avatar.webp" width="110" alt="Cartoon avatar of Bradley Ross with a small friendly robot">

Made by **Bradley Ross**, who builds and teaches practical AI. Part of [Practical AI](../../README.md).
[linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)
