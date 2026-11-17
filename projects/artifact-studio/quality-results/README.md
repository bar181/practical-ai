# Quality results: Artifact Studio

What has been checked, who ran it, and where the raw evidence is. Nothing below is edited after
the run that made it.

**The headline:** the paste-in instructions had 22 independent runs on 16 November 2026, each in a
fresh Claude session. Every run finished its page. Across three rounds of re-tests, the points that
would change the page fell from 13 to 9 to 6; those 6 are fixed and **not re-tested**. No
assistant other than Claude has been tried, and nobody but its author has used it for real work.

## The evidence

| Check | Who ran it, and when | What it showed | Raw evidence |
| --- | --- | --- | --- |
| The paste-in instructions | 22 fresh Claude sessions, 16 November 2026: thirteen, then three rounds of three on the fixed text | Every run finished its page. About 230 points of friction in the first thirteen; the ones that would change the page fell from 13 to 9 to 6 | [`_build/examples/runs/`](../_build/examples/runs/), [`retests/`](../_build/examples/runs/retests/) |
| Ten worked examples | A fresh Claude session for each, 16 November 2026 | Each page made from its prompt alone, unedited. All ten pass the automated checks in Chrome | [`base/examples/`](../base/examples/) |
| The one-link prompt | A fresh Claude session | It fetched the instructions from the link and finished its page from them alone | [`link-run/`](../_build/examples/runs/link-run/) |
| The skill | A second agent, 16 November 2026 | It made a six-slide deck and reported ten places where the skill and its reference cards disagreed. The deck ones are fixed | [`skill-run/`](../_build/examples/runs/skill-run/) |
| The MCP server | An agent with only the server's tools | It made a page, and found the server broke when its folder was copied alone. Fixed and tested | [`mcp-run/`](../_build/examples/runs/mcp-run/) |
| The starter guide, cold | A fresh session as a first-time visitor, 16 November 2026 | 0 blocking and 12 minor points. The top screen capture was out of date and showed a claim the notes do not support; it was re-captured, and the prompt, fallback and check were fixed | [`2026-11-16-starter-run/`](../_build/examples/runs/2026-11-16-starter-run/) |

## The library report and its deck, 15 November 2026

"The studio becomes a library": what was built in the library work, how to use it, and what nobody
had checked yet, as a full page and as a short slide deck. Both are single HTML files; download one
and open it in a browser.

- [`2026-11-15-artifact-studio-library.html`](2026-11-15-artifact-studio-library.html): the report.
- [`2026-11-15-artifact-studio-library-deck.html`](2026-11-15-artifact-studio-library-deck.html): the deck.

A copy of each is in [`docs/reports/`](../../../docs/reports/).

## Not yet checked

- Any assistant other than Claude: ChatGPT, Gemini, Copilot and the others named on the README.
- A real phone, Firefox, or a screen reader. Pages were checked in Chrome and in the WebKit engine
  that Safari is built on.
- Use by anyone other than its author.
