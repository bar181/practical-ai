# Example: a deck that teaches one skill

A worked example: what was asked, what came with it, what the studio chose and what came back. The business and every figure are invented.

## The request

> New staff start Monday. I want ten minutes at the start of the shift to teach the allergen check before anyone packs an order. Here is how we do it.

## The notes that came with it

- We are a bakery. Orders are packed at the bench from trays
- Every order label has an allergen line. Every tray has a tray card saying what is in the batch
- The check: read the allergen line on the label, match it against the tray card, and if they differ or one is missing, stop and ask the shift lead
- Real case we use in training: an order for two loaves with no sesame, and the tray was a seeded batch
- The one people miss: what was baked on the tray before. Plain rolls baked after almond croissants are not safe for a nut-free order
- It should take under a minute
- I want a card for the wall by the packing bench

## What the studio picked

For "explain how something works", "my own team" and "a slide deck", the picker chose **Workshop deck** (strong fit, 15 of 15). Workshop deck: a strong fit for "explain how something works", a strong fit for "my own team".

## How it was made

The assistant copied the workshop deck starter, [`deck-workshop.html`](../../templates/starters/deck-workshop.html), and replaced the words. The comparison on the second slide is the assistant's, and the note that came back says so.

## The output

- [`output.html`](output.html): the deck, seven slides, with an exercise on the fifth

## The note that came back with it

- **Chose:** the workshop deck, because the job is to teach and the readers are the team.
- **Assumed:** the seat belt comparison on slide two. It is mine, not from your notes. Change it if it does not fit.
- **Missing:** nothing. The notes covered every slide.
- **Check before sharing:** the wording of the three steps against your written procedure. This deck is training, not the procedure itself.

## What a good result must have

1. The first slide promises one skill the person can use that day
2. There are three steps or fewer, each something a person can do
3. One worked example is shown whole, taken from the notes
4. One slide is an exercise with a time limit, and it looks different from the others
5. The last slide can be printed as a card
6. Nothing about allergens is stated that is not in the notes

## Try it yourself

Give an assistant the request and the notes above, with the starter attached. Score what comes back against the list above, one point for each. Record the result in [`../README.md`](../README.md).
