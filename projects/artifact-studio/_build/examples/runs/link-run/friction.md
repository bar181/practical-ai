# Friction log

## The fetch

- **Did it work?** Yes. `curl -sS -L <url> -o runs/link-run/guide.md` returned HTTP 200, first try, no redirect trouble, no proxy trouble.
- **How much came back?** 197 lines, 14,864 bytes. It ends cleanly on the last bullet of "Rules that never bend", so it does not look cut off.
- **Was the file alone enough?** Enough to finish the job, yes. I opened nothing else. It was not enough to finish it without guessing: the request ("an HTML presentation in the keynote voice") lands exactly where the guide is thinnest, the join between voices, recipes and decks. Items 1 to 6 below are all that join. The file has no links to other files that I needed, with one exception: line 12 tells me to load a skill that lives outside it (item 14).

## Where the guide left me guessing, worst first

**1. A deck in a named voice: recipe, manner, or both? The guide never says.**
> "2. **Recipe.** Pick one from the table. If named, use it. If none fits, use the one-page report."

> "The same steps make three other things. - **A slide deck.** ... Four manners: a visionary deck (black, huge type, a villain, one rule, three things, one number, "one more thing"), a story deck ..."

"The same steps" means I still pick a recipe. But each manner then carries its own section list, which is a second recipe. Nothing says which wins, or whether a deck takes a recipe at all. I ended up with three structures stacked on one deck: the one-page report's sections, the keynote voice's order, and the visionary deck's list. I kept the first two and dropped the third. That was a guess.

**2. The four deck manners are not mapped to the seven voices.**
The person said "keynote voice". The deck section offers "visionary", "story", "briefing", "workshop". Visionary is obviously the keynote's cousin (black, huge type) but the guide does not say so, and their orders differ:
> Keynote: "The world as it is, as one line or one painful number. The catch or the consequence. The idea in a few words. Proof as enormous numbers. The next step. A short closing line."

> Visionary deck: "a villain, one rule, three things, one number, "one more thing""

"A villain", "one rule" and "one more thing" are never defined. "One number" contradicts "Proof as enormous numbers" (plural) and my content has three proof numbers. I followed the voice because the person named the voice.

**3. The named voice is not on the fitting recipe's voice list, and the guide does not say whether that matters.**
The content is a month against a month, which is the one-page report ("Someone needs to know how a period went"). Its Voices column says "Analyst, executive brief". Keynote appears only under Scrolling explainer. Is the Voices column a whitelist or a list of defaults? Step 3 only says "If named, use it. Otherwise take the recipe's first voice." I read the column as defaults. If it is a whitelist, I should have switched recipe to the scrolling explainer, which does not fit the content.

**4. The recipe's must-have sections cannot survive the keynote's "avoid" line.**
> "Where the recipe and the voice disagree, the voice sets the order, the counts and the headings. The recipe sets which sections the page must have."

> Keynote, Avoid: "Bullet lists, more than twelve words a screen"

> One-page report: "Title, period, reader. Two-sentence summary. Three or four numbers with their change. One trend chart with a full-sentence heading. One breakdown table, weak row marked. What changed. What happens next."

A breakdown table in twelve words is not possible. A chart with "a full-sentence heading", labelled values and "Unit and source underneath" barely fits: mine is exactly twelve and I had to drop the October value from the heading to get there. "Title, period, reader" has no slot in the keynote order, which must open on "one line or one painful number". The rule says the recipe decides which sections "must" exist and the voice decides counts, and the two cannot both be obeyed here. I dropped the table (no data for it anyway), put the title in the browser tab only, and made the closing line double as the two-sentence summary. The guide should say what gives.

**5. "More than twelve words a screen": what counts as a word?**
Not defined. Do numbers count ("$84,200", "46%")? Do the deck's own controls count (Back, Next, "1 of 7"), which the deck section requires on every screen? Do chart labels and the mandatory "Unit and source underneath" line count? I counted numbers and chart text, and did not count the controls. Slides 1 and 6 sit at exactly twelve on that reading. On a stricter reading every slide fails, because the controls add four words.

**6. A slot the order demands and the content cannot fill.**
> Keynote order: "... The next step. ..." and recipe: "What happens next."

> "A gap is never filled with a guess. If the page would mislead without it, a number, a name, a date or a price the reader will act on, mark it on the page as `[needs: ...]`. Otherwise leave the page clean and list the gap under Missing."

The person gave no next step. A missing next step does not mislead, so the rule says leave the page clean. That means silently deleting a step from an order the guide calls the voice. The guide does not say whether to drop the slide, or show a `[needs: the next step]` slide. I dropped it and listed it under Missing. I think many readers of the guide would do the opposite.

**7. "Screens snap" against "buttons and a tap move between slides" against "a readable column".**
> Keynote: "One idea per screen, screens snap."

> Deck: "Arrow keys, buttons and a tap move between slides. With scripts off the slides are a readable column."

Is a deck a vertical snapping column with controls bolted on, or a one-slide-at-a-time stage that degrades to a column? I built the first because it satisfies all three lines at once. Also "a tap" is undefined: tap where, and which direction? I chose left third goes back, the rest goes forward. And the Back and Next buttons cannot do anything with scripts off, which collides with "Every button does something", so I hide them until the script runs. The guide does not cover that case.

