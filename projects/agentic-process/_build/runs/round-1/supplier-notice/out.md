# Build coach session: notice checker

Status: first version written on 16 November 2026. Nobody has tried it. No chatbot has run the prompt and no student has seen it.

I could not ask you questions and could not search the web. Every choice I would have put to you is listed under Assumed in the note. Nothing about existing tools or prices is checked.

This document has two parts: the nine steps as played, then the hand-over (1 the plan, 2 the first version, 3 the note).

## The session

### Step 1 of 9: scope

Would have asked: is the one user you or a student, and what would make a student stop and look?

Decided:
- User: one student in your small-business AI class, using the chatbot they already have.
- Job: turn one supplier notice or business report into a list of key facts, obligations, dates and questions, each tied to the exact words it came from, then check every item against the document.
- What is out, the wow and the test are in the plan.

Gate: "Can you say the job in one sentence?" Assumed yes: the job line above.

### Step 2 of 9: reuse check

I cannot search, so this step is not checked. Look up:
- For each chatbot your students use: does the free version take a pasted or attached document of the length you teach with, and does it quote the source when asked?
- Does any of those chatbots have a built-in feature that answers from a document you give it and shows the passage it used?
- Is there a free tool made for answering from your own documents with the source shown?
- Is there a standard checklist for reading a supplier notice, for example from a small-business body, that the four headings should follow?

Decided: common practice is to paste a document into a chatbot and ask. Whether that gives a quote for every item and a check, without careful instructions, is not checked. Those instructions are what this tool is.

Gate: "Does something existing do the whole job?" Assumed no, unchecked. If your lookups say yes, stop here and ask the coach for a short guide to that thing.

### Step 3 of 9: outside help

Not checked. I name no product and pick none. Look up:
- Paid versions of the chatbots your students use: what they add for documents (length, attachments) and how they charge.
- Services that pull fields out of business documents: what they cover and how they charge (by page, by document or by subscription).
- Tools that turn a scanned or photographed page into text. Needed only if your students' notices arrive on paper.

Decided: build the prompt. Buy nothing for the first version.

Gate: "Do you know what you would build and what you would buy?" Assumed yes.

### Step 4 of 9: cost

| Dependency | Who has it | Price | Limit |
| --- | --- | --- | --- |
| The student's own chatbot | each student, already | not checked | not checked: message caps, how long a document it reads, whether the free version takes attachments |
| Your git repository | you, already | not checked | not checked |
| Your coding agent | you, already | not checked | not checked |
| The prompt and example files | new: seven small text files | nothing to buy | none |
| The document as text | the student | not checked if it has to be converted from a scan or photo | scans and photos are out of the first version |

Decided: the first version adds no new paid thing. What you and your students already pay is not checked.

Gate: "Does the first version cost nothing, or an amount you accept?" Assumed yes.

### Step 5 of 9: simplest design

Would have asked: do you have a project template for your repository? Assumed no.

Decided:
- Assistant: whatever chatbot each student has. The prompt names no product.
- Files: the tool lives in a folder in your git repository. The student's document stays with the student and never goes in the repository.
- Manual: pasting the prompt, pasting the document, searching the document for each quote, and deciding what to do about any of it.

Folder layout, now fixed for the first version:

```
notice-checker/
  README.md                          the front page
  PLAN.md                            the one-page plan
  NOTE.md                            the hand-over note
  prompt.md                          what a student pastes
  examples/
    supplier-notice-invented.md      the invented notice
    supplier-notice-good-result.md   what a good result looks like
  tests/
    fresh-chat-test.md               how to test, and the pass list
```

Gate: "Could a beginner draw this?" Assumed yes. Three boxes in a row: prompt plus document, chatbot, checked list. One arrow back from the list to the document, done by the student.

### Step 6 of 9: plan and front door

Decided:
- The steps a student follows are in the plan and on the front page (section 2a).
- The first thing they see is the front page: one line saying what it does, then five steps.
- The worked example is one invented supplier notice and a good result for it (section 2c).

Gate: "Is the beginner version fully described?" Assumed yes.

### Step 7 of 9: review

Would have asked: who will read the plan? Assumed nobody can, so I read it as a stranger. Three weak points:

