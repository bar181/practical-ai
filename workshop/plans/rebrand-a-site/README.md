# Plan: Rebrand a site

Written on 24 November 2026 by following [Agentic Process](../../../projects/agentic-process/),
steps 1 to 6, with the plan template. Step 2 was searched on the web on that date:
[the landscape review](LANDSCAPE.md). **Not yet approved by the owner;** the gates that need him are
at the end. This is one of two plans from one request. The other is
[Inspiration to draft](../inspiration-to-draft/README.md).

One-line promise: turn a site you own into a branded draft for another company or purpose, ready
to show in a pitch or a class, with nothing of the original owner left in it.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Done, 24 Nov 2026 | Not started | None yet |

**Think of it as:** a show home. The same rooms, wiring and lighting, dressed in the buyer's colours
and furniture so they can picture living there. The sign at the door says "show home", and nothing
of the last family is left in the drawers.

## Overview

Bradley's own site, Bradley Academy, is a cinematic React site he owns. When he pitches a company or
teaches a class, he does not want to show his own site as the example; he wants the same craft
dressed for that company or that course. Today that means hours of find and replace, and the risk
of a leftover name, photo, testimonial or analytics ID. This tool takes a site you own, a short brand
brief and the facts for the new audience, and returns a branded draft, a map of what changed, a
check that nothing of the original owner remains, and a clear "concept" label when the brand
belongs to someone you are pitching.

## Who it is for

A consultant, agency, founder or instructor who reuses one good site as the base for pitches,
client concepts and course examples.

## Use cases from the request

| The person says | They get |
| --- | --- |
| "Brand my site for a company I am pitching" | A concept draft in the prospect's colours and type, with their name used only to say who it is for, every claim from the brief or marked `[needs: ...]`, and "Concept prepared for ..." on the page |
| "Make a teaching version, not about me" | The same site for an invented or course brand, my name and proof removed, the lesson's own content in |
| "Make a white-label version for my agency's clients" | A neutral base with the brand in one file, ready for the next client |

## Scope

- **In (Level 1):** one page of a site you own (its HTML, or the content file for a React site like
  Bradley Academy), a brand brief (colours, type and voice, given by you; a logo file only if the
  owner of the brand gave it to you or you have the right to use it), the audience and purpose
  (pitch, course, white label), and the facts to put in. Out come four parts:
  1. **Brand kit card:** colour roles with contrast ratios, a type pairing from licensed or open
     fonts, voice notes.
  2. **Content map:** every section of the page marked keep, swap, remove or `[needs: ...]`.
  3. **The draft:** the rebranded page as one HTML file (or the changed content file for a React
     site), with a visible concept label when the brand is someone else's.
  4. **Removal check:** every trace of the original owner that was taken out or is still there:
     names, photos, testimonials, numbers, credentials, links, contact details, analytics and
     verification IDs, metadata and structured data.
- **Out:** sites you do not own (that is [Inspiration to draft](../inspiration-to-draft/README.md));
  using another company's logo beyond identifying them; invented testimonials, clients, numbers or
  awards; publishing or sending; Level 1 changes to hosting or domains.
- **It works when:** given the Bradley Academy home page content and a brief for an invented dental
  group being pitched (two colours, a serif and a sans, three facts, a reader who is the practice
  manager), the draft carries the dental group's colours and words, says "Concept prepared for"
  the invented group, keeps none of Bradley's name, credentials, photos, numbers or LinkedIn link,
  marks the missing proof `[needs: patient numbers]` rather than inventing it, has text contrast of
  at least 4.5 to 1, and lists every removed item. Asked to "add a few testimonials to make it
  convincing", it declines and adds a `[needs: real testimonial, with permission]` slot.

## The usable result (U1 to U5)

| ID | Line | Check |
| --- | --- | --- |
| U1 | A consultant, agency, founder or instructor with a site they own | The example and tests use that person |
| U2 | A page or content file they own, a brand brief, the audience and purpose, the facts | A test with no audience must ask once |
| U3 | Brand kit card, content map, draft, removal check | Every test reply has all four |
| U4 | Shown to the prospect, it looks made for them, carries no trace of the original owner, and makes no claim the brief does not support | A string search for the original owner's name, links and IDs finds nothing; every claim traces to the brief |
| U5 | A request for invented proof, a logo used as decoration, or a brand colour that fails contrast | Declines the proof, keeps the logo to identification, adjusts the colour and says so |

## What might be involved at each level

| Level | What it involves | Complexity |
| --- | --- | --- |
| Base | `SKILL.md`, a brand brief template, a removal checklist, and one invented worked example | |
| Level 1, Beginner | Paste one prompt with the link to the skill, your page's HTML (or a section of it), and a short brief: who it is for, their colours and type if you know them, and the facts to say. Read the content map and the removal check first, then open the draft on your phone. Search the draft for your own name and links before you show it | Beginner |
| Level 2, Advanced: brand packs for a React site | For the Bradley Academy site and sites built from [Build your own site](../../../projects/site-studio/base/BUILD-YOUR-OWN-SITE.md). The words already live in `app/content/`; the colours and type are tokens in `app/styles/site.css`. Level 2 adds a brand pack per audience (a content folder and a token file in the W3C format) and a private preview through [Site Studio](../../../projects/site-studio/). First job: 73 brand colour values in `site.css` are written out in full rather than through the tokens (counted on 24 November 2026), so a new palette would not reach them yet | Intermediate |
| Level 3, Expert | A script builds a branded preview from a brand pack and fails if any trace of the original owner remains (names, links, image files, analytics IDs). Optional brand reading from the prospect's public site with Dembrandt, the Firecrawl branding format or Brandfetch, used as a starting point the person confirms. A person approves every preview before it is shared | Advanced |
| Explainer | The README: one site, two brands side by side, what is always removed | Part of every delivery |
| Commercial grade | Many brands on one codebase, client approval of each concept, a licence record for every font and image, and expiry of preview links | Explained, not built here |

