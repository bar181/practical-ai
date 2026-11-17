# Agentic Process: turn a job you repeat into a tool someone can use

**For people who build tools or workflows with a coding agent** such as Claude Code or Codex. Give
it a job you repeat. It hands back a small package someone can start in five minutes, and it tests
the package in a fresh session before you get it.

<p align="center">
  <img src="_build/img/builder-flow.svg" width="480" alt="Animation of the builder. A job you repeat goes in at the top. Four steps light up in turn: name the usable result, pick the simplest build, build one SKILL.md, and test it in a fresh session, with a loop back to fix. At the bottom, the package you get: README.md, SKILL.md and example.md, checked before you get it.">
</p>

**The picture, in words:** you describe a job. The builder writes down who will use the result
and the one catch it must spot, reuses anything that already does the job, builds one instruction
file, then runs it in a fresh session on a normal case and on the catch. It fixes what fails and
hands back three files: a README, a `SKILL.md` that works in any chatbot, and a worked example.

<p align="center"><a href="#try-it-build-a-tool-in-about-10-minutes"><b>Build your first tool in about 10 minutes</b></a></p>

## Try it: build a tool in about 10 minutes

You need a coding agent: Claude Code, Codex or similar. Open it in an empty folder, and paste
this. The job in it is an example; swap in your own later. The build takes about 5 minutes.

**Then the tests, about 5 minutes more.** The builder tests the tool in fresh sessions when it can
start them, which works when you run it as your main agent. If it cannot, it says "not yet run"
and hands you three short messages: paste each into a fresh chat and read what comes back. Until
then the tool is built, not ready.

```
Read the builder skill at
https://raw.githubusercontent.com/bar181/practical-ai/main/projects/agentic-process/level-2-files/agentic-process/SKILL.md
and follow it.

The job: when a supplier sends a notice
that changes our terms, work out what it
makes us do and by when.
Who uses the result: a café owner,
in the chatbot they already use.
Example input: write an invented
one-page supplier notice.
The catch: a notice that leaves out a date
or an attachment it mentions.

Put the tool in document-to-action-brief/.
Hand back what you built, the checks
you ran, and what you assumed.
```

**Your agent cannot open the link?** Download this repository, open the agent in its folder, and
replace the first three lines with: `Follow projects/agentic-process/level-2-files/agentic-process/SKILL.md`.

### What you get

A folder of three or four files. The one the builder made for this job in our pilot, from the
job's written plan rather than this exact request:
[`document-to-action-brief/`](quality-results/2026-11-16-builder-pilot/agentic-process/document-to-action-brief/).

| File | What it is |
| --- | --- |
| `README.md` | How to use the tool: a five-minute start, what to give it, what to check |
| `SKILL.md` | The tool: paste it into any chatbot with a notice |
| `example.md` | A worked example, and practice notices to try it on |

Here is that tool at work. A fresh chat had only its `SKILL.md` and a notice it had never seen:

<p align="center">
  <img src="_build/img/pilot-brief.webp" width="720" alt="Screen capture of a chat reply from the tool built with Agentic Process. It names the document, sums up that the notice asks for four things with the earliest deadline 15 December 2026, then a warning that three things are missing: the Effective Date is never stated, the Account Update Form was not attached, and the overdue charge is marked with an asterisk that points to nothing. Below it, a table of what you must do, each row with the exact words from the notice and where they are.">
</p>

**The capture, in words:** the reply opens with a short summary and a warning that the notice
never gives its Effective Date and leaves out the form it says is attached. Then come tables of
what you must do, the dates and the open questions, each line with the exact words and where they
are, and a column to tick each one against the page. [The whole reply](quality-results/2026-11-16-builder-pilot/runs/agentic-process-result.md).

### The evidence

**In one blind pilot, a tool built with Agentic Process scored 93/100. The direct-build version
scored 73/100 on the same brief.**

Both versions found all nine key items in an unseen supplier notice. The Agentic Process version
put the missing effective date and the missing form at the top, said who to ask, and needed zero
corrections before the owner could act. The direct-build version needed two: it filed the form as
a fact rather than something to do, and it never said who to ask about the date.

**The scope:** one build task, one unseen notice and one blind reviewer. A signal, not a study.
[The pilot and what it changed](quality-results/README.md) ·
[the raw review](quality-results/2026-11-16-builder-pilot/runs/BLIND-REVIEW.md).

## Use it with your own job

Keep the first three lines of the request. Replace the rest with four answers:

1. **The job:** what you do by hand, every week or month. *"Turn a client's meeting notes into
   actions with owners and dates."*
2. **Who uses the result,** and where. *"Me, in ChatGPT."*
3. **An example input:** a real one with private details removed, or ask for an invented one.
4. **The catch:** what goes wrong when people do it by hand. *"Notes that never say who owns an
   action."* The builder tests for it.

The builder asks once if something is missing, then gets on with it.

## Is it ready?

Open the hand-back and the new folder. It is ready when:

- [ ] **Every line of the spec has a check that ran.** The hand-back lists U1 to U5 (who uses it,
  what they give it, what they need, what makes it usable, the catch), each with a result.
- [ ] **The checks ran in a separate session,** and the hand-back says who ran them. "Not yet run"
  means not ready: paste the messages from the hand-back into a fresh chat yourself.
- [ ] **`example.md` is a real result,** unedited, not something the builder wrote.
- [ ] **The catch was caught** in its own test case.
- [ ] **Read only the first screen of a result,** as the person who will use it. Could they act on
  it as it is? If they would have to dig, rewrite or ask, send it back.

## Without a coding agent

Copy [`base/template/`](base/template/) and follow [the one-page process](base/PROCESS.md) with
any chatbot: write the five spec lines, fill in the `SKILL.md`, then test it in a new chat.

## What is inside

| Part | What it is |
| --- | --- |
| [`base/PROCESS.md`](base/PROCESS.md) | The method on one page: the spec, the build choices, the nine steps as a checklist, and how to verify |
| [`base/template/`](base/template/) | The three files every tool starts from |
| [`base/examples/`](base/examples/) | Two tools built this way: [decision support](base/examples/decision-support/) and a [learning log](base/examples/learning-log/) |
| [`level-2-files/agentic-process/`](level-2-files/agentic-process/) | The builder skill. Install it in your coding agent to skip pasting the link |
| [`quality-results/`](quality-results/) | What each test showed, and what it changed in the builder |
| [`_build/`](_build/) | The spec and the script that makes the screen capture. You do not need it |

**Levels.** Beginner: paste the build request above. Advanced: install the builder skill so you
just say "build a tool for this job". There is no Expert level yet: no connected workflow has been
built with it.

**North Star:** someone describes a job they repeat, and gets back a tool another person can start
in five minutes and trust, checked before it is handed over.

## Status

**16 November 2026.** Built by its author with Claude. The builder has made two tools on its own: the
learning log, which passed three fresh-session checks, and the pilot's document-to-action brief,
run once on an unseen notice and reviewed blind. Decision support was converted by hand. The checks
were started from outside the builder, because a builder running inside another agent could not
start sessions of its own. Not yet tried in Codex or any other coding agent, and nobody
but its author has used it. The pilot above is its only head-to-head comparison.

Part of [Practical AI](../../README.md). By [Bradley Ross](https://www.linkedin.com/in/bradaross/).
