# Friction log

Request: a short deck to get partners to agree to Saturday opening. Blunt summary: the skill is written for pages. A deck falls through steps 2, 3, 4 and 7, and the briefing deck starter breaks several of the build rules it is supposed to follow. I got to a result by picking which line to obey each time. Each choice is recorded below.

## A. Where SKILL.md and its reference files disagree (both lines quoted)

### A1. What file a deck starts from

- SKILL.md, step 7: "Start from `assets/page-skeleton.html`. Follow `references/build-rules.md`."
- SKILL.md, file table: "`assets/page-skeleton.html` | As the starting file for every page"
- build-rules.md: "Start from `assets/page-skeleton.html`. Keep its token block, its motion guard and its scroll helper."
- SKILL.md, Choosing for the person: "For a deck or a social picture, start from its starter in `assets/starters/` in this skill: a complete small file you copy and fill."

SKILL.md contradicts itself, and build-rules.md sides with the line that is wrong for a deck. The starter has no skeleton token block, a different motion guard and no scroll helper. I started from the starter, carried over the skeleton's token names, `color-scheme` and reduced-motion guard, and left out the scroll helper because nothing on the deck scrolls.

### A2. Where the look comes from: four sources or three

- SKILL.md, step 4: "the person's design spec or brand colours; colours taken from an image they supplied (the method is in `references/looks.md`); a palette built from their one brand colour (the method is in `references/design-ideas.md`); the default look for the chosen voice."
- looks.md: "Use the first of these that applies. 1. **The person's design spec or brand colours.** ... 2. **An image they supplied.** ... 3. **The default for the chosen voice.**"

looks.md has no brand-colour step. Did not bite here (no colour supplied), but the two lists differ.

### A3. The executive brief voice forbids what the briefing deck starter is

- voices.md, Executive brief: "Page behaviour | None. It is a document." and "Avoid | Images, animation, more than one page"
- SKILL.md: "The library also holds decks ... They follow the same rules as pages"
- assets/starters/deck-briefing.html: six slides, a picture pane (`<i class="dk-pic" role="img" aria-label="A cheetah in a suit and tie: the person who has to decide.">`), and a fade (`transition:opacity .35s ease`).

A briefing deck is more than one page by definition. I kept six slides, removed the picture pane and the fade, and reported "partly" on the checklist line "Follows the look card and the voice card, including each 'avoid' line". That line cannot pass for any deck in this voice.

### A4. The default look for the voice does not match the starter for the voice

- SKILL.md, step 4: "the default look for the chosen voice."
- looks.md: "Executive brief | Paper memo", and Paper memo: "A serif for text, a plain sans for headings and labels" and "Avoid | Images, icons, coloured panels, anything that moves"
- deck-briefing.html: sans for everything (`font:400 3.33cqw/1.35 var(--sans)`), a tinted recommended row (`.db tr.pick td{background:#e6eef7`), a picture pane, a fade.

"Copy and fill" the starter and you break step 4. Follow step 4 and you rewrite the starter's styles. I rewrote: serif text, no tint, no picture, no motion. That was about half the stylesheet, which is not "copy and fill".

### A5. Seven named colours, against a starter with about sixteen hard-coded ones

- build-rules.md: "Name at most seven colours as tokens at the top of the style block and use only those: background, panel, border, secondary text, main text, accent and highlight."
- deck-briefing.html: four tokens with other names (`--pine`, `--pine-2`, `--reed`, `--fog`) plus `#f7f8fa`, `#16202b`, `#1f4e79`, `#3d4a59`, `#8a5a00`, `#fff`, `#d5dbe3`, `#5b6878`, `#e6eef7`, `#c2cede`, `#5b6b7a`, `#000` written straight into rules.
- page-skeleton.html has five colour tokens (`--bg`, `--ink`, `--muted`, `--panel`, `--accent`): no border, no highlight.

Three files, three colour systems. I rebuilt the deck on six tokens with the skeleton's names plus `--border`.

### A6. What the accent is for

- build-rules.md: "The accent is for what to act on."
- design-ideas.md: "One accent. It marks what to act on. If it is also used for decoration, it stops meaning anything."
- looks.md, Paper memo: "one dark accent for rules and headings"

The look the skill told me to use spends the accent on rules and headings. I followed the look card. The one action on the last slide is the only filled block of accent.

### A7. Bare vh

