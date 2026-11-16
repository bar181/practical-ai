# Projects

Showcases you can try in five minutes.

| Project | What it does | State |
| --- | --- | --- |
| [`artifact-studio/`](artifact-studio/) | Turns any AI answer into a slide deck, a report or a web page, from a curated library of modern templates | Ready to try. Built and checked by its author. Not yet used by anyone else |

## How every project is laid out

`base/` is enough to try the tool. The other folders appear only when they hold something you can use.

```
a-project/
  README.md          the hook, the quick start, a sample input, the North Star, links to the levels
  AGENTS.md          instructions for AI agents
  LICENSE
  base/              the few files a beginner needs
  level-2-files/     Advanced: what you add to make it yours, with its own README
  level-3-files/     Expert: connections for agents, with its own README
  _build/            what the project is built from. Not needed to use it
```

`python3 tools/check_project.py projects/<name>` checks a folder against this.
