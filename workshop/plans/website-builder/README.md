# Website builder: the full plan

One-line promise: a real website for your business, made in the chatbot you already use, that
looks designed, works on a phone and lives at an address you control.

| Complexity | Research | Level 1 | Status |
| --- | --- | --- | --- |
| Beginner (level 1) to advanced (level 3) | Done, 19 November 2026 (sources below) | Not started | **Draft plan, waiting for the owner's approval.** It replaces the plan and draft for Publishing a website |

**Think of it as** opening a shop. Level 1 is setting it up yourself with a good shopfitter beside
you: the chatbot builds it, Artifact Studio makes it look designed, and you check it. Level 2 is
the shopfitter's own toolkit, so every new shop is fitted the same way. Level 3 is the lease: the
keys to an address that is yours, with the steps to move in written down for each landlord.

**North Star:** a business owner who has never opened GitHub can make, check and publish a site
they are proud to send a customer to, and update it next month without starting again.

**Dogfood:** the Practical AI site. The project's main worked example is the real site for this
repository, made with the project's own levels: a home page, a get started page, the examples and
one page per tool, for business users who will never open GitHub. It replaces the two plain index
pages that `workshop/tools/build_site.py` writes today, and it publishes through the same GitHub
Pages workflow.

---

## Why this is worth building, and the honest limit

The big chatbots now build and host sites themselves, so this project must not compete with them.

