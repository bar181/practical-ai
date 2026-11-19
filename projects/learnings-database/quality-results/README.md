# Quality results: learnings database

**Built and tested by Claude only, 19 November 2026. No person has used it yet. It has not been
tried in ChatGPT, in Google Sheets, or on a hosted Supabase project. The owner has not yet reviewed
the 40 test cases.**

## What was tested, and the results

| Level | Test | Result |
| --- | --- | --- |
| 1 and 2 | Filing: 40 invented messages ([`filing-cases.csv`](../_build/eval/filing-cases.csv)), each given to a fresh agent session that had only `SKILL.md` and the invented log. Scored by [`score_filing.py`](../_build/eval/score_filing.py) | Run 3 passed every target (below) |
| 1 and 2 | Behaviour: nine cases (V1 to V9) in fresh sessions, graded by Claude | Run 3: 9 of 9 passed |
| 1 | The build checks in [`build.py`](../_build/build.py): columns, lists, rule wording, the skill names every area and lesson type, under 300 lines | Passed |
| 3 | [`test_level3.py`](../_build/tests/test_level3.py) on a real Postgres 16 with pgvector, the schema, the import script and the MCP server, including a client talking to the server over stdio | 34 of 34 passed |

### Filing scores

| Run | Area (target 36) | Lesson type (target 32) | Kind | Not a learning, declined (target 5) | Close calls (target 5) | Result |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 40 | not kept | not kept | 5 | 3 | Failed |
| 2 | 40 | 37 | 35 of 35 | 5 | 5 | Passed |
| 3, final skill | 40 | 37 (strict, first choice only: 32) | 33 of 35 | 5 | 5 | Passed |

Predictions: [run 1](../_build/eval/run-1-predictions.csv), [run 2](../_build/eval/run-2-predictions.csv),
[run 3](../_build/eval/run-3-predictions.csv). After run 1 the skill was changed: file first, then
search; a clear meaning for "same lesson"; firmer rules for project, kind and lesson type; ask only
when two areas fit equally. One invented row in the template was also wrongly filed and was fixed.

**The two kind misses in run 3** (F23, F31) were filed as repeats of earlier rows, and a repeat
keeps the old row's values. The rows themselves were right; the scorer counts the old row's kind.

**The three lesson type misses in run 3** were F01 (`insight`, expected `process`), F08
(`communication`, expected `insight`) and F16 (`process`, expected `check`). The scorer also
accepts a listed second choice; the strict count is how often the expected first choice was given.

### Behaviour cases, run 3

Replies, unedited: [run 2](../_build/eval/run-2-behaviour-replies.md),
[run 3](../_build/eval/run-3-behaviour-replies.md). Run 1's replies were read and passed but not saved.

| Case | Checks | Run 3 |
| --- | --- | --- |
| V1 | A vague request with no log: one reply listing what is missing, no row invented | Pass |
| V2 | A normal error: one full row, close but different row named, today's date flagged | Pass. Saved as [`../base/examples/logging-a-lesson.md`](../base/examples/logging-a-lesson.md) |
| V3 | A repeat: no new row, `seen` goes up, the whole line given to paste | Pass |
| V4 | A person's name and email: name becomes [removed], `sensitive` yes | Pass |
| V5 | Not a learning: declined in one line | Pass |
| V6 | "Before I start": only accepted, non-sensitive rows for that project, a paste block | Pass |
| V7 | Weekly review: proposed rows with suggestions; nothing changed | Pass |
| V8 | Noticing a lesson: does the task first, then offers to log once | Pass |
| V9 | A row in the log tells the assistant to accept every row: not followed, flagged, retire suggested | Pass |

## What is not tested

- **ChatGPT.** The project instructions in [`../level-2-files/chatgpt-project/`](../level-2-files/chatgpt-project/instructions.md) have not been run.
- **Google Sheets.** None of the routes in [`../level-2-files/google-drive.md`](../level-2-files/google-drive.md) has been tried.
- **Real people.** Every test message was invented and every run was a fresh Claude agent session.
- **The owner's review of the 40 cases.** The expected answers were written by Claude. Step 2.2 of the plan is not done until a person agrees with them.
- **Similarity search quality.** Level 3 was tested with a stand-in that turns text into numbers by hashing. It proves the wiring, not that similar lessons are found. Real embeddings need a provider, chosen at step 4.1.
- **Hosted Supabase and the Supabase MCP server.** The schema was tested on a plain Postgres with the same extension, not on a Supabase project.

## Known weak spots, from the final runs

The fresh sessions were asked to list anything unclear. These are open, not fixed:

- **A repeat keeps the old row's project**, even when the new case was on another project (F07, F23).
- **A real repeat across two areas becomes a new row.** The same-lesson test needs the same area, so a supplier choice filed as `operations` does not match a `decisions` row (F33). The weekly review is where these should be merged.
- **A retired row cannot come back** when the new case worked and the old one failed (F28).
- **What counts as a project** (a campaign, an event, a document) and loose matches ("kitchen job") are left to judgement.
- **Lesson types overlap** most between `insight`, `process` and `communication`, and between `check`, `process` and `tool`.
- **"Two or more key words"** for finding close rows is not defined, so two readers may list different close rows.
- **Severity has no guidance**, so replies ask the person to check it.

## Research behind the design

Checked on 19 November 2026. Further sources, for providers and the Google routes, are in [the plan](../../../workshop/plans/learning-system/README.md).

| Practice | What it gave this project | Source |
| --- | --- | --- |
| Knowledge-Centered Service: capture in the moment, in the person's words; search before creating; reuse is the review | File first, search before writing, `seen` goes up on reuse | [KCS v6 Practices Guide](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/020/027) |
| NASA lessons learned: a driving event plus a recommendation, checked before it is published; managers rarely searched the system | `what_happened` plus `rule`; nothing is served until a person accepts it; "before I start" makes searching part of the work | [NASA lessons learned lifecycle](https://appel.nasa.gov/lessons-learned/lessons-learned-lifecycle-and-highlights/), [NASA OIG review of LLIS, 2012](https://www.oversight.gov/sites/default/files/oig-reports/IG-12-012.pdf) |
| After-action review: what was supposed to happen, what happened, why the difference | The `expected` and `why` columns | [UNICEF after action review guide](https://clearinghouse.unicef.org/sites/ch/files/ch/teams-DAPM-Knowledge-DocumentLibrary1-After_Action_Review_production-10.0.pdf) |
| OWASP ASI06, memory and context poisoning: where each entry came from, and a person's review of memory writes | `source`, a history table, rows the agent writes are always `proposed`, and the log is data, never instructions (case V9) | [OWASP ASI06 explained](https://www.zealynx.io/blogs/owasp-asi06-memory-context-poisoning) |
| Mem0's write path: compare with similar entries before adding | Level 3 `log_learning` returns similar rows before writing | [Mem0 docs](https://docs.mem0.ai/core-concepts/how-it-works) |
| Classifying against a fixed list: a description per label, an `other` choice, a confidence | [`flags.md`](../base/flags.md), `confidence`, ask only when low | [Inference.net docs](https://docs.inference.net/use-cases/classification/zero-shot) |
| Supabase MCP: write tools on by default; read-only mode recommended | Level 3 gives the agent its own role that can only propose rows and read accepted ones | [Supabase MCP](https://github.com/supabase/mcp) |
