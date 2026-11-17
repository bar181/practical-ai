# Agentic Process

<h3 align="center">An agentic engineer at your side, for everyday jobs.</h3>

<p align="center">A harness for everything.</p>

**Are you an AI agent?** Go to [AGENTS.md](AGENTS.md) for instructions you can follow now.

Most everyday AI work is a prompt and a hope. Agentic Process turns a job you repeat into a small
tool: one instruction file you paste into a new chat, a worked example, and a short test, so the AI
does the job the same way every time.

- **Work you can rely on.** A fresh AI session tests the tool before you use it.
- **The same way every time.** Written steps you save once, not a lucky prompt.
- **Time back.** Next week starts from the saved instructions, not a blank chat.

<a name="get-started-try-it-now"></a>

## Try it now

Copy this into the chatbot you already use. Swap in your own job, who uses the result, and the
mistake it must catch.

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
example, and a short test. Tested so far in Claude; not yet in ChatGPT or Gemini.

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

<p align="center"><b><i>"Like having an engineer sitting with me, so every new job is set up the proper way."</i></b></p>

## See the difference

**In one blind pilot, a tool built with Agentic Process scored 93/100. The direct-build version
scored 73/100 on the same brief.**

<p align="center">
  <img src="_build/img/pilot-score.svg" width="720" alt="Animated chart: in one blind pilot on the same brief, the tool built with Agentic Process scored 93 out of 100 and needed 0 corrections; the direct-build version scored 73 out of 100 and needed 2 corrections.">
</p>

<p align="center">
  <img src="_build/img/pilot-brief-direct.webp" width="49%" alt="Screen capture of the reply from the tool built directly: a title, a line counting penalties, actions, dates and questions, then a key facts table where the missing effective date and the account form sit among the facts.">
  <img src="_build/img/pilot-brief.webp" width="49%" alt="Screen capture of a chat reply from a tool built with Agentic Process, run on a supplier notice it had never seen. It sums up that the notice asks for four things, with the earliest deadline 15 December 2026, then warns that three things are missing: the Effective Date is never stated, the Account Update Form was not attached, and the overdue charge points to nothing. Below, a table of what you must do, each row with the exact words from the notice and where they are.">
</p>

<p align="center"><sub>Before, left: built the usual way, the missing date is buried in a table. After, right: built with Agentic Process, it warns first.</sub></p>

Both tools found all nine key items in a notice neither had seen. Only the Agentic Process tool put
the missing date and form first and said who to ask. The owner could act on it with no
corrections; the other needed two.

One build task, one unseen notice, one blind reviewer: a strong signal, not a study.
[The full pilot](quality-results/README.md) · [the raw review](quality-results/2026-11-16-builder-pilot/runs/BLIND-REVIEW.md).

## Get started: make it your standard

Set it up once, and every new job starts from the same method.

| Level | You use | Do this |
| --- | --- | --- |
| **1. Try it** | The chatbot you already use | Paste [the prompt above](#try-it-now) into a new chat, with your own job |
| **2. Save it** | A chatbot project, or an assistant that loads skills | Paste [`base/PROCESS.md`](base/PROCESS.md) into a Claude or ChatGPT Project, or a Gemini Gem. Or add [the builder skill](level-2-files/) |
| **3. Hand it over** | A coding agent (Claude Code, Codex) | Paste the coding-agent prompt above. It runs the whole build, tests included |

**No AI help at all?** Copy [`base/template/`](base/template/) and follow
[the one-page process](base/PROCESS.md).

**It is ready when** every check ran in a fresh session, the example is a real result, and the
person could act on its first screen as it is.

## What it has built, and how

| Tool | What it does, and how it scored |
| --- | --- |
| [**Document to action brief**](quality-results/2026-11-16-builder-pilot/agentic-process/document-to-action-brief/) | A supplier notice or report becomes what you must do, by when, and what is missing, each with the exact words.<br>*93/100 in the blind pilot, zero corrections.* |
| [**Decision brief**](base/examples/decision-support/) | A business question becomes options weighed against your goals and limits, with dated sources and a recommendation.<br>*86 to 89 in blind grading, against 61 to 67 for a plain chatbot answer: one question, three blind graders. Every grader also said a busy owner would rather receive the plain answer.* |
| [**Learning log**](base/examples/learning-log/) | Each lesson recorded once, and brought back before similar work starts.<br>*Passed three fresh-session checks.* |

<p align="center">
  <img src="_build/img/builder-flow.svg" width="420" alt="Animation of the builder. A job you repeat goes in at the top. Four steps light up in turn: name the usable result, pick the simplest build, build one SKILL.md, and test it in a fresh session, with a loop back to fix. At the bottom, the package you get: README.md, SKILL.md and example.md, checked before you get it.">
</p>

<p align="center"><sub>How every tool above was built: name the result, reuse first, write it once, test it fresh.</sub></p>

1. **Name the result:** who uses it, and the one mistake it must catch.
2. **Reuse first:** use what already does the job; build only what is missing.
3. **Write the instructions once,** for the chatbot people already use.
4. **Test it fresh:** does it hold up, and would the person use it as it is? Fix, then hand back.

**What it adds.** It uses what you already have: your chatbot, Claude's skill creator, existing
plugins and skills. It adds only the structure and the steps they are missing.

## Questions

<details>
<summary><b>Which chatbots has it been tested in?</b></summary>

Claude only, so far, including the blind reviews and the try-it prompt. It is written for any
chatbot, but it has not yet been tried in ChatGPT or Gemini.

</details>

<details>
<summary><b>What does "a tool" mean here?</b></summary>

A small package for one job you repeat: one instruction file you paste into a new chat, a worked
example, and a short explainer with a test. [What a tool is](base/PROCESS.md#what-a-tool-is).

</details>

<details>
<summary><b>Do I need to write code?</b></summary>

No. Level 1 is a prompt you paste into your chatbot. The tool it builds is plain written
instructions. A coding agent is optional, for level 3.

</details>

<details>
<summary><b>What does it cost?</b></summary>

The method is free to use under the [Apache 2.0 licence](LICENSE). It runs in the chatbot you
already use.

</details>

<details>
<summary><b>Where does my information go?</b></summary>

Nothing is hosted by this project. It is files you read or paste, so your work stays in the
chatbot you already use. Nothing is sent, posted or published without you.

</details>

<details>
<summary><b>What does it not do, and who has used it?</b></summary>

It does not replace your chatbot's own features, plugins or skills; it adds the missing piece. In
a plain chat it cannot start a fresh session to test itself, so it gives you the test to run. So
far only its author has used it.

</details>

## Quick start in one line

```
Hey chatbot, act as my agentic engineer using https://github.com/bar181/practical-ai/blob/main/projects/agentic-process/base/PROCESS.md and set up a tool for a job I repeat: <describe the job, who uses the result, and the mistake it must catch>.
```

This one-line version is not yet tested. The tested prompt is in [Try it now](#try-it-now).

## Status

**17 November 2026.** Built by its author with Claude. All testing so far was in Claude, including
the blind reviews and the try-it prompt above. Not yet tried in other chatbots or coding agents, or by anyone else. [The evidence](quality-results/README.md).

## About Bradley Ross

<img src="_build/img/bradley-ross-avatar.webp" width="110" alt="Cartoon avatar of Bradley Ross with a small friendly robot">

Made by **Bradley Ross**, who builds and teaches practical AI. Part of [Practical AI](../../README.md).
[linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)
