# Component gallery

One photo, twelve components. A single page that shows what a chat assistant can build from one
picture, with the sentence that asks for each effect.

**Think of it as:** a paint chart. You do not learn the chemistry. You point at a swatch and say
"that one".

## Open it

GitHub shows HTML files as source. To see the page, download
[`component-gallery.html`](component-gallery.html) and open it in a browser. It is one file of
769 KB with the photo and fonts inside it, and it loads nothing from the network.

## What is on the page

| Component | What it shows |
| --- | --- |
| Pan and zoom | A slow documentary zoom on a still photo |
| Parallax window | The photo moving slower than the page |
| Photo-filled type | One large word with the photo showing through the letters |
| Scrolling photo tour | The photo stays put and zooms to a new detail with each paragraph |
| Self-drawing line art | A line drawing that draws as you scroll, then fades into the photo |
| Chart from the photo | Brightness from top to bottom, and the six main colours, both measured from the pixels |
| Before and after | Two versions of one picture with a divider to drag |
| Looks and voices | Five colour treatments, each paired with a writing voice |
| Frosted glass card | Facts on a blurred pane over the photo |
| Bento grid | A summary as tiles of different sizes |
| Swipe gallery | Cards that snap sideways one at a time |
| Flip postcard | A photo with a note on the back |

The page also has a reading progress bar and three reference lists: pages worth studying, free
tools to grow into, and skills that already exist.

The sentences are collected in
[`../level-simple/component-sentences.md`](../level-simple/component-sentences.md). The research
behind the reference lists is in [`../landscape-review.md`](../landscape-review.md).

## What was checked, and what was not

Checked on 2026-11-14:

- Rendered in Chrome at phone width (390 px) and desktop width (1280 px) with no script errors and
  no sideways scrolling.
- Both scroll paths: the browser's own scroll-driven animations, and the script used where a
  browser lacks them.
- The numbers on the page come from the photo. `source/prepare_assets.py` computes them.

Not checked:

- A real iPhone or Android phone, Safari or Firefox.
- Whether the twelve sentences reproduce these effects when pasted into a fresh chat. This is the
  main open test.
- Anyone other than the author using it.

## Known gaps

- It shows effects, not finished pages. Nothing here is a proposal, a report or an explainer yet.
- Everything is written by hand. The free tools in the reference lists are named, not used.
- The treeline, island and trunk in the line art are traced from the photo's pixels. The branches,
  reeds and ripples are sketched to match and are approximate.
- The fifth voice card is a guess at the repository owner's teaching style and has not been
  corrected by him.

## Rebuild it

```
cd source
python3 prepare_assets.py --photo photo.jpg --fonts path/to/fonts
python3 build.py
```

`prepare_assets.py` needs pillow, numpy, fonttools and brotli, and a folder holding the National
Park and Crimson Pro font files named in its header. `build.py` writes `component-gallery.html`
one folder up.

A rebuild from `source/photo.jpg` looks the same but is not byte for byte identical to the
committed page, because the photo is compressed a second time. The committed page was built from
the original camera file. To use your own picture, pass it with `--photo`. The tour stops, the
crops and the page text describe the lake photo, so edit `page-template.html` to match.

## Credits and licences

- Photo: taken by the repository owner. Saved without location or camera metadata.
- Fonts: National Park and Crimson Pro, embedded as subsets under the SIL Open Font License 1.1.
  The licence texts are in [`source/licences/`](source/licences/).
- Code: Apache-2.0, like the rest of this repository.