- **Claude** publishes an artifact to a public link that anyone can open without signing in
  ([Claude docs](https://code.claude.com/docs/en/artifacts), checked 19 November 2026).
- **ChatGPT Sites** has been in public beta since 9 July 2026. It builds a site from a prompt,
  hosts it, and can connect a domain you already own
  ([OpenAI help](https://help.openai.com/en/articles/20001339), checked 19 November 2026).
- **Gemini Canvas** makes web pages and apps and shares them by link
  ([Google help](https://support.google.com/gemini/answer/16047321?hl=en), checked 19 November 2026).

What none of them gives you is the part this project adds:

1. **A brief before the build.** Which pages, what each one is for, and the one action each page
   asks for. Most weak sites skip this.
2. **Design that does not look generated.** Artifact Studio's voices, looks and photo effects,
   applied to a whole site rather than one page.
3. **A site, not a page.** Shared navigation, a title and description on every page, links that
   work, and a check at phone width.
4. **Your own address and your own files.** A site hosted inside a chatbot lives on that
   provider's address and in its account. Level 3 moves the same files to a host you choose.

**Stop rule check:** if all you need is one page shared with a few people, the chatbot's own share
button is enough. The Level 1 guide says so first, and this project adds nothing on top of it.

---

## The usable result (U1 to U5)

| | |
| --- | --- |
| **U1, who uses it** | A small-business owner or manager with a chatbot and no web developer. Level 1 must work for a student using ChatGPT with no skills or folders |
| **U2, what they give it** | A short brief: the business, who visits, what visitors should do, and the content they already have (notes, prices, photos). One brief form is provided |
| **U3, what they get** | A finished site in one of three shapes, with a delivery note listing what was assumed and what is missing. At level 3, a live address |
| **U4, what makes it usable** | It opens on a phone. Every page has one job and one main button. Nothing is invented: a missing price or address is marked, not guessed. A person approves before anything is published |
| **U5, the exception it must catch** | Private or unchecked material on a public page: a home address, a draft price, a client's name, a photo with location data. The publish check flags it, and the site is not published until a person decides |

## The three shapes of site (the Level 1 examples)

| Shape | What it is | Good for | Made as |
| --- | --- | --- | --- |
| **One-page site** | One file. The menu jumps to sections on the same page | A local service, an event, a single offer | One artifact, canvas or Site |
| **Multi-page site** | Several pages that share a menu and a footer | A business with services, prices, about and contact | One file per page, then one folder |
| **Showcase page** | One page built around photographs, using Artifact Studio's photo effects: slow pan and zoom, parallax, photo-filled type, before and after | A portfolio, a product launch, a renovation gallery | One artifact, made with the Artifact Studio guide |

All three examples use invented businesses, and each says so.

## What each level holds

A tool has a base, which holds everything, and up to three levels, each holding only what it adds.
The layout and stages are in the [Agentic Process method](../../../projects/agentic-process/base/PROCESS.md).

| Level | What it involves | Complexity |
| --- | --- | --- |
| Base | The Practical AI site, live, and the three example sites, each with the prompt that made it | Beginner |
| Level 1, Beginner: make it in your chatbot | A guide for Claude, ChatGPT and Gemini. Fill in the brief, paste one prompt that points at the guide, and get one of the three shapes back. For a multi-page site the chatbot gives one file per page; you put them in one folder. Check it on your phone, then share it with the chatbot's own button or take the folder to Level 3 | Beginner |
| Level 2, Advanced: the skills | One `website-builder` skill that chains what exists: the brief, Artifact Studio for the design, the site checklist, and `publish-check` before anything leaves your hands. Saved as a skill or a Project so every site is made the same way | Intermediate |
| Level 3, Expert: your own address | Step by step for each route, tried and dated: the chatbot's own hosting, a drag-and-drop host, and GitHub Pages with an automatic workflow, which is how the Practical AI site is published. A custom domain is the last, optional step | Intermediate to advanced |
| Explainer | One step-by-step page made with Artifact Studio: from brief to live site, with screenshots of the Practical AI site being built | Part of every delivery |
| Commercial grade | Forms that store data, sign-in, analytics, backups and a content editor for staff | Explained, not built here |

### Level 3 routes, at a glance

| Route | Steps in short | Address | Your files |
| --- | --- | --- | --- |
| The chatbot's own hosting | Claude: Share. ChatGPT: deploy the Site. Gemini: Share | The provider's address. ChatGPT Sites can use a domain you own | Stay in the chatbot unless you copy them out |
| Drag and drop | Put the files in one folder with `index.html` as the home page, then drop the folder on the host's page | The host's address, or your domain | Yours, in the folder |
| GitHub Pages | Put the folder in a repository, turn on Pages with GitHub Actions as the source, and merge to publish | `name.github.io/repository`, or your domain | Yours, with every version kept |

Netlify Drop publishes a dropped folder with no account, and a site you do not claim is deleted
([Netlify docs](https://docs.netlify.com/start/get-started-with-drop/), checked 19 November 2026).
Sources disagree on how soon: Vercel's comparison says within an hour, an older guide says 24 hours.
The guide will say "claim it straight away" and give the time only after it is tried.

## Established best practices

1. **Give every page a unique, descriptive title and meta description.** Search engines show them,
   and visitors decide from them whether to click.
   [Google Search Central](https://developers.google.com/search/docs/guides/get-started), checked 19 November 2026.
2. **Publish a sitemap.** It tells search engines which pages exist and how they relate.
   [Google Search Central](https://developers.google.com/search/docs/guides/get-started), checked 19 November 2026.
3. **Treat a shared app or page as public.** Anyone with the link can open it, so keep confidential
   material out. [Lead with AI guide to Gemini Canvas](https://www.leadwithai.co/guides/gemini-canvas-vibe-coding), checked 19 November 2026.
4. **Review a version before it goes live.** On ChatGPT Sites every deployment URL is a production
   URL, so save a version and deploy only after you have reviewed it.
   [OpenAI help](https://help.openai.com/en/articles/20001339), checked 19 November 2026.
5. **Publish from an automated workflow when the site changes often.** GitHub Pages can be built
   and deployed by a GitHub Actions workflow, which keeps history and runs checks first.
   [GitHub docs](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site), checked 19 November 2026.
6. **Design at phone width first.** Artifact Studio's build rules already require it: 390 pixels
   wide, 44 pixel tap targets, readable with motion off. Reused, not rewritten.

## What it reuses

| Need | Reused from |
| --- | --- |
| The look, the voices and the photo effects | [Artifact Studio](../../../projects/artifact-studio/): its guide, skill and two master pages |
| The check before anything is shared | [`publish-check`](../../skills/publish-check/) skill in this repository |
| Hosting inside the chatbot | Claude publishing, ChatGPT Sites, Gemini Canvas sharing |
| Hosting at your own address | Drag-and-drop hosts, and GitHub Pages |
| The automatic publishing for the Practical AI site | `.github/workflows/pages.yml` and `workshop/tools/build_site.py`, added with the Artifact Studio master pages |
| How the project is built | [Agentic Process](../../../projects/agentic-process/) |

What is new: the brief form, the site checklist, the Level 1 guide and prompts, the three example
sites, the `website-builder` skill, the step-by-step route guides, and the Practical AI site.

## Build steps, with a definition of done for each

Each step is built with Agentic Process. A person approves before the next step starts.

| Step | What is built | Done when |
| --- | --- | --- |
| 0 | Owner answers the open questions below | Each one has a written answer in this plan |
| 1 | The brief form and the Practical AI site map: the pages, the job of each, the main button on each, and where the content comes from in the repository | The owner approves the site map. No page has more than one main action |
| 2 | Level 1 guide and the three example sites, made from invented briefs | Each example was made by a fresh Claude session from its prompt, in one try or with the tries counted, and is kept unedited with its prompt. Each opens at 390 pixels with no sideways scrolling. The guide is tried in ChatGPT and Gemini, or the README says it has not been |
| 3 | The Practical AI site, made with Level 1 and Artifact Studio from the repository's own READMEs | Every fact on it is found in the repository. Every page has a unique title and description. Every internal link works. A fresh reader agent, briefed as a business owner, scores it 80 or more out of 100 and can say what to do first |
| 4 | Level 3 guides: chatbot hosting, drag and drop, GitHub Pages | The GitHub Pages route is walked end to end: the Practical AI site is live at bar181.github.io/practical-ai after the owner merges. Every other route says tried, with the date, or not tried |
| 5 | Level 2: the `website-builder` skill | A fresh agent with only the skill and the brief rebuilds one example site and runs `publish-check` without being told to |
| 6 | README landing page, explainer, quality results, indexes | `check_links.py` and `check_project.py` pass. The status line says who has and has not tried it |

## Decisions to record

- [x] **Reuse check:** the chatbots build and host; this project adds the brief, the design, the
  site checks and the move to your own address. Done, 19 November 2026.
- [x] **Build or license:** reuse every host; build only the guide, the forms, the skill and the
  examples. No hosting provider is chosen for the user; the routes are compared.
- [ ] **Dependencies and pricing:** Level 1 needs a chatbot account. Free plans may not include
  every feature; ChatGPT Sites is on paid plans only. To check per chatbot during step 2.
- [ ] **Where it lives:** the project in `projects/website-builder/`, and the Practical AI site's
  source as its main worked example. To confirm in step 0.

## Open questions for the owner (step 0)

1. **Where the site's source lives.** Proposed: inside the project, as its main worked example,
   published at the root of bar181.github.io/practical-ai. The alternative is a `site/` folder at
   the repository root.
2. **A custom domain.** Use one you own for the Practical AI site, or stay on the github.io address
   for now?
3. **Pages on the site.** Proposed: Home, Get started, Examples, one page per tool, About. Add
   anything else, for example a course page or a newsletter sign-up? A sign-up form stores data,
   which is commercial grade here.
4. **Voice and look.** Proposed: the practical instructor voice in your style, with one showcase
   section in the visionary voice. Or one voice throughout?
5. **Priority.** Where does this sit against Meeting notes to actions, which was recommended next?
   Steps 1 to 3 give the repository its public front door quickly; steps 4 and 5 can follow.

## What it replaces

The plan and draft for Publishing a website are retired by this plan and deleted; the git history
keeps them. Their landscape review is rechecked above. The `publish-check` skill is kept and
becomes part of Level 2.
