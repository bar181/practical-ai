# Quality results: Practical AI guide

**22 November 2026: in use.** Bradley reports that people other than the author now use this
project, from business owners to agentic developers. Their results are not recorded here yet. The
checks below were run by the author and by fresh Claude sessions; the dates on them still hold.

What was checked, by whom, and what was not.

## 22 November 2026: the index and the skill

Checked by Claude, the author:

- `llms.txt` is generated from every project's README by `_build/build_index.py`. Every one of the
  12 projects (11 on 22 November, then Research brief) is listed, with links to its README, its AGENTS.md and its skill. The script fails if
  a project is missing, and `--check` fails if the file is out of date.
- Every link in the index points at a file that exists in the repository.
- The skill was followed on three invented questions, recorded in
  [`../base/examples/office-hours-session.md`](../base/examples/office-hours-session.md): a job
  matched to a tool, a price question declined, and a hidden instruction ignored. All three passed.

Not checked:

- No person has used the guide, and no fresh agent has followed the skill without context.
- The Level 2 setups (Claude Project, custom GPT, Gem, GitMCP) were not tried.
- The Level 3 chat window is a plan.
