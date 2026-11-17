# Agentic Process: specification

**Version 1.** This is the source of truth for what Agentic Process is
for and when it is done. The README, the skill and every check follow it. Where they differ, this
file wins and they are fixed. Decisions the owner has not yet confirmed are marked **Owner to
confirm**, with the default this spec uses until then.

**Think of it as** a general contractor's method. The owner hands over a drawing (the spec) and a
note (the guidance). The method decides the order of work, an inspector signs off each stage (the
gates), and the owner comes back to an inspected first floor and a list of what was assumed.

## 1. The problem

AI agents build fast and build the wrong thing. Artifact Studio, the first tool in this repository,
was rebuilt three times before its shape was right. The repository now holds 24 plans and 9 drafts
waiting to be built. Building each one by guiding an agent step by step costs the owner hours per
project, and the result depends on how well the owner remembered every step that day.

## 2. Purpose, goal and North Star

**Agentic Process builds useful tools for work people repeat.**

**Goal.** Start with one real job, use the simplest suitable implementation, and get an output
you can use. Bring fresh input next time without recreating the workflow.

**User value.** Save time or improve the quality of a specific result. Measure one of those
outcomes against the usual way of doing the job. Every project has a short explainer that shows
what it does, how to start, what goes in and comes out, and what to check. Include one worked
example. The explainer can live in the README.

**North Star.** Someone opens a project and gets a usable result with their own input. At
Level 3, connected systems supply the inputs and the workflow runs mostly on its own, with
a person handling decisions or exceptions that need them.

**How we build.** The nine steps in [PROCESS.md](../../../projects/agentic-process/base/PROCESS.md)
are the builder's process. A simple chat tool takes the short path: scope, design and test,
with a quick reuse check. The operator starts with the explainer and the runnable tool.

### Reuse first

1. **Use an existing capability** when it already does the job. Ship the explainer with the
   setup and example an operator needs to use it.
2. **Wrap an existing skill or plugin** when the job needs business rules, a specific output or
   an extra step. Verify the inputs, permissions and output in the intended environment.
3. **Build the missing piece** when existing tools leave a material gap. Anthropic's
   `build-agent` can package recurring work as a reusable Claude skill. Our builder skill
   applies this repository's process, selects what to reuse, fills the gaps, and delivers
   a usable tool with an explainer and a tested example.

