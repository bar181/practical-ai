# Tool inventory

Every tool this repository has a North Star page or a plan for, with its Beginner and Advanced
level, and the research on which simple tools people use most. Written on 15 November 2026.

**What to build next, and in what order, is in
[`practical-ai-priorities.md`](practical-ai-priorities.md).** This page is the inventory behind it.

**North Star:** practical AI tools a person can use the same day. Every tool comes at two depths.
A **Beginner** level a student or a business owner runs in any chat assistant with nothing
installed, and **Advanced** levels, with skills and connectors, for someone who works with agents
every day.

**Think of it as** a cookbook where every recipe is printed twice: once for a home kitchen with a
pan and a hob, and once for a professional kitchen with the full line.

## The levels, and who each is for

| Level | For | What it is | Depends on |
| --- | --- | --- | --- |
| Base | Everyone | The thing itself, a worked example with invented data, and the template | A browser or a reader |
| Level 1, **Beginner** | Students and business owners | Instructions to paste, a template to fill, one example to copy. No install, no code, under an hour | Any chat assistant |
| Level 2, **Advanced** | Someone who builds with agents | A skill, and connectors to where the work already lives: mail, calendar, drive, sheets. Gates so it repeats | An assistant that runs skills and connectors |
| Level 3, **Expert**, only where it earns its place | The owner's own setup | A database, an MCP server, a schedule or a second agent | Other systems |

A tool is not on this list unless its Beginner level can be described in two sentences.

## Part 1. Builds with a North Star page or a plan

26 tools. Grouped by how far each has got, not ranked. The Demand column points to Part 2: a
number means independent research found people already doing this job with AI.

### Built

Closed as a draft on 15 November 2026. Built and checked by its author. Not yet used by anyone else.

| Tool | What it does | Beginner: a student can run it | Advanced: skills and connectors | Demand |
| --- | --- | --- | --- | --- |
| [Artifact studio](../projects/artifact-studio/) | Pages, slide decks and social posts from your notes, from a library of 20 templates. | Paste the instructions into any assistant, copy the sentence from an example, attach your notes, and check every number. | The `artifact-studio` skill and a preferences file, so a short ask gives your look and voice. Expert: an MCP server with ten tools gives any assistant the library. | #7, and just outside the ten |

### North Star page written, not approved

One to three pages each: who it is for, what already exists, what is in scope. Nothing is built
until a person approves the page.

| Tool | What it does | Beginner: a student can run it | Advanced: skills and connectors | Demand |
| --- | --- | --- | --- | --- |
| [Decision support assistant](../workshop/plans/decision-support/) | A decision worked the way a consulting team would, in seven steps, with every link checked. | Describe a decision. The assistant walks seven steps with a template for each and stops twice for your correction. You get a one-page recommendation. | A skill that keeps the working folder in Google Drive, checks every link, scores its own recommendation, and builds the brief and deck with the artifact studio. | #6 |
| [Source and link verifier](../workshop/plans/source-verifier/) | Every link in a document opened on a known date and checked against the sentence it supports. | Paste a document into an assistant that can browse. Get a table: each link, whether it opens, and whether it supports its sentence. | A skill that checks a whole Google Drive folder, writes a dated report, and runs as a gate so a document with a dead link cannot be marked finished. | #1, in part |
| [Learnings database](../workshop/plans/learning-system/NORTH-STAR.md) | One row for every error, redo and thing that unexpectedly worked, in a store you own, read before similar work starts. | Keep a private sheet with the given columns. Say "log that" when something breaks or unexpectedly works, paste the row, and paste the relevant rows in before similar work. | A skill that writes and finds rows through a Google Sheets connector and checks for duplicates first. Expert: Supabase with keyword and similarity search behind an MCP server. |  |
| [Task decomposition and dependency graph](../workshop/plans/task-graph/) | A goal becomes tasks with what depends on what, drawn five ways from one file. | Describe a goal. The assistant asks up to five questions and returns the tasks, what blocks what, and one picture: a tree or a Mermaid diagram. | A skill that keeps the task file, redraws all five views (tree, Mermaid, sticky notes, Gantt, ready list) and saves them to a Google Drive folder. Expert: an MCP server an agent works from. |  |
| [Core memory system](../workshop/plans/core-memory/) | Notes, policies, websites, code and repository pointers as labelled records in a store you own. Not a wiki. | One private sheet with labels. Say "keep this", paste the row it gives you, and paste the rows you need when you ask a question. | A skill that files and finds records through a Google Sheets connector, exactly by kind and label, and retires what is replaced. Expert: Supabase with similarity search behind an MCP server. |  |
| [Connections hub](../workshop/plans/connections-hub/) | Reads a meeting, an email thread, a web page or a file and files what is worth keeping, after you review it. | Paste one transcript, thread or page. The assistant proposes the records worth keeping. Delete what you do not want and paste the rest into your sheets. | A skill that reads through connectors you already have (Gmail, Google Drive, Granola, Zoom), shows a review queue and files what you accept into the two stores. |  |
| [Rubric reviewer](../workshop/plans/rubric-reviewer/) | Any piece of work scored out of 100 against a rubric written beforehand, by a reviewer with fresh eyes. | Paste a rubric and a piece of work into a fresh chat. Get a score, evidence for each line and the three changes that would raise it most. | A skill that runs the review in a separate session, writes it beside the work, and serves as the scoring stage for every other tool. |  |

