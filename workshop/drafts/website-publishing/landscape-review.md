# Publishing a website: landscape review

Where a single page or a small static site can be put, checked on 2026-11-15. Hosting offers
change often. Follow the link and read the host's own page before relying on a limit.

## Summary

- **Sharing a link from the assistant is the simplest route** and needs nothing else.
- **Free static hosting is plentiful.** Several hosts accept a dragged folder with no command line.
- **A repository connected to a host** adds history, previews and automatic publishing.
- **Nothing here was walked end to end.** These are descriptions from the sources listed.

## Hosts

| Host | What the sources say | Source |
| --- | --- | --- |
| Cloudflare Pages | Direct upload is available: in the dashboard, create a Pages application and upload a folder by dragging it in. Free for static sites, with 500 builds a month on the free plan and unlimited static requests | [Setup walkthrough](https://medium.com/@kaklotarrahul79/how-to-host-your-website-for-free-using-cloudflare-pages-cbe764a18811), [free tier limits](https://temps.sh/blog/cloudflare-pages-free-tier-limits-2026) |
| Cloudflare Workers with static assets | A folder of files can be deployed with no server code, using the `wrangler deploy` command and an `assets` directory in the configuration. No drag and drop: it uses the command line or a Git connection. Cloudflare has described a plan to bring Pages and Workers together | [Pages or Workers](https://flaviocopes.com/cloudflare-pages-vs-workers/), [comparison of hosts](https://bootstrap.build/articles/cloudflare-pages-alternatives/), [GitHub Pages or Cloudflare](https://smartscope.blog/en/blog/github-pages-cloudflare-free-hosting/) |
| Cloudflare Drop | Drag a folder or zip into the browser and get a live address, with no account. Meant for showing something quickly, not for a permanent site | [Cloudflare Drop explained](https://flaviocopes.com/cloudflare-drop.md) |
| GitHub Pages | Serves a site straight from a repository. Free for public repositories | [Free hosting guide](https://www.supadrop.host/blog/free-static-website-hosting-guide/) |
| Vercel and Netlify | Publish from a Git push, with a preview for each proposed change. Free tiers exist, with Vercel's listed as personal use | Same guide |

Two sources disagree on detail: one calls the Pages upload command deprecated but working, another
recommends it. Treat the dashboard upload as the stable path for a beginner.

## Not rechecked for this review

From general knowledge:

- How each assistant's share control works, and what a viewer needs in order to open a shared page.
- Whether a site published from a private repository is public. On most hosts it is.
- Agent connections to hosting platforms. An earlier note in this repository records that
  Cloudflare offers connections an agent can use to manage deployments. Not re-verified here.

## Build or license

| Level | Lean | Why |
| --- | --- | --- |
| Simple | Reuse the assistant's own sharing | Nothing to set up |
| Working | Reuse a free static host with dashboard upload | No command line, and your own address |
| Automated | Reuse a repository plus a host's Git connection | History, previews, and approval before anything goes live |

## Still to do

- Walk each route end to end and record the exact steps with screenshots.
- Check current free-plan limits on each host's own pricing page.
- Decide the recommended route for a page meant for one private client.
