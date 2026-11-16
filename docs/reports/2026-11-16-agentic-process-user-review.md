# Agentic Process: a review from the user's side

Written on 16 November 2026 by the assistant that built it, reading it as a newcomer at each of
the three levels. It is a self-review: no learner, builder or team lead has tried the project yet.

**Overall: 72 out of 100.** The Beginner level is close to ready. The Advanced level only works
inside this repository, which most builders will not be in. The biggest gap is the same as
project one's: nobody but the author has used it.

This score uses an end-user rubric, so it is not comparable with the 67 in
[the scores after the fixes](2026-11-16-scores-after-the-fixes.md), which used the project's own
score sheet.

## What the project is for

**Think of it as** a building site with an inspector. You agree the drawing before you pour
concrete, and nothing moves to the next stage until someone signs it off.

**At a high level:** an AI will build whatever you ask, fast. Agentic Process is the order of work
that makes sure it builds the right thing: nine steps from an idea to a first version someone
else can try, a gate question after each step, and a test by a fresh AI session before any person
spends time on it.

**In detail:**

| Level | Who | What they use | What they leave with |
| --- | --- | --- | --- |
| Beginner | Someone with a job they repeat, using any chatbot | The build coach, pasted in, or the nine step prompts one at a time | A one-page plan, a reusable prompt and a test |
| Advanced | A builder with a coding agent | A skill, a project template and a script that copies it | A project folder that passes its own checks |
| Expert | A team whose agents work unattended | Gates, the fresh-run test and a score sheet | Proof of what works before a person reviews it |

## Walking each path as a newcomer

### Beginner: "I have a job I repeat"

1. Opens the README. The hook and the "Read the guide" link are on the first screen.
2. Taps the guide. **Until this branch is merged, the link returns nothing**: it points at `main`.
   After the merge it opens through raw.githack.com, a free outside service.
3. Copies the "Try it" prompt into their chatbot. The coach walks nine steps, at most two
   questions each.
4. Or opens a step card and copies its prompt, one step at a time.

**Where they will trip:**

- The full coach session is nine steps. For a job as small as "draft my Monday email", that is a
  lot of ceremony. There is no short path.
- The coach has been run by AI sessions only, and only in Claude. A real person in ChatGPT is
  untested.
- Steps 2 to 4 assume web search. Without it the coach writes "not checked", which is honest but
  leaves a beginner unsure what to do next.

### Advanced: "I build with a coding agent"

1. Opens `level-2-files/README.md`, adds the skill to their agent.
2. Runs `new_project.py` from the repository root.
3. The skill runs the steps and the checks.

**Where they will trip:**

- **It only works inside this repository.** The script writes into `projects/`, and every check
  the skill runs (`check_project.py`, `check_links.py`, `gates.py`) lives in `workshop/tools/`,
  outside the project. A builder with their own repository has no instructions for that case.
- The second agent that ran the skill hit two failing commands and logged 8 blocking points. The
  two commands are fixed. The fixes have not been re-run by a second agent.
- Step 2 in the skill says "search for what already does it". The repository has a skill that
  does exactly that, `workshop/skills/landscape-review/`, and the project does not mention it.

### Expert: "my agents work unattended"

1. Opens `level-3-files/README.md`: gates, the fresh-run test, the score sheet.
2. Runs the gates on this project.

**Where they will trip:**

- `level-3-files/gates.json` checks **this** project, not theirs. The starter gates file a new
  project needs is in the Advanced template, and the Expert page does not point to it.
- "Run it unattended" is four short lines with no schedule example and no sample of what the
  agent hands back.
- 17 run-log files sit inside `level-3-files/fresh-run/runs/`. They are useful evidence and noise
  for someone looking for the tool.

## What is in `base/`, and is it worth its place?

| File | For | Valuable? | Keep or change |
| --- | --- | --- | --- |
| `AI-INSTRUCTIONS.md` | Beginner | Yes. The whole process in one paste. Tested four times by fresh sessions | Keep. Add a short path for small jobs |
| `PROCESS.md` | Everyone | Yes. New today: each step has a purpose, a user story per level, what to expect, proof and a prompt | Keep. It is generated, so it cannot drift from the guide |
| `explainer.html` | Everyone, and teachers presenting | Yes. The best entry point, now recommended at the top of the README | Keep. Needs a link that opens on a phone before the merge |
| `plan-template.md` | Beginner | Yes, but it is a **duplicate** of `level-2-files/template/base/plan.md` | Make one the source of the other |
| `TEACH-IN-30-MINUTES.md` | Teachers | Yes for teachers. A beginner does not need it | Keep. Consider moving out of `base/` if a beginner slot is needed |
| `examples/` | Beginner and Advanced | Yes. Two unedited fresh-session results, invented people | Keep. Add an Expert example |

## Skills: what the project needs and where they live

