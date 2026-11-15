# Sources for the method

What was read on 15 November 2026 when the method was revised, and the one thing taken from each.
Nothing here is quoted. Where a page reports another organisation's guidance, the row says so.

| Source | What it describes | What the method takes |
| --- | --- | --- |
| [Spotdev: how to work with AI coding agents](https://www.spotdev.co.uk/blog/working-method-for-ai-coding-agents) | A routine of explore, plan, test and review, citing the guidance published for the main coding agents | Explore before changing anything. A plan names what changes, in what order, and the test that proves it |
| [Ready Solutions: agentic development starter guide](https://readysolutions.ai/blog/2026-04-08-agentic-development-starter-guide/) | A plan, audit, implement, verify cycle | Audit the plan before building. Move on only when a deterministic gate passes |
| [Plannotator: how to plan with AI coding agents](https://docs.plannotator.ai/learn/planning/how-to-plan-with-ai-coding-agents) | A nine-step planning loop that keeps revising as evidence arrives | Plan the decisions, not every keystroke. Verify with fresh evidence and a fresh reviewer |
| [Augment Code: spec-driven development](https://www.augmentcode.com/guides/ai-coding-agents-for-spec-driven-development-automation) | The specify, plan, tasks, implement sequence of the open-source Spec Kit | Each phase writes a file that feeds the next, with a person checking at each boundary |
| [Verdent: spec driven development](https://www.verdent.ai/guides/coding/spec-driven-development) | Where the specification approach earns its cost and where it does not | A specification describes behaviour. If it restates the plan, the phases are not doing separate jobs |
| [A spec-driven skill with adaptive depth](https://www.skills.lc/adeonir/agent-skills/adeonir-agent-skills-skills-development-spec-driven-skill-md) | A pipeline where planning steps are skipped for small scope | "How much method a tool needs" |
| [Anthropic: effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Agents that work across many sessions, each starting with no memory | Carry the work in files. Read through summaries of it, not the article itself, in this pass |
| [Agent Patterns: goal monitoring and progress tracking](https://agentpatterns.ai/agent-design/goal-monitoring-progress-tracking/) | A feature list as an objective measure of done, and a progress file on disk | `gates.json` as the measure of done, and `docs/progress.md` |
| [Mejba: the long-running agent harness](https://www.mejba.me/blog/anthropic-long-running-agent-harness) | The harness as a set of files, started small | Level 2 is a skill, a gate list and a progress note. No orchestration code |

## Not adopted

- **Running several agents at once.** Nothing here needs it yet, and it adds merge problems.
- **A specification as the source the code is generated from.** These tools are mostly documents,
  templates and small scripts. A North Star page and gates are enough.
- **Any one vendor's commands.** The method is files and plain commands, so it works with any
  assistant that can read and run them.
