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
