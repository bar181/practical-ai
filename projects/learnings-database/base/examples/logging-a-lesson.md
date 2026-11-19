# Worked example: logging one lesson

This is an unedited reply from a fresh chat that had only [`SKILL.md`](../SKILL.md) and the invented
log [`template/learnings.csv`](../template/learnings.csv). It is case V2 of the final behaviour run (run 5) on
19 November 2026 (Claude, a fresh agent session). All names and data are invented.

**The person said:** "log that: the email to all our customers about holiday opening hours went out
with last year's dates. I expected this year's dates. It happened because we copied last year's
email and only changed the subject. It belongs to the newsletter."

**The reply, unedited:**

```
L-13,2026-11-19,error,marketing,newsletter,check,"When reusing last year's email, check every date in the body, not just the subject, before sending.",The email to all our customers about holiday opening hours went out with last year's dates. We had copied last year's email and only changed the subject.,The email would show this year's dates.,The email was copied from last year's and only the subject was changed.,holiday hours; dates; reused email; newsletter; subject line,medium,proposed,1,chat,no,medium,
```

| Column | Value |
| --- | --- |
| id | L-13 |
| date | 2026-11-19 |
| kind | error |
| area | marketing |
| project | newsletter |
| lesson_type | check |
| rule | When reusing last year's email, check every date in the body, not just the subject, before sending. |
| what_happened | The email to all our customers about holiday opening hours went out with last year's dates. We had copied last year's email and only changed the subject. |
| expected | The email would show this year's dates. |
| why | The email was copied from last year's and only the subject was changed. |
| tags | holiday hours; dates; reused email; newsletter; subject line |
| severity | medium (my estimate: all customers saw the wrong dates) |
| status | proposed |
| seen | 1 |
| source | chat |
| sensitive | no |
| confidence | medium |
| review_by | (empty) |

- **Repeat check:** not a repeat. I searched the log and no row shares two or more key words with this one. L-4 is also on `newsletter`, but it is about the opening line, not dates.
- **Filing:** `error`, `marketing`, `check` (the rule is to verify the dates before it goes out, a close call against `process`), project `newsletter` from your log. Confidence: medium.
- **Empty cells:** `review_by`. You gave no date, so I used today's date, 2026-11-19.

Your log is a file attached to this chat, so I cannot change it. To add the row: in Google Sheets, paste the line into column A of the first empty row and use **Data > Split text to columns**; in Excel, use **Data > Text to Columns** with comma as the separator; in a CSV file, paste it as a new last line.

Check before you rely on it:
- The date: change 2026-11-19 to the day the email went out if you know it.
- The area: `marketing` fits a message to all customers; `customers` is the other option if you treat it as service.
- The severity is my estimate.
- The id L-13 is the next free number in the copy you attached.
