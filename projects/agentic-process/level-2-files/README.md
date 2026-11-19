# Level 2: install the builder skill

[`agentic-process/`](agentic-process/) is the builder as a skill in the open Agent Skills format.
Install it once in your coding agent and you no longer paste the link: say "build a tool for this
job" and describe the job.

- **Claude Code:** copy the `agentic-process` folder into `.claude/skills/` in your project, or
  into `~/.claude/skills/` for every project.
- **Codex and other agents that read Agent Skills:** put the folder where that agent loads skills.
  Not yet tried there.

The folder name must stay `agentic-process`, to match the skill's name.
