# Source and link verifier: North Star

Stages 1 to 3 of the [project method](../../drafts/project-method/base/METHOD.md). Written
15 November 2026. **Not yet approved.** Proposed by the assistant, not asked for by the owner.
Complexity: beginner to intermediate.

**Think of it as** a fact-checker's desk. Before anything goes out, each reference is opened, read,
and marked: it says this, it does not say this, or the page has gone.

**North Star:** every link in something you send has been opened on a known date and supports the
sentence it sits beside.

## Understand

| | |
| --- | --- |
| Who it is for | As someone who sends research, briefs or recommendations, I want every source checked, so that I am never caught citing a page that is gone or says something else |
| The one job | For each claim and its link: does the link open, and does the page support the claim? |
| The finished thing is | A product: a check that returns a table, and a mark to put beside each source |

## Research: what already exists

| Source | Checked | What we take from it |
| --- | --- | --- |
| [Spotdev: working with coding agents](https://www.spotdev.co.uk/blog/working-method-for-ai-coding-agents) | 15 Nov 2026 | A page that states when it was last checked is easier to trust. Put the date beside the claim |
| `tools/check_links.py` in this repository | 15 Nov 2026 | Links inside the repository are already checked as a gate. Links to the outside are not |
| Link checkers and citation managers | Common tools, not reviewed yet | Whether a link opens is solved. Whether the page supports the claim is the part worth building |

**Decision:** build on top, and check the landscape properly first. Researched lightly: stage 2
proper is still to do. It may turn out to be a feature of decision support and the weekly brief,
not a tool of its own.

## Scope

**In:** finding every claim with a link in a document; opening each link; four results (supports,
partly supports, does not support, gone); the date checked; a table and an in-place mark.

**Out:** judging whether a source is reputable; checking claims that have no link; paywalled pages
it cannot read, which are marked "could not read" and never guessed.

**Where the data lives:** nowhere. It reads a document and returns a table.

| | Holds | Done when |
| --- | --- | --- |
| Base | The four results, three invented documents with known good and bad links, the table format | The check finds every planted bad link |
| Level 1 | Paste the instructions and a document into an assistant that can browse. Get the table | A real brief with ten links is checked in five minutes |
| Level 2 | A skill, and a gate any project can add to its `gates.json` for outside links | A document with a dead link cannot pass |

## Open questions

- Is this a tool, or a step inside two other tools? Decide after stage 2.
- How is "partly supports" kept from becoming the answer to everything?

## Approved

Not yet.
