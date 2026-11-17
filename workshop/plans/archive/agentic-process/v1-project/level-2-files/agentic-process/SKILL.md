---
name: agentic-process
description: Takes an idea or a spec for a small AI tool to a first version someone else can try, in nine steps with a gate after each, with a person deciding at each gate or, on autopilot, from a spec to a draft pull request. Use when asked to "start a new tool", "plan a tool", "build this project", "build this spec on autopilot", "follow the process", "set up a project folder", "what is the next step on this tool", or to review whether a tool is ready to share.
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

## Autopilot: from a spec to a finished tool

Use this when the person gives you a spec (a plan, a draft, notes), guidance and a delivery
target, and says "autopilot", or when you run on a schedule. The person decides by writing the
spec and by reviewing what you hand back. You decide everything in between, and record why.
Any tool that can be written as a workflow of steps fits, such as a chatbot tool that researches
a decision and writes a SWOT. The target is `repository` (a draft pull request), `chatbot` (a
package to install in a chatbot project) or `folder` (a local or Drive folder). Without one, ask
once, or use `folder` when no person is there.

1. **Read the inputs and check the spec is ready.** The spec, any draft it links to, and the
   guidance. Guidance wins over the spec when they differ. Write both paths at the top of the
   plan. A ready spec answers five things: the job in one sentence, what is out, one acceptance
   test (an input and a good result), where it runs, and what the demo must show. If the job or
   the acceptance test is missing, draft them, hand them back, and stop before building, unless
   the guidance says "proceed on assumptions". Anything else missing: choose, and mark it `Assumed:`.
2. **Steps 1 to 6 from the spec.** Take each answer from the spec. Where the spec is silent, make
   the smallest reasonable choice and mark it `Assumed:` in the plan. Do not stop to ask. Still
   run the reuse check: if something already does the whole job, stop, write the guide to it,
   and go to step 6 below with that guide as the result.
3. **Build the tool and a demo.** The instructions in `base/AI-INSTRUCTIONS.md` are the system
   prompt the tool runs on, with its workflow steps. Put any skill it needs in `level-2-files/`.
   The README's "Try it in five minutes" says where to save it (a chatbot project, a Drive
   folder, a repository) and how to run it each time. For a chatbot tool the demo is one worked
   example a fresh chat makes from the instructions, in `base/examples/`. If the tool needs code,
   build the smallest working version in `level-2-files/` with one command that runs it on
   invented data, and add that command to `_build/gates.json` as a gate named `demo`. If the
   spec asks for good-looking results, the instructions hand them to Artifact Studio.
4. **Steps 7 and 8 with fresh sessions.** Use sub-agents with no memory of this work for the
   review and for two test runs (see "The fresh-session test"). Fix repeats and blocking points,
   then run one more round. Without sub-agents, prepare the test folders and mark the gates open.
5. **Every gate passes or is open, never failed.** Run
   `python3 <project>/_build/checks/gates.py <project>`. Fix any failure. After two failed fixes
   of one gate, stop and hand back with that gate failed.
6. **Hand back.** Always write `_build/HANDBACK.md`: the four headings (Decided. Assumed. Not
   checked. Test this next.), each gate with pass or open and why, the gate output, and how to
   run the demo. Then deliver to the target. `repository`: a branch `build/<slug>`, one commit,
   and a draft pull request whose description is the hand-back; never merge. `chatbot`: the
   folder, plus a short list of what to paste where. `folder`: write it where the person said.

## The nine steps

The gate is the same question in every version of this process. The check is how you answer it.

<!-- steps:start -->
| # | Step | You do | Gate | Check |
| --- | --- | --- | --- | --- |
| 1 | Scope | One user, one job, what is out, the wow, and one test with a specific input and a good result | Can you say the job in one sentence? | The plan's job line is one sentence |
| 2 | Reuse check | Search in the order under "Step 2 in detail" below. Put up to five options in the plan, a longer list in `_build/landscape.md` | After what already exists, is there still something to build? If not, stop and write a guide to that thing. | If something does the whole job, stop and write a guide to it. Instructions written for an assistant the user already has count as building, unless one plain sentence already gives a result they would send unchanged |
| 3 | Outside help | List paid options for what is left. Do not pick a provider: decide only build, buy or by hand for each part, and write it under "Build or buy" in the plan | Do you know what you would build and what you would buy? | Your answer, written in the plan |
| 4 | Cost | Every dependency of the first version with its price and limit | Does the first version cost nothing, or an amount you accept? | Your answer, written in the plan |
| 5 | Simplest design | Which assistant, where files live, what stays manual. Make the folder from the template (see "Make the folder") | Could a beginner draw it? | The design is three lines in the plan. In the new folder, `python3 _build/checks/gates.py .` passes layout and links. `filled` fails until step 6, `built` until step 8 |
| 6 | Plan and front door | Fill `base/plan.md`. Write the README's hook, its "Try it in five minutes" section and at least one worked example: one for each kind of request the beginner version handles differently. Most first versions have one or two | Is the beginner version fully described? | The `filled` gate passes: the front page, the agent file and the plan have no blanks left |
| 7 | Review | A person, or a fresh session given only `base/plan.md`, explains it back | Can someone else explain it back to you? | The reviewer's summary matches the plan. With neither available, the gate stays open: say so and go on to step 8, whose test also reads the plan |
| 8 | Build and test | Build the beginner version. Run the fresh-session test (see "The fresh-session test") | Did a fresh session finish the job, and have you read what it tripped on? | The `built` gate passes. The fresh session finished the job. Its friction log has been read and the points in two or more logs fixed |
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

Code a builder runs (a script, a package file, tests) goes in `level-2-files/`. Nothing else sits
beside these.

The new folder starts with four gates in `_build/gates.json`: the layout, the links, `filled`
(the front page, agent file and plan have no blanks left) and `built` (the beginner version has
no blanks left). Expect `filled` to fail until step 6 and `built` until step 8; stop on any
other failure. A placeholder the tool's own users fill in, such as `[paste your notes]`, goes
inside a code block, where the checks leave it alone. Add one
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
