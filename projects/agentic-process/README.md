# Agentic Process: from an idea to a tool people can try, in nine steps

<p align="center">
  <img src="_build/img/nine-steps.svg" width="800" alt="Animation: nine steps in a row, from scope to grow. A marker moves along them and stops at a gate after each step. The eighth step, build and test, is highlighted.">
</p>

<h3 align="center">Your AI can build almost anything. That is the problem.</h3>

**An AI agent will happily build the wrong thing three times.** Agentic Process is the order of
work that stops it: nine steps, a gate after each, and a test by a fresh AI session before any
person sees the result. It is free. Use it with ChatGPT, Claude, Gemini or the chatbot you
already have, or hand it to your coding agent.

<p align="center">
  <a href="#try-it-in-five-minutes"><b>Try it in five minutes</b></a> &nbsp;·&nbsp;
  <a href="#what-you-save">What you save</a> &nbsp;·&nbsp;
  <a href="base/TEACH-IN-30-MINUTES.md">Teach it in 30 minutes</a>
</p>

## Try it in five minutes

### 1. Ask the coach about your own idea

Paste this into the chatbot you already use. Change the last line to a job you repeat.

```
Read the build coach at https://raw.githubusercontent.com/bar181/practical-ai/main/projects/agentic-process/base/AI-INSTRUCTIONS.md and follow it.

My idea: every Monday I turn last week's sales notes into an email for my team. I want an AI to draft it.
```

It walks you through the steps one at a time, asks at most two questions in each, and ends with a
one-page plan and a first version you can test.

- **It cannot open the link?** Open [`base/AI-INSTRUCTIONS.md`](base/AI-INSTRUCTIONS.md), copy all
  of it, and paste it in before your idea.
- **Want to see the whole process first?** It is one page: [`base/PROCESS.md`](base/PROCESS.md).
- **Want to see it rendered?** Download [`base/explainer.html`](base/explainer.html) and open it in
  a browser. GitHub shows an HTML file as code.

### 2. Use it at your level

| You are | You use | You get |
| --- | --- | --- |
| **New to this** (Beginner) | The coach, pasted into any chatbot | A one-page plan and a first prompt you can test today |
| **Building with an agent** (Advanced) | [The skill and the project template](level-2-files/) | A project folder in your repository, with the front page and first version in place |
| **Running agents unattended** (Expert) | [Gates, the fresh-run test and the score sheet](level-3-files/) | Proof of what works, before a person spends time on it |

### 3. See it used

| Example | Level | What it is |
| --- | --- | --- |
| [A Monday email from sales notes](base/examples/monday-email.md) | Beginner | The plan, the prompt and the note a new AI session made from one paragraph, unedited |
| [A notice checker for a class](base/examples/supplier-notice.md) | Advanced | The same for a teacher who builds with a coding agent: six files written out in full, unedited |
| [Project one, step by step](base/examples/project-one-through-the-nine-steps.md) | All | What each step would have saved on the first tool in this repository |

The first two were made by sessions that had only the coach. Nobody has used what they made.

**If you are an AI agent:** follow [`AGENTS.md`](AGENTS.md).

## What you save

These compare working with the process against working without it. The first row of each pair
is measured on this repository. The second is an estimate and says so.

| Who | Without the process | With it | Basis |
| --- | --- | --- | --- |
| **Beginner** turning a repeated job into a reusable prompt | An afternoon of trial and error in a chat, and a prompt that works on the day | About 45 minutes with the coach, and a plan, a prompt and a test | Estimate. Not yet timed with a real learner |
| **Advanced** building a small tool with an agent | Project one: 3 days, 4 folder layouts, more than 60 commits in one change request | Project two: built in one sitting, one layout, by following the steps | Measured, on two projects of different size by one author. Project two is the simpler tool |
| **Expert** finding faults before users do | The author's own review over two days found 2 faults in the instructions | 13 fresh sessions in parallel, 5 to 11 minutes each, logged about 230 points of friction and one broken server | Measured on project one, 16 November 2026 |

