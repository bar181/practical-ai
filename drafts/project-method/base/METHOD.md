# The method

Nine stages. Each ends at a gate. A gate is either a command that must succeed or a person who
must say yes. Do not start a stage until the gate before it has passed.

**Think of it as** a relay. Each runner carries one thing and hands it over cleanly. Nobody runs two
legs at once, and three of the handovers are to a person.

| Stage | In one word | You produce | The gate |
| --- | --- | --- | --- |
| 1 | **Understand** | Who it is for, the one job, a North Star | The page reads true to the person who asked |
| 2 | **Research** | What already exists, with dated sources | Every source dated. Build, use or build on top: decided |
| 3 | **Scope** | In, out, the levels, and a "done when" line for each item | **A person approves the North Star page. Stop** |
| 4 | **Plan** | The folder, both front doors, the gates and the rubric, before any content | The layout check passes |
| 5 | **Prove** | One real request taken to one finished output | **A person says it is what they wanted. Stop** |
| 6 | **Build** | One source file, generated copies, then breadth | The build and the link check pass |
| 7 | **Verify** | Worked examples, a scripted agent, every request run | The example and agent gates pass |
| 8 | **Score** | A self-review out of 100 on the rubric written at stage 4 | Scored, with "evidence from real use" as one line |
| 9 | **Close** | Clean-up, lessons logged, status final, a short report | Every gate passes. **A person closes it. Stop** |

## Contents

- Where this comes from
- How much method a tool needs
- Stage 1: Understand
- Stage 2: Research
- Stage 3: Scope
- Stage 4: Plan
- Stage 5: Prove
- Stage 6: Build
- Stage 7: Verify
- Stage 8: Score
- Stage 9: Close
- Working across sessions
- The levels of a tool
- When the direction changes

## Where this comes from

Two sources. The first is our own build: the artifact studio was rebuilt three times, and each
wrong turn is a row in [`LESSONS.md`](LESSONS.md). The second is what people who build with agents
have converged on, read on 15 November 2026 and listed with links in
[`SOURCES.md`](SOURCES.md).

| What others do | Where it shows up here |
| --- | --- |
| Explore before planning, and plan before changing anything | Stages 1 to 4 come before any content |
| Write the specification, the plan and the tasks as separate files, each feeding the next, with a person checking at each boundary | The North Star page, then the plan, then the gates. Three stops for a person |
| Give the agent a check it can run, and never accept "looks done" | Every stage ends at a gate. `gates.json` is written at stage 4, before the work it checks |
| Keep progress in files, not in the agent's memory: a list of what must be true, a progress note, the history | `gates.json`, `docs/progress.md` and git |
| Do one thing in a session, verify it, record it, stop | One stage at a sitting |
| Verify with fresh evidence and, where possible, a fresh reviewer | Stage 7 plays the user and the agent. Stage 8 scores |
| Match the ceremony to the size of the job | "How much method a tool needs", below |

## How much method a tool needs

| Size | Example | What you may shorten |
| --- | --- | --- |
| Small | One skill, one template, one script | Stages 1 to 3 fit in ten lines. Stage 7 is two examples |
| Medium | A tool with a base and level 1 | Nothing. This is what the method is written for |
| Large | A tool with a store, connections or several outputs | Split it. Build the base as a medium tool first, and each level as its own pass from stage 3 |

A gate is never skipped at any size.

## Stage 1: Understand

Fill in the top of [`docs/north-star.md`](scaffold/docs/north-star.md). Nothing else yet.

| On the page | Example |
| --- | --- |
| Who it is for, as a user story | "As a consultant I want to deliver a presentation from my notes" |
| The one job | Turn notes into something worth sending |
| An analogy | "Ordering at a counter" |
| A North Star | One sentence that says what success is, for a person, in plain words |
| What the finished thing is | A product someone uses, a guide someone follows, or a demo someone watches. Pick one |

Ask the person who wants it. At most five questions, one at a time. Read what they have already
written before you ask anything.

**Gate:** the person reads the top of the page and says it is true.

Why first: the most expensive change is a change of purpose. It is cheap on one page.

## Stage 2: Research

Find what already exists before deciding what to build: features built into assistants,
open-source projects, paid services, and how people who do this well do it. Use the
[`landscape-review`](../../../skills/landscape-review/) skill. Write the three to six strongest
influences into the North Star page, each with a link, the date you checked it and the one thing
you take from it.

**Gate:** every source carries a date, and one line records the decision: build, use something that
exists, or build on top of it.

## Stage 3: Scope

Finish the North Star page.

1. **In and out.** What the tool does, and three things it will not do.
2. **The levels.** What the base holds, and what each level adds. Level 1 in a few sentences. Later
   levels in one line each.
3. **Done when.** One line for each thing in scope that says how anyone can tell it is finished.
   "The picker works" is not a line. "The picker gives the same answer in the page and in the
   server for every request" is.
4. **Where the data lives.** If the tool stores anything, say where. Nothing private goes in the
   repository.

The page is one to three pages long. If it is longer, the tool is too big: split it.

