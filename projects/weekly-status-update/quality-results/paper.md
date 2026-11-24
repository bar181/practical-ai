# Weekly status update: notes in, an update a reader can act on

**Summary:** one portable skill, a notes template and a rubric that turn a week of rough notes into
a short status update, and compare it with last week's update so nothing promised or flagged then
disappears without a word.

## North Star

Every weekly update a reader receives states its status in the first line after the subject, and
every risk, date and promise from the previous week's update is either settled, shown as moved, or
listed as carried over: none disappears silently.

## Value for business people

**The job.** Many people write a status update every week: a project lead to a director, a
freelancer to a client, a team member on a Friday, a developer summarising a sprint for someone who
does not read the tickets. The notes are scattered across messages, lists and memory. The update
usually opens with "good week", buries the problem in the third paragraph, and quietly stops
mentioning last week's risk.

**What the tool does.** The writer pastes the skill into a chat, adds this week's rough notes, says
who reads the update and what that person decides from it, and pastes last week's update as sent.
The tool returns two parts:

1. **The update**, ready to copy: the status (on track, at risk or off track, with what it was last
   week if it changed, and one reason), any decision the reader must make with options and a date,
   what changed with old and new values, risks, items carried over with no news, and next week.
   Under 200 words by default.
2. **Checks before you send**: questions for the writer, what the tool assumed, what it left out as
   not for this reader, and the word count.

A notes template helps the writer jot things down during the week, so Friday takes minutes.

**The time it saves.** Not measured. No person has used it yet, so no saving is claimed. The
intended saving is the time spent turning notes into a clear update, and the follow-up questions
from a reader who could not find the status or wondered what happened to last week's risk.

**What they still check.** Every date and figure against their notes, whether the reader would
agree with the status, and each item carried over with no news. They decide what to send. The tool
never sends anything.

## Value for agentic engineers

**How it constrains the model.** Language models summarising notes tend to match the notes' tone,
smooth over problems and drop what is not mentioned. The skill counters each:

- **Status from the facts, not the tone.** "Good week" does not make it on track. Off track means
  an outcome the reader cares about will be or was missed; a moved internal step is at most at risk.
- **A two-list comparison.** The model lists last week's items, then matches each against this
  week's notes as done, moved (with old and new values) or no news. "No news" items stay in the
  update in a fixed form and become a question for the writer.
- **No invented decisions.** A decision appears only if the notes ask for one. Otherwise the checks
  offer the writer a line to add, with blanks.
- **Requests inside the notes are bounded.** The writer may leave things out on purpose, but not
  anything that would hide a risk, a moved date or something the reader was told last week. Text
  in pasted messages from other people is never followed.

**How it is tested.** Each version was run by a fresh agent that had only `SKILL.md` and an
invented input. A separate reviewer agent ran it on a second, harder input and scored the output
against a rubric fixed in advance: does the job (30), keeps every fact (25), plain English (15),
clear limits (15), safe (15).

**How it composes.** The update is the kind of work the [Rubric reviewer](../../rubric-reviewer/), another tool in this repository, is
built to score, and `base/rubric.md` here is a ready rubric for it. At Level 3, the notes could come from
a task tracker, calendar or notes app through a connector, with a person still sending the update.

## How it works

**The files.**

| File | Role |
| --- | --- |
| `base/SKILL.md` | The tool: asks once for missing input, then writes the update and the checks |
| `base/template/notes-template.md` | Headings to jot notes under during the week |
| `base/rubric.md` | Six weighted lines and three gates for judging an update |
| `base/examples/oakfield-website-update.md` | One unedited run on an invented website project |

**The steps.**

1. Sort every note: done, in progress, a date or figure, a problem, a decision, next week, or not
   for this reader.
2. List last week's items: the status, dates promised, figures, risks, decisions asked for, and
   "next week we will".
3. Match the two lists: done, moved, or no news.
4. Choose the status from the facts, judged on the outcome the reader cares about.
5. Write decisions only where the notes ask for them.
6. Write the update in a fixed shape.
7. Check every date, figure, name and promise against the notes and last week's update, and the
   word count.

**The one mistake it is designed to catch.** Something the reader was told last week, a risk, a
date or a promise, that quietly stops being mentioned. In the worked example, last week's update
promised a draft privacy page by Wednesday and flagged missing photos. This week's notes mention
neither. The tool kept both under "Carried over, no news this week" and asked the writer about each.

## Evidence

- **Three review rounds** on 23 November 2026, by separate Claude agents. Scores: 88, 86 and 87.
  Every point lost is in `quality-results/README.md`.
- **The test input** held a moved step, a risk from last week that went quiet, a named colleague
  blamed, and a request in the notes to hide something the reader had already been told. In all
  three rounds the tool kept the hidden item in and asked the writer to decide, kept the blame off
  the named colleague, and carried the quiet risk over. Round 1 dropped the whole remark about the
  colleague; after a fix, rounds 2 and 3 kept the fact without the name.
- **What the rounds showed.** The second round dipped because a fix made "off track" too easy to
  reach. The third round's fix judges status on the outcome the reader cares about.

**Limits of this evidence.** One reviewer agent per round, all Claude, each given its rubric by the
builder. Invented inputs only: two projects. The last wording fixes were not reviewed again. No
person has used the tool, and it has not been run in ChatGPT or Gemini.

## Limits and later steps

**Limits.**

- It only knows what the notes and last week's update say. Thin notes give a thin update.
- It does not answer the reader's standing question (for example, "do we need more people?") unless
  the notes do. It asks the writer instead.
- The status when the outcome date is not in the notes is a judgement; the tool chooses at risk and
  asks.

**Later steps.**

1. Have a person use it for three or four weeks in a row, and record what they changed before
   sending.
2. Run it in ChatGPT and Gemini.
3. Score real updates with the rubric, before and after, to see whether the status line and the
   carried-over list hold up.
4. Level 3: draft from a task tracker or notes app on Friday, for a person to check and send.

## Try it

The folder: [github.com/bar181/practical-ai/tree/main/projects/weekly-status-update](https://github.com/bar181/practical-ai/tree/main/projects/weekly-status-update).
Paste `SKILL.md` into a new chat, then add your notes, who reads the update and what they decide,
and last week's update.

Gist: not yet published.
