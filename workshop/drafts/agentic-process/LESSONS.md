# What version 1 taught

Each line is a finding from a test or a review of version 1, and what it changes here. The logs
are in [`workshop/plans/archive/agentic-process/v1-project/level-3-files/test-runs/`](../../plans/archive/agentic-process/v1-project/level-3-files/test-runs/).
All tests were AI sessions in Claude. No person has used either version.

## From testing

| Finding | Evidence | What it changes |
| --- | --- | --- |
| The author cannot see their own gaps. A new session with only the instructions finds them at once | Coach rounds: blocking points per run fell 4.5, 3.5, 2.5 as each round's findings were fixed | Every build ends with a fresh-session test, under [`builder/TEST-RULES.md`](builder/TEST-RULES.md) |
| A fix that works for one input can break on the next | The decision tool held at 0 blocking on the bakery, then hit 5 on a truck decision: its rules were tuned to the bakery | Test on at least two different inputs before calling a tool done |
| A rule cannot remove judgement. Showing it works better | After three rounds of tighter rules, what remained were real judgement calls. Listing each, with the other reading and whether it changes the answer, brought blocking points to 1 | Instructions show their judgement calls to the person instead of hiding them |
| A beginner stalls on setup, not on the tool | A walkthrough by a session playing an office manager: 3 blocking points, all about saving the tool, test data and who runs the test | Every explainer says where to save the tool, step by step, and that tests use invented data |
| A chatbot cannot run its own test | The coach claimed it would test the tool; in a chat it cannot | The person runs the test and pastes the reply back, or the test is listed as not run |
| Missing data reads as good news unless told otherwise | Anthropic's small-business plugin rule "absent is not zero" | Instructions report missing data as missing, never as zero |

## From the build itself

| Finding | What it changes |
| --- | --- |
| Generated pages multiplied: one source wrote 12 files, and three were parked the same day | Write plain Markdown. Generate nothing until two files would otherwise drift |
| Teaching material grew faster than the tool | The tool is the product. The explainer is short and can live in the README |
| Tests and their logs sat inside the project and doubled its size | Logs live apart from the tool, at Level 3 |
| The reuse check found Anthropic's `build-agent` only at the end | Reuse first: use an existing capability, wrap it, or build only the missing piece |

## Worth borrowing, from Anthropic's `build-agent` skill

1. If the person has just done the task in a chat, that conversation is the spec. Their corrections are the business rules.
2. Sort every part of the task into fixed, varies and judgement. Judgement points become approval gates.
3. Test on a past case whose right answer is known, and show the two side by side.
4. Gate only what sends, spends, publishes or deletes, and where the person hesitated.
