# Projects

Showcases you can try in five minutes.

| Project | What it does | State |
| --- | --- | --- |
| [`artifact-studio/`](artifact-studio/) | **Make your first report.** Rough notes in, a one-page report out, then the same notes as a deck, a post or a page with your photo | Ready to try. Built and checked by its author. Not yet used by anyone else |
| [`agentic-process/`](agentic-process/) | **Build a tool.** A job you repeat in, a checked package out: a README, one portable `SKILL.md` and a worked example. Beat a direct build 93 to 73 in one blind pilot | Ready to try with a coding agent. Built and checked by its author with Claude. Not yet tried in Codex or by anyone else |

## How every project is laid out

`base/` is enough to try the tool. The other folders appear only when they hold something you can use.

```
a-project/
  README.md          the hook, the quick start, a sample input, the North Star, links to the levels
  AGENTS.md          instructions for AI agents
  CLAUDE.md          points Claude Code at AGENTS.md
  LICENSE
  base/              the few files a beginner needs, and examples/: one worked example per style,
                     each with its prompt, its sample input and the finished result
  level-2-files/     Advanced: what you add to make it yours, with its own README
  level-3-files/     Expert: connections for agents, with its own README
  _build/            what the project is built from. Not needed to use it
  quality-results/   the evidence: what was checked, by whom, with the raw results
```

`python3 workshop/tools/check_project.py projects/<name>` checks a folder against this.
