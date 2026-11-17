# Friction with the guide

Blunt list, worst first. Each item quotes the line.

## 1. There is no recipe for a picture-led page, and the fallback produces nonsense

> "Pick one from the table. If named, use it. If none fits, use the one-page report."

> "Otherwise take the recipe's first voice."

The request is three photo effects and nothing else. None of the four "Use when" lines is true of it. Followed exactly, the guide hands a photo showcase to the one-page report (numbers, a trend chart, a breakdown table) and then to the analyst voice, whose look says:

> "One picture at most, at the top."

and whose only other voice option, the executive brief, says "no images, no motion". So the guide's own "With a photo" parts list (pan and zoom, photo-filled type, flip card) can never be reached through a recipe and voice that welcome them unless the person names a recipe. I obeyed the fallback, used the report for a title and a two-sentence summary, and listed seven report sections as Missing. That is obedience, not a good outcome. The storyteller or keynote look would have suited the request far better, and the guide forbade me from choosing either. This was the single biggest problem.

## 2. The guide does not say what to do when the missing thing is the thing that was asked for

> "A gap is never filled with a guess. If the page would mislead without it, a number, a name, a date or a price the reader will act on, mark it on the page as `[needs: ...]`. Otherwise leave the page clean and list the gap under Missing."

> "Ask at most two questions, only if you cannot tell the audience or the job."

The person asked for "one word in huge letters" and did not give the word. Leaving the page "clean" means leaving out a part they named. Setting `[needs: your word]` in huge letters is absurd. Guessing is banned. And the questions rule does not even allow asking, because the word is neither the audience nor the job. Same problem for the back of the postcard. I picked a descriptive word and recorded it, which is a guess by another name.

## 3. Three rules about the look collide and the guide does not rank them fully

> "Look. In order: the person's design spec; colours taken from an image they supplied; the voice's default look."

> Voices table column: "Look and behaviour"

The look order says photo colours beat the voice's default look. But the voice column mixes look and behaviour in one cell ("Quiet, one data colour, grey for comparison, source under each chart. One picture at most, at the top."). Which words in that cell are "look" (overridden) and which are "behaviour" (kept)? Unstated. I kept "quiet" and full-sentence headings and dropped the rest.

## 4. The photo colour rule breaks on a sunset

> "The most vivid that is not skin or sky becomes the accent, used sparingly."

The picture is about 75% sky and the rest is water reflecting that sky plus black silhouettes. Every vivid colour in it is sky. I took the most vivid colour from the water and called it "not sky", which is a technicality.

> "Darkest becomes text. Lightest, or a paler step of the largest, becomes the background."

For a dark picture this forces a pale page around a dark photo. The literal "lightest" here is a loud orange (`#f6a35d`), unusable as a page background. No rule covers dark or low-key pictures, and nothing says which of "lightest" or "a paler step of the largest" to prefer. Also "Take the five or six colours that cover most of the picture" gives no method. A chat assistant with no tools would be eyeballing hex values.

## 5. The motion rule assumes all movement is scroll-driven

> "Tie movement to scrolling with a small script that sets one CSS custom property from the scroll position, so it behaves the same in every browser."

Read literally, a timed animation is not allowed. But "slow pan and zoom" is in the guide's own parts list and is a timed effect by nature, and a flip card moves on tap. The guide says nothing about timed motion: how long, whether it loops, whether it needs a pause control. I added a pause control from general accessibility practice, not from the guide.

## 6. The script form and the CSS-only form fight each other, and the guide does not say how to stop that

> "Add the CSS-only form inside `@supports ((animation-timeline: view()) and (animation-range: entry))` so it still moves with scripts off."

In a browser that supports both, the CSS animation overrides the script-driven value unless you guard it. I had to invent a `js` class on the root and scope the CSS-only form to `html:not(.js)`. The guide should give that pattern. It also gives no reduced-motion pattern beyond "readable ... with reduced motion on".

