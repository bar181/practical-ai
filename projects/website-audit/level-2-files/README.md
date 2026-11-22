# Level 2: the basics a business site is expected to have

**The core idea:** once the site is found and fast, add what visitors and owners expect: a way to
get in touch that is saved, and a way to see what works.

**Think of it as** fitting a mailbox and a visitor log to a house that already passed inspection.

**Status, 22 November 2026:** written from Google's and Supabase's documentation, listed under
Sources. Not yet followed by anyone.

A page shared from a chatbot (a Claude artifact, a ChatGPT or Gemini canvas) cannot hold any of
this. Publish it first: [Site Studio, Level 2](../../site-studio/level-2-files/README.md).

## 1. Google Search Console (15 minutes)

1. Open Search Console and add your domain as a property.
2. Verify it with the DNS record it shows you, at your domain provider.
3. Submit your sitemap (`https://your-domain/sitemap.xml`).
4. Use URL Inspection on your home page, then **Test live URL**, to see the page as Google renders it.

**You know it worked when** the sitemap shows "Success" and the home page says "URL is on Google"
within a few days.

## 2. A contact form that saves to a database (1 hour, with a coding agent)

Supabase gives you a database with a free tier. The form writes one row per message; only you can
read them.

1. **You create** a Supabase project.
2. Ask your coding agent for a `contact_messages` table (name, email, message, created time) with
   Row Level Security on, and one policy: anyone may **insert**, nobody may read from the browser.
3. The form uses only the **publishable key**. The secret key never goes in the site.
4. Add spam protection: a hidden field bots fill in (a honeypot), or a challenge such as Cloudflare
   Turnstile.
5. Say under the form what you keep and why, and link a short privacy note.
6. Read messages in the Supabase dashboard, or have the agent add an email alert on each new row.

**You know it worked when** a test message appears in the table, and the browser cannot read the
table back.

## 3. Analytics, with consent where required (30 minutes)

1. Create a Google Analytics 4 property and add its tag to every page, or use a privacy-friendly
   analytics service instead.
2. If any visitors are in the European Economic Area, the UK or Switzerland, add a consent banner
   and Google's consent mode, so analytics storage waits for a yes.
3. Mark your key events: a form sent, a button to your main call to action.

**You know it worked when** your own visit shows in the real-time report.

## 4. Logging what matters (optional)

The same Supabase project can keep a simple events table (page, event, time, no personal data) for
the few actions you care about. Insert-only from the browser, as with the form.

## Then audit again

Run Level 1 again. "Measured" and "Trust and contact" should now score in full.

## Sources

Checked 22 November 2026.

- [URL Inspection tool](https://support.google.com/webmasters/answer/9012289), Search Console Help
- [Consent mode overview](https://developers.google.com/tag-platform/security/concepts/consent-mode), Google
- [Securing your data](https://supabase.com/docs/guides/database/secure-data), Supabase

Part of the [Website audit](../README.md).
