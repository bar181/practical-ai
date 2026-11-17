# Hand-back: learning-log

## Assumptions (I could not ask)

1. **The plan is the North Star page,** although it says "Not yet approved". It updates the older
   README, so where the two differ I followed the North Star (rows of error, redo or worked, not
   questions and answers).
2. **The tool is named `learning-log`,** because the plan says the existing `learning-log` skill
   "is rewritten, not replaced". I could not see that skill, so I could not check that nothing it
   does is lost.
3. **One job, two halves in one file:** log a learning, and find the rows that apply. The plan's
   one job names both. The weekly review is handled as one of the find questions, with suggested
   accept, merge or retire actions that the person carries out in their own file.
4. **Levels follow PROCESS.md, not the plan.** The plan's Level 2 (a skill writing to Google
   Sheets through a connector) is a connection, which PROCESS.md calls Level 3, so it is left out
   as the owner asked. Level 2 here is saving the file as a skill or project, which removes daily
   re-pasting for someone who uses a chatbot every day.
5. **The plan's "Base" was not built:** no viewer page (a script), no twelve-row sample file
   (an extra file). The worked example carries three invented rows instead.
6. **Labels are the person's own.** The plan says labels come from "a fixed list" but does not
   give one, so the skill reuses labels already in the log and marks any new one `new:`.
7. **Small design choices:** ids are `L-` plus a number; lists inside a cell are separated by `;`;
   a row whose `sensitive` cell is empty is treated as sensitive; "before I start" returns at most
   five rows, newest first (the plan's open question says start with five); no `review_by` column
   (left as the plan's open question).
8. **The skill-creator skill was not used.** It was listed as available, but the test rules let me
   read only files under the kit, so I filled in `template/SKILL.md` instead.

## What I built and where

`/tmp/ac3/out/learning-log/`, three files:

- `SKILL.md`: the tool. Log mode writes one 15-column row (CSV line plus a readable table) and
  checks a pasted log for a repeat, raising `seen` instead of adding a copy. Find mode answers the
  plan's seven exact questions as filters, plus keyword search and "before I start".
- `README.md`: what it does, quick start, where the log lives and how to paste a row, what to
  check, Level 2, why there is no Level 3, and the check table.
- `example.md`: one worked example with an invented two-person framing shop. **Written by me by
  following the file, not produced by a fresh chat**, and labelled as such.

## Reuse decision: nothing fits, so a full SKILL.md

Checked 16 November 2026:

| Source | What it does | Why it does not fit |
| --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's public skills | The page names no learnings or lessons skill. The full `skills/` folder listing could not be fetched, so this check is partial |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | 11 described plugins (productivity, sales, finance and others) | None keeps a log of lessons with review, accept or retire |
| [Claude memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context.md) | Remembers context; you can view, edit and delete it; each project has its own memory | No row shape, statuses or exact filters, and nothing a colleague or another chatbot can read. Matches the plan's own note |
| [self-improving-agent skill](https://playbooks.com/skills/openclaw/skills/self-improving-agent) (openclaw / pskoett fork) | Logs learnings, errors and requests to `.learnings/*.md` with ids, status and a recurrence count | Closest match, but needs file-system write access and an agent with hooks; it does not run in a plain chatbot, which Level 1 requires. Its recurrence count is the same idea as `seen` |

## Check results

None run. I could not start a fresh session: the Claude command-line tool on this machine returned
an authentication error twice, and I have no other way to start a separate agent. The README's
check table says "Not yet run" on every line.

To run them, in a fresh chat with only `SKILL.md`:

1. The message in `example.md`. Compare with the example.
2. A different input: the same invented log plus row L-4, then *"before I start the December price
   list"*. A correct answer offers no rows from L-4 (it is `proposed`), says what filter it used,
   and does not offer L-3.
3. *"log that"* with nothing else. It should reply once with the four-item list and wait.
4. Repeat 1 in a second chatbot.

## What a person should decide next

- Approve, or change, the North Star page; this tool rests on it.
- Run the four checks above and replace `example.md` with an unedited fresh-chat result.
- Who reviews the log and how often (the README suggests weekly).
- Whether `applies_to` should become a fixed list, like labels, so "before I start" matches
  reliably.
- Whether to compare this against the existing `learning-log` skill before it replaces it.

Nothing was merged, published or sent.
