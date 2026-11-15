# Sentences

Every sentence in the studio, in one place. Copy one, attach your notes (and a photo if the page uses one), and paste both into a chat assistant.

**Status: untested.** These sentences describe what the demo pages do. They have not yet been run in fresh chats and scored. Record results in [`sentence-test.md`](sentence-test.md).

This file is generated from the examples by `base/source/build.py`. Edit the views, not this file.

## Recipes

### One-page report

A one-page report answers "how did it go and what happens next" before the reader has to scroll far. This one uses the analyst voice with a quiet look.

- **Short ask:** Turn this spreadsheet into a one-page report: a two-sentence summary, four key numbers, one chart and what happens next.
- **Full ask:** Build a one-page monthly report from my spreadsheet in the analyst voice. Title and period, a two-sentence summary, four key numbers each with its change from last month, one trend line with a full-sentence heading, one breakdown table with a small bar per row and the weakest row marked, then "what changed" and "what we will do next". One data colour, grey for comparisons.
- **With the skill:** Use the artifact-studio skill. Recipe: one-page report. Voice: analyst. Look: quiet, one data colour from my brand spec. Content: the attached spreadsheet and last month's report. Check that the breakdown rows add up to the totals and tell me if they do not.

### Proposal

A proposal turns a conversation into a decision. It repeats what the customer asked for, shows the answer, prices it three ways and makes yes easy. This one uses the practical voice with a calm look.

- **Short ask:** Turn my estimate and site notes into a one-page proposal with three price options and a schedule.
- **Full ask:** Build a proposal page from my estimate and site notes. Cover with the promise, the customer and a valid-until date. Then "what you asked for" in their words, "what we propose" with a simple floor plan drawing, three options as price cards with our suggestion marked, a six-week schedule chart, included and not included, payment terms, and one accept button. Dark green and brass, a serif for headings.
- **With the skill:** Use the artifact-studio skill. Recipe: proposal. Voice: practical instructor. Look: my brand spec (attached). Content: the attached estimate, site notes and photos. Every price must come from the estimate; flag any line you could not match.

### Scrolling explainer

A scrolling explainer teaches a process one stage at a time while a diagram keeps the reader's place. This one uses the teacher voice and no photographs at all.

- **Short ask:** Explain my five-step process as a scrolling page with a diagram that stays on screen and lights up each step.
- **Full ask:** Build a scrolling explainer of my process in the teacher voice. Title and one line on why it matters. Pin a diagram of the five stages at the top, with a small icon and label for each and a line that fills as I scroll. Under it, one block per stage: who does it, what happens in two or three sentences, and one fact set apart. End with a line that adds the stages up. Dark navy with one amber highlight.
- **With the skill:** Use the artifact-studio skill. Recipe: scrolling explainer. Voice: teacher. Look: dark with one highlight colour from my brand spec. Content: the attached procedure document. Keep my stage names exactly; if a stage has no fact worth setting apart, leave the fact out.

### Landing page

A landing page has one job: get one kind of visitor to take one action. Everything on it either builds the case or removes a doubt. This one uses a plain confident voice and a moving ledger in place of a photograph.

- **Short ask:** Make a landing page for my service with one clear promise, how it works in three steps, the price and one button.
- **Full ask:** Build a landing page for my service. Open with the promise in one line that includes a number, and one button. Under it, show a short animated ledger with rows being ticked off. Then "what you get" as three numbered items, "how it works" in three steps, one customer quote, the price as two cards, three questions that open on tap, and the promise and button again. Deep teal, pale mint, and one coral colour used only for the button.
- **With the skill:** Use the artifact-studio skill. Recipe: landing page. Voice: storyteller. Look: take two colours from my logo (attached) and choose one button colour that appears nowhere else. Content: the attached service description and two customer emails. Use only real customer words for quotes; if I gave you none, leave the quote section out.

## Voices

### The keynote

The keynote voice sells a vision by removing everything else. Inspired by Steve Jobs's product launches. The company and every figure here are invented for the demo.

- **Short ask:** Turn my notes into a keynote-style page: one idea per screen, huge type, almost no words.
- **Full ask:** Build a keynote-style page from my notes. Black background, one sans-serif typeface. Open with the problem as one huge number, reveal the answer in three words, show my photo once full screen, compare before and after as two numbers, and finish with "one more thing". Screens snap as I scroll.
- **With the skill:** Use the artifact-studio skill. Recipe: scrolling explainer. Voice: keynote. Look: black and white, with one colour taken from my attached photo. Content: the attached notes. Mark any number you could not find in my notes instead of inventing one.

