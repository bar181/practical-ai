# Level 2: save the guide, or connect it to your coding tool

**The core idea:** set it up once, so every question gets office hours without pasting anything.

**Think of it as** saving the teaching assistant's number in your phone instead of looking it up
each time.

**Status, 22 November 2026:** written from each product's own help pages. Not yet tried by anyone.

## In a chatbot (10 minutes)

| Chatbot | Do this |
| --- | --- |
| **Claude** | Create a Project named "Practical AI office hours". Paste [`../base/SKILL.md`](../base/SKILL.md) into the project instructions, and add [`llms.txt`](../../../llms.txt) as a project file |
| **ChatGPT** | Create a custom GPT. Paste the skill into Instructions and upload `llms.txt` under Knowledge |
| **Gemini** | Create a Gem. Paste the skill into its instructions and add `llms.txt` as a file |

Then ask your question in that project, GPT or Gem. If an answer names a file the chatbot cannot
open, open the link yourself; every link in the index is to a plain text file.

Saving the index as a file means it can go out of date. Replace it when the repository changes, or
keep the skill's first step, which reads the live index.

## In a coding tool (5 minutes)

Coding agents such as Claude Code can read the repository directly:

- **Clone it.** `git clone https://github.com/bar181/practical-ai`, then ask your agent. It starts
  at `AGENTS.md`, which routes each task to the right project.
- **Or connect it without cloning,** through GitMCP, which serves any public GitHub repository to
  an MCP client: add `https://gitmcp.io/bar181/practical-ai` as an MCP server in your tool's
  settings. Nothing to build or host.

## Check it worked

Ask the three questions in [`../base/examples/office-hours-session.md`](../base/examples/office-hours-session.md).
Each answer should name a file, the price question should be declined, and the hidden instruction
should be ignored.

Part of the [Practical AI guide](../README.md).
