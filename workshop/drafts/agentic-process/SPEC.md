# Agentic Process: specification, version 2

**Draft, 16 November 2026.** The source of truth for what Agentic Process is for and when it is
done. Everything in this folder follows it. Sections 2 to 4 keep the owner's own words from the
version 1 spec. Decisions not yet confirmed are marked **Owner to confirm**, with the default used
until then. Why version 1 was restarted: [`EVALUATION.md`](EVALUATION.md).

## 1. The problem

AI agents build fast and build the wrong thing. Artifact Studio, the first tool here, was rebuilt
three times before its shape was right. Version 1 of this project then grew to 145 files around
teaching and its own tests. The repository holds 24 plans and 9 drafts waiting to be built, each
of which should become a useful tool without the owner guiding every step.

## 2. Purpose, goal and North Star

**Agentic Process builds useful tools for work people repeat.** Its nine-step method and its
builder skill are shared scaffolding for every project in this repository. Each project gives
someone a useful tool they can start quickly, with a short explainer that shows how to use it.

**Goal.** Start with one real job, use the simplest suitable implementation, and get an output
you can use. Bring fresh input next time without recreating the workflow.

**User value.** Save time or improve the quality of a specific result. Measure one of those
outcomes against the usual way of doing the job. Every project has a short explainer that shows
what it does, how to start, what goes in and comes out, and what to check. Include one worked
example. The explainer can live in the README.

**North Star.** Someone opens a project and gets a usable result with their own input. At
Level 3, connected systems supply the inputs and the workflow runs mostly on its own, with
a person handling decisions or exceptions that need them.

### Reuse first

1. **Use an existing capability** when it already does the job. Ship the explainer with the
   setup and example an operator needs to use it.
2. **Wrap an existing skill or plugin** when the job needs business rules, a specific output or
   an extra step. Verify the inputs, permissions and output in the intended environment.
3. **Build the missing piece** when existing tools leave a material gap. Anthropic's
   `build-agent` can package recurring work as a reusable Claude skill. Our builder skill
   applies this repository's process, selects what to reuse, fills the gaps, and delivers
   a usable tool with an explainer and a tested example.

Reuse Anthropic's capabilities wherever they fit. Its `build-agent` skill already turns recurring
work into a reusable Claude skill, and its plugins bundle existing workflows and connectors. For
each project, use what already does the job, add a thin layer for any business rules or missing
steps, and build only what is still missing. How much Anthropic covers depends on the individual
workflow and where it runs.

## 3. Who it is for

| Who | What they need |
| --- | --- |
| A person doing recurring work | A tool they can start quickly with their own input and use again |
| A builder or coding agent | One builder skill and a shared nine-step method for producing a tool from an idea or spec |
| A team or client operating a connected workflow | A mostly automated run that uses the systems where work already happens |

## 4. Implementation levels

Levels describe setup and automation, so the same person can use Base for one job and Level 3
for another.

| Level | What the user gets |
| --- | --- |
| Base | An explainer with a quick start and worked example, plus one runnable instruction file or a direct link to an existing tool. The user brings the input and starts the run |
| Level 2 | A saved workflow, such as a Claude Project or reusable skill, that the user can start whenever needed |
| Level 3 | A mostly automated workflow. Connected systems supply the inputs and receive the outputs, a trigger starts the run, and a person handles exceptions or decisions that need them |

## 5. What this project delivers

Four things, and nothing else until the acceptance criteria hold:

| Deliverable | File | State |
| --- | --- | --- |
| One process document | [`PROCESS.md`](PROCESS.md) | Written |
| One builder skill, with its project template, checks and Autopilot prompt | [`builder/`](builder/) | Carried over from version 1; to align with this spec (section 9) |
| One Base package template | [`package-template/`](package-template/) | Carried over; to align |
| One complete example tool, built with the process | [`examples/decision-support/`](examples/decision-support/) | Carried over, tested on two decisions |

The explainer for Agentic Process itself is [`README.md`](README.md).

## 6. The builder: what goes in and comes out

