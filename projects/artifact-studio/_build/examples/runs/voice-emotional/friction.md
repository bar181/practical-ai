# Friction with the guide

Ordered by how much each one cost. The first three changed what the page is.

## 1. The look rules contradict the voice. Following them kills the "dark, warm room".

> "4. **Look.** In order: the person's design spec; colours taken from an image they supplied; the
> voice's default look."

> "Darkest becomes text. Lightest, or a paler step of the largest, becomes the background."

> "Personal story | ... | A dark, warm room. Serif type. Faded photographs with paper borders."

The personal story voice asks for photographs. So a personal story request always arrives with
images. Step 4 ranks those images above the voice's look, and the from-a-photo rule can only make a
light page with dark text. Read literally, the dark, warm room can never happen. I followed step 4
and built a light page. I expect that is not what the author wanted. The guide needs to say either
that keepsake pictures are content and not a colour source, or that the voice fixes light or dark
and the photo only supplies the hues.

## 2. No recipe fits the personal story voice, and the fallback is absurd for it.

> "If none fits, use the one-page report."

> "One-page report | ... Three or four numbers with their change. One trend chart ..."

> "Personal story | ... Avoid: Features, numbers, charts ..."

No recipe lists Personal story in its Voices column. The stated fallback demands numbers and a
chart, which the voice forbids. I picked Scrolling explainer on the "Use when" column alone. The
guide also never says whether the Voices column is a limit or only the source of the default in
step 3 ("Otherwise take the recipe's first voice").

## 3. The voice says to ask for a true memory. The person said theirs is invented. No path given.

> "An invented memory: ask for a true one"

> "Example content is labelled as an example"

The person wrote "This one is invented for the demo." The avoid line says ask. The checklist line
implies labelling is enough. The guide does not say which wins when the person has knowingly
supplied a demo memory. I labelled it at the top and bottom of the page. A stricter reader would
refuse to build.

## 4. "an image they supplied" is singular. I had three.

> "colours taken from an image they supplied"

> "Take the five or six colours that cover most of the picture."

Three pictures with three unrelated palettes: white and orange, near-black and bright colours,
grey-blue. No rule for which one, or for pooling them. I took the first, the balloon drawing. Any
other choice gives a different page.

## 5. A voice beat with no content: no rule.

> "What has changed and what has not."

> "If the page would mislead without it, a number, a name, a date or a price the reader will act
> on, mark it on the page as `[needs: ...]`. Otherwise leave the page clean and list the gap under
> Missing."

The gap rule is written for numbers, names, dates and prices. It does not clearly cover a whole
missing section of the voice's order. I dropped the beat and listed it. The checklist line "Follows
the voice's order" then cannot be fully met, and the guide does not say whether that is a fail.

## 6. "named in one sentence": the person gave two, and nothing that names a feeling.

> "The feeling, named in one sentence."

The person's line is two sentences and states a realisation, not an emotion. Does the count let me
edit their words? Does "named" mean an emotion word must appear? I joined the two with a semicolon
and added no emotion word. Both were guesses.

## 7. Recipe sections and voice order had to be mapped by guesswork.

> "Where the recipe and the voice disagree, the voice sets the order, the counts and the headings.
> The recipe sets which sections the page must have."

> "Title and why it matters. ... One block per stage: who, what happens, one fact."

"Why it matters" is the feeling, which the voice places third, not beside the title. "One fact" per
stage had to be squeezed from a note that holds one clause per keepsake ("It went in the drawer").
The rule tells me who wins but not how to map a recipe section onto a voice beat when they are
different things.

## 8. "One accent, used only for what to act on", on a page with nothing to act on.

> "One accent, used only for what to act on."

> "The most vivid that is not skin or sky becomes the accent, used sparingly."

The chosen recipe has no button and the person gave no link. I put the accent under the offer name
as the nearest thing. The guide also does not say whether a missing link is a `[needs: ...]` gap. A
link is not "a number, a name, a date or a price". I left the page clean.

## 9. "one CSS custom property" cannot do what the same sentence asks.

> "Tie movement to scrolling with a small script that sets one CSS custom property from the scroll
> position"

One page-level value cannot make each line arrive as it comes into view, because CSS does not know
where each line sits. I set one property name, `--p`, on each moving element. If that breaks the
rule, the rule and "Everything arrives slowly" cannot both be met.

## 10. Script form and CSS-only form: nothing says how to stop both running at once.

> "Add the CSS-only form inside `@supports ((animation-timeline: view()) and (animation-range:
> entry))` so it still moves with scripts off."

In a browser that supports both, both run and fight unless one is switched off. I gated the CSS
form behind a class the script adds. One line in the guide would save every reader working this
out.

## 11. "At most three moving parts": what is one part?

> "At most three moving parts on a page."

> "Everything arrives slowly."

If every line that fades in is a moving part, the voice breaks the limit by itself. I counted kinds
of movement (arrival, push-in), which gives two.

## 12. The request-size table has no row for this request.

> "One sentence (beginner) ... Names recipe, voice, look, parts (advanced) ... 'Use the
> artifact-studio skill' (expert)"

The request named a voice only, ran longer than one sentence, and linked the guide without the
magic phrase. I could not tell how long the note should be. I wrote the full one.

## 13. "Load a front-end design skill" brings in advice that contradicts the guide.

> "If a front-end design skill is available (for example `frontend-design`), load it as well."

The skill I loaded warns against a fade-in on every section, against a serif on a pale page with a
warm accent, and against small labels above content. The voice asks for all three. The guide does
not say which wins. I let the guide win.

## 14. "Show the page as a rendered page" against "stop before anything is published".

> "Show the page as a rendered page if you can: an artifact, a canvas or a preview."

> "Stop before anything is posted, sent, paid or published. A person decides."

Publishing an artifact is the usual way to show a rendered page, and it is also publishing. I wrote
the file and published nothing.

## 15. Two different descriptions of the same default look.

> "Personal story: faded film."

> "A dark, warm room. Serif type. Faded photographs with paper borders."

"Faded film" is never defined. Is it the same thing as the dark, warm room, or a treatment of the
photographs only? I treated it as a fade on the pictures.

## 16. Does the browser tab count as "before the end"?

> "The offer, named once, at the end." / "Avoid: ... the product name before the end."

The page title is read before anything else, and is what shows in a link preview. I kept the
product name out of it. The guide is silent.

## 17. Small ones

- "Two equal halves. On a phone the message comes first" against the recipe's "A diagram or image
  that stays on screen". On a phone a pinned picture sits above its text. I put only the heading
  first.
- "saved without location data": in a chat I can check an attached picture but the guide does not
  say whether to re-save it. I checked and left the files alone.
- "Seven named colour tokens at most": unclear whether a shadow made from a see-through step of the
  text colour counts as a token. I did not count it.
- "ask at most two questions" and "ask for a true one" give no fallback for a setting where asking
  is impossible. Here the test rules filled that hole. The guide itself does not.