### The storyteller

The storyteller voice makes the customer the hero and the company the guide. Inspired by Donald Miller's story framework. Priya, the company and the figures are invented for the demo.

- **Short ask:** Tell this as a story on one page, with my customer as the hero and us as the guide. Use my photo large.
- **Full ask:** Write a one-page story from my notes. Hero: my customer. Open on one moment with a time and a place. Give the problem at three depths, then introduce us as the guide with empathy before proof, a three-step plan, one button, the stakes side by side, and an ending that returns to the opening. Dark warm page, large serif type, my photo with a slow push-in. Take the colours from the photo.
- **With the skill:** Use the artifact-studio skill. Recipe: landing page. Voice: storyteller. Look: take the palette from my attached photo. Content: the attached customer interview notes. Invent nothing about the customer; where a story beat has no material, ask me one question.

### The teacher

The teacher voice makes a hard idea feel obvious by starting somewhere familiar. Inspired by David Malan's lectures. The company and the timings are invented for the demo.

- **Short ask:** Explain this like a great teacher: start with an everyday analogy, then one example, then the detail.
- **Full ask:** Build a one-page lesson from my notes. Open with the question. Give one everyday analogy in very large type, then one worked example with real times, then the same idea as numbered pseudocode I can step through line by line, then three check-yourself questions that open on click, and a one-sentence recap that reuses the analogy. Black and white with a single highlight colour.
- **With the skill:** Use the artifact-studio skill. Recipe: scrolling explainer. Voice: teacher. Look: black and white with one highlight colour. Content: the attached procedure. Keep every step of my procedure; if the analogy stops fitting at some step, say so rather than bending the step.

### The pitch

The pitch voice sells a feeling and lets the product arrive last. Inspired by Don Draper's carousel pitch in Mad Men. The father, the shop and the figures are invented for the demo.

- **Short ask:** Pitch this as a feeling, not a feature. First person, a handful of slides, and the product named only at the end.
- **Full ask:** Build a six-slide pitch from my notes that I advance by hand. Dark background with one lit slide at a time. Open with a personal memory in the first person, name the feeling, show what was lost, give one hard fact, say three things this is not, then name the product as the feeling. Make my photos look like faded film. End with a short close below the slides.
- **With the skill:** Use the artifact-studio skill. Recipe: landing page. Voice: pitch. Look: faded film, taken from my attached photos. Content: the attached notes. The memory must be mine: ask me for one true memory before you write, and do not invent one.

### The practical instructor

The practical instructor voice gets someone doing the thing within the hour. A best guess at Bradley Ross's teaching style: core concept, one analogy, steps for today. The company and figures are invented for the demo.

- **Short ask:** Turn this into a practical one-page guide: the core idea, one analogy, then steps I can do today.
- **Full ask:** Build a one-page field guide from my notes. Start with the core idea in one sentence, then one boxed analogy, three numbers on why it matters, five numbered steps with a time estimate and a tick box each plus a progress bar, a table of the same job at beginner, advanced and expert level, three common mistakes, and one next step. Navy and one bright accent, condensed headings, squared grid paper background.
- **With the skill:** Use the artifact-studio skill. Recipe: scrolling explainer. Voice: practical instructor. Look: field guide in my brand colours (attached spec). Content: the attached procedure. Give every step a time estimate; ask me for any you cannot judge.

### The analyst

The analyst voice gives the answer first and then earns it with evidence. Inspired by Barbara Minto's pyramid principle. The company and every figure are invented for the demo.

- **Short ask:** Write this up as an evidence-first one-pager: the answer at the top, then three findings with a chart each.
- **Full ask:** Build an evidence-first report from my data. The title states the conclusion. Then the answer in two sentences, three key numbers, and three findings where each heading is a full sentence with one chart and a "so what" line. Add how it was measured, what it does not show, and next steps with owner and date. One data colour, grey for comparisons, values labelled at the bar ends, source under every chart.
- **With the skill:** Use the artifact-studio skill. Recipe: one-page report. Voice: analyst. Look: quiet, one data colour from my brand spec. Content: the attached spreadsheet and notes. Show your calculation for every number in a collapsed table, and list anything you could not verify under "what this does not show".

