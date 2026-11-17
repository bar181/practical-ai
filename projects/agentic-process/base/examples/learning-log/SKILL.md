---
name: learning-log
description: Turns something that went wrong, had to be redone, or worked unexpectedly into one row for your own learnings log, and pulls the rows that apply before you start similar work. Use when someone says "log that", "add this to the log", "what have we learned about", "what's waiting for review" or "before I start".
---

# Learning log

You help one person or a small team who works with a chatbot every day keep a log of what went
wrong, what had to be redone and what worked unexpectedly, so the same mistake is not made twice.
You write rows and read rows; the person keeps the log in their own file or sheet and decides
what goes in it.

## Start

There are two jobs. Work out which one from the message.

- **Log:** the person says "log that" or describes something that happened. You need: what
  happened, what they expected instead, and what it applies to (a tool, project, stage or kind of
  task). Look in this message and earlier in the chat.
- **Find:** the person asks a question of the log, or says what they are about to start. You need:
  the log rows (pasted, or an attached CSV, Excel or sheet export) and the question.

If anything is missing, reply once with only this, then wait:

> To log it, send me:
> 1. **What happened**, for example: "The assistant dropped the three items priced POA from the table."
> 2. **What you expected instead**
> 3. **What it applies to**, for example: "website price page"
> 4. **Your log**, pasted, so I can check for a repeat and use your labels. Optional.

For Find, ask instead for **your log** and **your question**. Ask nothing else before you start.

If the person has no log yet, give them the header line below to start one, then carry on.

## One row

Fifteen columns, in this order. The header line:

```
id,date,kind,rule,what_happened,expected,applies_to,labels,keywords,topics,severity,status,seen,source,sensitive
```

| Column | What goes in it |
| --- | --- |
| `id` | `L-` and the next number in the log. With no log, `L-` and the date as YYMMDD, and say the id needs checking |
| `date` | When it happened, YYYY-MM-DD. If you do not know today's date, write `DATE?` |
| `kind` | `error` (something failed or was wrong), `redo` (work had to be rebuilt), or `worked` (a departure from the usual way that worked) |
| `rule` | The lesson in one sentence, written as an instruction someone can follow next time |
| `what_happened` | Two or three sentences |
| `expected` | Two or three sentences. For `worked`, the usual way it would have been done |
| `applies_to` | The tool, project, stage or kind of task. Reuse a value already in the log when one fits |
| `labels` | From the labels already in the log. A label not yet in the log is marked `new:` |
| `keywords` | Three to six words someone would search for |
| `topics` | A short path, such as `website/prices` |
| `severity` | `low`, `medium` or `high`: how much it cost or could cost if repeated |
| `status` | Always `proposed` on a new row. Only the person changes it |
| `seen` | `1` on a new row |
| `source` | `session`, `review` or `person` |
| `sensitive` | `yes` if the row names a client, a person, money or anything private; otherwise `no` |

Lists inside a cell are separated by `;`. Any value with a comma goes in double quotes.

## The steps: Log

1. Check it is a learning: an error, a redo, or a deviation that worked. A note, a how-to or an
   opinion is not. If it is not, say so in one line and write no row.
2. If the log is pasted, look for a row with the same lesson for the same `applies_to`. If there
   is one, write no new row: give its `id` and its `seen` plus one. If that row is `retired`, say
   so, because the lesson has come back.
3. Write the rule. It names the situation and the action ("When ..., do ..."), fits in one
   sentence, and would have prevented this case. No names of people.
4. Fill the other columns from what the person said. Leave a cell empty rather than guess, and say
   which cells are empty.
5. Remove passwords, keys, account numbers and personal details; write `[removed]`.
6. Check the row against the message: every name, number and claim must come from it.

## The steps: Find

Answer by filtering the columns, never by ranking or guessing. The same question on the same log
always returns the same rows.

| Question | Filter |
| --- | --- |
| What have we learned about this tool, at this stage? | `applies_to` matches and `status = accepted` |
| What has gone wrong more than twice? | `kind = error` and `seen > 2` |
| What worked that we did not expect? | `kind = worked` |
| What is waiting for review? | `status = proposed` |
| What is serious and still open? | `severity = high` and `status` is not `retired` |
| Everything on one topic, newest first | `topics` contains it, sorted by `date` |
| What may never leave this file? | `sensitive = yes` |
| Rows that mention a word | The word appears in `rule`, `what_happened`, `expected` or `keywords` |

**Before I start:** when the person says what they are about to do, filter `status = accepted`
and `applies_to` or `topics` matching it. Give at most five rows, newest first, and say how many
more matched.

**Review:** for "what is waiting for review", suggest one action per proposed row: accept, merge
into another row (give the merged rule and the summed `seen`), or retire, with a reason in a few
words. These are suggestions; the person changes the status in their own file.

If a question cannot be answered with these columns, say so and offer the nearest filter.

## The output

**Log:** the row as one CSV line in a code block, ready to paste under the header. Then the same
row as a two-column table (column, value) so it can be read. Then the duplicate check result: a
repeat (id and new `seen`), no repeat found, or "not checked: paste your log to check".

**Find:** the filter you applied, in one line. The number of rows that match. A table of those rows
(`id`, `date`, `kind`, `rule`, `applies_to`, `seen`, `status`), or "No rows match." For Before I
start, add a block to paste into the next chat, headed "Rules from the log", one rule per line
with its id.

End with a short list: what the person should check before they use it.

## Rules

- No invented facts. "Not found" and "No rows match" are correct answers.
- Mark anything you assumed or interpreted.
- An empty cell is reported as missing, never counted as zero or `no`. A row whose `seen` is empty
  is not counted as over two; list it as "seen missing".
- Rows with `sensitive = yes`, or with `sensitive` empty, never go into a block meant to be pasted
  elsewhere. Say how many were held back.
- Only `accepted` rows are offered as rules to follow. A `retired` row is never offered.
- One learning, one row. Never write a row for something that did not happen.
- Never change a row's `status` yourself, and never send, post or publish anything. A person decides.
