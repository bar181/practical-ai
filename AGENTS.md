# For agents working in this repository

Practical AI is a set of tools a person can use with an AI assistant the same day. The tool is the
product. Each has a Beginner level, the simplest version that works, started in minutes in any chat
assistant; an Advanced level that makes it repeatable with skills and connectors; and an Expert
level that is connected and automated. Levels describe setup and automation, not audience. Each
has a short explainer: what it does, how to start, what goes in and comes out, and what to check, with one worked example. It can live in the README. Teaching is not the product. Reuse first: use an existing capability, wrap it,
or build only the missing piece. Reuse Anthropic's own skills and plugins wherever they fit. Each tool has a plan in `workshop/plans/`. A showcase you can try is in `projects/`, and work in progress, including Agentic Process version 2, is in `workshop/drafts/`.

| You were asked to | Go to |
| --- | --- |
| Make a page, a slide deck or a social post | [`projects/artifact-studio/AGENTS.md`](projects/artifact-studio/AGENTS.md): the path from a request to a finished file |
| Understand what the repository holds | [`README.md`](README.md) |
| Decide what to build next | [`docs/practical-ai-priorities.md`](docs/practical-ai-priorities.md): the owner's priorities. The inventory and research behind it are in [`docs/tool-inventory.md`](docs/tool-inventory.md) |
| Start a new tool, or continue one | [Agentic Process](workshop/drafts/agentic-process/README.md): the [nine-step method](workshop/drafts/agentic-process/PROCESS.md), the tool template and the builder skill. Each tool is a README, one portable `SKILL.md` and a worked example |
| Write or update a plan for a tool | [`workshop/skills/plan-writer/`](workshop/skills/plan-writer/) |
| Check what already exists before building | [`workshop/skills/landscape-review/`](workshop/skills/landscape-review/) |
| See how the work has been reviewed | [`docs/SELF-REVIEW.md`](docs/SELF-REVIEW.md) |

## Rules for this repository

- Invent no facts. Where content is missing, leave a visible gap and say so.
- Examples use invented data and say so. No real company or person is named.
- Every status line says who has and has not tried the thing. Keep that true when you change it.
- Generated files say so at the top. Change the source and run the build, not the output.
- Before you say a showcase is ready, run `python3 workshop/tools/check_project.py projects/<tool>` and `python3 workshop/tools/check_links.py .`, and rebuild it from its `_build/` folder.
- Retired work moves to [`workshop/plans/archive/`](workshop/plans/archive/) with a line saying what replaced it. Do not delete it.