- build-rules.md: "Use `svh` units with a pixel cap, never bare `vh`."
- deck-briefing.html: `.dk-stage:fullscreen .dk-s{inset:auto;width:min(100vw,177.78vh);height:min(56.25vw,100vh)}`

I left it, because it only applies in full screen where `vh` is safe. The rule says "never".

### A8. Dark mode

- pre-ship-checklist.md: "Text is easy to read against its background in light and dark mode"
- page-skeleton.html: `color-scheme:light;`

Nothing in SKILL.md, looks.md or build-rules.md says how to do dark mode. The skeleton switches it off. The checklist line cannot be passed as written. I reported "light only".

### A9. The recipe's own Look field is never used

- recipes.md, Proposal: "Look | Calm, two colours, a serif for the large words"
- SKILL.md, step 4 never mentions the recipe's Look field. The look comes from the voice: looks.md "Practical instructor | Field guide", whose type is "A condensed bold face for headings".

Did not bite here, but for a default Proposal the recipe card and the look card describe two different pages and nothing says which wins. Step 3 only settles recipe against voice for "the order, the counts and the headings".

### A10. Moving big numbers in a voice with no motion

- components.md: "Big numbers | Three figures large enough to read from across a room. They count up once when they come into view."
- voices.md, Executive brief: "Page behaviour | None." The briefing starter has a big-numbers slide (`<div class="two">`).

I dropped the numbers slide. The voice card asks for "Background in numbered paragraphs" and the three facts are already there.

## B. Places the guide left me guessing

1. **There is no recipe for a deck.** Step 2: "Pick one page type from `references/recipes.md`. If the person named one, use it. If none fits, use the one-page report and say so." The person named a deck. recipes.md has four page types and no deck. Read literally, step 2 tells me to build a one-page report for someone who asked for slides. I ignored that and called the recipe "briefing deck".

2. **Step 3 has nothing to point at.** "If not, take the first voice listed for the recipe." A deck has no recipe card, so no first voice. If I had used the nearest page recipe (Proposal: "Get a customer to choose an option and say yes"), the first voice is Practical instructor, which means numbered steps with times and tick boxes for a partners' meeting. I chose Executive brief from the voices.md table ("Make a decision in three minutes"). That is my judgement, not the rule.

3. **Nothing says which starter goes with which voice.** The starters are named briefing, story, visionary and workshop. The voices are named executive brief, storyteller, keynote, teacher, practical instructor, analyst and personal story. I guessed briefing = executive brief from the starter's sample text. There is no starter for analyst or personal story, and "workshop" could be teacher or practical instructor.

4. **The scoring method cannot be run from the skill.** "The library's index is `level-3-files/mcp/library/index.json`, beside this skill's folder in the project. ... Score each as three times the goal fit plus twice the reader fit and take the highest". That file is not in the skill folder. A skill that is installed on its own cannot do the step it describes. Same for "read the person's saved finds ... in `level-3-files/mcp/inspiration/`" and for "`base/studio.html`" in recipes.md and voices.md. I chose by judgement and still gave the runner-up the section asks for.

5. **Which of the three kinds of request is this?** "'Use the artifact-studio skill' with attachments | Run every step ... give the delivery note in full". The person said the trigger phrase but pasted notes and attached nothing. It is also "One sentence" (a short ask), which gets "one line under each of its four headings". I gave the full note. The table should say whether the phrase or the attachments is the trigger.

6. **"If a front-end design skill is available (for example `frontend-design`), load it as well."** One was listed in my session. The test rules forbade reading anything outside the skill folder, so I did not load it. Outside the test this line would have had me take visual advice from a second skill with no rule for which one wins.

7. **Voice sets order, but the starter already has an order.** Step 3: "the voice sets the order, the counts and the headings." Executive brief order: header, decision, background, options, recommendation, risks, next steps. Starter order: recommendation, why, numbers, options, what we do not know, decision. Two orders for the same voice. I used the voice card's order and headings, and reused the starter's slide shapes.

8. **Executive brief header: "Header: to, from, date, decision needed by."** The notes give no name and no date. The gap rule says mark a gap only "If the page would mislead without it". A missing "From" does not mislead, so I left it off and listed it. But then the header the voice requires is half a header. No guidance on a required field with no content.

9. **"Options in one table, including 'do nothing'."** The person gave two options and no "do nothing". The voice makes me add a row, and "No invented facts" makes me fill it with nothing. I wrote "None" and "None", true by definition, and flagged it. The guide should say that a "do nothing" row may only restate the present.

