# Core memory system: North Star

Stages 1 to 3 of the [project method](../../drafts/project-method/base/METHOD.md). Written
15 November 2026. **Not yet approved.** Complexity: intermediate to advanced.

**Think of it as** a filing cabinet with a good clerk. Each thing you want kept goes in one folder
with a label on the tab. Ask the clerk for "the travel policy" or "everything about that client
since June" and the right folders come back, with where each came from.

**North Star:** anything you told your assistant to keep can be found again in one question, by you
or by an agent, with its source attached.

## Understand

| | |
| --- | --- |
| Who it is for | As a consultant or owner, I want notes, policies, calendar facts, useful sites, code and repository pointers kept in one store I own, so that any assistant I use can find them |
| The one job | Keep a record with enough labels that it can be found exactly, and return it with its source |
| The finished thing is | A product: a store you own, a skill that files into it, and a search that reads from it |

**What goes in.** Six kinds to start: a note, a policy, a calendar fact, a website, a code block,
a repository pointer. Each is one record.

**What it is not.** It is **not a wiki**. Records are not rewritten into linked pages, and nothing
is summarised into articles. It is not a document store either: a long document stays where it
lives, and the record holds a pointer and a short description. It is separate from the
[learnings database](../learning-system/NORTH-STAR.md), which holds only mistakes, redos and things
that worked.

## Research: what already exists

| Source | Checked | What we take from it |
| --- | --- | --- |
| [A comparison of Mem0, Letta and Zep](https://dev.to/plur9/mem0-vs-letta-vs-zep-which-should-you-use-for-agent-memory-1n8m) | 15 Nov 2026 | The three best-known open-source memory layers solve different problems: simple recall, an agent that manages its own state, and facts that change over time. Choose by the question you need answered |
| [Developers Digest: memory providers compared](https://www.developersdigest.tech/blog/best-ai-agent-memory-providers-2026) | 15 Nov 2026 | Mem0 extracts and retrieves. Zep's open engine, Graphiti, keeps a graph of facts with times. Letta lets the agent edit its own memory |
| [Techsy: memory tools](https://techsy.io/en/blog/best-ai-agent-memory-tools) | 15 Nov 2026 | Products in this field change their terms within months. One retired its self-hosted edition. Own the store, and treat any layer above it as replaceable |
| [A guide to agent knowledge systems](https://dev.to/sebastian_chedal/agent-memory-038-knowledge-systems-compared-2026-guide-568p) | 15 Nov 2026 | Ask five questions before picking a system. "Build it yourself on files" is a real option, and is the path this project leaves to others |
| [Supabase: hybrid search](https://supabase.com/docs/guides/ai/hybrid-search) | 15 Nov 2026 | One Postgres table can answer by keyword and by meaning together |

**Decision:** build on top of what exists, and stay small. The store is a sheet or a Postgres
table. No memory framework is adopted at levels 1 and 2. At level 3 the table is plain enough that
a framework could be put in front of it later.

## Scope

**In:** filing a record in one sentence ("keep this"); labels, keywords, topics and flags on every
record; exact search by those; a source and a date on everything returned; similarity search at
level 3; a way to forget.

**Out:** rewriting records into pages; storing whole documents, transcripts or mailboxes; deciding
for the person what is worth keeping.

**Where the data lives:** outside this repository, always. The repository holds the column list
and invented example records only.

### One record

The same shape as a learning, so one viewer and one search serve both.

| Column | Holds |
| --- | --- |
| `id`, `date`, `updated` | A short id, when filed, when last changed |
| `kind` | note, policy, calendar, website, code, repository |
| `title`, `body` | A line, and the content or a short description of it |
| `pointer` | Where the full thing lives: a link, a path, a repository address |
| `labels`, `keywords`, `topics` | From a fixed list, a free list, and a short tree |
| `source` | Who or what supplied it, and when |
| `valid_from`, `review_by` | For anything that goes out of date, such as a policy or a price |
| `status` | current, superseded, forgotten |
| `sensitive` | yes or no. Rows marked yes are never exported or sent to a hosted model without a person's say |

### Questions it must answer exactly

| Question | How it is answered |
| --- | --- |
| What is our policy on this? | `kind = policy`, `topics` contains it, `status = current` |
| Everything about one client or project | `labels` contains it, any kind, newest first |
| Which sites did I save on this subject? | `kind = website` and `topics` |
| What is due for review this month? | `review_by` within the month |
| Where is the code we used for that? | `kind = code` or `repository`, by `keywords` |
| What did this record replace? | `status = superseded`, linked by id |

Similarity search, at level 3, answers "anything like this?" and is then narrowed by the same
filters. It never replaces them.

### Levels

| | Holds | Done when |
| --- | --- | --- |
| Base | The column list, the six kinds, twenty invented records, the same one-page viewer as the learnings database, and rules for a good title and label | A person finds a record by kind and label in three taps |
| Level 1 | A private file or Google Sheet you own. You paste the instructions into your assistant, say "keep this", and paste the row it gives you. To recall, you paste the sheet or a filtered part of it | Twenty real records filed in a week, and five found again on request |
| Level 2 | A skill that files and finds through a Google Sheets connection, marks an older record superseded when a newer one replaces it, and always returns the source | A superseded policy is not returned as current |
| Level 3 | Supabase with full-text and vector columns behind an MCP server: keep, find, supersede, forget | A question in different words finds the record. "Forget" removes it from every answer |

## Depends on, and feeds

- **Built after** the [learnings database](../learning-system/NORTH-STAR.md), on the same row
  shape and viewer.
- **Fed by** the [connections hub](../connections-hub/README.md).
- **Read by** the [decision support assistant](../decision-support/README.md), the weekly brief and
  the inbox summary.

## Open questions

- Where is the line between a record and a document? Proposed: over one screen of text, keep a
  pointer and a description.
- Calendar facts go stale fastest. Should they be read live from the calendar and never stored?
- How does a person see everything held about one subject, and remove it?

## Approved

Not yet.
