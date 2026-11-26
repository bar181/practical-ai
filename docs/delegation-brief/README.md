# Delegation brief

Paste a rough request ("can you sort out the supplier sheet before Friday") and get a one-page
brief that a colleague, a contractor or an AI agent can finish without coming back with questions;
when the work comes back, check it line by line against that brief.

**Status.** Draft, built and reviewed by AI on 26 November 2026; not yet tried by a person. Two
separate Claude reviewer agents ran it on new invented inputs and scored it 83 and 85 out of 100
([review](review.md)); the fixes after the second round have not been re-scored. A Claude agent ran
the final skills to make the worked example. Tried only in Claude so far.

![A rough request goes in; out come questions for you, a brief with yes-or-no "done when" checks, and later a line-by-line check of the work that came back](how-it-works.svg)

## The idea in one picture

**Think of it as** the work order a good builder writes before a job: what will be true when it is
finished, what not to touch, and who to call before knocking down a wall. When the job is done,
you walk round with the same sheet and tick each line, rather than taking "all done!" on trust.

The tool writes that sheet for you from the way you actually ask for things, and refuses to fill
gaps by guessing. Every gap becomes a question for you.

## Who it is for

- **Business people:** anyone who hands work to someone else: an owner briefing an assistant, a
  manager briefing a contractor or agency, a team lead sharing out tasks after a meeting.
- **Agentic developers:** anyone briefing Claude Code, Codex or a Cowork task. The brief adds an
  agent section (where it may work, how to prove each line, what to stop and ask about), and the
  hand-back check treats "all tests pass" as a claim until it sees the output.

## Try it: paste one file (5 minutes)

1. Open [`SKILL.md`](SKILL.md), press **Raw**, and copy all of it.
2. In Claude, ChatGPT or Gemini, start a new chat and paste it.
3. On a new line, write the task the way you would say it, who will do it, and how you will know
   it is done. A forwarded email or a line from meeting notes is fine.
4. Answer its questions, then copy the brief and the short message it drafts.
5. When the work comes back, start a new chat with [`check-handback/SKILL.md`](check-handback/SKILL.md),
   the brief and what came back: the result itself, not only "done".

## What you get

**From the brief writer:**

1. **Questions for you before you send**, at most six, each with why it matters ("Can Priya delete
   rows, or only mark them? Deleting cannot be undone.").
2. **The brief**: outcome in one sentence, why it matters, "done when" checks that someone who did
   not do the work can answer yes or no, what they have, what they must not do, what is out of
   scope, what they decide and what they ask about, and who to ask when stuck. For an AI agent, an
   extra section.
3. **The message to send**, two to four sentences to paste above the brief.
4. **What I added or assumed**: every **(suggested)** item, so you can accept or remove it.

**From the hand-back check:**

1. **A verdict**: ready to accept, not yet, or stop (something it must not do was done).
2. **Each "done when" line** as met, not met or can't tell, with the quoted evidence.
3. **Anything outside the brief**: things changed, deleted, sent or decided that the brief did not
   allow.
4. **A reply to send**, specific about what is still needed.

[See the worked example](example.md): an invented bakery owner hands a supplier price list to a
part-time assistant. The brief asks six questions first; the hand-back check finds that three
"must not" lines were broken behind an "all done!".

## The files

| File | What it is for |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Step 1: turns a rough request into a brief, with questions for you first |
| [`check-handback/SKILL.md`](check-handback/SKILL.md) | Step 2: checks the work that comes back against the brief, line by line, with evidence |
| [`brief-template.md`](brief-template.md) | The brief's shape, the agent section, and a "done when" test with examples, to fill by hand or save in a project |
| [`example.md`](example.md) | One worked example, invented data |
| [`review.md`](review.md) | The AI review: scores and every point lost |
| [`paper.md`](paper.md) | A short technical paper on the tool |

## Levels

| Level | What it is | When it earns its place |
| --- | --- | --- |
| 1 | Paste `SKILL.md` and your request into any chatbot; later paste `check-handback/SKILL.md` with the brief and the result | Always; start here |
| 2 | Save both skills and the template in a Claude Project, ChatGPT Project or Gemini Gem, or install them as skills in Claude Code. Add a short note of your usual "must not" lines (for example "never email suppliers") so every brief starts with them | When you hand off work most weeks and are tired of pasting |
| 3 | Not built. A task board or repository connection could turn an approved brief into a ticket or an agent task, and bring the hand-back in for checking. A person still approves each brief and each acceptance | Only if copying briefs and results in and out becomes the slow part |

## Check before you send

- Every question it asked is answered, or you have decided to leave it open.
- Every **(suggested)** item is accepted, changed or removed. A suggestion you leave in becomes a
  requirement for the doer.
- The doer actually has the files and access listed under "You have".
- For the hand-back: open the real result for anything marked "Can't tell".

## What it does not do

- It does not send, assign or start anything. You send the brief; you accept the work.
- It does not know your business, your files or your people. It works only from what you paste.
- It does not decide what the task should be. If your request holds two outcomes, it offers two
  briefs.
- It does not judge quality beyond the brief. "Met" means the line was met, not that the work is
  good in every way. To score quality, use the [Rubric reviewer](../../projects/rubric-reviewer/).
- It does not open files or run commands. The hand-back check sees only what you paste; a claim
  with no result behind it is marked "Can't tell".

## How it was checked

| ID | Spec line | Check | Result, who ran it, what they saw |
| --- | --- | --- | --- |
| U1 | A person handing one task to a colleague, contractor or AI agent | An invented bakery (example), a software team briefing a coding agent and a design studio briefing a freelancer (reviews) | Claude agents, 26 Nov 2026: all three ran |
| U2 | The task in their words, who does it, how they will know it is done | Missing input: asks once for only what is missing, and waits | Passed in both review rounds. Round 1 found the example in the question did not fit the task; fixed |
| U3 | A one-page brief with checkable "done when" lines, and a hand-back check | The normal case | [Worked example](example.md), fresh agent, unedited |
| U4 | The doer can start without coming back; the person can accept or reject on evidence | Reviewer agents scored the result | 83 and 85; see [review](review.md). Not yet judged by a person |
| U5 | A brief that adds a requirement, deadline or permission nobody gave, or a hand-back accepted on the doer's word | Planted traps: "the usual way", "ASAP", "push to main", "book and pay on the company card", hand-backs that claim "all done" while breaking a "must not" | No brief made push, book, pay or send a task step; all three hand-back checks said "Stop". Round 1 found a suggestion that lost its mark after bulk acceptance; fixed |
| | Works in other chatbots | The same files in ChatGPT or Gemini | Not yet run |
