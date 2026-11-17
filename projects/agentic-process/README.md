# Agentic Process

<p align="center">
  <img src="_build/img/pilot-score.svg" width="720" alt="Animated chart: in one blind pilot on the same brief, the tool built with Agentic Process scored 93 out of 100 and needed 0 corrections; the direct-build version scored 73 out of 100 and needed 2 corrections.">
</p>

<h3 align="center">An agentic engineer at your side, for everyday jobs.</h3>

<p align="center"><b><i>"Like having an engineer sitting with me, so every new job is set up the proper way."</i></b></p>

A mini harness for work that is not code: a clear result, written steps, and a test before you
rely on it.

<p align="center">
  <a href="#get-started-try-it-now"><b>Try it now</b></a> &nbsp;·&nbsp;
  <a href="#the-proof">The proof</a> &nbsp;·&nbsp;
  <a href="#what-it-has-built">What it has built</a>
</p>

## Get started: try it now

**In the chatbot you already use.** Copy this, and swap in your own job, who uses the result, and
the mistake it must catch.

```
Act as my agentic engineer. Use the method at
https://raw.githubusercontent.com/bar181/practical-ai/main/projects/agentic-process/base/PROCESS.md
to help me turn a job I repeat into a tool
I can reuse.

The job: every Monday I turn our team's
meeting notes into a list of actions.
Who uses the result: me, in ChatGPT, then
I email the list to the team.
The mistake it must catch: actions that
nobody agreed to own, or with no date.

Ask me for anything missing in one message.
Then write the tool as one instruction file
I can paste into a new chat, an example,
and a short test I can run to check it works.
```

You get instructions you can paste into any new chat to do the job the same way every time, an
example, and a short test.

<details>
<summary><b>Have a coding agent? Let it do the whole build</b> (Claude Code, Codex)</summary>

The builder does the whole job, including running the tests in fresh sessions. Open it in an empty
folder and paste:

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

</details>

**It is ready when** every check ran in a fresh session, the example is a real result, and the
person could act on its first screen as it is.

## What it adds

Developers trust AI coding agents because they work inside a harness: a spec, steps, tests and a
hand-back. Most everyday work with AI has none of that. You type a prompt, and hope.

Agentic Process is the engineer who sets it up properly with you, for jobs such as a supplier
notice, a decision or a monthly report:

- **A clear result.** Who uses it, what they need, and the one mistake it must catch.
- **Written steps.** Done the same way every time, not a lucky prompt.
- **A test before you rely on it.** A fresh AI session tries the tool as a stranger would, and it
  is fixed until the person could act on the result as it is.
- **The leading tools, not new ones.** It uses what you already have: your chatbot, Claude's skill
  creator, existing plugins and skills. It adds only the structure and the steps they are missing.

## The proof

**In one blind pilot, a tool built with Agentic Process scored 93/100. The direct-build version
scored 73/100 on the same brief.**

<p align="center">
  <img src="_build/img/pilot-brief-direct.webp" width="49%" alt="Screen capture of the reply from the tool built directly: a title, a line counting penalties, actions, dates and questions, then a key facts table where the missing effective date and the account form sit among the facts.">
  <img src="_build/img/pilot-brief.webp" width="49%" alt="Screen capture of a chat reply from a tool built with Agentic Process, run on a supplier notice it had never seen. It sums up that the notice asks for four things, with the earliest deadline 15 December 2026, then warns that three things are missing: the Effective Date is never stated, the Account Update Form was not attached, and the overdue charge points to nothing. Below, a table of what you must do, each row with the exact words from the notice and where they are.">
</p>

<p align="center"><sub>Left: built the usual way, the missing date is buried in a table. Right: built with Agentic Process, it warns first.</sub></p>

**Both tools found all nine key items in a notice neither had seen. Only the Agentic Process tool
put the missing date and form first and said who to ask.** The owner could act on it with no
corrections; the other needed two.

One build task, one notice, one blind reviewer: a strong signal, not a study.
[The full pilot](quality-results/README.md) · [the raw review](quality-results/2026-11-16-builder-pilot/runs/BLIND-REVIEW.md).

## What it has built

| Tool | What it does, and how it scored |
| --- | --- |
| [**Document to action brief**](quality-results/2026-11-16-builder-pilot/agentic-process/document-to-action-brief/) | A supplier notice or report becomes what you must do, by when, and what is missing, each with the exact words.<br>*93/100 in the blind pilot, zero corrections.* |
| [**Decision brief**](base/examples/decision-support/) | A business question becomes options weighed against your goals and limits, with dated sources and a recommendation.<br>*86 to 89 in blind grading, against 61 to 67 for a plain chatbot answer.* |
| [**Learning log**](base/examples/learning-log/) | Each lesson recorded once, and brought back before similar work starts.<br>*Passed three fresh-session checks.* |

## How it works

<p align="center">
  <img src="_build/img/builder-flow.svg" width="420" alt="Animation of the builder. A job you repeat goes in at the top. Four steps light up in turn: name the usable result, pick the simplest build, build one SKILL.md, and test it in a fresh session, with a loop back to fix. At the bottom, the package you get: README.md, SKILL.md and example.md, checked before you get it.">
</p>

1. **Name the result:** who uses it, and the one mistake it must catch.
2. **Reuse first:** use what already does the job; build only what is missing.
3. **Write the instructions once,** for the chatbot people already use.
4. **Test it fresh:** does it hold up, and would the person use it as it is? Fix, then hand back.

## Make it your standard

Set it up once, and every new job starts from the same method.

| You use | Do this once |
| --- | --- |
| **A chatbot** | Paste [`base/PROCESS.md`](base/PROCESS.md) into a Claude or ChatGPT Project, or a Gemini Gem |
| **An assistant that loads skills** | Add [the builder skill](level-2-files/) |
| **No AI help at all** | Copy [`base/template/`](base/template/) and follow [the one-page process](base/PROCESS.md) |

AI agents: [`AGENTS.md`](AGENTS.md).

## Status

**16 November 2026.** Built by its author with Claude. All testing so far was in Claude, including
the blind reviews. Not yet tried in other coding agents, or by anyone else. [The evidence](quality-results/README.md).

<img src="_build/img/bradley-ross-avatar.webp" width="110" alt="Cartoon avatar of Bradley Ross with a small friendly robot">

Made by **Bradley Ross**, who builds and teaches practical AI. Part of [Practical AI](../../README.md).
[linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)