### The executive brief

The executive brief voice exists to get a decision from busy people. It is the plainest voice here on purpose. It follows the convention of a board or cabinet decision memo. The company and figures are invented for the demo.

- **Short ask:** Write this as a one-page decision brief for busy executives. Decision first, then background, options, recommendation and risks.
- **Full ask:** Build a decision brief from my notes that looks like a paper memo. Header with to, from, date and decision deadline. State the decision first in a shaded box. Background in numbered paragraphs. One options table including "do nothing", with the recommended row shaded. Then the recommendation in two sentences, each risk with its control, and next steps. Serif type, one navy accent, no images, no animation.
- **With the skill:** Use the artifact-studio skill. Recipe: one-page report. Voice: executive brief. Look: paper memo, navy accent. Content: the attached notes and costs. Keep it to one printed page; if the content does not fit, tell me what you would cut rather than shrinking the type.

## Page components

### Big numbers

Three figures large enough to read from across a room. They count up once when they come into view.

> Show my three key numbers as large tiles that count up from zero when they scroll into view. One short label under each.

Effort: Easy. One sentence. Use it for: Results, impact pages, the top of a report.

### Timeline

What happened, or what will happen, in order. The line fills as you scroll past it.

> Lay out these five stages as a vertical timeline with a date and one line each. Fill the line with colour as I scroll down it.

Effort: Easy. One sentence and your dates. Use it for: Project plans, company history, onboarding.

### Process flow

A small diagram that draws itself. It shows how a thing moves from start to finish.

> Draw my four-step process as a simple diagram: numbered circles joined by a line, with a one-word label under each. Draw the line when it scrolls into view.

Effort: Easy. One sentence and your steps. Use it for: How it works sections, explainers, training.

### Comparison table

Options side by side on the same questions, with the recommended one picked out.

> Compare my three options in a table with four rows. Use ticks and dashes, put cost on the last row, and pick out the recommended column in a solid colour.

Effort: Easy. One sentence and your options. Use it for: Proposals, decision briefs, plan pages.

### Price table

Plans with one switch between monthly and yearly. The numbers change in place.

> Show my three plans as price cards with a switch between monthly and yearly prices. Highlight the middle plan. One line under each price.

Effort: Easy. One sentence and your prices. Use it for: Landing pages and proposals.

### Questions and answers

Each question opens on a tap. People read only the ones they came with.

> Add a questions and answers section where each question opens when I tap it. Use a plus sign that turns into a cross.

Effort: Easy. One sentence and your questions. Use it for: Landing pages, proposals, help pages.

### Customer quote

One person's words, set large. Use real words from a real customer, with their permission.

> Set this customer quote large in italics on a dark panel, with the customer's first name and town underneath.

Effort: Easy. One sentence and a real quote. Use it for: Landing pages, case studies, proposals.

### Tabs

Several short answers in the space of one. Good when readers want different things.

> Put these three short answers behind tabs, one tab per audience. Make the tabs work with the arrow keys.

Effort: Easy. One sentence. Use it for: Pages with more than one kind of reader.

### Bar chart

A handful of values compared. Thin bars, the number at the end of each, nothing else.

> Chart these four values as thin horizontal bars with the number at the end of each. Make the "before" bar grey and the rest one colour. Grow the bars when they scroll into view.

Effort: Easy. One sentence and your numbers. Use it for: Reports, proposals, results pages.

### Progress ring

One share of a whole. Use it for a single figure that matters more than the rest.

> Show 81% as a ring that fills when it scrolls into view, with the number and one line of explanation beside it.

Effort: Easy. One sentence. Use it for: One headline figure on a report or landing page.

### Callouts

A note, a warning and a confirmation. Each has an icon and a label as well as a colour, so it reads without the colour.

> Add three callout boxes: a note, a warning and a confirmation. Give each an icon and a bold label as well as its colour.

Effort: Easy. One sentence. Use it for: Guides, checklists, anything with a risk to flag.

### Old way, new way

The change in two lists. The old one is struck through, so the eye lands on the new one.

> Show the change as two lists side by side: the old way struck through on a pale panel, the new way on a dark panel. Three lines each.

Effort: Easy. One sentence. Use it for: Change announcements, proposals, case studies.

## Photo components

### Pan and zoom