## 7. "Real controls" and "scripts off" pull in opposite directions for a flip card

> "Real controls for interaction: `button`, `input`, `details`, `select`."

> "With scripts off, the first screen shows content and any tabs still switch"

Tabs get an explicit scripts-off recipe (radio buttons and labels). The flip card, before and after slider and swipe gallery get none. A `button` flip is dead with scripts off. I used a tick box and labels so it still turns, but the guide never says whether other interactive parts must work with scripts off, and "Every button does something" does not say under which conditions.

## 8. "Moving part" is never defined

> "At most three moving parts on a page."

Is a flip card a moving part? A pause control? The same picture drifting inside letters? I counted pan and zoom, the drifting fill and the flip as three and stopped. Under a stricter reading the request alone already uses the whole budget, under a looser one it uses one.

## 9. The parts are names with no definitions

> "With a photo: slow pan and zoom, parallax window, photo-filled type, pinned photo tour that zooms per paragraph, self-drawing line art, before and after slider, frosted glass card, bento grid, swipe gallery, flip card."

No description, no markup pattern, no accessibility note for any of them. What goes on the back of a flip card? How is photo-filled type exposed to a screen reader? What keeps a word from overflowing 390 pixels? All left to the builder. This contradicts the test's "do not improve on it from your own taste", because here taste is all there is.

## 10. "Each must carry content" versus a flip card with nothing for its back

> "One component per section that needs one. Each must carry content."

The request gave no words for the back of the postcard. I reused the one content-like sentence in the person's notes. The guide gives no way to tell content from remarks addressed to the assistant inside "My notes" ("One picture of my own is attached" is plainly a remark; "Any picture works: ..." could be either).

## 11. The request table has no row for this request

> "Names recipe, voice, look, parts (advanced) | Follow them exactly"

The person named parts only. Not a one-sentence request, not all four named, not "use the artifact-studio skill". The table does not say which row a partial request falls in or how long the note should be. I followed the named parts exactly and wrote a full note.

## 12. Contrast rules cannot be applied to picture-filled letters or to an accent drawn from a photo

> "Ordinary text needs a contrast of 4.5 to 1 against its background, large text 3 to 1."

Letters filled with a picture have no single colour, and the fill moves. No guidance. Separately, the photo-derived accent came out at 2.3 to 1 against the photo-derived background. The guide checks text contrast only and is silent on control boundaries, so I added a dark outline on my own.

## 13. Image rules that a pan contradicts or that cannot be verified

> "Images: alt text that says what is shown, cropped to the subject at phone width, saved without location data."

A pan and zoom deliberately moves off the subject, and a square picture in a tall phone frame cannot show the whole subject at once. "Saved without location data" assumes the assistant can inspect and re-save files; many chat assistants cannot. It also does not say whether a file name (`toronto.jpg`) counts as supplied content that may be used in alt text or as the word.

## 14. Intake asks for things this kind of request does not have

> "Find the content, any media, the audience, the one job of the page, and where it will be seen."

A picture showcase has no stated audience and no action for a reader to take. The guide has no default for "no job".

## 15. Smaller points

- > "If a front-end design skill is available (for example `frontend-design`), load it as well."
  It does not say which wins when that skill and this guide disagree. Under the test rules I did not load one.
- > "Seven named colour tokens at most"
  Unclear whether shadows, the colours inside the photo, or tints of a token count. I used six and derived the shadow from a token.
- > "Show the page as a rendered page if you can"
  Conflicts with being asked for a file. Minor.
- > "Design at 390 pixels wide first."
  Nothing about what wide screens should do with a 1024 pixel picture. I capped the opening frame at 1200 pixels wide to limit blur.
- The voices table has a "Personal story" voice that no recipe lists, so the "first voice" rule can never select it.
- The checklist item "Follows the voice's order and its 'avoid' line" cannot be met in any real sense here: the analyst order is seven content blocks and the request supplied none of them.
