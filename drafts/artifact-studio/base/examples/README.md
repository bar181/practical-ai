# Worked examples

Six requests, each with the notes that came with it, what the studio picked, and what came back. Read one to see what to expect. Run one to test the studio.

**Think of them as** the photographs on a menu. They show what the dish looks like when it is made properly.

| Example | What was picked | Output | Tested in a fresh chat |
| --- | --- | --- | --- |
| [A deck for a decision](01-briefing-deck/request.md) | Briefing deck | [`output.html`](01-briefing-deck/output.html) | Not yet |
| [A deck that teaches one skill](02-workshop-deck/request.md) | Workshop deck | [`output.html`](02-workshop-deck/output.html) | Not yet |
| [A week of social pictures](03-social-set/request.md) | Square post | [`square.svg`](03-social-set/square.svg), [`carousel-1.svg`](03-social-set/carousel-1.svg), [`carousel-2.svg`](03-social-set/carousel-2.svg), [`carousel-3.svg`](03-social-set/carousel-3.svg) | Not yet |
| [A one-page report](04-one-page-report/request.md) | One-page report in the analyst voice | [`output.html`](04-one-page-report/output.html) | Not yet |
| [A palette from one brand colour](05-brand-palette/request.md) | No template: one rule | [`output.md`](05-brand-palette/output.md) | Not yet |
| [Keeping a design you like](06-inspiration-card/request.md) | No template: one rule | [`output.md`](06-inspiration-card/output.md) | Not yet |

## How to test one

1. Open the example's `request.md`.
2. Give a fresh assistant the request and the notes. Attach the starter if the example names one. At level 1, paste [`AI-INSTRUCTIONS.md`](../../level-1/AI-INSTRUCTIONS.md) first.
3. Score what comes back against "What a good result must have", one point for each line.
4. Change "Not yet" in the table above to the score and the date, in [`make_examples.py`](make_examples.py), which writes this file.

## What these are and are not

- Every business and figure is invented.
- The outputs were made by the assistant that built this repository, following the skill, with the content typed into [`make_examples.py`](make_examples.py). **No fresh assistant has been given these requests yet.** That is what the last column is for.
- They are rebuilt from the starters each time the script runs, so they cannot fall out of step with the library.
- The same six requests are the skill's test cases, in [`skills/artifact-studio/evals/evals.json`](../../../../skills/artifact-studio/evals/evals.json).
