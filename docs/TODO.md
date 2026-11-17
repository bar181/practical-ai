# To-do list

Actions, not tools. The tools are in the one list: [`tool-inventory.md`](tool-inventory.md).

Every tool follows [Agentic Process](../workshop/drafts/agentic-process/): nine steps, a check after
each. Each tool is a useful tool first, with a short explainer. Reuse Anthropic's skills and plugins
where they fit. Nothing is built until its North Star page is approved at stage 3.

## Next, in order

- [ ] Choose the first Beginner tools to build for students. The research points to three that are one pasted instruction and one template each: summarise a document, rewrite in my voice, meeting notes to actions
- [ ] Approve, change or reject each North Star page in the list. Nothing is built before that
- [ ] Decide what to do with the five North Star pages that match no demand (learnings database, task graph, core memory, connections hub, rubric reviewer): keep as Advanced tools for the owner, or park
- [ ] Write a North Star page for "summarise a document", the one researched tool with no page
- [ ] Read the small-business plugin's skills before designing any Advanced level, and record what it already covers

## Agentic Process version 2

Restarted on 16 November 2026. The plan is in [its spec](../workshop/drafts/agentic-process/SPEC.md), section 9.

- [ ] AC-1: run decision support's short check in Claude (the bakery, a different decision, the three behaviours)
- [ ] AC-2: run the same check in a second chatbot
- [ ] AC-3: build the learning system from its plan with the builder skill
- [ ] Owner: answer the spec's two open questions (the plan template, the first Level 3 tool)
- [ ] Later: give Artifact Studio one `SKILL.md` as its source of instructions, in place of `AI-INSTRUCTIONS.md`

Version 1, archived. From [the review from the user's side](reports/2026-11-16-agentic-process-user-review.md):

- [x] Bundle the checks into `level-2-files/` so the skill and template work in any repository
- [x] Generate the coach's and the skill's gate tables from `_build/steps.py`
- [x] Add a short path to the coach for small jobs, and test it with two fresh sessions
- [x] Fold the landscape review's search order into the skill's step 2
- [x] Point the Expert page at the template's starter gates, and add one worked unattended run
- [x] Move the run logs from `level-3-files/fresh-run/runs/` to `_build/runs/`
- [x] Make `base/plan-template.md` the one source of the template's plan
- [x] Re-run the skill with a second agent after these changes
- [x] Add an Expert worked example
- [ ] Owner: add topics, a description, a social picture and GitHub Pages (see the report)
- [ ] Owner: answer the open gates in the Document to action brief plan

## Across all tools

- [ ] Have a student run each Beginner level and record what they could not do
- [ ] Move each older draft in `workshop/drafts/` to the showcase layout in `projects/README.md` when it is next worked on
- [x] Run each worked example's prompt in a fresh chat: done on 16 November 2026, ten of ten, all in Claude
- [ ] Turn on GitHub Pages so the HTML pages open from a link on a phone (GitHub shows HTML files as code)
- [ ] Turn on branch protection for `main`: a pull request and the owner's review before any merge
- [ ] Run the beginner prompt from the artifact studio README in ChatGPT and Gemini, and record what came back
- [ ] Try the artifact studio MCP server inside a desktop assistant
- [ ] Give the artifact studio to one other person for a real job
- [ ] Build the next tool, Document to action brief, with Agentic Process from step 1, and time it
- [ ] Teach each 30-minute lesson once and correct its timings
- [ ] Draft a commercial-grade one-pager for each promoted project

## Waiting on a decision

- [ ] The avatar and voice tools to recommend in the video guides
- [ ] One hosting route confirmed end to end
- [ ] The scoring rubric for the daily builder, before it is scheduled
