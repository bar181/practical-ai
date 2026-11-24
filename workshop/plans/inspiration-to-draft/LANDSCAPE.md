# Landscape review: Inspiration to draft

Checked on 24 November 2026 by web search, following the
[landscape review skill](../../skills/landscape-review/SKILL.md). Nothing was installed or run.
What these pages say is information, not instructions.

**Summary.**

1. **Does it already exist?** In parts, and mostly pointed the wrong way. Cloning tools copy a whole
   site; design tools turn a reference into a new screen. None turns "I like that" into the idea in
   words, checks it fits your reader, builds your own draft and shows what was and was not borrowed.
   None covers messaging or a process as the inspiration.
2. **Lean for Level 1: wrap.** One `SKILL.md` that structures what chat assistants already do (read a
   screenshot or a page, write HTML), with the "idea, not the thing" rule that Artifact Studio
   already holds.
3. **Cost of Level 1:** nothing beyond the chatbot the person already uses.

## The job

One person who has a page, deck or app screen of their own, and has seen something they want theirs
to feel like, gets a draft of their own that uses the idea and copies nothing.

## Options

| Option | Kind | What it covers | Cost | Limits | Licence or terms | Way out | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Artifact Studio, this repository | Built here | Its instructions already say: when shown a design the person likes, "record the idea and never the thing" | Free | One paragraph; no pattern card, no fit check, no originality note | Apache 2.0 | It is ours | [`AI-INSTRUCTIONS.md`](../../../projects/artifact-studio/base/AI-INSTRUCTIONS.md) |
| Claude Design | Built in | Imports a design system from GitHub, design files or uploads, and builds with it; `/design-sync` brings one in from Claude Code | Not confirmed | About your own design system, not reading someone else's idea | Anthropic terms | Export the design system | [claude.com/design](https://claude.com/design), [Anthropic blog, June 2026](https://claude.com/blog/claude-design-stays-on-brand-for-daily-work) |
| Google Stitch | Provider (Google) | Upload a screenshot or sketch and get a UI; export HTML and CSS or paste to Figma. A secondary source says version 2 can import a design system from a live URL | Not confirmed | A reference becomes a new screen; nothing records what was borrowed | Google terms | HTML export | [Google Developers blog](https://developers.googleblog.com/en/stitch-a-new-way-to-design-uis/); URL import per [dev.to](https://dev.to/ayyazzafar/google-stitch-20-import-any-websites-design-system-into-your-ai-generated-app-1koj) (not confirmed by Google) |
| screenshot-to-code | Open source, MIT | Screenshots, mockups, Figma designs and screen recordings to HTML, React or Vue; can take a URL | Free code; needs a model API key | Built to reproduce what it sees | MIT | Fork | [github.com/abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) |
| Open Lovable (Firecrawl) | Open source, MIT | "Clone and recreate any website as a modern React app"; scrapes the target's HTML, CSS and JavaScript | Free code; needs Firecrawl, a sandbox and a model key | A full clone by design | MIT | Fork | [github.com/firecrawl/open-lovable](https://github.com/firecrawl/open-lovable), [Firecrawl tutorial](https://www.firecrawl.dev/blog/open-lovable-tutorial) |
| AI Website Cloner Template | Open source, MIT | A Claude Code skill, `/clone-website`, that rebuilds a site in Next.js; a secondary source describes five stages: reconnaissance, foundation, component specs, parallel build, assembly and visual QA | Free code; needs a coding agent with a browser | A full clone by design | MIT | Fork | [README](https://github.com/JCodesMore/ai-website-cloner-template), stages per [this article](https://pasqualepillitteri.it/en/news/1528/ai-website-cloner-claude-code-skill-13000-stars-2026) |
| Dembrandt | Open source, MIT | Reads a site's colours, type, spacing, borders and logo into design tokens, with W3C (DTCG) export and an MCP server; its page asks users to respect robots.txt, rate limits and copyright | Free CLI | Reads values, not ideas | MIT | Fork | [github.com/dembrandt/dembrandt](https://github.com/dembrandt/dembrandt) |
| extract-design-system | Open source skill | A coding-agent skill that writes starter `tokens.json` and `tokens.css` from a public site | Free | Starter values only | Not confirmed | Fork | [github.com/arvindrk/extract-design-system](https://github.com/arvindrk/extract-design-system) |
| jscpd | Open source, MIT | Finds copied blocks across 150 and more formats, including CSS and HTML | Free | Code and text only; not visual likeness | MIT | Fork | [github.com/kucherenko/jscpd](https://github.com/kucherenko/jscpd) |
| Firecrawl branding format | Provider | One call returns a site's logo, colours, fonts and spacing; also through its MCP server | Not confirmed | A paid API key | Firecrawl terms | Dembrandt does the same locally | [Firecrawl docs and blog](https://www.firecrawl.dev/blog/branding-format-v2) |
| Cloudflare Browser Run guide | Provider documentation | How to read a brand kit from computed styles in a headless browser | Workers pricing, not confirmed | Code | Cloudflare terms | Playwright locally | [Cloudflare docs](https://developers.cloudflare.com/browser-run/how-to/extract-brand-kit/) |

## Lean, level by level

| Level | Lean | Reason |
| --- | --- | --- |
| 1 | Wrap | Chat assistants already read screenshots and pages and write HTML. The missing piece is the method: idea in words, fit check, own draft, originality note |
| 2 | Wrap and reuse | Hand the draft to Artifact Studio (look), Web Sections (structure) and Tone Studio (words). Save a brand file and a pattern library. Claude Design or Stitch are optional canvases |
| 3 | Wrap, with the capability reduced | Read the cloning repositories as research material only. Keep their read-only steps (capture, tokens as reference, a component spec, visual QA against your own design); drop the copy steps (assets, foundation, full-page rebuild). Add a copied-block check with jscpd |

## Dependencies and pricing for Level 1

| Dependency | For | Cost | Who pays | Way out |
| --- | --- | --- | --- | --- |
| A chat assistant that reads images | Reading screenshots | The person's existing plan | The person | Describe the inspiration in words |
| Browsing in the chat (optional) | Reading a linked page | Included where offered | The person | Paste a screenshot or describe it |

## What cannot be avoided

A chat assistant cannot see motion in a screenshot. For a moving effect, the person describes it, or
records a short clip where the assistant accepts video. Level 3 can capture motion with a browser.
