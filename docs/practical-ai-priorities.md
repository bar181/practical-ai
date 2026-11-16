# Practical AI · What to build next

*Priorities report for Bradley Ross · 15 November 2026*

## North Star

Practical AI is my public showcase for tools that solve real business problems and projects students can build themselves. In Practical AI for Small Business, a business owner or employee can build a useful first version in one class using their usual chat assistant. For my own work and client projects, I build tools that can apply business rules, use approved sources, remember what worked, and carry a job across multiple steps.

Every showcase project should answer three questions. What job does it do? How can someone try it with fictional data? How can they tell whether it helped? The repository’s build method and Artifact Studio support those projects.

Beginner uses a prompt, a template, and a worked example. Advanced adds repeatable instructions, checks, and connectors where useful. Expert adds persistent storage, a server, or scheduling when the workflow needs it. The two lists reflect different audiences. A project can appear in both when the classroom exercise and the operational tool do distinct jobs.

## 1. Practical AI for business people

These are one-session projects. Learners work from pasted text or sample files and check the output before using it. The order is a proposed teaching sequence based on how quickly a learner can see a result, check it, and take it back to work.

| # | Project | What a learner builds and checks | Starting point |
| --- | --- | --- | --- |
| 1 | **Document to action brief** | Turn a supplier notice or business report into key facts, obligations, dates, and questions. Find each item on the cited page. | New lesson. Reuse the Artifact Studio’s report layout. |
| 2 | **Write and edit in my voice** | Use three writing samples to create a voice guide and revise a real-world email or post. Verify that the commitments and facts stayed accurate. | Extend the Voice Post Drafter draft to everyday writing. |
| 3 | **Meeting notes to actions** | Turn a transcript into decisions, tasks, and a follow-up draft. Flag owners or dates the meeting never established. | Meeting to Actions plan. |
| 4 | **Research brief with checked sources** | Compare three options on one page. Open each source and check that it supports the specific claim. | One-off lesson adapted from the Weekly Brief draft and Source and Link Verifier proposal. |
| 5 | **Inbox triage and draft replies** | Sort a mock inbox into reply today, delegate, and wait. Draft the two most important responses and explain why they come first. | Inbox Daily Summary draft. |
| 6 | **Customer issue resolver** | Use a one-page business policy to handle a delayed order or refund. Give the customer a next step and explain when a manager should step in. | Classroom adaptation of the Website Chatbot and Lead Responder plans. |
| 7 | **Ask your spreadsheet** | Explain what changed in a small sales export, show the rows behind the answer, and reconcile the total. | Extend the Dashboard draft with a question-and-answer exercise. |
| 8 | **Receipts into an expense sheet** | Extract supplier, date, amount, and category. Spot-check against the originals and flag blurry or incomplete receipts. | Expense Form Creator plan. |
| 9 | **Business decision helper** | Compare three suppliers against a weighted rubric. See whether changing one assumption changes the recommendation. | Classroom adaptation of the Decision Support proposal. |
| 10 | **Quote a job** | Use a fictional price sheet and customer request to prepare a first quote. Recalculate the total and flag details needed before it can go out. | Estimator draft. Use as the course capstone. |

Build the first class around 1–3. They cover reading, writing, and turning a conversation into work. Use the same fictional company across exercises so students can carry outputs forward into later projects. Give each learner a finished template and one check they can repeat independently.

## 2. Tools for my work, agents, and clients

The sequence emphasizes repeated use, existing work to build on, and dependencies. Each project has a first proof a person can inspect before more systems are connected.

