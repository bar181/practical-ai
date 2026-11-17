# Friction with the guide

Ordered from most to least damaging. Each entry quotes the line, says what was unclear, and says what I did.

## 1. Attached pictures silently replace the voice's look

> "4. **Look.** In order: the person's design spec; colours taken from an image they supplied; the voice's default look."

> Teacher: "Black and white, one highlight, monospace code."

The person attached two pictures as illustrations, not as a colour source. Read as written, any
attached picture outranks the voice's look, so the Teacher's black and white never applies once a
picture is in the message. I doubt that is intended, and the guide does not say. It also says
"an image": with two pictures it gives no way to pick one. I took the colours from the cartoon
(first named, wider range) and kept the Teacher's arrangement: pale page, near-black text, one
highlight. That is a compromise the guide does not describe.

## 2. Required sections with no content, and no rule for them

> Scrolling explainer: "Title and why it matters."

> Teacher: "A harder case. Check-yourself questions."

> "You never add facts."

The notes give no "why it matters", no check-yourself questions and exactly one variation that
could pass for a harder case. The guide says the recipe "sets which sections the page must have"
but not what to do when the content has nothing for a required section: leave it out, mark
`[needs: ...]`, or write it myself. I left "why it matters" out and listed it under Missing. I
wrote the questions myself from the notes, which sits close to the line of adding content.

## 3. Content that has no slot in the voice's order

> "Where the recipe and the voice disagree, the voice sets the order, the counts and the headings."

The person's notes include a five-minute exercise. Neither the scrolling explainer nor the Teacher
order has a place for it. The guide covers a recipe and a voice disagreeing, but not content that
fits neither. I put it under check yourself. A guess.

## 4. How the recipe's sections and the voice's order fit together

> Recipe: "A diagram or image that stays on screen. One block per stage: who, what happens, one fact."

> Teacher: "Pseudocode or a diagram stepped through."

Is the recipe's pinned diagram the same thing as the Teacher's stepped diagram, or are there two?
Where do the recipe's stage blocks go inside the Teacher's seven-part order? Nothing says. I
merged them: one pinned strip of four steps, with the stage blocks scrolling under it, placed at
the Teacher's "diagram" position.

## 5. The person's order against the voice's order

> Teacher: "One question. An everyday analogy, very large. ..."

The person wrote "start with an everyday analogy". The Teacher order starts with a question. The
guide says "What the person says in this request overrides" only about the preferences file, and
"Follow them exactly" only for the advanced row. It never says whether an order given in the
request beats the voice's order. I made the question the title and the analogy the first block.

## 6. The request fits none of the three rows

> "One sentence (beginner)" / "Names recipe, voice, look, parts (advanced)" / "Use the artifact-studio skill (expert)"

This request is several sentences plus notes, describes a voice without using its table name
("like a great teacher"), and names no recipe, look or parts. No row covers it, so the length of
the note is undefined. I wrote the full note. It is also unclear whether a description of a voice
counts as "named".

## 7. Page or deck, for a class

> "When the person says what they need and not which kind, choose for them: a page to be read, a deck to be presented, a post to be scrolled past."

> Workshop deck: "a promise, a picture, three steps, one worked example, an exercise, a check, a card to keep"

A class is presented to, and the workshop deck's list matches these notes almost item for item
(picture, steps, worked example, exercise, check). But "explain" and "teacher" point at the
scrolling explainer. There is no tie-break, and voices are never mapped to deck "manners", so I
could not tell whether a Teacher-voice deck exists. I chose the page.

## 8. "Who, what happens, one fact" forced onto a one-person procedure

> "One block per stage: who, what happens, one fact."

Every step here is done by the learner, so "who" is "You" four times. "One fact" does not fit a
step with three checks (step 4) or a step that is all instructions (step 3). The guide does not
say a field may be dropped. I kept all three and relabelled them Who, Do, Know.

## 9. "Steps" against "complete at rest"

> Teacher: "The reader steps and answers."

> "The page is complete at rest" / "Everything is readable before any animation runs"

Stepping normally means revealing one thing at a time. Complete at rest forbids hiding anything.
So "the reader steps" shrinks to moving a highlight over text that is already all visible. If
that is the intent, say so.

