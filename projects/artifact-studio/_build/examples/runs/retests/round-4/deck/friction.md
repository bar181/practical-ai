# Friction with the guide

## BLOCKING

**1. A question addressed to the assistant has no home.** The request ends "tell me three ways I could tailor it for my own business". Three lines of the guide pull in different directions:

- "If the request names two jobs, the page does the one its reader will act on and the other becomes a section."
- "Offer a recommendation only when the person asked what to do, and label it on the page as proposed."
- "The page, then a note with four headings: Chose, Assumed, Missing, Check before sharing."

Read literally, the first two put the three tailoring ideas on the page as a slide marked "proposed". Read sensibly, they are advice to the owner about the deck and do not belong in front of the deck's audience. But the note is defined as exactly four headings, none of which fits an answer. I kept them off the deck and added a fifth section to the note. A second careful reader would add a seventh slide. The guide needs one sentence: something like "A question the person asks you is answered in the reply, after the note, never on the page."

**2. "the strongest number" is undefined.** "otherwise one short closing line that brings back the strongest number." The content has four candidates: $84,200, 46%, 23 and the two days. Strongest by size, by change, by closeness to the idea? I picked revenue. A reader who picked 46% or "two days" writes a different last slide. Give a tie-break (for example: the money figure if there is one, otherwise the largest change).

## MINOR

**3. Order of the "Three things" is not given.** "Three things: three slides, one proof on each, a number where there is one." Nothing says which proof goes first. I went quotes, jobs, revenue (cause towards money). The person's own order was revenue, jobs, quotes. Same slides, different sequence.

**4. The manner implies cause; the guide is silent on implied claims.** Villain, rule, then proof reads as "we did this, so that happened". The notes only say both things are true. "No invented facts" covers numbers and names but not an implied causal link created by ordering. I flagged it under Check before sharing. The guide should say whether that is enough.

**5. What counts toward "more than twelve words a screen"?** Does a figure such as "$84,200" count as a word? Do the slide counter and button labels count? I counted figures, used arrow glyphs with hidden labels, and did not count "5 / 6".

**6. Voice order against manner order.** The keynote voice lists "The catch or the consequence." The visionary deck has no such slide. "a deck follows its manner instead" settles the order, but step 5 also says "A beat in the voice's own order that the content cannot fill is left out too, and listed under Missing." It is unclear whether a voice beat the manner drops must be listed as Missing. I did not list it.

**7. "screens snap" against "Arrow keys, buttons and a tap move between slides."** Is a deck a scroll-snapping column that the keys scroll, or one slide shown at a time? I did one at a time with scripts on and a snapping column with scripts off. Both satisfy the text and behave differently.

**8. "a tap move between slides" does not say how a tap goes back.** I made a tap anywhere go forward only, with the left button for back.

**9. "Big numbers that count up" does not say from what.** Counting from zero shows figures that are not in the content, which rubs against "Every number, name, date and quote is in the supplied content." I counted from September's value to October's. The guide should name the start value.

**10. "At most three moving parts on a page."** Are three count-ups one part used three times, or three parts? Does changing slide count as a moving part? I treated it as three, which is the cap, and made slide changes instant.

**11. "Use `svh` with a pixel cap, not bare `vh`."** A slide is meant to fill the screen. A pixel cap on its height leaves a short slide on a tall display. I capped the type size and the scripts-off slide height (900px) and let the scripts-on slide fill the viewport. The rule reads as written for pages, not decks.

**12. "Design at 390 pixels wide first" for a thing made "to be presented".** The guide says a deck is "to be presented", so its real home is a wide screen. I followed the rule and checked both, but the priority is odd for a deck.

**13. How long is the note?** The request names a kind and a voice, so "Anything in between: Treat it as a one-sentence request" applies and "one line under each is enough". But step 5 says "List every gap and assumption" and the checklist says "Every gap is listed in the note". Five assumptions do not fit one line. I wrote one short paragraph under each heading.

**14. Does the contrast list apply to a default look?** "List the contrast ratio of each text and background pair in your note" sits inside the paragraph about building seven colours from one brand colour. Unclear whether it applies when the voice's default look is used. I gave the two ratios anyway.

**15. Whether to show the change.** The report recipe asks for "numbers with their change". The deck asks for "a number where there is one". The checklist says "derived numbers show their working", which cannot fit in twelve words. I showed each October figure with its September figure and derived nothing. Another reader might show "+$12,700".

**16. Facts that fit no slide.** "We are a landscaping company" fits no slide in the visionary deck, and the manner has no title slide. It is not a gap, so it is not Missing. The guide does not say where an unused fact is recorded. I used "two crews" in the closing line and left "landscaping" off.

**17. "Every button does something" at the ends of a deck.** The back button on slide one and the forward button on the last slide have nothing to do. I marked them `aria-disabled` with a dashed outline. The guide could allow a disabled state in so many words.

Blocking: 2. Minor: 15.