### Drafted in the earlier layout

A Beginner level exists as a draft. None has been reviewed by a second person. Each moves to the
base-and-levels layout when it is next worked on. Plans are in [`workshop/plans/`](../workshop/plans/).

| Tool | What it does | Beginner: a student can run it | Advanced: skills and connectors | Demand |
| --- | --- | --- | --- | --- |
| [Weekly brief with research](../workshop/drafts/weekly-brief/) | One page a week: what changed outside, with links, and what your own documents and transcripts say. | Give a watch list of topics and attach the week's documents. Get one page with a link for every outside item. Check the links yourself. | The `weekly-brief` skill with web search and a Google Drive connector to a folder of transcripts and documents, a saved watch list, and the same shape every week. | #1 |
| [Inbox triage and daily summary](../workshop/drafts/inbox-daily-summary/) | One morning summary across email, calendar and social media feedback, with replies drafted for approval. | Paste or connect today's email and calendar. Get one summary: needs you today, drafted and waiting, meetings, can wait. Nothing is sent without you. | The `morning-summary` skill with Gmail and Google Calendar connectors: replies written in your voice as drafts, finished threads filed, run each morning. | #5 |
| [Voice post drafter](../workshop/drafts/voice-post-drafter/) | A draft post or newsletter that sounds like you, for you to edit and publish yourself. | Build a voice file from three to five things you wrote. Give a point of view. Get one draft for one channel and edit it yourself. | The `voice-drafter` skill keeps the voice file and applies saved feedback every time. Source material from a Google Drive folder, post pictures from the artifact studio. | #2 and 7 |
| [Dashboard](../workshop/drafts/dashboard/) | Your key numbers on one page, each showing where it came from. | Put five to eight figures in one sheet. Ask for a one-page dashboard that shows the source of each number. | The `dashboard-builder` skill with a Google Sheets connector, then connectors to the systems the numbers come from: sales, accounting, customers. | #9 |
| [Estimator](../workshop/drafts/estimator/) | A first-draft quote with its reasoning, from your own price list and written rules. Three example businesses. | Put your price list and rules in a sheet. Paste a job description. Get a first-draft quote that shows every step. | The `quote-drafter` skill reads the price list through a Google Sheets connector, saves the quote to Google Drive and hands it to the proposal builder. |  |
| [Publishing a website](../workshop/drafts/website-publishing/) | A page goes from a chat artifact to a hosted site. | Build the page as an artifact and share its link. Check it on a phone and check nothing private is in it. | The `publish-check` skill runs the checklist, then a hosting connection such as Cloudflare puts the page at your own address. Expert: a repository that deploys on every approved change. |  |
| [Short video guide](../workshop/drafts/short-video/) | The right route for a short video by length and purpose, finished in under 30 minutes. | Write a four-beat script of about 50 words, pick one of four routes, and follow its steps in that tool's own app. | The `script-and-beat-sheet` skill with a saved prompt set per route and your voice file, so every video sounds like you. |  |
| [Training explainer with avatar](../workshop/drafts/training-explainer/) | A topic becomes a taught video in a teaching style chosen from a menu. | Fill in a five-line brief, pick a teaching style, build a beat sheet and a script, and record it yourself over slides. | A skill that turns the brief into a script and slides from the artifact studio, with generated visuals and your own cloned voice from a provider you choose. |  |

### Plan only

