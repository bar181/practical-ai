# Practical AI: put your smart intern to work

<p align="center">
  <img src="docs/assets/smart-intern.svg" width="800" alt="Animation: AI is a smart intern that has read every book and has never met you. It needs your priorities, your tone of voice, what your business does and how it can help you. Then it is ready to work">
</p>

<h3 align="center">AI has read every book in the world. It has never met you.</h3>

**Practical AI is a free set of tools that turn the AI you already have into a productive digital
employee.** Think of AI as a **smart intern**: a new hire who has read everything and knows
nothing about you. It needs your priorities, your tone of voice, what your business does and how
it can help. Each tool here hands it exactly that, for one job you repeat. It works with ChatGPT,
Claude, Gemini, Microsoft Copilot and other chatbots, and with personal agents.

<p align="center">
  <a href="#make-your-first-report-artifact-studio"><b>Make your first report</b></a> &nbsp;·&nbsp;
  <a href="#build-a-tool-agentic-process"><b>Build a tool</b></a> &nbsp;·&nbsp;
  <a href="#the-jobs-you-repeat">The jobs it helps with</a> &nbsp;·&nbsp;
  <a href="#created-by-bradley-ross">Who made this</a>
</p>

## Choose a project

Two projects are ready. Pick the one that matches what you want to do today.

### Make your first report: Artifact Studio

**For someone with rough notes and something to share.** Paste one prompt into the chatbot you
already use and get a one-page report your reader can take in on a phone. Then the same notes as a
slide deck, a social post or a page that opens with your photo.

<p align="center">
  <a href="projects/artifact-studio/"><img src="projects/artifact-studio/_build/img/example-report.webp" width="560" alt="Screen capture of a one-page monthly report made by an AI chatbot from eight lines of notes about an invented landscaping company: the headline October beat September, revenue up 12,700 dollars, four more jobs done and more quotes became jobs; three key numbers for revenue, jobs completed and quotes won; and a bar chart comparing September and October"></a>
</p>

An AI chatbot made this page from eight lines of invented notes, in one try, unedited.

<p align="center"><a href="projects/artifact-studio/#try-it-make-your-first-report-in-5-minutes"><b>Make your first report in 5 minutes</b></a></p>

### Build a tool: Agentic Process

**For someone who builds tools or workflows with a coding agent** such as Claude Code or Codex.
Paste one build request with a job you repeat. You get back a small package another person can
start in five minutes: a README, one `SKILL.md` that works in any chatbot, and a worked example,
tested in a fresh session before you get it.

<p align="center">
  <a href="projects/agentic-process/"><img src="projects/agentic-process/_build/img/builder-flow.svg" width="400" alt="Animation of the builder: a job you repeat goes in; four steps light up in turn, name the usable result, pick the simplest build, build one SKILL.md, test it in a fresh session; out comes a checked package of README.md, SKILL.md and example.md"></a>
</p>

**In one blind pilot, a tool built with Agentic Process scored 93/100. The direct-build version
scored 73/100 on the same brief.** Both found all nine key items in an unseen supplier notice; the
Agentic Process version also put the missing date and form at the top, said who to ask, and needed
no corrections before acting. One build task, one notice, one blind reviewer:
[the evidence](projects/agentic-process/quality-results/README.md).

<p align="center"><a href="projects/agentic-process/#try-it-build-a-tool-in-about-10-minutes"><b>Build your first tool in about 10 minutes</b></a></p>

### Not sure?

