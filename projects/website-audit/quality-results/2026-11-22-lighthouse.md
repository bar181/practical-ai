# Lighthouse before and after the fixes

Run by Claude on 22 November 2026 with Lighthouse 12.8.2, mobile emulation with its standard simulated
slow connection, one run per page. Both builds were served from the same machine with compression,
as GitHub Pages serves them: "before" is commit fa6b289, "after" is the commit that adds this file.
These are lab figures. Real-user figures need the live site in PageSpeed Insights. One run can move
a few points, so a change of 3 or less is noise.

| Page | Build | Performance | Accessibility | Best practices | SEO | First paint | Largest paint | Layout shift | Blocking time | KB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Home | Before | 88 | 100 | 100 | 100 | 2.6 s | 3.4 s | 0.035 | 20 ms | 667 |
| Home | After | 91 | 100 | 100 | 100 | 2.4 s | 3.1 s | 0.001 | 0 ms | 409 |
| Research | Before | 94 | 100 | 100 | 100 | 2.5 s | 2.5 s | 0.001 | 30 ms | 275 |
| Research | After | 94 | 100 | 100 | 100 | 2.4 s | 2.5 s | 0.001 | 0 ms | 230 |
| Practical AI (/tools) | Before | 87 | 100 | 100 | 100 | 2.7 s | 3.5 s | 0.001 | 30 ms | 528 |
| Practical AI (/tools) | After | 90 | 100 | 100 | 100 | 2.5 s | 3.1 s | 0.017 | 10 ms | 389 |

On the home page, about 75% of the largest-paint time is the photo waiting to be drawn (render
delay), not downloading: the stylesheet and fonts come first. That is fix 3 in the
[worked example](../base/examples/bradley-academy-audit.md).
