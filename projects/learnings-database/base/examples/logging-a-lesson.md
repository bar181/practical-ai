# Worked example: logging one lesson

This is an unedited reply from a fresh chat that had only [`SKILL.md`](../SKILL.md) and the invented
log [`template/learnings.csv`](../template/learnings.csv). It is case V2 of the final behaviour run on
19 November 2026 (Claude, a fresh agent session). All names and data are invented.

**The person said:** "log that: the email to all our customers about holiday opening hours went out
with last year's dates. I expected this year's dates. It happened because we copied last year's
email and only changed the subject. It belongs to the newsletter."

**The reply, unedited:**

```
L-13,2026-11-19,error,marketing,newsletter,check,"When reusing last year's email, check and update every date in the body before it is sent.",The email to all our customers about holiday opening hours went out with last year's dates.,The email would show this year's dates.,"The email was copied from last year's, and only the subject was changed.",reused email; dates; holiday hours; check before sending,medium,proposed,1,chat,no,medium,
```

| Column | Value |
| --- | --- |
| id | L-13 |
| date | 2026-11-19 |
| kind | error |
| area | marketing |
| project | newsletter |
| lesson_type | check |
| rule | When reusing last year's email, check and update every date in the body before it is sent. |
| what_happened | The email to all our customers about holiday opening hours went out with last year's dates. |
| expected | The email would show this year's dates. |
| why | The email was copied from last year's, and only the subject was changed. |
| tags | reused email; dates; holiday hours; check before sending |
| severity | medium |
| status | proposed |
| seen | 1 |
| source | chat |
| sensitive | no |
| confidence | medium |
| review_by | |

- **Repeat check:** not the same lesson as any row. Close but different: L-3 ("When an AI summarises a document, ask it to mark any date it did not find in the text.") shares "date" and "check", but it is about AI summaries in `working-with-ai`. You can decide at the review whether they belong together.
- **Filing:** `error` in `marketing`, project `newsletter` (as in your log), lesson type `check` because the rule is to verify the email before it goes out. Confidence medium: the check-or-process close call settled the lesson type.
- **Date:** you gave no date, so I used today's, 2026-11-19. Change it if it happened on another day.
- **Empty cells:** `review_by` (the rule does not depend on a price, a tool version or a policy).

Your log is an attached file, so I cannot change it. To add the row, paste the line above:
- in Google Sheets, into column A of the first empty row, then **Data > Split text to columns**;
- in Excel, **Data > Text to Columns** with comma as the separator;
- in the CSV file, as a new last line.

Check before you rely on it:
- The id L-13 is the next number in the log you attached; check that no one has added rows since.
- The date, since I used today's.
- Severity `medium`: raise it if wrong dates to all customers would cost more than that.
- Whether L-3 should be merged with this row at the review.
