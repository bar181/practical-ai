# Plan: Inspiration to draft

Written on 24 November 2026 by following [Agentic Process](../../../projects/agentic-process/),
steps 1 to 6, with the plan template. Step 2 was searched on the web on that date:
[the landscape review](LANDSCAPE.md). **Not yet approved by the owner;** the gates that need him are
at the end. This is one of two plans from one request. The other is
[Rebrand a site](../rebrand-a-site/README.md).

One-line promise: point at something you admire and at your own page, deck or app, and get a draft
of yours that uses the idea, in your words and your brand, never a copy.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Done, 24 Nov 2026 | Not started | None yet |

**Think of it as:** a chef who eats at a great restaurant, writes down why the dish works (the
balance, the order of the courses, the surprise at the end), and then cooks her own dish from her
own pantry. She never walks out with the recipe card or the plates.

## Overview

People see a website, a sales deck, an app screen or even a way of running a meeting and think "I
want ours to feel like that". Today the choice is to describe it badly to a chatbot, or to use a
cloning tool that copies the whole thing, words, pictures and code included. This tool sits in
between. It names the idea behind what the person likes, in their own words, checks that it suits
their reader, rebuilds it from scratch with their content and brand, and lists exactly what was
borrowed (ideas) and what was not (text, images, logos, fonts, code). A reengineering project, toned
down to the part that is useful and safe.

## Who it is for

Anyone with a page, deck or screen of their own who has seen something they want theirs to feel
like: a small business owner, a marketer, a presenter, a front-end developer.

## Use cases from the request

| The person says | They get |
| --- | --- |
| "Here is my website, and here is a site I love. Make mine feel like that" | Pattern cards for what they love, the ones that fit, and their page as one HTML file |
| "I like this one section of their site. Put my content in something like it" | One section, rebuilt from scratch around their content, as an HTML file to paste in |
| "Here is my sales deck, and this keynote's story" | The story order and slide rhythm as a card; their deck outline (or slides through Artifact Studio) in that order, with their facts |
| "My site is on a website builder. I saw a cinematic scrolling story elsewhere" | The effect named, the nearest version the builder can run (its own scroll effects, or an embed block), and the full version as HTML for a builder that takes custom code |
| "Here is a process I admire" (an onboarding flow, a checkout, a meeting format) | The steps and why they work as a card; their own version as a checklist or flow |
| A developer: "Build me this one interaction as a component" | Level 3: a proof of concept of one component on their stack, never a site clone |

## Scope

- **In (Level 1):** one thing of the person's own (pasted HTML, a deck outline, screenshots, or a
  description) and one to three inspirations (a link, a screenshot, a description of motion, or a
  description of a process), plus who reads it and what it must get them to do. Out come four parts:
  1. **Pattern cards,** one per inspiration: what works, in the person's own words, through four
     lenses: structure (the order of parts), visual system (type scale, colour roles, spacing
     rhythm, described rather than copied as values), motion and interaction (what moves, when,
     and why), and messaging moves (the kind of hook, the kind of proof, the shape of the ask).
     Each lens says why it works for that site's reader.
  2. **Fit check:** which patterns suit the person's reader and job, which do not, and why.
  3. **The draft:** their page or section as one self-contained HTML file, or a deck outline, built
     fresh from their content and brand, phone first, readable with motion off.
  4. **Originality note:** the ideas borrowed, and a list confirming that no text, image, logo,
     icon, font file or code came from the inspiration; what makes the draft look like theirs.
- **Out:** copying a page or a whole site; taking words, pictures, logos, icons, font files or code;
  anything a visitor could mistake for the other brand; pages behind a sign-in; publishing.
- **It works when:** given an invented bakery's plain "About us" page in HTML and a description of
  a scroll story on an invented furniture maker's site (a pinned photo, text panels that change as
  you scroll, one large number per panel), the reply names those three patterns, says the large
  numbers fit only if the bakery has real numbers (and asks for them), and returns the bakery's
  page with its own words, `[needs: photo]` placeholders, a different palette and type, and a
  version that reads in order with motion off. No sentence from the inspiration appears in the
  draft. When asked to "make it exactly like theirs", it declines that part in one line and offers
  the closest original route.

## The usable result (U1 to U5)

