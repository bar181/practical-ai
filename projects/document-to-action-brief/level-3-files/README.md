# Level 3: hands-off (planned, not built)

**Status: a design, not a working tool.** The repository's rule is to build Level 3 only when real
use shows a manual step that keeps coming back. Nothing on this page has been built or tested.

Level 1 answers one document when you paste it. Level 3 notices the document arrived, briefs it,
keeps track of what it asks of you, and reminds you in time, while a person still checks and
decides. It is the same brief, run on a schedule with your apps connected.

## What it would include

| Part | What it does | Where the idea comes from |
| --- | --- | --- |
| **1. Watch** | A scheduled task checks an inbox label (for example "To brief") or a shared folder, once a day or once an hour | Claude and ChatGPT both run scheduled tasks that can use connected apps such as Gmail and Google Drive |
| **2. Brief** | Runs the Level 2 skill, with your house rules, on each new document | The skill in `base/` |
| **3. Register** | Writes each action and date as a row in a sheet: what, by when, who owns it, the exact words, the document, status | Contract tools keep an obligations register: AI drafts the obligations, and every obligation has an owner |
| **4. Review lane** | Clear rows go in as drafts. Anything unclear, any penalty, any date that cannot be worked out, and any unreadable file goes to a person first. Nothing is marked done by the AI | Document-processing practice: route uncertain or high-stakes items to a person, automate the clear ones |
| **5. Remind** | Before each deadline, drafts a reminder email or a calendar hold for a person to send or accept | Connectors can draft in Gmail and create calendar events; sending stays with you |
| **6. Learn** | Each correction a person makes is recorded once and read before the next brief, so the same mistake is not repeated | Practical AI's [Learnings database](../../learnings-database/) |

**Handed off, not rebuilt:** a contract that needs a risk review goes to a lawyer or a legal
review tool, such as Anthropic's open-source Legal plugin. This tool stays the business person's
brief.

## What it would need

- A paid plan with scheduled tasks and connectors (Claude or ChatGPT), and the apps connected with
  the smallest permissions that work: read the inbox label or folder, write to one sheet, draft
  only.
- One sheet for the register. Storage stays with you, not in this repository.
- One person who owns the review lane.

## Risks, and how the design handles them

| Risk | Handled by |
| --- | --- |
| A wrong action or date goes into the register | Every row keeps its exact words. Penalties, unclear lines and unworked dates always go to a person first |
| A document is sent to an app it should not reach | Only an inbox label or a folder you choose is read. Your workplace's rules decide which chatbot may see which documents |
| The AI acts for you | It drafts. It never sends, signs, accepts, pays or replies |

## Sources, checked 17 November 2026

- Claude scheduled tasks with connectors: [Claude Help Center](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- ChatGPT scheduled tasks and connectors: [OpenAI Help Center](https://help.openai.com/en/articles/10291617-connectors-in-chatgpt)
- Skills in ChatGPT follow the open Agent Skills format: [OpenAI Help Center](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- AI-drafted obligation records, tested on samples first: [Ironclad support](https://support.ironcladapp.com/hc/en-us/articles/42037412989975-Extract-Obligations-with-Ironclad-AI)
- Every obligation has an owner: [Gatekeeper](https://www.gatekeeperhq.com/blog/how-to-manage-contract-obligations-compliance)
- Review lanes for uncertain items: [Parseur on human-in-the-loop workflows](https://parseur.com/blog/hitl-best-practices)
- Anthropic's Legal plugin for contract review: [knowledge-work-plugins on GitHub](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal)
