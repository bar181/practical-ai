# Artifact studio: student guide

By the end you will have a design spec of your own, and one page built twice in two different
styles so you can see the difference a style card makes.

## Why pages come out "meh"

An assistant asked for "a page about X" has to guess the look. A guess aims for the middle, and the
middle is generic. The fix is to stop making it guess: decide the look once, then name a style
every time you ask.

## Step 1: Fill in your design spec, once

Use [`level-simple/design-spec-template.md`](level-simple/design-spec-template.md). Ten minutes.
Colours, fonts, spacing, tone of the words, three things you never want.

You will attach this to every request from now on.

## Step 2: Say what the page is for

Two sentences: what it is for, and who will use it. Then name the one thing a visitor should do.

**One page, one job.** A calculator calculates. A landing page lands. Split anything that does two.

## Step 3: Pick a style card

Read [`level-simple/style-cards.md`](level-simple/style-cards.md).

| Style | Choose it when |
| --- | --- |
| Clean | The content is the point and should be read quickly |
| Cinematic | You want an impression first and detail second |
| Scrollytelling | There is a story or a sequence to walk through |
| Dashboard | People will come back to check numbers |
| Editorial | It is long-form reading |

## Step 4: Ask for it

Give the assistant three things together: the two sentences, the design spec and the style card.
For anything visual, ask for two directions and choose one.

Give feedback in three lists: keep, change, remove.

## Step 5: Run the pre-ship checklist

Use [`level-simple/pre-ship-checklist.md`](level-simple/pre-ship-checklist.md). The two most common
failures in generated pages are a layout that breaks on a phone and text that is hard to read
against its background.

## Step 6: Share or host it

| Route | Use when | Trade-off |
| --- | --- | --- |
| A shared link from your assistant | A quick demo or a private preview | Lives inside that product |
| A hosted static site | It needs a public address or your own domain | Needs a hosting account. One option is a static site served from an edge platform, which an agent can deploy for you |
| A page in a code repository | The work already lives in a repository | Simple. Check the limits of your plan |

A public page is one share away from anyone. Keep private material out of it, and let a person,
not an agent, make the decision to publish.

## Good habits

1. **Design for the phone first.**
2. **Real content, never placeholder text.** Placeholder text hides layout problems.
3. **One primary action per screen.**
4. **Keep a hand-built page in one self-contained file.**
5. **Do not rely on the browser remembering things.** Saved state can come back empty.
6. **Show a draft early.** Two rough directions beat one polished guess.

## Add-ons, for later levels

A page can carry more than text: a short explainer video, a 20-second avatar clip, a generated
audio track. Each costs money per render and each needs a person to review it. They belong to the
working and automated levels. See the short video guide for how each is made.

## Guardrails

- Never build a page that imitates another organisation's site, sign-in or branding.
- No private or client material on a public page.

## Try it

1. Fill in the design spec.
2. Ask for the same one-page explainer twice: once as Clean, once as Scrollytelling.
3. Run both through the checklist. Note what the style card changed and what it did not.

## Open slots in this draft

- A gallery page showing one request in every style
- One hosting route confirmed end to end, with exact steps
- Example pages worth imitating, with a note on why each works

## Sources

Checked 2026-11-14.

- [Managing an edge platform through an agent connection](https://www.fast.io/resources/mcp-server-for-cloudflare.md)
- [Serving a static site and deploying it in one step](https://dev.to/umesh_malik/deploy-an-mcp-server-on-cloudflare-workers-free-stateless-at-the-edge-31d6)