| ID | Line | Check |
| --- | --- | --- |
| U1 | A person with a page, deck or screen of their own and something they admire | The try-it example and tests use that person |
| U2 | Their own thing, one to three inspirations, the reader and the job | A test with no reader named must ask once |
| U3 | Pattern cards, a fit check, the draft, an originality note | Every test reply has all four |
| U4 | The draft is clearly theirs, works on a phone and with motion off, and they can say in one line what they borrowed | A reviewer shown both cannot mistake one brand for the other; no shared sentence |
| U5 | A request to copy exactly, a logo or character in the inspiration, or a builder that cannot run the effect | Declines the copy, leaves the logo out, offers the nearest version the platform runs |

## What might be involved at each level

| Level | What it involves | Complexity |
| --- | --- | --- |
| Base | `SKILL.md`, a pattern card template, an originality checklist, and one invented worked example | |
| Level 1, Beginner | Paste one prompt with the link to the skill, your page (or deck outline), and a link or screenshot of what you admire, with a line on who reads yours. If the chatbot cannot browse, paste screenshots or describe the inspiration. Read the pattern cards and the fit check first, then open the draft on your phone. Check the originality note and look at both side by side | Beginner |
| Level 2, Advanced | The skill saved in Claude, a ChatGPT Project or a Gemini Gem, with your brand file (colours, type, voice) and a pattern library: your saved cards, a swipe file you can reuse. The draft hands on to [Artifact Studio](../../../projects/artifact-studio/) for the look, [Web Sections](../../../projects/web-sections/) for the structure and [Tone Studio](../../../projects/tone-studio/) for the words. Claude Design or Google Stitch can be the canvas | Intermediate |
| Level 3, Expert: a component, not a clone | For developers. A coding agent with a browser captures the inspiration for analysis only (screenshots, a short recording, computed styles, tokens read with Dembrandt as reference), writes a component spec in its own words, and builds one component (a pinned scroll story, a view transition, a hover effect) from scratch on the person's stack with their tokens. Checks: no asset or font file fetched into the repository, no copied blocks reported by jscpd against the captured source, robots.txt and the site's terms respected, a person approves the merge | Advanced |
| Explainer | The README: before and after, the four parts, what it never copies | Part of every delivery |
| Commercial grade | A team pattern library, font and media licence checks, a visual likeness check before release, an audit trail of what was borrowed, and a legal review step | Explained, not built here |

## How Level 3 reduces the reengineering tools

The cloning repositories in the [landscape review](LANDSCAPE.md) were read, not run. Their stages
are kept or dropped like this:

| Stage in a cloning pipeline | Here |
| --- | --- |
| Reconnaissance: open the site, capture screens and styles | Kept, read only, for one section, respecting robots.txt and terms |
| Foundation: copy fonts, colours, global styles and assets | Dropped. The person's own tokens and licensed fonts are the foundation |
| Component specs | Kept, written in our own words from the pattern card |
| Parallel build of every page | Reduced to one component, a proof of concept |
| Assembly and visual QA against the original | Changed: QA against the person's own design, plus a check that it does not match the original |

## Established best practices

