# Artifact Studio: instructions for agents

You are here because a person wants a web page, a slide deck or a social post picture made from
their own content. This file is written for you. People start at the [README](README.md).

## The path

Take the first of these that you can do.

| You can | Do this |
| --- | --- |
| Load skills | Load [`level-2-files/artifact-studio/SKILL.md`](level-2-files/artifact-studio/SKILL.md) and follow it. It is the whole procedure, with reference cards it reads when needed |
| Call MCP tools, and the `artifact-studio` server is connected | Call `studio_overview`, then `recommend`. [`level-3-files/README.md`](level-3-files/README.md) lists every tool |
| Neither | Read [`base/AI-INSTRUCTIONS.md`](base/AI-INSTRUCTIONS.md). It is the same procedure in one file |

Whichever you use, the steps are the same: find out the job, the reader and the shape; choose a
template, a voice and a look and say why in one line; build one self-contained file from the
person's content only; check it; return it with the delivery note below.

## Where things are

| You need | Read |
| --- | --- |
| A complete small file to copy and fill, for a deck or a social picture | [`level-2-files/artifact-studio/assets/starters/`](level-2-files/artifact-studio/assets/starters/) |
| The skeleton every page is built on | [`page-skeleton.html`](level-2-files/artifact-studio/assets/page-skeleton.html) |
| The rules, and the cards for each recipe, voice and look | [`level-2-files/artifact-studio/references/`](level-2-files/artifact-studio/references/) |
| Every template with its fit scores, and reference code for each | [`level-3-files/mcp/library/`](level-3-files/mcp/library/): `index.json`, `sources/` and `svg/` |
| What a good result looks like | [`base/example.html`](base/example.html): one finished report. Its request and notes are in the README |
| The person's standing preferences | A file named `preferences.md`, if they have one. The template is [`level-2-files/preferences.md`](level-2-files/preferences.md) |
| Designs the person liked, in their own words | [`level-3-files/mcp/inspiration/`](level-3-files/mcp/inspiration/), or call `list_inspiration` |

## Inputs you can expect

| Input | Form | If it is missing |
| --- | --- | --- |
| Content | Notes, a document, a spreadsheet, a transcript, a link | Ask for it. Do not write a page from nothing |
| Media | Photos, a logo, a chart image, a video link | Build without. Never use a stock image as if it were theirs |
| Preferences | `preferences.md` | Use the defaults for the template |
| Request | A sentence, or a template id from the index | Choose with the rules above and say what you chose |

## Output contract

Return two things.

1. **One HTML file.** Self-contained, phone first, readable with motion off and with scripts off.
2. **A delivery note** with these four headings, in this order.

```
Chose: <template>, <voice>, <look>. <one line on why, if you chose>
Assumed: <each assumption, one per line, or "nothing">
Missing: <each gap marked [needs: ...] on the page, or "nothing">
Check before sharing: <the numbers, names and claims a person must verify>
```

## Rules that never bend

1. No invented facts. Mark gaps as `[needs: ...]`.
2. A voice is a style. Never attribute words to the person who inspired it.
3. Every company, person and figure in the templates is invented. Adapt the pattern and never
   carry the example content into the person's page.
4. When the person shows you a design they like, record the idea in your own words. Do not copy
   its text, pictures, logo, characters or code.
5. Stop before anything is posted, sent or published. A person decides.

## To change the library

Edit the files in [`_build/`](_build/), run `python3 _build/build.py`, and check that both gallery
files open: `base/studio.html` and `base/components.html`. Never edit a generated file. Each one says so at the top.

## Known limits

- The skill has not yet been run end to end by a second agent. Treat the first runs as tests.
- The MCP server has been tested with a client on the machine that built it, not inside a desktop
  assistant. Nothing is hosted.
