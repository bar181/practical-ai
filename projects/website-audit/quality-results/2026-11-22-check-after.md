<!-- Output of level-3-files/check_site.py on the Bradley Academy build served locally, 22 November 2026, after shortening titles and adding structured data. Unedited. -->

# Website check: http://localhost:8765/practical-ai/

Run 2026-11-22 13:35 by check_site.py. Read-only. Pages fetched without JavaScript, as a crawler first sees them.

## Site files

- **Security:** the site is served without HTTPS.
- No robots.txt at the domain root (404): every crawler may read everything. Fine, but there is nowhere to list the sitemap.
- **Findable:** a robots.txt sits in a sub-folder. Crawlers read robots.txt only at the domain root, so it is ignored. It starts working on your own domain.
- Sitemap: 16 URLs at http://localhost:8765/practical-ai/sitemap.xml.
- llms.txt found: an index for AI agents.
- **Security:** response headers missing: strict-transport-security, content-security-policy, x-content-type-options, referrer-policy, permissions-policy. Some hosts, GitHub Pages among them, cannot set these; a host or CDN that can (Cloudflare, Vercel, Netlify) fixes it.

## Pages

- **Page:** `/practical-ai/`: 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools`: 4 images without width and height (the page may jump as they load); 1 images after the first three are not lazy loaded.
- **Page:** `/practical-ai/about`: 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/web-sections`: 6 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/tone-studio`: 18 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/artifact-studio`: 15 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/site-studio`: 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/document-to-action-brief`: 4 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/meeting-notes-to-actions`: 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/write-in-my-voice`: 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/research-brief`: 4 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/learnings-database`: 6 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/practical-ai-guide`: 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/rare-find`: 7 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/agentic-process`: 6 images without width and height (the page may jump as they load).

16 pages checked. Structured data (JSON-LD) on 2 of them.

## Links

80 distinct links checked.

4 links could not be checked from here (no response, or the site refuses automated checks). Open them in a browser:
- https://agentics.org (no response)
- https://github.com/bar181/aisp-open-core (403)
- https://github.com/bar181/bar-observatory (403)
- https://www.linkedin.com/in/bradaross/ (no response)

## Summary

| Area | Findings |
| --- | --- |
| Findable | 1 |
| Page | 15 |
| Links | 0 |
| Security | 2 |
| Works | 0 |

Next: run PageSpeed Insights (speed and Core Web Vitals), the MDN HTTP Observatory (security headers) and Google Search Console's URL Inspection (what Google indexed), then score the site with the Website audit scorecard.
