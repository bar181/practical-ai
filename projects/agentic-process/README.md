# Agentic Process: from an idea to a tool people can try, in nine steps

<p align="center">
  <img src="_build/img/nine-steps.svg" width="800" alt="Animation: nine steps in a row, from scope to grow. A marker moves along them and stops at a gate after each step. The eighth step, build and test, is highlighted.">
</p>

<h3 align="center">Your AI can build almost anything. That is the problem.</h3>

**An AI agent will happily build the wrong thing three times.** Agentic Process is the order of
work that stops it: nine steps, a gate after each, and a test in a fresh chat, run before anyone
else sees the result. It is free. It is written for any chatbot (so far it has been
tested in Claude only), or hand it to your coding agent.

### Start here: [read the guide](https://raw.githack.com/bar181/practical-ai/main/projects/agentic-process/base/explainer.html)

**Recommended.** [The guide](https://raw.githack.com/bar181/practical-ai/main/projects/agentic-process/base/explainer.html) is one scrolling page: what the process is, why it matters at
your level, and all nine steps, each with its purpose, who it helps, what to expect, how you know
it is done, and a prompt to copy. It takes about ten minutes to read.

The link opens the page through raw.githack.com, a free service that shows a GitHub HTML file as
a page. If it does not open, download [`base/explainer.html`](base/explainer.html) and open it in
a browser: GitHub itself shows HTML files as code.

<p align="center">
  <a href="https://raw.githack.com/bar181/practical-ai/main/projects/agentic-process/base/explainer.html"><b>Read the guide</b></a> &nbsp;·&nbsp;
  <a href="#try-it-in-five-minutes">Try it in five minutes</a> &nbsp;·&nbsp;
  <a href="base/PROCESS.md">The nine steps in detail</a> &nbsp;·&nbsp;
  <a href="https://raw.githack.com/bar181/practical-ai/main/projects/agentic-process/base/training.html">Teach it in 30 minutes</a>
</p>

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
path: steps 1, 6 and 8 in full, steps 2 to 5 in a line each, and step 7 folded into the test. You can start in five minutes; a full first run takes about an hour.

- **It cannot open the link?** Open [`base/AI-INSTRUCTIONS.md`](base/AI-INSTRUCTIONS.md), press
  **Raw**, select all, copy, and paste it in before your idea.
- **Rather go one step at a time?** [The nine steps in detail](base/PROCESS.md) give each step a
  purpose, user stories, what to expect, proof you are done, and a prompt to paste.

### 2. Use it at your level

| You are | You use | You get |
| --- | --- | --- |
| **New to this** (Beginner) | The coach, pasted into any chatbot | A one-page plan and a first prompt you can test today |
| **Building with an agent** (Advanced) | [One skill folder](level-2-files/) to copy into your agent's skills. Works in any repository | A project folder with its own checks, the front page and the first version in place |
| **Running agents unattended** (Expert) | [Gates, the fresh-run test and the score sheet](level-3-files/) | Proof of what works, before a person spends time on it |
| **Teaching it** | [The 30-minute training](https://raw.githack.com/bar181/practical-ai/main/projects/agentic-process/base/training.html): slides with a lesson timer and your notes, and [the plan](base/TEACH-IN-30-MINUTES.md) | One lesson where each learner leaves with a plan of their own |

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
| The coach | Run six times by new AI sessions that had only the coach, across three rounds and three invented people. Every run handed over a plan, a first version and a note. Blocking points per run: 4 to 5 in round 1, 3 to 4 in round 2, 2 to 3 in round 3. The round 3 points are fixed and **not re-tested**. In round 3 the short path was chosen for the small job and all nine steps for the team job, as intended. Not yet run in ChatGPT, Gemini or Copilot, or by a person |
| The process | Nine steps, each with a purpose, user stories, proof and a prompt. Used by its author to build this project. Nobody else has followed it yet |
| The template and the skill | Run end to end by a second agent on 16 November 2026, on an invented idea. The layout check passed first time. Two commands failed as written: the skill gave no path for the template script, and the template had no gates file. Both are fixed and tested by the author, **not yet re-run** by a second agent. [Its log](_build/runs/skill-run/SKILL-RUN.md) lists 8 blocking points. No real tool has been built from the template |
| The fresh-run test | Used on both projects in this repository by their author. The logs are in [`_build/runs/`](_build/runs/) |
| The training | Made with Artifact Studio's workshop deck, from one source with the lesson plan. Checked at phone and laptop width with an accessibility scan and with scripts off. **Not yet taught.** Opens from the link once this branch is merged |
| The guide | Made by following Artifact Studio's instructions, from the same source as the detailed steps page. Checked in Chrome at three widths with an accessibility scan, with scripts off, and in the WebKit engine that Safari is built on. Not checked on a real phone. The raw.githack.com link works only once this branch is merged |
| The times | All estimates. Nobody has been timed |
| Real use | **None yet.** Nobody outside its author has built a tool with it |

## How it is laid out

```
agentic-process/
  README.md               this page
  AGENTS.md               the path for an AI agent
  base/                   Beginner: everything you need
    AI-INSTRUCTIONS.md    the build coach: paste into your chatbot
    PROCESS.md            the nine steps in detail, and the one-page plan to fill in
    explainer.html        the guide: the same steps as a page to read or present
    training.html         the 30-minute training: slides, a lesson timer and the teacher's notes
    TEACH-IN-30-MINUTES.md  the same lesson as a plan to read
    examples/             unedited runs: two of the coach, one of an agent working unattended
  level-2-files/          Advanced: one skill folder, with the project template and its checks inside
  level-3-files/          Expert: gates, the fresh-run test and a score sheet
  _build/                 steps.py and lesson.py, the sources; build.py, which writes every page from them; runs/, the test logs
```

## About the creator

<img src="../artifact-studio/_build/img/bradley-ross.jpg" width="130" alt="Bradley Ross, creator of Practical AI">

**Bradley Ross** is an agentic AI architect and developer for businesses of every size, from
start-up to enterprise. He builds and teaches practical AI.

**Training, questions or feedback:** [linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)

Free to use, change and share under Apache-2.0. See [`LICENSE`](LICENSE).
