# Hand-over note: Friday deal-sheet helper

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
