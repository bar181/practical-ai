One accepted rule covers the price page: check the item count before and after (L-2). Two rows are waiting for review (L-3, L-4). Two high-severity rows are not retired (L-2, L-3).

### 1. Before I start: website price page

**Filter:** `status = accepted` and `applies_to` matches "website price page" or `topics` matches `website/prices`.

**Rows that match:** 1 (none beyond this one)

| id | date | kind | rule | applies_to | seen | status |
| --- | --- | --- | --- | --- | --- | --- |
| L-2 | 2026-10-14 | error | When updating the website price page, check the item count before and after. | website price page | 3 | accepted |

L-5 is also about the price page, but it is `retired`, so the filter leaves it out and it is not offered as a rule.

Nothing in the log is about December itself. I matched on the page, not the month.

**Rules from the log**
```
L-2: When updating the website price page, check the item count before and after.
```
Held back as sensitive: 0.

### 2. What is waiting for review

**Filter:** `status = proposed`

**Rows that match:** 2

| id | date | kind | rule | applies_to | seen | status |
| --- | --- | --- | --- | --- | --- | --- |
| L-3 | 2026-10-29 | redo | When quoting the Greenway Clinic job, use their contract rates, not list prices. | client quotes | 1 | proposed |
| L-4 | 2026-11-04 | redo | When building the monthly sales table, paste the raw export, not a summary. | monthly sales table | seen missing | proposed |

Suggested actions (these are only suggestions; you change the status in your own file):

- **L-3: accept, after filling `sensitive`.** That cell is empty (missing). The row names a client, so it should probably be `yes` *(my interpretation)*. Until it is filled, I keep this row out of any paste block.
- **L-4: accept, after filling `seen`.** That cell is empty, so it is listed as "seen missing", not counted. If this has happened once, it would be `1` *(assumption: check it)*.

Neither row repeats the lesson of another row, so I suggest no merges and no retirements.

### 3. Serious and still open

**Filter:** `severity = high` and `status` is not `retired`

**Rows that match:** 2

| id | date | kind | rule | applies_to | seen | status |
| --- | --- | --- | --- | --- | --- | --- |
| L-2 | 2026-10-14 | error | When updating the website price page, check the item count before and after. | website price page | 3 | accepted |
| L-3 | 2026-10-29 | redo | When quoting the Greenway Clinic job, use their contract rates, not list prices. | client quotes | 1 | proposed |

*Interpretation:* I read "still open" as the log's own test, which is "not retired". That counts L-2 even though it is accepted. If you meant only rows not yet reviewed, the answer is just L-3.

### Check before you use this

- L-3: fill in the empty `sensitive` cell before you share or paste the row anywhere.
- L-4: fill in the empty `seen` cell.
- The "Rules from the log" block holds only L-2. Make sure that is all you want in the next chat.
