<!-- Output of level-3-files/check_site.py on the Bradley Academy build served locally, 22 November 2026, before the fixes. Unedited. -->

# Website check: http://localhost:8765/practical-ai/

Run 2026-11-22 13:33 by check_site.py. Read-only. Pages fetched without JavaScript, as a crawler first sees them.

## Site files

- **Security:** the site is served without HTTPS.
- No robots.txt at the domain root (404): every crawler may read everything. Fine, but there is nowhere to list the sitemap.
- **Findable:** a robots.txt sits in a sub-folder. Crawlers read robots.txt only at the domain root, so it is ignored. It starts working on your own domain.
- Sitemap: 16 URLs at http://localhost:8765/practical-ai/sitemap.xml.
- llms.txt found: an index for AI agents.
- **Security:** response headers missing: strict-transport-security, content-security-policy, x-content-type-options, referrer-policy, permissions-policy. Some hosts, GitHub Pages among them, cannot set these; a host or CDN that can (Cloudflare, Vercel, Netlify) fixes it.

## Pages

- **Page:** `/practical-ai/`: 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/research`: title is 67 characters (search results show about 60).
- **Page:** `/practical-ai/tools`: title is 66 characters (search results show about 60); 4 images without width and height (the page may jump as they load); 1 images after the first three are not lazy loaded.
- **Page:** `/practical-ai/about`: 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/web-sections`: title is 101 characters (search results show about 60); 6 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/tone-studio`: title is 96 characters (search results show about 60); 18 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/artifact-studio`: title is 73 characters (search results show about 60); 15 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/site-studio`: title is 88 characters (search results show about 60); 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/document-to-action-brief`: title is 108 characters (search results show about 60); 4 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/meeting-notes-to-actions`: title is 115 characters (search results show about 60); 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/write-in-my-voice`: title is 105 characters (search results show about 60); 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/research-brief`: title is 132 characters (search results show about 60); 4 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/learnings-database`: title is 73 characters (search results show about 60); 6 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/practical-ai-guide`: title is 134 characters (search results show about 60); 2 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/rare-find`: title is 102 characters (search results show about 60); 7 images without width and height (the page may jump as they load).
- **Page:** `/practical-ai/tools/agentic-process`: title is 100 characters (search results show about 60); 6 images without width and height (the page may jump as they load).

16 pages checked. Structured data (JSON-LD) on 0 of them.

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
| Page | 16 |
| Links | 0 |
| Security | 2 |
| Works | 0 |

Next: run PageSpeed Insights (speed and Core Web Vitals), the MDN HTTP Observatory (security headers) and Google Search Console's URL Inspection (what Google indexed), then score the site with the Website audit scorecard.
