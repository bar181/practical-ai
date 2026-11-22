# Plan: Research brief with checked sources

Written on 22 November 2026 by following [Agentic Process](../../../projects/agentic-process/),
steps 1 to 6, with the plan template. Step 2 was searched on the web on that date.
**The owner has not yet answered the gates;** each is marked open where it needs him.

One-line promise: compare your options on one page, and see the exact words behind every claim.

| Complexity | Research | Level 1 | Draft |
| --- | --- | --- | --- |
| Beginner | Done, 22 Nov 2026 | Built: [the project](../../../projects/research-brief/) | None. The earlier [weekly brief draft](../../drafts/weekly-brief/) is a different job (see below) |

**Think of it as:** a fact-checker who sits beside the researcher. Nothing goes into the table
until she has read the line that says it, and anything she could not find is written "not found".

## Overview

Owners and managers already ask their chatbot to compare suppliers, software or venues, and the
deep research modes now return long reports with links. The links are the weak point: studies
find many cited claims are not supported by the page cited. This tool turns a question, the
options and what matters into one comparison table, where every cell carries a source number and
the exact words from that source. Claims with no source, links that say something else, and pages
it could not open are listed first. It compares; the person decides.

## Who it is for

An owner or manager who has to compare two to four options and show someone else why.

## Scope

- **In:** one question; two to four options; up to six things that matter; sources the person
  gives (links, pasted pages, or a report from a deep research mode or a colleague), or sources the
  chatbot finds if it can search. Out comes one page: a count, the flags, the table, the quotes,
  what was not found.
- **Out:** choosing for the person (that is the planned Business decision helper); judging whether
  a source is reputable beyond "maker's own page" and "opinion"; legal, tax or investment advice;
  paywalled pages, which are marked "could not open" and never guessed; a weekly repeat (that is the
  Recurring research brief).
- **It works when:** given an invented AI research summary comparing three oat milk suppliers,
  with the text of the pages it cites, the brief marks the one claim whose page says something
  else, the one claim with no citation, the one "free delivery" that the page limits to orders over
  a sum, and the one page that was never supplied, and quotes the exact words for every claim it
  marks checked. Nothing is invented to fill a gap.

## The usable result (U1 to U5)

| ID | Line | Check |
| --- | --- | --- |
| U1 | An owner or manager comparing two to four options for a choice they must explain to someone | The try-it example and tests use that person |
| U2 | The question, the options, what matters, and sources: links, pasted pages, or a report to check | t3 gives too little and the reply must ask once |
| U3 | One page: a count, flags, a comparison table with a source number in every cell, each source's exact words, and what was not found | t1 and t2 replies have every section, every cell numbered |
| U4 | The reader can find any quoted words on the source page in under a minute, and would forward the page as it is | Every quote in t1 and t2 appears word for word in the supplied pages |
| U5 | A claim with no source, or a source that does not say what the claim says, or a page it could not open | t2 plants all three; t1 plants a criterion no page covers and an instruction inside a page |

## What might be involved at each level

| Level | What it involves | Complexity |
| --- | --- | --- |
| Base | `SKILL.md`, an invented worked example (three salon booking systems) and three test cases with answer keys | |
| Level 1, Beginner | Paste one prompt with the link to the skill, your question, options, what matters, and your links or pasted pages. Or run your chatbot's deep research first and paste its report to be checked. Read the flags first, then open two sources and find the quoted words | Beginner |
| Level 2, Advanced | The skill saved in Claude, or the text in a ChatGPT Project or a Gemini Gem, with your usual criteria and a short list of sources you trust | Beginner to intermediate |
| Level 3, Expert | Not assigned. A connection would not remove recurring work for a one-off comparison. The weekly repeat belongs to the Recurring research brief | None |
| Explainer | The README | Part of every delivery |
| Commercial grade | An automatic re-check of every link before sending, and an archive of past briefs | Explained, not built here |

## Step 2: what already exists, checked 22 November 2026

