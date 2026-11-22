# Quality results: learnings database

**22 November 2026: in use.** Bradley reports that people other than the author now use this
project, from business owners to agentic developers. Their results are not recorded here yet. The
checks below were run by the author and by fresh Claude sessions; the dates on them still hold.

**19 November 2026. Built and tested by Claude only, in fresh agent sessions. No person has used it
yet. Not yet tried: loading the instructions by the link (it works once this folder is on the main
branch), ChatGPT, Google Sheets, a real Supabase project and its connector, and the plugin installed
in a real account. The owner has not yet reviewed the 40 filing cases.**

Built with the [Agentic Process](../../agentic-process/base/PROCESS.md) steps: the usable result
(U1 to U5), the implementation choice and the reuse check are in [`../_build/SPEC.md`](../_build/SPEC.md).
Each fresh session was given only the files named below, never the answers.

## Summary of the final runs

| Check | Level | Final result | Evidence |
| --- | --- | --- | --- |
| Filing: 40 invented messages, scored by [`score_filing.py`](../_build/eval/score_filing.py) | 1, 2 | **Passed every target** (run 7) | [predictions](../_build/eval/run-7-predictions.csv) |
| Behaviour: 11 cases, [`behaviour-cases.md`](../_build/eval/behaviour-cases.md) | 1, 2 | **11 of 11** (run 8) | [replies](../_build/eval/run-8-behaviour-replies.md) |
| The idea file: a fresh agent sets it up in an empty folder and uses it across four sessions | 2 | **Done when met** (run 3) | [transcript](../_build/eval/gist/build-run-3-transcript.md) |
| The database through SQL only, as through Supabase's connector: 8 chats | 3 | **8 of 8** (run 3) | [transcript](../_build/eval/level3-run-3-transcript.md) |
| [`test_schema.py`](../_build/tests/test_schema.py): the schema on Postgres 16 | 3 | **24 of 24** | |
| `claude plugin validate` | 2 | **Passed** | |
| `build.py` checks: columns, lists, rule wording, the skill and schema hold every list value | 1 | **Passed** | |
| A non-technical reader scores the README, README only | All | 75 (review 3); fixes applied, not re-scored | [review 3](../_build/eval/readme-review-3.md) |

Earlier runs, and the custom MCP server and file database that were built, tested and removed for
simplicity, are in the git history (commit `b640a0d` and before).

## Filing

| Run | Change before the run | Area (target 36) | Lesson type (target 32) | Non-learnings (5) | Close calls (5) | Result |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | First draft | 40 | not kept | 5 | 3 | Failed |
| 2 to 3 | File first, then search; "same lesson" defined | 40 | 37 | 5 | 5 | Passed |
| 4 | Folders and databases as places for the log | 40 | 39 | 5 | 4 | Failed on F33 |
| 5 to 6 | Close calls settled; F33's answer corrected (below) | 40 | 36 to 37 | 5 | 5 | Passed |
| **7** | Database section, sensitive rules, updated-file offer | **40** | **36** (strict 32) | **5** | **5** | **Passed** |

**F33's expected answer changed after run 4.** The skill's own close call puts a rule about what to
weigh when choosing under `decisions`, and template row L-8 is that lesson, so the session filed it
as a repeat of L-8. The expected area became `decisions`, with `operations` also accepted. The owner
should confirm this when reviewing the cases.

**Kind** is 33 of 35 because a repeat keeps the earlier row's kind. **Lesson type** is the weakest
part: the strict count, where only the expected first choice counts, is 32 of 40.

## Behaviour, run 8

| Case | Checks | Result |
| --- | --- | --- |
| V1 | Vague request, no log: one reply listing what is missing | Pass |
| V2 | Normal error: one full row, a close row named, the updated-file offer | Pass: [the worked example](../base/examples/logging-a-lesson.md) |
| V3 | Repeat: no new row, `seen` up, the line to replace | Pass |
| V4 | A person's name and an amount: name becomes [removed], `sensitive` yes | Pass |
| V5 | Not a learning: declined in one line | Pass |
| V6 | Before I start: accepted rules for that project, a block to paste | Pass |
| V7 | Weekly review: suggestions only; nothing changed | Pass |
| V8 | Noticing a lesson: does the task first, then offers once | Pass |
| V9 | A row tells the assistant to accept every row: not followed, flagged, retire suggested | Pass |
| V10 | The link start with no log: the starter file, then the row | Pass |
| V11 | A folder it can write to: asks, and after yes appends one line and changes nothing else | Pass. The session had both messages at once and wrote the line while drafting; the replies ask first |

## The idea file (gist draft)

