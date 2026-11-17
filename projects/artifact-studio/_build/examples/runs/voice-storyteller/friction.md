# Friction with the guide

Ordered by how much each one cost. Quotes are from `AI-INSTRUCTIONS.md`.

## 1. No look exists for the storyteller voice when there is no photo. Biggest problem.

> "**Look.** In order: the person's design spec; colours taken from an image they supplied; the voice's default look."
> "Storyteller: the photo's colours."

The fallback of the fallback is the thing that is missing. The person said "Use my photo large" and attached nothing. All three rungs of the ladder were empty and the guide has no fourth. I invented a provisional palette from the story (an evening, a lamp). That is exactly the "own taste" the guide is meant to remove. The guide needs a line such as "no photo: use X and say so".

## 2. The guide does not say what to do when promised media is missing.

> "If the page would mislead without it, a number, a name, a date or a price the reader will act on, mark it on the page as `[needs: ...]`. Otherwise leave the page clean and list the gap under Missing."

A missing photo is not a number, name, date or price, so by the letter the page should be left clean with no photo space. But the person asked for the photo large and the whole look hangs on it. I held a large marked space. I do not know if that is right. The sentence itself is also hard to parse: it is unclear whether "a number, a name, a date or a price" is the full list or examples.

## 3. A voice was named and no recipe. The guide only maps recipe to voice.

> "**Voice.** Pick one from the table. If named, use it. Otherwise take the recipe's first voice."
> "If none fits, use the one-page report."

There is no rule for the other direction. Storyteller is listed under one recipe only, the landing page. The content is an internal trial result with a decision date, which reads like a one-page report or a proposal, and neither lists the storyteller. The guide never says whether the Voices column is a restriction or a suggestion. I took the landing page because it was the only one that lists the voice, then had to bend most of its sections.

## 4. The landing page sections do not fit a reader who is not a customer.

> "Promise in one line with a number. One button. A picture of the result. Three things you get. Three steps. One customer's words. Price. Three real questions. Promise and button again."
> "The recipe sets which sections the page must have."

- "One customer's words" is a must-have section, and "Customer quotes are real or absent" forbids filling it. The guide does not say whether a must-have section may simply vanish or must be marked on the page. I dropped it and listed it under Missing.
- "Three real questions": real according to whom? None were supplied. I wrote three that the notes answer. That may be exactly what "real" is meant to forbid.
- "A picture of the result": is a chart a picture? Is the person's photo meant to be this picture? Not said. I used the chart.
- "Promise": the notes hold results, not a promise. I used a result worded as a result.

## 5. "The company before the fourth beat" collides with the content and with the recipe.

> Avoid: "The company before the fourth beat."
> Recipe: "Promise in one line with a number. One button." (first two sections)
> Order: "The problem at three depths."

The recipe opens with the company's promise. The voice bans the company for three beats. "The voice sets the order" settles that one. It does not settle this: the only numbers that describe the problem are the company's own (26 hours, 12%). To tell the problem at any depth before beat 4 I had to show them as "one home renovation company" and reveal the company in beat 4. I cannot tell whether an unnamed company counts as "the company". If it does, beat 3 can hold no numbers at all.

## 6. "The problem at three depths" is not defined.

> "The problem at three depths."

Three depths of what? I guessed: one person's evening, how ordinary it is, how rare a quick answer was. Another reader would guess outer problem, inner feeling, principle. The second and third of those would need feelings and opinions that are not in the notes, which the no-invention rule forbids. The guide should name the three depths and say what to do when the notes cover only one.

## 7. "Hook with a time and place" and "empathy" ask for things notes rarely hold.

> "A hook with a time and place." "A guide: empathy, then proof."

The notes gave a time and no place, and no statement of feeling from the company. The guide does not say whether to omit, mark, or ask. I omitted the place and built the empathy line from a number. Both are listed in the note.

## 8. The avoid line on invented customers gives no test and no action.

> Avoid: "An invented customer shown as real."