**Gate:** a person approves the whole North Star page. **Stop here and wait.**

## Stage 4: Plan

Make the folder before the content. Run `new_project.py`. Then write four things:

1. `README.md`: the front door for people, from the North Star page.
2. `AGENTS.md`: the front door for agents. The path from a request to a result, in numbered steps.
3. `gates.json`: one gate for each "done when" line. They may fail today.
4. `docs/rubric.md`: the six to eight lines the finished tool will be scored on at stage 8. One of
   them is "evidence from real use".

**Gate:** `python3 tools/check_project.py drafts/<tool>` passes.

Why now: gates and a rubric written before the work cannot be bent to fit it.

## Stage 5: Prove

Take one real request all the way to one finished output, by the shortest route. No options, no
variations, no second example.

**Gate:** a person looks at the output and says "this is what I wanted". **Stop here and wait.**
If they say anything else, including "nearly", go back to stage 1 with what you learned. That is
the method working, not failing.

## Stage 6: Build

Now widen, in this order.

1. Put the tool's facts in one file: the list of things it offers and the rules for choosing
   between them.
2. Generate everything that repeats those facts: indexes, counts in documents, reference sheets.
   A person edits the source. A script writes the rest.
3. Add content, one piece at a time, running the gates after each.

**Gate:** the build runs, the link check passes, and where a rule exists in two places a test
proves they agree.

## Stage 7: Verify

The author is the worst tester, because the author knows where everything is. So pretend not to.

1. **Worked examples.** Several requests as a person would type them, with the notes they would
   attach, and the finished output. Mark anything the notes did not say as missing.
2. **A scripted agent.** A script that reaches the tool only through what an outside agent can
   reach, and has to finish a file.
3. **Every request.** If the tool chooses, run every possible request through it and look at the
   worst answers.

**Gate:** the example and agent gates pass, and the worst answers are either fixed or the tool says
plainly that the fit is weak.

## Stage 8: Score

Score the tool out of 100 on the rubric written at stage 4. Do not rewrite the rubric now.

1. One score for each line, with one sentence of evidence: a gate that passed, a file, a number.
2. A line with no evidence scores 40 or less.
3. Where you can, have the scoring done by a reviewer who has not seen the work being made.
4. List what the checks found and what was fixed.

**Gate:** the review is written into `docs/` with every line scored, and "evidence from real use"
is one of the lines.

## Stage 9: Close

Closing is cleaning up so the next person, or the next session, finds only what is true.

| Check | How |
| --- | --- |
| Every gate passes | `python3 tools/gates.py drafts/<tool> --all` |
| Nothing stale | Front doors, status table and counts match what is there |
| Nothing left over | Retired work is in [`plans/archive/`](../../../plans/archive/) with a line saying what replaced it. Scratch files are gone |
| Lessons kept | Anything that went wrong, was redone, or worked unexpectedly well is a row in [`LESSONS.md`](LESSONS.md), and in the learnings database once it exists |
| The list is current | The tool's row in [`docs/tool-inventory.md`](../../../docs/tool-inventory.md) shows its state |
| Handed over | A short report: what it is, how to use it, what nobody has tried, the decisions still open |

**Gate:** all of the above, and a person says close. **Stop here.**

Closed is not the same as used. A tool is **closed as a draft** when it is built and checked by
its author. It moves to `projects/` when one other person has used it for a real job.

## Working across sessions

An agent starts each session knowing nothing of the last one. Three files carry the work across.

| File | Holds | Read |
| --- | --- | --- |
| `gates.json` | What must be true for the tool to be done | First. Run it |
| `docs/progress.md` | What was done, what is in progress, what is next, what to be careful of | Second |
| The git history | What changed and why | When the other two are not enough |

Start a session by running the gates and reading the progress note. End it by updating the note
and committing. Do one stage, or one piece of stage 6, in a session.

## The levels of a tool

Every tool has a base and up to three levels.

| | Called | For | Holds | A person depends on |
| --- | --- | --- | --- | --- |
| `base/` | Base | Everyone | Everything: the thing itself, its examples, its source | Nothing but a browser or a reader |
| `level-1/` | Beginner | Students and business owners | Only instructions: for the assistant, and for the person using it. Nothing to install | Any chat assistant |
| `level-2/` | Advanced | Someone who builds with agents | Only what makes it repeatable or agentic: a skill, connectors, a preferences file, gates | An assistant that runs skills and connectors |
| `level-3/` | Expert | The owner's own setup | Only what needs another system: a database, an MCP server, a plugin, a schedule | Other systems |

The Beginner level is the test of the tool. If a student cannot run it in a chat assistant in
under an hour, the tool is not ready for an Advanced level.

A level never copies the base. If you find yourself copying, the thing belongs in the base.

## When the direction changes

It will. When it does:

1. Rewrite the North Star page first, and get it approved.
2. Run the link check before and after moving anything. It is the net under the move.
3. Move retired work to [`plans/archive/`](../../../plans/archive/) with a line saying what replaced
   it. Do not delete it, and do not leave it where a newcomer will mistake it for current.
4. Update the status table the same day.
