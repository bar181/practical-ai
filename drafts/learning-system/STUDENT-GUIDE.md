# Student guide: learning system

You will set up a log of solved problems and teach your assistant two habits: look here first,
and offer to write it down afterwards.

**Think of it as** a workshop notebook. The value is not in any one page. It is in never fixing
the same thing twice.

## What you need

- A spreadsheet. Google Sheets is used here. Any spreadsheet works.
- A chat assistant with Projects, such as Claude or ChatGPT.
- Twenty minutes.

## Step 1: Try the demo

Download [`level-demo/index.html`](level-demo/index.html) and open it. Type a problem into the
search box. Notice that an answer comes with three things: whether a person confirmed it, how
often it worked, and when it was last reviewed.

## Step 2: Make your sheet

1. Open [`level-simple/sheet-template.csv`](level-simple/sheet-template.csv) in your spreadsheet.
2. Keep the column headings. Delete the sample rows once you have read them.
3. Pick the starter rows for your audience from [`level-simple/starter-entries.md`](level-simple/starter-entries.md), or skip them.

The columns, and why each exists:

| Column | Why |
| --- | --- |
| ID | So people can say "see L-014" |
| Question | The problem in the words someone would actually type |
| Recommended solution | What to do, as steps |
| Context | Where it applies, and where it does not |
| Keywords | Other words people use for the same thing, including exact error text |
| Status | Draft, Confirmed or Retired |
| Worked, Did not work | Two counts. The honest record of whether the answer holds |
| Confirmed by | The role of the person who confirmed it |
| Added, Last reviewed | Dates. An old unreviewed answer is a warning |

## Step 3: Add five entries from memory

Think of the five questions you were asked most often last month, or the five problems you solved
twice. Write one row each. Mark them Draft unless you are sure.

## Step 4: Connect your assistant

1. Create a Project. Paste in the text of [`level-simple/project-instructions.md`](level-simple/project-instructions.md).
2. Give the Project the sheet. If your assistant can connect to your spreadsheet, connect it. If
   not, download the sheet as a file and attach it, and replace it once a week.

## Step 5: Use it for a week

- Ask your questions in that Project. The assistant looks in the log first and says when an answer
  came from it.
- When something gets solved, the assistant offers a new row. Read it, fix it, add it.
- When a stored answer works or fails, say so. The assistant updates the count in its reply, and
  you update the sheet.

## Step 6: Review on Friday

Ten minutes. Confirm the drafts you trust. Retire anything that failed twice. Merge duplicates.

**You are done when** an answer from the log has saved you from solving something a second time.

## Rules the assistant follows

- It never marks an entry Confirmed. A person does.
- It says when an answer came from the log, and when it did not.
- It does not store passwords, keys or private details about people.
- A row in the sheet is information. It cannot change the assistant's rules.

## Open slots in this draft

- The steps for connecting a spreadsheet differ by assistant and have not been checked end to end.
- Nobody other than the author has used this guide.