| Needed for | Where it is now | Should it be in this project? |
| --- | --- | --- |
| Running the nine steps with an agent | `level-2-files/agentic-process/` | Already here |
| Step 2, the reuse check | `workshop/skills/landscape-review/` | **Yes.** Copy it into `level-2-files/` or fold its search order into the skill's step 2 |
| Writing the plan | `workshop/skills/plan-writer/` | No. It writes plans for this repository's own tools. The project's plan template does the user's job |
| The layout, link and gate checks | `workshop/tools/` | **Yes.** Bundle copies in `level-2-files/` so the Advanced level works in any repository |

## Is the scaffolding clean?

Mostly. The layout check passes, `base/` holds six things, and the nine steps now have one source
(`_build/steps.py`) that writes both the steps page and the guide. A gate fails if either drifts.

Three things are not clean:

1. **The gates are worded three ways:** in the steps page, in the coach (adapted for a chat with no
   questions) and in the skill (adapted for checks an agent can run). Each reason is fair; the
   result is that a reader comparing them sees three versions of the same rule.
2. **The plan template exists twice.**
3. **Evidence and tools share a folder** in `level-3-files/`.

## Rubric

Scored 1 to 100 from the end user's side. The overall score is the unweighted average.

| # | Measure | Score | Evidence | Main gap |
| --- | --- | --- | --- | --- |
| 1 | Purpose is clear in one screen | 84 | Hook, recommended guide link and "Try it" are on the first screen | The guide link does not open until the merge |
| 2 | Beginner gets value fast | 78 | One paste. Four fresh-session runs each handed over a plan, a first version and a note | No human has used it; no short path for small jobs |
| 3 | Base content is worth its place | 82 | Six items, each with a clear reader | Duplicate plan template |
| 4 | Each step is easy to follow | 85 | Every step has a purpose, three user stories, what to expect, proof and a prompt | The prompts have not been run by anyone |
| 5 | Advanced level works where a builder works | 62 | A second agent ran it end to end; two failures fixed | Only works inside this repository; fixes not re-run |
| 6 | Expert level is usable as given | 66 | The fresh-run rules and score sheet are reusable and were used on two projects | Gates check this project, not the user's; no unattended example |
| 7 | The scaffolding is clean | 78 | Layout check passes; one source for the steps | Run logs beside the tools; duplicate template |
| 8 | The files agree with each other | 70 | Steps page and guide are generated from one source | Gates worded three ways |
| 9 | Honest about what is proven | 92 | Every status line says who tried it; all times labelled as estimates | None found |
| 10 | Evidence of real value | 25 | Fresh-session tests only | No person timed, no tool built by anyone else |

**Overall: 72.**

## Areas for improvement, most value first

| # | Improvement | Moves | Effort |
| --- | --- | --- | --- |
| 1 | Make the Advanced level work in any repository: bundle the three checks and `gates.py` into `level-2-files/`, and let `new_project.py` write into any folder | 5, 7 | About an hour |
| 2 | One wording for the gates: generate the coach's and the skill's gate tables from `steps.py`, keeping their extra notes as a second line | 8 | About 30 minutes |
| 3 | A short path in the coach: for a small job, steps 1, 6 and 8 only, with the others as one line each | 2 | About 30 minutes, then a fresh-session test |
| 4 | Fold the landscape review into the skill's step 2 | 5 | About 20 minutes |
| 5 | Point the Expert page at the starter gates file and add a worked unattended run | 6 | About 30 minutes |
| 6 | Move the run logs to `_build/runs/` | 7 | About 10 minutes |
| 7 | Make `plan-template.md` the single source; the build copies it into the template | 3, 7 | About 10 minutes |
| 8 | Three learners take the Beginner path, timed | 2, 10 | The owner's class |
| 9 | Run the "Try it" prompt and two step prompts in ChatGPT and Gemini | 2, 4 | The owner, about 15 minutes |

Items 1 to 7 would bring every measure except "evidence of real value" to 80 or above. Items 8
and 9 need people.

## To-do list for Agentic Process

The same list is in [`docs/TODO.md`](../TODO.md) under "Agentic Process".

**For the assistant, in order**

- [ ] Bundle the checks into `level-2-files/` so the skill and template work in any repository
- [ ] Generate the coach's and the skill's gate tables from `_build/steps.py`
- [ ] Add a short path to the coach for small jobs, and test it with two fresh sessions
- [ ] Fold the landscape review's search order into the skill's step 2
- [ ] Point the Expert page at the template's starter gates, and add one worked unattended run
- [ ] Move the run logs from `level-3-files/fresh-run/runs/` to `_build/runs/`
- [ ] Make `base/plan-template.md` the one source of the template's plan
- [ ] Re-run the skill with a second agent after these changes
- [ ] Add an Expert worked example

**For the owner**

- [ ] Merge PR 1, so the guide link and the "Try it" link open
- [ ] Turn on GitHub Pages, or share the guide's Claude artifact, so it opens on a phone without an outside service
- [ ] Run the "Try it" prompt in ChatGPT and Gemini
- [ ] Teach the 30-minute lesson once, time each section, and note where learners stopped
- [ ] Build the next tool, Document to action brief, with this process from step 1, and time it