| # | Project and branch status | First useful version | How I’d know it earned a place |
| --- | --- | --- | --- |
| 1 | **Learnings database** · North Star and earlier draft | Record what happened, the rule to use next time, and the evidence. Retrieve relevant lessons before similar work starts, and record when a lesson was applied. Start with a private sheet and the existing learning-log skill. | Log ten real lessons and verify that one is retrieved and applied in later work. |
| 2 | **Task and dependency graph** · North Star | Turn a goal into a task file and a ready/blocked board. Show what slips when a prerequisite moves, and let agents pick work that is ready. Reuse Artifact Studio for the display. | Change one prerequisite in a real project and verify that the board updates the downstream work correctly. |
| 3 | **Decision support assistant** · North Star | Take a decision from options and assumptions through evidence and a recommendation. Produce a briefing page and next steps. | Use it for one live business decision. A reviewer can trace the main reasons to their sources and identify what would change the answer. |
| 4 | **Commercial estimate to proposal** · Estimator draft and Proposal Builder plan | Start with the commercial pool case. Combine form inputs, salesperson notes, comparable past jobs, and a parts list into a draft estimate and proposal. | Time the draft against the manual baseline and compare scope omissions and pricing corrections on representative examples. |
| 5 | **Recurring research brief** · Earlier draft | Compare this week’s evidence with the previous run. Surface what changed and one useful implication for teaching, consulting, or AISP research. | Run two distinct briefs and verify that each new finding points to a source and has a concrete implication. |
| 6 | **Source and link verifier** · North Star | Check whether cited sources support each claim. Start inside the research and decision workflows with a dated result for each link. | Catch planted dead links and unsupported claims in a test brief. |
| 7 | **Rubric reviewer** · North Star | Have a fresh review session score a proposal, lesson, or demo against a fixed rubric, with evidence for every score. | Score two revisions on the same rubric and verify that the feedback points to real changes a reviewer can find. |
| 8 | **Core memory** · North Star | Retrieve current policies, project facts, and source pointers from a private, structured store. Start with the record format and viewer from the learnings database. | Answer a set of known questions with the right source and current record. Superseded entries stay traceable. |
| 9 | **Connections hub** · North Star | Start with one source. Extract proposed facts, commitments, and lessons into a review queue with links back to the original material. File accepted items into the appropriate store. | Review one week’s batch. Track how many candidates are accepted, corrected, or duplicates. |
| 10 | **Daily builder** · Plan | Run the project method on one small approved backlog item. Produce changes, checks, and a reviewable branch. | Complete one manually triggered run that a maintainer can review end to end. Use that run to decide whether scheduling saves work. |

Build #1 and #2 first. The learnings database helps a new session start with what worked last time. The task graph tells it what can be done next. Use both while building the commercial estimator, so the first client showcase also tests whether the agentic tools help on a real workflow. Core memory and the connections hub can follow once the related record types and retrieval behaviour have been tried.

## Evidence and branch status

**Classroom demand.** Pew found that among U.S. workers who had used chatbots at work, 57% had used them for research, 52% for editing, 47% for drafting, and 40% for summarizing documents or meetings. The Federal Reserve’s 2026 small-business report found writing or marketing and planning or analysis were common uses among AI-using employer firms. These studies support the choice of classroom tasks. The teaching sequence remains a recommendation and has yet to be tested with students. Pew Research Center, p. 19 · Federal Reserve Small Business Credit Survey

**Business impact.** A field study of 5,172 customer-support agents at one firm found 15% more issues resolved per hour on average with AI assistance. For the classroom project, check whether the proposed action complies with the sample policy and resolves the issue. Quarterly Journal of Economics

**Agentic precedents.** Anthropic documents how progress records help long-running agents resume work. Nx shows how a dependency graph can identify work affected by a change. These are examples to learn from. The benefit of the proposed tools should be measured in Bradley’s workflows. Anthropic · Nx

**Repository baseline.** This report uses `scaffold/structure` at `99551d4`. The branch records Artifact Studio as a closed draft checked by its author. The agentic North Star pages remain proposals, including the refreshed learnings database, which has an earlier draft. The branch’s project index records zero tools promoted after outside use. [Branch snapshot](https://github.com/bar181/practical-ai/tree/99551d4) · [Artifact Studio status](../projects/artifact-studio/README.md#status) · [Project index](../projects/README.md)

The [repository inventory and original demand research](tool-inventory.md) and the [archived 24-tool ranking](../workshop/plans/archive/priorities-2026-11-15.md) retain the full branch history. The two lists above are proposed build priorities.
