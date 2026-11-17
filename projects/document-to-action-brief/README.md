# Document to action brief

<h3 align="center">Know what a document asks of you, by when, and where it says so.</h3>

<p align="center">For the notice, contract, tender, policy or bill you have to act on, in the chatbot you already use.</p>

**Are you an AI agent?** Go to [AGENTS.md](AGENTS.md) for instructions you can follow now.

- **The answer first.** Two lines: how many things you must do, the earliest date, and every
  penalty or cost, including the one buried in a friendly paragraph.
- **Every line you can check.** Each action, date and fact carries the exact words it came from
  and where they are. Search for them, tick them, then act.
- **Fitted to the situation.** A contract before signing, a change of terms, a tender or a bill
  each get the one extra section that reader needs.

<p align="center"><b><i>"Now I know what the letter wants from me, by when, and I can point to the line that says so."</i></b></p>

## Try it now: one prompt

Copy all of this into the chatbot you use. It holds the instructions and an invented supplier
notice, so you see the result before you use your own document. Tested so far in Claude; not yet
in ChatGPT or Gemini.

```
Read the document below and give me a one-page action brief.
I am the customer, Tallowmere Café. My manager will read it on her phone.

- Start with two lines: how many things we must do, the earliest
  date, and every penalty or cost.
- It is a change of terms, so add "What changes": old and new where
  the document states both, and any deadline to accept or say no.
- Then four short tables: What we must do (by when), Dates, Open
  questions, Key facts.
- Every row quotes the exact words it came from, in quotation marks,
  and says where (clause or paragraph), so I can find it with Ctrl+F.
- A line that can be read two ways, or depends on something I may not
  know, goes under Open questions, never Key facts.
- Use only the document. Do not tell me what to do: I decide.
- End with: "Check it: search for each quote, then write your one
  action: I will ... by ..."

DOCUMENT:
KESTREL FOLD WHOLESALE LTD
Trade supplies for cafés and restaurants

3 November 2026

To: Tallowmere Café (account TC-0418)

Subject: Changes to your terms of supply

Dear customer,

Thank you for buying from Kestrel Fold. We are updating the terms of supply for all trade accounts. The changes below take effect on 1 December 2026. Our prices are not changing as part of this notice.

1. Ordering

From 1 December 2026, orders must be placed by 2:00 pm two working days before your delivery day. Orders received after this time will be delivered on your next scheduled delivery day.

2. Delivery days

Accounts on our standard plan will move to Tuesday and Friday deliveries. Your driver will confirm the new delivery window in the week before the change.

3. Minimum order

The minimum order value for free delivery rises from $150 to $200, before tax. Orders below the minimum carry a delivery charge of $18.

4. Payment

Invoices are now due 14 days from the invoice date, down from 30 days. We accept payment by bank transfer or card, and card payments over $1,000 carry a 1.5% surcharge. We know that cash flow matters to small businesses, and our accounts team is always happy to talk. Where an invoice remains unpaid after its due date, an administration fee of $35 per invoice will be added, and further orders may be held until the account is settled. Statements will continue to be sent at the start of each month.

5. Confirming the new terms

Please sign the acceptance form below and return it to accounts@kestrelfold.example by 20 November 2026. If you have any questions about these changes, please speak to your account manager.

Thank you for your continued business.

Accounts team
Kestrel Fold Wholesale Ltd

ACCEPTANCE FORM

I accept the Kestrel Fold Wholesale terms of supply that take effect on 1 December 2026.

Account number: TC-0418
Name: ____________ Signature: ____________ Date: ____________
```

<p align="center">
  <img src="_build/img/example-brief.webp" width="460" alt="The first screen of the brief a fresh Claude session wrote from this prompt: the title Action brief: Kestrel Fold change of terms; the answer first, 3 things to do, earliest date 20 November 2026, and every cost and penalty; then a What changes table of old and new terms, each with the exact words and the clause">
</p>

**You get a brief like this.** A fresh Claude session wrote it from the prompt above in one try,
unedited: three actions, the earliest date, every penalty up top, and nine open questions, such as
whether the café is on the "standard plan" the notice mentions.
[Read the whole brief](quality-results/2026-11-17-try-it-prompt/reply.md).

## Get started

<p align="center">
  <img src="_build/img/how-it-works.svg" width="720" alt="How it works, in three steps. 1: paste the prompt and your document. 2: get the brief: the answer first, then what you must do, dates, open questions and key facts, each with the exact words. 3: find each quote, tick it, then decide. The AI lists. You check and decide.">
