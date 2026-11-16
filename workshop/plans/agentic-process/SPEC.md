# Agentic Process: specification

**Version 1, written on 16 November 2026.** This is the source of truth for what Agentic Process is
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

## 2. Purpose

**Agentic Process turns a spec and a few lines of guidance into a reviewed, runnable first version
of a tool, delivered as a draft pull request, with a person deciding only at the start and the end.**

**North Star:** a person, or an agent working alone, can take an idea or a spec to a tool that
someone else can use, without rebuilding it three times on the way.

The value is the method and its automation: a fixed order of work, gates a script can check, a
test by a fresh session, and a hand-back a person can review in minutes. Courses and guides for
end users are not the product (see section 10).

## 3. Who it is for

| Who | Role | What they need from it |
| --- | --- | --- |
| The repository owner | Primary user | Hand a plan from `workshop/plans/` to an agent and get back a pull request worth reviewing, without guiding each step |
| A coding agent | Primary actor | One skill folder that says what to do, in what order, what to check, and when to stop |
| A builder in another repository | Secondary user | The same skill folder, copied into their repository, working without anything else from here |
| A person with only a chatbot | Kept, not extended | The coach (`base/AI-INSTRUCTIONS.md`): the same nine steps, one question at a time. Frozen at its current state |

## 4. Use cases

| ID | Use case | Trigger | Result | In version 1 |
| --- | --- | --- | --- | --- |
| UC-1 | **Build a repository project from its spec** | Owner runs the autopilot prompt with a spec path and guidance | Draft pull request on `build/<slug>` with the project folder, a runnable demo, the gate record, two test logs and the hand-back note | Yes. The core |
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

**Output:** one draft pull request containing

| Output | Where | Checked by |
| --- | --- | --- |
| The project folder, made from the template | `projects/<slug>/` | `layout`, `links` |
| The plan, filled from the spec, assumptions marked | `projects/<slug>/base/plan.md` | `filled` |
| The beginner version: instructions anyone can paste | `projects/<slug>/base/AI-INSTRUCTIONS.md` | `built` |
| A runnable demo, if the first version needs code | `projects/<slug>/level-2-files/` | `demo`: one command, invented data, exit code 0 |
| Two fresh-session test logs, unedited | `projects/<slug>/_build/runs/` | `tested` |
| The gate record and the hand-back note | The pull request description, and `_build/HANDBACK.md` | `handback` |

The hand-back note has four headings: Decided. Assumed. Not checked. Test this next.

## 6. The method

Nine steps, a gate after each. The steps, their purpose, proof and prompts are defined once in
`projects/agentic-process/_build/steps.py`; everything else is generated from it.

| Stage | Steps | Autopilot behaviour |
| --- | --- | --- |
| Decide | 1 Scope, 2 Reuse check, 3 Outside help, 4 Cost | Answers come from the spec. The reuse check is always run, with dated sources. If something already does the whole job, the result is a guide to it, not a build |
| Design | 5 Simplest design, 6 Plan and front door, 7 Review | The folder is made from the template at step 5 and its layout never changes. The review is done by a fresh session given only the plan |
| Build and test | 8 Build and test | Build the beginner version and the demo. Two fresh sessions test it. Fix points that repeat, then blocking points. One more round |
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
| AC-1 | From the learning-system spec and three lines of guidance, an agent with only the skill opens a draft pull request in one session | The pull request exists on `build/learning-system` |
| AC-2 | In AC-1, the owner is asked nothing between giving the prompt and reading the pull request, unless the `spec-ready` stop applies | The session transcript |
| AC-3 | Every gate in section 7 reports pass or open; the demo command exits 0 | `gates.py` output in the pull request |
| AC-4 | Every choice the spec did not make is listed under Assumed | The owner reads the hand-back |
| AC-5 | The owner would merge after review with small edits only | The owner's judgement, recorded in the pull request |
| AC-6 | AC-1 to AC-5 hold for a second, different spec (meeting notes to actions) | A second pull request |
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

- End-user courses, guides and explainer pages. The three built so far (the guide, the North Star
  page and the course) are parked in `projects/agentic-process/_build/deferred/` and not linked.
- A Slack bot or a tool server (UC-5).
- A queue that builds several plans in a row.
- Testing the coach in ChatGPT, Gemini or Copilot.
- Changes to the coach beyond keeping it in step with `steps.py`.

## 11. How the project is scored

Out of 100. No item counts users.

| Item | Weight | What 100 looks like |
| --- | --- | --- |
| Spec and method are defined | 20 | This file, the nine steps from one source, every step with purpose, proof and gate |
| Gates a machine can check | 20 | Every gate in section 7 exists and runs |
| Autopilot works | 25 | AC-1 to AC-5 hold |
| It generalises | 15 | AC-6 holds |
| Works in any repository | 10 | AC-7 holds |
| Focus | 10 | Nothing in the project that section 10 defers |

## 12. Where it stands on 16 November 2026

| Item | Score | Why |
| --- | --- | --- |
| Spec and method | 85 | This file now exists; the method has been stable since the fourth audit |
| Machine gates | 55 | Five of eight exist; `spec-ready`, `tested` and `handback` do not |
| Autopilot | 20 | Written into the skill; never run |
| Generalises | 0 | Not run |
| Any repository | 90 | The template gate passes in an empty repository; one unattended run from an idea |
| Focus | 80 | The end-user pages are parked; 50 test-log files remain as evidence |
| **Total** | **52** | |

**Next, in order:** build the three missing gates (about 45 minutes), then run AC-1 on the
learning-system spec and read the pull request.

## 13. Open questions for the owner

1. **The coach for chatbot users:** keep it frozen as now (default), or drop it from this project?
2. **Spec readiness stop:** may guidance say "proceed on assumptions" to skip it? Default: yes.
3. **Demo for a chatbot-only tool:** is the instructions file plus one example output from a fresh
   session enough? Default: yes.
4. **One pull request per project** (default), or one per stage?
