# Friction with the guide

Ordered by how much each one cost. Items 1 to 4 changed what the page is. The rest were smaller guesses.

## 1. The look rules contradict each other for a keynote with photos

> "4. **Look.** In order: the person's design spec; colours taken from an image they supplied; the voice's default look."

> "Darkest becomes text. Lightest, or a paler step of the largest, becomes the background."

> "Keynote | ... | Black, one typeface, enormous numbers."

The person supplied pictures and named the keynote voice. Followed literally, step 4 puts photo colours above the voice's look, and the photo rule produces a pale page with dark text. The keynote row says black. Nothing says which wins. I had to argue that "keynote-style" counts as "the person's design spec" to get a black page. A different assistant will produce a pale grey or cream keynote and also be "following the guide".

Related gaps in the same rule:

- It says "an image". The person sent three, with three unrelated palettes (grey, brown, orange). No rule for which picture to use.
- "The most vivid that is not skin or sky becomes the accent". In the sunset picture the only vivid colour is the sky. In the fog picture nothing is vivid. The rule yields no accent and does not say what to do then.
- Is "Black" in the "Look and behaviour" column the same thing as the "default look" in step 4, or part of the voice that step 4 cannot override? The table and the "Defaults by voice" line say it twice, differently ("Black" and "black and white").

## 2. "Seven stages at most" against "one idea per screen"

> "One block per stage: who, what happens, one fact. A closing line. Seven stages at most."

> "One idea per screen, screens snap." / Avoid: "more than twelve words a screen"

The guide never says what a stage is under the keynote voice. If a stage is a screen, seven screens of twelve words hold 84 words, and the notes hold about 118 words and at least 13 separate ideas. It cannot be done without dropping content. I read "stage" as one of the keynote's six beats and let each beat run over several screens (17 in all). That is a guess. The tiebreak line does not settle it:

> "Where the recipe and the voice disagree, the voice sets the order, the counts and the headings. The recipe sets which sections the page must have."

"Counts" could mean the voice overrides "seven stages", but the keynote row gives no count to replace it.

## 3. The recipe's block contents cannot fit the voice

> "One block per stage: who, what happens, one fact."

"Who, what happens, one fact" in twelve words is not possible for most stages, and the notes have no "who" for most of them. The guide does not say whether a voice can waive what goes inside a section, only its order, counts and headings. I dropped the who, what, fact shape entirely. I do not know if that is allowed.

## 4. The `[needs: ...]` rule is hard to parse and misses the common case

> "If the page would mislead without it, a number, a name, a date or a price the reader will act on, mark it on the page as `[needs: ...]`. Otherwise leave the page clean and list the gap under Missing."

The sentence does not read as grammar. I think it means "if the gap is a number, name, date or price the reader will act on". The notes say "paste one link" and give no link. A link is not in the list, and the page does not mislead without it. It is just useless at that step. I marked it, but the rule as written points the other way. The checklist uses a different test again: "A gap that would mislead the reader". Two tests, neither covers "the reader cannot act".

Also unanswered: does the marker count towards the keynote's twelve words? I counted it.

## 5. Title first or world first

> "Title and why it matters." (recipe, first section)

> "The world as it is, as one line or one painful number." (keynote, first in the order)

The voice sets the order, the recipe sets required sections. So the title must exist but cannot be first. I made it a small wordmark on screen 1 above the world line. The guide does not say if that is the intended answer, or whether the wordmark's two words count towards twelve. I counted them.

## 6. What counts as a word

> "more than twelve words a screen"

Not stated: whether numbers count ("20 templates" is one word or two), whether small labels count, whether a `[needs: ...]` marker counts. With six numbers and labels on one screen the answer decides whether proof takes one screen or two. I counted everything and used two.

## 7. Which row of the request table this is

> "One sentence (beginner)" / "Names recipe, voice, look, parts (advanced)" / "'Use the artifact-studio skill' (expert)"

The message is several lines, names a voice but no recipe, look or parts, and says "read the design guide and follow it". It fits none of the three rows. The row decides whether the note is four lines or a full list. I wrote the full note.

## 8. Page or deck, and two names for one style

> "Keynote" (voice table) / "a visionary deck (black, huge type, a villain, one rule, three things, one number, 'one more thing')"