| Option | Kind | What it covers | Cost | Limits | Source |
| --- | --- | --- | --- | --- | --- |
| Claude Research | Built in | Several searches that build on each other, across the web and connected tools | Paid Claude plans (Pro, Max, Ultra, Team, Enterprise), per the help page | The help page does not say how sources are reported or checked | [Claude help: research](https://support.claude.com/en/articles/11088861-using-the-research-feature) |
| ChatGPT deep research | Built in | A planned, multi-step search ending in a structured report; "All deep research outputs include citations or source links so you can verify the information" | Usage varies by plan and country; price not confirmed here | Says nothing about errors; the reader is left to verify | [OpenAI help: deep research](https://help.openai.com/articles/10500283-deep-research) |
| Gemini Deep Research | Built in | A research plan, then a report in about 5 to 10 minutes, from Google Search and optionally Gmail, Drive or uploads | Free with limits; higher limits on Google AI Pro and Ultra | The help page does not mention citations or checking | [Google help: Deep Research](https://support.google.com/gemini/answer/15719111) |
| Claude API Citations | Built in, for developers | Returns the exact passage (`cited_text`) behind each claim from documents you supply | API pricing; not confirmed here | Documents you supply, not open web pages; needs code | [Claude docs: citations](https://platform.claude.com/docs/en/build-with-claude/citations) |
| GPT Researcher | Open source, Apache-2.0 | An agent that researches the web or local files and writes a report with citations | Free code; needs an OpenAI and a Tavily key | Python install; the page describes no check that a source supports its claim | [github.com/assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) |
| STORM (Stanford) | Open source, MIT | Writes Wikipedia-like articles with citations from internet search | Free code; needs a model and a search API key | Python install; last dated news January 2025 | [github.com/stanford-oval/storm](https://github.com/stanford-oval/storm) |
| Perplexity and other answer engines | Built in | Answers with numbered sources | Not confirmed here | Not reviewed today | General knowledge, not checked |

**What the evidence says about citations.**

- The Tow Center tested eight AI search tools on 1,600 queries: together they "provided incorrect
  answers to more than 60 percent of queries", and more than half of the Gemini and Grok 3
  responses cited fabricated or broken links.
  [Columbia Journalism Review, 6 March 2025](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php).
- DeepTRACE, an audit of deep research systems, found citation accuracy between 40% and 80% across
  systems, with large fractions of statements unsupported by their own listed sources.
  [arXiv 2509.04499, September 2025](https://arxiv.org/abs/2509.04499v1).

**Lean for the Beginner level: wrap.** The built-in research modes already find sources and write
reports. None of the help pages describes checking that each cited page says what the report
claims, and the studies say that check is where they fail. The missing piece is small: one page,
every claim with its exact words, and the failures listed first. The open source tools need code
and keys, and add nothing to that check.

## Established best practices

1. **Trace each claim to its original context.** Follow the claim back to its source to see whether
   it was presented accurately; this is the fourth move of SIFT. [Mike Caulfield, SIFT (The Four
   Moves), 19 June 2019](https://hapgood.us/2019/06/19/sift-the-four-moves/), checked 22 Nov 2026.
2. **Quote the passage, not a summary.** Claude's Citations feature returns the exact passage behind
   each claim "so you can verify answers". The same habit works in any chatbot by asking for the
   quote. [Claude docs](https://platform.claude.com/docs/en/build-with-claude/citations), checked
   22 Nov 2026.
3. **Treat a cited link as unchecked until opened.** The Tow Center and DeepTRACE results above.
   Checked 22 Nov 2026.
4. **Put the bottom line first.** Agreed practice for short briefs, recorded in the
   [weekly brief landscape review](../../drafts/weekly-brief/landscape-review.md), 15 Nov 2026.
5. **Prefer the maker's own page for the maker's facts; label reviews as opinion.** Investigate the
   source, the second SIFT move. Same source as 1.

## What it reuses

The person's own chatbot and its search or deep research mode; the four results from the
[source and link verifier](../source-verifier/README.md) plan (supports, partly, does not support,
could not open), plus "no source"; the bottom-line-first layout from the weekly brief draft; the
"exact words" habit from [Document to action brief](../../../projects/document-to-action-brief/).

**Overlap checked.** The [decision support](../decision-support/README.md) example recommends; this
compares and stops. The source and link verifier checks links in any document; this tool contains
that check for one comparison, so the verifier stays a plan for checking other documents. The
weekly brief draft is a recurring news digest; it stays the starting point for the Recurring
research brief.

## Decisions to record during research

- [x] **Reuse check:** built-in research modes find and cite; none checks support. Wrap them.
- [x] **Build or license:** Level 1 builds one `SKILL.md`. Nothing to license.
- [x] **Dependencies and pricing:** any chatbot. Opening links needs a chatbot that can browse;
      without that, the person pastes page text, and the brief says it did not browse.
- [x] **Where it lives:** the person's chatbot. Nothing is stored. The person shares the page.

## Steps 3 to 6, in one line each

- **3, outside help:** nothing to buy.
- **4, cost:** nothing new.
- **5, simplest design:** one `SKILL.md`. No script: the check is reading, not arithmetic.
- **6, plan and front door:** this page, and the promise above.

## For the owner: the gates that need you

1. **Gate 2:** is "every cell with its exact words, failures first" enough on top of the built-in
   research modes? The author's view is yes, because their reports are the input, not the
   competition.
2. **Gate 7:** read this page, or give it to a new chat with the review prompt from step 7.

## Built: 22 November 2026

- **What was built:** [`projects/research-brief/`](../../../projects/research-brief/): one
  `SKILL.md`, a worked example, three invented test cases with answer keys, and Level 2 steps.
- **Tests:** three invented cases, each run by a fresh Claude subagent with pasted pages and no
  browsing: 3 of 3 passed their keys. One defect (the tool flagged its own shortening of a "from"
  price) was fixed in the skill; the rerun, a second rerun of the report check and the try-it
  example all passed. [The evidence](../../../projects/research-brief/quality-results/README.md).
- **Decisions made in the build:** flags first; every cell numbered to exact words; "partly" only
  for someone else's claim, with the difference written; a review is labelled opinion; no
  recommendation; Level 3 not assigned.
- **Not yet tried:** ChatGPT, Gemini, live web pages, a real decision, and anyone but the author.

## Open questions

- How often do live pages change between the check and the reader opening them? The brief dates
  every check, but no re-check is built.
- Does "partly" stay rare in real use? The skill requires the difference in words to use it.
