# Publishing a website

Take a page from a chatbot artifact to a hosted site: a shared link first, then a hosting platform, then a repository that deploys itself.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner to advanced | Done: landscape review in the draft | [Drafted](../../drafts/website-publishing/) | [`workshop/drafts/website-publishing/`](../../drafts/website-publishing/) |

**Think of it as:** Moving out of a sketchbook. First you show the page to a friend, then you hang it in a gallery, then you set up a studio that hangs each new piece for you.

## Overview

The path from a page an assistant built to a site anyone can visit, in three steps of rising effort.

## Who it is for

Anyone who has built a page with an assistant and wants it at a real address.

## Scope

- **In:** the Beginner level described below.
- **Out:** the Advanced level and beyond, until the Beginner level is in use.
- **It works when:** to be written before anything is built.

## What might be involved at each level

Level 1 is described in most detail, because it is built first. The later levels are
outlines and will change.

Level 1 is the Beginner level: a student can run it in any chat assistant with nothing installed. Levels 2 and 3 are the Advanced levels, with skills and connectors, for someone who works with agents every day.

| Level | What it involves | Complexity |
| --- | --- | --- |
| Base | One sample page published by each route, with the steps listed. | Beginner |
| Level 1, Beginner: for students | Build the page as an artifact in a chat assistant such as Claude or ChatGPT and share its link. Check it on a phone, check that nothing private is in it, and decide who should have the link. | Beginner |
| Level 2, Advanced: skills and connectors | The `publish-check` skill runs the checklist, then a hosting connection such as Cloudflare puts the page at your own address. | Intermediate |
| Level 3, Expert: automation | Keep the site in a public or private GitHub repository connected to a host such as Vercel, so every approved change publishes itself. | Advanced |
| Commercial grade | Custom domains across environments, access rules, backups, monitoring and a rollback plan. | Explained, not built here |

## Established best practices

Done. See the [landscape review](../../drafts/website-publishing/landscape-review.md) for what already exists, with dated sources.

## What it reuses

Artifact sharing in chat assistants, hosting platforms with agent connections, repository hosting with automatic deployment.

## Decisions to record during research

Follow the [build process](../plans-template/BUILD-PROCESS.md). Tick each as it is settled.

- [ ] **Reuse check:** what is built in, what is open source, and whether to stop here
- [ ] **Build or license:** the lean for each level, with outside providers reviewed but not selected
- [ ] **Dependencies and pricing:** what the Beginner level depends on and what it costs
- [ ] **Where it lives:** which assistant, where the files are kept, what stays manual

## First step

1. Research established best practices. Record each one with a source link and the date checked.
2. Write the Beginner level solution and its overview.

The Advanced level and beyond are planned only after the Beginner level is in use.

## Open questions

- Which route suits a private client page?
- What are the exact steps for each host, checked end to end?