1. The chatbot marks its own work. The second pass is done by the same chatbot that made the list, so it can agree with its own mistake. The check that counts is the student searching for the quote.
2. Pages and long documents. Pasted text often loses its page numbers, so "where" may be a heading or a paragraph. A long report may be cut short without warning. The last-sentence line in the prompt is the only guard.
3. "Whatever chatbot they have" means the prompt is tested on none of them, and a real supplier document goes wherever that chatbot sends it. Neither is checked.

Explained back, as the stranger: a student pastes a set of instructions and one document into a chatbot. They get four lists with the exact words behind each item, a table saying whether each item holds up, and then they check the quotes themselves.

Gate: "Can a reviewer explain it back?" Assumed yes, on my own reading only. No person has reviewed it.

### Step 8 of 9: build and test

Decided:
- The first version is written: front page, prompt, worked example and test sheet (section 2).
- Of the four checks in the test sheet, I ran one: all 14 quotes in the good result appear word for word in the invented notice. The other three need the folder, which does not exist yet.
- The fresh-chat test is described in section 2d. It has not been run.

Gate: "Did the fresh chat finish the job, and what did it trip on?" Open. I cannot answer this for you. I went on to step 9 only so the hand-over is complete.

### Step 9 of 9: grow

Decided: the next three additions, smallest first, one at a time.
1. A test log in the repository: which chatbot, which date, who ran it, what it tripped on.
2. A second worked example: a short invented business report.
3. A longer invented document with page numbers, to see where page references and length break.

Gate: "Is the first version in use?" No.

---

## 1. The plan

**The job.** Turn one supplier notice or business report into key facts, obligations, dates and questions, each with the exact words it came from, then check every item against the document.

**The user.** One student in a small-business AI class, using the chatbot they already have.

**What is out.** More than one document at a time. Scanned pages and photos. Advice on what to do. Replies to the supplier. Storing documents. Anything that runs without a person. Comparing documents.

**The wow.** Every item shows the exact words it rests on. A student can see in seconds whether the chatbot made something up, and items that fail the check stay on the page, marked.

**What already exists.** Not checked. Common practice is to paste a document into a chatbot and ask. The lookups are in step 2.

**Cost.** No new paid thing. Prices and limits of the students' chatbots, your repository and your coding agent are not checked.

**The design.** One prompt in plain text, kept in a folder in your git repository with one worked example and one test sheet. Layout in step 5. The chatbot makes the list and checks it once. The student checks it again by eye.

**The steps.**
1. Open a new chat.
2. Paste the prompt.
3. Paste the document under it and send.
4. Read the check table.
5. Search the document for each quote, dates and obligations first. Read for yourself any part marked Partly backed or Not found.

**The test.** Input: the invented Northfield Packaging Supply notice (section 2c). A good result passes all seven lines of the pass list in section 2d. In short: all five dates are there, every quote can be found word for word, the missing hold date shows up as a question and never as a fact, and there is no advice.

**Next three additions.** A test log. A second worked example from an invented business report. A longer invented document with page numbers.

---

## 2. The first version

Written, not used. Nobody has tried it.

### 2a. The front page (`README.md`)

```
# Notice checker

Turn one supplier notice or business report into key facts, obligations,
dates and questions, each with the exact words from the document. Then check
every item against the document.

Status: first version, 16 November 2026. Nobody has tried it yet.
Change this line when someone has, and say who.

## Use it

1. Open a new chat in the chatbot you already use.
2. Paste everything in prompt.md.
3. Paste your document under it and send. The first time, use
   examples/supplier-notice-invented.md.
4. Read the check table at the end of the answer.
5. Search your document for each quote. Start with the dates and the
   obligations. If an item is marked Partly backed or Not found, read that
   part of the document yourself.

## Before you paste a real document

Find out what your chatbot does with what you paste: who can see it and how
long it is kept. This has not been checked for any chatbot.

## What it does not do

More than one document at a time. Scanned pages or photos. Advice on what to
do. Replies to the supplier.

## Files

prompt.md        what you paste
examples/        one invented notice and a good result for it
tests/           how to test the prompt in a fresh chat
PLAN.md          the one-page plan
NOTE.md          what was decided, assumed and not checked
```

### 2b. The prompt (`prompt.md`)

