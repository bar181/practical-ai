# Level 2: save it once

Level 1 is a link or a paste in each chat. Level 2 saves the instructions where you work, so every
chat can log a lesson and bring back the rules. Worth it once you log more than once a week.

| Where you work | Do this | Saving a row |
| --- | --- | --- |
| **Claude, as a plugin** | Add [`claude-plugin/learnings-database/`](claude-plugin/learnings-database/) as a plugin. In Claude Code: `claude plugin install` from a marketplace that lists this folder, or `claude --plugin-dir` with its path. It adds the skill and three commands: `/log`, `/before-i-start` and `/weekly-review` | In a folder it can write to, it adds the row after your yes; otherwise it gives you the line |
| **Claude, as a skill** | Zip [`claude-skill/learnings-database/`](claude-skill/learnings-database/) and upload it in Claude's skill settings, or copy the folder into a coding agent's skills folder | The same |
| **Claude, as a project** | Paste the Option A text from the [ChatGPT steps](chatgpt-project/instructions.md) into the project's instructions, and add your log as a project file | You paste the line it gives you |
| **ChatGPT** | Follow [`chatgpt-project/instructions.md`](chatgpt-project/instructions.md) | You paste the line, or it adds it to a Google Sheet |
| **A Google Sheet as the log** | Follow [`google-drive.md`](google-drive.md) | Depends on the chatbot and plan: see the table there |
| **A coding agent or desktop app with a folder** | Keep `learnings.csv` in the folder and give it the skill. It adds rows after your yes | Appended to the file after your yes |

**Status.** The plugin passes `claude plugin validate` (19 November 2026). Nobody has installed it,
or the skill, in a real account yet. The ChatGPT and Google Sheets routes have not been tried.

**A gist.** [`gist/learnings-log.md`](gist/learnings-log.md) is a draft one-page version of the
idea, with a short paste-in that covers logging, for sharing as a public gist. A person reviews
and publishes it.

Generated folders (`claude-plugin/`, `claude-skill/`) are rebuilt by `_build/build.py` from
`base/`. Change `base/`, then rebuild.