**8. "Use `svh` with a pixel cap" gives no cap and fights "one idea per screen".**
> "Use `svh` with a pixel cap, not bare `vh`."

How many pixels? Mine is 1200. On any screen taller than the cap a slide stops filling the screen and the next one shows underneath, which breaks "One idea per screen" and "A picture fills the screen". The rule is written for pages, not decks.

**9. The scroll-movement rule reads as compulsory.**
> "Tie movement to scrolling with a small script that sets one CSS custom property from the scroll position ... Add the CSS-only form inside `@supports ((animation-timeline: view()) and (animation-range: entry))` so it still moves with scripts off."

Is this "if you have scroll movement, build it this way" or "every page has scroll movement"? I could not tell, so I added a mild arrive-on-scroll effect mostly to comply. The rule also does not say how to stop the scripted form and the CSS form both running at once in a browser that supports both. I gated them on a `js` class. "One CSS custom property": one name set on each slide, or literally one property on one element? I set one name per slide.

**10. "At most three moving parts on a page": what is a moving part?**
Does scroll snap count? Does arrive-on-scroll count? Is "Big numbers that count up" one part or one per number? I counted two (arrive, count-up).

**11. Count-up numbers against "Every number ... is in the supplied content".**
> Parts: "Big numbers that count up."

> Checklist: "Every number, name, date and quote is in the supplied content"

A number counting up shows numbers that are not in the content for most of a second. The guide lists the part and the check without reconciling them. I counted from the old figure to the new one (38 to 46) so every value shown lies between two real ones. That is my patch, not the guide's.

**12. Black and white, an accent, and a data colour.**
> "Keynote: black and white."

> "One accent, used only for what to act on." / "One data colour, which is its own token and never the accent."

In a black and white look, what is the accent and what is the data colour? If both are white they are the same colour in two tokens, which obeys the letter and defeats the point. I made the accent white and the data colour a light grey. Also "Greys carry a trace of the brand colour": there is no brand colour, so my greys are neutral.

**13. "One trend chart" with two data points.**
Two months is not a trend. The recipe demands the chart anyway. The guide does not say what to do when the content has fewer points than a trend needs. I drew two bars and said so in the note. Related: "derived numbers show their working". A bar's length is a derived number (71,500 / 84,200 = 84.92% width). Does that need working on the page? I assumed not.

**14. Line 12 points outside the file.**
> "If a front-end design skill is available (for example `frontend-design`), load it as well."

A person who pastes a link to this file into a chat assistant cannot know whether one is "available", and the test rules here say read nothing else. I did not load one. If the page quality depends on that skill, the single-file edition is not single-file.

**15. Which size of delivery note?**
> "| One sentence (beginner) | ... | Names recipe, voice, look, parts (advanced) | ... | "Use the artifact-studio skill" (expert) |"

This request is five sentences, names a voice and a format, and names no recipe, look or parts. It fits none of the three rows. I wrote a full note.

**16. Intake wants things the guide then gives no way to settle.**
> "Find the content, any media, the audience, the one job of the page, and where it will be seen. ... Ask at most two questions, only if you cannot tell the audience or the job."

I could not tell the audience. In this test I could not ask, so I assumed the company's own team. That is the test's constraint, not the guide's fault, but note that the keynote order would be different for customers (the six days would be an odd thing to open on).

**17. "The world as it is" when the content is the world as it was.**
The painful number here is in the past ("It used to take six"). I wrote slide 1 in the past tense. The guide's order assumes the pain is current. Minor.

**18. The request's second half has no home in the guide.**
"Tell me three ways I could tailor it for my own business." The guide has no section on tailoring. I assembled an answer from Look ("From a photo", one brand colour), the recipe table, and the preferences file. The preferences file is mentioned in step 1 ("a file named `preferences.md`, or a section headed Preferences") but the guide never shows what goes in one or how a person without a file system would supply it. For someone arriving from a bare link, that is the most useful tailoring hook and it is the least explained.

**19. Noise for a reader who arrives by link.**
> "<!-- Generated from level-2-files/artifact-studio/SKILL-single-file.md by _build/build.py. Edit that file, not this one. -->"

Harmless, but it is an instruction ("Edit that file") aimed at a maintainer and it is the first thing an assistant reads. "(single-file edition)" also implies a fuller edition exists somewhere, which invites going to look for it.

**20. "Show the page as a rendered page if you can".**
> "Show the page as a rendered page if you can: an artifact, a canvas or a preview."

Here the output had to be a file, so I warned in the note that a bare file can open as code on a phone. Not a contradiction in the guide, just a place where the guide and the delivery channel pulled apart.

## Things that were clear and worked

The keynote row itself (order, look, avoid) was unambiguous once I decided it won. The build rules were specific enough to check by machine: 390 pixels, 44 pixel targets, no network, complete at rest. The four note headings were easy to follow. The "no invented facts" rules were clear and did real work: they stopped me writing a next step and a causal claim.
