# Level demo: every example in one file

[`artifact-studio.html`](artifact-studio.html) holds every working example in the studio. Nothing
to set up. Download it and open it in a browser. GitHub shows HTML files as source, so it has to
be opened locally.

**Think of it as** a showroom. Every item on the floor works, and each has a tag saying how to
order one.

## What is in it

| Tab | What it shows | Count |
| --- | --- | --- |
| Voices | The same case made seven ways, each a complete page with its own tab: keynote, storyteller, teacher, pitch, practical instructor, analyst, executive brief | 7 |
| Looks | The same line dressed nine ways, with the look cards underneath | 9 |
| Photo parts | Parts built from one photograph: pan and zoom, scrolling tour, line art and more | 12 |
| Page parts | Parts that need no photograph: numbers, timeline, tables, chart, questions and more | 12 |
| Recipes | Whole pages made from the parts, each with its own tab: a report, a proposal, an explainer, a landing page | 4 |

Every voice and recipe page ends with "Behind this page": how it is built, its design rules, and
the sentence that asks for it at beginner, advanced and expert level.

## The four pages built from this source

| Page | File | Tabs |
| --- | --- | --- |
| All examples | [`artifact-studio.html`](artifact-studio.html) | 7 voices, 9 looks, photo parts, page parts, 4 recipes |
| Level 1: Beginner | [`../level-simple/artifact-studio-beginner.html`](../level-simple/artifact-studio-beginner.html) | Start here, 4 recipes, photo parts, page parts, every sentence, how to test a sentence |
| Level 2: Advanced | [`../level-working/artifact-studio-advanced.html`](../level-working/artifact-studio-advanced.html) | Start here, 7 voices, 9 looks, the request mixer, three reference cards, two templates |
| Level 3: Expert | [`../level-automated/artifact-studio-expert.html`](../level-automated/artifact-studio-expert.html) | Start here, the skill in three forms, build rules, a tickable checklist, the agent guide, best practices |

## Facts about the file

- Each page is one HTML file. The three with photographs are about 1.4 MB. The expert page has no
  photographs and is about 0.3 MB.
- It loads nothing from the network and uses no libraries.
- Tabs are radio buttons styled as tabs, so they switch with scripts turned off. The script adds
  the animated parts and keeps the address after the `#` in step.
- All example companies, people and figures are invented, and each page says so.

## What was checked, and what was not

Checked on 2026-11-15, in Chrome:

- Every tab of all four pages at 320, 390 and 1280 pixels wide: no script errors, no sideways
  scrolling, exactly one tab showing.
- Tabs with scripts turned off: the first tab shows on load and tapping a tab changes it.
- The script path used by browsers without scroll-driven animations.
- Arithmetic in the examples: report rows add up to the totals, and percentages match.
- An automated accessibility scan (axe-core, WCAG 2 A and AA rules) of every tab of all four pages: no violations after fixes. An automated scan covers only part of the
  standard.

Not checked:

- A real phone, Safari or Firefox.
- A screen reader. Controls use standard elements and labels, and that is as far as it went.
- Anyone other than the author using it.

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
| `source/build.py` | Assembles the four pages. Which tabs go in which page is the `EDITIONS` table near the top. Also regenerates `level-simple/sentences.md` and the skill's component catalogue |

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
