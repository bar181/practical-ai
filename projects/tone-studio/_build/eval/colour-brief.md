# Brief: rebalance one tone page to 60-30-10

You are revising one existing page: `projects/tone-studio/base/examples/<tone>/landing.html`. Keep
its words, its order, its photos, its accessibility and its cinematic motion. Change only the
colour system and, where this brief says so, the background.

## The rule

- **60 percent: one dominant colour**, usually the page background. Calm.
- **30 percent: one secondary colour**, for text, structure and any dark or tinted panels.
- **10 percent: one bold accent**, and only one. Use it for the call to action and at most one
  emphasis per screen (a key number, a highlight, a progress fill). Never for body text, borders on
  every card, or decoration.
- Tints of the 60 and 30 colours are fine for borders and quiet panels. No second accent.
- Photos keep one shared grade, chosen to sit in the palette. A photo is not counted as colour.
- **Cinematic stays the focus:** keep the opening and the effects. "Clean background" means a flat,
  quiet 60 colour behind the text, not a dark gradient behind everything.

## Declare the roles

In `:root`, declare `--c60`, `--c30` and `--c10` as six-digit hex values and use them (directly or
through your existing tokens) for the dominant, secondary and accent colours.

## Measure, then adjust until it passes

Run `python3 workshop/tools/check_colour_balance.py projects/tone-studio/base/examples/<tone>/landing.html`
from the repository root. It hides photos and counts pixels by role at 1280 and 390 px. Aim for
the 60 role 45 to 75 percent, the 30 role 15 to 45, the 10 role 2 to 13. Iterate until both widths
say ok. If text alone cannot reach 15 percent for the 30 role on a light page, use the 30 colour
for one or two structural panels (for example the hero band or the footer), not more accent.

Then check: text contrast at least 4.5:1 for body text (3:1 for large text) on its real background,
including the accent button's label; no sideways scrolling at 390 px; it reads completely with
JavaScript off and with reduced motion (Playwright, Chrome at /usr/bin/google-chrome).

## Your tone's palette plan

| Tone | 60 | 30 | 10 (the only accent) | Background |
| --- | --- | --- | --- | --- |
| visionary | near black | white type | one electric colour (for example a vivid yellow or cyan) on the button and one number | dark, cinematic |
| storyteller | clean warm off-white page | deep ink, used for the dark graded photo hero band and text | one bold warm colour (a deep amber or vermilion, not a clay or terracotta) | clean light after the hero |
| emotional | warm paper | deep sepia brown text and photo borders | one rose or deep red | clean light, faded-film photos |
| explainer | white | near-black ink and grey structure | one marker yellow highlight, plus the button | clean light |
| practical-instructor | off-white | forest green structure and text | one bright orange for ticks, progress and the button | clean light |
| analyst | white | greys and near-black text | one data blue for bars, key numbers and the button | clean light |
| executive-brief | paper white | ink | one oxblood for the decision label and the button | clean light, no motion |

Edit only your page. Do not commit. Report in under 100 words: the three hex values, the measured
percentages at both widths, and the contrast of body text and of the button label.
