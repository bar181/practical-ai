# Quality results: Document to action brief

What has been checked, who ran it, and where the raw evidence is. Nothing below is edited after
the run that made it. Every company, document and amount in the tests is invented.

**The headline:** three fresh Claude sessions on 17 November 2026, each given only what a user
would paste. All three briefs passed: every quote was found word for word in its document, no gap
was filled with a guess, and the tender run caught a real mistake in its document. No chatbot other
than Claude has been tried, and nobody but its author has used it for real work.

## The evidence

| Check | Who ran it, and when | What it showed | Raw evidence |
| --- | --- | --- | --- |
| The try-it prompt, notice A | A fresh Claude session as a chatbot, 17 November 2026, with only the prompt | Passed the [answer key](../base/examples/answer-key.md): three actions, both dates, the $35 penalty at the top, and the "standard plan" line under open questions, not facts. It also caught that "Invoices are now due 14 days" conflicts with the 1 December start date. Friction: whether "please" counts as a must, and the brief is long for one phone screen | [`2026-11-17-try-it-prompt/`](2026-11-17-try-it-prompt/) |
| The skill, notice B (no date, schedule missing), for a boss | A fresh Claude session with `SKILL.md` as a saved skill, 17 November 2026 | A warning up top. Both dates marked "cannot be worked out" with who can supply them; no prices made up; the ambiguous line given both readings. Friction: four rule clashes, fixed in `SKILL.md` afterwards and **not re-tested** | [`2026-11-17-skill-missing-details/`](2026-11-17-skill-missing-details/) |
| The skill, a tender, for a business partner | A fresh Claude session with `SKILL.md`, 17 November 2026 | The "Can we bid" section with a five-item checklist, both deadlines and both penalties up top. It caught that the tender's three "Saturdays" are all Sundays: a real mistake by the author of the practice tender, left in since. Friction: five points, three fixed in `SKILL.md` and **not re-tested** | [`2026-11-17-skill-tender/`](2026-11-17-skill-tender/) |
| The earlier version, blind pilot | Agentic Process's builder pilot, 16 November 2026: one build task, one unseen notice, one blind reviewer | The tool built with Agentic Process scored 93/100 and needed 0 corrections; the direct build scored 73/100 and needed 2 | [Agentic Process evidence](../../agentic-process/quality-results/README.md) |

## Not yet checked

- Any chatbot other than Claude, and the one-line link quick start.
- The house rules file in Level 2.
- A real document from a real business, used by someone other than the author.
- Level 3, which is a design and is not built.
