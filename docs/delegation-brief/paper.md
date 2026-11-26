# Delegation brief: hand off a task once, and check it on evidence

A two-skill tool that turns a rough request into a one-page brief a colleague, a contractor or an
AI agent can finish without coming back, then checks the returned work against that brief line by
line.

![How it works: a rough request becomes a brief with yes-or-no checks; the hand-back is checked line by line](how-it-works.svg)

## North Star

A person who hands off a task gets work back that meets every "done when" line on the first
attempt, and can tell in under five minutes, from evidence rather than the doer's word, whether it
does.

## Value for business people

**The job.** Handing work to someone else is one of the most repeated jobs in any office: an owner
asks an assistant to tidy a price list, a team lead shares out actions after a meeting. Most
hand-offs are one or two sentences long: "can you sort out the supplier sheet before Friday?" The
person asking knows what they mean. The doer has to guess, and the guesses are where time goes.
"Sort out" means deleting rows to one person and marking them to another. "Do it the usual way"
means nothing to a new contractor.

**What the tool does.** Step 1 reads the request and asks the person the questions the doer would
otherwise ask later, at most six, most important first, each with a suggested answer where one is
sensible. Then it writes the brief: the outcome in one sentence, two to six "done when" lines that
someone who did not do the work can answer yes or no, what the doer has, what they must not do,
what is out of scope, which decisions they may make alone, and who to ask when stuck. It drafts a
short message to paste above the brief. Every addition it makes is marked "(suggested)".

Step 2 runs when the work comes back. It takes the brief and the result, and gives each "done when"
line one verdict: met, not met or can't tell, with the quoted evidence. It lists anything the doer
did that the brief did not allow, does any sums and date checks, and drafts a specific reply.

**The time it saves.** Not yet measured; no person has used it. By design it removes the second
round: the doer's questions after the brief is sent, and the rework after the work comes back.

**What they still check.** The questions and the suggestions before sending, since a suggestion
left in becomes a requirement. That the doer actually has the access listed. And, after the
hand-back, anything marked "can't tell", by opening the real result.

## Value for agentic engineers

The same two steps are the loop of agentic coding: write the task, let the agent work, check what
it hands back. The tool constrains both ends.

**The brief constrains the agent.** For an AI doer the brief adds a short section: where the agent
may work, the command or check that proves each "done when" line, and a fixed stop-list. The agent
must stop and ask before deleting, sending, posting, paying, publishing, merging, pushing to a
shared branch, deploying, releasing or changing a test, whatever the request says. If the request
itself asks for one of these ("bump the version and push to main"), the brief writer never turns it
into a task step. It asks the person and offers the safer form: "open a pull request and do not
merge it".

**The check constrains the reviewer.** The hand-back skill treats the agent's own words as claims.
"All tests pass" is a claim until the test output is pasted. The agent's own list of changed files
is a claim until the diff or the tool's file list is seen. A test the agent changed weakens every
line that rests on tests passing. A line in the brief that cannot be answered yes or no is marked
"can't tell: the line is not checkable", which pushes the fix back into the brief, not into a
judgement call.

**How it is tested.** Both skills are plain instructions in the open Agent Skills format, so they
can be run by any chatbot or coding agent and scored by a separate one. This draft was reviewed by
separate Claude agents that ran it on new invented inputs with planted traps and scored the result
against a rubric fixed in advance.

**How it composes.** Meeting notes to actions produces tasks; each can become a brief. The "done
when" lines are pass or fail; when work also needs a quality score, the Rubric reviewer scores it.
A lesson from a hand-back that went wrong belongs in the Learnings database and can become a
standing "must not" in the next brief.

## How it works

**The files.** `SKILL.md` writes the brief. `check-handback/SKILL.md` checks the result.
`brief-template.md` holds the brief's shape, the agent section and a short "done when" test with
examples of lines that fail and pass. `example.md` is one worked example with invented data.

**The steps.** The brief writer pulls every fact out of the request and keeps it exactly as
written. It writes the outcome, turns "done" into one-check-per-line tests, separates what the
person said from what it suggests, names the edges, lists what the doer needs, adds the agent
section where needed, and checks the brief against the request: every fact kept, nothing new
unmarked, every vague word ("usual", "ASAP", "best", "walkable") defined or asked about.

The hand-back check lists the brief's checks, finds the evidence for each in what came back, gives
one verdict per line, compares the result with the brief's "must not", "out of scope" and "ask
first" lines, does the arithmetic and the calendar itself, and drafts the reply. If money was
spent or a commitment made, it says how much, to whom and the last date it can be undone, and puts
that first.

**The one mistake it is designed to catch.** A brief that quietly adds a requirement, a deadline or
a permission nobody gave, and its mirror image: a hand-back accepted on the doer's word. The first
is caught by the "(suggested)" mark and the questions list. The second is caught by the rule that
a claim is not evidence.

## Evidence

- **Two review rounds** on 26 November 2026, each by a separate Claude agent that had not seen the
  tool being built or any earlier review. Rubric, fixed in advance: does the job (30), keeps every
  fact (25), plain English (15), clear limits (15), safe (15).
- **Round 1: 83 of 100.** An invented software team briefing a coding agent on a slow export, with
  "ASAP", "work like the PDF export", a folder it must not touch, and "push to main". The hand-back
  claimed "all tests pass" with no output and had changed a file in the forbidden folder. The check
  said "Stop" and named the file.
- **Round 2: 85 of 100.** An invented design studio briefing a freelance assistant on a team
  offsite, with "book whatever looks best and put the deposit on the company card". The hand-back
  had already paid a deposit. The check said "Stop", worked out the VAT, and caught a weekday that
  did not match its date.
- **Points lost** were mostly in the skill text: a stop-list that did not name pushing to main,
  and "done when" lines that packed three checks into one. Each was fixed; all are in `review.md`.
- **The worked example** was re-run on the final skills. It found three broken "must not" lines
  behind an "all done!".

**The limits of this evidence.** One reviewer agent per round, the same model family as the
builder. Inputs invented by the builder. The fixes after round 2 have not been re-scored. The
example was re-run by an agent that had seen an earlier version's replies. No person has used the
tool, and it has not been run in ChatGPT or Gemini.

## Limits and later steps

- It knows only what is pasted. It cannot open the shared drive, the repository or the booking
  site, so "can't tell" will be common until the real result is pasted.
- "Met" means the line was met, not that the work is good. A quality score needs a rubric.
- A brief is only as good as the answers to its questions. If the person skips them, the brief says
  so but cannot fill the gap.
- Later steps: try it with people on real hand-offs; run it in ChatGPT and Gemini; and, only if
  copying becomes the slow part, a Level 3 connection that turns an approved brief into a ticket or
  agent task, with a person approving each step.

## Try it

The folder: [github.com/bar181/practical-ai/tree/main/docs/delegation-brief](https://github.com/bar181/practical-ai/tree/main/docs/delegation-brief).
Paste `SKILL.md` into a new chat, then your task, who will do it, and how you will know it is done.

Gist: not yet published.
