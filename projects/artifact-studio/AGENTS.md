# Artifact Studio: instructions for agents

You are here because a person wants a web page, a slide deck or a social post picture made from
their own content, and wants it to look designed. This file is written for you. People start at the [README](README.md).

Artifact Studio is the design step. If the person mainly needs the words in a tone (a pitch, a
one-pager, a story), go to [Tone Studio](../tone-studio/AGENTS.md). If they mainly need the sections
of a site laid out, go to [Web Sections](../web-sections/AGENTS.md). If they hand you words or
sections from either, keep them and design around them.

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
| How to show a social post, an email or a blog as its audience will see it | Moved to [Web Sections](../web-sections/AGENTS.md) on 21 November 2026: its post previews page and reference |
| The skeleton every page is built on | [`page-skeleton.html`](level-2-files/artifact-studio/assets/page-skeleton.html) |
| Which effect fits which job, including the cinematic effects | [`effects-index.md`](level-2-files/artifact-studio/references/effects-index.md) |
| The rules, and the cards for each recipe, voice and look | [`level-2-files/artifact-studio/references/`](level-2-files/artifact-studio/references/) |
| Every template with its fit scores, and reference code for each | [`level-3-files/mcp/library/`](level-3-files/mcp/library/): `index.json`, `sources/` and `svg/` |
| Every template, voice and effect, open in a browser | [`showcase.html`](showcase.html) (photo, scroll and cinematic effects, layouts, social picture sizes, voices) and [`components.html`](components.html) (pages, decks, parts, design ideas, the picker, the skill). Live at https://bar181.github.io/practical-ai/artifact-studio/showcase.html and https://bar181.github.io/practical-ai/artifact-studio/components.html |
| What a good result looks like | [`base/examples/`](base/examples/): one worked example for each voice, for photo effects and for a report. Each shows the prompt, the sample input and the finished page. [`before-after/`](base/examples/before-after/) is one lesson the author made for a client three ways (plain, teacher, story) from one source, with that source |
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
Missing: <every gap, one per line, or "nothing". Say which are marked [needs: ...] on the page>
Check before sharing: <the numbers, names and claims a person must verify>
```

## Rules that never bend

1. No invented facts. A gap that would mislead the reader is marked `[needs: ...]` on the page.
   Every gap is listed in the delivery note.
2. A voice is a style. Never attribute words to the person who inspired it.
3. Every company, person and figure in the templates is invented, except on the visionary page,
   which is about this repository and names its author. Adapt the pattern and never
   carry the example content into the person's page.
4. When the person shows you a design they like, record the idea in your own words. Do not copy
   its text, pictures, logo, characters or code.
5. Stop before anything is posted, sent or published. A person decides.

## To change the library

Edit the files in [`_build/`](_build/), run `python3 _build/build.py`, and check that
the two master pages, `showcase.html` and `components.html`, and the files in `base/examples/` open. Never edit a generated file. Each one says so at the top.

## Known limits

- A second agent ran the skill end to end on 16 November 2026 and an agent built a page from the
  MCP tools alone. Both worked and both reported friction; the logs are in
  [`_build/examples/runs/`](_build/examples/runs/). Read `friction.md` there before you trust a rule
  that looks odd.
- The MCP server has not been tried inside a desktop assistant, and it is not hosted. The two master
  pages and the worked examples are published to GitHub Pages by `.github/workflows/pages.yml`.