Sources: [Anthropic's knowledge-work plugins](https://github.com/anthropics/knowledge-work-plugins)
and [build-agent](https://github.com/anthropics/knowledge-work-plugins/blob/main/small-business/skills/build-agent/SKILL.md).

## 3. Who it is for

| Who | What they need |
| --- | --- |
| A person doing recurring work | A tool they can start quickly with their own input and use again |
| A builder or coding agent | One builder skill and a shared nine-step method for producing a tool from an idea or spec |
| A team or client operating a connected workflow | A mostly automated run that uses the systems where work already happens |

## 3a. Implementation levels

Levels describe setup and automation. The same person can choose any level.

| Level | What runs | Minimum deliverable |
| --- | --- | --- |
| Base | A person provides input and starts the workflow in chat or through an existing tool | Explainer with a quick start and worked example, plus one runnable instruction file or a direct link to an existing tool |
| Level 2 | A saved workflow a person starts when needed | A saved Project or reusable skill, using existing skills or plugins where they add value |
| Level 3 | A mostly connected and automated workflow | Connected inputs and outputs, a trigger or schedule, and a tested normal run and exception path |

**Shared scaffolding.** Keep one process document and one builder skill. A Base project needs
an explainer and a runnable entry point. Add a workflow card, standalone example, setup file
or custom runtime skill when it serves the job. The builder tests the result and records what ran.

## 4. Use cases

| ID | Use case | Trigger | Result | In version 1 |
| --- | --- | --- | --- | --- |
| UC-1 | **Build a tool from its spec** | A person runs the autopilot prompt with a spec, guidance and a delivery target | The tool, tested by fresh sessions, with the gate record and the hand-back note, delivered to the target (section 5) | Yes. The core |
| UC-1a | ... for a project on GitHub | Target: a repository | A draft pull request on `build/<slug>`. Example: the learning database in this repository | Yes |
| UC-1b | ... for a chatbot | Target: a chatbot project or a folder | A tool package. Example: a decision-support tool that researches a decision and writes a SWOT, saved as a Claude Project, a ChatGPT Project or a Gemini Gem, or in a Drive folder the chatbot is connected to | Yes |
| UC-2 | **Decide whether something should be built** | Owner or agent proposes a change to this repository | A decision record from steps 1 to 4: stop (it exists), wrap, or build, with sources and dates | Yes |
| UC-3 | **Guided build from an idea** | A person works step by step with an agent | The same outputs as UC-1, with the person answering at each gate | Yes, exists |
| UC-4 | **Build on a schedule** | A scheduler (Claude Code routine, ChatGPT or Codex task, an issue assigned to an agent) runs UC-1 | The same as UC-1 | The prompt only. The scheduler is the owner's |
| UC-5 | **Start from Slack or a tool server** | A message or a call starts UC-4 | The same as UC-1 | No. Later |

## 5. Inputs and outputs (UC-1)

**Input**

| Field | Required | Example |
| --- | --- | --- |
| Spec | Yes | `workshop/plans/learning-system/README.md` and the draft it links to |
| Guidance | Yes, a few lines | Who the demo is for, what it must show, what to avoid |
| Delivery target | Yes | `repository` (a draft pull request), `chatbot` (a tool package to install in a chatbot project), or `folder` (the package in a local or Drive folder) |
| Mode | No | `autopilot` (default for UC-1) or `guided` |

**A spec is ready when it answers five things.** The agent checks these first (the `spec-ready`
gate in section 7):

1. **The job:** one user and one job, in one sentence.
2. **Out of scope:** what the first version will not do.
3. **The acceptance test:** one specific input and what a good result looks like.
4. **Where it runs:** a chatbot, a script, or both.
5. **The demo:** what the owner must be able to run or see.

If 1 or 3 is missing, the agent drafts them, writes them into the hand-back, and stops before
building: that is the one mid-run decision. If 2, 4 or 5 is missing, it chooses, marks the choice
`Assumed:`, and goes on. **Owner to confirm**: whether guidance can say "proceed on assumptions"
to skip the stop. Default: yes.

**Output by target.** The table describes a full Autopilot delivery. For a Base tool, the
minimum in section 3a applies. A reused tool can be delivered as an explainer with a direct link.

| Part | Where, in the project folder | Checked by |
| --- | --- | --- |
| The plan, filled from the spec, assumptions marked | `base/plan.md` | `filled` |
| The instructions: the system prompt the tool runs on, with its workflow steps | `base/AI-INSTRUCTIONS.md` | `built` |
| How to install and use it: where to save it (a chatbot project, a Drive folder, a repository) and how to run it each time | `README.md`, "Try it in five minutes" | `filled` |
| Skills, if the workflow needs them | `level-2-files/<skill>/SKILL.md` | the skill rules |
| A demo: for a chatbot tool, one worked example made by a fresh chat from the instructions; for code, one command on invented data | `base/examples/`, or `level-2-files/` and the `demo` gate | `demo` |
| Two fresh-session test logs, unedited | `_build/runs/` | `tested` |
| The gate record and the hand-back note | `_build/HANDBACK.md` | `handback` |

| Target | Delivered as |
| --- | --- |
| `repository` | A branch `build/<slug>` and a draft pull request whose description is the hand-back. Never merged by the agent |
| `chatbot` | The folder, plus a short list of what to paste where: the instructions into the project's instructions, the skills and examples as project files |
| `folder` | The folder written to the place the person named, such as a Drive folder their chatbot is connected to |

The **project explainer** is part of every delivery. The tool's own output, such as a document,
page or deck, can use [Artifact Studio](../../../projects/artifact-studio/) for layout when
the project calls for it.

The hand-back note has four headings: Decided. Assumed. Not checked. Test this next.

## 6. The method

Nine steps, a gate after each. The steps, their purpose, proof and prompts are defined once in
`projects/agentic-process/_build/steps.py`; everything else is generated from it.

| Stage | Steps | Autopilot behaviour |
| --- | --- | --- |
| Decide | 1 Scope, 2 Reuse check, 3 Outside help, 4 Cost | Answers come from the spec. The reuse check is always run, with dated sources. If something already does the whole job, the result is a guide to it, not a build |
| Design | 5 Simplest design, 6 Plan and front door, 7 Review | The folder is made from the template at step 5 and its layout never changes. The review is done by a fresh session given only the plan |
| Build and test | 8 Build and test | Build or assemble the Base version and the demo. Two fresh sessions test it. Fix points that repeat, then blocking points. One more round |
| Grow | 9 Grow | Not run on autopilot. Additions are later pull requests |

## 7. Gates

A gate is a name, what it proves, and one command that fails when it is not true. Judgement gates
are recorded as pass, fail or open with a reason; machine gates are run.

| Gate | Proves | Kind | State today |
| --- | --- | --- | --- |
| `spec-ready` | The spec answers the job and the acceptance test | Recorded by the agent | **To build** |
| `layout` | The folder follows the agreed shape | Script | Exists |
| `links` | No broken link | Script | Exists |
| `filled` | The plan, README and agent file have no blanks | Script | Exists |
| `built` | The instructions have no blanks | Script | Exists |
| `demo` | The demo runs on invented data | Script, added by the agent when code is needed | Written into the skill, not run |
| `tested` | Two test logs exist and each blocking point is fixed or listed as open | Script | **To build** |
| `handback` | The hand-back note exists with its four headings and the gate record | Script | **To build** |

**People decide three times:** approving the spec (D1), the stop before building when the job or
the acceptance test is missing (D2, only if it happens), and merging (D3). Agents never merge,
post, send, pay or publish.

## 8. Acceptance criteria for version 1

Version 1 is done when all of these hold. Each is checked by a command or by the owner reading a
pull request.

| ID | Criterion | How it is checked |
| --- | --- | --- |
| AC-1 | From the learning-system spec, three lines of guidance and the `repository` target, an agent with only the skill opens a draft pull request in one session | The pull request exists on `build/learning-system` |
| AC-2 | In AC-1 and AC-6, the person is asked nothing between giving the prompt and reading the hand-back, unless the `spec-ready` stop applies | The session transcript |
| AC-3 | Every gate in section 7 reports pass or open; the demo command exits 0 | `gates.py` output in the pull request |
| AC-4 | Every choice the spec did not make is listed under Assumed | The owner reads the hand-back |
| AC-5 | The owner would merge after review with small edits only | The owner's judgement, recorded in the pull request |
| AC-6 | From the decision-support spec and the `chatbot` target, the agent delivers a tool package; the owner saves it as a chatbot project and runs one real decision to a SWOT without changing the instructions | The package, and the owner's run |
| AC-7 | This project's own gates pass, including the template running in an empty repository | `gates.py` on `level-3-files/gates.json` |

## 9. Constraints

- One skill folder (`SKILL.md`, `new_project.py`, `template/`) works in any repository with no
  other files from here.
- Gates are plain Python with no packages, so they run anywhere an agent runs.
- Invented data only in demos and tests. No real company or person is named.
- Every status line says who has tried the thing. "Written" is not "run".
- Runner of record is Claude Code. Other runners are expected to work and are listed as untested.
- Scope stays small: each addition to this project is its own pull request, reviewable in minutes.

## 10. Out of scope for version 1

Deferred until the acceptance criteria hold:

- End-user courses. Each project gets a short explainer for day-to-day use.
- A Slack bot or a tool server (UC-5).
- A queue that builds several plans in a row.
- Testing the coach in ChatGPT, Gemini or Copilot.
- An additional runtime or plugin where the Base workflow already meets the acceptance check.

## 11. How the project is scored

Out of 100. No item counts users. Rewritten on 16 November 2026 to match the goal in section 2;
the earlier rubric weighted Autopilot at 25 and scored 57.

| Item | Weight | What 100 looks like |
| --- | --- | --- |
| A person gets a useful Base result fast | 15 | From the explainer, a person can run a sample and get a usable result with fresh input in the stated environment |
| The Base package is simple and complete | 15 | The explainer, runnable entry point and worked example are enough to adopt the tool |
| The method helps people decide | 15 | Each step names the decision it helps make and what it adds to the files; the short path is the default for simple work and delivers the runnable tool and explainer |
| It is proven on fresh input | 15 | Fresh sessions run the example tool on at least two different inputs, its result follows its own rule, and the last fixes are re-tested |
| The hand-back is reviewable and honest | 10 | Every change, test and open item is shown; nothing untested is called tested |
| Coders get an idea, intent and spec path | 10 | One worked example from a messy request to intent to a testable spec, handed to an agent without explaining it again |
| Level 3: connections and automation | 10 | A connected workflow runs from its trigger to usable output with a demonstrated exception path |
| Autopilot | 10 | AC-1 and AC-6 hold (tracked in [`AUTOPILOT-PROGRESS.md`](AUTOPILOT-PROGRESS.md)) |

## 12. Evidence recorded on 16 November 2026

These scores describe the build under the earlier rubric.

| Item | Before today's pass | Now | Why |
| --- | --- | --- | --- |
| Beginner result | 50 | 80 | The README opens on the finished tool with a sample and a "you got it right if" list. A beginner walkthrough said yes to running it. Not yet run by a person, or in ChatGPT |
| Four-file package | 60 | 75 | Setup steps for ChatGPT, Claude and Gemini projects, and a no-setup route. A person has not filled in the template yet |
| Method helps decide | 65 | 80 | Every step names its decision and what it adds; the short path comes first; the coach's test loop is explicit. The changed coach is not re-tested |
| Proven on fresh input | 55 | 75 | Nine runs on two decisions; the final run of each followed its rule with 1 blocking point, since fixed and not re-tested. Claude only |
| Reviewable hand-back | 80 | 85 | [`HANDBACK-2026-11-16.md`](HANDBACK-2026-11-16.md) |
| Coder path | 30 | 30 | Not built: the meeting-notes walkthrough is the next piece of work |
| Level 3 | 55 | 55 | Five of eight gates; logs now in Level 3; no connection example |
| Autopilot | 20 | 20 | Not run |
| **Total** | **53** | **66** | |

## 13. Next implementation pass

1. Align the README, builder skill and project template with the Base package. Keep the
   nine steps in their existing source. Use a pasteable instruction or direct tool link
   for the Base entry point.
2. Use the existing decision-support project to prove the smaller package. Check for a
   suitable existing skill first, then run from the explainer on sample and fresh inputs.
   Record the result, setup time and any manual work still required.
3. For a later Level 3 pilot, take one working Base tool and connect only the steps that
   remove recurring work. Verify the trigger, inputs, output and exception path in that
   environment before calling it automated.

## 14. Open questions for the owner

1. **Level 3 pilot.** Which recurring workflow merits the first connected run?
2. **Spec readiness stop:** may guidance say "proceed on assumptions" to skip it? Default: yes.
3. **Demo for a chatbot-only tool:** is the instructions file plus one example output from a fresh
   session enough? Default: yes.
4. **For the `repository` target:** one pull request per project (default), or one per stage?
5. **Artifact Studio for outputs:** offered only when the spec asks (default), or on by default for any tool whose result is a document?
