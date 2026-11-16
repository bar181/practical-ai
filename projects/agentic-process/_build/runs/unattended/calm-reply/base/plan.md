# Plan: Calm Reply

Fill this in as you go through the nine steps. One page. If a section needs more than five
lines, the scope is too big.

**Think of it as:** a calm friend who reads the angry letter first and hands you a short, polite
answer, with blanks where only you know the facts.

**North Star:** a shop owner who is not technical can answer an upset customer email with a short,
calm reply in five minutes, without promising anything they have not decided.

| Heading | Write here |
| --- | --- |
| The job | Turn one long, upset customer email into a short, calm reply draft that the shop owner edits and sends. |
| The user | The shop owner: not technical, already uses ChatGPT. |
| What is out | Sending anything. Connecting to the inbox or the shop system. Looking up orders. Deciding refunds or policy. Saving past replies. Other staff. Any reply longer than 120 words. |
| The wow | The answer starts with one line saying what the customer actually wants, and every fact only the owner knows is a visible `[needs: ...]` blank, so the draft never promises what the shop has not decided. |
| What already exists | ChatGPT (Free) can draft replies but carries no shop rules from one email to the next. Open prompts exist (MIT, CC0) but write longer replies and suggest offers. Help desks with AI drafts are paid and need the shop's email moved into them. Practice: the HEARD method. Sources and dates: "Reuse check" below (all checked 2026-11-16). |
| Cost | ChatGPT Free: US$0, "unlimited everyday text chats, subject to abuse-prevention safeguards". Nothing else. |
| The design | ChatGPT, any plan. One file, `base/AI-INSTRUCTIONS.md`, pasted at the start of a chat (or into a ChatGPT Project's instructions, if the owner's plan has Projects: not confirmed). Manual: copying the email in, every fact and decision, editing, sending. |
| The folder layout | The fixed showcase layout: README.md, AGENTS.md, LICENSE, base/ (AI-INSTRUCTIONS.md, plan.md, examples/), _build/ (gates.json, checks/, runs/). No level-2 or level-3 folders yet. |
| The steps | 1. Open ChatGPT. 2. Paste the instructions once. 3. Paste the customer email; optionally add `What I know:` lines. 4. Read "What they want" and the draft. 5. Fill each `[needs: ...]` blank, edit, send it yourself. |
| The front door | README: a before-and-after picture, then "Try it in five minutes": copy one block (instructions plus a sample angry email) into ChatGPT and compare with the worked example. |
| The test | Input: the email in `base/examples/example-1-email-only.md`. Good result: "What they want" line; reply of 120 words or fewer; every ask answered or blanked; no refund, date or replacement promised; no blame; the four-part note. |
| Who reviewed it | Nobody yet. Step 7 is open (2026-11-16): no person or fresh session was available. |
| Next three additions | 1. A "Shop facts" block (returns, shipping times) pasted once. 2. A second tone on request (firmer). 3. Replying to the customer's second email in the same thread. |

## Status

| Part | State |
| --- | --- |
| The plan | Draft, steps 1 to 6 filled. Not reviewed (step 7 open) |
| The first version | Built by an AI agent: `base/AI-INSTRUCTIONS.md`. Not used by anyone |
| Tested by | Two fresh AI sessions, round 1 (2026-11-16): `_build/runs/round-1/`. Instructions fixed after; round 2 not run. No person yet |

## Reuse check (steps 2 to 4)

All rows checked on 2026-11-16 by web search. "Not confirmed" means the source could not be read or
did not say.

| Option | Kind | What it covers | Cost | Limits | If it goes away | Link |
| --- | --- | --- | --- | --- | --- | --- |
| ChatGPT Free | Built in | Drafts any reply from a prompt; can use existing GPTs | US$0 | "unlimited everyday text chats, subject to abuse-prevention safeguards"; "New GPT creation and publishing are not available on personal ChatGPT accounts, including Free, Go, Plus, and Pro" | The instructions file works in any chat assistant | https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq |
| ChatGPT Projects | Built in | Keeps custom instructions and files for a set of chats | Free per a Sept 2025 article; today's status not confirmed | 5 files per project on Free (2025 article); OpenAI's own page could not be read | Paste the instructions at the start of each chat instead | https://tech.co/news/openai-chatgpt-projects-tool-free ; https://help.openai.com/en/articles/10169521-projects-in-chatgpt (not readable) |
| ChatGPT Go / Plus | Built in, paid | More model access than Free | Go US$8/month (US); Plus US$20/month | Not needed for this job; other limits not confirmed | Use Free | https://openai.com/index/introducing-chatgpt-go |
| Gemini in Gmail ("Help me write", "Suggested Replies") | Built in, if the shop uses Gmail | Drafts and suggests replies inside Gmail | Personal accounts: no price stated; Google AI plan prices not confirmed | Personal Gmail accounts: "US only"; does not carry the shop's rules (not confirmed) | Use ChatGPT | https://support.google.com/mail/answer/16831098 |
| Shopify Inbox suggested replies | Built in, if the shop is on Shopify | AI suggested replies in Inbox conversations | Not confirmed | "available only in English"; whether it covers email is not confirmed | Use ChatGPT | https://help.shopify.com/cs/manual/inbox/chat-settings-and-appearance/shopify-magic |
| useful-ai-prompts "Escalation Handler" | Open source (MIT, maintainer handle aj-geddes, last updated 2026-02-28) | A prompt that turns an angry email into a draft plus coaching notes | US$0 | Draft is 150 to 300 words and proposes resolution options and timelines (the owner's decisions) | Copy kept locally under MIT | https://aj-geddes.github.io/useful-ai-prompts/prompts/escalation-handler |
| f/awesome-chatgpt-prompts | Open source (CC0-1.0, owner "f") | General prompt collection; a prompt for this exact job: not confirmed | US$0 | Last push 2025-04-30 per a snapshot synced 2025-05-05; current state not confirmed | Not relied on | https://awesome.ecosyste.ms/projects/github.com%2Ff%2Fawesome-chatgpt-prompts |
| HEARD method | Established practice | Hear, Empathize, Apologize, Resolve, Diagnose | US$0 | Written for all channels; email not addressed by name | Not a product | https://pollackpeacebuilding.com/blog/heard-method/ |
| Gorgias | Outside provider | Help desk with an AI Agent add-on | Starter US$10/month (50 tickets), Basic US$60/month (300 tickets); AI Agent "starts at $250 monthly as an add-on" | The shop's email moves into Gorgias | Replies stay in the owner's mailbox | https://gorgias.com/pricing/choose-your-plan |
| Help Scout | Outside provider | Shared inbox; AI Drafts writes draft emails | Free plan (5 users, 1 inbox, 100 contacts/month); Standard US$25 and Plus US$45 per user/month; AI Drafts US$50 per 100 conversations on legacy plans; whether Free includes AI Drafts: not confirmed | The shop's email moves into Help Scout | Replies stay in the owner's mailbox | https://www.helpscout.com/pricing ; https://docs.helpscout.com/article/1539-ai-drafts-billing-pricing |
| Zendesk, Outlook Copilot | Outside provider / built in | Not checked | Not checked | Not checked | Not checked | The person should look these up if the shop uses them |

**Step 2 answer:** nothing found does the whole job for this user at no cost while keeping the
shop's rules (short, no promises, blanks for facts). What is left to build is one paste-in
instruction file for the assistant the owner already uses. **Step 3 answer:** build the instruction
file; buy nothing for the first version. The paid options above are listed, not chosen.
**Step 4 answer:** the first version costs US$0 (ChatGPT Free).
