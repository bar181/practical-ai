# Connections hub: North Star

Stages 1 to 3 of the [project method](../../drafts/agentic-process/PROCESS.md). Written
15 November 2026. **Not yet approved.** Complexity: intermediate to advanced. The owner's working
name is "connection and understanding master".

**Think of it as** the mail room of a small firm. Things arrive from everywhere: a meeting, an
email, a web page. The mail room opens each one, works out what it is, stamps it with a date and
a label, and sends it to the right shelf. It does not keep the mail itself.

**North Star:** something useful said in a meeting, an email or a web page on Monday can be found
by label on Friday, without anyone having filed it by hand.

## Understand

| | |
| --- | --- |
| Who it is for | As a consultant or owner, I want what comes in through meetings, email and the web to be read, understood and logged with the right flags, so that I can find it later and my other tools can use it |
| The one job | Read from a source, decide what is worth keeping, and write it as records to the memory system or the learnings database |
| The finished thing is | A product: a short list of supported sources, one intake step for each, and a review queue |

**What it is not.** It is not a store. It keeps nothing itself: records go to the
[core memory system](../core-memory/README.md) or the
[learnings database](../learning-system/NORTH-STAR.md). It is not a wiki builder, and it does not
copy whole transcripts or mailboxes anywhere.

## Research: what already exists

| Source | Checked | What we take from it |
| --- | --- | --- |
| [Layer3 Labs: Granola MCP setup guide](https://www.layer3labs.io/guides/granola-mcp) | 15 Nov 2026 | Granola has an official MCP server with sign-in. It suits asking questions in a chat. It is not built for unattended background runs, where its API and webhooks are the route |
| [ContextBolt: Granola MCP](https://contextbolt.com/blog/granola-mcp/) | 15 Nov 2026 | What you can read depends on the plan: full transcripts are a paid feature, and they can be too large to send in one piece |
| [Spinach: MCP and meeting transcripts](https://www.spinach.ai/blog/what-is-mcp-server-meeting-transcripts-2), a vendor's page | 15 Nov 2026 | It says Zoom offers no MCP route of its own. **The connector directory below contradicts this**, which is the lesson: check the directory on the day, and treat a vendor's account of its rivals with care |
| The assistant's own connector directory | 15 Nov 2026 | Listed today: Gmail, Google Drive, Google Sheets, Granola, a Zoom connector that searches meetings and recordings, Grain, and Supabase. Seen in the directory, not tested |
| [Circleback: MCP meeting tools](https://circleback.ai/blog/what-is-mcp-meeting-tool), a vendor's page | 15 Nov 2026 | Several meeting-notes products now have MCP servers. Answers improve when meetings and email are searched together |
| [A walkthrough of stacking connectors](https://openclawdatabase.com/news/videos/2026-06-25-granola-mcp-connector-claude-chatgpt/index.md) | 15 Nov 2026 | Meeting notes beside drive, email and calendar connectors already give an assistant a wide view. The same page warns that this is broad access to private data |

**Decision:** use what exists, and build only the intake step. Level 1 pastes an export. Level 2
uses the connectors a person already has. Connecting is solved by others.
What is missing is the step between reading a source and having a clean, labelled record.

## Scope

**In:** four sources to start (a meeting transcript or notes, an email thread, a web page, a file
you drop in); an intake step that extracts decisions, facts, commitments, people and dates; labels
and flags applied from the fixed lists; a review queue where a person accepts or rejects before
anything is filed; a log of what was read and when.

**Out:** storing source material; reading anything a person has not pointed it at; sending,
replying or posting; unattended ingestion of a whole mailbox.

**Where the data lives:** nowhere here. Sources stay where they are. Records go to a store the
person owns. The repository holds invented examples only.

### The intake step

| Step | What happens |
| --- | --- |
| 1. Read | One source the person points at, through a connector or a pasted export |
| 2. Classify | What is it: a meeting, a thread, a page, a file. Who and when |
| 3. Extract | Candidate records: a decision, a fact, a commitment, a learning. Each with the sentence it came from |
| 4. Flag | Labels, keywords, topics, and whether it looks sensitive |
| 5. Review | The person accepts, edits or rejects each candidate |
| 6. File | Accepted records go to memory or to learnings, with a pointer back to the source |

### Levels

Level 1 is the Beginner level: a student can run it in any chat assistant with nothing installed. Levels 2 and 3 are the Advanced levels, with skills and connectors, for someone who works with agents every day.

| | Holds | Done when |
| --- | --- | --- |
| Base | The intake step, four invented sources with the records each should produce, and the rules for what is worth keeping | A reader can predict the records for a fifth example |
| Level 1, Beginner | You paste a transcript, a thread or a page with the instructions. The assistant returns candidate records as rows. You delete the ones you do not want and paste the rest into your sheet | Five real sources produce records you would have filed yourself, and none you would not |
| Level 2, Advanced | A skill that reads through the connectors you already have, shows the review queue, and files what you accept | A meeting from this week is filed in under two minutes, and nothing is filed without your say |
| Level 3, Expert | Scheduled intake from sources you name, through their APIs or webhooks, into a queue that waits for review | A week of meetings is waiting in the queue on Friday, with nothing filed unreviewed |

## Depends on, and feeds

- **Needs** the [learnings database](../learning-system/NORTH-STAR.md) and the
  [core memory system](../core-memory/README.md) to exist first. Without a shelf, the mail room has
  nowhere to send anything.
- **Works beside** the [meeting notes to actions](../meeting-notes-to-actions/) plan. This page first proposed absorbing it. Research on 15 November 2026 found meeting notes to actions is one of the most wanted simple tools, so it stays a tool of its own and the hub files what it produces.
- **Feeds** the weekly brief, the inbox summary and decision support.

## Open questions

- Which connector for each source, and on which plan? This is the research for stage 2 proper, and
  it must be redone when building, because these products change monthly.
- How much of the review can be trusted to rules? Start with none.
- Consent: a meeting has other people in it. What is the rule for keeping what they said?

## Approved

Not yet.
