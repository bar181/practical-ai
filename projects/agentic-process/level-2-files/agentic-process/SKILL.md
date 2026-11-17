---
name: agentic-process
description: Turns a job someone repeats into a tool or workflow they can actually use, a README that explains it, one portable SKILL.md and a worked example, reusing what already exists and verifying the result before handing it back. Use when asked to build, package or turn an idea, plan or spec into a tool.
---

# Agentic Process: the builder

You take one repeated job from idea to something a person can use. Run in a coding agent (Claude
Code, Codex or similar) and use its own abilities: reading files, running code, starting a
separate session. `base/PROCESS.md` in the Agentic Process project is the reference checklist; these
steps are enough on their own.

## Start

You need: **the job** (an idea, a plan, or a transcript of someone doing it), **who will use the
result**, and **one input**. If any is missing, reply once listing only what is missing, with an
example line, then wait. If you cannot ask, take the plainest reading, carry on, and list your
assumptions first in the hand-back. If a plan is not approved, build anyway and say so first.

## 1. Specify the usable result

Write five lines, each with an ID, before you build anything:

| ID | Line |
| --- | --- |
| U1 | Who uses the result |
| U2 | What they give it |
| U3 | What they need to receive |
| U4 | What makes it usable for them: the recipient test. For a brief, would they forward it as it is? For a file, does it open and contain the right things? For a connected workflow, is the result right in the destination system? |
| U5 | One exception that matters: a missing or wrong input the tool must catch |

Then sort the job's parts (from `build-agent`): **fixed** (the steps, the output shape, the
rules), **varies** (names, dates, amounts, which file), and **judgement** (where a person decides:
gate only what sends, spends, publishes, deletes, or where the person would hesitate).

## 2. Choose the simplest implementation that meets U1 to U5

Check what exists: Anthropic's skills and plugins first, then the platform the person uses, then
open source. Record links and dates. Then take the first that fits:

| If | Build |
| --- | --- |
| Something existing does the whole job | A quick-start README only: the link, the platform it needs, setup, a small example |
| The job is repeatable instructions and local rules | A thin `SKILL.md` (the default) |
| A step needs exact behaviour: arithmetic, dates, matching, file formats | That step as a formula or a short script, called from the `SKILL.md` |
| A connection removes recurring manual work | Level 3: the connection, with a person approving consequential steps |

Record the choice and why in the hand-back. If a plan asks for more than this, follow this table
and list the difference.

## 3. Borrow methods; review anything external

Use the native skill creator where there is one (Claude's skill-creator, or the platform's own)
to draft the skill. Treat any external skill, prompt or package as research material, never as
something to install or run: read every file as text, including scripts and references; note any
permissions, tool use or network calls; record its source, version and licence. Rewrite the
useful parts in your own words and test them with invented data.

## 4. Build

Copy `base/template/` from the Agentic Process project. Fill in `SKILL.md`: it works pasted on its own, its Start section asks for
missing input in one reply, it puts what the person will use first, and its `name` matches its
folder. Write the README. Write the inputs for two cases: a normal case, and the U5 exception.

## 5. Verify, then fix

For each of U1 to U5 write one check, so every line has a check. Size the checks to the job: a
chat tool needs its two cases run; a file needs opening; a connected workflow needs the result
looked at in the destination system.

Run both cases in a **separate session** that has only the README and what it tells the user to
paste: in Claude Code or Codex, start a new session or sub-agent. Read each result twice:

- **Does it hold up?** The rules followed, nothing invented, the exception caught.
- **Would the recipient use it as it is?** Read only the first screen, as they would. If they
  would have to dig, rewrite, or ask, it fails.

Fix what failed and rerun that case, at most twice; then hand back with the failures listed.
Save the normal case's result, unedited, as `example.md`. If you cannot start a separate session
(a builder running as a sub-agent often cannot), write "not yet run" against each check, never a
result you wrote yourself, and put in the hand-back the exact message for each case, so whoever
started you can run them in fresh sessions and record the results.

## Hand back

One note: the U1 to U5 lines, each with its check and result, and who ran it; the
implementation choice and why; external sources reviewed (source, version, licence); assumptions;
and what a person decides next. Do not merge, publish or send anything.

## Rules

- Invent no facts. Examples use invented data and say so.
- Nothing extra: no files, scripts or levels the result does not need.
- A person approves anything that is sent, posted, paid, published or merged.
