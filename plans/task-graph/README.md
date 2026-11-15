# Task decomposition and dependency graph: North Star

Stages 1 to 3 of the [project method](../../drafts/project-method/base/METHOD.md). Written
15 November 2026. **Not yet approved.** Complexity: beginner to intermediate.

**Think of it as** a recipe laid out before cooking. You can see every step, which ones must wait
for another, which can run side by side, and what to start with right now.

**North Star:** any goal, from a decision to a new coding project, becomes a picture of the work
that shows what to do first and what is blocked, in under ten minutes.

## Understand

| | |
| --- | --- |
| Who it is for | As a decision maker or a builder, I want a goal broken into tasks with what depends on what, so that I and my agents start in the right place and nothing is skipped |
| The one job | Turn a goal into a list of tasks with dependencies, then show it in the form the reader needs |
| The finished thing is | A product: one data file for the tasks, and output templates that draw it |

## Research: what already exists

| Source | Checked | What we take from it |
| --- | --- | --- |
| [Beads](https://github.com/steveyegge/beads), an open-source issue tracker for agents | 15 Nov 2026 | Tasks that block other tasks, and a "ready" list that shows only work with nothing open in front of it. An agent cannot skip a step it is never shown |
| [A guide to Beads](https://betterstack.com/community/guides/ai/beads-issue-tracker-ai-agents/) | 15 Nov 2026 | A flat checklist hides order and priority. A graph with ids, epics and sub-tasks makes them explicit |
| [Why agents skip steps](https://trilogyai.substack.com/p/how-to-fix-your-ai-agents-keep-cutting) | 15 Nov 2026 | Make each step its own task with an unambiguous "done". Skipping should be structurally impossible, not merely forbidden |
| [Task Master](https://www.mdskills.ai/skills/claude-task-master), an open-source task manager for coding agents | 15 Nov 2026 | A written requirements document is parsed into one tasks file with dependencies and priorities, and the agent asks for the next task. A small set of core tools keeps the cost down |
| [prd-taskmaster](https://awesome.ecosyste.ms/projects/github.com%2Fanombyte93%2Fprd-taskmaster), an open-source engine | 15 Nov 2026 | Interview first, then a graded requirements page, then a task graph in dependency order. A task is done only with evidence |
| [Spec-driven development](https://www.verdent.ai/guides/coding/spec-driven-development) | 15 Nov 2026 | Tasks are the unit that can be handed out. Each is small enough to review alone |
| Task lists and planning modes built into coding assistants | Known from using the products, not researched today | They hold the steps for one session and are gone after it. They show order, not what blocks what, and they draw nothing a decision maker can read |
| Work breakdown structures, the critical path and Gantt charts | Long-standing project practice, no single source | Break work down until each piece has one owner and one result. The longest chain of dependent tasks sets the finish date |
| [The artifact studio](../../drafts/artifact-studio/) in this repository | 15 Nov 2026 | Its templates, looks and one-file output are reused for every view |

**Decision:** build on top. The task file is plain and small, and close to what Task Master
already writes, so a plan can move between them. What these tools lack is what this one adds: a
goal that is not code, and views a decision maker can read. For coding projects that outgrow the
file, hand over to a real tracker such as Beads or Task Master: the plan says when.

## Scope

**In:** breaking a goal into tasks; dependencies, owners, estimates and a "done when" line for each
task; finding what is ready now and what the longest chain is; five output templates.

**Out:** tracking work day by day (use a tracker); resource levelling and budgets; assigning work
to people without their say.

**Where the data lives:** the task file belongs to the project it describes. Nothing private is
kept in this repository. Level 2 can write the outputs to a Google Drive folder you choose.

### One task

`id`, `title`, `done_when`, `depends_on` (a list of ids), `owner`, `estimate`, `status`, `group`,
`notes`. The whole plan is one JSON file, so every output is drawn from the same data.

### Output templates

| Template | For |
| --- | --- |
| Workflow tree | Seeing how a goal breaks down |
| Dependency diagram, as Mermaid | Pasting into a README or a document |
| Sticky-note board, as one HTML page | A planning session: columns for ready, blocked, doing, done |
| Gantt chart | Dates and the longest chain |
| Ready list | An agent or a person asking "what do I do now?" |

### Levels

| | Holds | Done when |
| --- | --- | --- |
| Base | The task file format, three invented plans (a decision, a client project, a coding project), the five templates, and a check that finds loops and tasks with no "done when" | Each invented plan opens in all five templates from the same file |
| Level 1 | You describe the goal to your assistant with the pasted instructions. It asks up to five questions, returns the task file and the view you asked for. You correct the dependencies | A real goal becomes a plan a second person can follow without asking what comes first |
| Level 2 | A skill that keeps the task file, redraws every view when it changes, and saves outputs to a folder you choose | Changing one dependency updates all five views, and the check catches a loop |
| Level 3 | An MCP server: break down, add, link, ready, done. Hand-over to a tracker for large coding projects | An agent works a plan through the "ready" tool alone and never starts a blocked task |

## Depends on, and feeds

- **Reuses** the artifact studio for every output.
- **Feeds** the [project method](../../drafts/project-method/): stage 4 could produce its plan here.
- **Feeds** the [decision support assistant](../decision-support/README.md): a recommendation ends
  in a plan of next steps.

## Open questions

- How small is a task? Proposed: one owner, one result, done in a sitting.
- Estimates from an assistant are guesses. Show them as ranges, or leave them to the person?
- Is a sixth view needed for decisions, with options as branches?

## Approved

Not yet.
