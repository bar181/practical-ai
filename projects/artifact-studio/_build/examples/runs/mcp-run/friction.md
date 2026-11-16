# Friction: building a page from the MCP tools alone

## The short version

Started exactly as instructed (`python3 runs/mcp-run/mcp/server.py`), **every tool that
returns code or rules fails**. Only the tools that answer from `index.json` work. An assistant
connected to this server as it sits in this folder can choose a template and then cannot get a
single line of it.

- `get_rules`: all 7 values fail. I never saw the build rules, the checklist, or the recipe, voice
  and look cards. This did not get fixed at any point in the run.
- `get_template(part='source')`, `get_template(part='starter')`, `get_component`: all fail.

Cause, read from the tracebacks and the first 40 lines of `server.py`: the server works out its
project folder as two levels above itself and then joins the paths in the index, which all begin
`level-3-files/mcp/library/...`, and the rules, which live in `level-2-files/artifact-studio/...`.
So it only works if (a) its parent folder is literally named `level-3-files`, and (b) a
`level-2-files` folder sits beside it. Here the parent is `mcp-run` and there is no `level-2-files`.
The README mentions (b) ("keep the two folders together") but says nothing about (a). Neither path
can be changed by a flag or an environment variable.

### What I did about it, so the test could still say something

I did not edit the server and did not read the library from disk. Inside my own run folder I made
`_layout/level-3-files`, a link back to `runs/mcp-run`, and started the **same server file**
through that path (`_layout/level-3-files/mcp/server.py`). That satisfies (a), so `source` and
`get_component` began to answer. It cannot satisfy (b): the skill folder is not in anything I am
allowed to read, so `get_rules` and the page starter stayed broken for the whole run.

This is a departure from the instructed start command. Judge the results below with that in mind:
calls marked **A** used the instructed path, calls marked **B** used the linked path. A real
connected assistant would have had only the A results. The server was always started with
`--read-only`, so `add_inspiration` was never even offered.

## Every tool call, in order

| # | Path | Call | Result | Enough to act on? |
| --- | --- | --- | --- | --- |
| 1 | A | `studio_overview()` | ok | Yes for the goal, audience and format words. Its `how_to_choose` text talks about "paths relative to the project folder", `base/studio.html` tabs and `sources/02-posts-lib.html`: file-system talk that means nothing to a tool-only client. |
| 2 | A | `recommend(report, team, any)` | ok | Yes for the choice: one-page report + analyst voice, "strong". Not for the look: it says `"look": "Dashboard"` and no tool that worked could tell me what Dashboard is. Scores are not comparable across formats (page 28, deck 15) because the page score adds two templates; I ignored the numbers and used "strength". |
| 3 | A | `list_inspiration()` | ok, empty `[]` | Yes. Nothing saved, nothing to act on. |
| 4 | A | `get_template(recipe-report, options)` | ok | Partly. Good summary and "ask" sentences. The `options` text names "seven voices, nine looks" without listing them. |
| 5 | A | `get_template(voice-analyst, options)` | ok | Partly. Same. The only place `default_look` appears. |
| 6 | A | `get_rules(build)` | **error** | No. `FileNotFoundError .../level-2-files/artifact-studio/references/build-rules.md` |
| 7 | A | `get_rules(checklist)` | **error** | No |
| 8 | A | `get_rules(recipes)` | **error** | No |
| 9 | A | `get_rules(voices)` | **error** | No |
| 10 | A | `get_rules(looks)` | **error** | No |
| 11 | A | `get_rules(design)` | **error** | No |
| 12 | A | `get_rules(skill)` | **error** | No |
| 13 | A | `get_template(recipe-report, starter)` | **error** | No. Missing `page-skeleton.html` in the level-2 folder. |
| 14 | A | `get_template(recipe-report, source)` | **error** | No. Looks for `runs/level-3-files/...` |
| 15 | A | `list_templates(page)` | ok | Yes, as a list. Added nothing after `recommend`. |
| 16 | A | `list_components(page)` | ok | Yes for names and uses. |
| 17 | A | `make_palette(140)` | ok | A probe to see which tools were alive. **Not used.** The person gave no brand colour and the tool's own description says it is "not for picking the brand colour itself". The answer itself is complete and clear: seven colours, jobs, contrast checks. |
| 18 | A | `get_component(page-big-numbers)` | **error** | No |
| 19 | A | `get_component(svg-line-draw)` | **error** | No |
| 20 | A | `get_template(voice-analyst, source)` | **error** | No |
| 21 | A | `get_template(deck-briefing, starter)` | **error** | No. A probe: the deck starter is broken too, so the deck route was no escape. |
| 22 | B | `get_template(recipe-report, source)` | ok | Mostly. The single most useful answer of the run: real styles, real markup, and a "Behind this page" block that states the recipe order. Not a complete file (see below). |
| 23 | B | same call again | ok | Repeat. My client printed it badly the first time. No new information. |
| 24 | B | `get_template(voice-analyst, source)` | ok | Mostly. Its "How it is built" and "Design rules" lists were the only voice rules I ever saw. |
| 25 | B | `get_template(recipe-report, starter)` | **error** | No. Still needs the level-2 folder. |
| 26 | B | `list_components(card)` | ok | Yes |
| 27 | B | `list_components(layout)` | ok | Yes |
| 28 | B | `list_components(colour)` | ok | Yes |
| 29 | B | `get_component(page-big-numbers)` | ok | No. Markup only, no styles, no script. |
| 30 | B | `get_component(page-bar-chart)` | ok | No. Markup only. I wrote the `.hb` bar styles myself. |
| 31 | B | `get_component(card-stat-card)` | ok | Partly. Markup only, but its one-line rule ("the change is written in words and never shown by colour alone") was usable and I followed it. |
| 32 | B | `get_component(card-action-card)` | ok | Partly. Same: the rule "the state is written out" gave me the "Decision needed" chip in words. |
| 33 | B | `get_component(page-old-way-new-way)` | ok | Not used. It asks for three lines a side; the notes have one. |
| 34 | B | `get_component(page-callouts)` | ok | Partly. Rule used (a bold label as well as colour). Styles and icons guessed. |
| 35 | B | `get_component(colour-60-30-10)` | ok | Yes as a rule. Not as code. |

