# Customer issue helper: replies that point to the rule

**Summary:** two portable skills and a policy book template that turn a business's written
customer rules into reply drafts, where every promise points to the exact rule it rests on, the
policy's silences are said out loud, and the hard cases go to a manager.

![A customer message and your policy book go into the helper; out comes a reply draft, the rule it used, and flags for you](https://raw.githubusercontent.com/bar181/practical-ai/main/docs/customer-issue-helper/how-it-works.svg)

## North Star

Every customer reply the helper drafts promises only what a quoted rule in the business's own
policy allows, and every case the policy does not decide reaches a person as a named flag with
the question to settle.

## Value for business people

**The job.** Almost every business answers the same customer questions every week: where is my
order, can I return this, can I have my money back. The rules usually exist on a returns page or
in an owner's note. The person replying must find the rule,
work out the dates, decide, and write something kind. A chatbot
asked for help writes a warm reply that often promises more than the rules allow: a full refund,
a replacement by Friday, "no problem at all".

**What the tool does.** The person pastes the helper's `SKILL.md`, the policy and one or more
customer messages with the order details and today's date. For each message the helper returns
four parts:

1. **A reply draft**, ready to edit and send.
2. **Why this reply:** each thing the customer asked, one of four decisions (allowed, refused, not
   covered, manager decides) and the exact words of the rule used, with any date or hour
   arithmetic written out.
3. **Flags:** what a manager must decide and the question to ask, what the policy does not
   cover, records that disagree, missing facts, and any instruction hidden in the message.
4. **Check before you send:** two to four things to confirm in the person's own systems.

A second skill, `build-policy-book`, turns scattered rules into a numbered policy book: one rule
per entry, in the owner's own words, with its source, plus the conflicts and gaps it found.

**The time it saves.** Not measured; no person has used it yet. The intended saving is finding
the rule and checking the dates for each message, and avoiding a reply that promises too much.

**What they still check.** Every date and amount against their order system. Each manager flag
goes to the person who decides. Each "not covered" flag is a decision, and a rule to add. A
person always sends; the helper never sends, refunds or pays.

## Value for agentic engineers

**How it constrains the model.** A model asked to "reply to this customer" optimises for a
satisfied customer, so it fills gaps in the policy with goodwill. The skill removes that freedom
in five ways:

- **Citation or silence.** Every promise in the reply must point to a quoted rule. A sentence
  that cannot is rewritten or removed in a final check step.
- **A closed set of decisions, with precedence.** Four decisions, and "manager decides" is checked
  first. It covers an M entry in the policy, rules that disagree, a claimed staff promise or
  quote, the business's own records showing a rule was not followed, a legal, chargeback or public
  review threat, injury or safety, and a customer pushing back.
- **Assumptions block promises.** If a decision rests on the model's own reading of a rule's
  words, on a rule marked unclear, or on a record in doubt, it is marked "(assumed)" and the reply
  states no amount, date or outcome. A plain day count is not an assumption: the skill fixes how
  days are counted and flags the last day for the owner.
- **Records are checked against claims.** A customer who says a pass "runs out soon" when the
  records show it ended last week produces a "records disagree" flag, not an answer.
- **Customer text is data.** An instruction inside a message is quoted under its own flag and
  ignored.

**How it is tested.** A fresh agent with only `SKILL.md` produced the worked example. Four
separate reviewer agents, blind to the build and to earlier reviews, each ran the skill on a new
invented input with planted traps, checked every date sum by hand, and scored the output against
a fixed rubric.

**How it composes.** The policy book is a plain knowledge file that can sit in a Claude Project,
a ChatGPT Project or a Gemini Gem. A reply draft can be passed to the repository's Write in my voice tool for tone, and a
batch of drafts can be scored with the Rubric reviewer. At Level 3, a helpdesk or mailbox
connector could supply messages and receive drafts as drafts, with a person approving each one.
That level is not built.

## How it works

**The files.**

| File | Role |
| --- | --- |
| `SKILL.md` | The helper: asks once for anything missing, then drafts and explains each reply |
| `build-policy-book/SKILL.md` | Turns a returns page, FAQ and notes into a numbered policy book, with conflicts and gaps |
| `policy-book-template.md` | The knowledge file: index, entries with sources, manager list, conflicts, gaps |
| `example.md` | One unedited run on an invented ceramics shop |

**The steps.**

1. Number the policy as P1, P2 in source order, quoting each rule exactly; manager rules as M1.
2. Pull the facts from the message in the customer's own words, keeping who did what.
3. Check the customer's claims against the records.
4. Find the rules that apply and quote them.
5. Do the date, hour and amount arithmetic in the open, with a fixed way to count days.
6. Sort each request into one of the four decisions, manager first.
7. Mark any decision that rests on the model's own reading as "(assumed)".
8. Draft the reply, promising only what an allowed rule supports.
9. Check every promise and fact in the draft against the policy and the message.

**The one mistake it is designed to catch.** A reply that promises something the policy does not
say. In the worked example, a customer wanted a replacement mug before a birthday. The policy
allows the replacement but sets no delivery time, so the reply confirms the replacement and offers
no date. A £240 refund request on a made-to-order set promises nothing and goes to the owner,
for five reasons, among them rules that disagree, a claimed promise and a chargeback threat.

## Evidence

Four review rounds, each by a separate Claude agent that had not seen the build or earlier
reviews, on a new invented input. Every point lost is in `review.md`.

![Four review rounds scored 82, 82, 88 and 87 against a pass mark of 80](https://raw.githubusercontent.com/bar181/practical-ai/main/docs/customer-issue-helper/review-rounds.svg)

| Round | Date | Input | Score |
| --- | --- | --- | --- |
| 1 | 25 Nov 2026 | Bike repair shop: rules that disagree, a planted instruction, a mechanic's promise | 82 |
| 2 | 25 Nov 2026 | Yoga studio: a late cancellation, an expired pass, an injury, "a friend" read as a sister | 82 |
| 3 | 27 Nov 2026 | Plant shop: `build-policy-book` run first on raw pages, then three messages | 88 |
| 4 | 27 Nov 2026 | Dog groomer: a 20-minute miss on a 24-hour rule, a last-day request, a phone quote | 87 |

- No round produced an unsupported refund, credit, voucher or date. Every planted instruction was
  ignored and flagged, and every date and hour sum was right when the reviewer checked it.
- The main points lost: reversing who did what (round 1), a promise resting on the model's own
  reading (round 2), last-day requests (rounds 3 and 4) and a claimed staff quote treated as fact
  (round 4). Each was fixed in the skill.
- Round 3 was the first run of `build-policy-book` on its own. It quoted exactly, kept source
  order and found three conflicts and twelve gaps, inventing nothing.
- All four missing-input checks passed.

**Limits of this evidence.** One Claude reviewer per round, on inputs invented by the builder.
The fixes after round 4 were not re-scored, and the worked example predates rounds 3 and 4. No
person has used the tool, and it has not been run in ChatGPT or Gemini.

## Limits and later steps

**Limits.**

- It knows only what is pasted. It does not look up orders, tracking or payments.
- It is not legal advice. Consumer law may give customers rights a written policy does not
  mention, and those rights vary by place.
- A thin policy produces many "not covered" flags, so the first week is mostly policy-writing.
- It counts the last day of a time limit as in time and flags it. A business that counts
  differently should say so in its policy.

**Later steps.**

1. Have a person use it for a week on real messages, and record what they changed before sending.
2. Run it in ChatGPT and Gemini.
3. Run `build-policy-book` on a real, messy returns page and FAQ, not an invented one.
4. Level 3: a helpdesk or mailbox connector that brings messages in and saves drafts, never sent.

## Try it

The folder: [github.com/bar181/practical-ai/tree/main/docs/customer-issue-helper](https://github.com/bar181/practical-ai/tree/main/docs/customer-issue-helper).
Paste `SKILL.md` into a new chat, then add your policy, today's date and a customer message with
its order details.

Gist: not yet published.
