# Example: what does the supplier's change of terms ask of us?

**The result is not yet run.** This page will hold one unedited result from a new chat that had
only [`SKILL.md`](SKILL.md) and the message below. The build session that wrote this tool could
not start a separate chat, and a result written by the tool's author would not be a fair example,
so the slot below the line is empty. Until it is filled, use the answer key: it says what a good
result must contain, and was written from the notice, not from any chatbot's output.

Tallowmere Café, Kestrel Fold Wholesale Ltd and the notice are invented.

**The message** (sent after pasting `SKILL.md`):

> We are the customer, Tallowmere Café. Here is the notice from our supplier:
>
> [Notice A from [`practice-notices.md`](practice-notices.md#notice-a-change-of-terms), pasted in
> full, from "KESTREL FOLD WHOLESALE LTD" to the acceptance form]

## The answer key

A good result has every row below, with these exact words or a shorter continuous run of them.
Each quote here has been matched, character for character, against the notice.

| Must appear as | Item | Exact words | Where |
| --- | --- | --- | --- |
| What you must do | Order by 2:00 pm, two working days before delivery, from 1 December 2026 | "orders must be placed by 2:00 pm two working days before your delivery day" | Clause 1 |
| What you must do | Pay each invoice within 14 days (was 30) | "Invoices are now due 14 days from the invoice date, down from 30 days." | Clause 4 |
| What you must do | Sign and return the acceptance form by 20 November 2026 | "Please sign the acceptance form below and return it to accounts@kestrelfold.example by 20 November 2026." | Clause 5 |
| Dates | 1 December 2026: the new terms start | "The changes below take effect on 1 December 2026." | Opening paragraph |
| Dates | 20 November 2026: the form is due | As above | Clause 5 |
| Penalty, in the summary too | $35 per unpaid invoice, and orders may be held | "an administration fee of $35 per invoice will be added, and further orders may be held until the account is settled" | Clause 4, fourth sentence |
| Open questions, not facts | Is Tallowmere on the "standard plan"? If yes, deliveries move to Tuesday and Friday; if not, the notice does not say | "Accounts on our standard plan will move to Tuesday and Friday deliveries." | Clause 2 |
| Cost (fact) | $18 delivery charge under the $200 minimum | "Orders below the minimum carry a delivery charge of $18." | Clause 3 |
| Cost (fact) | 1.5% surcharge on card payments over $1,000 | "card payments over $1,000 carry a 1.5% surcharge" | Clause 4 |

**It fails if** it lists the standard-plan line as a fact ("your deliveries move to Tuesday and
Friday"), says what happens if the form is not returned (the notice does not say), says prices
are changing (the notice says they are not), or gives any quote you cannot find with Find.

Also fine under Open questions: what "may be held" means in practice, which days count as working
days, and what happens if the form is not returned.

## Practise the check: one row with a planted mistake

This row was **written wrong on purpose by the builder**. It is not output from any chatbot. Try
the check on it before you run the tool: search the notice for the exact words.

| # | What you must do | By when | Exact words | Where | ✓ or ✗ |
| --- | --- | --- | --- | --- | --- |
| O2 | Pay each invoice within 30 days | 30 days from the invoice date | "Invoices are now due 30 days from the invoice date" | Clause 4 | |

It gets a ✗: those words are not in the notice. Clause 4 says "due 14 days from the invoice date,
down from 30 days". A summary that reads the old figure would cost $35 an invoice from December.

---

**Result: not yet run.** To fill this in: start a new chat in any chatbot, paste all of
`SKILL.md`, then the message above with notice A. Paste the reply below this line without
editing it, and add the date and the chatbot's name to the first paragraph of this page.
