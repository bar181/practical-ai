# Worked example: Deal updates for a sales team

**Level:** Beginner, all nine steps. **Made on** 16 November 2026 by a new AI session that had only the
[build coach](../AI-INSTRUCTIONS.md) and the message below. It could not ask questions and did
not search the web, so it decided where the coach would ask, and marked prices and existing tools
"not checked". The coach took all nine steps, because five people write the notes and a shared spreadsheet is involved. Nothing below the line has been edited. Nobody has yet used what it made.
The person in the message is invented: a member of a five-person sales team who is not technical and uses Copilot.

**The message it was given**

> Read the build coach and follow it.
>
> My idea: five of us in a sales team share one spreadsheet of deals. After each call, whoever made it is supposed to update the row, and nobody does. I want an AI to read our call notes each Friday and suggest the updates for each row, for our team lead to approve. We all use Microsoft Copilot at work. I am not technical.

**Where it tripped** is in
[`friction.md`](../../level-3-files/test-runs/round-3/shared-tracker/friction.md). Read that too: it is the honest
half of the example. The coach was changed afterwards to fix what it found, and its plan headings have changed since.

---

## Friday deal-sheet helper: build coach session and hand-over

You told me the idea in a few sentences and said you are not technical, so this runs all nine
steps in plain words, and the first version is a prompt you paste. No code.

Why not the short path: the short path is for one person turning one input into one result in a
chat. This tool involves other people (five of you write the notes, your team lead approves) and
a shared file (the deal spreadsheet). The coach says to use all nine steps in that case.

I could not ask you questions, so I decided where I had to. Every decision is listed under
"Assumed" in the note at the end.

---

## The session, step by step

### Step 1 of 9: Scope

- **The user:** your team lead. They run it on Friday and approve the updates. You (the
  builder) may be one of the five reps; the first version is shaped for the lead.
- **The job:** each Friday, turn the week's call notes and the current deal rows into a list of
  suggested row updates the team lead can approve line by line.
- **What is out:** changing the spreadsheet automatically; reminding reps to write notes; running
  on a timer without someone starting it; adding new deals as rows; listing deals that had no
  call this week; forecasts or reports.
- **The wow (proposed):** every suggested change quotes the exact words from the call note it
  came from, so the lead can approve a week of updates without opening a single note.
- **The test:** the invented worked example below: three deal rows plus three call notes in, and
  the specific list of suggested updates shown under "What a good result looks like".

Decided: one user (team lead), one job (notes plus rows in, suggested updates out). Approval is
the check of that same result, so it stays in the job.
Gate: "Can you say the job in one sentence?" Assumed yes: the sentence is under "The job".

### Step 2 of 9: Reuse check

Not checked: I could not search the web. Look up:
- Which Microsoft Copilot your company gives you, and whether it can open your spreadsheet and
  notes files directly or only reads what you paste in.
- Whether Copilot inside Excel can already suggest updates to rows from text you give it.
- Whether your company already has a sales system (a CRM) with call logging that does this.
- Whether your company allows customer call notes to be pasted into Copilot.

Going on as if nothing was found. The assistant you already have counts only if one plain
sentence typed into it gives a result the lead would use unchanged. I cannot see that, so "try
one plain sentence first" is under Test this next.
Decided: build on the Copilot you already use.
Gate: "After what already exists, is there still something to build?" Open: not checked. Went on
as the step says.

### Step 3 of 9: Outside help

Not checked: I could not search, and I will not name products or prices I have not checked.
Kinds of paid help to look up: sales systems (CRMs) with built-in call logging; add-ons that
connect call notes to spreadsheets; a freelancer to set up an automatic flow later.
Decided: build a prompt; buy nothing for the first version.
Gate: "Do you know what you would build and what you would buy?" Assumed yes: build a prompt, buy
nothing now.

### Step 4 of 9: Cost

| Dependency | Price | Limit |
| --- | --- | --- |
| Microsoft Copilot (already provided at work) | Nothing new to buy. Your company's cost: not checked | How much text one message can hold: not checked |
| The shared deal spreadsheet (already exists) | Nothing new | None for this |
| The reps' call notes (already written, or meant to be) | Nothing new | Only as good as the notes |
| The team lead's time on Friday | Not money | Not checked; the test will show it |