| Tool | What it does | Beginner: a student can run it | Advanced: skills and connectors | Demand |
| --- | --- | --- | --- | --- |
| [Meeting to actions](../workshop/plans/meeting-to-actions/) | A transcript becomes decisions, owners and dates. | Paste a transcript. Get decisions, actions with an owner and a date, open questions and a follow-up email. Check names and dates. | A skill that reads the transcript from your meeting recorder through a connector (Granola and Zoom each have one), writes actions to a sheet and drafts the follow-up email. | #4 |
| [Expense form creator](../workshop/plans/expense-form/) | A folder of receipt photos becomes a categorised expense form. | Upload receipt photos with your category list. Get a filled form: date, supplier, amount, tax, category. Check every line against the photo. | A skill that reads a connected Google Drive folder of receipts and writes rows through a Google Sheets connector, with your accounting and tax codes in the category list. | #10 |
| [Lead responder](../workshop/plans/lead-responder/) | A fast, qualified reply to every new enquiry, drafted for approval. | Write what makes an enquiry a good fit and one reply you are proud of. Paste each new enquiry. Get a draft reply and whether it fits. You send it. | A skill with a Gmail connector that watches the inbox and web forms, drafts with real meeting times from the calendar, logs each lead to a sheet and waits for approval. | #8, in part |
| [Website chatbot](../workshop/plans/website-chatbot/) | A site assistant that answers from your own notes and captures enquiries. | Write one page of facts and the ten questions you hear most. Load it into a chat Project and test it with awkward questions. | Embedded on the site, answering only from notes kept in a connected Google Drive folder or sheet, and writing a name and a question to a sheet when it cannot answer. | #8, in part |
| [Proposal builder](../workshop/plans/proposal-builder/) | Notes from a client conversation, or a finished estimate, become a formatted proposal. | Give your proposal template, your notes and the price. Get a filled proposal and a list of what it assumed. | A skill that builds the proposal with the artifact studio from templates and past proposals in a connected Google Drive folder, with prices from the estimator. |  |
| [Client onboarding kit](../workshop/plans/client-onboarding-kit/) | A welcome pack and a checklist for each new client. | Give a welcome template, a checklist and your notes from the sales conversation. Get a tailored pack for week one. | A skill that fills the pack from your customer records and the signed proposal through connectors, and puts the checklist dates in the calendar. |  |
| [Client project tracking and support site](../workshop/plans/client-project-portal/) | A page each client can open to see where their project stands. | One page per client: where the project stands, what was done, what is next. Ask the assistant to revise it and share the link. | A skill that rebuilds each page from a project sheet through a Google Sheets connector and publishes it. Expert: sign-in with a hosted service such as Supabase. |  |
| [Student AI assistant](../workshop/plans/student-assistant/) | A course assistant that answers from the lesson material and names the lesson it used. | A chat Project holding the course materials, told to answer only from them, name the lesson, and say when the material does not cover the question. | A skill with a Google Drive connector to the lesson folder, embedded in the training website, with a sheet of the questions the material could not answer. |  |
| [Training website](../workshop/plans/training-website/) | A course site with lessons, a schedule and a built-in assistant. | One page per course built as an artifact: the outline, this week's lesson, what is due, links to materials. | A skill that builds lesson pages from a Google Drive folder of materials, with a schedule that updates itself and the student assistant embedded. |  |
| [Daily builder](../workshop/plans/daily-builder/) | A scheduled agent that takes the next item on this list through the project method and opens a pull request. | Not a student tool. By hand: ask the assistant to take the next item here, draft its Beginner level and stop for your review. | The `project-builder` skill with a fixed rubric, a second agent that scores the work, and a GitHub connection that opens a pull request for every run. |  |

The [project method](../workshop/drafts/project-method/) is how any of these gets built. It supports the
tools and is not one of them.

## Part 2. The ten most in-demand simple tools

Researched on 15 November 2026 from usage studies and surveys, without looking at Part 1 first.
The question was: what do people and small businesses already use AI for most, that is simple
enough to teach in one sitting?

