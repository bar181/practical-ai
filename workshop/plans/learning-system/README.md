# Learnings database: the full plan

One-line promise: what went wrong, what had to be redone and what worked better than expected is
written down once, in a sheet you own, and put in front of you and your AI before you start
similar work.

| Complexity | Research | Level 1 | Status |
| --- | --- | --- | --- |
| Beginner (level 1) to advanced (level 3) | Done, 19 November 2026 (sources below) | Being built in [`projects/learnings-database/`](../../../projects/learnings-database/) | **Approved** by the owner, 19 November 2026 (pull request #14). Step 0 answers below |

**Think of it as** a ship's log with a good first mate. Every time the crew hits a rock, finds a
faster channel or has to turn back, one line goes in the log. At level 2 the first mate notices
the moment, writes the line, files it under the right heading and asks the captain to sign it.
Before the next voyage, the mate reads out the lines that apply.

**North Star:** the same mistake is never made twice, and a shortcut found once is found by
everyone after.

This page replaces the North Star of 15 November 2026 and the plan before it. The
[earlier draft](../../drafts/learning-system/) and the
[learning-log example](../../../projects/agentic-process/base/examples/learning-log/) are inputs to
it, not competitors: the example is where level 1 starts.

---

## The usable result (U1 to U5)

| | |
| --- | --- |
| **U1, who uses it** | A business owner, manager or builder who works with a chatbot every day, and the agents they run. Level 1 must work for a small-business student using ChatGPT with no skills or folders |
| **U2, what they give it** | A moment ("log that: the client email went out with last month's prices") or a start ("before I start the December price list") |
| **U3, what they get** | One row in their own sheet, filed under a type of learning and a topic; or, before work, the three to five accepted rules that apply, ready to paste |
| **U4, what makes it usable** | Logging takes under a minute. Nothing is written that the person did not say. Nothing is saved without their yes. The rules come back as short instructions, not an essay |
| **U5, the exception it must catch** | A repeat of a lesson already in the log: it raises `seen` on the old row instead of adding a copy. Also: a "lesson" that names a client, a person or money is marked sensitive and never leaves the sheet |

**What counts as a learning.** Three kinds, and nothing else:

| Kind | Example (invented) |
| --- | --- |
| `error` | The assistant dropped the three items priced "on request" from the price table |
| `redo` | The newsletter was rewritten because it led with the product, not the customer's problem |
| `worked` | Asking the supplier for the delivery date in writing ended the "it's coming Friday" loop |

**What it is not.** Not a wiki, not meeting notes, not a document store. Reference material
belongs in the [core memory](../core-memory/README.md) plan. A learning is one row whose `rule`
is one sentence someone can follow.

---

## What already exists, checked 19 November 2026

### Built into the chatbots

| What | What it does | What it means here |
| --- | --- | --- |
| Chatbot memory (ChatGPT, Claude, Gemini) | Remembers facts and preferences across chats | Personal and automatic. One review of Claude's memory notes it is personal, not usable team-wide, with no structured organization and no links between entries ([studiomeyer.io](https://studiomeyer.io/en/blog/ki-assistent-gedaechtnis.md)). A log you can read, filter, retire and share is a different job. The two complement each other |
| Projects (ChatGPT, Claude) | Instructions and files that every chat in the project reads | Level 1 "in a project" uses this: the skill as the instructions, the sheet as a file. A project file is read, not edited, so new rows come back to paste |
| ChatGPT and Google Drive | Since a June 2026 update, Docs, Sheets and Slides actions live in the Google Drive app, so ChatGPT can create and edit those files, not only read them; free plans have no app connections ([Tactiq, updated 1 Sep 2026](https://tactiq.io/learn/how-to-connect-google-drive-to-chatgpt)). Eligible paid users edit native Sheets with changes written back to the file ([Let's Data Science](https://letsdatascience.com/news/chatgpt-adds-direct-editing-for-google-drive-files-503e4d8d)) | Level 1 "linked to Google Drive" can append the row itself in ChatGPT on a paid plan, after the person says yes |
| ChatGPT for Google Sheets | A sidebar inside Sheets that edits the open sheet; listed for Free, Go, Plus and Pro plans as well as business plans ([Google Workspace Marketplace, page updated 31 May 2026](https://workspace.google.com/marketplace/app/chatgpt/870214997678)) | A no-connector route: work from inside the sheet |
| Claude and Google Drive | Claude reads Sheets as CSV exports through the Drive connector and can save files to Drive ([Let's Data Science](https://letsdatascience.com/news/claude-adds-gmail-sending-and-drive-management-bb1013c9)). Third-party reviews report no first-party way to append rows to an existing Sheet from a Claude chat ([Carly, 2026](https://www.usecarly.com/blog/can-claude-edit-google-sheets/)) | In Claude, level 1 reads the linked sheet and gives back the row to paste. Writing needs Claude for Google Workspace or level 3 |
| Claude for Google Workspace | Public beta on all paid Claude plans since 6 October 2026 ([Anthropic](https://claude.com/blog/claude-now-works-in-google-docs-sheets-and-slides)); in Sheets it writes formulas, builds pivot tables and charts, and adds tabs ([Anthropic](https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides)) | A Claude user can work from inside the sheet. Not tried for this plan |

### Open source and research

| What | What we take from it | Checked |
| --- | --- | --- |
| [Mem0](https://docs.mem0.ai/core-concepts/how-it-works) | Its original write path compared each new fact with the five most similar stored ones and let the model choose add, update, delete or no change ([summary of the pipeline](https://zby.github.io/commonplace/sources/mem0-memory-layer)). Its current automatic path only adds; correcting or removing is an explicit step ([Mem0 docs](https://docs.mem0.ai/core-concepts/how-it-works)). **We take:** compare before writing, propose add or merge, and leave every change of status to a person | 19 Nov 2026 |
| [Reflexion](https://www.promptlayer.com/glossary/reflexion) | An agent improves when its failures are written as plain-language lessons and read before the next attempt | 15 Nov 2026 |
| [Reflexio](https://www.everydev.ai/tools/reflexio/llms.txt) | Every learned rule is visible, reviewable and revocable; a rejected rule stops being served at once | 15 Nov 2026 |
| [Mistake Notebook Learning](https://www.alphaxiv.org/abs/2512.11485.md) | Group similar failures before writing the rule, so the notebook holds a few general lessons, not hundreds of near-copies | 15 Nov 2026 |

### Practice

| Practice | What we take | Source |
| --- | --- | --- |
| Lessons learned registers | Record what worked as well as what failed, and use the register when the next piece of work starts. Many organizations file lessons by phase or by knowledge area, such as risk, cost, scope or communications | [projectmanagementdocs.com](https://www.projectmanagementdocs.com/?p=347), [Rework](https://resources.rework.com/libraries/project-management/lessons-learned) |
| Known error databases | A draft is approved by a named owner before it counts; entries are reviewed on a schedule | [earlier landscape review](../../drafts/learning-system/landscape-review.md), 15 Nov 2026 |
| Classifying with a model against a fixed list | Give each label a description, keep labels specific and not overlapping, add an "other" choice so the model is not forced into the least-wrong label, and send low-confidence results for review ([Braindrip course](https://braindrip-web.vercel.app/courses/prompt-engineering/structured-output-and-format-control/classification-and-labeling-output), [Inference.net docs](https://docs.inference.net/use-cases/classification/zero-shot)) | 19 Nov 2026 |

### Databases and connections for level 3

| What | What it gives | Caution | Checked |
| --- | --- | --- | --- |
| [Supabase MCP server](https://supabase.com/docs/guides/ai-tools/mcp) | Official; hosted, with OAuth; listed in Claude's connectors since 3 Feb 2026 ([Supabase](https://supabase.com/blog/supabase-is-now-an-official-claude-connector)); tools include `list_tables`, `apply_migration`, `execute_sql` | Writing tools are on by default. Supabase recommends read-only mode, which runs `execute_sql` as a read-only Postgres user ([GitHub](https://github.com/supabase/mcp)). Its own description warns that query results may hold untrusted data ([PolicyLayer](https://policylayer.com/tools/supabase.md)) | 19 Nov 2026 |
| [Supabase hybrid search](https://supabase.com/docs/guides/ai/hybrid-search) | Keyword and similarity search in one query, each weighted; similarity combined with ordinary filters | Confirm current pricing at step 4.1 | 15 Nov 2026 |
| Google Sheets MCP servers | Community and hosted servers that read, write and append rows (for example [mcp-gdrive](https://claudemarketplaces.com/mcp/isaacphi/mcp-gdrive)) | Third-party code with access to your Drive: read every file before use, never install unread | 19 Nov 2026 |

**Decision (the reuse check):** nothing existing does the whole job. Memory is personal and
opaque; registers are templates without the habit; memory libraries automate what this tool
deliberately leaves to a person. So: **build a thin `SKILL.md` on top of a sheet** (level 1),
**make it notice, file and merge** (level 2), and **connect it to a real database through an
existing MCP server or a thin one of our own** (level 3). Buy nothing for levels 1 and 2.

---

## One row, the same at every level

The same columns at every level, so a level 1 sheet imports into level 3 unchanged. Level 1 fills
the first sixteen; level 2 adds `confidence` and `review_by`; level 3 adds what the database needs.
`why` was added on 19 November 2026 from the research: an after-action review asks what was
supposed to happen, what happened, **why**, and what to do next time.

| # | Column | Holds | Who fills it |
| --- | --- | --- | --- |
| 1 | `id` | `L-` and the next number | The assistant |
| 2 | `date` | When it happened, YYYY-MM-DD | The assistant, from the person |
| 3 | `kind` | `error`, `redo` or `worked` | The assistant |
| 4 | `area` | **The type of learning**, one from the Areas list (below) | The assistant; the person confirms |
| 5 | `project` | **The topic it belongs to:** a project, client job, product or process name, from the Projects list or `new:` | The assistant; the person confirms |
| 6 | `lesson_type` | **What sort of lesson it is**, one from the Lesson types list (below) | The assistant |
| 7 | `rule` | The lesson as one instruction: "When ..., do ..." | The assistant; the person may edit |
| 8 | `what_happened` | Two or three sentences | The assistant, from the person's words |
| 9 | `expected` | Two or three sentences; for `worked`, the usual way | The assistant, from the person's words |
| 10 | `why` | Why it happened, in a sentence: the cause, not the person | The assistant, from the person's words; empty if unknown |
| 11 | `tags` | Three to six search words, separated by `;` | The assistant |
| 12 | `severity` | `low`, `medium`, `high`: what a repeat would cost | The assistant; the person confirms |
| 13 | `status` | `proposed`, `accepted`, `merged`, `retired` | Always `proposed` on a new row. Only the person changes it |
| 14 | `seen` | How many times it has happened. Should stop rising | The assistant raises it on a repeat |
| 15 | `source` | `chat`, `review`, `person`, `agent` | The assistant |
| 16 | `sensitive` | `yes` if it names a client, a person, money or anything private | The assistant; empty counts as `yes` |
| 17 | `confidence` | Level 2: `high`, `medium`, `low` for the filing in columns 4 to 6 | The assistant |
| 18 | `review_by` | Level 2: a date to check the rule still holds, for rules tied to a tool's version or a price | The assistant proposes; the person sets |

### The flags: type of learning and topic

Two fixed lists and one growing list, kept on a `Lists` tab in the sheet so the person can edit
them without touching the instructions. The assistant may only use what is on the lists; anything
else is written `new:<word>` and offered to the person to add.

**Areas (the type of learning).** One per row. Each has a one-line description the assistant
reads, so the boundaries do not overlap.

| Area | Holds lessons about |
| --- | --- |
| `marketing` | Messages, posts, campaigns, the website, brand and audience |
| `sales` | Leads, quotes, proposals, follow-up and pricing to a customer |
| `customers` | Service, complaints, onboarding and what customers actually want |
| `decisions` | How a choice was made: the options, the evidence, what we would weigh differently |
| `operations` | Suppliers, scheduling, delivery and the steps of the work itself |
| `finance` | Invoices, payments, costs, budgets and the numbers behind them |
| `people` | Hiring, delegating, training and working with a team or contractor |
| `coding` | Software, scripts, spreadsheets with formulas, and building with agents |
| `working-with-ai` | Prompts, instructions, checking AI output and what a chatbot gets wrong |
| `other` | Anything that fits none of the above. Three `other` rows on the same theme suggest a new area |

**Lesson types (what sort of lesson).** One per row.

| Lesson type | Means |
| --- | --- |
| `process` | A step was missing, in the wrong order or done twice |
| `tool` | A tool, app or platform behaved in a way we did not expect |
| `instruction` | How something was asked, of a person or an AI, decided the result |
| `check` | A check would have caught it, or did |
| `judgement` | A rule of thumb for a decision |
| `communication` | Who was told what, when, and how |
| `insight` | Something learned about customers, the market or the work that changes what we do |

**Projects (the topic).** A growing list: client jobs, products, internal projects, and named
processes such as `month-end` or `website`. For coding, the repository or app name. A row with no
project is allowed and means "applies everywhere".

**Example (invented):** "log that: the agent rebuilt the whole page when I asked for one fix" is
filed `kind=redo`, `area=coding`, `project=company-website`, `lesson_type=instruction`, rule
"When asking an agent for one fix, name the file and say leave everything else as it is."

### The questions it must answer exactly

Filters, not guesses: the same question on the same sheet always returns the same rows.

| Question | Filter |
| --- | --- |
| Before I start work on X | `status = accepted`, and `project` is X or empty, and the `area` of the work; newest and most `seen` first; at most five |
| What have we learned about marketing? | `area = marketing`, `status = accepted` |
| What keeps going wrong? | `kind = error`, `seen > 2` |
| What worked that we did not expect? | `kind = worked` |
| What is waiting for review? | `status = proposed` |
| What is due for a re-check? | `review_by` is on or before today |
| What may never leave the sheet? | `sensitive = yes` or empty |

At level 3 one more kind of question is added, and only one: "anything like this?", answered by
similarity and then narrowed by the same filters.

---

## The levels

| Level | What it is | Earns its place because |
| --- | --- | --- |
| **Base** | The column list, the three lists, a sheet template (`.xlsx` and `.csv`) with twelve invented rows, and the rules for writing a good rule | Anyone can see the shape before using it |
| **Level 1, a spreadsheet** | One `SKILL.md` that logs and finds, working with the sheet in one of three places (below). The assistant writes the row; the person saves it | It works in any chatbot, free, today |
| **Level 2, smart learning** | The same skill, saved, that notices learning moments, files each under area, lesson type and project with a confidence, finds repeats and proposes merges, serves rules before work, and runs a weekly review | It removes the remembering and the filing, which is why logs die |
| **Level 3, a real database** | The same rows in Supabase, a Google Sheet written through a connection, or a company database, behind a few MCP tools: log, find, review, and change a status with the person's approval | It removes the copy and paste, works for agents, and finds lessons by meaning |

### Level 1: where the sheet lives

All three use the same `SKILL.md` and the same columns. The person picks one.

| Where | How it works | Writes | Best for |
| --- | --- | --- | --- |
| **A. In a project** (recommended start) | Create a ChatGPT or Claude project. Paste `SKILL.md` as the project's instructions and add the sheet (`.xlsx` or `.csv`) as a project file. Every chat in the project reads the log | The assistant gives the new row as one line to paste, and on request a whole updated file to replace the project's copy | Daily use without connections, on any plan with projects |
| **B. Uploaded** (proof of concept and fallback only) | Attach the sheet to a chat with `SKILL.md` | The assistant gives the row to paste, or an updated file to download | Trying it once, or when nothing else is available. The person must keep the newest copy themselves |
| **C. Linked through Google Drive** | Connect Google Drive and point the assistant at the sheet | **ChatGPT, paid plans:** the assistant appends the row to the Google Sheet itself, after the person says yes. **Claude:** the Drive connector reads the sheet; the assistant gives the row to paste, or the person works from inside the sheet with Claude for Google Workspace. **Free ChatGPT:** no connections; use A, B or the ChatGPT sidebar in Sheets | People whose work already lives in Google Workspace |

Not checked for this plan: Gemini, Microsoft Copilot, and OneDrive or SharePoint. Each is tried at
step 2.6 before the README claims it.

### Level 2: smart learning

Five behaviours, added to the same `SKILL.md` (with the lists in `flags.md`) and saved as
a Claude skill or a ChatGPT project, so nothing is pasted again.

1. **Notice.** When the conversation shows a learning moment (the person corrects the assistant,
   says "that didn't work", redoes something, or says something went better than usual), it
   offers once: "That sounds like a lesson. Log it?" It never logs without a yes, and never asks
   twice about the same moment.
2. **File.** It chooses `area`, `lesson_type` and `project` from the lists, using each label's
   description, and gives a `confidence`. A `low` confidence, or two areas that fit equally, is
   asked about in one line ("Marketing or sales?"). A word not on a list is written `new:` and
   offered for the list.
3. **Merge, don't copy.** Before proposing a row it searches the sheet for rows with the same
   `area` and `project` whose `rule` or `tags` share the key words. If one says the same thing it
   proposes "seen again" (raise that row's `seen` by one) or a merged rule, instead of a new row. It never deletes; a person retires.
4. **Serve.** "Before I start ..." returns at most five accepted, non-sensitive rules for that
   project and area, as a block headed "Rules from the log" to paste into the next chat or an
   agent's instructions, and says how many more matched.
5. **Review.** "Weekly review" lists proposed rows with one suggestion each (accept, merge into a
   named row, retire, with a reason), rows past `review_by`, and any `other` theme seen three
   times. The person decides; at level 1 and 2 they change the sheet themselves, or approve the
   assistant's edit where it can write (ChatGPT with Drive).

**What "smart" does not mean here:** it does not watch every conversation in the background, it
does not change its own instructions, and it does not decide what is true. Those are the choices
that make memory tools hard to trust; this tool leaves them with the person.

### Level 3: a real database

One table with the same columns, plus what a database adds, and four tools.

| Part | Design |
| --- | --- |
| **Table** | `learnings`: the 18 columns, plus `created_at`, `updated_at`, `last_seen`, `owner`, a full-text column over `rule`, `what_happened`, `expected`, `tags`, and an embedding column for similarity |
| **What agents may read** | A view, `served_rules`: `status = accepted` and `sensitive = no` only |
| **Tools (MCP)** | `log_learning` (inserts, always as `proposed`), `find_learnings` (the filters above, plus "anything like this?" by hybrid search), `review_queue`, and `set_status` (only after the person approves in the chat) |
| **Targets, in order** | 1. **Supabase**, for the owner's own use: Postgres with full-text and vector search, its official MCP server in read-only mode for reading, and writes only through two database functions (`log_learning`, `set_status`) so an agent never runs free SQL that writes. 2. **Google Sheets** for teams who stay in Workspace: a Sheets MCP server, or a small Apps Script endpoint, with the same four tools over the same tab. 3. **A company database**: the same table and tools through the MCP server the company already runs |
| **Agents** | Coding agents read the rules before work: one line in the project's `AGENTS.md` ("Before you start, call `find_learnings` for this project and follow the accepted rules"), or a session-start hook where the agent supports one |
| **Import** | The level 1 sheet, exported as CSV, loads unchanged |

---

## Step by step, with a definition of done

Each step names its files and what "done" means. A step is done only when every line of its
definition of done is true and recorded. Steps follow the nine steps of
[Agentic Process](../../../projects/agentic-process/base/PROCESS.md), grouped by level. A person
approves anything sent, posted, published or merged.

### Step 0: the owner's gates

| | |
| --- | --- |
| **Do** | The owner answers the [open questions](#open-questions-for-the-owner) and approves this plan |
| **Definition of done** | Every gate below is ticked or changed in this file. The "Status" line at the top reads "Approved" with the date |

The owner approved the plan by merging it and asked for the build to start, without answering the
open questions one by one. The defaults below were chosen by Claude on 19 November 2026 and stand
until the owner changes them.

- [x] The ten areas and seven lesson types, as listed
- [x] The product name is "Learnings database"; the project folder is `projects/learnings-database/`
- [x] Level 3's first target is Supabase (Postgres with pgvector); tested on a local Postgres 16 with pgvector
- [x] The weekly review is the owner's; the day is the owner's choice
- [x] The [learning-log example](../../../projects/agentic-process/base/examples/learning-log/) stays as Agentic Process's worked example
- [x] Open questions, defaults: `owner` only at level 3; "before I start" returns five rules in a chat and up to ten for agents; a rule expires only when it has a `review_by` date; the first repository to read the log is this one

**Added from the research of 19 November 2026** (sources in [the build's evidence](../../../projects/learnings-database/quality-results/README.md)):
search before writing and capture in the person's own words (Knowledge-Centered Service); a `why`
column (the after-action review); a history of every change, where each row came from, and a
person's review before a row is trusted, because memory an agent reads is an attack surface (OWASP
ASI06, memory and context poisoning).

### Level 1, base and spreadsheet

**Step 1.1: the base files**

| | |
| --- | --- |
| **Do** | Create `projects/learnings-database/base/`: `template/learnings.xlsx` with three tabs (`Learnings`, `Lists`, `How to use`), the same as `learnings.csv`, twelve invented rows covering all three kinds and at least six areas, and `flags.md` with the lists and their descriptions |
| **Definition of done** | The `.xlsx` opens in Excel and imports into Google Sheets with its tabs. The header matches the 16 level 1 columns exactly. Every row is invented and says so on the `How to use` tab. The `Lists` tab and `flags.md` agree, checked by a script in `_build/` |

**Step 1.2: the `SKILL.md`**

| | |
| --- | --- |
| **Do** | Write `base/SKILL.md` from the learning-log example: the v2 columns, the three kinds, the area and lesson type lists inline (so it works pasted alone), Log, Find and Before I start, the one-reply question for missing input, and the three storage paths of level 1 |
| **Definition of done** | It is one file, in the open Agent Skills format, under 300 lines, with `name: learnings-database`. Pasted alone into a fresh chat with no sheet, it asks for what is missing in one reply. It never sets `status` to anything but `proposed`. It names its output shape: one CSV line, the same as a two-column table, then the repeat check |

**Step 1.3: the three storage paths**

| | |
| --- | --- |
| **Do** | Write the README section "Where your log lives": A (project), B (upload), C (Google Drive), each with five numbered steps a beginner can follow, and what writes where on which plan |
| **Definition of done** | Each path has been followed once by someone other than the author, or is marked "not yet tried". Path C states plainly that a Claude chat reads the sheet but does not append to it |

**Step 1.4: the worked example**

| | |
| --- | --- |
| **Do** | Run the normal case in a fresh chat with only the README and `SKILL.md`; save the unedited result in `base/examples/` |
| **Definition of done** | The example is unedited, uses invented data, and shows a row, its table, and a repeat found |

**Step 1.5: verify level 1**

| | |
| --- | --- |
| **Do** | In fresh sessions, with only what the README tells the person to paste, run: (1) missing input; (2) the normal case; (3) a repeat, which must raise `seen`; (4) a lesson naming a client and an amount, which must be `sensitive = yes` and kept out of the "Rules from the log" block; (5) an opinion that is not a learning, which must be declined in one line |
| **Definition of done** | All five pass in Claude, and in ChatGPT on a free plan using path A or B. Each run is recorded in `quality-results/README.md`: who ran it, where, what happened. Anything failed is fixed and rerun, at most twice |

### Level 2, smart learning

**Step 2.1: the filing rules**

| | |
| --- | --- |
| **Do** | Add to `SKILL.md` and `flags.md`: label descriptions, `confidence`, the one-line question for a close call, and `new:` proposals |
| **Definition of done** | Every area and lesson type has a description of one line, written so no two overlap. The skill asks rather than guesses when confidence is low |

**Step 2.2: a test set for filing**

| | |
| --- | --- |
| **Do** | Write `_build/eval/filing-cases.csv`: 40 invented learnings, at least three per area, each with the expected `area`, `lesson_type` and `project`, including five close calls and five that are not learnings |
| **Definition of done** | The cases are reviewed by the owner before the skill is tested on them, so the answers are not written to fit |

**Step 2.3: notice, merge, serve, review**

| | |
| --- | --- |
| **Do** | Add the four other behaviours to `SKILL.md`, with the merge rule (same area and project, shared key words) and the review output shape |
| **Definition of done** | On a sheet of 30 invented rows: a repeat is found and `seen` raised; a near-repeat is offered as a merged rule; "before I start" returns at most five accepted, non-sensitive rows; the review lists every proposed row once with one suggestion |

**Step 2.4: measure filing**

| | |
| --- | --- |
| **Do** | Run the 40 cases in fresh chats in Claude and ChatGPT; score with `_build/eval/score_filing.py` |
| **Definition of done** | `area` right on at least 36 of 40, `lesson_type` on at least 32, every non-learning declined, every low-confidence case asked about. Results recorded with the date and the chatbot |

**Step 2.5: save it**

| | |
| --- | --- |
| **Do** | Package `level-2-files/`: the skill folder for Claude (`SKILL.md` plus `references/`), and a ChatGPT project setup (instructions and the sheet). For ChatGPT with Drive, the steps to let it append rows after a yes |
| **Definition of done** | A person sets each up from the README alone in under ten minutes, recorded once for each. The skill never writes to a sheet without the person's yes in the same chat |

**Step 2.6: real use**

| | |
| --- | --- |
| **Do** | The owner uses level 2 for two weeks of normal work |
| **Definition of done** | At least 15 real rows, at least one weekly review run, and at least one rule served before work and followed. What went wrong is logged in the log itself, and the README status says who has used it |

### Level 3, a real database

**Step 3.1: choose and price**

| | |
| --- | --- |
| **Do** | Confirm current Supabase plans and limits, and how embeddings will be made (a model the owner already pays for, or Supabase's own) |
| **Definition of done** | The cost of a 1,000-row log is written here with the date checked, and the owner accepts it |

**Step 3.2: the schema**

| | |
| --- | --- |
| **Do** | Write `level-3-files/supabase/schema.sql`: the table, full-text and vector columns, indexes, the `served_rules` view, row-level security, and two functions, `log_learning` (forces `status = proposed`) and `set_status` |
| **Definition of done** | It runs cleanly on an empty project. A read-only role can read `served_rules` and nothing that is `sensitive`. An insert that tries `status = accepted` is stored as `proposed`. Tested with SQL in `_build/tests/` |

**Step 3.3: the tools**

| | |
| --- | --- |
| **Do** | Expose `log_learning`, `find_learnings`, `review_queue`, `set_status` as MCP tools: either the official Supabase MCP server in read-only mode plus the two functions, or a thin server of our own if that is not enough. Decide by trying the official server first |
| **Definition of done** | From a Claude chat with only the connection: a row is logged as `proposed`; it is found by a filter; it is found by a question in different words; `set_status` runs only after the person's yes in that chat; no tool can run free SQL that writes |

**Step 3.4: import and hybrid search**

| | |
| --- | --- |
| **Do** | Write `_build/import_csv.py` (level 1 CSV in, rows out, embeddings made) and the hybrid search query |
| **Definition of done** | The 30-row test sheet imports unchanged. Ten paraphrased questions each find their intended row in the first three results, with filters applied exactly |

**Step 3.5: the Google Sheets and company options**

| | |
| --- | --- |
| **Do** | Write the same four tools over a Google Sheet (a reviewed Sheets MCP server or an Apps Script endpoint), and a page on using a company's own database |
| **Definition of done** | The Sheets route logs and finds a row from a Claude chat, or is marked "not built" with the reason. Any third-party server was read in full before use, and its source, version and licence are recorded |

**Step 3.6: agents read before they start**

| | |
| --- | --- |
| **Do** | Add the `AGENTS.md` line and, where supported, a session-start hook, to one real repository of the owner's |
| **Definition of done** | In three agent sessions, the agent called `find_learnings` before its first change and named the rules it followed |

### Shipping it

**Step 4.1: the project**

| | |
| --- | --- |
| **Do** | Create `projects/learnings-database/` to the repository layout: `README.md` (a product page), `AGENTS.md`, `CLAUDE.md`, `LICENSE`, `base/`, `level-2-files/`, `level-3-files/`, `quality-results/README.md`, `_build/` |
| **Definition of done** | `python3 workshop/tools/check_project.py projects/learnings-database` and `python3 workshop/tools/check_links.py .` pass. The README status says who has and has not tried each level |

**Step 4.2: the explainer**

| | |
| --- | --- |
| **Do** | Make `docs/reports/learnings-database.html` with Artifact Studio from the README |
| **Definition of done** | It opens offline, reads at phone width, and every number on it is in the README |

**Step 4.3: the indexes**

| | |
| --- | --- |
| **Do** | Update the root README, `docs/README.md`, `docs/reports/README.md` and the [plans index](../README.md); point [core memory](../core-memory/README.md) and the [connections hub](../connections-hub/README.md) at the project |
| **Definition of done** | No page calls it a plan after it ships. The pull request is opened, and the owner merges it |

---

## Costs

| Level | Costs |
| --- | --- |
| 1 | Nothing beyond the chatbot. Path C writing in ChatGPT needs a paid plan; Claude for Google Workspace needs a paid Claude plan |
| 2 | Nothing new |
| 3 | A Supabase project and embeddings: priced at step 3.1, not before |

## Risks and how the plan handles them

| Risk | Handled by |
| --- | --- |
| Nobody reviews, and the log becomes noise | The weekly review is a gate in step 0; `seen` and `review_by` show what matters |
| The filing is wrong and nobody notices | Fixed lists with descriptions, a confidence, a question on close calls, and the 40-case test at step 2.4 |
| Private details leak into a pasted block or to an agent | `sensitive`, empty counted as `yes`, never served; the `served_rules` view at level 3 |
| An agent writes or changes the log on its own | Only `proposed` can be written; only the person changes a status; no free SQL that writes |
| Text in the log tells an agent what to do | Rows are data, never instructions. The skill and the tools say so, as the Supabase server's own description warns |
| Claims about chatbots go stale | Every claim in the README carries the date it was checked, and step 1.5 tests before it claims |

## Open questions for the owner

- Are the ten areas right for your students and your own work? Add or drop before step 1.1.
- Should rows hold who logged them (`owner`) at level 1, or only at level 3?
- How many rules should "before I start" return: five, or three for chat and ten for agents?
- Should a rule expire by default after a time, or only when it has a `review_by` date?
- For your own use, which repository should be the first to read the log at step 3.6?