</p>

1. **Paste.** Use the prompt above and replace everything after `DOCUMENT:` with your own
   document, or attach the file. Change the second line to say who you are and who reads it.
2. **Read the answer first,** then the tables.
3. **Check, then decide.** Search for each quote (Ctrl+F or Cmd+F) and tick it. Write your one
   action: "I will ... by ...". The brief lists; you decide.

Paste real documents only into a chatbot your workplace allows for them. A scan or photo with no
selectable text will not work: copy the text out first.

## Fitted to your situation

Say what kind of document it is, or let the AI work it out. Each kind adds one section to the brief.

| Your document | The brief adds |
| --- | --- |
| A contract or agreement, before you sign | **Before you sign:** what you commit to, how it renews and ends, what leaving early costs, and questions to ask the other side |
| A change of terms or a supplier notice | **What changes:** old and new, side by side, and the deadline to accept or say no |
| A policy, rule or regulation update | **Does it apply to us:** who it covers, as written, and when it starts |
| A tender or request for quotes | **Can we bid:** who may bid, the question and bid deadlines, and every document to send |
| A report, board pack or proposal | **What it asks of me:** the decisions asked for, numbers that changed, risks named |
| A bill, tax notice or official letter | **Pay or reply:** the amount, the due date, how to pay or reply, and what happens if you do not |

**Who reads it** changes the top: for a busy boss, three lines they can forward; for your team, a
"who does it" column.

## Level 2: save it, so every document gets the same brief

For anyone who gets documents like this every week. Install the full instructions,
[`base/SKILL.md`](base/SKILL.md), once:

- **Claude:** add it as a skill, or paste it into a Project's instructions.
- **ChatGPT:** add it as a skill (it uses the same open Agent Skills format) or paste it into a
  Project's instructions.
- **Gemini:** paste it into a Gem's instructions.

Then just attach a document. Level 2 also adds your **house rules**: who you are, the documents you
get, and who answers which question, so every brief fits your business.
[Set up Level 2](level-2-files/README.md).

## Level 3: hands-off (planned, not built)

The brief runs on its own when a document arrives: a scheduled task watches an inbox label or a
folder, writes each action and date to a register with an owner, drafts reminders for you to
send, and puts anything unclear or costly in a review lane for a person. Nothing is sent or signed
without you. [What Level 3 would include, and why](level-3-files/README.md).

## What it is not

- **Not legal, tax or financial advice.** It lists what the document says. Whether a term is fair or
  binding is a question for a lawyer or an accountant.
- **Not a contract risk review.** For that, a legal team can use a review tool such as Anthropic's
  open-source Legal plugin. This brief is for the business person who has to act.
- **Not a sender.** It never replies, signs, accepts or pays. You do.

## Questions

<details><summary><b>Which chatbots does it work in?</b></summary>

Tested so far in Claude only. It is plain instructions, so it should work in ChatGPT, Gemini and
others, but that has not been tried yet.
</details>

<details><summary><b>How do I know the brief is right?</b></summary>

You check it. Every row has the exact words from the document, so you can find each one with
Ctrl+F in seconds. A row you cannot find gets a cross and is not acted on.
</details>

<details><summary><b>What if the document leaves something out?</b></summary>

The brief says so at the top, marks any date it cannot work out, and puts the gap under open
questions with who could answer. It never fills a gap with a guess.
</details>

<details><summary><b>Does it cost anything?</b></summary>

No. It is free under the Apache 2.0 licence and runs in the chatbot you already pay for or use free.
</details>

**Quick start in one line:** "Hey chatbot, follow https://raw.githubusercontent.com/bar181/practical-ai/main/projects/document-to-action-brief/base/SKILL.md and brief me on this document: [paste it]". Not yet tested with the link.

## Status

**17 November 2026.** Built by its author with [Agentic Process](../agentic-process/), where an
earlier version scored 93/100 in a blind pilot against 73/100 for a direct build. Tested in three
fresh Claude sessions: the try-it prompt above, a notice that leaves out its date and its price
list, and a tender. Not yet tried in other chatbots, or by anyone else. Level 3 is not built. All
example documents and businesses are invented. [The evidence](quality-results/README.md).

<img src="../agentic-process/_build/img/bradley-ross-avatar.webp" width="110" alt="Cartoon avatar of Bradley Ross with a small friendly robot">

Made by **Bradley Ross**, who builds and teaches practical AI. Part of [Practical AI](../../README.md).
