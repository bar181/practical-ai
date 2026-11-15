# Student guide: publishing a website

You have a page. This guide gets it in front of the right people, and only them.

**Think of it as** hanging a picture. Decide which wall first. A private wall, a gallery wall and
a billboard are different decisions.

## Before any route: the pre-publish check

Publishing is the one step that is hard to undo, because a link can be copied. Run
[`level-simple/pre-publish-check.md`](level-simple/pre-publish-check.md) first. It takes five
minutes. The demo page lets you tick through it.

The three questions that matter most:

1. **Is anything on the page private?** Names, prices, addresses, client material, anything inside
   an embedded image.
2. **Is every fact on it true?** Open the page on your phone and read it as a stranger would.
3. **Who should be able to open it?** Named people, anyone with the link, or everyone.

## Level 1, beginner: share the link

**Time:** minutes. **You will have:** a link you can send.

1. Build the page as an artifact in your assistant. Claude and ChatGPT can both do this.
2. Use the assistant's share control on that page. Choose who can open it. Start with the
   narrowest choice that works.
3. Open the link in a private browser window, signed out. That shows what other people see.
4. Send it. Note where you sent it, so you can take it down later.

**Limits of this route:** the address belongs to the assistant, not to you. Some pages need the
viewer to sign in. If you delete the conversation or the page, the link may stop working.

## Level 2, advanced: upload it to a host

**Time:** about 15 minutes. **You will have:** a public address, and your own domain if you want.

1. Ask the assistant for the page as one HTML file, or a folder with `index.html` at the top.
2. Open the file on your own computer first. If it works from a folder, it will work on a host.
3. Create a free account with a static host. Several let you drag a folder into the browser.
4. Upload. You get an address on the host's domain.
5. Optional: connect a domain you own. The host issues the security certificate.
6. To change the page, upload the new file. To take it down, delete the project.

Which host: see [`landscape-review.md`](landscape-review.md). It lists what each offers and was
checked on the date shown there. Free plans change. Read the host's own page before you rely on a
limit.

## Level 3, expert: a repository that deploys itself

**Time:** an hour, once. **You will have:** a site that updates when a change is approved.

1. Put the page in a repository. Public if the source can be seen, private if not.
2. Connect the repository to a host. Each approved change to the main branch goes live.
3. Changes that are still being reviewed get their own preview address.
4. Protect the main branch, so nothing goes live without a person approving it.

A private repository does not make the site private. On most hosts the published site is public
unless you add sign-in.

## Taking it down

Know this before you publish, not after.

| Route | How to take it down |
| --- | --- |
| Shared link | Turn off sharing on the page, or delete it |
| Host upload | Delete the project in the host's dashboard |
| Repository | Disconnect the host, or delete the deployment |

Taking a page down does not recall copies people have saved.

## Open slots in this draft

- None of the routes has been walked end to end for this draft. The first student to do one
  should record the exact steps and what surprised them.
- Which route suits a page for one private client is not settled.
