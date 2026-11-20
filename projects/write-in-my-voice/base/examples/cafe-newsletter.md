# Worked example: a café newsletter

**Invented.** The café, the owner and the samples are made up. This is the reply a fresh Claude
session gave on 20 November 2026 when given [`../SKILL.md`](../SKILL.md) and the input below. It
was graded against the [answer key](../../_build/eval/t1-key.md) and passed.

## The input

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

## The reply (output, unedited)

**In short:** 3 facts kept, 5 reworded, 0 changed. Voice: brief, warm, plain.

**Assumed:**
- Three samples, all signed Dana. I assumed this goes to customers by email or on the café page.
- Changed "Dear Valued Customers," to "Hi all," and "Kind regards, The Management" to "Dana", as in your samples. Moved the coffee offer up so "To celebrate" follows the new hours, not the Christmas closure.
- Kept "the first week of December" as written. Customers may ask which days, so you may want to name them.

### Your voice guide

| Trait | On voice (from your samples) | Off voice |
| --- | --- | --- |
| Short sentences, one idea each | "The new grinder arrives Thursday." | "We are pleased to confirm that the new grinder is scheduled for delivery on Thursday." |
| Gets straight to the point | "Quick one." | "We are delighted to announce that..." |
| Greets with "Hi" and a name or "all" | "Hi all," | "Dear Valued Customers," |
| Signs with first name only | "Dana" | "Kind regards, The Management" |
| Uses contractions | "We're closed this Sunday for a family thing." | "We are closed this Sunday owing to a family matter." |
| Thanks plainly, for something specific | "Thanks for the note about the oat milk." | "We thank you for your continued patronage." |
| Says sorry in a few words | "Sorry for the short notice." | "Please accept our sincere apologies for any inconvenience caused." |
| Everyday words, no exclamation marks or emoji | "It's simpler than the old one, I promise." | "The new model offers a significantly streamlined experience!" |

**Words to avoid:** "Dear Valued Customers" → "Hi all"; "we are delighted to announce that" → "Quick one."; "with effect from" → "from"; "commence opening" → "open"; "Furthermore, please be advised that" → drop it and just say it; "priced at" → "will be"; "throughout" → "all through"; "We thank you for your continued patronage" → "Thanks for coming in."; "look forward to welcoming you" → "See you soon."; "Kind regards, The Management" → "Dana".

Fix any line that is not you, and I will use the fixed guide.

### Revised draft

> Hi all,
> Quick one. From Tuesday 1 December 2026, Tallowmere Café will open at 7:30am, Monday to Saturday. To celebrate, every regular-size filter coffee will be £2.50 all through the first week of December. We'll be closed on Friday 25 December. Thanks for coming in. See you soon.
> Dana

### Facts check

| # | In your draft | In the revision | Status |
| --- | --- | --- | --- |
| 1 | "with effect from Tuesday 1 December 2026" | "From Tuesday 1 December 2026" | Kept, reworded: same start date |
| 2 | "Tallowmere Café" | "Tallowmere Café" | Kept |
| 3 | "will commence opening at 7:30am" | "will open at 7:30am" | Kept, reworded: same time, "will" kept |
| 4 | "Monday to Saturday" | "Monday to Saturday" | Kept |
| 5 | "the café will be closed on Friday 25 December" | "We'll be closed on Friday 25 December" | Kept, reworded: "we" is the café, "will" kept as "we'll" |
| 6 | "every regular-size filter coffee" | "every regular-size filter coffee" | Kept |
| 7 | "will be priced at £2.50" | "will be £2.50" | Kept, reworded: same price |
| 8 | "throughout the first week of December" | "all through the first week of December" | Kept, reworded: same period |

Check the facts table, then send it yourself.