```
I am going to give you one business document: a supplier notice or a business
report. I have to act on it, so I need to know exactly what it says and be
able to prove each point from the document itself. Please work in two passes.

If I have not given you the document yet, ask me for it and wait. If I give
you more than one document, ask me which one to do first.

PASS 1: PULL OUT THE ITEMS

Read the whole document. Then give me four tables.

1. Key facts: what is changing or being reported, such as amounts, prices,
   quantities, names and terms.
2. Obligations: anything someone must do or must stop doing. Say who has to
   do it: me, the supplier or someone else.
3. Dates: every date and deadline in the document, and what happens on it.
4. Questions: things I would need to know before acting that the document
   does not say or leaves unclear.

Number every item: F1, F2 for facts, O1 for obligations, D1 for dates, Q1 for
questions. For each fact, obligation and date, give three things:

- The item in plain words, in one sentence.
- The exact words from the document that back it, copied letter for letter,
  in quotation marks. Copy, do not reword. I will search the document for
  this quote, so a reworded quote is no use to me.
- Where it is: the page number if the text shows page numbers. If it does
  not, the heading it sits under or the paragraph counted from the top.

For each question, say which part of the document raised it, or say "the
document is silent on this".

Use only the document. If something is usual in documents like this but is
not written in this one, it belongs under Questions, not under facts. If a
table has nothing in it, write "None found".

PASS 2: CHECK YOUR OWN LIST

Go back to the document and check each numbered fact, obligation and date
against it, one at a time. Give me a table with the item number, a verdict
and a reason. Use these verdicts:

- Backed: the quote is in the document word for word, and it says what the
  item says.
- Partly backed: the quote is there, but the item says more than the quote
  does. Tell me what the extra part is.
- Not found: you cannot find the quote word for word in the document.

Do not quietly fix or remove an item that fails. Leave it in and mark it, so
I can see what went wrong.

FINISH WITH THREE LINES

- The last sentence of the document as you received it, in quotation marks,
  so I can tell whether you got all of it.
- How many items are Backed, Partly backed and Not found.
- This line, as written: "Now check it yourself: search the document for
  each quote. Start with the dates and the obligations."

Give me no advice on what to do, no summary paragraph and no draft reply.
I only want what the document says, where it says it, and what it leaves
open.

My document:
```

### 2c. The worked example

**The input (`examples/supplier-notice-invented.md`).** Invented data. Northfield Packaging Supply does not exist. Every name, price and date below is made up for testing.

```
Northfield Packaging Supply
Notice to trade customers
5 January 2027

Changes to prices, minimum order and payment terms

Prices
From 1 March 2027 the list price of all corrugated boxes will rise by 6 percent. Prices of tape and labels will not change.

Orders at the current price
Orders received on or before 15 February 2027 will be invoiced at the current price, provided delivery is taken by 31 March 2027.

Minimum order
From 1 March 2027 the minimum order will be 25 cases. The current minimum is 10 cases.

Payment terms
Payment terms will change from 30 days to 21 days from the invoice date for all invoices issued on or after 1 March 2027. A late fee of 2 percent per month will apply to overdue balances.

Your account
To keep your account active, you must confirm your billing contact by 31 January 2027 using the form sent with this notice. Accounts that have not confirmed will be placed on hold.

We will write to you again before any further change. Questions about this notice can be sent to your account representative.
```

**A good result (`examples/supplier-notice-good-result.md`).** Written by hand by the coach to show the target. It is not the output of a chatbot run. A real run may word things differently, split items differently, or mark some items Partly backed or Not found. A marked item means the check is working.

Key facts

| No. | Item | Exact words | Where |
| --- | --- | --- | --- |
| F1 | The list price of all corrugated boxes rises by 6 percent from 1 March 2027. | "From 1 March 2027 the list price of all corrugated boxes will rise by 6 percent." | Prices |
| F2 | Tape and label prices stay the same. | "Prices of tape and labels will not change." | Prices |
| F3 | An order received on or before 15 February 2027 is invoiced at the current price if delivery is taken by 31 March 2027. | "Orders received on or before 15 February 2027 will be invoiced at the current price, provided delivery is taken by 31 March 2027." | Orders at the current price |
| F4 | The minimum order becomes 25 cases from 1 March 2027. It is 10 cases now. | "From 1 March 2027 the minimum order will be 25 cases. The current minimum is 10 cases." | Minimum order |
| F5 | Overdue balances carry a late fee of 2 percent per month. | "A late fee of 2 percent per month will apply to overdue balances." | Payment terms |
| F6 | Accounts that have not confirmed are placed on hold. | "Accounts that have not confirmed will be placed on hold." | Your account |

Obligations

