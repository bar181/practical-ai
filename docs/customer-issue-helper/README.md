# Customer issue helper

Paste your refund, returns, delivery or booking rules with a customer message, or save them once in a
project; for each message, get a reply draft
that quotes the rule it relied on, says "not covered" when your policy is silent, and flags when a
manager must decide.

**Status.** Draft, built and reviewed by AI on 25 November 2026, revised on 27 November 2026; not
yet tried by a person. A fresh Claude agent ran it to make the worked example (before the 27
November changes). Four separate reviewer agents ran it on new invented inputs and scored it 82,
82, 88 and 87 out of 100 ([review](review.md)); the fixes after the fourth round have not been
re-scored. Tried only in Claude so far.

![A customer message and your policy book go into the helper; out comes a reply draft, the rule it used, and flags for you](how-it-works.svg)

## The idea in one picture

**Think of it as** a new shop assistant with the rule book open on the counter. They answer every
question by pointing to the page, they say "I'll have to check with the manager" instead of making
something up, and they never hand over money themselves.

## Who it is for

- **Business people:** anyone who answers customers from written rules: a small shop owner, a
  customer service team, a freelancer with terms of service, an office manager with a booking
  policy.
- **Agentic developers:** a small, testable pattern for answering from a knowledge file with a
  citation on every claim, an "out of scope" answer, and a hand-off to a person.

## Try it: paste one file (5 minutes)

1. Open [`SKILL.md`](SKILL.md), press **Raw**, and copy all of it.
2. In Claude, ChatGPT or Gemini, start a new chat and paste it.
3. On a new line, paste your policy (your returns page is fine as it is), today's date, and one or
   more customer messages with the order number and dates. If a rule counts hours (for example
   "cancel 12 hours before"), add the exact times.
4. If anything is missing, it replies once with what to give it.

## What you get

For each customer message:

1. **A reply draft**, ready to edit and send.
2. **Why this reply:** each thing the customer asked, the decision (allowed, refused, not covered
   or manager decides) and the exact words of the rule used, with any date or amount arithmetic
   written out.
3. **Flags:** what a manager must decide and the question to put to them, what your policy does
   not cover (with a suggested rule to add), and any missing facts.
4. **Check before you send:** two to four things to confirm in your own systems.

[See the worked example](example.md): three invented customer messages for an invented ceramics
shop, with a deadline the policy cannot promise, a refund that five things send to a manager, and
a request the policy has no rule for.

## The files

| File | What it is for |
| --- | --- |
| [`SKILL.md`](SKILL.md) | The helper: answers customer messages from your policy |
| [`build-policy-book/SKILL.md`](build-policy-book/SKILL.md) | Turns your scattered rules (returns page, FAQ, notes) into a numbered policy book, and lists the conflicts and gaps it finds |
| [`policy-book-template.md`](policy-book-template.md) | The knowledge file: an index, one rule per entry with its source, what a manager decides, conflicts and gaps |
| [`example.md`](example.md) | One worked example, invented data |
| [`review.md`](review.md) | The AI review: scores and every point lost, with a chart ([`review-rounds.svg`](review-rounds.svg)) |
| [`paper.md`](paper.md) | A short technical paper on the tool |

## Levels

| Level | What it is | When it earns its place |
| --- | --- | --- |
| 1 | Paste `SKILL.md`, your policy and the messages into any chatbot | Always; start here |
| 2 | Run `build-policy-book` once, check the book, then save `SKILL.md` and the book in a Claude Project, ChatGPT Project or Gemini Gem. Each day, paste only the messages | When you answer customers most days and are tired of pasting the policy |
| 3 | Not built. A helpdesk or mailbox connection could bring messages in and put drafts back as drafts, never sent, with a person approving each one | Only if copying messages in and out becomes the slow part |

## Check before you send

- Every date and amount against your order system. The helper only knows what you paste.
- Each "Manager decides" flag goes to the person who decides, with the question it gives.
- Each "Not covered" flag: decide the answer, then add it to your policy book so the next reply is
  covered.

## What it does not do

- It does not send, refund, pay or post anything. A person decides and sends.
- It does not look up orders, tracking or payments. It works only from what you paste.
- It does not give legal advice. Consumer rights depend on where you and your customer are; your
  written policy may not be the whole of what the law requires. Check with a qualified adviser.
- It does not decide hard cases. A rule that says a manager decides, rules that conflict,
  promises or quotes by staff, your own records showing a rule was not followed, legal threats,
  chargebacks, threatened public reviews, injury or safety, and a customer pushing back always go
  to a manager. An answer that rests on its own reading of your
  words, on a rule marked unclear, or on records that disagree is marked "assumed": the reply
  promises nothing and a flag asks you. A plain request the policy says no to is refused kindly,
  with the reason.

## How it was checked

| ID | Spec line | Check | Result, who ran it, what they saw |
| --- | --- | --- | --- |
| U1 | A person who answers customers from written rules | Five invented businesses: a ceramics shop (example), a bike repair shop, a yoga studio, a plant shop and a dog groomer (reviews) | Claude agents, 25 and 27 Nov 2026: all five ran with no question needed |
| U2 | Their policy, the customer messages, today's date | Missing input: asks once for only what is missing, and waits | Passed in all four review rounds; see [review](review.md) |
| U3 | A reply draft with the rule it relied on | The normal case | [Worked example](example.md), fresh agent, unedited |
| U4 | Ready to send after a quick check | Would the person send the reply after the checks listed? | Reviewer agents scored 82, 82, 88 and 87; see [review](review.md). Not yet judged by a person |
| U5 | A reply that promises what the policy does not say | Planted traps: staff promises and a phone quote, a chargeback and a review threat, a sign-off limit, rules that disagree, instructions inside messages, an injury, an expired pass, a rule word ("a friend") that may not fit, last-day requests, a 20-minute miss on a 24-hour rule | No unsupported promise in any run. Round 2 found a promise resting on the tool's own reading, round 4 a staff quote stated as fact; both fixed, the round 4 fix not re-scored |
| U6 | Scattered rules into a policy book | `build-policy-book` run on its own on an invented returns page, delivery page, FAQ and owner's note | Round 3 reviewer, 27 Nov 2026: exact quotes, source order kept, three conflicts and twelve gaps found, nothing invented |
| | Works in other chatbots | The same file in ChatGPT or Gemini | Not yet run |
