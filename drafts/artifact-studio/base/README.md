# The base: everything you need

This folder is the product. It holds every example, the templates, the sentences and the source.
The [skill](../../../skills/artifact-studio/) sits in the repository's `skills/` folder and is
part of the base. The level folders beside this one only add to it.

**Think of it as** a showroom with a stockroom behind it. Every item on the floor works, each has
a tag saying how to order one, and you can carry any of them out as a file.

## What is in it

| You want | Open | What it is |
| --- | --- | --- |
| To see everything | [`studio.html`](studio.html) | One page with a tab for every example, then the cards, the skill and how to use it |
| One example as a file | [`examples/`](examples/) | Fourteen complete pages, each a single file you can copy as a starting point |
| The words that ask for each one | [`sentences.md`](sentences.md) | Every sentence, generated from the examples |
| Your colours and type on one page | [`templates/design-spec.md`](templates/design-spec.md) | A form to fill in once |
| A brief for one page | [`templates/content-brief.md`](templates/content-brief.md) | A form to fill in per page |
| The instructions an assistant follows | [`skills/artifact-studio/`](../../../skills/artifact-studio/) | The skill, its cards, the build rules, the checklist and the page skeleton |
| To hand the job to an agent | [`AGENT-GUIDE.md`](AGENT-GUIDE.md) | Inputs, steps and the output contract |
| The reasoning | [`BEST-PRACTICES.md`](BEST-PRACTICES.md) | Ten practices and how to add a recipe, voice, look or part |
| To test a sentence | [`sentence-test.md`](sentence-test.md) | The sheet for scoring a sentence in a fresh chat |
| To change or rebuild any of it | [`source/`](source/) | Views, build script and checks |

GitHub shows HTML files as source, so download a file and open it in a browser.

## The examples

| File | What it shows |
| --- | --- |
| `examples/voice-keynote.html` | The same case in the keynote voice: one idea per screen, huge type |
| `examples/voice-story.html` | The storyteller voice: the customer as the hero |
| `examples/voice-teacher.html` | The teacher voice: analogy, worked example, check-yourself questions |
| `examples/voice-pitch.html` | The pitch voice: a memory, a feeling, the product last |
| `examples/voice-practical.html` | The practical instructor voice: numbered steps with a time on each |
| `examples/voice-analyst.html` | The analyst voice: the answer first, then findings with one chart each |
| `examples/voice-brief.html` | The executive brief voice: the decision first, an options table |
| `examples/recipe-report.html` | A one-page report |
| `examples/recipe-proposal.html` | A proposal with three options |
| `examples/recipe-explainer.html` | A scrolling explainer |
| `examples/recipe-landing.html` | A landing page |
| `examples/looks.html` | One line dressed in nine looks, with the look cards |
| `examples/photo-parts.html` | Twelve parts built from one photograph |
| `examples/page-parts.html` | Twelve parts that need no photograph |

Every voice and recipe page ends with "Behind this page": how it is built, its design rules, and
the sentence that asks for it as a short ask, a full ask, and with the skill.

All seven voices use the same invented case, so the only thing that changes between them is the
voice.

## Facts about the file

- Each page is one HTML file with its fonts and any photograph inside it. Examples without a
  photograph are about 0.3 MB. Those with one are 0.6 to 1.4 MB. The studio page is about 1.5 MB.
- It loads nothing from the network and uses no libraries.
- Tabs are radio buttons styled as tabs, so they switch with scripts turned off. The script adds
  the animated parts and keeps the address after the `#` in step.
- Each tab's script sits in its own script element, so a fault in one cannot stop the others.
- All example companies, people and figures are invented, and each page says so.

## What was checked, and what was not

Checked on 2026-11-15, in Chrome:

- Every tab of the studio page and every example file at 320, 390 and 1280 pixels wide: no
  script errors, no sideways scrolling, exactly one view showing, no photo frame left empty.
- Every tab at 768 and 1024 pixels wide, either side of the layout's breakpoint, before the
  pages were reorganised into this folder: no errors, no sideways scrolling.
- Tabs with scripts turned off: the first tab shows on load and tapping a tab changes it.
- One tab's script broken on purpose: the other tabs still set themselves up, and every tab
  still opens.
- The script path used by browsers without scroll-driven animations.
- Arithmetic in the examples: report rows add up to the totals, and percentages match.
- An automated accessibility scan (axe-core, WCAG 2 A and AA rules) of every tab of the studio page and of every example file: no violations after fixes. An automated scan covers only part of the
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
| `check_tabs.py` | Every tab of the studio page and every example file at three widths: script errors, sideways scrolling, whether exactly one tab shows, the accessibility scan if `AXE_JS` is set, and the tabs with scripts off. A clean run prints `problems []` on every line |
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
| `source/build.py` | Assembles `studio.html` and the fourteen files in `examples/`. The studio's tabs are the `STUDIO_GROUPS` list. Also regenerates `sentences.md`, the skill's component catalogue and `level-1/AI-INSTRUCTIONS.md` |

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
