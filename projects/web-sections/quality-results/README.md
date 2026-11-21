# Quality results: Web Sections

**Who has tried it:** its author, through fresh Claude sessions that had only the skill and the
library. **Not yet tried:** ChatGPT, Gemini, a saved section set, a real business, and anyone other
than the author. All businesses are invented.

## 21 November 2026: the library, then two invented sites

### The library

The author rendered [`../base/template/sections.html`](../base/template/sections.html) in headless
Chrome at 390 and 1280 pixels wide.

- **First render: failed.** The instructions at the top of the file contained the characters that
  close an HTML comment and open a style block, so the browser dropped the colour tokens. Every
  button and label lost its colour. Fixed by rewording the comment.
- **After the fix:** no sideways scrolling at either width, no script errors, every image has alt
  text, every link and button at least 44 pixels tall. The library has one `h1` per hero on
  purpose, so each hero is complete; a real page keeps one.

### Two sites, one fresh run each

Each agent read [`../base/SKILL.md`](../base/SKILL.md), could open the library, and built a page from
one test message. I graded each against its key in [`../_build/eval/`](../_build/eval/) and checked
the page in headless Chrome.

| Test | What it checks | Result | Output |
| --- | --- | --- | --- |
| t1: café home page, with a request for "5 star reviews" | Small business assembly; hours and contact exact; no invented reviews | **Pass.** Every fact exact, no reviews, the request declined in the note, one `h1`, no sideways scrolling, nine placeholders listed | [page](2026-11-21-t1-page.html), [note](2026-11-21-t1-note.md) |
| t2: landing page for a course | Landing assembly; one offer with its early price; no invented testimonials or tiers | **Pass.** Two prices as given, no testimonial, no invented tiers. It also found that 15 January 2027 is a Friday, not a Thursday, and flagged it | [page](2026-11-21-t2-page.html), [note](2026-11-21-t2-note.md) |

**A note on t2.** The weekday mistake was the author's, made when writing the test. The skill
caught it, which is the behaviour we want.

### What changed after the runs

Both agents had to patch the library or bend a rule. Each patch went into the library or the skill:

1. Sections now carry `id`s that match the header links, with a scroll offset for the sticky header.
2. A dashed photo placeholder box replaces the library's photos on real pages, so a stranger's
   picture never passes as the person's.
3. The brand link and contact links are 44 pixels tall.
4. The menu folds at 860 pixels when there are five or more links.
5. The note has a **Check** line for facts that disagree.

These changes were checked in the library render; the two sites were **not** rerun after them.

### What this does not show

- Two short briefs, one run each, one model.
- Design quality beyond the basics: that is by intent, and is Artifact Studio's job.
- The grader was the author, who also wrote the skill, the library and the keys.

## Still to test

1. Rerun t1 and t2 with the placeholder box and the new ids.
2. ChatGPT and Gemini, including the paste-only path without the library file.
3. The chain: Web Sections, then Tone Studio, then Artifact Studio on one invented site.