10. **"Risks, each with its control."** The notes give two unknowns and no controls. The only control in the content is the trial. I wrote one control for both and flagged it as an assumption. The pull to invent a measurement plan here is strong and the voice card pushes toward it.

11. **"Next steps."** The content has none beyond the decision. Step 5 says "either drop the section or mark the gap". I kept it as the closing ask because the checklist wants "One clear primary action". That makes slides 1, 4 and 6 say nearly the same thing. In a six-slide deck, the voice's "decision, recommendation, next steps" is one idea three times.

12. **When does a missing number get `[needs: ...]`?** "If the page would mislead without it, a number, a name, a date or a price the reader will act on". The number of appointments from the evening option: I marked it, because a comparison table with an empty cell misleads. The trial start date and the cost: I did not mark them. Both readings were defensible each time. "Would mislead" is doing all the work and is not defined.

13. **Derived numbers.** SKILL.md: "Show how any derived number was calculated, in a collapsed table under the chart." I had one derived number (12 = 8 + 4) and no chart. I put the working in the table cell. The rule only describes the chart case.

14. **"One clear primary action" and "Every button and link does something" on a deck.** The starter's action is `<span class="cta">Decide by Friday</span>`: it looks like a button and does nothing. On a deck the action happens in the room. The checklist does not say whether a button-shaped label passes. I kept it and said so.

15. **"Reads well at phone width" against a fixed 16:9 slide.** build-rules.md: "Design at 390 pixels wide first, then widen." The starter is a 16:9 stage with type in `cqw`. At 390 pixels its table text renders at about 11 pixels. I added an upright-phone rule (3:4 slide, larger type, fixed table columns). The starter fails the first line of the checklist as shipped.

16. **"One h1."** build-rules.md: "Headings in order. One `h1`." The starter has no `h1` at all, and three of its six slides have no heading element, only `<p class="k">`. I added an `h1` and made the labels `h2` where a slide had no headline.

17. **"Give each part's set-up its own `try`"** (build-rules.md). The starter's script has none. I added one, and a fallback that returns the deck to a readable column if set-up fails.

18. **Preferences.** Step 1: "If there is a preferences file (a file named `preferences.md`, or a section headed Preferences in your instructions), read it". Where should I look for the file? The skill folder, the working folder, the conversation? Not said. I found none and said so.

19. **"Show the page as a rendered page if you can: an artifact, a canvas or a preview."** I was told to write a file. No guidance on what to tell the person when only a file can be given, beyond the warning that it "opens as code on many phones".

20. **`SKILL-single-file.md` sits beside SKILL.md and SKILL.md never mentions it.** I did not read it. If it differs from SKILL.md, a reader cannot know which is current.

21. **The file table lists the answer key as a reference.** "`evals/evals.json` | To test this skill: six requests, each with what a good result must contain". It sits in the same table as the files to read "as you need them". I did not open it.

## C. Faults in the briefing deck starter itself

1. **Space on a focused button moves the slide.** `dk.addEventListener('keydown',key)` catches Space from the Notes and Full screen buttons, calls `preventDefault()` and advances. A keyboard user cannot press Notes with Space. I added a guard.
2. The header comment says "no photograph", and slide 1 carries a picture pane labelled "A cheetah in a suit and tie".
3. The print rule hides classes that are not in the file: `:is(.mast,.about,.dk-top,.dk-bar,.dk-notes,.anat,.tabs,.pager,.progress)`. Also unused: `.dk-top`, `.dk-hold`, `.ph`. Leftovers from the full template. "Every part must carry content."
4. The slide count is hard-coded in `aria-label="The briefing deck, six slides"`. Add or remove a slide and it is wrong.
5. The unknowns list uses a second accent, amber `#8a5a00`, for the question marks. build-rules.md allows one accent.
6. `border-top:1.2cqw` is set on the element that is itself the container, so `cqw` there resolves against the viewport and not the slide.
7. The starter's sample text is about a kitchen company. It has to be replaced completely. I checked that none of it is left.

## D. What was clear and worked

- The "No invented facts" rule and the `[needs: ...]` form. Same wording in SKILL.md and build-rules.md.
- The delivery note's four headings.
- The voice card's order line for Executive brief: specific enough to lay out slides from.
- "Complete at rest": the starter does this well. With scripts off, all six slides show as a column.
