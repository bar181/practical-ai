# Artifact studio: start here if you are an agent

This folder is a library of templates for web pages, slide decks and social post pictures, with
rules for choosing between them and a skill for building from them. Your job is to turn the
person's own content into one finished file that follows a template.

## The path, in order

1. **Find out what is needed.** The job (report, decide, sell, teach, inspire, announce), the
   reader, and the shape (page, deck, social post). Infer what you can. Ask at most two questions.
2. **Choose.** Read [`base/templates/index.json`](base/templates/index.json). Score each template
   as three times its goal fit plus twice its audience fit, and take the highest. With the MCP
   server connected, call `recommend` and it does this for you. Tell the person what you chose and
   why in one line. Each answer carries a `strength`: strong, fair or weak. When the best answer in
   the shape they asked for is weak, its `note` names a shape that suits the job better. Say so.
3. **Read the person's saved finds** in [`base/inspiration/`](base/inspiration/), or call
   `list_inspiration`. They are designs the person liked, described in their own words. Let them
   shape the choice of voice, look and parts. Never copy the thing a card describes.
4. **Look at one worked example** of the shape you chose, in [`base/examples/`](base/examples/). It
   shows the level of finish expected and how a gap in the notes is marked.
5. **Start from the starter** when there is one. Decks and social formats have a `starter` field in
   the index: a complete file of about 10 KB or less, with system fonts and no photograph, that you
   copy and fill. Pages and voices have none: build on the skill's
   [`page-skeleton.html`](../../skills/artifact-studio/assets/page-skeleton.html) and read the
   template's `source` field, one small file with a style block, the markup and a script.
6. **Read the rules.** [`build-rules.md`](../../skills/artifact-studio/references/build-rules.md)
   before you write, and the card for the voice and look in
   [`voices.md`](../../skills/artifact-studio/references/voices.md) and
   [`looks.md`](../../skills/artifact-studio/references/looks.md).
7. **Build** one self-contained file from the person's content, on the starter or skeleton from
   step 4: HTML for a page or a deck, SVG for a social picture.
8. **Check** with [`pre-ship-checklist.md`](../../skills/artifact-studio/references/pre-ship-checklist.md).
9. **Return** the file and the delivery note below.

If you can load skills, load [`skills/artifact-studio/SKILL.md`](../../skills/artifact-studio/SKILL.md)
and follow it. It says all of this in more detail.

## Where everything is

| You need | Read |
| --- | --- |
| Every template, with its options and fit scores | [`base/templates/index.json`](base/templates/index.json), or [`base/templates/README.md`](base/templates/README.md) for a page a person can read |
| The rules that choose between templates | [`base/source/catalog.py`](base/source/catalog.py) |
| A finished template to look at | The `file` field in the index, under [`base/templates/`](base/templates/) |
| A complete small file to copy and fill | The `starter` field in the index, under [`base/templates/starters/`](base/templates/starters/) |
| Its reference code | The `source` field in the index, under [`base/source/views/`](base/source/views/) |
| The parts: page parts, photo parts, animated SVG | The `components` list in the index |
| Design ideas: kinds of card, layouts, colour rules and the palette rule | [`design-ideas.md`](../../skills/artifact-studio/references/design-ideas.md), or the Design tabs of the studio page |
| What a good result looks like | Six worked examples in [`base/examples/`](base/examples/): the request, the notes, what was picked and the output |
| The person's standing preferences | A file named `preferences.md`, if they have one. See [`level-2/`](level-2/) |
| Their colours, type and a brief for this page | [`base/forms/`](base/forms/), filled in |
| What to use when the studio is the wrong tool | [`base/RESOURCES.md`](base/RESOURCES.md) |
| How to take in a design the person likes | [`base/inspiration/README.md`](base/inspiration/README.md) |
| The same library as tools you can call | [`level-3/mcp/`](level-3/mcp/) |

## Inputs you can expect

| Input | Form | If it is missing |
| --- | --- | --- |
| Content | Notes, a document, a spreadsheet, a transcript, a link | Ask for it. Do not write a page from nothing |
| Media | Photos, a logo, a chart image, a video link | Build without. Never use a stock image as if it were theirs |
| Preferences | `preferences.md` | Use the defaults for the template |
| Request | A sentence, or a template id from the index | Choose with the rules above and say what you chose |

## Output contract

Return two things.

1. **One HTML file.** Self-contained, phone first, readable with motion off and with scripts off.
2. **A delivery note** with these four headings, in this order.

```
Chose: <template>, <voice>, <look>. <one line on why, if you chose>
Assumed: <each assumption, one per line, or "nothing">
Missing: <each gap marked [needs: ...] on the page, or "nothing">
Check before sharing: <the numbers, names and claims a person must verify>
```

## Rules that never bend

1. No invented facts. Mark gaps as `[needs: ...]`.
2. A voice is a style. Never attribute words to the person who inspired it.
3. Every company, person and figure in the templates is invented. Adapt the pattern and never
   carry the example content into the person's page.
4. When the person shows you a design they like, record the idea in your own words. Do not copy
   its text, pictures, logo, characters or code.
5. Stop before anything is posted, sent or published. A person decides.

## Reference code by pattern

Each file in `base/source/views/` is one complete example. Class names carry a two-letter prefix
per file, so a part can be lifted out without collisions.

| Looking for | Read |
| --- | --- |
| Pinned visual with scrolling steps | `20-photo.html` (tour) and `53-recipe-explainer.html` (diagram) |
| Scroll-linked motion with a fallback | `shell.html` (driver) and `20-photo.html` (parallax, line art) |
| Line chart and bars | `01-lib.html` |
| Full-screen snapping sections | `41-voice-keynote.html` |
| Hand-advanced slides | `44-voice-pitch.html` |
| Tick boxes with a progress bar | `45-voice-practical.html` |
| A table that stacks on phones | `47-voice-brief.html` |
| Price cards, questions, tabs, callouts, ring | `30-parts.html` |
| Page tabs that switch with scripts off | `shell.html` (styles) and `build()` in `build.py` (radio buttons, labels and the rules that show one view) |
| Tap-to-choose buttons that write a request | `70-mix.html` |
| One line dressed in nine looks | `25-looks.html` |
| A Markdown file shown as a tab | `md_view()` in `build.py` |

| Slides that are a readable column until the script makes them a stage | `01-lib.html` (deck engine), `81-deck-visionary.html` |
| Post pictures drawn as SVG and saved as PNG with their fonts inside | `85-social.html` |
| Animation with no script, scoped so parts do not clash | any file in `base/templates/components/svg/` |
| Choosing a combination from a request | `catalog.py` (rules) and `75-pick.html` (the same rules in the page) |

## Running without skill support

In an assistant that cannot load skill folders, the person pastes
[`level-1/AI-INSTRUCTIONS.md`](level-1/AI-INSTRUCTIONS.md) into the project instructions. It
condenses the skill and its cards into one file. The full reference files have more detail and
take precedence where the two differ.

## Known limits

- The skill has not yet been run end to end by a second agent. Treat the first runs as tests and
  record what went wrong.
- The MCP server has been tested with a client on the machine that built it. It has not been
  tried inside a desktop assistant or over the internet.
- The fit scores in the catalogue are the author's judgement. Nobody has measured them.
- Video handling is specified in the skill and has no worked example.