Prices are not checked, so this gate passes only because the first version buys nothing new.
Decided: first version costs nothing new.
Gate: "Does the first version cost nothing, or an amount you accept?" Assumed yes, on that basis.

### Step 5 of 9: Simplest design

- **Assistant:** the Microsoft Copilot you already use at work, in an ordinary chat.
- **Where files live:** the deal spreadsheet stays where it is now. Add one small shared folder
  next to it (fixed layout below).
- **What stays manual:** gathering the week's notes; copying rows and notes into the chat;
  approving each line; typing approved changes into the spreadsheet. A person makes every change
  to the shared sheet.

Fixed folder layout:

```
Deal sheet helper/
  1 - Prompt (copy this into Copilot).txt
  2 - Worked example (invented data).txt
  3 - How to run it on Friday.txt
```

Decided: one chat, one prompt, three files, all changes to the sheet made by the lead.
Gate: "Could a beginner draw it?" Assumed yes: notes and rows go into a chat; a list comes out;
the lead ticks lines and types them into the sheet.

### Step 6 of 9: Plan and front door

**First thing the user sees:** the file "3 - How to run it on Friday", which says:

> Every Friday: 1. Open a new Copilot chat. 2. Paste everything from "1 - Prompt". 3. Under
> ROWS, paste the deal rows with their column headings. 4. Under NOTES, paste this week's call
> notes. 5. Read the list. Reply with the line numbers you approve, change or reject. 6. Type the
> approved changes into the spreadsheet yourself.

**The steps a user follows:** the six steps above.
**The worked example:** the invented example in "The first version" below, the same test as
step 1.

Decided: the front door is a six-line instruction; the worked example is kept beside the prompt,
not inside it.
Gate: "Is the beginner version fully described?" Assumed yes.

### Step 7 of 9: Review

Who will read the plan: nobody I can ask, so I reviewed it myself as a stranger. Three weak
points:
1. Where the call notes are kept is not known. If they are scattered (emails, notebooks,
   phones), step 4 of the Friday routine is the real work, not the AI.
2. The spreadsheet's columns and allowed values (for example the list of stages) are not known.
   The prompt tells Copilot to use only values already in the sheet, but this is untested.
3. The team lead has not said they want this. The whole design rests on them giving it time
   each Friday.

Gate: "Can someone else explain it back to you?" Passes on my own reading only. Nobody else has
read it.

### Step 8 of 9: Build and test

The first version is the prompt and worked example below. I cannot run the test here. The exact
test is under "Test this next" in the note.
Gate: "Did a fresh session finish the job, and have you read what it tripped on?" Open: not run.

### Step 9 of 9: Grow

Next three additions, smallest first, one at a time:
1. Add a short list of deals that had no call notes this week (a second result, so a second job).
2. Give reps a fixed four-line note format (deal, date, what happened, next step) so matching is
   easier.
3. If your Copilot can open files directly (not checked), point it at the spreadsheet and a
   shared notes file instead of pasting.

Gate: "Is the level below in use before you build the next?" Open: nothing is in use yet.

---

## Hand-over

## 1. The plan

**The job.** Each Friday, turn the week's call notes and the current deal rows into a list of
suggested row updates the team lead approves line by line.

**The user.** The team lead, who runs it on Friday and approves. The five reps write the notes.

**What is out.** Changing the spreadsheet automatically; reminding reps; running on a timer;
adding new deals as rows; listing deals with no calls; forecasts and reports.

**The wow.** Each suggested change quotes the exact words from the call note behind it, so the
lead approves without opening the notes. (Proposed, not tested.)

**What already exists.** Not checked. Look up: which Copilot you have and whether it can open
files; whether Copilot in Excel already does this; whether your company has a CRM with call
logging; whether pasting customer notes into Copilot is allowed.

**Cost.** Nothing new to buy: Copilot, the spreadsheet and the notes already exist. Copilot's
price to your company and its message-size limit: not checked.

**The design.** One Copilot chat, one pasted prompt. Rows and notes are pasted in; a numbered
list of suggestions comes out. The lead approves, and types approved changes into the sheet.
Folder: "Deal sheet helper" with three files (prompt, worked example, Friday instructions).

