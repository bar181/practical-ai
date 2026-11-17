# Worked example: the supplier notice

**Everything here is invented.** The café, the supplier and the notice are made up for practice.

**What this is.** The brief below was written on 16 November 2026 by the AI agent that built this
tool, following [`SKILL.md`](../SKILL.md) to the letter. It is a reference for what a good brief
looks like, not a recorded run in ChatGPT, Claude or Gemini. Your chatbot's brief will differ in
its wording.

**One item in the brief is wrong on purpose.** It was changed by hand after the brief was written,
so you can see what the check catches. Try to find it with the [check sheet](../check-sheet.md)
before you read part 3.

## 1. What was pasted

1. All of [`SKILL.md`](../SKILL.md). The chatbot asked for the document.
2. The notice, from [`supplier-notice.md`](../supplier-notice.md), and one line:
   `I own the café. Make the brief.`

## 2. The brief that came back

<!-- brief:start -->

# Action brief: Quillmoor Provisions, Notice of changes to your supply terms, 2 November 2026

Read as: Lantern Step Café, the customer the notice is addressed to. Watch out: 1 penalty, 3
things you must do, 2 dates, 4 open questions.

## Key facts

| # | Fact | Quote | Where |
| --- | --- | --- | --- |
| F1 | Every change in the notice starts on 4 January 2027 | "The changes take effect on 4 January 2027" | para 1 |
| F2 | Deliveries move from Monday and Thursday to Tuesday and Friday | "deliveries to your area will move from Monday and Thursday to Tuesday and Friday" | para 2 |
| F3 | Free delivery now needs an order of $400 before tax, up from $250 | "The minimum order for free delivery will rise from $250 to $400 before tax." | para 5 |
| F4 | Dairy and eggs go up 6%. Dry goods stay the same | "Prices on dairy and eggs will increase by 6%. Prices on dry goods are unchanged." | para 8 |
| F5 | Invoices are still due 30 days after the invoice date | "Invoices remain due 30 days from the invoice date." | para 10 |
| F6 | Suggestion, not required: review your usual quantities before the change | "We recommend that customers review their usual quantities before the change." | para 7 |

## What you must do

| # | You must | By | Quote | Where |
| --- | --- | --- | --- | --- |
| O1 | Confirm your delivery window, 7 to 9 a.m. or 9 to 11 a.m., in the customer portal. If you do not, one is assigned to you | 1 December 2026 | "You must confirm your preferred delivery window (7 to 9 a.m. or 9 to 11 a.m.) in the customer portal by 1 December 2026." | para 3 |
| O2 | Place each order by 2 p.m. the business day before your delivery day | Every order, from 4 January 2027 | "orders must be placed by 2 p.m. the business day before your delivery day" | para 6 |
| O3 | If you pay by cheque, switch to pre-authorized debit using the enclosed form. **Penalty:** $25 added to each invoice paid by cheque after 4 January 2027 | Before 4 January 2027 | "Customers who currently pay by cheque must switch to pre-authorized debit before the effective date." and "An administration fee of $25 will be added to each invoice paid by cheque after the effective date." | para 9, para 10 |

## Dates

| # | Date | What happens | Quote | Where |
| --- | --- | --- | --- | --- |
| D1 | 1 December 2026 | Last day to confirm your delivery window | "in the customer portal by 1 December 2026" | para 3 |
| D2 | 4 January 2027 | New delivery days, order cut-off, minimum order, prices and the cheque fee all start | "The changes take effect on 4 January 2027" | para 1 |

## Open questions

| # | Question | Why it is unclear | Quote | Where |
| --- | --- | --- | --- | --- |
| Q1 | Will my standing order carry over, and do I need to enter it again? | The notice does not say what "where possible" means, or how you will find out | "Standing orders will carry over where possible." | para 4 |
| Q2 | What does delivery cost on an order under $400? | The notice sets the minimum for free delivery but gives no charge below it | "The minimum order for free delivery will rise from $250 to $400 before tax." | para 5 |
| Q3 | Does the payment change apply to this account? | It applies only to customers who pay by cheque, and the notice does not say how this account pays | "Customers who currently pay by cheque must switch to pre-authorized debit" | para 9 |
| Q4 | Which window will I get if I miss 1 December? | The notice says one will be assigned, not how | "Accounts that have not confirmed will be assigned a window." | para 3 |

**Check it yourself.** Find each quote in the notice. Tick an item if the words are there and say
what the brief says. Cross it if not, and tell me its number, for example: O2 is wrong. Then write
down the one action you will take first, and its date. I have not chosen it for you.

<!-- brief:end -->

## 3. The check, filled in

The café owner opened the notice beside the chat and looked for each quote.

| Item | Found at the place given? | Same words, same numbers? | Says what the brief says? | Tick or cross |
| --- | --- | --- | --- | --- |
| F1 to F6 | Yes | Yes | Yes | Tick |
| O1 | Yes, para 3 | Yes | Yes | Tick |
| **O2** | Para 6 is about the order cut-off | **No.** Para 6 says "two business days before", not "the business day before" | **No** | **Cross** |
| O3 | Yes, para 9 and para 10 | Yes | Yes. The $25 fee is in the middle of para 10 | Tick |
| D1, D2 | Yes | Yes | Yes | Tick |
| Q1 to Q4 | Yes | Yes | Yes | Tick |

**Why the cross matters.** With the wrong rule, a Tuesday delivery would be ordered on Monday. The
notice needs it by 2 p.m. on the Friday before. Every Tuesday order would miss its truck.

What the owner pasted into the chat:

```
O2 does not match the document: para 6 says two business days before.
Show me the exact words from the document, or correct the item.
```

The corrected line:

<!-- corrected:start -->
| O2 | Place each order by 2 p.m. two business days before your delivery day. For a Tuesday delivery that is Friday; for a Friday delivery, Wednesday (worked out from para 2 and para 6) | Every order, from 4 January 2027 | "orders must be placed by 2 p.m. two business days before your delivery day" | para 6 |
<!-- corrected:end -->

The owner ticked the new O2 after finding the words in para 6.

## 4. The one action

| My one action | By when | Who does it |
| --- | --- | --- |
| Confirm the 7 to 9 a.m. window in the customer portal | Friday 27 November 2026, a few days before the 1 December deadline | Me |

## 5. Who to ask

| Question | Who I will ask | By when |
| --- | --- | --- |
| Q1, standing order | Our account representative at Quillmoor | 27 November 2026 |
| Q2, delivery charge under $400 | Our account representative at Quillmoor | 27 November 2026 |

Q3 the owner answered alone: the café pays by bank transfer, so O3 does not apply. Q4 no longer
matters once O1 is done.

## 6. How it did against the test

The test in the plan: the brief lists all three obligations and both dates with exact quotes,
flags the penalty, and puts the ambiguous line under questions, not facts.

| Test | As returned (with the planted error) | After the check fixed O2 |
| --- | --- | --- |
| Three obligations with exact quotes | Two of three. O2's quote is not in the notice | Pass |
| Both dates with exact quotes | Pass | Pass |
| The buried $25 penalty flagged | Pass, inside O3 | Pass |
| "Standing orders will carry over where possible" under questions, not facts | Pass, Q1 | Pass |

These results come from the checker in [`_build/`](../../_build/README.md), which compares every
quote with the notice word for word. It is there to test the instructions. The check that counts
is yours.
