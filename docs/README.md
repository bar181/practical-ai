# Practical AI: what is ready, and what comes next

A one-page summary for anyone deciding where to start. Updated 19 November 2026.

## What is ready

Five projects are built and ready to try. Users are testing the first four as of 18 November
2026; the Learnings database was finished on 19 November. The two with the most evidence are
below; Document to action brief, the Learnings database and the Rare Find game follow in the lists.
Artifact Studio, Agentic Process, the Learnings database and Rare Find each have an explainer page
in [`reports/`](reports/) (download the HTML file and open it in a browser).

### Artifact Studio: designer-quality reports you make yourself

**What it does:** your AI can already make scrollytelling pages, photo effects, animated diagrams,
a visionary keynote or a lesson to teach from, but most people do not know to ask. Artifact Studio
puts them on a menu, so one sentence turns rough notes into a professional page fitted to the
reader.

**How you use it:** paste one prompt with your notes, read the page that comes back, check the
numbers against your notes, and share it. Then ask for the same notes as a deck or a post in one
sentence.

**Use cases:** a monthly report for a business partner, a deck for a team meeting, a week of posts
from one piece, a page that opens with your own photo.

**Where it stands:** built and checked by its author, with 22 runs by fresh AI sessions. Tried
only in Claude so far. [Open the project](../projects/artifact-studio/) ·
[the explainer page](reports/artifact-studio.html) ·
[the evidence](../projects/artifact-studio/quality-results/README.md).

### Agentic Process: an agentic engineer at your side

**What it does:** gives a job you repeat with AI the structure developers give coding agents: a
clear result, written steps, the one mistake to catch, and a test in a fresh session before you
rely on it. It uses the AI tools you already have and adds only what they are missing.

**How you use it:** paste one build request into a coding agent such as Claude Code, with the job,
who will use the result and the one thing that usually goes wrong. Read the hand-back, run any
tests it left for you, and check it against the "Is it ready?" list.

**Use cases:** supplier notices into actions and dates, a business decision brief with sources, a
log of lessons learned, meeting notes into actions.

**Where it stands:** in one blind pilot, a tool built with Agentic Process scored 93/100. The
direct-build version scored 73/100 on the same brief. That was one build task, one unseen notice
and one blind reviewer. [Open the project](../projects/agentic-process/) ·
[the explainer page](reports/agentic-process.html) ·
[the evidence](../projects/agentic-process/quality-results/README.md).

## What comes next

The next tools, in the order they are planned. "Example built" means a working version exists
inside Agentic Process; it becomes its own project once someone other than its author has used it.

### For everyday work

Jobs you already do, done faster with the chatbot you have. Each is one file and one worked example.

| # | Tool | What it will do for you | Where it stands |
| --- | --- | --- | --- |
| 1 | **Document to action brief** | Turn a notice, contract, tender or bill into what you must do, the dates and the open questions, each with the line it came from | **In user testing:** [project](../projects/document-to-action-brief/) |
| 2 | **Write and edit in my voice** | Learn your style from three samples, then revise an email or post without changing a fact or a promise | Plan |
| 3 | **Meeting notes to actions** | Turn a transcript into decisions, tasks and a follow-up, and flag any owner or date nobody agreed | Plan |
| 4 | **Research brief with checked sources** | Compare options on one page, with every claim linked to a source you can open | Early draft |
| 5 | **Inbox triage and replies** | Sort the inbox into reply today, delegate and wait, and draft the two replies that matter most | Early draft |
| 6 | **Customer issue helper** | Handle a late order or a refund from your one-page policy, and say when a manager should step in | Idea |
| 7 | **Ask your spreadsheet** | Explain what changed in a sales export and show the rows behind the answer | Early draft |
| 8 | **Receipts into an expense sheet** | Read each receipt into a sheet and flag any that are blurry or incomplete | Plan |
| 9 | **Business decision helper** | Compare options against your goals and limits, with sources, and say what would change the answer | Example built |
| 10 | **Quote a job** | Prepare a first quote from your price sheet and a customer request, with the arithmetic shown | Early draft |

### For people who build with agents

Support tools that make every other tool better. Each starts with a version a person can inspect.

| # | Tool | What it will do for you | Where it stands |
| --- | --- | --- | --- |
| 1 | **Learnings database** | Record each lesson once, filed by type and topic, and bring it back before similar work starts | **Built, tested by Claude, 19 Nov 2026:** [project](../projects/learnings-database/) · [explainer](reports/learnings-database.html) · [idea file](../projects/learnings-database/level-2-files/gist/learnings-log.md) |
| 2 | **Task and dependency graph** | Turn a goal into tasks, and show what is ready and what is blocked | Plan |
| 3 | **Decision support** | Take a decision from options to a recommendation with the working shown | Example built |
| 4 | **Estimate to proposal** | Combine a request, notes and past jobs into a draft estimate and proposal | Early draft |
| 5 | **Recurring research brief** | Compare this week's evidence with last week's and surface what changed | Early draft |
| 6 | **Source and link checker** | Check that every cited link still says what the document claims | Plan |
| 7 | **Rubric reviewer** | Score a piece of work against a rubric written in advance, with evidence for each line | Plan |
| 8 | **Core memory** | Keep policies, facts and pointers you ask to be kept, and find them with their source | Plan |
| 9 | **Connections hub** | Read a meeting or an email thread and propose what is worth keeping, for you to accept | Plan |
| 10 | **Daily builder** | Take one approved item from this list through Agentic Process and hand back a reviewable change | Plan |

### Side quest

| Project | What it does for you | Where it stands |
| --- | --- | --- |
| **Rare Find** | A five-minute daily trivia game in Claude or any browser, where the right answer nobody else thought of scores the most | **In user testing:** [play in Claude](https://claude.ai/artifact/HyfbDjPjofvRttRYKgMCis) · [play in a browser](https://bar181.github.io/practical-ai/rare-find/) · [project](../projects/rare-find/) · [explainer](reports/rare-find.html) |

The full list of ideas, sorted into everyday tasks, agent tools and hybrid projects, is in
[the plans](../workshop/plans/README.md).

## How the order is chosen

Need first: tools people already use AI for most, by usage studies and small-business surveys read
in November 2026. Then foundation: tools that make others cheaper to build. Then reuse: tools whose
first version needs nothing new. The order is a judgement, not a measurement.
