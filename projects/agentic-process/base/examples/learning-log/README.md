# Learning log

Tell your chatbot "log that" when something goes wrong, has to be redone, or works better than
expected, and it gives you one row to paste into your own log. Before similar work, paste the log
back and it gives you the rules that apply, so the same mistake is not made twice.

**Think of it as** a ship's log: one line each time the crew hits a rock or finds a faster
channel, read by the next crew before they sail.

**Status, 16 November 2026.** Built by the Agentic Process builder skill from the learning-system
plan, with no help, as the builder check (AC-3). Three fresh Claude chats ran it; all three
passed. No other chatbot has tried it, and nobody has used it on a real log. It is kept as an
example of the builder's work. The finished tool it led to, built on 19 November 2026, is the
[Learnings database](../../../../learnings-database/).

## Try it: paste one file (5 minutes)

1. Open [`SKILL.md`](SKILL.md), press **Raw**, and copy all of it.
2. In any chatbot, start a new chat and paste it. On a new line, add your input: *"log that: the
   assistant left three items out of the price table, and I expected all of them. Applies to the
   website price page."*
3. If anything is missing, it replies once with what to give it.

**Shortcut:** if your chatbot can open links, send *"Follow the instructions at [the Raw link to
SKILL.md]. [Your input]"* instead of pasting.

**Your log lives with you,** never in this folder: a private CSV file, Excel file or Google Sheet.
If you have none, the tool gives you the header line to start one. To add a row, paste the line it
gives you under the last row. In Google Sheets, paste into column A and use **Data > Split text to
columns**; in Excel, use **Data > Text to Columns** with comma as the separator; in a CSV file,
paste it on a new line.

## What to give it

- **To log:** what happened, what you expected instead, and what it applies to (a tool, a project,
  a stage or a kind of task). Paste your log too, so it can spot a repeat and reuse your labels.
- **To find:** your log, and a question such as "what is waiting for review?", "what has gone
  wrong more than twice?" or "before I start the December price list".

## What you get

- **Log:** one row in 15 fixed columns, as a line to paste and as a table to read, with a note on
  whether it repeats a row you already have. A repeat raises that row's `seen` count instead of
  adding a copy. Notes, how-tos and opinions are turned away: only errors, redos and things that
  worked unexpectedly are logged.
- **Find:** the filter it used, how many rows match, and the rows. Before new work, up to five
  accepted rules as a block to paste into your next chat.

[See the worked example](example.md).

## Check before you act

- The row's date, `applies_to` and severity: the tool marks what it assumed.
- The rule: would it have prevented this case, and can someone follow it without the story?
- New rows are `proposed`. Only you change a row to `accepted`, `merged` or `retired`, and only
  `accepted` rows are offered before new work. Once a week, ask "what is waiting for review?" and
  decide each one. A log nobody reviews becomes noise.
- Rows marked `sensitive = yes` are never put in a block meant for another chat. Check the flag
  before you share any part of your log.
- The measure that matters: `seen` should stop rising on the rows you have accepted.

## Save it (Level 2)

Worth doing if you use it every day: it saves pasting the file into each new chat.

- **Claude:** add `SKILL.md` as a skill (in a folder named `learning-log`), or paste it into a
  Project's instructions.
- **ChatGPT** Project or **Gemini** Gem: paste it into the instructions.
- In a Project, you can also add an export of your log as a project file so "find" works without
  pasting. It is a copy: add it again after you add rows.

There is no Level 3: the owner asked for none. Writing rows straight into a Google Sheet or a
database would remove the pasting, and is the next step to weigh once the log is in daily use.

## The check

Run on 16 November 2026, each in a fresh Claude chat with only `SKILL.md` and one message.
[The logs](../../../quality-results/2026-11-16-decision-support-checks/learning-log/).

| Check | Result |
| --- | --- |
| An input missing something ("log that" alone): asks for it in one reply, and waits | **Pass.** Asked for what happened, what was expected and what it applies to; wrote no row |
| The worked example's input: usable, follows the rules | **Pass.** A correct row, the duplicate check, and five things to check, including a step it added to the rule. Now the [worked example](example.md) |
| A different input (three questions on a log with a retired row, an empty `seen` and an empty `sensitive`): flags what it cannot settle | **Pass.** Filtered correctly, left out the retired row, held back the row with no `sensitive` value, reported `seen` as missing, and flagged its reading of "still open" |
| The same file in a second chatbot | Not yet run |