| No. | Who | Item | Exact words | Where |
| --- | --- | --- | --- | --- |
| O1 | You | Confirm your billing contact by 31 January 2027, using the form sent with the notice. | "you must confirm your billing contact by 31 January 2027 using the form sent with this notice" | Your account |
| O2 | You | Pay within 21 days of the invoice date, not 30, on invoices issued on or after 1 March 2027. | "Payment terms will change from 30 days to 21 days from the invoice date for all invoices issued on or after 1 March 2027." | Payment terms |
| O3 | The supplier | Write to you again before any further change. | "We will write to you again before any further change." | Closing lines |

Dates

| No. | Date | What happens | Exact words | Where |
| --- | --- | --- | --- | --- |
| D1 | 5 January 2027 | The notice is dated. | "5 January 2027" | Top of the notice |
| D2 | 31 January 2027 | Deadline to confirm your billing contact. | "you must confirm your billing contact by 31 January 2027" | Your account |
| D3 | 15 February 2027 | Last day an order can be received at the current price. | "Orders received on or before 15 February 2027 will be invoiced at the current price" | Orders at the current price |
| D4 | 1 March 2027 | The box price rise starts. The new minimum order (F4) and the new payment terms (O2) start on the same date and carry their own quotes. | "From 1 March 2027 the list price of all corrugated boxes will rise by 6 percent." | Prices |
| D5 | 31 March 2027 | Last day to take delivery of an order at the current price. | "provided delivery is taken by 31 March 2027" | Orders at the current price |

Questions

| No. | Question | What raised it |
| --- | --- | --- |
| Q1 | When is an unconfirmed account placed on hold, and how is a hold lifted? | Your account: it says accounts "will be placed on hold" and gives no date and no way back. |
| Q2 | If the supplier cannot deliver by 31 March 2027, does an order received by 15 February 2027 still get the current price? | Orders at the current price: the document is silent on this. |
| Q3 | Is the 2 percent late fee new, and from what date does it apply? | Payment terms: the document is silent on this. |
| Q4 | Does the 25-case minimum apply to each order or to each product? | Minimum order: the document is silent on this. |
| Q5 | Where is the form? The notice refers to "the form sent with this notice" and no form is in the text I received. | Your account |

Check

| Item | Verdict | Reason |
| --- | --- | --- |
| F1 | Backed | Quote found under Prices. It gives the date, the product and the 6 percent. |
| F2 | Backed | Quote found under Prices. |
| F3 | Backed | Quote found under Orders at the current price. It gives both dates and the condition. |
| F4 | Backed | Both sentences found under Minimum order. They give 25 cases, the date and the current 10 cases. |
| F5 | Backed | Quote found under Payment terms. |
| F6 | Backed | Quote found under Your account. |
| O1 | Backed | Quote found under Your account. It gives the duty, the date and the form. |
| O2 | Backed | Quote found under Payment terms. It gives 30 days, 21 days and the start date. |
| O3 | Backed | Quote found in the closing lines. |
| D1 | Backed | Date found at the top of the notice. |
| D2 | Backed | Quote found under Your account. |
| D3 | Backed | Quote found under Orders at the current price. |
| D4 | Backed | Quote found under Prices. |
| D5 | Backed | Quote found under Orders at the current price. |

Last sentence received: "Questions about this notice can be sent to your account representative."

Backed: 14. Partly backed: 0. Not found: 0.

Now check it yourself: search the document for each quote. Start with the dates and the obligations.

### 2d. The test sheet (`tests/fresh-chat-test.md`)

**The fresh-chat test.** A person runs this. It has not been run.

1. Open a new chat in one chatbot your students use. If that chatbot keeps memory or saved instructions, turn them off for this chat. How to do that in each chatbot is not checked.
2. Paste the whole of `prompt.md`. Paste the invented notice under it. Send. Add nothing else and do not help it.
3. Go down the pass list.
4. Write down the chatbot, the date, who ran it and what it tripped on.

Pass list:

1. All five dates appear: 5 January, 31 January, 15 February, 1 March and 31 March 2027.
2. Every fact, obligation and date has a quote, and each quote can be found word for word by searching the notice.
3. Confirming the billing contact by 31 January 2027 appears as something you must do.
4. Nothing appears as a fact that the notice does not say. In particular: no date for when accounts go on hold, and no claim that the late fee is new.
5. There is a check table with a verdict for every numbered fact, obligation and date.
6. The last sentence reported is "Questions about this notice can be sent to your account representative."
7. There is no advice, no summary paragraph and no draft reply.

