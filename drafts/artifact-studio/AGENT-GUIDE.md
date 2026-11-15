# Agent guide: artifact studio

For an AI agent asked to build a page with this studio, and for the person configuring one.

## The short version

Load [`skills/artifact-studio/SKILL.md`](../../skills/artifact-studio/SKILL.md) and follow it. It
is self-contained: the skill folder holds every card and rule it needs. This guide explains the
contract around it.

## Inputs you can expect

| Input | Form | If it is missing |
| --- | --- | --- |
| Content | Notes, a document, a spreadsheet, a transcript | Ask for it. Do not write a page from nothing |
| Media | Images, a video file or link | Build without. Do not add stock or generated images unless asked |
| Recipe, voice, look | Named in the request, or absent | Choose, and say what you chose in one line |
| Design spec | `level-working/design-spec-template.md`, filled in | Use the default look for the voice |
| Content brief | `level-working/content-brief-template.md`, filled in | Infer audience and job; ask at most two questions |

## Output contract

Return two things.

1. **One HTML file.** Self-contained, phone first, readable with motion off. Rules:
   [`build-rules.md`](../../skills/artifact-studio/references/build-rules.md).
2. **A delivery note** with these four headings, in this order.

```
Chose: <recipe>, <voice>, <look>. <one line on why, if you chose>
Assumed: <each assumption, one per line, or "nothing">
Missing: <each gap marked [needs: ...] on the page, or "nothing">
Check before sharing: <the numbers, names and claims a person must verify>
```

## Where each fact lives

Read these files. Do not rely on memory of them.

| Need | File |
| --- | --- |
| Section order for a page type | [`recipes.md`](../../skills/artifact-studio/references/recipes.md) |
| Order, sentence style and behaviour for a voice | [`voices.md`](../../skills/artifact-studio/references/voices.md) |
| Colour, type and layout for a look, and the photo palette method | [`looks.md`](../../skills/artifact-studio/references/looks.md) |
| Which parts exist and what each is for | [`components.md`](../../skills/artifact-studio/references/components.md) |
| A working example of any part | [`level-demo/source/views/`](level-demo/source/views/), one file per tab or page |
| The starting file | [`page-skeleton.html`](../../skills/artifact-studio/assets/page-skeleton.html) |
| The final check | [`pre-ship-checklist.md`](../../skills/artifact-studio/references/pre-ship-checklist.md) |

## Using the demo source as reference code

Each file in `level-demo/source/views/` is one complete example: a `<style>` block, the markup,
and a small script. Class names carry a two-letter prefix per page, so a part can be lifted out
without collisions.

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
| Tap-to-choose buttons that write a request | `72-l2-mix.html` |
| One line dressed in nine looks | `73-l2-looks.html` |
| A Markdown file shown as a tab | `md_view()` in `build.py` |

Adapt the pattern. Do not copy the example content: every company and figure in it is invented.

## Rules

The skill's "Rules that never bend" section is binding. The three that matter most:

1. No invented facts. Mark gaps as `[needs: ...]`.
2. A voice is a style. Never attribute words to the person who inspired it.
3. Stop before anything is posted, sent or published. A person decides.

## Running without skill support

In an assistant that cannot load skill folders, paste
[`SKILL-single-file.md`](../../skills/artifact-studio/SKILL-single-file.md) into the project
instructions. It condenses the skill and its cards into one file. The full reference files have
more detail and take precedence where the two differ.

## Known limits

- The skill has not yet been run end to end by a second agent. Treat the first runs as tests and
  record what went wrong.
- Video handling is specified but has no worked example in the demo.
- The reference files describe four recipes and seven voices. A request outside them falls back
  to the one-page report and the practical instructor voice.
