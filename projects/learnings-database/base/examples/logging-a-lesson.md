# Worked example: logging one lesson

This is an unedited reply from a fresh chat that had only [`SKILL.md`](../SKILL.md) and the invented
log [`template/learnings.csv`](../template/learnings.csv). It is case V2 of the final behaviour run (run 8) on
19 November 2026 (Claude, a fresh agent session). All names and data are invented.

**The person said:** "log that: the email to all our customers about holiday opening hours went out
with last year's dates. I expected this year's dates. It happened because we copied last year's
email and only changed the subject. It belongs to the newsletter."

**The reply, unedited:**

```
L-13,2026-11-19,error,marketing,newsletter,check,"When reusing a past email, check every date in the body against this year's calendar before it is sent.",The email to all our customers about holiday opening hours went out with last year's dates. We copied last year's email and only changed the subject.,We expected the email to show this year's dates.,Last year's email was copied and only the subject was changed.,holiday hours; dates; copied email; customer email; newsletter,medium,proposed,1,chat,no,medium,
```

| Column | Value |
| --- | --- |
| id | L-13 |
| date | 2026-11-19 (today; you did not say when it went out) |
| kind | error |
| area | marketing |
| project | newsletter |
| lesson_type | check |
| rule | When reusing a past email, check every date in the body against this year's calendar before it is sent. |
| what_happened | The email to all our customers about holiday opening hours went out with last year's dates. We copied last year's email and only changed the subject. |
| expected | We expected the email to show this year's dates. |
| why | Last year's email was copied and only the subject was changed. |
| tags | holiday hours; dates; copied email; customer email; newsletter |
| severity | medium (my estimate: customers received it) |
| status | proposed |
| seen | 1 |
| source | chat |
| sensitive | no |
| confidence | medium |
| review_by | (empty) |

- **Repeat check:** not a repeat. I searched your log and no row shares two or more key words with this one. L-4 is also on the newsletter, but it is about the opening line, not dates.
- **Filing:** error, marketing, check, project `newsletter` (matched to your log). Confidence medium: I used the close calls to choose `check` over `process`, and `marketing` over `customers`.
- **Empty cells:** `review_by` (the rule does not depend on a price, a tool version or a policy).

To add it: in Google Sheets, paste into column A of the first empty row and use **Data > Split text to columns**; in Excel, **Data > Text to Columns** with comma as the separator; in a CSV file, on a new last line.

Or say yes and I will give you the updated file.

Check before you rely on it:
- The date is today's. Change it to the day the email went out if you know it.
- Severity is my estimate. Raise it if customers turned up on a closed day or complained.
- The id assumes L-12 is still your last row.
- Move it to `customers` if you file notices to existing customers there.
