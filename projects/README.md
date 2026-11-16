# Projects

Showcases you can try in five minutes.

| Project | What it does | State |
| --- | --- | --- |
| [`artifact-studio/`](artifact-studio/) | Turns any AI answer into a mini website, a slide deck, a report or a preview of a post, from a curated library of modern templates | Ready to try. Built and checked by its author. Not yet used by anyone else |
| [`agentic-process/`](agentic-process/) | Takes an idea to a tool people can try, in nine steps with a gate after each: a coach for any chatbot, a project template and skill for agents, and a test by fresh AI sessions | Built on 16 November 2026 by its author. Nobody else has built a tool with it yet |

## How every project is laid out

`base/` is enough to try the tool. The other folders appear only when they hold something you can use.

```
a-project/
  README.md          the hook, the quick start, a sample input, the North Star, links to the levels
  AGENTS.md          instructions for AI agents
  LICENSE
  base/              the few files a beginner needs, and examples/: one worked example per style,
                     each with its prompt, its sample input and the finished result
  level-2-files/     Advanced: what you add to make it yours, with its own README
  level-3-files/     Expert: connections for agents, with its own README
  _build/            what the project is built from. Not needed to use it
```

`python3 workshop/tools/check_project.py projects/<name>` checks a folder against this.