"Keynote-style page: one idea per screen" matches the keynote voice and also the visionary deck. The two have different required contents. The deck's list (a villain, one rule, three things, one number, "one more thing") could not be filled from these notes without inventing. The guide gives no rule for a request that sits between them except "a page to be read, a deck to be presented". I went with the word "page". The two names (keynote, visionary) for what looks like the same style made me unsure they were meant to be different things.

## 9. The image that "stays on screen" against snapping screens

> "A diagram or image that stays on screen." (recipe)

> "A picture fills the screen or sits beside one short paragraph." (keynote)

Three pictures, and the recipe wants one that stays. The guide does not say for how long it must stay, whether it may also fill the screen, or whether other pictures are allowed once one is pinned. I pinned the fog picture for three screens and used the other two once each.

## 10. "svh with a pixel cap" gives no cap and breaks the keynote

> "Use `svh` with a pixel cap, not bare `vh`."

No value is given. Any cap means that on a window taller than the cap the next screen shows at the bottom, which breaks "one idea per screen". I used 1200 pixels and accepted the break. The guide should say the value, or say that full-screen snapping screens are exempt.

## 11. The two forms of scroll movement fight each other

> "Tie movement to scrolling with a small script that sets one CSS custom property from the scroll position ... Add the CSS-only form inside `@supports ((animation-timeline: view()) and (animation-range: entry))` so it still moves with scripts off."

If both are present and scripts are on, both drive the same element. The guide does not say how to keep them apart. I had the script add a class and limited the CSS form to pages without that class. Also unclear: "one CSS custom property" means one for the whole page or one per moving part? And is a count-up that starts when a screen arrives "movement tied to scrolling" that needs a CSS-only form? I gave it none.

## 12. Count-up numbers against "complete at rest"

> "Big numbers that count up." / "Everything is readable before any animation runs"

A count-up shows wrong numbers for a moment by design (0, 7, 15, then 20). The guide lists the part and the rule without saying how they live together. I kept the real value in the page, start the count only when the screen arrives, skip it with motion off, and hide the changing digits from screen readers behind a fixed copy. None of that is in the guide.

## 13. Accent and buttons on a page with nothing to click

> "One accent, used only for what to act on."

> "Every button does something, and it works by keyboard"

The keynote look is "black and white", and the notes give no link, so there is nothing to act on by clicking. The guide does not say whether a keynote page may have an accent at all, or whether a snapping page needs next and back buttons. The deck paragraph demands "Arrow keys, buttons and a tap" but only for decks. I used no accent and no buttons and left movement to the browser's own scrolling.

## 14. "A section headed Preferences in your instructions"

> "If there is a preferences file (a file named `preferences.md`, or a section headed Preferences in your instructions), read it before you choose anything."

A chat assistant often carries general stored preferences about the person (tone, punctuation, answer length) that have nothing to do with page design. The wording sweeps those in. It is not clear whether they count, or whether I must list them in the note as "preferences applied". I treated only a page-design preferences file as in scope, found none, and said so.

## 15. The front-end design skill has no rank

> "If a front-end design skill is available (for example `frontend-design`), load it as well."

I loaded one. It pushes for distinctive typefaces, personal aesthetic risk and a palette invented for the brief. The guide demands system fonts, a look set by the voice, and "black". The guide never says which wins. I let the guide win everywhere it has a rule, which left the skill almost nothing to do.

## 16. Smaller guesses

- > "saved without location data"

  The pictures arrive from the person. The guide does not say how to check, or whether to re-save them (which lowers quality). I inspected them, found no metadata, and embedded them unchanged.

- > "cropped to the subject at phone width"

  A square picture that fills a tall phone screen loses about half its width. The guide does not say whether that is acceptable for a full-screen picture. I set the crop point on the house and the tower.

- > "Bullet lists" (keynote, avoid)

  Three start steps are a sequence. The guide does not say if three short sentences on one screen are a bullet list. I gave each step its own screen.

- > "Proof as enormous numbers."

  Six numbers, and "one idea per screen". The guide does not say whether one screen may hold several numbers. I put three on each of two screens.

- > "Greys carry a trace of the brand colour."

  There is no brand colour. I took the grey from the fog picture.

- The Layout table has no row for a one-idea screen. The closest is "Do one thing: Name top left, message low on the left, one button low on the right." I used the name at top left and left-aligned type, and could not tell if the row was meant to apply.

- > "5. **Outline.** ... List every gap and assumption."

  Step 5 does not say where to list them. I assumed the delivery note.

- > "Seven named colour tokens at most"

  Not stated whether a translucent shade over a photo is a colour token. I counted it.
