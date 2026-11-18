# Quality results: Document to action brief

What has been checked, who ran it, and where the raw evidence is. Nothing below is edited after
the run that made it. Every company, document and amount in the tests is invented.

**The headline:** nine runs in fresh Claude sessions, 17 and 18 November 2026, each given only what a
user would paste. Every run that had the instructions passed. A script found every quote word for
word in its document (136 of 136 on 18 November), no gap was filled with a guess, and the tender
runs caught a real mistake in the document. On 18 November the house rules file was tried for the first time, and the brief applied its rules.
No chatbot other than Claude has been tried. As of 18 November 2026, users are testing it; their
results are not in yet.

## How the runs are checked

- **Fresh sessions.** Each run is a new Claude session playing the chatbot. It sees only the
  user's message, plus `SKILL.md` or the house rules where a user would have saved them.
- **Quotes, by script.** [`../_build/check_quotes.py`](../_build/check_quotes.py) looks for every
  quote of four words or more in the document, character for character. It is the person's Ctrl+F
  check, done by a script.
- **The answer key.** The try-it runs are graded against
  [the answer key](../base/examples/answer-key.md), written from the notice before any run.
- **Friction.** After each reply, the session steps out of role and writes where it had to guess.

## 18 November 2026: the re-test

| Check | What it showed | Quotes found | Raw evidence |
| --- | --- | --- | --- |
| The try-it prompt, notice A | Passed the answer key: three actions, both dates, every penalty in the top lines, and the "standard plan" line under open questions, not facts. Friction: five tables with full quotes run to several phone screens | 28 of 28 | [`2026-11-18-try-it-prompt/`](2026-11-18-try-it-prompt/) |
| The skill, notice B (no date, schedule missing), for a boss | Re-tests the 17 November fixes. A warning up top, four dates marked "cannot be worked out", no prices made up, and the boss's three-line summary. Friction: the boss summary overrides "two sentences" without saying so | 23 of 23 | [`2026-11-18-skill-missing-details/`](2026-11-18-skill-missing-details/) |
| The skill, a tender, for a business partner | Re-tests the 17 November fixes. "Can we bid", and again caught that the three "Saturdays" are Sundays. Friction: a penalty not tied to an action, and the 25-word quote limit | 42 of 42 | [`2026-11-18-skill-tender/`](2026-11-18-skill-tender/) |
| The skill, with no document | Replied with the skill's request for the document, word for word, and nothing else | None to check | [`2026-11-18-skill-no-document/`](2026-11-18-skill-no-document/) |
| Level 2: the skill with a filled-in house rules file | First test of house rules. The brief was written for the manager the file names, put the $35 penalty in bold at the top as the file asks, applied the "payment terms go to the bookkeeper" rule, and named who answers each question | 41 of 41 | [`2026-11-18-house-rules/`](2026-11-18-house-rules/) |
| The one-line quick start | **Not a fair test.** The test session's web access refused the link, so it never saw the instructions. It said so in its first line, then wrote a brief of its own that gave advice the skill forbids. Lesson: if a chatbot cannot open the link, use the try-it prompt | 2 of 2 | [`2026-11-18-one-line-link/`](2026-11-18-one-line-link/) |

## 17 November 2026: the first runs

| Check | Who ran it | What it showed | Raw evidence |
| --- | --- | --- | --- |
| The try-it prompt, notice A | A fresh Claude session, with only the prompt | Passed the answer key. It also caught that "Invoices are now due 14 days" conflicts with the 1 December start date | [`2026-11-17-try-it-prompt/`](2026-11-17-try-it-prompt/) |
| The skill, notice B, for a boss | A fresh Claude session with `SKILL.md` as a skill | Passed. Four rule clashes, fixed in `SKILL.md` afterwards and re-tested on 18 November | [`2026-11-17-skill-missing-details/`](2026-11-17-skill-missing-details/) |
| The skill, a tender, for a business partner | A fresh Claude session with `SKILL.md` | Passed, and caught the Sunday dates: a real mistake by the author of the practice tender, left in since. Three fixes made afterwards, re-tested on 18 November | [`2026-11-17-skill-tender/`](2026-11-17-skill-tender/) |
| The earlier version, blind pilot | Agentic Process's builder pilot, 16 November 2026 | Built with Agentic Process: 93/100, 0 corrections. Direct build: 73/100, 2 corrections | [Agentic Process evidence](../../agentic-process/quality-results/README.md) |

## Not yet checked

- Any chatbot other than Claude.
- The one-line quick start, in a chatbot that can open links.
- A real document from a real business. Users are testing this now; no results yet.
- Level 3, which is a design and is not built.

## What the runs say to improve next

- **Length on a phone.** Two runs said five tables of full quotes run to several phone screens.
- **One page is a stretch.** The prompt asks for a one-page brief; the 18 November try-it reply runs
  to about 900 words.
- **Two small rule gaps.** The boss summary and "two sentences at most" clash. A penalty not tied to
  an action has no clear home.

`SKILL.md` was not changed after these runs, so the results above describe the version in `base/`.
