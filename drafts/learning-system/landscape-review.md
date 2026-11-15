# Learning system: landscape review

What already exists for keeping solved problems, checked on 2026-11-15 before building.

## Summary

- **The practice is old and settled.** Service desks keep a known error database and projects keep
  a lessons learned register. Both are a table of problems and what to do about them. Reuse their
  columns.
- **The simple level needs nothing new.** A spreadsheet and a chat Project.
- **The gap is the habit, not the tool.** Templates are everywhere. What is usually missing is the
  rule that the assistant looks first, and an honest count of whether an answer held.

## Established practice

| Practice | What to borrow | Source |
| --- | --- | --- |
| Known error database | The fields: an ID, a short searchable title, symptoms, cause, workaround, status, dates created and last reviewed, and search keywords including exact error text | [Trupeer's template](https://www.trupeer.ai/doc-template/kedb-template) |
| Approval before an entry counts | A record starts as a draft and a named owner approves it | [SimpleOne documentation](https://docs.simpleone.io/itsm/problem-management/known-error-database/create-known-error-records) |
| Regular review | A recurring task to review and update the entries | [ClickUp's template notes](https://clickup.com/templates/itsm-known-errors-t-31v3a2w) |
| Lessons learned register | Record what worked as well as what failed, and use the register at the start of the next piece of work | [Lessons learned register guide](https://lofficina.eu/download/pages/lessons_learned_register_template.html) |

A caution from practice: one team reported confusion because "known error" meant three different
things in their system. Keep one log, one meaning for each status.
[Source](https://www.servicenow.com/community/knowledge-managers/do-we-need-a-separate-known-error-knowledge-base/td-p/354083/page/2)

## What assistants already do

Not rechecked for this review. From general knowledge:

- Chat assistants offer Projects that hold instructions and files, and some keep memory across
  conversations. Memory is automatic and hard to inspect. A log is deliberate and can be read,
  corrected and shared. They complement each other.
- Some assistants can read and edit a connected spreadsheet. Where they cannot, an attached file
  replaced weekly does the job.

## Build or license

| Level | Lean | Why |
| --- | --- | --- |
| Simple | Build nothing. A spreadsheet and Project instructions | The columns are known. The instructions are short |
| Working | Still a spreadsheet, with a weekly review | Ranking and retiring are sorting and a status change |
| Automated | A hosted database with search by meaning, such as Supabase with its vector extension | Matching words stops working once there are a few hundred entries. Not rechecked: confirm current features and prices before choosing |

## Still to do

- Check, end to end, how each assistant connects to a spreadsheet.
- Review a hosted database for the automated level, with prices.
- Find out at what number of entries keyword search stops being enough. This draft guesses a few hundred.
