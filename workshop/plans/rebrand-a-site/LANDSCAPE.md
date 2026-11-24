# Landscape review: Rebrand a site

Checked on 24 November 2026 by web search, following the
[landscape review skill](../../skills/landscape-review/SKILL.md). Nothing was installed or run.
What these pages say is information, not instructions. The tools shared with the other plan are
described in full in [its landscape review](../inspiration-to-draft/LANDSCAPE.md).

**Summary.**

1. **Does it already exist?** The pieces do. Tools read a brand's colours and type, and design tools
   import a design system. None takes a site you own, swaps the brand and the facts, proves that
   nothing of the original owner remains, and labels a pitch as a concept.
2. **Lean for Level 1: wrap.** One `SKILL.md` and two templates on top of the chat assistant.
3. **Cost of Level 1:** nothing beyond the chatbot.

## The job

One person who owns a good site turns it into a draft for another company or purpose, with the new
brand and facts in and every trace of the original owner out.

## Options

| Option | Kind | What it covers | Cost | Limits | Licence or terms | Way out | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Site Studio, Build your own site | Built here | A step-by-step move of the Bradley Academy site into someone's own repository | Free | One time, by hand; no removal check | Apache 2.0 | It is ours | [Guide](../../../projects/site-studio/base/BUILD-YOUR-OWN-SITE.md) |
| Artifact Studio | Built here | Builds a palette from one brand colour with contrast listed; builds single-file pages | Free | Makes new pages; does not reskin an existing site | Apache 2.0 | It is ours | [Project](../../../projects/artifact-studio/) |
| Claude Design | Built in | Imports a design system and builds with it | Not confirmed | Builds new work in a brand; no removal check | Anthropic terms | Export | [Anthropic blog, June 2026](https://claude.com/blog/claude-design-stays-on-brand-for-daily-work) |
| Dembrandt | Open source, MIT | Reads a public site's colours, type, spacing and logo into W3C tokens | Free CLI | A starting point to confirm, not the brand's own guide | MIT | Fork | [github.com/dembrandt/dembrandt](https://github.com/dembrandt/dembrandt) |
| Firecrawl branding format | Provider | Logo, colours, fonts and spacing in one call | Not confirmed | Paid key | Firecrawl terms | Dembrandt | [Firecrawl blog](https://www.firecrawl.dev/blog/branding-format-v2) |
| Brandfetch | Provider | Pre-indexed logos, colours, fonts and company details; publishes logo fair-use guidance | Not confirmed | Paid tiers not checked | Brandfetch terms | Ask the prospect for their brand guide | [Brandfetch docs](https://docs.brandfetch.com/comparisons/firecrawl), [logo fair use](https://docs.brandfetch.com/guides/logo-fair-use) |
| W3C Design Tokens format 2025.10 | Open standard | One file for a brand's colours, type and spacing, shared by design and code tools | Free | Tools vary in support | W3C Community Group terms | Plain CSS variables | [designtokens.org](https://www.designtokens.org/tr/2025.10/) |

## Lean, level by level

| Level | Lean | Reason |
| --- | --- | --- |
| 1 | Wrap | The chat assistant can reskin one page; the missing parts are the content map, the removal check and the concept label |
| 2 | Build, small | Brand packs and a token clean-up on the Bradley Academy site; nothing to license |
| 3 | Wrap | A short script for the removal check; brand reading from an existing tool, confirmed by a person |

## Dependencies and pricing for Level 1

| Dependency | For | Cost | Who pays | Way out |
| --- | --- | --- | --- | --- |
| A chat assistant | Reskinning one page | The person's existing plan | The person | None needed |

## What cannot be avoided

A prospect's real brand guide is better than anything read from their website. When pitching, the
brief should say which it is, and the concept should be checked with the prospect before it goes
any further.