| You are | Go to |
| --- | --- |
| **New to AI, on a phone or a laptop** | [Make your first report](projects/artifact-studio/#try-it-make-your-first-report-in-5-minutes) |
| **Using a chatbot every day** | Artifact Studio's [one-time setup](projects/artifact-studio/#advanced-setup-use-it-every-day) |
| **Building with a coding agent** | [Build a tool](projects/agentic-process/#try-it-build-a-tool-in-about-10-minutes) |
| **An AI agent** | [`AGENTS.md`](AGENTS.md) |

Some pages here are HTML files. GitHub shows an HTML file as code, so download it and open it in a
browser to see the page. The times are estimates.

## Practical, not breakthrough

This is not about new technology. It is about getting more done, and done better, by letting AI
do the things AI is good at.

- **Tasks, not theory.** Each tool is one job you already do every day, every week or every month.
- **Time back, and better quality.** The AI gets you most of the way to a solid draft. You spend
  your time on the part that needs you.
- **A clear split.** Every tool says what the AI does and what stays your responsibility.

**Think of it as** a cookbook where every recipe works three ways: cooked by hand tonight, saved as
the house recipe for any night, or run by a kitchen where the orders come in and the line cooks it.

**North Star:** someone opens a tool and gets a usable result with their own input, fast. Each
tool has a short explainer: what it does, how to start, what goes in and comes out, and what to
check, with one worked example.

## The jobs you repeat

<p align="center">
  <img src="docs/assets/jobs-you-repeat.svg" width="800" alt="Card showing the jobs Practical AI helps with. Daily: sort the inbox, turn meetings into actions. Weekly: a slide deck or report, ready now, and posts for the week. Monthly: the monthly report and receipts into a sheet. The AI does the drafting. You check it and make the call">
</p>

| Job you repeat | The AI does | You do |
| --- | --- | --- |
| **A slide deck, report or mini website from your notes**<br>Weekly. Ready now | The design, the layout, the first draft | Check the numbers, decide what to cut |
| **Sort the inbox and draft replies**<br>Daily. Drafted | Reads, sorts, drafts | Approve and send |
| **Meeting notes to actions**<br>Daily. Planned | Pulls decisions, owners and dates | Confirm names and dates |
| **Posts for the week from one piece**<br>Weekly. Previews ready now | Drafts in your voice, shown as they will look in the feed | Choose, edit and post |
| **Research brief with checked sources**<br>Weekly. Partly drafted | Finds, reads, links every claim | Open the links, judge the answer |
| **Receipts and invoices into a sheet**<br>Monthly. Planned | Reads each receipt and fills the form | Check each line against the photo |

These are the jobs people most often use AI for, from usage studies and small-business surveys
read in November 2026. What gets built next is in [`docs/practical-ai-priorities.md`](docs/practical-ai-priorities.md),
and the research is in [`docs/tool-inventory.md`](docs/tool-inventory.md).

## How each tool is built

**Reuse first.** For each job: use what already does it, such as Anthropic's own skills and
plugins; add a thin layer for business rules or missing steps; build only what is still missing.

**One file per tool.** Each tool is a README that explains it, one `SKILL.md` and a worked
example. `SKILL.md` uses the open Agent Skills format, so the same file installs as a Claude skill,
works in other tools that support the format, and can be pasted into any chatbot. No lock-in to one
provider.

**[Agentic Process](projects/agentic-process/)** builds them: it writes down the usable result,
picks the simplest build, and tests the tool in a fresh session before handing it back. Tools it
has made: [decision support](projects/agentic-process/base/examples/decision-support/), a
[learning log](projects/agentic-process/base/examples/learning-log/), and the pilot's
[document to action brief](projects/agentic-process/quality-results/2026-11-16-builder-pilot/agentic-process/document-to-action-brief/).

## Explainers

Every tool has a short explainer: what it does, how to start, what goes in and comes out, and what
to check, with one worked example. It can live in the README. It explains the finished tool; it is
not a course. [Artifact Studio](projects/artifact-studio/) also has a page version, and a
[30-minute lesson plan](projects/artifact-studio/base/TEACH-IN-30-MINUTES.md) for anyone who presents it.

## What comes next

The next tools. Each has a plan waiting on the owner's review, and each checks every AI-made item
against its source before you act. [Document to action brief](projects/agentic-process/quality-results/2026-11-16-builder-pilot/agentic-process/document-to-action-brief/),
the third planned tool, was built as the builder's pilot and is kept with its evidence.

1. [**Write and edit in my voice**](workshop/plans/write-in-my-voice/): three samples become a
   voice guide, and a revised draft keeps every fact and promise.
2. [**Meeting notes to actions**](workshop/plans/meeting-notes-to-actions/): a transcript becomes
   actions, with every owner or date nobody agreed to flagged.

After that, the tools in [the priorities](docs/practical-ai-priorities.md), one change request each.

## Three levels: how much is set up and automated

<p align="center">
  <img src="docs/assets/levels.svg" width="640" alt="Animation: every Practical AI tool comes at three levels. Beginner: start in minutes, you start the run. Advanced: a saved project or skill you start any time. Expert: connected and automated, a trigger runs it and people decide the exceptions">
</p>

| Level | What you get |
| --- | --- |
| **Beginner** (Level 1, always) | Standalone in any chatbot: paste the file or share the link, add your context, get the result |
| **Advanced** (Level 2) | Saved as a skill or project, started whenever needed |
| **Expert** (Level 3) | Connected through MCP, endpoints or a trigger that supply inputs and take outputs. A person approves exceptions |

Not every tool has all three: a level is added only when it removes setup or recurring work. The
levels describe setup, not people. Start at Beginner. It is the whole tool.

## Created by Bradley Ross

<p>
  <img src="docs/assets/bradley-ross.jpg" width="150" alt="Bradley Ross, creator of Practical AI">
  &nbsp;
  <img src="docs/assets/bradley-ross-avatar.webp" width="150" alt="Cartoon avatar of Bradley Ross with a small friendly robot, in front of a red-brick campus building">
</p>

**Bradley Ross** is an agentic AI architect and developer for businesses of every size, from
start-up to enterprise.

- **Specialty:** deterministic AI, and advanced AI research into AI with learning transfer abilities.
- **Harvard CS50:** 10 terms as a Teaching Fellow.
- **Agentics Foundation:** Director, working with and sharing teaching with the top agentic
  engineers in the world.
- **Practical AI training:** 12 courses, over 40 cohorts and more than 900 students.

These tools come out of that teaching: what people ask for most, in the form that worked in the
room.

**More information, training or feedback:** [linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)

<details>
<summary>How the repository is organised, and the ground rules</summary>

| Folder | What it holds |
| --- | --- |
| [`projects/`](projects/) | The two projects: Artifact Studio and Agentic Process |
| [`docs/`](docs/) | What gets built next, the to-do list and dated reports |
| [`workshop/`](workshop/) | How the tools get built: plans, earlier drafts, skills and checking scripts. You do not need it to use a tool |

Inside every project, `base/` is enough to try the tool. Beside it, `level-2-files/` and
`level-3-files/` hold the saved and the connected versions.

- Reuse what already exists before building anything new.
- A person approves anything that posts, sends, pays or publishes.
- Examples use invented data and say so. No real names, companies or client material. The exception is a page about this repository and its author, which says so.
- Every claim about something that changes often carries the date it was checked.
- Every status line says who has and has not tried the thing. "Built" is not "used".

`python3 workshop/tools/check_project.py projects/artifact-studio` checks a project against the layout in
[`projects/README.md`](projects/README.md). How a tool gets built is
[Agentic Process](projects/agentic-process/): it specifies the usable result, builds the simplest version and tests it in a fresh session.

</details>

Free to use, change and share under Apache-2.0.