1. **Borrow the idea; express it your own way.** US copyright law excludes "any idea, procedure,
   process, system, method of operation, concept, principle, or discovery", and the Copyright Office
   will not generally accept a claim in "format" or "layout". In Canada, "copyright only protects
   the expression of an idea, not ideas by themselves". So the card records the idea; the draft is
   new expression. [US Copyright Office, Circular 33](https://www.copyright.gov/circs/circ33.pdf);
   [CIPO, Copyright: learn the basics](https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/node/928).
   Checked 24 Nov 2026. Not legal advice.
2. **Keep the overall look and feel distinct.** Courts have allowed trade dress claims for the
   overall "look and feel" of a website when visitors could be confused about who is behind it, so
   copying no single file is not enough. The draft keeps the person's own palette, type and marks.
   [Nolo, What is trade dress](https://www.nolo.com/legal-encyclopedia/what-trade-dress.html);
   [Fish & Richardson](https://www.fr.com/news-insights/articles/website-owners-may-allege-protectable-trade-dress-website-design/).
   Checked 24 Nov 2026.
3. **Study structure, not words.** The copywriter's swipe file is for taking concepts (headlines,
   layouts, offers) and applying them in your own copy; Bly's word is "apply", and he warns against
   swiping copy word for word. The pattern card is
   a swipe file entry in words. [Robert W. Bly, Writer's Digest](https://writersdigest.com/getting-published/what-is-a-swipe-file-for-copywriters-and-content-writers).
   Checked 24 Nov 2026.
4. **Judge a pattern by how it serves the reader.** A competitive evaluation looks at how others
   solve the same design problem, what works and what does not; it is not a style survey. Hence
   the fit check. [Nielsen Norman Group, Competitive usability evaluations](https://www.nngroup.com/articles/competitive-usability-evaluations/).
   Checked 24 Nov 2026.
5. **Never reuse font files or media.** Font licences restrict hosting; Adobe Fonts, for example,
   does not allow self-hosting its font files. Use the person's licensed or open fonts and their
   own images. [Adobe, Web fonts from Adobe Fonts](https://helpx.adobe.com/fonts/web/font-licensing/webfont-licensing.html).
   Checked 24 Nov 2026.
6. **Build motion as an addition.** Scroll-driven animations work in Chrome, Edge and Safari 26 but
   not in Firefox, so the cinematic draft reads in order without them and respects reduced motion.
   [Can I use: scroll-driven animations](https://caniuse.com/wf-scroll-driven-animations).
   Checked 24 Nov 2026.
7. **For automated capture (Level 3): respect robots.txt and the site's terms.** Check the rules
   before any capture and pace requests. [AWS, best practices for ethical web crawlers](https://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/best-practices.html).
   Checked 24 Nov 2026.

## What it reuses

- **Artifact Studio's rule** "record the idea and never the thing", its voices, looks and build
  rules for the HTML draft, and its checklist. This tool adds the method in front of it.
- **Web Sections** for the order of sections, and **Tone Studio** for the words, at Level 2.
- **The chat assistant's own vision and browsing** to read the inspiration at Level 1.
- **Design tokens in the W3C format** ([DTCG 2025.10](https://www.designtokens.org/tr/2025.10/))
  for the brand file at Level 2 and 3.
- **Dembrandt and jscpd** as read-only helpers at Level 3, after a licence and security read.

**Overlap checked.** Artifact Studio builds a designed page from your content; this tool decides
which borrowed idea to build and proves nothing was copied, then can hand off to it. Website audit
scores a site; it does not draw on another one. [Rebrand a site](../rebrand-a-site/README.md)
reskins a site you already own for another brand; this tool brings an outside idea into your own
work. They share the rule "nothing of someone else's is copied".

## Decisions to record during research

- [x] **Reuse check:** cloning tools copy too much; design tools do not explain or prove
      originality; nothing covers messaging or process. Wrap, as above.
- [x] **Build or license:** Level 1 builds one `SKILL.md` and two small templates. Nothing to license.
- [x] **Dependencies and pricing:** any chat assistant that reads images. Browsing is optional.
- [x] **Where it lives:** the person's chatbot. Nothing is stored at Level 1.
- [ ] **The name:** "Inspiration to draft" is a working name. Open for the owner.
- [ ] **One project or two:** recommended two (see the gates).

## Steps 3 to 6, in one line each

- **3, outside help:** nothing to buy for Levels 1 and 2. Level 3 may use a free CLI or a paid
  extraction API; choose when Level 3 is built.
- **4, cost:** nothing new at Level 1.
- **5, simplest design:** `SKILL.md`, `template/pattern-card.md`, `template/originality-check.md`,
  one worked example. No script at Level 1.
- **6, plan and front door:** this page; the README's first screen is a before and after picture,
  the four parts, and the line "the idea, never the thing".

## For the owner: the gates that need you

1. **Two projects or one?** Recommended: two. This one (bring an outside idea into your own work)
   and [Rebrand a site](../rebrand-a-site/README.md) (turn your own site into a branded draft for
   another company or purpose). They have different inputs, risks and users, and each stays one job.
2. **Gate 2:** is "pattern card, fit check, draft, originality note" enough on top of Claude Design,
   Stitch and the cloning tools? The author's view is yes: none of them explains or proves what was
   borrowed.
3. **Level 3 scope:** one component per run, read-only capture, no assets. Agree, or set a
   different line.

## Open questions

- How well do chat assistants describe motion from a short screen recording? Not tested.
- What counts as "too close" for a layout? The originality note can show differences, but there is
  no agreed measure for visual likeness. Level 3 could add one; its method is not chosen.
- Which website builders accept custom HTML, and where (a code block, a full page, a header
  script)? To be checked per builder when the Level 1 guide is written.
- Should a messaging-only inspiration (a competitor's headline style) route to Tone Studio instead?
