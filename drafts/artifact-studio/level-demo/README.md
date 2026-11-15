# Level demo: the studio in one file

[`artifact-studio.html`](artifact-studio.html) is the whole studio as a single page with six tabs.
Nothing to set up. Download it and open it in a browser. GitHub shows HTML files as source, so it
has to be opened locally.

**Think of it as** a showroom. Every item on the floor works, and each has a tag saying how to
order one.

## What is in it

| Tab | What it shows | Count |
| --- | --- | --- |
| Start | A sentence builder: choose a recipe, a voice, a look and a level, then copy the sentence | |
| Recipes | Whole pages made from the parts: a report, a proposal, an explainer, a landing page | 4 |
| Voices | The same case made seven ways, each a complete page | 7 |
| Page components | Parts that need no photograph: numbers, timeline, tables, chart, questions and more | 12 |
| Photo components | Parts built from one photograph: pan and zoom, scrolling tour, line art and more | 12 |
| How to use | The three levels, steps for people, rules for agents | |

Every voice and recipe page ends with "Behind this page": how it is built, its design rules, and
the sentence that asks for it at beginner, advanced and expert level.

## Facts about the file

- One HTML file of about 1.4 MB. Two photographs and fifteen subset fonts are inside it.
- It loads nothing from the network and uses no libraries.
- Tabs are views in the same file, switched by the address after the `#`.
- All example companies, people and figures are invented, and each page says so.

## What was checked, and what was not

Checked on 2026-11-15, in Chrome:

- Every tab and page at 390 and 1280 pixels wide: no script errors, no sideways scrolling.
- The script path used by browsers without scroll-driven animations.
- Arithmetic in the examples: report rows add up to the totals, and percentages match.

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
| `source/shell.html` | The page frame: tabs, the router, shared helpers |
| `source/base.css` | Shared styles |
| `source/views/` | One file per tab or page: style, markup, script |
| `source/prepare_assets.py` | Encodes photos and fonts, measures the lake photo, traces its line art. Writes `assets.json` |
| `source/build.py` | Assembles the page. Also regenerates `level-simple/sentences.md` and the skill's component catalogue |

`prepare_assets.py` needs pillow, numpy, fonttools and brotli, and a folder holding the font files
named in its header. `assets.json` is a build product and is not committed.

A rebuild from the stored photos looks the same but is not byte for byte identical, because the
photos are compressed a second time.

## Credits and licences

- Photographs: taken by the repository owner. Stored without location or camera data.
- Fonts: National Park, Crimson Pro, Instrument Sans, JetBrains Mono, Gloock, Big Shoulders, Work
  Sans and IBM Plex Serif, embedded as subsets under the SIL Open Font License 1.1. Licence texts
  are in [`source/licences/`](source/licences/).
- Code: Apache-2.0, like the rest of this repository.
