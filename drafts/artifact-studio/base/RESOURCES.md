# Outside help: skills, open source and paid services

The studio makes one kind of thing well: a single self-contained page, deck or post picture, built
by an assistant from your content. This page lists what to reach for when you need something else,
and what is already better than anything here.

Checked on 2026-11-15 unless a row says otherwise. Nothing on this page has been installed or
tested for this review. **Prices are left out on purpose:** the sources found disagree with each
other, and prices change. Read the vendor's own page.

## When to use something else

| You need | Use | Why not the studio |
| --- | --- | --- |
| A deck someone will edit in PowerPoint or Google Slides | A slide service below, or your assistant's own deck feature | The studio's decks are web pages. They present well and do not open in a slide editor |
| Many posts on a schedule, with brand locked down for a team | A design service below | The studio makes one picture at a time and has no scheduling |
| A deck written as text and kept in a code repository | An open-source slide framework below | They have speaker notes, export and plugins that the studio's small engine does not |
| Heavy animation or video | The libraries in the [landscape review](../landscape-review.md), or the short video guide in this repository | The studio keeps motion small on purpose |

## Skills for assistants

| Skill | What it adds | Source |
| --- | --- | --- |
| frontend-design, web-artifacts-builder, theme-factory | Anthropic's own skills for design judgement, multi-part artifacts and ready-made themes | [anthropics/skills](https://github.com/anthropics/skills), checked 2026-11-14 |
| Community skills for scroll effects and animated components | Recipes for one library each | Listed with links in the [landscape review](../landscape-review.md). Unreviewed. Read one before installing it |

The studio's own skill is in [`skills/artifact-studio/`](../../../skills/artifact-studio/). It uses the same open
skill format, so it can sit beside any of these.

## Open-source slide frameworks

| Framework | Write in | Best for | Licence | Source |
| --- | --- | --- | --- | --- |
| reveal.js | HTML, or Markdown with a plugin | The most control. The oldest and largest of the browser slide frameworks | MIT | [opendesigner.io](https://opendesigner.io/blog/reveal-js), [open-design.ai](https://open-design.ai/ja/blog/slidev/) |
| Slidev | Markdown with Vue components | Technical talks with live code, and decks kept beside the project they describe | MIT | [PkgPulse](https://www.pkgpulse.com/guides/slidev-vs-marp-vs-revealjs-code-first-presentations-2026), [open-design.ai](https://open-design.ai/ja/blog/slidev/) |
| Marp | Markdown only | The simplest route from notes to slides, with HTML, PDF and PowerPoint output from one command | MIT | [PkgPulse](https://www.pkgpulse.com/guides/slidev-vs-marp-vs-revealjs-code-first-presentations-2026), [marp-cli](https://best-of-web.builder.io/library/marp-team/marp-cli) |

One limit applies to all three. Their PowerPoint export produces pictures of slides, not slides
you can edit ([open-design.ai](https://open-design.ai/ja/blog/slidev/), [opendesigner.io](https://opendesigner.io/blog/reveal-js)).

## Open-source libraries for motion, charts and components

Already reviewed, with licences, in the [landscape review](../landscape-review.md): GSAP, Motion,
Anime.js, Scrollama, Observable Plot, D3, Apache ECharts, Chart.js and four component sets.

## Paid services

| Service | What it is best at | Source |
| --- | --- | --- |
| Gamma | Turning a prompt into a presentation, a document, a small site or a social graphic, with export to PowerPoint or Google Slides. Has a free plan | [The Neuron, 1 September 2026](https://www.theneuron.ai/guides/best-ai-presentation-makers/) |
| Canva | One tool for slides, social posts, handouts and print, with brand kits and a very large template library | [The Neuron](https://www.theneuron.ai/guides/best-ai-presentation-makers/), [Dupple, October 2026](https://dupple.com/learn/best-presentation-software) |
| Beautiful.ai | Layouts that rearrange themselves as you add content, which keeps a team's decks consistent | [The Neuron](https://www.theneuron.ai/guides/best-ai-presentation-makers/), [Presentations.AI](https://www.presentations.ai/tr/compare/beautiful-ai-vs-gamma-vs-presentations-ai) |
| Plus AI, Pitch, Microsoft 365 Copilot | Named in the same comparisons. Not looked at further here | [Dupple, October 2026](https://dupple.com/learn/best-ai-presentation-tools) |

Two cautions from the same sources. Export to PowerPoint is where several of these tools lose their
layout ([Presentations.AI](https://www.presentations.ai/blog/best-ai-presentation-makers)). And
products in this category close: one comparison records that Tome ended its presentation product
([PostEverywhere](https://posteverywhere.ai/blog/15-best-ai-presentation-makers)).

Most of these sources are comparison sites, and some sell a competing product. Treat the
"best for" column as a starting point.

## Connecting the studio to an assistant

| Assistant | How | What it needs | Source |
| --- | --- | --- | --- |
| Desktop assistants that run local MCP servers, such as Claude Desktop | Add the server to the assistant's MCP settings as a command | Python and the `mcp` package on the same computer | From general knowledge. Not rechecked today. Steps are in [`level-3/mcp/`](../level-3/mcp/) |
| ChatGPT | Turn on developer mode, then add the server as a custom connector | A server reachable at an HTTPS address ending in `/mcp`. A file on your own computer is not enough | [Boomi](https://help.boomi.com/docs/Atomsphere/Platform/Connect_chatgpt_setup), [Celigo](https://developer.celigo.com/mcp/connect/chatgpt), [Dataddo](https://docs.dataddo.com/docs/chatgpt.md) |

Details that matter for ChatGPT, from those pages: developer mode is a beta on paid plans and on the
web app; on business plans an admin may have to allow it; the connector form offers sign-in by
OAuth or no sign-in at all; and one guide says the individual plans are limited to tools that only
read. The guides do not fully agree on plans, so check your own account.

## Still to do

- Install and try one outside skill beside the studio's own.
- Rebuild one studio deck in reveal.js or Marp and compare the effort.
- Recheck this page before relying on it. It was written in one sitting.
