# Learnings database: North Star

Stages 1 to 3 of the [project method](../../drafts/project-method/base/METHOD.md). Written
15 November 2026. **Not yet approved.** This page updates the direction of the earlier
[plan](README.md) and [draft](../../drafts/learning-system/), which framed the tool as questions
and answers.

**Think of it as** a ship's log. Every time the crew hits a rock, finds a faster channel, or has to
turn back, one line goes in the log. The next crew reads it before they sail.

**North Star:** the same mistake is never made twice, and a shortcut found once is found by
everyone after.

## Understand

| | |
| --- | --- |
| Who it is for | As someone building with an AI assistant, I want what went wrong and what unexpectedly worked to be kept and found again, so that I and my agents stop relearning it |
| The one job | Capture a learning in one line at the moment it happens, and put the right ones in front of whoever starts similar work |
| The finished thing is | A product: a store you own, a skill that writes to it, and a search that reads from it |

**What counts as a learning.** Three kinds, and nothing else:

| Kind | Example |
| --- | --- |
| An error | A tool returned half of what an agent needed |
| A redo | The levels were built as full copies, then rebuilt as a base and add-ons |
| A deviation that worked | Showing failing colour samples as pictures, not text, satisfied the accessibility scan |

**What it is not.** Not a wiki, not notes, not a knowledge base. A learning is one row with a rule
in one sentence. Reference material belongs in the [core memory system](../core-memory/README.md).

## Research: what already exists

| Source | Checked | What we take from it |
| --- | --- | --- |
| [Reflexion](https://www.promptlayer.com/glossary/reflexion), a research pattern from 2023 | 15 Nov 2026 | An agent improves without retraining when its failures are written down as plain-language lessons and read before the next attempt. A lesson is text a person can read and correct |
| [Reflexio](https://www.everydev.ai/tools/reflexio/llms.txt), an open-source harness | 15 Nov 2026 | Every learned rule should be visible, reviewable and revocable. A rejected rule stops being retrieved at once |
| [Mistake Notebook Learning](https://www.alphaxiv.org/abs/2512.11485.md), a 2026 paper | 15 Nov 2026 | Group similar failures before writing the rule, so the notebook holds a few general lessons and not hundreds of near-duplicates |
| [Supabase: hybrid search](https://supabase.com/docs/guides/ai/hybrid-search) | 15 Nov 2026 | Keyword search and similarity search in one Postgres query, each with a weight. Exact terms and close meanings are both found |
| [Supabase: semantic search](https://supabase.com/docs/guides/ai/semantic-search) | 15 Nov 2026 | Similarity is combined with ordinary column filters, so labels and flags narrow the search first |
| Project "lessons learned" registers and blameless reviews | Common practice, no single source | A fixed set of columns, a named owner for each lesson, and a review on a schedule |

**Decision:** build on top of what exists. The store is a spreadsheet or a Postgres table that
others maintain. What is built here is the shape of a row, the skill that writes it, the rules for
finding it, and the habit of reading it before work starts.

## Scope

**In:** capturing a learning in under a minute; a fixed set of labels, keywords, topics and flags;
searching by those exactly; a weekly review that accepts, merges or retires rows; a "read before
you start" step for agents; similarity search at level 3.

**Out:** storing documents or notes; an agent that changes its own instructions from the log
without a person's review; analytics dashboards.

**Where the data lives:** outside this repository, always. Level 1 uses a private file or sheet you
own. The repository holds the column list and a few invented rows, so the tool can be shared
without anyone's history in it.

### One row

| Column | Holds | Searched |
| --- | --- | --- |
| `id`, `date` | A short id and when it happened | Exactly |
| `kind` | error, redo, or worked | Exactly |
| `rule` | The lesson in one sentence, written as an instruction | By keyword, and by similarity at level 3 |
| `what_happened`, `expected` | Two or three sentences each | By keyword |
| `applies_to` | Tool, project, stage or kind of task | Exactly |
| `labels`, `keywords`, `topics` | From a fixed list, a free list, and a short tree | Exactly |
| `severity` | low, medium, high | Exactly |
| `status` | proposed, accepted, merged, retired | Exactly. Only accepted rows are served to agents |
| `seen` | How many times it has happened | The measure of success: this should stop rising |
| `source` | Where it came from: a session, a review, a person | Exactly |
| `sensitive` | yes or no | Rows marked yes are never exported |

### Levels

| | Holds | Done when |
| --- | --- | --- |
| Base | The column list, the fixed labels, twelve invented rows, a one-page viewer that filters a file you open, and the rules for writing a good rule | A person can open the viewer, load the example file and find a row by label in three taps |
| Level 1 | You keep a private CSV, Excel file or Google Sheet. You paste the instructions into your assistant. When something goes wrong or works, you say "log that", and it gives you a row to paste. Before new work you paste the relevant rows in | Ten real rows are logged in a week, and one is used to avoid a repeat |
| Level 2 | A skill that writes the row itself through a Google Sheets connection, checks for a near-duplicate first, and reads accepted rows at the start of a task | The skill logs a row, finds it again by label, and raises `seen` on a repeat instead of adding a copy |
| Level 3 | Supabase: one table, full-text and vector columns, hybrid search behind an MCP server with tools to log, find and review | A question in different words from the rule still finds it, and filters by label and status are exact |

## Depends on, and feeds

- **Feeds** the [project method](../../drafts/project-method/): stage 9 writes its lessons here,
  and every stage starts by reading the rows that apply. `LESSONS.md` becomes the first import.
- **Shares its row shape** with the [core memory system](../core-memory/README.md). Build this
  first: it is the smaller of the two.
- **Fed by** the [connections hub](../connections-hub/README.md), later.

## Open questions

- Who reviews, and how often? A log nobody prunes becomes noise within a month.
- How many accepted rows can an agent usefully read at the start of a task? Start with five.
- Should a rule ever expire? Probably: a `review_by` date for anything tied to a tool's version.

## Approved

Not yet.
