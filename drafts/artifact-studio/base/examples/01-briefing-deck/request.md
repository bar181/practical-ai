# Example: a deck for a decision

A worked example: what was asked, what came with it, what the studio chose and what came back. The business and every figure are invented.

## The request

> I need to get the partners to agree to Saturday opening at the clinic. Make me a short deck for Thursday's meeting from these notes.

## The notes that came with it

- We are a physiotherapy clinic with four physiotherapists
- Evening appointments are booked three weeks ahead
- 41 people are on the waiting list for an evening or weekend appointment
- Spring survey: 58 of 90 patients said they would use a Saturday
- Proposal: Saturday 9 to 1, two physiotherapists (8 hours) and reception (4 hours), which gives 8 appointments
- Other option we discussed: later weekday evenings, about 6 extra staff hours a week
- Not sure if Saturday people would be new patients or just weekday ones moving
- Not sure the two who volunteered will want to keep doing it
- Want an eight-week trial

## What the studio picked

For "get a decision", "a busy decision-maker" and "a slide deck", the picker chose **Briefing deck** (strong fit, 15 of 15). Briefing deck: a strong fit for "get a decision", a strong fit for "a busy decision-maker".

## How it was made

The assistant copied the briefing deck starter, [`deck-briefing.html`](../../templates/starters/deck-briefing.html), and replaced the words on each slide with the notes. Nothing was added that is not in the notes.

## The output

- [`output.html`](output.html): the deck, six slides. Open it in a browser. Arrow keys move, N shows the speaker's notes

## The note that came back with it

- **Chose:** the briefing deck, because the job is a decision and the readers are the people who decide.
- **Assumed:** 12 staff hours is the sum of 8 hours of physiotherapy and 4 of reception, as the notes give them.
- **Missing:** a start date for the trial. The last slide shows the gap.
- **Check before sharing:** the survey figures, and whether the partners have seen the waiting list.

## What a good result must have

1. The first slide states the recommendation in one sentence
2. Every number on the slides appears in the notes: 41, 58 of 90, 12 hours, 8 appointments, eight weeks
3. The options slide includes doing nothing, and marks the recommended option
4. A slide says what is not known
5. The missing start date is marked as missing, not invented
6. The file opens with no internet connection and arrow keys move between slides

## Try it yourself

Give an assistant the request and the notes above, with the starter attached. Score what comes back against the list above, one point for each. Record the result in [`../README.md`](../README.md).
