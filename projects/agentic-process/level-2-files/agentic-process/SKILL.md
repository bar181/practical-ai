---
name: agentic-process
description: Takes an idea for a small AI tool from a sentence to a first version someone else can try, in nine steps with a gate after each. Use when asked to "start a new tool", "plan a tool", "build this project", "follow the process", "set up a project folder", "what is the next step on this tool", or to review whether a tool is ready to share.
---

# Agentic process

You take a tool from an idea to a first version someone else can try. You do the drafting and
the building. A person makes the decisions. Nothing moves to the next step until its gate passes.

Think of it as a small building job with an inspector: frame before curtains, and a check at
every stage.

This folder is all you need, in any repository: this file, `new_project.py`, and `template/`,
which carries its own checks.

## Before you start

1. Ask at most two questions in a step. If the person has a plan already, find which step it has reached. Start there, not at step 1.
2. Find the project folder. If there is none, you make one at step 5. Keep your answers to steps
   1 to 4 in your notes until then, and copy them into `base/plan.md` at step 5.
3. Small job? If it is one person turning one kind of input into one result inside a chat, offer
   the short path: steps 1, 6 and 8 in full, steps 2 to 5 in a line each, step 7 folded into the test, and step 9 left open. Use all nine if they
   say no, or if the tool needs shared files, more than one person using it, or anything paid.
   People who only receive the result, such as customers, do not count; text pasted into the
   chat is not a file. Working unattended, take all nine steps: a person can shorten it later.

## The nine steps

The gate is the same question in every version of this process. The check is how you answer it.

<!-- steps:start -->
| # | Step | You do | Gate | Check |
| --- | --- | --- | --- | --- |
| 1 | Scope | One user, one job, what is out, the wow, and one test with a specific input and a good result | Can you say the job in one sentence? | The plan's job line is one sentence |
| 2 | Reuse check | Search in the order under "Step 2 in detail" below. Put up to five options in the plan, a longer list in `_build/landscape.md` | After what already exists, is there still something to build? If not, stop and write a guide to that thing. | If something does the whole job, stop and write a guide to it. Instructions written for an assistant the user already has count as building, unless one plain sentence already gives a result they would send unchanged |
| 3 | Outside help | List paid options for what is left. Do not pick a provider: decide only build, buy or by hand for each part, and write it under "Build or buy" in the plan | Do you know what you would build and what you would buy? | Your answer, written in the plan |
| 4 | Cost | Every dependency of the first version with its price and limit | Does the first version cost nothing, or an amount you accept? | Your answer, written in the plan |
| 5 | Simplest design | Which assistant, where files live, what stays manual. Make the folder from the template (see "Make the folder") | Could a beginner draw it? | The design is three lines in the plan. In the new folder, `python3 _build/checks/gates.py .` passes layout and links. `filled` fails until step 6 |
| 6 | Plan and front door | Fill `base/plan.md`. Write the README's hook, its "Try it in five minutes" section and at least one worked example: one for each kind of request the beginner version handles differently. Most first versions have one or two | Is the beginner version fully described? | The `filled` gate passes: no blanks are left from the template |
| 7 | Review | A person, or a fresh session given only `base/plan.md`, explains it back | Can someone else explain it back to you? | The reviewer's summary matches the plan. With neither available, the gate stays open: say so and go on to step 8, whose test also reads the plan |
| 8 | Build and test | Build the beginner version. Run the fresh-session test (see "The fresh-session test") | Did a fresh session finish the job, and have you read what it tripped on? | The fresh session finished the job. Its friction log has been read and the recurring points fixed |
| 9 | Grow | One addition at a time, each its own change request | Is the level below in use before you build the next? | Someone other than the builder has used the level below |
<!-- steps:end -->

## Step 2 in detail: the reuse check

Look in this order, cheapest first, and stop as soon as something does the whole job.

1. **Built in.** What the assistants the person uses already do: features, bundled skills,
   official catalogues of skills and plugins, connectors.
2. **Open source.** Repositories and community skills. Note the licence, the last update and who
   maintains it.
3. **Established practice.** How people who do this well do it, without a tool.
4. **Outside providers.** Only for what is left. List them evenly. Do not rank them.

Record one row per option: what it covers, cost, limits, what happens if it goes away, a link,
and the date you checked. Write "not confirmed" for any price or limit you could not check.
Never invent a product, a price or a feature. If you cannot search, write "not checked" and
list what the person should look up.

## Make the folder (step 5)

```
python3 <this folder>/new_project.py <slug> "<Title>" [<where>]
```

It makes `<where>/<slug>/`. Without `<where>` it uses `projects/` if there is one, otherwise the
current folder. Then check it at once:

```
python3 <slug folder>/_build/checks/gates.py <slug folder>
```

Every project uses this layout. Fix it now and do not change it later.

```
README.md          hook, one picture, the value, then "Try it in five minutes" as the first section
AGENTS.md          the path for an agent
LICENSE
base/              what a beginner needs: six things at most, counting examples/
level-2-files/     what a builder adds. Only if it holds something usable
level-3-files/     what a team adds. Only if it holds something usable
_build/            gates.json, checks/, runs/ for fresh-session tests, img/ for the README's picture
```

The new folder starts with three gates in `_build/gates.json`: the layout, the links, and
`filled`, which fails while any blank from the template is left and passes once step 6 is done.
Until step 6, expect `filled` to fail and stop only if another gate fails. Add one
whenever a step produces something a command can check. A gate is a name, what it proves, and
one command that fails when the thing is not true.

## The fresh-session test (step 8)

1. Make `_build/runs/round-1/<a few words for the request>/` and put in it only: a copy of the
   beginner version's instructions (`base/AI-INSTRUCTIONS.md`), the message a user would send
   (`prompt.txt`), and any files they would attach.
2. Start a new session with no memory of the project: a sub-agent, or a new chat. Tell it to
   follow the instructions using only that folder, decide where it would ask, and write the
   result, a hand-over note and `friction.md`: every place it had to guess, quoted, numbered and
   marked BLOCKING (a different guess would change the result) or MINOR.
3. Do not help it. Read `friction.md` before the result.
4. Fix first every point that appears in two or more logs, then every blocking point. Run a second round.

If you cannot start a new session, prepare the folder, say the test was not run, and leave the
gate open.

## Rules that never bend

- **One user, one job.** A second job goes under "Next" in the plan.
- **Stop at the gate.** If a gate fails, fix the step. Do not carry on and come back. A gate you
  cannot answer without a person is open, not failed: say so, and go on.
- **Say what a result is.** A result you wrote yourself is a reference. A result a fresh session
  made from the prompt is an example. Label each, in `base/examples/` and in the README.
- **Status lines say who tried it.** "Built" is not "used".
- **Numbers shown to a reader are checked by a script, or not shown.**
- **One addition, one change request.**
- **A person approves anything that is merged, posted, sent, paid or published.**

## What you hand back

After each step, three lines: what was decided, what you assumed, and the gate with pass, fail
or open. Write the same answer for each gate in the plan's "Gates" row. At the end: the plan, the
first version, the gate output, the friction logs unedited, and a note with four headings:
Decided. Assumed. Not checked. Test this next. (That note is about the build. The tool you build
hands its own users a different note, the one in the template's instructions.)