## 10. Script-driven buttons with scripts off

> "Every button does something, and it works by keyboard"

> "With scripts off, the first screen shows content and any tabs still switch"

The guide gives the radio-button trick for tabs only. A "Next" button needs a script, so with
scripts off it is a button that does nothing, which breaks the first line. I hid the button until
the script runs. The guide does not say this is allowed.

## 11. The scroll rule is underspecified

> "Tie movement to scrolling with a small script that sets one CSS custom property from the scroll position ... Add the CSS-only form inside `@supports ((animation-timeline: view()) and (animation-range: entry))` so it still moves with scripts off."

- It does not say how to stop the script form and the CSS form both running at once. I added a
  class from the script and scoped the CSS form to pages without it.
- For a marker that shows the current step, the CSS-only form needs four named view timelines,
  `timeline-scope` and insets. That is far more than the sentence suggests.
- It is unclear whether marking the current step counts as "movement" at all.

## 12. "Moving parts" is not defined

> "At most three moving parts on a page."

Does a `details` that opens on tap move? A sticky strip? A highlight that changes? I counted every
part that changes on screen and landed on exactly three, but I could argue for one or for four.

## 13. The Teacher's look is stated two ways, and "highlight" against "accent"

> Voices table: "Black and white, one highlight, monospace code."

> Look defaults: "Teacher: white with one highlight."

> Design ideas: "One accent, used only for what to act on."

Two wordings of the same default. And is the Teacher's highlight the accent? The highlight marks
where you are, which is not something to act on, so the two rules pull apart. I used the accent
for the button and link underlines, and a soft step of it as the highlight.

## 14. The photo colour rules break on a cartoon

> "The most vivid that is not skin or sky becomes the accent" / "Lightest, or a paler step of the largest, becomes the background."

In this cartoon the faces are teal and so is the wall, and teal was the most vivid colour
measured. I treated it as skin and background and took the red-orange. "Lightest, or a paler step
of the largest" gives two options and no way to choose. The rule also says to check text contrast
but not what to do when the accent fails it against the background (here 3.1 to 1). I kept the
accent off all text.

## 15. Pictures with no stated purpose

> "6. **Parts.** One component per section that needs one. Each must carry content."

The person attached two pictures and said nothing about where they go or what they mean. The
guide has rules for alt text and cropping but none for placing a picture whose role is unknown,
and intake says to ask only about the audience or the job. Any caption tying them to the lesson
would be an invented claim. I placed them at the start and the end with no captions.

## 16. "Cropped to the subject at phone width"

> "Images: alt text that says what is shown, cropped to the subject at phone width, saved without location data."

Crop the file, or crop with CSS? I cropped the wide cartoon with CSS at phone width and showed it
whole on wider screens.

## 17. Tap targets and links inside a sentence

> "Tap targets 44 pixels."

A link inside a line of text is about 26 pixels tall. The guide gives no exception. I moved each
in-text link onto its own line with padding.

## 18. "Avoid: Two new ideas in one step" against the person's own steps

> Teacher, Avoid: "Two new ideas in one step"

The person's step 3 holds several instructions. Following the avoid line strictly means splitting
their step and changing their numbering. The guide does not say which wins. I kept their steps.

## 19. The front-end design skill line

> "If a front-end design skill is available (for example `frontend-design`), load it as well."

It does not say which wins when that skill and this guide disagree. In this test, rule 1 (read
only the named files) conflicts with it. I did not load any skill.

## 20. What counts as a preferences file

> "a file named `preferences.md`, or a section headed Preferences in your instructions"

An assistant with a memory feature may hold saved preferences that are neither of these. The
guide does not say whether those count. I treated the request as having no preferences file.

## 21. Small ones

- "A heading on every section, key word first" works against "an everyday analogy, very large":
  a normal heading above the analogy competes with it. I made that heading a small label.
- "Example content is labelled as an example": unclear whether this means filler I invent or the
  person's own example. I labelled the person's good ask "Example".
- "Seven stages at most" and "Three or four numbers" are clear. The Teacher row gives no counts at
  all, although the outline step says "the voice sets ... the counts". How many check-yourself questions?