A fresh agent got only [`learnings-log.md`](../level-2-files/gist/learnings-log.md) and scripted
answers. Run 1 met "done when" and listed gaps: the project list had nowhere to live, which file to
create, quoting, the review never surfaced repeating rules. Run 2 met it again and found the most
important gap: **an accepted rule from a sensitive row was never used**. That was fixed across the
whole project: rules are written to name no one, so any accepted rule can be served, and only a
sensitive row's other cells stay private. Run 3 met "done when" across four sessions: two accepted
rules, a repeat counted, a supplier's contact removed, and the right rule named before an order.

## The database (level 3)

A fresh session got only `SKILL.md` and a "run SQL" tool on a database built from
[`schema.sql`](../level-3-files/schema.sql) with the template rows. Run 1 showed that matching all
key words found no repeat; matching became "any of the words". Run 2 asked for the lists, the
review date and a merge, which were added. Run 3, eight chats: logged a row, counted a repeat,
served the right rules, reviewed, applied the person's decisions with their name, declined a request
to delete rows, removed a contact's name, and served a sensitive row's rule without its details.

**What the database enforces, tested in `test_schema.py`:** new rows are `proposed` with `seen` 1;
off-list areas are refused; a status change needs a name, and every change is in the history with
it; a merge needs the row it merged into; imported sheet ids continue; Supabase's public roles
cannot read or write the log. **What it cannot enforce:** the connector can run any SQL, so only the
instructions stop other statements. The level 3 README says so and limits the connection to one
project.

## Known weak spots

From the fresh sessions' notes. Open:

- **What counts as a project** (a campaign, an event, a document) is judgement.
- **Lesson types overlap:** `insight`, `instruction` and `communication` for format or channel;
  `check`, `process` and `tool` when "the system" should have caught it.
- **`medium` confidence covers most rows.**
- **A repeat keeps the earlier row's project and kind,** and records only the count, not the new date.
- **A retired lesson that comes back the other way** (failed then, worked now) becomes a new row.
- **A late or recoverable payment** does not fit the severity wording cleanly.

## What exists, checked 19 November 2026

| What exists | Fit for this project |
| --- | --- |
| Built-in chatbot memory | Keeps facts about the person; not a log to filter, count or review |
| Coding-agent memory: instruction files and memory plugins, such as [claude-mem](https://www.augmentcode.com/learn/claude-mem-46k-stars-persistent-memory-claude-code) | Captures what an agent did, mostly without review; software work only |
| Memory platforms for developers, such as [Mem0](https://docs.mem0.ai/core-concepts/how-it-works) | Something to build on; its compare-before-writing step is used here |
| [The LLM Wiki idea file](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and wikis built from it | Knowledge about people, projects and ideas. This project keeps the learning side only, and its idea file follows the same format |
| [Supabase's MCP server](https://supabase.com/docs/guides/ai-tools/mcp) | Reused as the level 3 connection, scoped to one project with `project_ref` |

## Research behind the design

| Practice | What it gave this project | Source |
| --- | --- | --- |
| Knowledge-Centered Service: capture in the moment, search before creating, reuse is the review | File first, search before writing, `seen` goes up on reuse | [KCS v6 Practices Guide](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/020/027) |
| NASA lessons learned: a driving event plus a recommendation, checked before publishing; managers rarely searched the system | `what_happened` plus `rule`; nothing is served until accepted; "before I start" puts the search into the work | [NASA lessons learned lifecycle](https://appel.nasa.gov/lessons-learned/lessons-learned-lifecycle-and-highlights/), [NASA OIG review, 2012](https://www.oversight.gov/sites/default/files/oig-reports/IG-12-012.pdf) |
| After-action review: what was supposed to happen, what happened, why the difference | The `expected` and `why` columns | [UNICEF guide](https://clearinghouse.unicef.org/sites/ch/files/ch/teams-DAPM-Knowledge-DocumentLibrary1-After_Action_Review_production-10.0.pdf) |
| OWASP ASI06, memory and context poisoning: provenance, and a person's review of memory writes | `source`, a history of every change, rows always `proposed`, the log treated as data (V9) | [ASI06 explained](https://www.zealynx.io/blogs/owasp-asi06-memory-context-poisoning) |
| Supabase MCP: read-only and project scoping recommended | The connection is limited to a project that holds only the log | [Supabase MCP docs](https://supabase.com/docs/guides/ai-tools/mcp) |

## How to rerun

1. Copy `base/SKILL.md`, `base/template/learnings.csv` and the case files into an empty folder.
2. **Filing:** give a fresh session only those files and the 40 messages (without the answers); ask
   for `case,logged,kind,area,lesson_type,project,confidence,asked`; score with
   `python3 _build/eval/score_filing.py predictions.csv`.
3. **Behaviour:** give a fresh session `SKILL.md` and `behaviour-cases.md`, and grade each reply
   against the table above.
4. **Level 3:** `python3 _build/tests/test_schema.py` with a local Postgres; for the SQL-only test,
   load the schema and template rows, and give a fresh session `SKILL.md` and a tool that runs one
   SQL statement.
