# Friction with the guide

Ordered by how much each one cost. The first three forced real guesses.

## 1. The practical instructor voice demands content the guide forbids me to supply

> "Practical instructor | The core idea in one sentence. One boxed analogy. Three numbers. Numbered steps with a time each. Three levels. Common mistakes. One next step."

against

> "No invented facts, numbers, names, customers or quotations."
> "A gap is never filled with a guess."

Four of the seven slots had nothing in the notes:

- **"One boxed analogy."** The notes held no analogy. The guide never says whether an analogy I write counts as "craft" or as an invented thing. I wrote one and declared it in the note. A stricter reader would have left an empty box.
- **"a time each."** The notes give one total ("about an hour"). The guide does not say what to do when the voice's count cannot be met. I showed the total and listed the gap.
- **"Three levels."** Levels of what? Skill, effort, ambition, price? There is no definition and no example anywhere in the guide. This was a pure guess. I read it as three depths of use.
- **"Common mistakes."** The notes record none. I turned the person's three rules round and renamed the heading "Mistakes to avoid", because "common" would be a claim. That bends "the voice sets ... the headings".

The guide needs one sentence saying what to do when a voice slot has no content: drop the slot, mark it, or build it from what is there.

## 2. When to mark a gap on the page is ambiguous

> "If the page would mislead without it, a number, a name, a date or a price the reader will act on, mark it on the page as `[needs: ...]`. Otherwise leave the page clean and list the gap under Missing."

The sentence does not parse cleanly. Is "a number, a name, a date or a price the reader will act on" a second condition, a list of examples, or a definition of "it"? My real cases:

- Per-step times: a number the reader would act on, but the page does not mislead without it. I left it unmarked.
- The chat tool's name: a name the reader needs in order to act, but the page does not mislead without it. I left it unmarked.
- How a new message reaches the chat project: not a number, name, date or price at all, yet the page really would mislead without it, because the five steps do not produce "drafted the moment a message arrives". I marked it.

So the one thing I marked is outside the list the sentence gives. The checklist says it more simply ("A gap that would mislead the reader is marked") and I followed that version.

## 3. No rule for picking a recipe when the voice is named and the recipe is not

> "2. **Recipe.** Pick one from the table. If named, use it. If none fits, use the one-page report."
> "3. **Voice.** Pick one from the table. If named, use it. Otherwise take the recipe's first voice."

The person said "practical one-page guide: the core idea, one analogy, then steps". That names a voice, not a recipe. "One-page" pulls toward the one-page report, whose voices are "Analyst, executive brief", so not the one asked for. Nothing says whether the "Voices" column is a restriction or a suggestion, or what happens when a named voice is not in the chosen recipe's list. I picked the scrolling explainer because it lists the practical instructor. There is no recipe for a plain how-to guide or checklist, which is the most obvious thing this voice is for.

## 4. Recipe and voice merge badly, and the tie-break rule does not cover the collisions

> "Where the recipe and the voice disagree, the voice sets the order, the counts and the headings. The recipe sets which sections the page must have."

- **Sections the voice has no place for.** The explainer requires "Title and why it matters" and "A closing line". The voice's order starts with the core idea and ends with "One next step". Where do the recipe's extra sections go in the voice's order? I put "why it matters" under the title and the closing line after the next step, which means the page does not end on the next step.
- **"One block per stage: who, what happens, one fact."** In a how-to the reader does every step, so "who" is "You" four times. That is filler, which collides with "Each must carry content". "One fact" per step also pushed me to hang facts on steps the notes never linked them to.
- **"A diagram or image that stays on screen"** against "Design at 390 pixels wide first". A pinned element on a phone eats the screen. The guide gives no height limit and no advice. I kept it to about 82 pixels and unpinned it on short screens, both my own call.
- **"Title"** against "The core idea in one sentence". Is the core idea the title, or is there a title and then the core idea? I made the core idea the `h1` with a small label above it.

## 5. The second job has no place in the order

> "If the request names two jobs, the page does the one its reader will act on and the other becomes a section."

It does not say where that section goes when the voice fixes the order. It also does not cover my actual case: the request named one job and the notes carried a second (the owners' decision by 26 May). I treated the notes' job the same way. I placed it between the mistakes and the next step. Nothing in the guide supports or forbids that.

The same hole swallows the limits. The notes include "What this does not show". The practical instructor voice has no slot for limits, and only the Analyst voice mentions them ("hidden limits"). I put them under the numbers because hiding them felt wrong, but the guide gave me no instruction to.

## 6. "At most two questions" with no way to ask

> "Ask at most two questions, only if you cannot tell the audience or the job."

I could not tell the audience. "Steps I can do today" comes from a person whose notes show they have already done the steps. I had to decide and record it. The guide says nothing about what to do when asking is impossible, which is the normal case for a one-shot chat reply. One line would fix it: "If you cannot ask, decide, and say so under Assumed."

## 7. Unused content, and content of uncertain permission

Nothing in the guide says whether every supplied fact must appear, or how to choose "Three numbers" when the notes hold six candidates. I chose three and moved or kept the rest.

The notes include "A customer story we may tell" about a named customer. The checklist says "Nothing private". The guide gives no rule for a named real person whose consent is unclear. I used the story and flagged it under Check before sharing. A guide this strict about invented customers should say something about real ones.

## 8. "Field guide" is five words

> "Field guide: two colours, tick boxes, a progress bar, tables."

- "two colours" against "Seven named colour tokens at most". I took "two colours" to mean two hues on a paper ground, built out to seven tokens. That is a guess.
- "a progress bar": progress of what? Scrolling, or steps ticked? I chose steps ticked.
- "One accent, used only for what to act on": is a filled progress bar something to act on? I decided not and filled it with the text colour.
- No type guidance at all for this look, although other voices get some ("serif", "monospace code", "one typeface").

## 9. Smaller things

- > "If a front-end design skill is available (for example `frontend-design`), load it as well."

  The test rules allow only the named files, so I did not load it. Outside a test this line also makes results depend on what happens to be installed.
- > "Every request gets all four. After a one-sentence request, one line under each is enough."

  The request table has rows for one sentence, for named recipe and parts, and for "Use the artifact-studio skill". Mine was none of these: a few sentences, a voice implied, a long set of notes. No row says how full the note should be. I wrote it in full.
- > "Tie movement to scrolling with a small script that sets one CSS custom property from the scroll position"

  This reads as an instruction to add scroll movement. I think it means "if you add movement, do it this way". My page has none tied to scrolling.
- > "Show the page as a rendered page if you can: an artifact, a canvas or a preview."

  against "Stop before anything is posted, sent, paid or published." If an artifact counts as publishing, these two collide. I wrote a file and published nothing.
- > "Totals add up and derived numbers show their working"

  Does a derived number the person already supplied ($150 a month, so $1,800 a year) need its working shown? I showed it.
- > "Every button does something"

  with "One next step" and the layout line "one button low on the right". On a guide with nothing to submit, the only honest button is a link back to step 1. The guide does not say whether a link styled as a button satisfies this, or whether a page may have no button.
- "Parts you can use" lists no checklist, no tick box and no progress bar, although the field guide look requires all of them.
