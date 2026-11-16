# Inspiration: taking in something you like

You see a page, a deck or a post that works. This folder is how it gets into the studio without
copying it.

**Think of it as** a chef eating at another restaurant. You come home with the idea of the dish,
written in your own words. You do not come home with their plate.

## The three outcomes

| Outcome | When | What happens |
| --- | --- | --- |
| A note | It is interesting and you are not sure why yet | The card stays in `inbox/` |
| A change to an existing template | The library already has something close | The card names the template and the change. The template is edited and rebuilt |
| A new part or template | Nothing in the library does this job | It is built to the same rules as everything else, added to the catalogue, and appears in the index |

## Steps

1. **File a card.** Tell your assistant what you saw and why it works, or write the card yourself
   from [`card-template.md`](card-template.md) and save it in [`inbox/`](inbox/). With the MCP
   server connected, the assistant can file it for you with the `add_inspiration` tool.
2. **Say what works, in your own words.** Structure, order, rhythm, proportion, how a number is
   shown, where the eye goes first. Three to six lines.
3. **Compare it with the library.** Open the studio page, `base/studio.html`, and
   name the closest template or part. Most new finds are a variation on something already here.
4. **Decide the outcome** from the table above and write it on the card.
5. **If it becomes a part or a template,** follow "Adding to the library" below.
6. **Move the card** from `inbox/` to this folder once decided, so the inbox only holds open ones.

## Using what is on file

A card is read again when something is made. An assistant following [`AGENTS.md`](../../../AGENTS.md)
reads the cards before it chooses a voice, a look and parts, and with the MCP server connected it
calls `list_inspiration`. Tags on a card (page, deck, social, motion, number, photo) are how it
finds the ones that matter for the job.

## What may and may not come in

| May | May not |
| --- | --- |
| The idea, described in your own words | The original's text, pictures, logo, characters or code |
| A structure: "one number, then the old number struck through" | A copy close enough to be mistaken for the original |
| A link to where you saw it | A saved copy of someone else's page or file |
| Your own screenshots of your own work | Screenshots of other people's work, in this repository |

A design idea is free to learn from. A specific piece of work belongs to whoever made it. When
unsure, describe it and link to it.

## Adding to the library

| To add | Do this | It is done when |
| --- | --- | --- |
| An animated SVG | Add one `.svg` file to `_build/svg/` with a `<title>` and a `<desc>` | It makes sense when still, stops under reduced motion, and its styles are scoped to its own id |
| A page or photo part | Add a section to `_build/views/30-parts.html` or `20-photo.html` with an `@@ask` line | It works at phone width with motion off and has a sentence |
| A template | Add a view file to `_build/views/`, an entry in `_build/catalog.py` with its fit scores, and a line in `build.py` | It opens cleanly at phone width and passes the pre-ship checklist |

Then run `python3 build.py` in `_build/`. The index, the studio page and the sentences are
regenerated, so the new piece appears everywhere at once.

## Status

The process is written and the `add_inspiration` tool has been tested. No real find has been taken
through it yet.
