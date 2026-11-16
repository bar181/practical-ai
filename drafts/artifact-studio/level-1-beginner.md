# Level 1, Beginner: use it in any chatbot

Nothing to install. You give your chatbot one set of instructions, then ask for what you want.
This level is the whole product. Levels 2 and 3 only remove steps.

**Think of it as** handing the cook a recipe card. You do it once, then you only say what you
want for dinner.

## What you need

- A chatbot that can make a web page. Claude and ChatGPT both can.
- Notes for one real thing: last month's numbers, a quote you need to send, a process you keep
  explaining, or a service you sell.
- Ten minutes.

## Set up once

**The quick way.** In a chatbot that can open links, start your request with:

```
Use the design guide at https://raw.githubusercontent.com/bar181/practical-ai/scaffold/structure/drafts/artifact-studio/base/instructions/AI-INSTRUCTIONS.md
```

**The reliable way.** Open [`base/instructions/AI-INSTRUCTIONS.md`](base/instructions/AI-INSTRUCTIONS.md),
copy all of it, and paste it where your chatbot keeps standing instructions. In Claude or ChatGPT
that is the instructions of a Project. If you have neither, paste it as the first message of a new
chat.

That is the whole installation.

## Make a page

1. Decide which template your notes fit. The four pages are below. Decks and social posts are in the [index](base/templates/README.md), and the Pick tab of the studio page will suggest one.

   | Your notes are about | Recipe | Example to open |
   | --- | --- | --- |
   | How a week, month or project went | One-page report | [`pages/report.html`](base/templates/pages/report.html) |
   | Something a customer has to say yes to | Proposal | [`pages/proposal.html`](base/templates/pages/proposal.html) |
   | How something works | Scrolling explainer | [`pages/explainer.html`](base/templates/pages/explainer.html) |
   | Something you want people to sign up for or buy | Landing page | [`pages/landing.html`](base/templates/pages/landing.html) |

2. Copy the sentence for it. Every example ends with its sentence, and all of them are in
   [`base/sentences.md`](base/sentences.md). Start with the short ask.
3. Paste the sentence into your assistant. Attach or paste your notes underneath. Add a photo if
   the page should use one.
4. Open the result on your phone. Most people who receive it will read it there.
5. Check every number and name against your notes. Fix anything wrong by telling the assistant
   exactly what to change.

**You are done when** the page says what your notes say and nothing else.

## Make a deck or a social post

The same instructions make these too. Two things make it go better.

1. Pick the one you want in the Decks or Social tab of [`base/studio.html`](base/studio.html),
   or let the Pick tab choose, and copy its sentence.
2. Attach its starter from [`base/templates/starters/`](base/templates/starters/) with your
   notes. A starter is a small complete file of that deck or picture. Say "fill this in from my
   notes". The assistant then changes words in a file that already works, which is more reliable
   than building one from a description.

| You need | Starter to attach |
| --- | --- |
| To move a room | `deck-visionary.html` |
| To win a customer | `deck-story.html` |
| A decision from the people who decide | `deck-briefing.html` |
| To teach a skill, with an exercise | `deck-workshop.html` |
| A post | One of the `social-*.svg` files: square, portrait, story, carousel, link |

Present a deck from a browser: arrow keys or a tap move between slides, N shows your notes, and
printing gives one slide a page.

## Using it properly

| Do | Why |
| --- | --- |
| Use real notes | The assistant is told never to add facts. Thin notes give a thin page, with the gaps marked |
| Ask for one page with one job | A page that reports and sells and explains does none of them well |
| Ask for changes by naming parts | "Make the three numbers a bar chart" works. "Make it pop" does not |
| Name a voice when the first try sounds generic | The seven voices are in [`base/templates/voices/`](base/templates/voices/). Say "use the storyteller voice" |
| Read the list of gaps and guesses it returns | That list is where the mistakes are |
| Decide yourself what is published and where | The assistant builds a file. It does not send or post anything |

| Do not | Why |
| --- | --- |
| Paste anything you could not send to the reader | The page is made to be shared |
| Accept a customer quote you did not supply | If it is not in your notes, it was made up. Have it removed |
| Skip the phone check | A page can look right on a laptop and be unreadable on a phone |

## If it goes wrong

| What you see | What to say |
| --- | --- |
| It made up a number or a customer quote | "Remove anything that is not in my notes. Mark gaps with [needs: ...]." |
| It looks like every other AI page | Name a voice and a look, or go to [level 2](level-2-advanced.md) and put your own on file |
| Text is tiny or runs off the side on your phone | "Fix the layout at phone width. Nothing may scroll sideways." |
| It asks many questions before starting | "Make your best guess and list what you assumed." |

## What this level does not do

| It does not | Where that is |
| --- | --- |
| Remember your colours, fonts and layout between pages | [Level 2, Advanced](level-2-advanced.md) |
| Let an agent browse the library and choose for itself | [Level 3, Expert](level-3-expert.md) |

## Status

The instructions and sentences are written. They have not yet been run in fresh chats and scored,
and the quick way has not been tried from inside each chatbot.
