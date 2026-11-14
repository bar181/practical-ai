# Priorities

The tools this repository is working toward, in priority order. This file is generated from what
is on disk, so the flags always match the folders.

| Flag | Means |
| --- | --- |
| Published | How many levels of the tool are in `projects/` (demo, simple, working, automated) |
| Student guide | Whether a step by step explainer or other support exists, and where |
| Plan | Whether a plan is published in `plans/` |
| Commercial | Whether a commercial-grade explainer exists |

| # | Tool | What it does | Published | Student guide | Plan | Commercial |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Artifact studio | Ask for a web page or small tool and choose its style, from clean to cinematic to scrollytelling, with optional video and audio add-ons. | 0 | Draft guide | [Yes](../plans/artifact-studio/) | No |
| 2 | Voice post drafter | A draft post or newsletter that sounds like you, for you to edit and publish yourself. | 0 | Draft guide | [Yes](../plans/voice-post-drafter/) | No |
| 3 | Short video guide | Pick the right route by length and purpose and finish a short video in under 30 minutes. | 0 | Draft guide | [Yes](../plans/short-video/) | No |
| 4 | Daily builder | A scheduled agent that researches and builds the next item on this list, then opens a pull request for review. | 0 | No | [Yes](../plans/daily-builder/) | No |
| 5 | Training explainer with avatar | Turn a topic into a taught video in a teaching style chosen from a menu. | 0 | Draft guide | [Yes](../plans/training-explainer/) | No |
| 6 | Student AI assistant | A course assistant that answers from the lesson material and names the lesson it used. | 0 | No | [Yes](../plans/course-operations/) | No |
| 7 | Website chatbot | A site assistant that answers from your own notes and captures enquiries. | 0 | No | [Yes](../plans/sales-department/) | No |
| 8 | Course program manager | Schedules, reminders and surveys for a cohort, with a summary of the results. | 0 | No | [Yes](../plans/course-operations/) | No |
| 9 | Daily topic scout | A morning list of topics with draft posts, ready for review. | 0 | No | [Yes](../plans/voice-post-drafter/) | No |
| 10 | Expense form creator | A folder of receipt photos becomes a categorised expense form. | 0 | No | [Yes](../plans/expense-form/) | No |
| 11 | Lead responder | A fast, qualified reply to every new enquiry, drafted for approval. | 0 | No | [Yes](../plans/sales-department/) | No |
| 12 | Meeting to actions | A transcript becomes decisions, owners and dates. | 0 | No | No | No |
| 13 | Outreach agent | Follow-up sequences drafted in your voice and sent only on approval. | 0 | No | [Yes](../plans/sales-department/) | No |
| 14 | Website from your notes | A small hosted site generated from your own notes and kept in step with them. | 0 | No | [Yes](../plans/artifact-studio/) | No |
| 15 | Call agent | A voice agent that answers common questions and books appointments. Inbound first. | 0 | No | [Yes](../plans/sales-department/) | No |
| 16 | Sales department blueprint | A map of sales and marketing roles to agents, assembled from the tools above. | 0 | No | [Yes](../plans/sales-department/) | No |
| 17 | Song and jingle add-on | A short generated track for a video or page. | 0 | No | [Yes](../plans/artifact-studio/) | No |
| 18 | Proposal builder | Notes from a client conversation become a formatted proposal. | 0 | No | No | No |

Order follows three tests: it is useful to the maintainer first, it can be taught without code, and
it reuses something that already exists.
