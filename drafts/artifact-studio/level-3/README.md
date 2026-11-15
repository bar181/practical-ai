# Level 3: connected

Level 2, plus connections, so content comes in and pages go out without copying and pasting.

**One connection is built: an MCP server.** It has been tested with a client on the machine that built it, and not yet inside a desktop assistant or over the internet. The other slots are listed so that an addition has a place to go and a bar to clear. The base and levels 1 and 2 need none of this.

**Think of it as** plumbing. The kitchen works with buckets. Pipes save carrying, and a badly
fitted pipe floods the floor, so each one is tested before it is trusted.

## Built

| Addition | What it does | Where | Status |
| --- | --- | --- | --- |
| The studio as tools | Lets an assistant browse the library, get a recommendation, read reference code and rules, and file a note about a design you like | [`mcp/`](mcp/) | Works over stdio and local HTTP with a test client, 2026-11-15. Not yet tried in a desktop assistant or from the web |

## Slots not yet built

| Addition | What it would do | What it depends on | Status |
| --- | --- | --- | --- |
| Content in | Read the notes, documents or spreadsheet from where they already live, in place of an attachment | A connector to your file store | Not built |
| Brand in | Read colours, type and logo from your design system or design tool, in place of the preferences file | A connector to that tool, or a design system the assistant can read | Not built |
| Page out | Put the finished page at a web address | A hosting route. The options are reviewed under "Publishing a website", and no route has been walked | Not built |
| One-step install | Package the skill, the preferences file and a short command as a plugin, so a team installs everything at once | An assistant that supports plugins | Not built |
| On a schedule | Rebuild a page from fresh content each week and wait for approval | Scheduled tasks in the assistant, and "content in" | Not built |
| Richer media | Narration, video or an avatar on the page | Outside services, reviewed under the short video guide and training explainer | Not built |

## The bar an addition must clear

An addition moves out of this table and into a folder here only when all of these are true.

1. It has been walked end to end once, on real content, and the date is written down.
2. Its folder says exactly what it depends on, what it costs if anything, and what it is allowed
   to do.
3. Anything that sends, posts or publishes stops and waits for a person.
4. Taking it away leaves level 2 working as before.

## What stays manual at every level

Checking numbers, names and quotes. Answering the gaps the assistant lists. Deciding what is
published.

## Which one first

That depends on where the copying and pasting hurts most. "Page out" is the usual answer, because
a page nobody can open is not finished, and it is the one slot that another tool in this
repository already covers in research.
