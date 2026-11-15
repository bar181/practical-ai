# The method

Seven stages. Each ends at a gate. A gate is either a command that must succeed or a person who
must say yes. Do not start a stage until the gate before it has passed.

**Think of it as** a relay. Each runner carries one thing and hands it over cleanly. Nobody runs two
legs at once.

## Contents

- Stage 1: Purpose
- Stage 2: Reuse check
- Stage 3: Skeleton
- Stage 4: One real example
- Stage 5: One source, then breadth
- Stage 6: Play the user and the agent
- Stage 7: Ship honestly
- The levels of a tool
- When the direction changes

## Stage 1: Purpose

Write one page, and nothing else yet.

| On the page | Example |
| --- | --- |
| Who it is for, as a user story | "As a consultant I want to deliver a presentation from my notes" |
| The one job | Turn notes into something worth sending |
| An analogy | "Ordering at a counter" |
| A North Star | One sentence that says what success is, for a person, in plain words |
| What the finished thing is | A product someone uses, a guide someone follows, or a demo someone watches. Pick one |
| What is out of scope | Three things it will not do |

**Gate:** a person reads the page and approves it. **Stop here and wait.**

Why first: the most expensive change is a change of purpose. It is cheap on one page.

## Stage 2: Reuse check

Find what already exists before building anything: features built into assistants, open-source
projects, paid services, and how people who do this well do it. Use the
[`landscape-review`](../../../skills/landscape-review/) skill.

**Gate:** every source carries the date it was checked, and one line records the decision: build,
use something that exists, or build on top of it.

## Stage 3: Skeleton

Make the folder before the content. Run `new_project.py`. Then write three things:

1. `README.md`: the front door for people, from the stage 1 page.
2. `AGENTS.md`: the front door for agents. The path from a request to a result, in numbered steps.
3. `gates.json`: the checks that will prove the tool works. They may fail today. Naming them now
   decides what "done" means before anyone is attached to the work.

**Gate:** `python3 tools/check_project.py drafts/<tool>` passes.

Why now: a layout chosen late gets chosen by accident, and every document then has to be rewritten
around it.

## Stage 4: One real example

Take one real request all the way to one finished output, by the shortest route. No options, no
variations, no second example.

**Gate:** a person looks at the output and says "this is what I wanted". **Stop here and wait.**
If they say anything else, the purpose page was wrong or was misread. Go back to stage 1 with what
you learned. That is the method working, not failing.

## Stage 5: One source, then breadth

Now widen, in this order.

1. Put the tool's facts in one file: the list of things it offers and the rules for choosing
   between them.
2. Generate everything that repeats those facts: indexes, counts in documents, reference sheets.
   A person edits the source. A script writes the rest.
3. Add content: more templates, more cases.

**Gate:** the build runs, the link check passes, and where a rule exists in two places (a page and
a server, say) a test proves they agree.

## Stage 6: Play the user and the agent

The author is the worst tester, because the author knows where everything is. So pretend not to.

1. **Worked examples.** Several requests as a person would type them, with the notes they would
   attach, and the finished output. Mark anything the notes did not say as missing.
2. **A scripted agent.** A script that reaches the tool only through what an outside agent can
   reach, and has to finish a file.
3. **Every request.** If the tool chooses, run every possible request through it and look at the
   worst answers.

**Gate:** the example and agent gates pass, and the worst answers are either fixed or the tool says
plainly that the fit is weak.

## Stage 7: Ship honestly

1. A status table in the README: each part, and who has and has not tried it.
2. A self-review scored out of 100 on a rubric, with "evidence from real use" as one line.
3. A short report for the owner and for users.

**Gate:** `python3 tools/gates.py drafts/<tool> --all` passes, and one person other than the author
has used the tool for a real job. **Stop here and wait.** Then it moves to `projects/`.

## The levels of a tool

Every tool has a base and up to three levels.

| | Holds | A person depends on |
| --- | --- | --- |
| `base/` | Everything: the thing itself, its examples, its source | Nothing but a browser or a reader |
| `level-1/` | Only instructions: for the assistant, and for the person using it | Any chat assistant |
| `level-2/` | Only what makes it repeatable or agentic: a preferences file, a skill, gates | An assistant that keeps files and runs skills |
| `level-3/` | Only connections: an MCP server, a plugin, a schedule | Other systems |

A level never copies the base. If you find yourself copying, the thing belongs in the base.

## When the direction changes

It will. When it does:

1. Rewrite the stage 1 page first, and get it approved.
2. Run the link check before and after moving anything. It is the net under the move.
3. Move retired work to [`plans/archive/`](../../../plans/archive/) with a line saying what replaced
   it. Do not delete it, and do not leave it where a newcomer will mistake it for current.
4. Update the status table the same day.
