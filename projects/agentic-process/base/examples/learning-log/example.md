# Example: log a table that dropped three items

This is what a good result looks like. Made on 16 November 2026 in Claude by a new chat that had
only [`SKILL.md`](SKILL.md) and the message below. Hartley & Moss, a two-person picture-framing
shop, its log and its price list are invented. Nothing below the line is edited.

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

Here is the new row, ready to paste under your header:

```
L-4,2026-11-16,error,"When asking for a price list as a table, tell the assistant to keep every item and keep non-number prices such as POA as text, then check the item count against the list before publishing.","The November price list was turned into a table for the website. Three frames priced POA were left out, and this was only noticed after the page was live.","Every item comes through, with POA kept as text.",website price page,data-loss,price list;POA;missing items;table;website,website/prices,medium,proposed,1,session,no
```

The same row, easier to read:

| Column | Value |
| --- | --- |
| id | L-4 |
| date | 2026-11-16 (assumed: today's date) |
| kind | error |
| rule | When asking for a price list as a table, tell the assistant to keep every item and keep non-number prices such as POA as text, then check the item count against the list before publishing. |
| what_happened | The November price list was turned into a table for the website. Three frames priced POA were left out, and this was only noticed after the page was live. |
| expected | Every item comes through, with POA kept as text. |
| applies_to | website price page |
| labels | data-loss |
| keywords | price list; POA; missing items; table; website |
| topics | website/prices |
| severity | medium (interpreted) |
| status | proposed |
| seen | 1 |
| source | session (interpreted) |
| sensitive | no |

No cells are empty.

**Duplicate check:** no repeat found. The closest row is L-2 (website product pages), but it is a different page and a different lesson, so this is a new row.

**Check before you use it:**
- **date:** I used today's date. If the page went live on an earlier day, change it to that day.
- **applies_to:** "website price page" is a new value. I kept it apart from "website product pages" (L-2) because they are different pages. Merge them if you treat them as one.
- **labels:** I reused your existing `data-loss` label, since items were dropped.
- **topics:** `website/prices` is new, chosen to sit next to `website/products`.
- **severity:** I set `medium`. Wrong or missing prices on a live page could cost sales or cause customer questions. Raise it to `high` if that happened.
- **source:** `session`, to match your other rows. Use `person` if you keep that for things you reported yourself.
- **rule:** the last part ("check the item count against the list before publishing") is my addition. You did not ask for it, but it is the step that would have caught this before the page went live. Cut it if you don't want it.
