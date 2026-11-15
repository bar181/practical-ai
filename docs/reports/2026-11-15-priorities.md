# Priorities: what to build next, and why

A report for the owner, 15 November 2026. The artifact studio is closed, the method for building the next tool is revised, and the whole list is re-ranked with your five candidates in it.

**Think of it as** the order of work on a building site. Foundations before walls, and the walls everyone leans on before the ones only one room needs.

## The short version

- **The artifact studio is closed as a draft.** Every gate passes. Nobody but its author has used it.
- **The method is now nine stages:** understand, research, scope, plan, prove, build, verify, score, close. It was seven. It gained a scoring stage and a closing stage, and was checked against how others build with agents.
- **Your five candidates each have a North Star page,** one to three pages, with what already exists and dated sources. I added two more of my own. **None is approved.**
- **The list is re-ranked on one rubric.** The learnings database is first and the task graph second.
- **No wiki.** Memory and learnings are two separate stores of labelled records, kept outside the repository.

## The top of the list

### 1. Learnings database: 90 of 100

| | |
| --- | --- |
| What it is | One row for every error, redo and thing that unexpectedly worked, kept in a store you own and read before similar work starts. |
| The value | The same mistake is never made twice, by you or your agents. |
| Why it ranks here | The smallest of the store tools, with a draft and a skill already here. The project method writes to it at every close, and the memory system reuses its row shape and viewer. Build it first and two other tools get cheaper. |
| The shape | Level 1 is a private CSV, Excel file or Google Sheet. Level 3 is Supabase with keyword and similarity search together. |
| Built on | Research on agents that learn from written lessons without retraining, an open-source harness whose learned rules can be reviewed and revoked, and hybrid search in Postgres. |
| North Star | [`plans/learning-system/NORTH-STAR.md`](https://github.com/bar181/practical-ai/blob/studio/component-gallery/plans/learning-system/NORTH-STAR.md) |

### 2. Task decomposition and dependency graph: 89 of 100

| | |
| --- | --- |
| What it is | A goal becomes tasks with what depends on what, drawn as a tree, a Mermaid diagram, a sticky-note board, a Gantt chart or a ready list. |
| The value | You and your agents always know what to do first and what is blocked. |
| Why it ranks here | Nothing private in it, so it can be shared and taught as it is. Every view reuses the artifact studio. It plans every other tool on this list, and it is the last step of a decision. |
| The shape | One small task file. Five views drawn from it: a tree, a Mermaid diagram, a sticky-note board, a Gantt chart and a "ready now" list. |
| Built on | An open-source tracker built for agents that only shows work with nothing blocking it, spec-driven development, and long-standing project practice. |
| North Star | [`plans/task-graph/README.md`](https://github.com/bar181/practical-ai/blob/studio/component-gallery/plans/task-graph/README.md) |

### 3. Decision support assistant: 82 of 100

| | |
| --- | --- |
| What it is | A decision worked the way a consulting team would: frame, structure, hypothesise, gather, analyse, recommend, deliver, with every link checked. |
| The value | A recommendation you can defend, in one sitting, with the working shown. |
| Why it ranks here | Closest to the owner's paid work, and the frameworks are public and well described. The deliverables already exist in the studio. Ranked below the task graph only because it ends in one. |
| The shape | Seven steps, a template for each, ending in a briefing deck and a plan. Level 3 adds your own material: transcripts, papers, spreadsheets. |
| Built on | The seven-step backbone the large consulting firms share, issue trees with no overlaps or gaps, a hypothesis on each branch, and answer-first presentation. |
| North Star | [`plans/decision-support/README.md`](https://github.com/bar181/practical-ai/blob/studio/component-gallery/plans/decision-support/README.md) |

### 4. Core memory system: 80 of 100

| | |
| --- | --- |
| What it is | Notes, policies, calendar facts, websites, code and repository pointers as labelled records in a store you own. Not a wiki. |
| The value | Anything you asked to be kept is found in one question, with its source. |
| Why it ranks here | A foundation for the hub, the brief and decision support. Ranked fourth because it should follow the learnings database, on the same row shape, and because the line between a record and a document needs settling first. |
| The shape | Six kinds of record to start: note, policy, calendar fact, website, code block, repository pointer. Same row shape and viewer as the learnings database. |
| Built on | Three open-source memory layers that each solve a different problem, and a warning from the field: products change their terms within months, so own the store. |
| North Star | [`plans/core-memory/README.md`](https://github.com/bar181/practical-ai/blob/studio/component-gallery/plans/core-memory/README.md) |

### 5. Rubric reviewer: 79 of 100

| | |
| --- | --- |
| What it is | Any piece of work scored out of 100 against a rubric written beforehand, with evidence for each line, by a reviewer with fresh eyes. |
| The value | "It looks good" becomes a number and a reason. |
| Why it ranks here | Small, and the project method needs it at stage 8. Six rounds of self-review here showed what goes wrong without it. Scored low on need because the owner has not asked for it. |
| The shape | A rubric format, five rubrics, and a reviewing skill that runs in a fresh session. |
| Built on | Published advice to keep doing and checking apart, and this repository's own six rounds of self-review. |
| North Star | [`plans/rubric-reviewer/README.md`](https://github.com/bar181/practical-ai/blob/studio/component-gallery/plans/rubric-reviewer/README.md). Proposed by the assistant, not asked for |

### 6. Source and link verifier: 76 of 100

| | |
| --- | --- |
| What it is | Every link in a document opened on a known date and checked against the sentence it supports. |
| The value | You are never caught citing a page that is gone or says something else. |
| Why it ranks here | The owner named link checking as what sets this work apart. It may turn out to be a step inside decision support and the weekly brief, not a tool of its own. Stage 2 decides. |
| The shape | Four results for each claim and its link: supports, partly supports, does not support, gone. |
| Built on | The repository's own link gate, which checks inside links only. Researched lightly so far. |
| North Star | [`plans/source-verifier/README.md`](https://github.com/bar181/practical-ai/blob/studio/component-gallery/plans/source-verifier/README.md). Proposed by the assistant, not asked for |

### 9. Connections hub: 66 of 100

| | |
| --- | --- |
| What it is | Reads a meeting, an email thread, a web page or a file you point it at, and files what is worth keeping as labelled records, after you review them. |
| The value | Something said on Monday is found by label on Friday, with nobody filing by hand. |
| Why it ranks here | The owner asked for it, and it will matter. It ranks ninth because it has nowhere to file until the two stores exist, and because it leans on outside products that change monthly. |
| The shape | Four sources to start: a meeting, an email thread, a web page, a file. One intake step, and a review queue. It keeps nothing itself. |
| Built on | An official meeting-notes MCP server suited to chat but not to unattended runs, and connectors for mail, calendar and drive that already exist. |
| North Star | [`plans/connections-hub/README.md`](https://github.com/bar181/practical-ai/blob/studio/component-gallery/plans/connections-hub/README.md) |

## How your five fit together

| Tool | Its job | Keeps data? | Needs first |
| --- | --- | --- | --- |
| Learnings database | Errors, redos and things that worked, one row each | Yes, in a store you own | Nothing |
| Core memory system | Things you asked to be kept, one record each | Yes, in a store you own | The learnings row shape |
| Connections hub | Reads a source, proposes records, files what you accept | No | Both stores |
| Task graph | A goal as tasks and dependencies, drawn five ways | Only the plan file, with the project | The artifact studio |
| Decision support | A decision from question to defended recommendation | Only the working folder, with the person | The studio. The task graph for its last step |

Three rules hold for all of them.

- **Storage stays outside the repository.** A file, a sheet or a database the person owns. The repository holds the shape of a record and invented examples, so it can be shared with nobody's history in it.
- **No wiki.** Nothing rewrites records into linked pages. A long document stays where it lives, and the record points to it.
- **Searched exactly first.** Labels, keywords, topics and flags come from fixed lists and are matched exactly. Similarity search is added at level 3, on Supabase, and never replaces them.

## The whole list

| # | Tool | Score | State |
| --- | --- | --- | --- |
| 1 | Learnings database | 90 | North Star, not approved. An earlier draft exists |
| 2 | Task decomposition and dependency graph | 89 | North Star, not approved |
| 3 | Decision support assistant | 82 | North Star, not approved |
| 4 | Core memory system | 80 | North Star, not approved |
| 5 | Rubric reviewer | 79 | North Star, not approved. Proposed by the assistant |
| 6 | Source and link verifier | 76 | North Star, not approved. Proposed by the assistant |
| 7 | Estimator | 71 | Draft, earlier layout |
| 8 | Proposal builder | 69 | Plan |
| 9 | Connections hub | 66 | North Star, not approved |
| 10 | Client onboarding kit | 65 | Plan |
| 11 | Weekly brief with research | 63 | Draft, earlier layout |
| 12 | Inbox triage and daily summary | 62 | Draft, earlier layout |
| 13 | Voice post drafter | 61 | Draft, earlier layout |
| 14 | Daily builder | 60 | Plan |
| 15 | Dashboard | 59 | Draft, earlier layout |
| 16 | Publishing a website | 57 | Draft, earlier layout |
| 17 | Client project tracking and support site | 55 | Plan |
| 18 | Short video guide | 54 | Draft, earlier layout |
| 19 | Training explainer with avatar | 50 | Draft, earlier layout |
| 20 | Expense form creator | 50 | Plan |
| 21 | Lead responder | 49 | Plan |
| 22 | Website chatbot | 47 | Plan |
| 23 | Training website | 45 | Plan |
| 24 | Student AI assistant | 43 | Plan |

Twelve more ideas are kept as "not scheduled". Meeting to actions is now the first source of the connections hub. The full list is in [`docs/PRIORITIES.md`](https://github.com/bar181/practical-ai/blob/studio/component-gallery/docs/PRIORITIES.md).

## How the scores are made

Five lines, 20 points each.

| Line | 20 looks like |
| --- | --- |
| Need | You would use it this week |
| Foundation | Other tools on the list are built on it |
| Reuse | Level 1 can be reached with what already exists |
| Share | It can be shared and taught with no private data in it |
| Low risk | Few outside products to depend on |

| # | Tool | Need | Foundation | Reuse | Share | Low risk | Score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Learnings database | 19 | 19 | 18 | 17 | 17 | 90 |
| 2 | Task decomposition and dependency graph | 17 | 16 | 19 | 19 | 18 | 89 |
| 3 | Decision support assistant | 18 | 13 | 17 | 18 | 16 | 82 |
| 4 | Core memory system | 17 | 18 | 15 | 15 | 15 | 80 |
| 5 | Rubric reviewer | 10 | 15 | 18 | 19 | 17 | 79 |
| 6 | Source and link verifier | 11 | 14 | 16 | 19 | 16 | 76 |
| 7 | Estimator | 15 | 8 | 16 | 16 | 16 | 71 |
| 8 | Proposal builder | 13 | 8 | 16 | 16 | 16 | 69 |
| 9 | Connections hub | 16 | 14 | 13 | 13 | 10 | 66 |
| 10 | Client onboarding kit | 13 | 6 | 15 | 15 | 16 | 65 |
| 11 | Weekly brief with research | 15 | 8 | 14 | 14 | 12 | 63 |
| 12 | Inbox triage and daily summary | 15 | 7 | 14 | 13 | 13 | 62 |

**These numbers are my judgement from what you have said.** Change any of them and the order follows. Two things I would look at first: I scored my own two proposals low on need because you did not ask for them, and I ranked the connections hub ninth although you asked for it, because it has nowhere to file until the two stores exist.

## The method, revised

| Stage | You produce | The gate |
| --- | --- | --- |
| 1. Understand | Who it is for, the one job, a North Star | The page reads true to the person who asked |
| 2. Research | What already exists, with dated sources | Build, use or build on top: decided |
| 3. Scope | In, out, the levels, a "done when" line for each item | **You approve the North Star page** |
| 4. Plan | The folder, both front doors, the gates and the rubric, before any content | The layout check passes |
| 5. Prove | One real request taken to one finished output | **You say it is what you wanted** |
| 6. Build | One source file, generated copies, then breadth | The build and the link check pass |
| 7. Verify | Worked examples, a scripted agent, every request run | The example and agent gates pass |
| 8. Score | A self-review out of 100 on the rubric written at stage 4 | Every line scored, with evidence |
| 9. Close | Clean-up, lessons logged, status final, a short report | Every gate passes. **You close it** |

What changed, and where it came from:

| Change | From |
| --- | --- |
| Research now comes before scope | What exists changes what is worth building |
| The rubric is written at stage 4, before the work | Six rounds of self-review here used three different rubrics, so their scores could not be compared |
| A closing stage with a checklist | The studio was called finished several times before anyone had cleaned up after it |
| A progress note in every tool, read at the start of a session | Published practice for agents that work across many sessions: carry the work in files, not in memory |
| A table for how much method a small tool needs | Published practice: match the ceremony to the size of the job |

The sources, with links and dates, are in `drafts/project-method/base/SOURCES.md`. The seven North Star pages are stages 1 to 3 of this method, waiting at its first stop.

## What was checked, and what was not

| Checked | Result |
| --- | --- |
| The artifact studio's ten gates, on the day of closing | All pass, including the page check: 84 of 84 at three widths |
| The project method's five gates, including one that builds a project from the new scaffold | All pass |
| Links in every Markdown file | No broken links in 198 files |
| All 12 skills against the published authoring rules | All pass |

Not checked:

- **The research is one sitting.** Each North Star lists three to six sources read today. Two of the sources on meeting tools are vendors describing their own market, and the pages say so.
- **No North Star is approved.** They are my reading of your five paragraphs. Each ends with open questions for you.
- **The method has closed one tool.** No tool has yet been built with it from stage 1.
- **Nothing new was built.** This sprint produced pages, a ranking and a revised method, as asked.

## Decisions for you

| Decision | My recommendation |
| --- | --- |
| Approve, change or reject each North Star | Start with the learnings database. It is the one the others lean on |
| The two tools I proposed | Keep the rubric reviewer. Decide on the source verifier after its research: it may be a step, not a tool |
| Where the line falls between a record and a document | Over one screen of text, keep a pointer and a description. This is what keeps memory from becoming a wiki |
| Merge pull request 1 into `main` | Yes. The studio is closed and everything described here is on the branch |
| Which store to try first for learnings | A Google Sheet. It proves the row shape before any database work |
