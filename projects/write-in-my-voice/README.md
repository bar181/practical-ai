<p align="center"><img src="_build/img/app-icon.svg" width="104" alt="Write and edit in my voice icon: a pen over lines of writing"></p>

<h1 align="center">Write and edit in my voice</h1>

<p align="center"><b>Make it sound like you, without changing what you promised.</b><br>
For anyone whose emails and posts come out stiff or generic.</p>

<p align="center"><a href="#try-it-now"><img src="_build/img/btn-try.svg" height="48" alt="Try it with one prompt"></a></p>

<p align="center"><b>Free</b> &nbsp;·&nbsp; <b>No setup</b> &nbsp;·&nbsp; <b>Your own chatbot</b><br><b>Tested in Claude</b> &nbsp;·&nbsp; <b>In use by other people</b></p>

Ask a chatbot to "make this sound like me" and two things go wrong. It sounds like a chatbot, and
it quietly changes things: "may" becomes "will", a date moves, an offer appears that you never made.

- **Your voice, written down.** Three things you wrote become a short voice guide: each trait with
  your own words beside it and the stiff version it replaces. You read it and fix any line.
- **Your draft, in that voice.** Greeting, sign-off, sentence length and tone, from your samples.
- **Every fact checked.** Each date, price, name and promise, before and after, side by side.
  Nothing is added from your samples; "may" stays "may".

**Think of it as** a tailor's pattern. You are measured once from three things you wrote, every new
piece is cut to fit, and you still check the fit in the mirror.

## Try it now

Copy the whole box into the chatbot you use. It holds the link to the instructions, three invented
samples from a café owner and a stiff newsletter, so you see a result first. Then try your own:
replace the samples with three things you wrote, and the draft with yours.

```
Read the instructions at this link and follow them for the rest of this chat:
https://raw.githubusercontent.com/bar181/practical-ai/main/projects/write-in-my-voice/base/SKILL.md

## Sample 1 (email to staff)
Hi all,
Quick one. The new grinder arrives Thursday. Marco will show you how it works. It's simpler than the old one, I promise.
Thanks for a busy week. You were great.
Dana

## Sample 2 (post on the café page)
We're closed this Sunday for a family thing. Back Monday at 8. Sorry for the short notice. Sundays we normally close at 3, so not much lost, but still.
Dana

## Sample 3 (email to a regular)
Hi Ruth,
Thanks for the note about the oat milk. You're right, it ran out twice last week. We've doubled the order. Let me know if it happens again.
Dana

## The draft to revise (newsletter to customers)
Dear Valued Customers,
We are delighted to announce that, with effect from Tuesday 1 December 2026, Tallowmere Café will commence opening at 7:30am, Monday to Saturday. Furthermore, please be advised that the café will be closed on Friday 25 December. To celebrate, every regular-size filter coffee will be priced at £2.50 throughout the first week of December. We thank you for your continued patronage and look forward to welcoming you.
Kind regards,
The Management
```

**Your chatbot cannot open links?** Open [`base/SKILL.md`](base/SKILL.md), press **Raw**, copy all of
it into a new chat, then paste your samples and your draft.

**You get back:** a one-line count, your voice guide, the revised draft and the facts check.
[A worked example](base/examples/cafe-newsletter.md).

## Get started

**Level 1: paste the prompt.** No setup. Use the box above with your own samples. Read the voice
guide first and fix any line that is not you. Check the facts table, then send it yourself.

**Level 2: save your voice guide.** Keep the guide from your first chat as a file, and save the
instructions as a skill or in a Project. Next time you paste only the draft.
[Set up Level 2](level-2-files/README.md).

**Level 3: connected (planned, not built).** Your sent mail supplies the samples, and your
corrections update the guide after you approve them. Nothing is sent without you.

| Level | Core user | User story |
| --- | --- | --- |
| **1. Paste** | Anyone who writes emails or posts | As a café owner, I want my newsletter to sound like me, so that regulars read it as a note from Dana, not from "The Management" |
| **2. Saved guide** | Someone who writes the same kind of message every week | As a plumber, I want my saved voice used on every customer reply, so that I paste only the draft |
| **3. Connected** | A consultant who writes for several clients | As a consultant, I want the guide kept current from my corrections, so that the tenth draft needs fewer edits than the first |

## What it is not

- **Not a writer from nothing.** It revises a draft you have. It adds no facts, offers or apologies.
- **Not a sender.** You check the facts table and send it.
- **Not a brand style guide** for a team of writers. It learns one person.

## Status

**20 November 2026: new.** Built by its author with [Agentic Process](../agentic-process/) and tested
in fresh Claude sessions on three invented cases. [The evidence](quality-results/README.md).
**Users:** In use by people other than the author, from business owners to agentic developers (reported by Bradley, 22 November 2026); their results are not recorded here yet. **Not yet tried:** ChatGPT, Gemini and a saved voice guide. All people, businesses and samples in the examples are invented.

**Are you an AI agent?** Read [AGENTS.md](AGENTS.md).

## About Bradley Ross

Created by **Bradley Ross**, who builds and teaches practical AI. Part of
[Practical AI](../../README.md). [linkedin.com/in/bradaross](https://www.linkedin.com/in/bradaross/)

Licence: [Apache 2.0](LICENSE).