**In:** an idea or a spec, a few lines of guidance, and a delivery target: `chatbot` (a package to
save in a chatbot project), `folder` (the same, written to a local or Drive folder) or
`repository` (a draft pull request).

**A spec is ready when it answers five things:** the job in one sentence; what is out; one test
input and what a good result looks like; where it runs; what the demo must show. If the job or
the test is missing, the builder drafts them and stops for approval. Anything else missing, it
chooses and marks `Assumed:`.

**Out:** the Base tool (section 4), tested by a fresh session on two different inputs, and a
hand-back note with four headings: Decided. Assumed. Not checked. Test this next.

**People decide** when they approve the spec, when the builder stops for a missing job or test,
and before anything is merged, sent, posted, paid or published.

## 7. Acceptance criteria for version 2

| ID | Criterion | How it is checked |
| --- | --- | --- |
| AC-1 | A fresh session with only the builder skill rebuilds the decision-support tool from its workflow card, and the result matches the carried-over tool on the bakery input | Side-by-side outputs on the known input |
| AC-2 | From the learning-system plan and three lines of guidance, the builder delivers a Base tool with an explainer, a runnable entry point and a worked example, asking nothing in between unless the spec-ready stop applies | The delivery, and the session transcript |
| AC-3 | Each delivered tool is tested on two different inputs, and every blocking point is fixed or listed | The test logs, outside the tool's folder |
| AC-4 | The owner runs one delivered tool from its explainer, with their own input, and gets a usable result without editing the instructions | The owner's run |
| AC-5 | One Level 3 pilot: a working Base tool, connected only where it removes recurring work, with its trigger, normal run and exception path verified | The pilot's run record |
| AC-6 | This draft stays small: under 40 files, and no generated file without a stated reason | A file count |

## 8. Out of scope for version 2

- Courses. Each tool has a short explainer.
- Generated pages and a build system.
- A Slack bot or a tool server, until a Level 3 pilot needs one.
- A queue that builds several plans in a row.

## 9. Next, in order

1. Align [`builder/agentic-process/SKILL.md`](builder/agentic-process/SKILL.md) and its template
   with this spec: the Base deliverable in section 4, the process in [`PROCESS.md`](PROCESS.md),
   reuse first, and the `build-agent` ideas in [`LESSONS.md`](LESSONS.md).
2. Run AC-1.
3. Run AC-2 on the learning-system plan.
4. Move this draft to `projects/agentic-process/` once AC-1 to AC-3 hold.

## 10. How it is scored

Out of 100. No item counts users.

| Item | Weight | What 100 looks like |
| --- | --- | --- |
| A person gets a useful Base result fast | 20 | From the explainer, a person runs a sample and gets a usable result with fresh input in the stated environment |
| The Base package is simple and complete | 15 | The explainer, runnable entry point and worked example are enough to adopt the tool |
| One process, one builder | 15 | The builder follows the process; nothing duplicates it |
| Proven on fresh input | 15 | Two different inputs per tool; the last fixes re-tested |
| Reuse first | 10 | Each delivery records what it reused, wrapped or built, with sources |
| Level 3: connected and automated | 15 | A connected workflow runs from its trigger to usable output with a demonstrated exception path |
| Small and honest | 10 | AC-6 holds; every status says who has tried it |

**Starting point:** version 1 scored 44 against the owner's spec ([`EVALUATION.md`](EVALUATION.md)).
Version 2 has not been scored yet: nothing in it has run since the restart.

## 11. Open questions for the owner

1. **One builder:** drop the separate chatbot coach, since the builder skill can be pasted into a
   chatbot? Default: yes.
2. **One process document:** the plan template has its own nine-step page
   (`workshop/plans/plans-template/BUILD-PROCESS.md`). Point it at [`PROCESS.md`](PROCESS.md)
   once this draft moves to `projects/`? Default: yes.
3. **Level 3 pilot:** which recurring workflow merits the first connected run?
4. **Spec readiness stop:** may guidance say "proceed on assumptions" to skip it? Default: yes.