The number of items and their wording may differ from the good result. That is not a fail.

**Checks your coding agent can run in the repository.** These are my reading of "runs the checks". The coach's instructions do not define them.

| # | Check | Run? |
| --- | --- | --- |
| 1 | Every file in the folder layout exists | Not run: the folder does not exist yet |
| 2 | Every quote in the good result appears word for word in the invented notice | Run on this hand-over: 14 of 14 found |
| 3 | Both example files say the data is invented | Not run |
| 4 | `prompt.md` names no chatbot product | Not run |

The coding agent stops there. Giving the prompt to students is your decision and your action.

---

## 3. The note

Who has tried it: nobody. The first version is written, not used. No chatbot has run the prompt and no student has seen it.

### Decided

These follow from your message or are plain drafting choices.

- The first version is a prompt a student pastes into a chat, in plain text, tied to no one chatbot, because your students use whatever chatbot they already have. No code.
- The tool is a small folder of text files that your coding agent can create in your git repository from section 2 of the hand-over.
- Every fact, obligation and date carries the exact words from the document and where they are, so a student can search for them.
- The chatbot must keep and mark an item that fails its check. It may not quietly fix or drop it.
- The chatbot reports the last sentence it received, so a student can see when a long document was cut short.
- The worked example uses an invented supplier, with invented prices and dates, and says so.
- The tool sends, posts, pays and publishes nothing. Handing the prompt to students is your action.

### Assumed

I could not ask you anything. Each line below is a question or a gate I answered for you. Change any of them and tell the coach.

1. The one user is a student, not you. You are the builder.
2. Both kinds of document (supplier notice, business report) and both halves (make the list, check the list) count as one job. Only the supplier notice has a worked example.
3. The wow is that each item shows the exact words it rests on, so a student can tell in seconds whether the chatbot made something up.
4. "The page it came from" means the place in the document: the page number when the text shows one, otherwise the heading or paragraph.
5. The check has two layers. The chatbot checks its own list, then the student searches the document for each quote. The student's check is the one that counts.
6. Step 2 gate, "Does something existing do the whole job?": answered no. This was not checked. If the true answer is yes, this build should stop and become a short guide to that thing.
7. Step 3 gate: you build the prompt and buy nothing for the first version.
8. Step 4 gate: the cost is acceptable, because the first version adds no new paid thing to what you and your students already have. No price was checked.
9. You have no project template. The folder is called `notice-checker` and sits at the top of your tools repository. The name and place are mine.
10. Students get the text of the prompt and the invented notice from you by hand. They never need the repository.
11. Students have their documents as text they can paste or attach. Scanned pages and photos are out of the first version.
12. Nobody is available to review the plan, so I reviewed it as a stranger.
13. Gates 1, 5, 6 and 7 are answered yes.
14. Gate 8, "Did the fresh chat finish the job, and what did it trip on?", is open. No fresh chat was run. I went on to step 9 only so the hand-over is complete.
15. Gate 9, "Is the first version in use?": no.
16. You fit the second kind of person (you build with agents and keep a repository) and your students fit the first (new, a prompt they can paste). I combined the two rows.

### Not checked

- The web. Nothing was searched, so steps 2, 3 and 4 give no links and no dates. The lists of what to look up are in those steps.
- Whether any chatbot or free tool already does the whole job.
- Any paid option, and any price or limit: chatbots, your repository host, your coding agent.
- Whether the prompt works in any chatbot. The "good result" in the worked example was written by hand by the coach. It is not the output of a chatbot run.
- What each student's chatbot does with a pasted document: who can see it and how long it is kept. Check this before a real supplier document goes in.
- Whether your repository has a template or naming rules.
- Checks 1, 3 and 4 in the test sheet, because the folder does not exist yet. You named no repository path, so I created nothing in it.

One thing was checked: all 14 quotes in the worked example appear word for word in the invented notice (check 2, run mechanically on the hand-over file).

### Test this next

1. Run the fresh-chat test yourself on the invented notice in one chatbot. Write down what it tripped on.
2. Run it again in a second chatbot that your students use.
3. Give the prompt and the invented notice to one student with no help. Watch where they stop.
4. Do the step 2 lookups. If something existing does the whole job, stop and write the guide instead.
5. Only then try a real document, after the privacy check above.
