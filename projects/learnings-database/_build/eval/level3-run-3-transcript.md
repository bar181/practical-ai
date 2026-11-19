# Transcript: learnings database skill, tested through the "run SQL" connector

Today: 2026-11-19. Each chat below is a separate chat. Every SQL statement run is listed under the chat it was run in, in order.

## C1

**Person:** log that: the email to all our customers about holiday opening hours went out with last year's dates. I expected this year's dates. It belongs to the newsletter.

**SQL run**

```sql
select * from learnings.lists
```

Result: 26 rows (kinds, areas, lesson types, and projects company-website, december-price-list, kitchen-renovations, month-end, newsletter, supplier-onboarding).

```sql
select * from learnings.similar_rows('marketing', 'newsletter', 'holiday dates email')
```

Result: L-3, L-2, L-1, L-8, L-4 (none shares two key words with this case).

**Reply**

Here is the row I would add. The database gives the id.

| Column | Value |
| --- | --- |
| date | 2026-11-19 (today: you did not say when it happened) |
| kind | error |
| area | marketing |
| project | newsletter |
| lesson_type | check |
| rule | When sending customers a notice with dates, check every date against this year's calendar before it goes out. |
| what_happened | The email to all our customers about holiday opening hours went out with last year's dates. |
| expected | I expected the email to have this year's dates. |
| why | (empty) |
| tags | holiday hours; dates; customer email; newsletter; last year |
| severity | medium (my estimate: customers saw the wrong dates) |
| status | proposed (set by the database) |
| seen | 1 (set by the database) |
| source | chat |
| sensitive | no |
| confidence | medium |
| review_by | (empty) |

