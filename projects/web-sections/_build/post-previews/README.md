# Post preview sources

The code behind [`../../base/template/post-previews.html`](../../base/template/post-previews.html):
one file per tab, each a style block, the markup and one script. They moved here from Artifact
Studio on 21 November 2026, when post previews became part of Web Sections.

| File | What it holds |
| --- | --- |
| `02-posts-lib.html` | The shared frame styles and the two behaviours (choose a draft, see more) |
| `86-socials.html` | Three drafts of one post, side by side |
| `87-post-linkedin.html` to `92-post-blog.html` | One platform each: LinkedIn, Instagram, TikTok, Facebook, email, short blog |
| `example-run/` | The recorded run that made the three-drafts example: prompt, page, notes and friction |

**How the page is made.** Web Sections has no build of its own yet. The page is a snapshot made by
Artifact Studio's build (`projects/artifact-studio/_build/build.py`), which wraps views in its page
frame, fonts and photos. To change it, copy these files back into Artifact Studio's
`_build/views/`, build one page with its `build()` function, and copy the result here. A small
build of Web Sections' own is a planned next step.

The example posts are about the Practical AI repository and name its author. Every other name is
invented.