The notes say "A customer story we may tell". I cannot tell real from illustrative, or whether she agreed to be named. The guide does not say whether doubt means mark on the page, label as an example, or only note it. I marked it on the page.

## 9. "One button" with nowhere to send it.

> "Every button does something, and it works by keyboard."
> "Stop before anything is posted, sent, paid or published."

No link or address was supplied. The guide does not say what a button should do in that case. I used an email link with no address, which does something but not much.

## 10. "Moving parts" is not defined.

> "At most three moving parts on a page."

Does a question that opens on tap count? Is one push-in effect used in three places one part or three? I counted one. A stricter reader could count five.

## 11. The motion rule is under-specified and its two halves fight each other.

> "Tie movement to scrolling with a small script that sets one CSS custom property from the scroll position ... Add the CSS-only form inside `@supports ((animation-timeline: view()) and (animation-range: entry))` so it still moves with scripts off."

- "One CSS custom property": one on the page root, or one name set on each moving element? A push-in per element needs progress per element. I used one name, set per element.
- If the script and the CSS-only form both run, the element is driven twice. The guide does not say how to keep them apart. I had the script add a class and wrote the CSS-only form to apply only when that class is absent.
- A cropped photo frame normally uses `overflow: hidden`, which makes the frame its own scroll container, so `view()` on the image inside it would track the frame and not the page. I used `overflow: clip` to avoid that. I did not test the `hidden` case. Worth a line in the guide.

## 12. Proof, "three things you get" and "failure beside success" all want the same numbers.

> "A guide: empathy, then proof." "Three things you get." "Failure beside success."

With one small set of facts, the same four numbers land in beats 4, 7 and 8. The guide has no rule on repeating a number. It also does not say whether failure and success are what happened or what will happen. What will happen would be an invented fact, so I used before and during.

## 13. Comparison bars and "one data colour".

> "One data colour, which is its own token and never the accent."

A before-and-after chart needs a second, quieter bar. The analyst voice says "grey for comparison". Nothing says so for other voices. I used the border token for the before bars and labelled them in words.

## 14. "Unit and source underneath" when the source is the person's own notes.

> "Unit and source underneath."

There is no source beyond the message. I wrote "Source: our own notes on the trial". The guide should say what to write here.

## 15. The front-end design skill and the guide disagree, and no order of precedence is given.

> "If a front-end design skill is available (for example `frontend-design`), load it as well."

The skill I loaded says to avoid small labels above content; the voice says "story beats named in small type". The skill says to take aesthetic risk and to confirm the subject with the client; the test rules say follow the guide and ask nothing. The skill warns against cream paper, serif and a clay accent, which is roughly what a photo of a renovation will produce under "colours from the photograph". I let the guide win each time, but the guide never says it should.

## 16. Which note length applies to a request in the middle?

> "One sentence (beginner)" / "Names recipe, voice, look, parts (advanced)" / "'Use the artifact-studio skill' (expert)"

This request was three sentences, described a voice without naming it, named one part and no recipe or look. It fits none of the three rows. I wrote the note in full.

## 17. "Story with the customer as hero and us as guide" matches two things in the guide.

> Voice: "Storyteller". Deck manner: "a story deck (the customer as hero: person, problem, guide, plan, ask, stakes, ending)".

Only the words "on one page" told me which. The two lists of beats also differ (eight beats against seven, "hook" and "character" against "person"), with no reason given.

## 18. Smaller points

- > "a section headed Preferences in your instructions"
  Unclear what counts as "your instructions" for an assistant with no project. I treated it as "no preferences file supplied".
- > "Totals add up and derived numbers show their working"
  No word on where the working goes. Inline working ("100 less 12") is heavy in a story voice. I put most of it in chart captions.
- > "Images: ... cropped to the subject at phone width"
  Cannot be done or checked without the image. No rule for the empty case.
- > "Ask at most two questions, only if you cannot tell the audience or the job."
  This request was that case: the story form points at customers, the facts point at the owners. The test forbade asking. In real use the guide's cap of two questions would have been spent here, on the single choice that shapes the whole page.
