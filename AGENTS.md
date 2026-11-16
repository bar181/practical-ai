# For agents working in this repository

Practical AI is a set of tools a person can use with an AI assistant the same day. Each has a
Beginner level a student can run in any chat assistant, and Advanced levels with skills and
connectors. Each tool has a plan in `plans/` and, once started, a folder in `drafts/` or `projects/`.

| You were asked to | Go to |
| --- | --- |
| Make a page, a slide deck or a social post | [`drafts/artifact-studio/base/AGENTS.md`](drafts/artifact-studio/base/AGENTS.md): the path from a request to a finished file |
| Understand what the repository holds | [`README.md`](README.md) |
| Decide what to build next | [`docs/practical-ai-priorities.md`](docs/practical-ai-priorities.md): the owner's priorities. The inventory and research behind it are in [`docs/tool-inventory.md`](docs/tool-inventory.md) |
| Start a new tool, or continue one | [`drafts/project-method/AGENTS.md`](drafts/project-method/AGENTS.md) and the [`project-builder`](skills/project-builder/) skill |
| Write or update a plan for a tool | [`skills/plan-writer/`](skills/plan-writer/) |
| Check what already exists before building | [`skills/landscape-review/`](skills/landscape-review/) |
| See how the work has been reviewed | [`docs/SELF-REVIEW.md`](docs/SELF-REVIEW.md) |

## Rules for this repository

- Invent no facts. Where content is missing, leave a visible gap and say so.
- Examples use invented data and say so. No real company or person is named.
- Every status line says who has and has not tried the thing. Keep that true when you change it.
- Generated files say so at the top. Change the source and run the build, not the output.
- Before you say a tool is done, run `python3 tools/gates.py drafts/<tool>`. It must end with "All gates that ran passed".
- Retired work moves to [`plans/archive/`](plans/archive/) with a line saying what replaced it. Do not delete it.
