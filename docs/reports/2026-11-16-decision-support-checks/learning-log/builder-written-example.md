# Example: log a table that dropped three items

This shows what a good result should look like. **It was not made by a fresh chat.** No fresh
chat could be started when the tool was built, so the builder wrote this on 16 November 2026 by
following [`SKILL.md`](../../../../projects/agentic-process/base/examples/learning-log/SKILL.md) step by step on the message below. Treat it as a target, not as
proof the file works, and replace it with an unedited fresh-chat result once one is run.
Hartley & Moss, a two-person picture-framing shop, its log and its price list are invented.

**The message** (sent after pasting `SKILL.md`):

> log that: I asked you to turn our November price list into a table for the website. Three frames
> priced "POA" were left out, and I only noticed after the page was live. I expected every item to
> come through, with POA kept as text. Applies to the website price page.
>
> Our log so far:
> ```
> id,date,kind,rule,what_happened,expected,applies_to,labels,keywords,topics,severity,status,seen,source,sensitive
> L-1,2026-10-02,error,"When asking for a supplier email, give the order number and dates yourself; never let the assistant fill them in.","The assistant wrote a reorder email with a delivery date we never agreed. The supplier queried it.","An email using only the dates I gave.",supplier emails,wrong-fact,reorder;delivery date;email,suppliers/orders,medium,accepted,2,session,no
> L-2,2026-10-20,worked,"When writing product descriptions, give three past descriptions as examples first.","Pasting three old descriptions before asking gave text in our own voice on the first try.","Two or three rounds of rewording to sound like us.",website product pages,voice,description;tone;examples,website/products,low,accepted,1,session,no
> L-3,2026-11-04,redo,"When building the monthly sales table, paste the raw export, not a summary.","I pasted my own summary and the totals were off by one week, so the table was rebuilt from the export.","One pass from my summary.",monthly sales table,data-loss;rebuild,sales;export;totals,finance/sales,medium,proposed,1,session,no
> ```

---

```
L-4,2026-11-16,error,"When turning a list into a table, count the items before and after, and keep entries without a price, such as POA, as text.","The November price list was turned into a table for the website. Three frames priced POA were left out. This was noticed only after the page was live.","Every item on the list in the table, with POA kept as text.",website price page,data-loss,price list;table;POA;missing items,website/prices,medium,proposed,1,session,no
```

| Column | Value |
| --- | --- |
| id | L-4 |
| date | 2026-11-16 (assumed: the day it was logged; change it if it happened earlier) |
| kind | error |
| rule | When turning a list into a table, count the items before and after, and keep entries without a price, such as POA, as text. |
| what_happened | The November price list was turned into a table for the website. Three frames priced POA were left out. This was noticed only after the page was live. |
| expected | Every item on the list in the table, with POA kept as text. |
| applies_to | website price page (new value; the log has "website product pages", which is a different page) |
| labels | data-loss (already in your log) |
| keywords | price list; table; POA; missing items |
| topics | website/prices (new branch under `website`) |
| severity | medium (assumed: the page went live incomplete, but you did not say it cost a sale) |
| status | proposed |
| seen | 1 |
| source | session |
| sensitive | no (no client, person or prices named) |

**Repeat check:** no repeat found. L-3 is also about a table, but its lesson is to work from the
raw export, not to keep every item, so this is a new row.

**Check before you paste:**
- The date: is 16 November the day it happened?
- `applies_to`: keep "website price page" as a new value, or use "website product pages" if you
  treat them as one page.
- Severity: raise it to `high` if the missing items lost an order.
- The row is `proposed`. It is offered as a rule before new work only after you mark it `accepted`.
