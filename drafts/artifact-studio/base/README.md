# The base: everything you need

This folder is the product. It holds every example, the templates, the sentences and the source.
The [skill](../../../skills/artifact-studio/) sits in the repository's `skills/` folder and is
part of the base. The level folders beside this one only add to it.

**Think of it as** a showroom with a stockroom behind it. Every item on the floor works, each has
a tag saying how to order one, and you can carry any of them out as a file.

## What is in it

| You want | Open | What it is |
| --- | --- | --- |
| To see everything | [`studio.html`](studio.html) | One page with a tab for every template and part, a picker, the cards, the skill and a guide |
| The library | [`templates/`](templates/) | Templates and components, each a file you can open or copy. [`templates/README.md`](templates/README.md) is the index for people and [`templates/index.json`](templates/index.json) is the index for agents |
| The words that ask for each one | [`sentences.md`](sentences.md) | Every sentence, generated from the templates |
| Your colours and type on one page | [`forms/design-spec.md`](forms/design-spec.md) | A form to fill in once |
| A brief for one piece | [`forms/content-brief.md`](forms/content-brief.md) | A form to fill in each time |
| To take in a design you like | [`inspiration/`](inspiration/) | How a find becomes a note, a change or a new part, without copying it |
| Something the studio does not do | [`RESOURCES.md`](RESOURCES.md) | Outside skills, open-source frameworks and paid services, with dates |
| The instructions an assistant follows | [`skills/artifact-studio/`](../../../skills/artifact-studio/) | The skill, its cards, the build rules, the checklist and the page skeleton |
| The reasoning | [`BEST-PRACTICES.md`](BEST-PRACTICES.md) | Ten practices and how to add to the library |
| To test a sentence | [`sentence-test.md`](sentence-test.md) | The sheet for scoring a sentence in a fresh chat |
| To change or rebuild any of it | [`source/`](source/) | Views, the catalogue, the build script and checks |

GitHub shows HTML files as source, so download a file and open it in a browser.

## The library at a glance

| Kind | Count | Where |
| --- | --- | --- |
| Pages | 4 | `templates/pages/`: report, proposal, explainer, landing page |
| Voices | 7 | `templates/voices/`: keynote, storyteller, teacher, pitch, practical instructor, analyst, executive brief |
| Decks | 4 | `templates/decks/`: visionary, story, briefing, workshop |
| Social formats | 5 | `templates/social/formats.html`: square, portrait stat, story, three-slide carousel, link preview. Three styles: Studio, Bold, Soft |
| Page parts | 12 | `templates/components/page-parts.html` |
| Photo parts | 12 | `templates/components/photo-parts.html` |
| Animated SVG | 12 | `templates/components/svg/`, one file each |
| Looks | 9 | `templates/looks/nine-looks.html` |
| Starters | 11 | `templates/starters/`: each deck and each social picture as one small file with system fonts, to copy and fill |

The build counts the library and writes the line below, and `templates/index.json`: <!-- counts -->20 templates (4 pages, 7 voices, 4 decks, 5 social formats), 36 components (12 page parts, 12 photo parts, 12 animated SVG files with 11 GIF copies) and 9 looks<!-- /counts -->. All seven voices and both decks
use the same invented case, so the only thing that changes between them is the manner.

## Facts about the file

- Each template is one HTML file with its fonts and any photograph inside it. Those without a
  photograph are about 0.3 MB. Those with one are 0.6 to 1.4 MB. The studio page is about 1.6 MB.
- Each animated SVG is one file of about 1 KB with no script.
- It loads nothing from the network and uses no libraries.
- Tabs are radio buttons styled as tabs, so they switch with scripts turned off. The script adds
  the animated parts and keeps the address after the `#` in step.
- Each tab's script sits in its own script element, so a fault in one cannot stop the others.
- All example companies, people and figures are invented, and each page says so.

## What was checked, and what was not

Checked on 2026-11-15, in Chrome:

- Every tab of the studio page and every template file at 320, 390 and 1280 pixels wide: no
  script errors, no sideways scrolling, exactly one view showing, no photo frame left empty.
- Every tab at 768 and 1024 pixels wide, either side of the layout's breakpoint, before the
  pages were reorganised into this folder: no errors, no sideways scrolling.
- Tabs with scripts turned off: the first tab shows on load and tapping a tab changes it.
- One tab's script broken on purpose: the other tabs still set themselves up, and every tab
  still opens.
- The script path used by browsers without scroll-driven animations.
- The picker: the page's script and the Python rules give the same answer for all 120 combinations
  of goal, audience and format. `source/tests/check_pick.py` runs this.
- The decks: buttons and arrow keys move between slides, and with scripts off the slides are a
  readable column.
- The social formats: the download button produces a PNG at full size with the fonts inside.
- Arithmetic in the examples: report rows add up to the totals, and percentages match.
- An automated accessibility scan (axe-core, WCAG 2 A and AA rules) of every tab of the studio page and of every template file: no violations after fixes. An automated scan covers only part of the
  standard.

Not checked:

- A real phone, Safari or Firefox.
- A screen reader. Controls use standard elements and labels, and that is as far as it went.
- Anyone other than the author using it.

## Rerun the checks

The checks above can be repeated from this folder. They need Python, the `playwright` package and
a Chrome or Chromium binary.

```
cd source/tests
CHROME=/path/to/chrome AXE_JS=/path/to/axe.min.js python3 check_tabs.py
CHROME=/path/to/chrome python3 check_at_rest.py
```

| Script | What it reports |
| --- | --- |
| `check_tabs.py` | Every tab of the studio page and every template file at three widths: script errors, sideways scrolling, whether exactly one tab shows, the accessibility scan if `AXE_JS` is set, and the tabs with scripts off. A clean run prints `problems []` on every line |
| `check_at_rest.py` | How much text each of the other nine demo pages shows with scripts off |

## Source and rebuild

```
cd source
python3 prepare_assets.py --lake photos/lake.jpg --sunset photos/sunset.jpg --fonts path/to/fonts
python3 build.py
```

| File | Role |
| --- | --- |
| `source/shell.html` | The page frame: header, tabs, shared helpers |
| `source/base.css` | Shared styles |
| `source/views/` | One file per tab: style, markup, script. Document tabs are rendered from the Markdown files in this folder and the skill |
| `source/prepare_assets.py` | Encodes photos and fonts, measures the lake photo, traces its line art. Writes `assets.json` |
| `source/catalog.py` | Every template, its fit scores, and the rules that pick between them. Read by the build, the Pick tab and the MCP server |
| `source/build.py` | Assembles `studio.html` and the files in `templates/`. The studio's tabs are the `STUDIO_GROUPS` list. Also regenerates the two indexes, `sentences.md`, the skill's component catalogue and `level-1/AI-INSTRUCTIONS.md` |

`build.py` needs the Python `markdown` package. `prepare_assets.py` needs pillow, numpy, fonttools and brotli, and a folder holding the font files
named in its header. `assets.json` is a build product and is not committed.

A rebuild from the stored photos looks the same but is not byte for byte identical, because the
photos are compressed a second time.

## Credits and licences

- Photographs: taken by the repository owner. Stored without location or camera data.
- Fonts: National Park, Crimson Pro, Instrument Sans, JetBrains Mono, Gloock, Big Shoulders, Work
  Sans and IBM Plex Serif, embedded as subsets under the SIL Open Font License 1.1. Licence texts
  are in [`source/licences/`](source/licences/).
- Code: Apache-2.0, like the rest of this repository.