| # | Mini project | Why it is in demand | Beginner | Advanced | Already on the list? |
| --- | --- | --- | --- | --- | --- |
| 1 | **Research brief with checked sources** | Pew: 57% of workers who use chatbots at work have researched a topic with one. A May 2026 poll of 524 business leaders: 69% search for information. Pythian: 66%. | Ask a question in a fixed shape. Get one page: the answer, what is uncertain, and a dated link for every claim. Open three of the links yourself. | A skill with web search that runs the source verifier on its own brief and saves it to Google Drive. Put on a schedule, it is the weekly brief. | Partly: weekly brief (draft), source verifier (North Star). No one-off brief |
| 2 | **Rewrite and draft in my voice** | The largest study of ChatGPT use names writing the most common work task. A summary of the paper puts it near 40% of work messages, two thirds of them edits to the person's own text. Pew: editing 52%, drafting 47%. | Build a voice file from five things you wrote. Paste any email or paragraph and ask for it tighter, warmer or shorter, in your voice. | A skill that keeps the voice file and leaves the result as a draft in your mail through a Gmail connector. | Partly: voice post drafter (draft) covers posts, not everyday editing |
| 3 | **Summarise a document** | Leaders poll: 68% summarise documents. Adobe: 77% of workers who use AI summarise information with it. Pythian: 43%. | Attach a report or a contract. Get a fixed shape: what it says, what it asks of you, what is missing, with the page for each point. | A skill that works through a Google Drive folder and writes one row per document to a sheet. | No. New |
| 4 | **Meeting notes to actions** | Listed first in two of the automation guides read (The Rundown, Krater) and named in a third (G2). Pythian: 41% take notes with AI. Section: summarising meeting notes is one of the basic uses that describe 70% of the workforce. | Paste a transcript. Get decisions, actions with an owner and a date, open questions and a follow-up email. Check names and dates. | A skill that reads the transcript from your meeting recorder through a connector (Granola and Zoom each have one), writes actions to a sheet and drafts the follow-up email. | Yes: meeting to actions (plan) |
| 5 | **Email triage and reply drafts** | Leaders poll: 58% draft emails. Email management is one of G2's six categories, and email drafting is on Krater's list of first automations. | Paste or connect today's email and calendar. Get one summary: needs you today, drafted and waiting, meetings, can wait. Nothing is sent without you. | The `morning-summary` skill with Gmail and Google Calendar connectors: replies written in your voice as drafts, finished threads filed, run each morning. | Yes: inbox triage and daily summary (draft) |
| 6 | **Decision helper** | Microsoft's 2026 Work Trend Index: nearly half of Copilot chat use supports analysis, decisions and problem-solving. The ChatGPT study says its value comes through decision support. | Describe a decision. The assistant walks seven steps with a template for each and stops twice for your correction. You get a one-page recommendation. | A skill that keeps the working folder in Google Drive, checks every link, scores its own recommendation, and builds the brief and deck with the artifact studio. | Yes: decision support assistant (North Star) |
| 7 | **One piece into a week of posts** | QuickBooks, January 2026: marketing is the most common small-business use, at 45% of those using AI. Bluevine: marketing and sales 37%. Content repurposing is on Krater's list. | Paste one article or talk and your voice file. Get five posts for the channels you use. Edit and post them yourself. | A skill that also makes the post pictures with the artifact studio and lays the week out in a sheet. | Yes: voice post drafter (draft) with the artifact studio (built) |
| 8 | **Customer reply assistant** | PYMNTS, October 2026: customer service and calls is the widest small-business use, at 58% of AI users. QuickBooks: 37%. | Write one page of facts and your ten most common questions. Paste a customer message. Get a reply drafted only from your page. | A skill with a Gmail connector that drafts replies for approval and logs each question to a sheet. Later the same page sits behind a website chatbot. | Partly: website chatbot and lead responder (plans) |
| 9 | **Ask your spreadsheet** | Bluevine, April 2026: data analysis and business insights is the most common use, at 39%. A survey of 311 decision-makers: 36%. Section: automated reporting is one of only three uses that reached real workflows. | Upload a spreadsheet and ask one question. Get the answer, the rows it used and one chart. Check the total against your own. | A skill with a Google Sheets connector that answers from the live sheet and builds the dashboard from it. | Partly: dashboard (draft) shows numbers, it does not answer questions |
| 10 | **Receipts and invoices into a sheet** | QuickBooks: bookkeeping 35%. PYMNTS lists bookkeeping among the four most common uses. Data entry and reconciliation is on Krater's list. | Upload receipt photos with your category list. Get a filled form: date, supplier, amount, tax, category. Check every line against the photo. | A skill that reads a connected Google Drive folder of receipts and writes rows through a Google Sheets connector, with your accounting and tax codes in the category list. | Yes: expense form creator (plan) |

**Just outside the ten:** a report or a deck from your notes (Anthropic, June 2026: documents and
reports are the output of 15% of conversations; already built here as the artifact studio),
scheduling and calendar planning (30% in one small-business survey), and a brainstorming partner
(Adobe: 69%).