A still photo that moves slowly reads as film. Use it to open a page or to hold a quote.

> Fill the frame with my photo and zoom in very slowly toward the island, like a documentary shot. Loop it back out.

Effort: Easy. One sentence. Seen in: Documentary title cards and photo essays.

### Parallax window

The photo moves slower than the page, so the frame feels like a window with depth behind it.

> Put my photo in a wide window and move it slower than the page as I scroll. Float a small caption card over it that moves the other way.

Effort: Easy. One sentence. Seen in: Product pages that tie movement to the scroll.

### Photo-filled type

One word, large enough that the letters become windows. Good for a chapter break.

> Write one huge word on a dark band and fill the letters with my photo. Slide the photo sideways inside the letters as I scroll.

Effort: Easy. One sentence. Seen in: Magazine covers and award-site title screens.

### Scrolling photo tour

The photo stays put while the text scrolls. Each paragraph moves the camera to the part it talks about.

> Pin my photo while I scroll. I will give you seven short paragraphs. For each one, zoom the photo to the part it describes.

Effort: Moderate. You say where to look; expect one round of nudging the zooms. Seen in: The Pudding, and the New York Times feature Snow Fall.

### Self-drawing line art

A sketch that draws itself as you scroll, then gives way to the real photo. The treeline, island and trunk were traced from the photo's own pixels.

> Trace the main shapes in my photo as a simple line drawing. Draw the lines as I scroll, far things first, then fade the real photo in underneath.

Effort: Harder. The assistant has to analyse the photo. Ask for a looser sketch if the first one is off. Seen in: Explainer intros and Codrops demos.

### Chart from the photo

A chart is a component too. These numbers are measured from the photo, so the chart and the picture tell the same story.

> Measure how bright my photo is from top to bottom and chart it as a line with a soft fill. Put a strip of the real colours under the axis. Label only the highest and lowest points, and let me touch the chart to read the rest.

Effort: Moderate. The chart is easy; ask the assistant to show how it measured. Seen in: The Pudding's data stories.

### Before and after

Two versions of one picture with a divider to drag. It makes a change obvious without a word of explanation.

> Show my photo as shot and with a warm sunset grade, as one picture with a divider I can drag from side to side.

Effort: Easy. One sentence. Seen in: Renovation portfolios and satellite image comparisons.

### Looks and voices

The same photo and the same message, five ways. A look sets the mood; a voice sets how it speaks. Describe both and a page stops sounding generic.

- **As shot:** Keep my photo as shot. Voice: a patient teacher. Open with an everyday analogy, then one worked example, then the detail.
- **Ink:** Make my photo high-contrast black and white. Voice: a keynote. One idea per screen, very short sentences, huge type.
- **Dusk:** Grade my photo like dusk, warm at the top and deep blue at the bottom. Voice: a storyteller. Start with a hook, give it a twist, end on a line that lingers.
- **Faded film:** Make my photo look like faded film, soft and slightly brown. Voice: an emotional pitch in the first person, about the feeling and never the feature.
- **Blueprint:** Turn my photo into a two-colour blueprint in navy and pale blue. Voice: a practical instructor. Core concept first, one analogy, then steps I can follow today.

### Frosted glass card

Facts float over the photo on a pane that blurs what is behind it. The photo stays the star and the text stays readable.

> Float the key facts in a frosted glass card over my photo. Keep the card over the sky so dark text stays readable.

Effort: Easy. One sentence. Seen in: Phone lock screens and weather apps.

### Bento grid

A summary as a tray of tiles in different sizes. Each tile holds one fact, so the eye can land anywhere.

> Summarise this as a bento grid: one tall photo tile, three big-number tiles, a colour palette tile and a small chart tile.

Effort: Easy. List the tiles you want. Seen in: Product launch summaries.

### Swipe gallery

Cards in a row that snap into place one at a time. On a phone it is the most natural way to browse a set.

> Crop six details from my photo and show them as cards I can swipe sideways, snapping one card at a time. Give each a two-word title and one line.

Effort: Easy. One sentence. Seen in: App store listings and social carousels.

### Flip postcard

A photo with a second side. Put the picture on the front and the message on the back.

> Make my photo a postcard with a white border. When I tap it, flip it over in 3D and show a short handwritten-style note, a stamp and address lines on the back.

Effort: Easy. One sentence. Seen in: Invitations, team pages and product cards.
