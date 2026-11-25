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

**The job.** Almost every business answers the same customer questions every week. Where is my
order? Can I return this? It arrived broken. Can I cancel? Can I have my money back? The rules
usually exist on a returns page or in an owner's note. The person replying must find the rule,
work out the dates, decide, and write something kind. When
they ask a chatbot for help, the chatbot writes a warm reply that often promises more than the
rules allow: a full refund, a free replacement by Friday, "no problem at all".

**What the tool does.** The person pastes the helper's `SKILL.md`, the policy and one or more
customer messages with the order details and today's date. For each message the helper returns
four parts:

1. **A reply draft**, ready to edit and send.
2. **Why this reply:** each thing the customer asked, one of four decisions (allowed, refused, not
   covered, manager decides) and the exact words of the rule used, with any date or hour
   arithmetic written out.
3. **Flags:** what a manager must decide and the question to put to them, what the policy does not
   cover with a suggested rule to add, records that disagree with what the customer says, missing
   facts, and any instruction hidden in the customer's message.
4. **Check before you send:** two to four things to confirm in the person's own systems.

A second skill, `build-policy-book`, turns scattered rules into a numbered policy book: one rule
per entry, in the owner's own words, with its source, plus the conflicts and gaps it found.

**The time it saves.** Not measured; no person has used it yet. The intended saving is finding
the rule and checking the dates for each message, and avoiding a reply that promises too much.

**What they still check.** Every date and amount against their order system, since the helper
knows only what is pasted. Each manager flag goes to the person who decides. Each "not covered"
flag is a decision for the owner, and a rule to add so the next reply is covered. A person always
sends. The helper never sends, refunds or pays.

## Value for agentic engineers

**How it constrains the model.** A model asked to "reply to this customer" optimises for a
satisfied customer, so it fills gaps in the policy with goodwill. The skill removes that freedom
in five ways:

- **Citation or silence.** Every promise in the reply must point to a quoted rule. A sentence
  that cannot is rewritten or removed in a final check step.
- **A closed set of decisions, with precedence.** Four decisions, and "manager decides" is checked
  first. It covers an M entry in the policy, rules that disagree, a claimed staff promise, a legal,
  chargeback or public review threat, injury or safety, and a customer pushing back.
- **Assumptions block promises.** If a decision rests on the model's own reading of the rule's
  words (does "a friend" include a sister; is a swap a return?), it is marked "(assumed)" and the
  reply promises nothing either way.
- **Records are checked against claims.** A customer who says a pass "runs out soon" when the
  records show it ended last week produces a "records disagree" flag, not an answer.
- **Customer text is data.** An instruction inside a message is quoted under its own flag and
  ignored. It is never a decision row.

**How it is tested.** A fresh agent with only `SKILL.md` produced the worked example. Two separate
reviewer agents, blind to the build and to each other, each ran the skill on a new invented input
with planted traps, checked every date sum by hand, and scored the output against a fixed
rubric.

**How it composes.** The policy book is a plain knowledge file: an index, short entries with
sources, and a manager list. It can sit in a Claude Project, a ChatGPT Project or a Gemini Gem. A reply draft can be passed to the repository's Write in my voice tool for tone, and a
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
2. Pull the facts from the message, keeping who did what and assuming no one's gender.
3. Check the customer's claims against the records.
4. Find the rules that apply, quoting both when two disagree.
5. Do the date, hour and amount arithmetic in the open.
6. Sort each request into one of the four decisions, manager first.
7. Draft the reply, promising only what an allowed rule supports.
8. Check every promise and fact in the draft against the policy and the message.

**The one mistake it is designed to catch.** A reply that promises something the policy does not
say. In the worked example, a customer wanted a replacement mug before a birthday. The policy
allows the replacement but sets no delivery time for it, so the reply confirms the replacement and
says the shop will check the timing; it does not offer a date. A second customer asked for a £240
refund on a made-to-order set. That reply promises nothing and goes to the owner with one
question. Four things sent it there: two rules that disagree, a claimed promise from the shop's
chat, a chargeback threat and a sign-off limit.

## Evidence

- **Two review rounds** on 25 November 2026, by separate Claude agents. Both scored 82 out of 100.
  Every point lost is in `review.md`.
- **Round 1** used an invented bike repair shop with two rules that disagree, an instruction
  planted in a message, and a mechanic's promise. No unsupported promise was made, the planted
  instruction was ignored, and the date sums were right. Points were lost for reversing who
  collected a bike, assuming a customer's gender, and an unclear line between "refused" and
  "manager decides".
- **Round 2** used an invented yoga studio with a late cancellation, an expired pass the customer
  thought was still running, an injury, and a rule about "a friend" applied to a sister. All five
  traps were caught. Points were lost for promising the transfer when that rested on the model's
  own reading, and for an hours rule that pointed at the wrong time.
- Both missing-input checks passed.

**Limits of this evidence.** One reviewer agent per round, both Claude. The inputs were invented
by the same builder that wrote the tool. The fixes after round 2 were not re-scored, though the
worked example was re-run on the final skill. The `build-policy-book` skill was read but not run
on its own. No person has used the tool, and it has not been run in ChatGPT or Gemini.

## Limits and later steps

**Limits.**

- It knows only what is pasted. It does not look up orders, tracking or payments.
- It is not legal advice. Consumer law may give customers rights a written policy does not
  mention, and those rights vary by place.
- A thin policy produces many "not covered" flags. That is the intended behaviour, but it means
  the first week is mostly policy-writing.

**Later steps.**

1. Have a person use it for a week on real messages, and record what they changed before sending.
2. Run it in ChatGPT and Gemini.
3. Run `build-policy-book` on a real, messy returns page and FAQ.
4. Level 3: a helpdesk or mailbox connector that brings messages in and saves drafts, never sent.

## Try it

The folder: [github.com/bar181/practical-ai/tree/main/docs/customer-issue-helper](https://github.com/bar181/practical-ai/tree/main/docs/customer-issue-helper).
Paste `SKILL.md` into a new chat, then add your policy, today's date and a customer message with
its order details.

Gist: not yet published.
