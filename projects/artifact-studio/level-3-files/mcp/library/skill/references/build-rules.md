# Build rules

How to write the HTML. These rules are why the studio's pages work on a phone, offline and for
people who turn motion off.

## Contents

- The file
- Complete at rest
- Layout
- Colour and type
- Motion
- Charts
- Images and video
- Words
- Accessibility
- Libraries

## The file

- One HTML file. CSS in one `<style>`, script inside the file. No build step.
- It opens from a folder with no network. Fonts and images are embedded, or the page uses system
  fonts and no images.
- Start from `assets/page-skeleton.html`, or from the starter in `assets/starters/` for a deck or a
  social picture. Keep its token block, its motion guard and its scroll
  helper.
- If the page will be published as a Claude artifact, only cdnjs, jsDelivr, unpkg and Google Fonts
  load from outside. Everything else is blocked without an error.

## Complete at rest

The page must make sense before any script runs. The first person to open the studio on a phone
could not find the examples, and this section is what that taught.

- The first screen shows real content. Never open on a form, a row of menus or an empty frame.
- Build tabs from radio buttons and labels, or from `<details>`, so they switch with scripts
  turned off. The first tab is showing on load. Give every item its own tab when there are
  fewer than about ten, instead of a menu page that leads to them.
- Offer choices as buttons that are all visible. A dropdown hides its choices.
- Scripts add to the page and never hold it up. Give each part's set-up its own `try`, so one
  failure cannot empty the rest. On a page with tabs, give each tab its own script element: a
  syntax fault stops the whole element it is in.
- A part that cannot work without script, such as a calculator or a player, starts with a worked
  default written into the HTML, or says so in a `<noscript>` line.

## Layout

- Design at 390 pixels wide first, then widen. Nothing scrolls sideways except a table or a
  swipe gallery inside its own container.
- Side padding of at least 16 pixels at every width.
- Text column no wider than about 65 characters.
- Tap targets at least 44 pixels high.
- Size sections to their content. Use `svh` units with a pixel cap, never bare `vh`.

## Colour and type

- Name at most seven colours as tokens at the top of the style block and use only those: background,
  panel, border, secondary text, main text, accent and highlight. A page with a chart adds one
  data colour. The accent is for what to act on. The data colour is never a second accent: on a
  page whose whole job is the data, the data colour may be the one accent.
- **60-30-10.** One dominant colour for about 60 percent of the page (usually the background), one
  secondary colour for about 30 percent (text, structure, any dark or tinted panel), and one bold
  accent for about 10 percent: the call to action and at most one emphasis per screen. Never a
  second accent. Name the three roles `--c60`, `--c30` and `--c10` in `:root`; the repository's
  `workshop/tools/check_colour_balance.py` measures them with photos hidden.
- Keep the background clean. A cinematic page gets its drama from photos, type and motion, not from
  gradients or coloured panels behind every section. A dark, full-bleed opening is fine; the
  sections after it can sit on a flat, quiet background.
- Text against its background: at least 4.5 to 1 for body text, 3 to 1 for large headings.
- One or two typefaces. If two, make them clearly different.
- Meaning never depends on colour alone. A warning has an icon and a label as well.

## Motion

- Motion must carry meaning: it shows what changed, where to look, or how far along you are.
- At most three moving parts on a page.
- Everything is readable before any animation runs. Never leave content at zero opacity waiting
  for a scroll.
- Tie movement to scrolling with the skeleton's small script, which sets one custom property from
  the scroll position and behaves the same in every browser. Keep the skeleton's CSS-only form,
  inside `@supports ((animation-timeline: view()) and (animation-range: entry))`, so the page
  still moves with scripts off.
- Wrap every animation in the reduced-motion guard. With motion off, the page shows its final
  state.
- No sound. No video that plays with sound by itself.

## Charts

- One chart, one point. The heading says the point as a sentence.
- One data colour, its own token and never the accent. Grey for the comparison. Thin bars with the value at the end. Two-pixel lines.
- Label the values that matter. Leave the rest to touch or a table.
- State the unit and the source under the chart.
- Every number on a chart came from the person's content. Show derived numbers in a table.

## Images and video

- Embed photos as JPEG at no more than 2,000 pixels on the long side, saved without metadata.
- Every image has alt text that says what it shows.
- Crop with `background-position` or `object-position` to keep the subject in frame at phone width.
- Video: `<video controls playsinline preload="metadata" poster="...">`. Add `muted` only for a
  silent loop. For a single-file page, link to the video and show its poster.

## Words

- Real content everywhere. No placeholder text.
- A button says what happens when it is pressed.
- Dates, prices and names are copied from the content, not retyped from memory.
- A number, a name, a date or a price the reader will act on, shown on the page with part of it
  missing, is marked `[needs: ...]`. A whole section the content cannot fill is left out, not
  marked. Every gap is listed in the delivery note.

## Accessibility

- Headings in order. One `h1`.
- Every control reachable and usable by keyboard, with a visible focus ring.
- Interactive parts use real controls: `button`, `input`, `details`, `select`.
- Regions that update (a counter, a status line) use `aria-live="polite"`.

## Libraries

Most pages need none. Add one only when it does substantial work, and ask first because it adds a
network dependency.

| Need | Library | Load from |
| --- | --- | --- |
| Timed, sequenced or path animation | GSAP | cdnjs, pinned to an exact version |
| Many charts, or chart types beyond line and bar | Observable Plot or Chart.js | cdnjs, pinned |
| Step triggers on a long story | Scrollama | cdnjs or unpkg, pinned |
| Large diagrams from text | Mermaid | cdnjs, pinned |

Check each library's licence before you ship with it.