### What this says about Part 1

- **Five of the ten already have a plan, a draft or a North Star page.** Four are partly covered.
  One, summarising a document, is new.
- **Five of the seven North Star pages match no demand at all:** the learnings database, the task
  graph, core memory, the connections hub and the rubric reviewer. They are equipment for someone
  who builds with agents. Students did not ask for them. They belong at the Advanced end.
- **Meeting notes to actions stands on its own.** The connections hub page proposed absorbing it.
  The research says it is one of the most wanted simple tools, so it stays a tool.
- **The fastest Beginner wins are 3, 2 and 4:** each is one pasted instruction and one template.

### How the ten were chosen, and the limits

Each candidate was counted by how many independent sources named it, then ordered by that count
and by how simple its Beginner level is. The order is a judgement, not a measurement.

- The surveys asked different people different questions, so their percentages cannot be compared
  with each other.
- Three sources are vendor guides to automation. They show what is commonly built, not how often.
- One sitting. Nothing here was tested with students.

### Sources, all read 15 November 2026

| Source | What it is |
| --- | --- |
| [How people are using ChatGPT](https://openai.com/index/how-people-are-using-chatgpt/) and [the paper](https://www.nber.org/papers/w34255) | OpenAI and Harvard, 1.5 million conversations |
| [A summary of the same paper](https://c3.unu.edu/blog/what-over-2-5-billion-daily-messages-reveal-about-how-people-use-chatgpt) | United Nations University |
| [2026 Work Trend Index](https://microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization), [summary](https://smartbridge.com/ai/work-trend-index-annual-report-highlights-insights) | Microsoft, Copilot use in one week of February 2026 |
| [Anthropic Economic Index, June 2026](https://www.anthropic.com/research/economic-index-june-2026-report) | What Claude conversations produce |
| [Pew Research Center](https://pewresearch.org/?p=200020) | Workers who use chatbots at work |
| [Leaders poll, May 2026](https://www.staffingindustry.com/news/global-daily-news/ai-use-rises-though-strategic-adoption-lags-survey-finds) | 524 business leaders in the United States and United Kingdom |
| [AI Proficiency Report, January 2026](https://www.sectionai.com/ai/the-ai-proficiency-report-january-2026) | Section, 5,000 knowledge workers |
| [AI use study](https://www.adobe.com/acrobat/resources/ai-use-iceberg-study.html) | Adobe |
| [AI in the workplace survey](https://www.pythian.com/blog/ai-in-the-workplace-employee-productivity-sentiment-survey) | Pythian, 2025 |
| [SMB Growth Report, October 2026](https://www.pymnts.com/report/study/ai-goes-to-work-how-smbs-grow-without-growing-payroll/) | PYMNTS |
| [2026 AI Impact Report, as reported](https://stacker.com/stories/small-business/77-small-businesses-now-use-ai-regularly-heres-where-theyre-starting) | Intuit QuickBooks, 34,364 owners |
| [Small business AI trends 2026](https://www.bluevine.com/blog/small-business-ai-trends-report-2026) | Bluevine, 942 owners, April 2026 |
| [Survey of 311 decision-makers](https://securitybrief.news/story/us-smbs-use-ai-mainly-for-data-analysis-schedules) | Businesses under 500 employees |
| [The Rundown](https://app.therundown.ai/blog/ai-workflow-automation-examples-business), [Krater](https://krater.ai/blog/ai-for-business-automation), [G2](https://learn.g2.com/how-to-automate-tasks-with-ai) | Guides to first automations. Vendors |

### Check before building any Advanced level

- **A small-business plugin already ships skills for several of these jobs:** inbox, proposals,
  leads, invoices, reports and customer replies. Seen in an assistant's skill list on 15 November
  2026. Read it at stage 2. Where it does the job, the Advanced level is "install that", and the
  work here is the Beginner level and the teaching.
- **Published skills lean toward code.** One directory says seven of its ten most installed
  skills are for building interfaces
  ([source](https://agenticskills.io/learn/what-are-claude-skills)). Everyday business skills are
  less crowded.

## What left this list

Archived, not deleted, in [`workshop/plans/archive/`](../workshop/plans/archive/):

- The ranked list of 24 with scores, from earlier on 15 November 2026. It ranked tools by how much
  they supported the build method, which is the drift this rewrite corrects.
- Twelve ideas that never had a plan.