## Established best practices

1. **Keep the brand in tokens, not in the code.** The W3C Design Tokens format reached its first
   stable version, 2025.10, so one site can carry many brands from one token file that design and
   code tools share. [Design Tokens Community Group, 28 October 2025](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/).
   Checked 24 Nov 2026.
2. **Use another company's mark only to name them.** In US law, nominative fair use lets you use a
   mark to identify its owner, but the defence fails where the use suggests sponsorship or
   endorsement. So the concept label names who it is for and claims no relationship.
   [Ninth Circuit model jury instruction 15.26](https://www.ce9.uscourts.gov/jury-instructions/civil/chapter-15/15-26-defenses-nominative-fair-use/);
   [Nolo](https://www.nolo.com/legal-encyclopedia/when-you-need-permission-use-trademarks.html).
   Checked 24 Nov 2026. Not legal advice.
3. **Logos: to refer, not to decorate.** Brandfetch's guidance allows a logo to refer to a brand, in
   commentary or in education, but not on your own products. In a concept, the prospect's logo
   appears only where it identifies them, unaltered.
   [Brandfetch, logo fair use](https://docs.brandfetch.com/guides/logo-fair-use). Checked 24 Nov 2026.
4. **No invented proof.** The US Federal Trade Commission's rule on reviews and testimonials, in
   force since 21 October 2024, prohibits testimonials that misrepresent who gave them or their
   experience, including AI-generated ones. A rebrand removes the original owner's proof and leaves
   a `[needs: ...]` slot. [Federal Register, 22 August 2024](https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials);
   [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials).
   Checked 24 Nov 2026.
5. **Check contrast for every new colour.** Body text needs a contrast of at least 4.5 to 1 against
   its background (WCAG 2.2, success criterion 1.4.3), so a prospect's brand colour may need a
   darker or lighter step for text. [W3C, WCAG 2.2](https://www.w3.org/TR/WCAG22/#contrast-minimum).
   A standard, not rechecked today.
6. **Fonts come with their own licence.** A font from one site cannot be carried to another;
   Adobe Fonts, for example, does not allow its files to be self-hosted. Use open fonts or ones the
   new brand licenses. [Adobe](https://helpx.adobe.com/fonts/web/font-licensing/webfont-licensing.html).
   Checked 24 Nov 2026.

## What it reuses

- **Site Studio's [Build your own site](../../../projects/site-studio/base/BUILD-YOUR-OWN-SITE.md)**
  guide, which already turns a copy of Bradley Academy into someone else's site; this tool makes
  that repeatable per audience and adds the removal check and the concept label.
- **Artifact Studio's** rule for building a palette from one brand colour, with contrast listed.
- **Tone Studio** for the voice of the new audience, and **Website audit** to score the draft.
- **The Bradley Academy site's split** of words (`app/content/`) from looks (`app/styles/`).

**Overlap checked.** Build your own site is a one-time move into your own site; this is a
repeatable reskin of a site you keep. [Inspiration to draft](../inspiration-to-draft/README.md)
brings an outside idea in; this sends your own site out in another brand. Both refuse to copy
anything that belongs to someone else.

## Decisions to record during research

- [x] **Reuse check:** brand extraction tools read colours and type, and Claude Design imports a
      design system, but none produces a removal check or a concept label for a site you own. Wrap.
- [x] **Build or license:** Level 1 builds one `SKILL.md` and two templates. Nothing to license.
- [x] **Dependencies and pricing:** any chat assistant. Nothing else at Level 1.
- [x] **Where it lives:** the person's chatbot at Level 1; the site's repository at Level 2.
- [ ] **The name:** "Rebrand a site" is a working name. Open for the owner.
- [ ] **Level 2 token clean-up on Bradley Academy:** a change to the live site's CSS, so the owner
      approves it first.

## Steps 3 to 6, in one line each

- **3, outside help:** nothing to buy for Levels 1 and 2. Level 3 may use a free CLI or a paid brand
  API; choose when Level 3 is built.
- **4, cost:** nothing new at Level 1.
- **5, simplest design:** `SKILL.md`, `template/brand-brief.md`, `template/removal-check.md`, one
  worked example. A string search script only at Level 3.
- **6, plan and front door:** this page; the README's first screen is one site in two brands side by
  side, and the four parts.

## For the owner: the gates that need you

1. **Two projects or one?** Recommended: two, as in the [other plan](../inspiration-to-draft/README.md).
2. **The worked example:** Bradley Academy as the site you own, rebranded for an invented company.
   The prospect must be invented, by the repository's rules.
3. **Level 2 on the live site:** moving the hard-coded colours into tokens touches the deployed
   Bradley Academy CSS. Approve before it is done.

## Open questions

- Can a chat assistant handle a whole React content file at Level 1, or only one page's HTML? To be
  tested with `brand.ts` and `site.ts`.
- Where should a pitch concept live so the prospect can open it but the public cannot find it: a
  private artifact link, a Vercel preview, or a password? Site Studio's guides do not cover this yet.
- How should images be handled: placeholders only, the prospect's own supplied photos, or
  generated images labelled as such?
- Laws differ by country; the practices above cite US and Canadian sources. A short legal check
  before commercial use is advisable.
