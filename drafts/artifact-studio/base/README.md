# The base: everything the studio is made of

This folder is the product. The landing page and the three level guides beside it only explain
how to use what is in here.

**Think of it as** a showroom with a stockroom behind it. Every item on the floor works, each has
a tag saying how to order one, and you can carry any of them out as a file.

| You want | Open | What it is |
| --- | --- | --- |
| To see everything in one page | [`studio.html`](studio.html) | Every template and part in tabs, with a picker and a palette maker. Download it and open it in a browser |
| The instructions for a chatbot | [`instructions/`](instructions/) | `AI-INSTRUCTIONS.md` to paste at level 1, and `preferences-template.md` to fill in at level 2 |
| The library | [`templates/`](templates/) | Every template, part and starter as its own file. [`README.md`](templates/README.md) is the index for people, [`index.json`](templates/index.json) for agents |
| Sample outputs | [`examples/`](examples/) | Six worked requests: what was asked, the notes, what was picked and what came back |
| The words that ask for each one | [`sentences.md`](sentences.md) | Every sentence, generated from the templates |
| The skill | [`skills/artifact-studio/`](skills/artifact-studio/) | What an assistant follows: the steps, the cards, the build rules, the checklist and the page skeleton |
| Connectors | [`connectors/`](connectors/) | The MCP server that gives an agent the library as tools |
| Your colours, and a brief for one piece | [`forms/`](forms/) | Two short forms to fill in |
| To keep a design you admired | [`inspiration/`](inspiration/) | How a find becomes a card, without copying it |
| Something the studio does not do | [`RESOURCES.md`](RESOURCES.md) | Outside skills, frameworks and services, with dates |
| Instructions for agents | [`AGENTS.md`](AGENTS.md), [`CLAUDE.md`](CLAUDE.md) | The path from a request to a finished file |
| To change or check any of it | [`source/`](source/), [`gates.json`](gates.json) | The catalogue, the views, the build script, the tests and the list of checks |

The build counts the library and writes this line: <!-- counts -->20 templates (4 pages, 7 voices, 4 decks, 5 social formats), 53 components (12 page parts, 12 photo parts, 12 animated SVG files with 11 GIF copies, 17 design ideas for cards, layouts and colour) and 9 looks<!-- /counts -->.

## Check it

```
python3 ../../../tools/gates.py .          # quick checks, about 30 seconds
python3 ../../../tools/gates.py . --all    # adds every page at three widths, about 10 minutes
```

It ends with "All gates that ran passed" or "DO NOT SHIP" and the reason. Each check in
[`gates.json`](gates.json) says what it proves. The page check needs `playwright` and a Chrome
binary, and runs an accessibility scan when `AXE_JS` points at `axe.min.js`.

## Rebuild it

```
python3 source/build.py
```

One file feeds everything: [`source/catalog.py`](source/catalog.py) holds the templates, their fit
scores and the palette rule. The build writes the studio page, the template files, both indexes,
`sentences.md`, the pasted instructions and the North Star page. It needs the Python `markdown`
package. Fonts and photographs are already encoded in `source/assets.json`.

## What was checked, and what was not

- **Checked, in Chrome:** every tab of the studio page and every template at 320, 390 and 1280
  pixels wide. No script errors, no sideways scrolling, and no violations in an automated
  accessibility scan, which covers only part of the standard.
- **Not checked:** a real phone, Safari, Firefox, a screen reader, or anyone other than the author
  using it.

Every example company, person and figure is invented, and each page says so.

## Credits and licences

- Photographs: taken by the repository owner. Stored without location or camera data.
- Fonts: National Park, Crimson Pro, Instrument Sans, JetBrains Mono, Gloock, Big Shoulders, Work
  Sans and IBM Plex Serif, embedded as subsets under the SIL Open Font License 1.1. Licence texts
  are in [`source/licences/`](source/licences/).
- Code: Apache-2.0, like the rest of this repository.