The quality difference is the larger one. On project one, worked examples scored 66 out of 100
when they were built by hand, and 84 once each was the unedited output of a fresh session.

## The nine steps

| # | Step | The gate |
| --- | --- | --- |
| 1 | Scope | Can you say the job in one sentence? |
| 2 | Reuse check | After what already exists, is there still something to build? If not, stop and write a guide to that thing |
| 3 | Outside help | Do you know what you would build and what you would buy? |
| 4 | Cost | Does the first version cost nothing, or a known amount? |
| 5 | Simplest design | Could a beginner draw it? |
| 6 | Plan and front door | Is the beginner version fully described? |
| 7 | Review | Can someone else explain it back? |
| 8 | Build and test | Did a fresh session finish the job, and what did it trip on? |
| 9 | Grow | Is the level below in use? |

**Think of it as** building a deck in the garden: decide what it is for, check for a kit, price
the wood, draw it, have someone check the drawing, build the smallest platform you can stand on.

**North Star:** a person, or an agent working alone, can take an idea to a tool someone else can
use, without rebuilding it three times on the way.

## What the AI does and what stays with you

| The AI does | You do |
| --- | --- |
| Asks the questions, searches for what exists, drafts the plan | Say no to anything outside the one job |
| Builds the first version and tests it in a fresh session | Read what the test tripped on and decide what to fix |
| Makes each addition | Approve each one, and use the tool yourself |

## Status

**Built on 16 November 2026.** By its author, in one sitting, by following its own steps.

| Part | State |
| --- | --- |
| The coach | Run four times by new AI sessions that had only the coach: two ideas, two rounds. Every run handed over a plan, a first version and a note. The runs logged 9 blocking points, then 7; those were fixed and **not re-tested**. Not yet run in ChatGPT or Gemini, or by a person |
| The process | Nine steps. Used after the fact on project one and from the start on this project |
| The template and the skill | Run end to end by a second agent on 16 November 2026, on an invented idea. The layout check passed first time. Two commands failed as written: the skill gave no path for the template script, and the template had no gates file. Both are fixed and tested by the author, **not yet re-run** by a second agent. [Its log](level-3-files/fresh-run/runs/skill-run/SKILL-RUN.md) lists 8 blocking points. No real tool has been built from the template |
| The fresh-run test | Used on project one (22 runs) and on this project (4 runs). The logs are in the repository |
| The explainer | Made by following Artifact Studio's instructions. Checked in Chrome at three widths with an accessibility scan, with scripts off, and in the WebKit engine that Safari is built on. Not checked on a real phone |
| The times in "What you save" | Two rows measured on this repository. One row is an estimate |
| Real use | **None yet.** Nobody outside its author has built a tool with it |

## How it is laid out

```
agentic-process/
  README.md               this page
  AGENTS.md               the path for an AI agent
  base/                   Beginner: everything you need
    AI-INSTRUCTIONS.md    the build coach: paste into your chatbot
    PROCESS.md            the nine steps on one page
    plan-template.md      the one-page plan to fill in
    explainer.html        a guide to the process, to read or present
    TEACH-IN-30-MINUTES.md  a lesson plan
    examples/             two unedited runs of the coach, and project one step by step
  level-2-files/          Advanced: a skill, a project template and a script to copy it
  level-3-files/          Expert: gates, the fresh-run test and a score sheet
  _build/                 the picture on this page, and the script that writes the explainer
```

## About the creator

<img src="../artifact-studio/_build/img/bradley-ross.jpg" width="130" alt="Bradley Ross, creator of Practical AI">

**Bradley Ross** is an agentic AI architect and developer for businesses of every size, from
start-up to enterprise. He builds and teaches practical AI.

**Training, questions or feedback:** [linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)

Free to use, change and share under Apache-2.0. See [`LICENSE`](LICENSE).
