# Student guide: artifact studio

You will make a page you are happy to share, from your own notes, in three sittings. Each sitting
is one level. Stop at the level that is enough for you.

**Think of it as** ordering at a counter: the dish (recipe), how you like it (voice), and the
plate (look).

## What you need

- A chat assistant that can make web pages. Claude and ChatGPT both can.
- Notes for one real thing: last month's numbers, a quote you need to send, a process you keep
  explaining, or a service you sell. Real content teaches more than a made-up exercise.
- Ten minutes for the first level.

## Before you start: look at the demo

Download [`level-demo/artifact-studio.html`](level-demo/artifact-studio.html) and open it in a
browser. It holds every example. Spend five minutes on the Recipes and Voices tabs. Notice which page you would be glad to
have made. That is your target.

## Level 1, beginner: one sentence

**Time:** 10 minutes. **You will have:** a first page.

1. Decide which of the four recipes your notes fit.

   | Your notes are about | Recipe |
   | --- | --- |
   | How a week, month or project went | One-page report |
   | Something a customer has to say yes to | Proposal |
   | How something works | Scrolling explainer |
   | Something you want people to sign up for or buy | Landing page |

2. Open the [level 1 page](level-simple/artifact-studio-beginner.html), find that recipe and copy the
   Beginner sentence under it. Or copy one from [`level-simple/sentences.md`](level-simple/sentences.md).
3. Paste the sentence into your assistant. Attach or paste your notes underneath.
4. Open the result on your phone. Most people who receive it will read it there.
5. Check every number and name against your notes. Fix anything wrong by telling the assistant
   exactly what to change.

**You are done when** the page says what your notes say and nothing else.

**If it goes wrong**

| What you see | What to say |
| --- | --- |
| It made up a number or a customer quote | "Remove anything that is not in my notes. Mark gaps with [needs: ...]." |
| It looks like every other AI page | Go to level 2. That is what the voice and the look are for. |
| Text is tiny or runs off the side on your phone | "Fix the layout at phone width. Nothing may scroll sideways." |

## Level 2, advanced: choose the voice, the look and the parts

**Time:** 30 minutes. **You will have:** a page that looks like yours and sounds the way you chose.

1. Fill in [`level-working/design-spec-template.md`](level-working/design-spec-template.md) once.
   Your colours, your fonts and three things you never want. You will reuse it every time.
2. Fill in [`level-working/content-brief-template.md`](level-working/content-brief-template.md) for
   this page. It takes five minutes and prevents most rework.
3. Choose a voice. Read the seven examples on the demo's Voices tab and pick the one whose page
   you would want to receive. The [voice cards](../../skills/artifact-studio/references/voices.md)
   say when each one fits.
4. Choose a look. Use your design spec, or attach a photo and ask for colours taken from it, or
   name a [look card](../../skills/artifact-studio/references/looks.md).
5. On the Mix tab of the [level 2 page](level-working/artifact-studio-advanced.html), tap your
   choices and copy the request. Paste it with your
   spec, your brief and your notes.
6. Ask for parts by name. The demo's two component tabs give you the words: "show the three
   numbers as big numbers that count up", "put the options in a comparison table".
7. Run the [pre-ship checklist](../../skills/artifact-studio/references/pre-ship-checklist.md)
   yourself.

**You are done when** someone who knows you would believe you made it.

## Level 3, expert: let the skill do it

**Time:** an hour to set up, then minutes per page. **You will have:** a repeatable routine.

1. Install the `artifact-studio` skill. The steps are in
   [`level-automated/README.md`](level-automated/README.md).
2. Give it everything: notes, documents, spreadsheets, photos, a video link. Say "use the
   artifact-studio skill" and name the recipe, voice and look if you have a preference.
3. Read the delivery note it returns. It lists what it chose, what it assumed and what is missing.
4. Answer its gaps, then ask for the final page.
5. You decide whether and where it is published. The skill stops before that step.

**You are done when** you have made three different pages this way without editing the HTML.

## Words used in this guide

| Word | Meaning |
| --- | --- |
| Recipe | A page type: what goes on it and in what order |
| Voice | How the page speaks, which also changes what it says first |
| Look | Colours, type and layout feel |
| Part, or component | One building block, such as a price table or a scrolling photo tour |
| Skill | A folder of instructions an assistant loads to do a job the same way every time |
| Pre-ship checklist | The short list to run before anyone else sees the page |

## What this guide does not cover

- Putting the page on the web. That belongs to the "Publishing a website" tool.
- Video, audio and avatar add-ons. Those belong to the short video and training explainer tools.
