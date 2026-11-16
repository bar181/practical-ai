# Friction log: deck run

Request: "show this as an HTML presentation in the keynote voice, and tell me three ways I could tailor it for my own business." Content: six facts about a landscaping company.

The deck section is the weakest part of the guide. One sentence carries the whole definition of four deck types, and I had to guess at almost every slide.

## BLOCKING

### B1. Two rules give the order, and they give different orders

> "5. **Outline.** The voice gives the order."

> "A manner is the slide order for a deck: build in the manner's order, and take the tone, the look and what to avoid from its voice."

> Keynote order: "The world as it is, as one line or one painful number. The catch or the consequence. The idea in a few words. Proof as enormous numbers. The next step. A short closing line."

> Visionary deck: "(black, huge type, a villain, one rule, three things, one number, "one more thing")"

The keynote voice has six beats. The visionary manner has five slide names, and they do not map one to one. The guide never says what happens to voice beats the manner does not list ("the catch or the consequence", "the next step", "a short closing line"). I followed the manner, dropped the catch and the closing line, and listed the next step under Missing. A second reader could fairly add a closing slide and a consequence slide. Different slide count, different deck.

Also: the manner list mixes look ("black, huge type") and slides ("a villain, one rule...") inside one parenthesis with no marker for where the look ends and the order starts.

### B2. "three things, one number" cannot be built without guessing

> "three things, one number"

> "One idea on each slide."

> "A number appears on one slide; the closing slide may bring one back."

> "never show one number twice to satisfy both lists"

Three unknowns:

- Is "three things" one slide holding three items, or three slides? "One idea on each slide" and "more than twelve words a screen" push toward three slides. The phrase itself reads like one slide.
- The content had exactly three results (46%, 23 jobs, $84,200). Either they are the three things and "one number" has nothing left, or revenue is the one number and "three things" has only two. Nothing in the guide picks.
- The obvious fix, a derived number such as the revenue difference, breaks "A number appears on one slide" because "derived numbers show their working" forces the inputs back onto the screen.

I made three slides, called them the three things, and skipped "one number". Another reader would put three figures on one slide, or add a derived-difference slide. Visibly different pages.

### B3. "a villain", "one rule" and "one more thing" are never defined

> "a visionary deck (black, huge type, a villain, one rule, three things, one number, "one more thing")"

That is all the guide says. What is a villain when the content is a month of results? What goes in "one more thing": a surprise fact, the next step, the closing line, the ask? Is "one more thing" the "closing slide" that "may bring one back"?

I used the old six-day wait as the villain, the two-day rule as the rule, and the only unused fact (two crews) as "one more thing". That last choice is a stretch: on a closing slide "Two crews" implies the crew count did not change, which the notes do not say. A second reader would skip the slide ("Skip a slide the content cannot fill") or use it to bring back a number. The other three manners have the same problem ("a picture", "a card to keep", "stakes").

## MINOR

### M1. No home for a second request that is not a page

> "Deliver. The page, then a note with four headings: Chose, Assumed, Missing, Check before sharing. Every request gets all four."

The person also asked for "three ways I could tailor it". The guide's two-jobs rule ("If the request names two jobs, the page does the one its reader will act on and the other becomes a section") is about the page. It would be wrong to put advice to the author on a slide. I added the answer after the four headings. The guide should say where a question to the assistant goes.

### M2. Short note against "list every gap"

> "Anything in between | Treat it as a one-sentence request and follow whatever it names"

> "Give the short note: one line under each of the four headings"

> "Write the words. List every gap and assumption."

> "Every gap is listed in the note"

With no questions allowed I had four assumptions and four gaps. One line each means four run-on lines. The short note and the full list pull against each other. I wrote one long line per heading.

### M3. The twelve-word limit does not say what counts

> "Avoid | Bullet lists, more than twelve words a screen"

Do "Back" and "Next" count? Does a numeral count as a word? Does a small label count? I counted everything visible, including the two button words, and stayed at twelve or under (busiest slide: ten words plus two buttons). A reader who did not count buttons would have more room, so wording would differ slightly.

### M4. How the deck moves is left open

> "Arrow keys, buttons and a tap move between slides. With scripts off the slides are a readable column."

> "One idea per screen, screens snap."

> "Nothing scrolls sideways except a table inside its own container."

Is the deck a snapping column or one slide shown at a time? Does a tap always go forward, or left half back and right half forward? I built a vertical snapping column where a tap goes forward and Back is a button. It works, but I chose it, the guide did not.

### M5. "svh with a pixel cap" fights "one idea per screen"

> "Use `svh` with a pixel cap, not bare `vh`."

No cap value is given. Any cap makes a slide shorter than a tall enough screen, so the next slide shows and "one idea per screen" breaks. I used `min(100svh, 1400px)` and accepted the edge case.

### M6. "Moving parts" has no unit

> "At most three moving parts on a page."

> "Big numbers that count up."

> "Tie movement to scrolling with a small script that sets one CSS custom property from the scroll position"

Is a count-up used on five slides one moving part or five? And a count-up is not tied to scroll position, so the movement rule seems to rule out the first part on the parts list. I used no motion at all. A keynote deck with no motion feels flat, but the guide gave me no safe way to add any.

### M7. Charts and the keynote voice

> "Two values are a comparison, not a trend: draw two bars."

> "Unit and source underneath."

Every figure here is a two-value comparison. The chart rules (sentence heading, unit, source line) cannot fit in twelve words, so I drew no bars and wrote the earlier value in words. The guide does not say whether a comparison stated in words still needs "Source: your notes". I left it off.

### M8. "Black and white" against the token list

> "Keynote: black and white."

> "Say under Assumed that the colours are yours."

I used two greys for secondary text and button borders. Is that still black and white? Probably. Saying "the colours are yours" about a look the guide dictated is odd, but I said it.

### M9. Preferences on a host that has its own

> "or a section headed Preferences in your instructions"

A chat assistant may carry general writing-style preferences for its user that have nothing to do with pages. The guide does not say whether those count, or whether the note must report them. I treated only a page-preferences file as in scope and said none was supplied.

### M10. Noise for an outside reader

> "<!-- Generated from level-2-files/artifact-studio/SKILL-single-file.md by _build/build.py. Edit that file, not this one. -->"

> "Show the page as a rendered page if you can: an artifact, a canvas or a preview."

The first line means nothing to someone who was handed a link. The second is not a rule I can follow or break when the output is a file. Neither changed the page.

Blocking: 3. Minor: 10.
