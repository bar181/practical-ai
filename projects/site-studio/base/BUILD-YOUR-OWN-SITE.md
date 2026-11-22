# Build your own site on GitHub, step by step

**The core idea:** copy the Bradley Academy site, put your own words and pictures in one folder,
and let GitHub publish it for free every time you save a change.

**Think of it as** moving into a furnished flat. The walls, the wiring and the lights are already
in. You bring your own things, hang your own pictures and put your name on the door. You never
pay rent: GitHub Pages hosts it free for a public repository.

**Status, 20 November 2026:** a fresh AI agent followed an earlier version of this guide for an
invented bakery, built the site and served it at `/my-site/`. It found six gaps; a second run of the revised guide found five smaller ones. All are fixed
here. The publish to GitHub Pages itself has not been tried with this guide, and no person has
followed it yet.

## What you need

| You need | Why |
| --- | --- |
| A GitHub account | The site lives in a repository, and GitHub Pages publishes it |
| Node.js 22.22 or newer on your computer | To run the site while you change it. Not needed if a coding agent does the work |
| About an hour | Most of it is writing your own words |
| Optional: a coding agent such as Claude Code | It can do steps 1 to 6 for you. The prompt is at the end |

## The steps

### 1. Copy the site into a new repository (10 minutes)

1. On GitHub, create a new **public** repository, for example `my-site`.
2. Copy the folder [`examples/bradley-academy/`](examples/bradley-academy/) into it, so `package.json`
   sits at the top of your repository.
3. Delete `node_modules/` and `build/` if you copied them.

### 2. Unhook it from Practical AI (10 minutes)

The Bradley Academy site copies its pictures and prompts out of the Practical AI repository before
each build. Your copy does not have that repository around it, so do this before you run anything.

1. In `package.json`, take `npm run sync && ` off the front of the `dev`, `build` and `typecheck`
   scripts, and delete the `sync` script. Delete `scripts/sync.mjs`.
2. In `.gitignore`, delete the lines `public/media/` and `app/content/generated/`, so your pictures
   and prompts are saved with the site.
3. Empty `public/media/` completely (it holds Bradley's pictures, which would otherwise be published
   with your site), then put your own pictures in it, for example `public/media/photos/hero.jpg`.
4. Create `app/content/generated/prompts.json` with one prompt called `starter` (the home page copy
   button) and one per product, named after the product's slug from step 5, for example
   `{ "starter": "...", "bread-box": "...", "cake-orders": "..." }`.
5. Delete the `.react-router/` folder if you copied it.

### 3. Set the address (2 minutes)

Open `site.config.ts`, the only place the address is set.

- **A project site** (the usual case) lives at `https://YOUR-NAME.github.io/my-site/`: set the base to
  `"/my-site/"` and the address to `"https://YOUR-NAME.github.io/my-site"`.
- **A user site** (a repository named `YOUR-NAME.github.io`) or **your own domain:** set the base to
  `"/"` and the address to your domain.

### 4. Run it on your computer (5 minutes)

```sh
npm install
npm run dev
```

Open the address it prints. The home page shows the old words, and the old product pages show an
error until step 5, because your prompts file has no prompts for them. That is expected.

### 5. Put in your own words and pictures (30 minutes)

Everything a visitor reads is in `app/content/`:

| File | What to change |
| --- | --- |
| `site.ts` | Your brand, your home page words, the `labels` used across pages, and your About page. The About page is a person's story: rewrite it all |
| `slugs.ts` | The short names of your products or services, in the order you want them |
| `tools.ts` | One entry per product. Every field is required: the promise, the core idea, an analogy, the benefits, how it is designed to help, who it is for, three levels, the try-it text, what it does not do, a status and the example tabs. Delete the ten Practical AI entries |
| `images.ts` | One slot per large picture, including one opening scene and one "who it is for" scene per product (`tool-<slug>` and `who-<slug>`). Point each at your picture and write alt text that says what it shows, then run `scripts/make_webp.py` for light copies |

Products without their own line drawing get a simple framed star. To draw your own, add a path
for your slug in `app/components/Glyph.tsx`.

**Write it the way you would explain it to a customer across a table:** the core idea in one
sentence, an everyday comparison, then the detail. Invent nothing: every number and claim should be
one you can stand behind.

Finally, rename the leftovers: the `name` and `description` in `package.json`, and the `README.md`
in your folder.

Run `npm run typecheck`. It names any field you missed.

### 6. Let GitHub publish it (10 minutes)

1. Create the file `.github/workflows/deploy.yml` in your repository with this content. The
   address comes from `site.config.ts`, so there is nothing to change in it.

```yaml
name: Publish the site
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: "22"
          cache: npm
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v5
        with:
          path: build/client
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v5
```

2. In your repository on GitHub, open **Settings**, then **Pages**, and under **Build and
   deployment** set **Source** to **GitHub Actions**.
3. Save your changes to the `main` branch. Open the **Actions** tab and watch the run. When it
   turns green, your site is live at the address from step 3.

### 7. Optional: your own domain (15 minutes, plus waiting for DNS)

1. In **Settings**, **Pages**, add your domain under **Custom domain**, and add the DNS records
   GitHub shows you at your domain provider.
2. In `site.config.ts`, set the base to `"/"` and the address to `https://your-domain`.
3. Save. The next run publishes the site at your domain.

## Before you share it

- Open every page on your phone. Nothing should scroll sideways.
- Click every link and every copy button.
- Read every number and claim once more. If you cannot stand behind it, take it out.
- Nothing private: no home address, draft prices or client names you have not cleared.

## Have a coding agent? Let it do the work

Open your new, empty repository in Claude Code (or another coding agent) and paste:

```
Read https://github.com/bar181/practical-ai/blob/main/projects/site-studio/base/BUILD-YOUR-OWN-SITE.md
and https://github.com/bar181/practical-ai/blob/main/projects/site-studio/AGENTS.md
Then build my site in this repository by following steps 1 to 5, and write the workflow in step 6.
My business: [one line].
My products or services: [a list, one line each].
My pictures: [where they are, or "use placeholders and list each one in your note"].
Invent no facts. Ask me for anything missing in one message.
Stop before anything is published, and show me the site running on your computer first.
```

Built by Bradley Ross. Part of [Site Studio](../README.md).
