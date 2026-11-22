# Level 2: publish your site, then put it on your own domain

**The core idea:** put your site in a GitHub repository, let a free host publish it at a lasting
address, then point your own domain at it.

**Think of it as** moving from a pin board to a frame in your own hallway. The address stays the
same, it is yours, and it updates every time you save.

**Complexity:** intermediate. About an hour the first time, plus up to a day waiting for a domain to
connect.

**Status, 22 November 2026:** written from the GitHub, Vercel and Vite documentation listed under
Sources. The Bradley Academy site is published this way on GitHub Pages. No person has followed
this page end to end yet.

## Pick your route

| Route | Best for | Cost |
| --- | --- | --- |
| **A. GitHub Pages, upload a file** | One page or a folder of plain files from your chatbot | Free for a public repository |
| **B. GitHub Pages with a build** | A React or Vite site, like Bradley Academy | Free for a public repository |
| **C. Vercel** | The easiest import: connect a repository and it builds itself | Free on the Hobby plan, check its limits |

## A. GitHub Pages: upload a page (15 minutes)

1. **Get the page as a file.** Ask your chatbot: "Give me this page as one complete `index.html`
   file." Save it on your computer as `index.html`.
2. **Create a repository.** Sign in to GitHub, choose **New repository**, name it `my-site`, choose
   **Public**, and create it.
3. **Upload the file.** Choose **Add file**, then **Upload files**, drop in `index.html` and any
   pictures, then **Commit changes**.
4. **Turn on Pages.** Open **Settings**, then **Pages**. Under **Build and deployment**, set
   **Source** to **Deploy from a branch**, choose `main` and `/ (root)`, then **Save**.
5. **Open it.** After a minute, refresh the Pages screen. Your address is shown at the top:
   `https://YOUR-NAME.github.io/my-site/`.

**You know it worked when** the address opens your page on your phone.

To make the address `https://YOUR-NAME.github.io/` with no folder name, name the repository
`YOUR-NAME.github.io` instead.

## B. GitHub Pages with a build: a React site like this one (1 hour)

Follow [Build your own site](../base/BUILD-YOUR-OWN-SITE.md). It copies the Bradley Academy site,
swaps in your words, and adds a workflow so GitHub builds and publishes on every save. A site with a
build step needs this, because the browser cannot run your source files directly.

**The worked example is this repository.** The workflow
[`.github/workflows/pages.yml`](../../../.github/workflows/pages.yml) builds the site with
`npm run build`, adds the other pages with
[`workshop/tools/build_site.py`](../../../workshop/tools/build_site.py), and publishes the result.
The address is set in one place, `site.config.ts` in the site folder.

## C. Vercel: the easiest import (15 minutes)

1. Put the site in a GitHub repository (route A or B, without turning on Pages).
2. Sign in to Vercel with GitHub. Choose **Add New**, then **Project**, and import the repository.
3. Vercel detects Vite and React and fills in the build settings. Accept them and choose **Deploy**.
4. Open the `.vercel.app` address it gives you.

Every push to `main` publishes again, and every other branch gets its own preview address.

On the free Hobby plan you cannot deploy from a private repository inside a GitHub organization.
Make the repository public or deploy from your personal account.

## Your own domain (15 minutes, plus waiting)

Buy the domain from any registrar first. Then:

1. **Add the domain at the host first.** GitHub: **Settings**, **Pages**, **Custom domain**, type
   it, **Save**. Vercel: **Settings**, **Domains**, add it. Adding it at the host first stops
   anyone else claiming your address.
2. **Add the records at your registrar.** Copy the values from the host's screen.

| Host | Your domain (`example.com`) | `www.example.com` |
| --- | --- | --- |
| GitHub Pages | Four A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` | CNAME to `YOUR-NAME.github.io` |
| Vercel | The A record on your project's domain card (often `76.76.21.21`) | The CNAME on your project's domain card |

3. **Wait and check.** Changes can take up to 24 hours. Then turn on **Enforce HTTPS** on GitHub;
   Vercel adds HTTPS itself.
4. **Tell the site its address.** For this site, set the base to `/` and the address to your
   domain in `site.config.ts` (or `SITE_BASE=/` and `SITE_URL=https://your-domain` in the build).

**You know it worked when** `https://example.com` and `https://www.example.com` both open the site
with a padlock.

## Before you share it

- Open every page on your phone. Nothing scrolls sideways.
- Nothing private: no client names you have not cleared, no home address, no draft prices.
- No password or secret key in any file. A public repository is public in full.

## Sources

Checked 22 November 2026.

- [Managing a custom domain for your GitHub Pages site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), GitHub Docs
- [Deploying Git repositories with Vercel](https://vercel.com/docs/git), Vercel
- [Can I use my domain on Vercel with A records?](https://vercel.com/kb/guide/a-record-and-caa-with-vercel), Vercel
- [Deploying a static site](https://vite.dev/guide/static-deploy), Vite

Part of [Site Studio](../README.md).
