# Level 3: build on a platform, with a database and sign-in

**The core idea:** when the site has to keep data or know who is signed in, move it to a platform
that runs code, and add a database with login.

**Think of it as** moving from a frame in your hallway to a gallery with a guard at the door. More
to run, so only do it when the site has to remember something or keep someone out.

**Complexity:** advanced. A coding agent does most of the work; you approve each account, key and
publish. Plan a day.

**Status, 22 November 2026:** a plan written from the Cloudflare, Firebase and Supabase
documentation listed under Sources. None of it has been built or tried for this site.

## Do you need Level 3?

| You need | Level 3? |
| --- | --- |
| To show pages, even many, with your own domain | No. Level 2 is enough |
| A contact form | Usually no. Use a form service or a mail link first |
| Visitors to sign in, save things, or see their own data | Yes |
| Server code, for example calling an AI model with a key you keep secret | Yes |

## Choose a platform

| Option | Best for | Watch out for |
| --- | --- | --- |
| **Cloudflare Workers with static assets** | A fast static site today that can grow server code later, in one project | Cloudflare now recommends Workers for new projects; Pages still works but new features land on Workers |
| **Google Cloud: Firebase Hosting** | Static sites deployed with one command, preview links and one-click rollback | Pair with Cloud Run or Cloud Functions for server code; App Hosting is Google's pick for full-stack framework apps |
| **Supabase** (with either host) | A Postgres database, sign-in and file storage, without running a server | Security lives in Row Level Security policies. Get them right before launch |

A common shape: the site on Cloudflare or Firebase, the data and sign-in on Supabase.

## The steps, for a coding agent

Give your agent this page and the site folder. It should stop for your approval at every bold step.

1. **Build the static site first** (Level 2). Everything below adds to it.
2. **Cloudflare:** add a `wrangler.jsonc` that points `assets.directory` at the build folder
   (`build/client` for this site), run `npm run build`, then **you approve** `npx wrangler deploy`.
   Add your domain in the Cloudflare dashboard.
3. **Or Firebase Hosting:** install the Firebase CLI, run `firebase init hosting` with the build
   folder as the public directory, then **you approve** `firebase deploy --only hosting`. Add your
   domain under Hosting in the Firebase console.
4. **Supabase:** **you create** the project. In the browser code use only the **publishable key**.
   Turn on Row Level Security on every table and write a policy for each action; without policies
   the browser can read nothing, which is the safe default. Keep the **secret key** on the server
   only, never in the site's files.
5. **Sign-in:** turn on email sign-in in Supabase Auth, add the site's address to the allowed
   redirect addresses, and test with a second account that it cannot see the first account's data.
6. **Check before launch:** a stranger's account sees nothing private; the secret key appears in no
   file the browser loads; the site still works on a phone.

## Rules

- You create every account and approve every deploy. The agent never holds your passwords.
- The publishable key may be public; the secret key never is.
- Store only the data you need, and say on the site what you keep.

## Sources

Checked 22 November 2026.

- [Workers best practices: use Workers static assets for new projects](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/#use-workers-static-assets-for-new-projects), Cloudflare
- [Your frontend, backend and database, now in one Cloudflare Worker](https://blog.cloudflare.com/full-stack-development-on-cloudflare-workers/), Cloudflare blog
- [Firebase Hosting](https://firebase.google.com/docs/hosting) and its [quickstart](https://firebase.google.com/docs/hosting/quickstart), Firebase
- [Securing your data](https://supabase.com/docs/guides/database/secure-data) and [API keys](https://supabase.com/docs/guides/api/api-keys), Supabase

Part of [Site Studio](../README.md).
