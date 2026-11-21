# Brief for the seven tone examples

You are making one tone's worked example for Tone Studio. Read, in this order:
1. `projects/tone-studio/base/SKILL.md`: the tones, the formats and the rules. Follow it.
2. `projects/tone-studio/base/examples/source-content.md`: the ONLY source of facts.
3. For design ideas only: `projects/artifact-studio/level-2-files/artifact-studio/references/voices.md`
   (how your voice looks and behaves on a page) and
   `projects/artifact-studio/level-2-files/artifact-studio/references/effects-index.md`.

## Make three files in `projects/tone-studio/base/examples/<tone>/`

1. **`landing.html`: a cinematic landing page, 200 to 400 words of visible copy.**
   - The section order is your tone's order from the skill, adapted to a landing page. The words
     are the point: the tone must be obvious from the order and rhythm alone.
   - One self-contained file: inline CSS and at most a small inline script, no libraries, no build,
     system fonts or a font stack only (no web font downloads), works offline.
   - Photos only from `../img/` (bulb, puzzle, class, sunset, lake, home, fog, heart .jpg). Open the
     ones you use to write true alt text. Give them one shared colour grade suited to the look.
   - The look: your voice's default look from voices.md, so the seven pages look different.
   - Motion: one or two effects at most from the effects index, written in plain CSS and a few lines
     of script, for example the letterbox opening with a masked title rise, the grade, the statement
     whose words light up on scroll, the clip, the stack. Executive brief has no motion.
   - Must work and read completely with JavaScript off and with prefers-reduced-motion: reduce
     (show final states). Phone first at 390 px: no sideways scrolling, tap targets 44 px, text
     contrast 4.5:1, one h1, real buttons or links, visible focus.
   - The call to action links to `#` and shows the text `[needs: registration link]` nearby or in
     its title, because the link is unknown.
   - A small footer line: "Invented example for Tone Studio. The course, people and numbers are made up."
2. **`post.md`: one post in the same tone,** of the type and length given for your tone below,
   written as it would be posted. Start the file with a heading (the tone and the post type), then
   the post in a quote block, then "**Words:** N" (count the post only).
3. **`notes.md`: a facts check,** in the skill's facts-check table format, covering both the page
   and the post: every fact you used, Kept or Kept-reworded; then Gaps (every `[needs: ...]`); then
   one line on how the order follows the tone.

## Rules

- Use only facts in source-content.md. Do not add numbers, results, quotes, people, dates or
  promises. Priya's memory and Marta's words may be used only as written (shortening is fine;
  changing words is not).
- Never name a real communicator who inspired the tone.
- No em dashes. Plain English. Sentence case headings.
- Do not edit any other file.

## Your tone, look and post

| Tone | Look | Post type and length |
| --- | --- | --- |
| visionary | Black, one typeface, enormous type, one idea per screen | LinkedIn post, 100 to 150 words |
| storyteller | Colours from the photograph, large serif, slow push-ins; the hero is the hook (a moment, a time, a place), then the story beats | Facebook post, 200 to 300 words |
| emotional | Faded film, warm, first person | Facebook post, 150 to 250 words |
| explainer | White with one highlight colour, monospace for the worked example | Blog article, 300 to 400 words |
| practical-instructor | Field guide: two colours, tick boxes, numbered timed steps | LinkedIn post, 120 to 180 words |
| analyst | Quiet, one data colour, grey for comparison, a source under each number | LinkedIn post, 120 to 180 words |
| executive-brief | A paper memo, serif, one accent, no images, no motion | A short blog post for partners or a board, 200 to 300 words |

When done, verify: open landing.html with Playwright (Chrome at /usr/bin/google-chrome) at 390x844
and 1280x800, with JavaScript on and off, and with reduced motion; fix anything broken; count the
visible words of the page (200 to 400) and of the post. Report in under 120 words: files written,
the two word counts, and anything you could not do.