**The steps.** 1. New Copilot chat. 2. Paste the prompt. 3. Paste ROWS. 4. Paste NOTES. 5. Reply
with approved, changed or rejected line numbers. 6. Type approved changes into the sheet.

**The test.** Run the invented worked example in a fresh Copilot chat with only the prompt, and
compare with the good result below.

**Next three additions.** 1. List of deals with no notes this week. 2. A fixed note format for
reps. 3. Copilot reading the files directly, if your Copilot can (not checked).

Who has tried it: nobody. It is built, not used.

## 2. The first version

### File: 1 - Prompt (copy this into Copilot).txt

```
You help a sales team lead keep the team's shared deal spreadsheet up to date.

Below this prompt I will paste two things:
ROWS: the current rows of our deal spreadsheet, with the column headings.
NOTES: this week's call notes. Each note shows who made the call and the date, if known.

Your job: suggest updates to the rows, based only on the notes.

Rules:
1. Use only what the notes say. Never guess. If a note is unclear, say what is unclear in the
   Check column.
2. Suggest a change only when a note gives a new or different value for a column that already
   exists. Use the sheet's own column names.
3. For columns with a fixed set of values (such as a stage), only suggest a value already used in
   that column. If none fits, keep the current value and explain in Check.
4. Turn words like "Thursday" into a date, and say in Check how you read it.
5. For every suggestion, quote the exact words from the note that support it.
6. If a note does not match any row, list it under "Notes I could not match". Do not add a row.
7. If two notes disagree, show both and say so in Check.
8. You do not change the spreadsheet and you do not message anyone. The team lead decides.

Answer in exactly this form:

Suggested updates
| # | Deal | Column | Now | Suggest | From the note (exact words) | Check |
One line per change. Leave Check empty when the note is clear.

Notes I could not match
- who, date: one line on what the note says

End with this line:
"Reply with the line numbers you approve, change or reject. Nothing changes until you update the
sheet yourself."
```

### File: 2 - Worked example (invented data).txt

All names, companies, dates and columns below are invented for this example. They are not your
real data.

**What goes in**

ROWS (invented):

| Deal | Owner | Stage | Next step | Next step date | Last contact |
| --- | --- | --- | --- | --- | --- |
| Maple Street Dental | Rep A | First call | Book discovery call | 2026-11-06 | 2026-10-30 |
| Harbour Tools | Rep B | Proposal sent | Follow up on proposal | 2026-11-09 | 2026-11-02 |
| Bright Lane Cafe | Rep C | Negotiation | Send revised price | 2026-11-12 | 2026-11-05 |

NOTES (invented):

- Rep A, Tue 2026-11-10, Maple Street Dental: "Spoke to the office manager. They want the
  3-chair package. Sending quote by Thursday. Decision expected end of month."
- Rep B, Wed 2026-11-11, Harbour Tools: "Left voicemail, no answer. Try again Monday."
- Rep C, Thu 2026-11-12, Greenfield Florist: "New lead from the trade show, interested in a
  demo."

**What a good result looks like**

Suggested updates

| # | Deal | Column | Now | Suggest | From the note (exact words) | Check |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Maple Street Dental | Next step | Book discovery call | Send quote for 3-chair package | "They want the 3-chair package. Sending quote by Thursday." | |
| 2 | Maple Street Dental | Next step date | 2026-11-06 | 2026-11-12 | "Sending quote by Thursday." | Read "Thursday" as Thu 2026-11-12, the Thursday after the call. |
| 3 | Maple Street Dental | Last contact | 2026-10-30 | 2026-11-10 | "Spoke to the office manager." | |
| 4 | Maple Street Dental | Stage | First call | First call (no change) | "Sending quote by Thursday." | The quote is not sent yet. Change to "Proposal sent" once it is. |
| 5 | Harbour Tools | Next step | Follow up on proposal | Call again | "Try again Monday." | |
| 6 | Harbour Tools | Next step date | 2026-11-09 | 2026-11-16 | "Try again Monday." | Read "Monday" as Mon 2026-11-16. |
| 7 | Harbour Tools | Last contact | 2026-11-02 | 2026-11-11 | "Left voicemail, no answer." | No one answered. Decide if a voicemail counts as contact. |