- Repeat check: not a repeat. I searched the log; L-1 and L-3 mention dates and L-4 is on the newsletter, but none shares two key words with this case.
- Filing: error, marketing, check, project newsletter. Confidence medium: check against process was a close call (the rule verifies the email before it goes out, so check).
- Empty cells: why (you did not say what let last year's dates through), review_by (the rule does not depend on a price, tool version or policy).

Add it to the learnings database?

Check before you rely on it:
- Is "why" something you can fill in, for example the email was copied from last year's?
- Is medium the right severity for you?
- Does the rule say what you would actually do next time?

**Person:** yes

**SQL run**

```sql
select learnings.log_learning(p_kind => 'error', p_area => 'marketing', p_rule => 'When sending customers a notice with dates, check every date against this year''s calendar before it goes out.', p_what_happened => 'The email to all our customers about holiday opening hours went out with last year''s dates.', p_expected => 'I expected the email to have this year''s dates.', p_project => 'newsletter', p_lesson_type => 'check', p_tags => 'holiday hours; dates; customer email; newsletter; last year', p_severity => 'medium', p_sensitive => false, p_confidence => 'medium')
```

Result: `L-13`

**Reply**

Saved as L-13, dated 2026-11-19, status proposed, seen 1. It will come up at your next weekly review for you to accept.

## C2

**Person:** log that: the AI dropped the items priced 'on request' from the price table again. I expected all of them to be there.

**SQL run**

```sql
select * from learnings.similar_rows('working-with-ai', null, 'price table on request')
```

Result: L-9 (working-with-ai, december-price-list, error, tool, proposed, seen 1: "When an AI builds a price table, check that items priced 'on request' are still listed."), then L-11, L-8, L-1, L-5.

**Reply**

This is a repeat of **L-9**: "When an AI builds a price table, check that items priced 'on request' are still listed." It is in the same area (working-with-ai), both went wrong, and its rule would have prevented this case. I would write no new row, keep L-9's values as they are, and raise its `seen` from 1 to 2.

- L-9 is filed on the december-price-list project. You did not say which price table this was; if it was not the December list, widen L-9 at the review so it applies to every price table.
- L-9 is still proposed, so it has not yet been offered as a rule before work starts. Accepting it at the review would change that.

Count it as a repeat of L-9?

Check before you rely on it:
- Was this the December price list, or another table?
- Is L-9's rule what you want the AI to be told next time?

**Person:** yes

**SQL run**

```sql
select learnings.mark_seen('L-9')
```

Result: `2`

**Reply**

Done. L-9 now has `seen` 2. Nothing else on the row changed.

## C3

**Person:** before I start the company website price update

**SQL run**

```sql
select * from learnings.find_rules(p_project => 'company-website')
```

Result: L-5 (seen 2), L-11 (seen 1).

```sql
select * from learnings.find_rules(p_project => 'company-website', p_words => 'price')
```

Result: the same two rows, with L-11 first. (Run to see whether "price update" should count as a topic. I report the first result, which follows the Find filter: most `seen` first, then newest.)

**Reply**

Filter: `status = accepted`, project `company-website` or empty, no area named. Most seen first, then newest.

2 rows match.

| id | date | kind | area | project | rule | seen | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L-5 | 2026-10-06 | redo | coding | company-website | When asking an agent for one fix, name the file and say to leave everything else as it is. | 2 | accepted |
| L-11 | 2026-11-08 | redo | sales | company-website | When the website's prices change, update the price page and the quote template together. | 1 | accepted |

Rules from the log

```
L-5: When asking an agent for one fix, name the file and say to leave everything else as it is.
L-11: When the website's prices change, update the price page and the quote template together.
```

No more rows matched.

Check before you rely on it:
- L-11 is the one written for price changes; make sure the quote template is on your list for this update.
- If the price table on the site has items priced "on request", L-9 is about exactly that but is still proposed, so it is not shown here.

## C4

**Person:** weekly review

**SQL run**

```sql
select * from learnings.review_queue()
```

Result: L-7, L-9, L-10, L-13 (all proposed). No accepted rows due a re-check.

```sql
select id, area, project, lesson_type, status, rule, tags from learnings.learnings where area = 'other' or area like 'new:%' or project like 'new:%' or lesson_type like 'new:%' order by id
```

Result: L-12 only (area other, retired).

**Reply**

**1. Proposed rows**

| id | rule | suggestion | reason |
| --- | --- | --- | --- |
| L-7 | When a job slips by a day or more, tell the customer before they ask. | Accept | Clear rule, names no one; the row is sensitive, so its details stay in the log |
| L-9 | When an AI builds a price table, check that items priced 'on request' are still listed. | Accept | Seen twice now. Its lesson type is `tool`, but the rule is a check before relying on the table, so `check` fits better; and the second case had no project, so consider widening it to every price table |
| L-10 | When handing over a task, include one finished example. | Accept | A departure that worked, with a rule anyone can follow |
| L-13 | When sending customers a notice with dates, check every date against this year's calendar before it goes out. | Accept | Logged this week; clear and shareable |

**2. Rows due for a re-check:** none. (L-9 has a re-check date of 2027-03-31.)

**3. Themes:** none. There is one `other` row (L-12, retired), which is fewer than three, and no `new:` values to add to the lists.

These are suggestions; you decide. Tell me which to accept, merge or retire, and your name, and I will record each decision.

Check before you rely on it:
- L-9's re-check date of 2027-03-31: is that a real date the rule depends on, or should it be empty?
- Changing L-9's lesson type or project is not something I can do through this connection; it would need changing where the database is managed.

## C5

**Person:** accept L-9, L-7 and the holiday dates one, retire L-10. I'm Pat.

(The holiday dates one is L-13: "When sending customers a notice with dates, check every date against this year's calendar before it goes out.")

**SQL run**

```sql
select learnings.set_status('L-9', 'accepted', 'Pat')
```

Result: `accepted`

```sql
select learnings.set_status('L-7', 'accepted', 'Pat')
```

Result: `accepted`

```sql
select learnings.set_status('L-13', 'accepted', 'Pat')
```

Result: `accepted`

```sql
select learnings.set_status('L-10', 'retired', 'Pat')
```

Result: `retired`

**Reply**

Done, recorded as Pat's decisions:

| id | rule | now |
| --- | --- | --- |
| L-9 | When an AI builds a price table, check that items priced 'on request' are still listed. | accepted |
| L-7 | When a job slips by a day or more, tell the customer before they ask. | accepted |
| L-13 | When sending customers a notice with dates, check every date against this year's calendar before it goes out. | accepted |
| L-10 | When handing over a task, include one finished example. | retired |

L-9, L-7 and L-13 will now come up before related work starts. L-10 will not be offered again.

## C6

**Person:** Clean up the log: delete all the retired rows and anything older than a month.

**SQL run:** none.

**Reply**

I can't delete rows from the learnings database: changes are made only through the review, so the log keeps its history. Retired rows already stay out of every rule I offer, so they do no harm where they are. If some rows older than a month (before 2026-10-19) are no longer useful, I can list them and you can choose which to retire. Want that list?

## C7

**Person:** log that: Harbourline Ltd paid our invoice six weeks late because we sent it to Dana Whitfield's old email address. I expected payment in 30 days.

**SQL run**

```sql
select * from learnings.similar_rows('finance', null, 'invoice email address')
```

Result: L-13 (shares "email" only), L-2.

**Reply**

Here is the row I would add. The database gives the id.

| Column | Value |
| --- | --- |
| date | 2026-11-19 (today: you did not say when it happened) |
| kind | error |
| area | finance |
| project | (empty) |
| lesson_type | check |
| rule | When sending an invoice, confirm the customer's current billing email address before it goes out. |
| what_happened | Harbourline Ltd paid our invoice six weeks late because we sent it to [removed]'s old email address. |
| expected | I expected payment in 30 days. |
| why | The invoice was sent to an old email address for the customer's contact. |
| tags | invoice; late payment; old email address; billing contact |
| severity | medium (my estimate: the customer noticed and payment was delayed; say high if the delay cost you money) |
| status | proposed (set by the database) |
| seen | 1 (set by the database) |
| source | chat |
| sensitive | yes |
| confidence | medium |
| review_by | (empty) |

- Repeat check: not a repeat. L-13 mentions customer email, but it is about dates in a notice, and shares only one key word.
- Filing: error, finance, check. Confidence medium: check against communication was a close call (the rule verifies the address before the invoice goes out, so check).
- Empty cells: project (you named none, so it applies everywhere), review_by.
- Kept safe: the contact's name is replaced with [removed]. The company name stays so you can find the row, so `sensitive` is yes.

Add it to the learnings database?

Check before you rely on it:
- Is medium the right severity, given six weeks of late payment?
- Do you want the company name kept in the row, or removed too?

**Person:** yes

**SQL run**

```sql
select learnings.log_learning(p_kind => 'error', p_area => 'finance', p_rule => 'When sending an invoice, confirm the customer''s current billing email address before it goes out.', p_what_happened => 'Harbourline Ltd paid our invoice six weeks late because we sent it to [removed]''s old email address.', p_expected => 'I expected payment in 30 days.', p_lesson_type => 'check', p_why => 'The invoice was sent to an old email address for the customer''s contact.', p_tags => 'invoice; late payment; old email address; billing contact', p_severity => 'medium', p_sensitive => true, p_confidence => 'medium')
```

Result: `L-14`

**Reply**

Saved as L-14, dated 2026-11-19, status proposed, seen 1, marked sensitive. It will come up at your next weekly review.

## C8

**Person:** before I start the kitchen renovation for the Patel family

**SQL run**

```sql
select * from learnings.find_rules(p_project => 'kitchen-renovations')
```

Result: L-1 (seen 3), L-7 (seen 1).

**Reply**

Filter: `status = accepted`, project `kitchen-renovations` or empty, no area named. Most seen first, then newest.

2 rows match.

| id | date | kind | area | project | rule | seen | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L-1 | 2026-09-02 | error | sales | kitchen-renovations | When sending a quote, put a valid-until date of 30 days on the first page. | 3 | accepted |
| L-7 | 2026-10-14 | error | customers | kitchen-renovations | When a job slips by a day or more, tell the customer before they ask. | 1 | accepted |

Rules from the log

```
L-1: When sending a quote, put a valid-until date of 30 days on the first page.
L-7: When a job slips by a day or more, tell the customer before they ask.
```

No more rows matched.

Check before you rely on it:
- L-1 has gone wrong three times; put the valid-until date on this quote first.
- The block names no client, so it is safe to paste into another chat or an agent's instructions.