Tally: 35 calls. On the instructed path, 21 calls, 13 errors. On the linked path, 14 calls, 1 error.
Tools never called: `add_inspiration` (forbidden, and not registered under `--read-only`).

## What was missing from the tools, and what I guessed

1. **All written rules.** `get_rules` never answered. Guessed: everything a build rule or checklist
   would have decided. Whether motion is allowed, what the delivery note must contain, what to do
   when the content cannot fill a recipe slot, how to handle derived numbers, what "check before
   showing" means. I made my own check (headless Chrome, two widths, motion off, scripts off).
2. **What the "Dashboard" look is.** `recommend` says `"look": "Dashboard"`. The report template's
   own source says "Looks: quiet, one data colour". No working tool defines either. Guessed: I
   copied the colours in the report template's style block (`#0f6b63` bar, `#b9c7c4` quiet,
   `#55635f` muted, `#14211f` ink, `#f4f6f5` page) and called that the look. If Dashboard is
   something else, the page is wrong and I cannot tell.
3. **The shell.** The source note says "Shared styles and helpers are in
   level-3-files/mcp/library/sources/shell.html". There is no tool that returns it. So these
   arrived undefined: `var(--sans)`, `var(--plex)`, the `.lc` line chart, the `.hb` bars,
   `.sample-note`, `.view`, `STUDIO.countUp`, `STUDIO.line`, `STUDIO.seen`, `onView`, `$`. Guessed:
   `--sans` is a system font stack; `--plex` is some IBM Plex face, which I replaced with the same
   system stack because no network fonts are allowed; I wrote my own count-up and bar-grow script
   and my own bar styles.
4. **A page starter.** Decks and social formats get a complete starter. Pages get a skeleton that
   lives in the folder that was missing. Guessed: the whole document frame (doctype, head,
   viewport, reset, print styles).
5. **Component styles.** Every `get_component` note says "Its styles and script are in the same
   source file", and then does not return them. A component without its CSS is a description, not
   a part. Guessed: the look of the callout and the chip.
6. **Which parts of a source are the template and which are the studio's own display.** The source
   includes a "Behind this page" section, an `@@levels` line and a `data-tab` wrapper. Nothing says
   "leave these out". I left them out. Likewise each component comes wrapped in
   `<section class="spec">` with an `@@ask` line of pipe-separated fields and no key to the fields.
7. **How a recipe and a voice combine when they disagree.** The report recipe says four numbers,
   one chart, one table. The analyst voice says three numbers, three findings each with a chart,
   how it was measured, limits, next steps with owner and date. `recommend` pairs them and nothing
   says which wins. Guessed: recipe for the order and counts, voice for the wording.
8. **What to do when the content is thinner than the recipe.** The recipe wants a trend line and a
   breakdown table with the weak row marked. The notes hold two months and no breakdown. Guessed:
   two bars for the chart, no table, and say so in the note.

## Smaller things

- **Errors are useless to a model and leak to the operator.** The client receives only
  "Error executing tool get_rules". The real reason (a missing file and its full path) goes to the
  server's stderr as a 40-line traceback. A connected assistant would see the short line, learn
  nothing, and most likely retry or give up. The server should check its folders at start-up and
  either refuse to start or have each tool return a plain sentence: "The rules folder is missing
  at X. Keep level-2-files beside level-3-files."
- **`test_client.py` would have caught this** and is the documented check, but nothing runs it at
  start-up, and a person who copies only the `mcp` folder gets a server that "sits and waits" (the
  README's sign that "it is working") while three of its tool families are dead.
- **The server instructions and the overview both say to call `get_rules('build')` "before
  writing" and `get_rules('checklist')` "before showing the result".** There is no fallback line
  for when they fail, so the stated method has a hard stop in the middle.
- **`make_palette`'s description** tells you what a few hues look like (0 red, 45 orange-brown,
  140 green) but there is no tool to turn a hex code into a hue, which is how a real person holds
  their brand colour.
- **Template answers carry paths** (`preview: base/studio.html#recipe-report`,
  `source: level-3-files/mcp/library/sources/51-recipe-report.html`) that a tool-only client
  cannot open. They read as an invitation to go to the disk.
- **Demo content in the source is close to this job** (a landscaper-style "site visits" example in
  the analyst voice). It is clearly marked invented, but a careless agent could carry a sample
  line or figure into a real page. I checked that none did.

## Verdict on the question the test asks

Can an agent with only these tools make a good page? As installed here: no. It can pick a template
and then gets errors. With the folder name fixed: it can make a decent page, as this run shows, but
about half of it (frame, fonts, bar styles, script, the look, every judgement a rule would have
settled) came from me and not from the studio. With the rules reachable as well, I cannot say; I
never saw them.