Notes I could not match
- Rep C, 2026-11-12: Greenfield Florist, a new lead from the trade show, interested in a demo.
  Not in the sheet.

"Reply with the line numbers you approve, change or reject. Nothing changes until you update the
sheet yourself."

What makes this result good: every line has a quote; nothing is guessed (the stage is not
moved early, the voicemail is flagged); Bright Lane Cafe gets no lines because it had no note;
the new lead is listed, not added as a row; Copilot does not claim to have changed the sheet.

### File: 3 - How to run it on Friday.txt

```
Every Friday:
1. Open a new Copilot chat.
2. Paste everything from "1 - Prompt".
3. Under it, type ROWS: and paste the deal rows with their column headings.
4. Type NOTES: and paste this week's call notes (who, date, what happened).
5. Read the list. Reply with the line numbers you approve, change or reject.
6. Type the approved changes into the spreadsheet yourself.
```

## 3. The note

### Decided
- All nine steps, not the short path: the tool involves five note-writers, a team lead and a
  shared spreadsheet.
- One user (the team lead) and one job: notes plus rows in, suggested updates out, approved line
  by line.
- First version is a prompt pasted into the Copilot you already use. Nothing new is bought.
- A person (the lead) makes every change to the shared sheet.
- Folder "Deal sheet helper" with three files: prompt, worked example, Friday instructions.

### Assumed
- The user is the team lead, who runs it each Friday and approves. (You may be a rep and the
  builder.)
- The team lead is willing to do this each Friday. Not confirmed by anyone.
- Notes and rows are pasted into the chat, because I do not know whether your Copilot can open
  files directly.
- Proposed wow: each suggestion quotes the note it came from.
- Out of scope for the first version: automatic sheet changes, reminders, timers, new rows,
  deals with no calls, reports.
- Tone and format: a numbered table plus a short "could not match" list.
- Editing the shared sheet counts as something a person must approve.
- Gate 1 (one sentence): yes. Gate 3 (build or buy): yes, build a prompt, buy nothing.
  Gate 4 (cost): yes, because nothing new is bought. Gate 5 (beginner can draw it): yes.
  Gate 6 (fully described): yes.
- Gate 2 (still something to build): open, not checked; went on as the step says.
- Gate 7 (someone can explain it back): passes on my own reading only.
- Gate 8 (fresh session finished the job): open, not run.
- Gate 9 (level below in use): open, nothing is in use yet.
- The spreadsheet columns in the worked example are invented; your real columns are not known.

### Not checked
- Which Microsoft Copilot you have, what it costs your company, and whether it can open your
  files or only read pasted text.
- How much text one Copilot message can hold (matters if a week of notes is long).
- Whether Copilot in Excel, or a sales system your company already has, does this job already.
- Paid options and their prices (no web search was possible).
- Whether your company allows customer call notes to be pasted into Copilot.
- Where the call notes are kept today and what form they take.
- Your real spreadsheet columns and allowed values.

### Test this next
1. **Try one plain sentence first.** In a new Copilot chat, paste the invented ROWS and NOTES
   from the worked example and type only: "Suggest updates to these deal rows from these call
   notes." If the team lead would use that answer unchanged, you need no prompt: stop there.
2. **The fresh-chat test.** Open a new Copilot chat that has nothing in it. Paste only the
   prompt from "1 - Prompt", then the invented ROWS and NOTES from "2 - Worked example". Do not
   paste the good result. Compare Copilot's answer with "What a good result looks like" and check:
   - every line has an exact quote from a note;
   - the Maple Street Dental stage is not moved to "Proposal sent";
   - "Thursday" and "Monday" are turned into dates and the reading is explained;
   - the voicemail is flagged in Check;
   - Bright Lane Cafe gets no lines;
   - Greenfield Florist is under "Notes I could not match", not added as a row;
   - Copilot does not say it changed the spreadsheet.
   Write down every place it tripped. Then fix the prompt and run the test again.
3. **Ask the team lead.** Show them the worked example result and ask if they would approve from
   it on a Friday.
4. **One real week**, only after checking company policy on call notes in Copilot: run it on last
   week's real notes and count how long the lead takes to approve.

Who has tried it: nobody yet.
