<p align="center"><img src="_build/img/icon.png" width="104" alt="Learnings database icon: a ruled page with a tick"></p>

<h1 align="center">Learnings database</h1>

<p align="center"><b>Stop making the same mistake twice.</b><br>
Say "log that" when something goes wrong, has to be redone, or works better than usual. Get the
rules back before similar work starts.</p>

<p align="center"><b>Free</b> &nbsp;·&nbsp; <b>For Claude, ChatGPT and other chatbots</b> &nbsp;·&nbsp; <b>Your log stays in your own file</b><br><b>Tested in Claude</b> &nbsp;·&nbsp; <b>Not yet used by a person</b></p>

**Think of it as** a ship's log: one line each time the crew hits a rock or finds a faster channel,
read by the next crew before they sail.

- **One line to log.** Tell your chatbot what happened and what you expected. You get one row,
  filed by the type of learning (marketing, sales, finance, coding and six more) and the kind of
  lesson, with the lesson written as an instruction: "When ..., do ...".
- **Fewer duplicates.** When your log is attached, it searches it first. If the lesson is already
  there, it counts it again instead of adding a row, so you can see what keeps happening.
- **The rules come back when you ask.** Say "before I start the price update" and get the
  rules that apply, as a block to paste into the next chat or an agent's instructions.
- **You stay in charge.** It asks before saving anything, and nothing is used as a rule until you
  accept it at a five-minute weekly review. It is told to remove names and contact details and to
  mark anything about a client, a person or money as sensitive: check each row before you keep it.

## Get started: try it now

Copy this into Claude, ChatGPT or another chatbot that can open links. It loads the instructions
from this folder, so you always get the latest version. Attach your log if you have one (the
paperclip or **+** button beside the message box); if not, you get a starter file. **Can't open
links?** Paste the instructions instead: see below the box.

```
Read the instructions at this link and follow them for the rest of this chat:
https://raw.githubusercontent.com/bar181/practical-ai/main/projects/learnings-database/base/SKILL.md

My log is attached. If I have not attached one, give me the starter file first.

log that: the email to all our customers about holiday opening hours went out with last year's dates. I expected this year's dates. We copied last year's email and only changed the subject. It belongs to the newsletter.
```

**If your chatbot cannot open links, or the link does not load:** open
[`base/SKILL.md`](base/SKILL.md), press **Raw** (the button above the text that shows the plain
file), copy all of it, paste it into a new chat, then add your "log that" message. The same prompt as a file:
[`base/try-it-prompt.txt`](base/try-it-prompt.txt).

**What you get back** is one line to paste under your log, the same row as a table, and a few lines
on what it checked. A real, unedited reply: [`base/examples/logging-a-lesson.md`](base/examples/logging-a-lesson.md).

**Then keep the row.**

1. The first time, download the starter file, [`learnings.xlsx`](base/template/learnings.xlsx), and
   keep it somewhere private: your computer, or your own Google Drive. Delete its twelve invented
   example rows.
2. Copy the line it gives you. In Excel, paste it in column A of the first empty row and use
   **Data > Text to Columns** with comma as the separator. In Google Sheets, paste it in column A
   and use **Data > Split text to columns**. Each value lands in its own column.
3. Next time, attach the file again, so it can spot a repeat and use your projects.

The first time takes about ten minutes; after that, about a minute a lesson. Each row gets an id
such as `L-9`, so you can refer to it later. If a lesson lands across two columns when you split
it, ask the chatbot for "the row as tab-separated" and paste that instead.

## What to say

| You say | You get |
| --- | --- |
| `log that: [what happened]. I expected [what you expected].` | One row, or "this is a repeat of L-9" with its count raised |
| `before I start [the work]` | At most five accepted rules that apply, and a block to paste |
| `weekly review` | The rows waiting for you, each with a suggestion: accept, merge with another row, or retire (stop using it) |
| `what keeps going wrong?` | Errors seen more than twice |
| `what have we learned about [an area or project]?` | The accepted rules for it |

When you correct its work in a chat that has these instructions, it does what you asked, then
offers once: "That sounds like a lesson for your log. Log it?"

## For a technical helper: where your log lives

Pick the first that fits. You can move up later without retyping: the columns are the same
everywhere, and [`csv_sync.py`](level-3-files/csv_sync.py) moves rows between a sheet and a database.

| Level | Your log is | Set up | Saving a row |
| --- | --- | --- | --- |
| 1 | A spreadsheet you attach or paste: [`learnings.xlsx`](base/template/learnings.xlsx) (with the lists on their own tab) or [`learnings.csv`](base/template/learnings.csv) | None | You paste the line it gives you |
| 2 | The same file, saved with the instructions: a [Claude skill or plugin](level-2-files/README.md), a [ChatGPT project](level-2-files/chatgpt-project/instructions.md), a [Google Sheet](level-2-files/google-drive.md) or a file in a folder your assistant can write to | About five minutes, once | Where it can write (a folder, an editable Google Sheet), it adds the row after your yes |
| 3 | A database, through a small [MCP server](level-3-files/README.md): one file in your folder (recommended), or a shared Postgres or Supabase database for a team | About fifteen minutes; needs Python | Saved as `proposed` after your yes; you accept it at the review |

**Searching by meaning** is optional at level 3, with any embedding service. Without it, finding is
by filters and words, which is exact and enough for a log of hundreds or thousands of rows.

## What it is not

The learning side only. It is not a wiki or knowledge base, not memory of your preferences, not a
note-taking app and not a coding tool. It keeps one thing: what to do differently next time,
approved by you. Chatbot memory and these tools can sit beside it.

## Status

**19 November 2026. Built and tested by Claude only. No person has used it yet.**

| Tried | Result |
| --- | --- |
| Filing 40 invented messages, each in a fresh Claude session with only the instructions | Final run: area right 40 of 40, lesson type 37 of 40, every non-lesson declined |
| Eleven behaviour cases in fresh Claude sessions: a vague request, a repeat, a name and an amount, not a lesson, before I start, the review, noticing a lesson, a row that gives orders, the link start, a folder it can write to | 11 of 11 |
| Level 3 on a real file database and a real Postgres with pgvector, including an MCP client | 29 of 29 and 35 of 35 checks |
| The Claude plugin | Passes `claude plugin validate`. Not yet installed by a person |

**Not yet tried:** loading the instructions by the link (it works only once this folder is on the
main branch), ChatGPT, Google Sheets (including how a pasted row splits into columns), a hosted
Supabase project, searching by meaning with a real embedding model, and use by a real person on a
real log. The details and the known weak spots: [quality results](quality-results/README.md).

## Questions

**Where is my data?** Wherever you keep the log: your file, your sheet, your folder or your
database. Nothing is stored in this repository. When you attach the log to a chat, the chatbot's
company handles it like anything else you send there, so keep client details out of it or mark
them sensitive.

**Why a link and not an app?** The instructions are the tool. A link means every chat gets the
latest version, reviewed by a person before it reaches the main branch. You can always paste a copy
instead and keep it as it is.

**What does it cost?** Nothing beyond the chatbot you already use. Level 3 runs on your computer, or
on a database you already pay for.

**How is it different from my chatbot's memory?** Memory keeps facts about you, automatically.
This keeps rules for the work, filed so you can filter them, counted so you can see what repeats,
and used only after you accept them.

---

Built with [Agentic Process](../agentic-process/). The plan and the research behind it:
[`workshop/plans/learning-system/`](../../workshop/plans/learning-system/README.md).
Examples use invented data. Licence: [Apache 2.0](LICENSE).
