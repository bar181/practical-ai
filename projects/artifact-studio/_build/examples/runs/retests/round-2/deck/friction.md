# Friction with the guide

Request: a keynote-voice HTML presentation from six facts about a landscaping company. Fourteen problems, three of which forced a guess that changed the page.

1. **BLOCKING. The deck manner and the voice order are two different lists and nothing says which wins.**
   The table says "A slide deck | ... Visionary deck with the keynote voice". The deck section defines the visionary deck as "black, huge type, a villain, one rule, three things, one number, "one more thing"". The keynote voice defines its order as "The world as it is, as one line or one painful number. The catch or the consequence. The idea in a few words. Proof as enormous numbers. The next step. A short closing line." These do not line up one to one: there is no "next step" in the manner and no "one more thing" or "one number" in the voice. The only tie-break in the guide is step 5: "Where the two disagree on a count or a heading, the voice wins", but "the two" there are the voice and the recipe, and a deck has no recipe. I guessed a mapping: villain = the six-day wait, one number = the opening "6 days", one rule = the idea, three things = the three proof slides, "one more thing" = the closing line. A different guess gives a different slide count and order.

2. **BLOCKING. A voice beat the content cannot fill has three allowed answers and no rule to pick one.**
   The keynote order requires "The next step". The notes hold none. Step 5 says "leave out any it cannot fill", but that sentence is about "the recipe's list", not the voice's order. The Voices section says "You may offer a recommendation if the page labels it as proposed." The rules that never bend say "A gap is never filled with a guess ... Otherwise leave the page clean and list the gap under Missing." So I could drop the slide, add a labelled proposal, or leave the gap. I added a slide labelled "Proposed next step". "May" is not a rule; the guide should say which is the default.

3. **BLOCKING. It is unclear whether a number may appear on two slides, and "the catch" had nothing of its own to hold.**
   The notes state no catch or consequence, so the only honest material for "The catch or the consequence" was the old conversion rate, 38%. That number also belongs on the proof slide ("46%, up from 38%"). Step 5 says "never show one number twice to satisfy both lists". Read narrowly that is only about recipe versus voice, which does not exist in a deck; read broadly it bans the repeat. I read it broadly, so the 46% slide carries no "up from" line, unlike the other two proof slides. The guide should say plainly whether a deck may repeat a number for comparison.

4. **MINOR. "more than twelve words a screen" does not say what counts as a word.**
   Do small labels count? Numerals such as "$84,200"? The slide counter? Button text? I counted every visible word and numeral in the slide and kept the controls wordless (arrow icons, "1 / 8"), which sidestepped it, but the limit decided how much labelling each slide could carry.

5. **MINOR. "Use `svh` with a pixel cap, not bare `vh`" gives no cap value and fights the deck.**
   The keynote behaviour is "One idea per screen, screens snap." A capped slide height means that on a screen taller than the cap the next slide shows underneath. I picked 1600 pixels so it almost never bites. The guide should give a number, or exempt decks.

6. **MINOR. Deck controls with scripts off, and what "a tap" means.**
   "Arrow keys, buttons and a tap move between slides. With scripts off the slides are a readable column." With scripts off those buttons do nothing, which breaks the checklist line "Every button does something". The guide does not say to hide them; I hid them until the script runs. "A tap" also does not say where or which direction; I made any tap on a slide go forward, with the back button for going back.

7. **MINOR. "Big numbers that count up" contradicts "complete at rest", and movement in a deck is undefined.**
   The parts list offers "Big numbers that count up". The build rules say "Everything is readable before any animation runs". A number that counts up is wrong until it finishes. I did not use it. Separately, "At most three moving parts on a page" does not say whether "screens snap" is a moving part, or whether a deck needs any movement at all. I added one scroll-tied settle-in, following "Tie movement to scrolling with a small script that sets one CSS custom property" and the `@supports` form, mainly because the rule exists.

8. **MINOR. The short note and the checklist disagree on length.**
   "Anything in between | Treat it as a one-sentence request" leads to "one line under each is enough". The checklist says "Every gap is listed in the note" and step 5 says "List every gap and assumption." With five assumptions and four gaps, one line under each heading becomes one very long sentence. I wrote the long sentences.

9. **MINOR. "Show the page as a rendered page if you can" has no fallback wording.**
   "A bare HTML file opens as code on many phones." True, and the guide stops there. It does not say what to tell the person when a file is all you can hand over. I added one line telling them to open it in a browser.

10. **MINOR. The preferences rule does not cover "there is none".**
    "Say in the delivery note which preferences you applied." With no `preferences.md` and no section "headed Preferences in your instructions", is silence correct or should the note say so? "Your instructions" is also vague about whose instructions. I wrote that none was supplied.

11. **MINOR. The keynote order manufactures a cause the notes do not state, and the guide has no rule for that.**
    World, catch, idea, proof reads as "we changed X, so Y happened". The notes only list facts side by side. "No invented facts" covers numbers and names, not a causal claim made by slide order. Likewise the notes give no period for 38% and 46%, and the voice pushes you to label them. I used "Before" and "Now" and put the causation warning under Check before sharing. The guide should name implied causation as something to flag.

12. **MINOR. No word on a title slide when there is no company name.**
    The keynote order opens on "The world as it is", the visionary manner lists no title, and the notes hold no company name. I skipped a title slide and listed the name under Missing. The `<title>` text is my wording.

13. **MINOR. Two-value comparisons: bars or enormous numbers?**
    The chart rule says "Two values are a comparison, not a trend: draw two bars." The keynote voice says "Proof as enormous numbers." All three proofs are two-value comparisons. I followed the voice and drew no chart, so "Source: your notes" appears nowhere on the page. The guide should say the chart rule only applies once you have decided to draw a chart.

14. **MINOR. An extra ask has no home in the note.**
    The person asked for "three ways I could tailor it". Step 9 fixes the note at "four headings: Chose, Assumed, Missing, Check before sharing." Nothing says where additional requested text goes. I put it after the four headings.

Blocking: 3. Minor: 11.
