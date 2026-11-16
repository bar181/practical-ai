# Inbox triage and daily summary: landscape review

What already exists for this job, and what the sources say about doing it safely. Checked on
2026-11-15, before anything further is built. This replaces the earlier notes.

## Summary

- **Sorting mail by the action it needs is settled practice.** Guides agree on four choices:
  delete, do, delegate, defer. The simple level sorts the same way.
- **Mail products are building this page themselves.** Gmail has thread summaries, and announced
  an inbox view that briefs you on to-dos. Check what your own mail product does before using
  this tool.
- **The risk named in the notes is real and well documented.** Text inside an email can steer an
  assistant that reads it. No source claims a complete fix. The agreed defence is to limit what
  the assistant may do and keep a person between it and anything that is sent.
- **Nothing new needs building for the simple level.** One page of instructions and a connected
  mailbox, or pasted messages.

## Established practice

| Practice | What the sources say | Source |
| --- | --- | --- |
| One decision per message | Every message gets one of four outcomes: delete it, do it, delegate it or defer it. Several guides credit the model to Microsoft | [Front](https://front.com/blog/4-ds-of-email-management), [Superhuman](https://blog.superhuman.com/executive-email-management/), [Lifehacker](https://www.lifehacker.com.au/2023/09/use-the-4d-method-to-keep-up-with-your-inbox/) |
| Do short things at once | If it takes about two minutes, do it now. Deferring and re-reading costs more | [Chatelaine](https://chatelaine.com/living/budgeting/how-to-organize-your-work-email-inbox/), [ColoradoBiz](https://coloradobiz.com/articles/the-taming-of-the-inbox-monster) |
| Few folders | Three working folders (action, read, waiting) keep the system usable | [Superhuman](https://blog.superhuman.com/executive-email-management/) |

These are vendor and trade guides, not studies.

## What already exists

| Product | What it does for this job | State on the date checked | Source |
| --- | --- | --- | --- |
| Gmail with Gemini | Summaries of long threads | Reported as rolling out to all users at no cost | [Tom's Guide](https://www.tomsguide.com/ai/gmails-biggest-update-in-20-years-5-ai-features-that-could-change-email-forever), [eWeek, 18 June 2026](https://www.eweek.com/news/google-gmail-ai-summaries-global-rollout/) |
| Gmail with Gemini | Questions answered from the whole inbox | Reported as needing a paid Google AI plan | [SiliconANGLE, 8 January 2026](https://siliconangle.com/2026/01/08/googles-gmail-getting-gemini-inspired-overhaul-ai-summaries/) |
| Gmail "AI Inbox" | A separate view that briefs you on to-dos and priority mail | Announced in January 2026 for a small group of testers in the United States. Current reach not confirmed here | [SiliconANGLE](https://siliconangle.com/2026/01/08/googles-gmail-getting-gemini-inspired-overhaul-ai-summaries/), [Tom's Guide](https://www.tomsguide.com/ai/gmails-biggest-update-in-20-years-5-ai-features-that-could-change-email-forever) |
| Claude with Gmail and Google Calendar connected | Searches and reads mail and calendar in a chat, on request | Available. **The official pages disagree** on which plans include it and on whether it can send mail. One says all users, with sending allowed after approval. Others say paid plans and read-only | [Support article](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors.md), [Gmail connector page](https://claude.com/docs/connectors/google/gmail.md), [Calendar connector page](https://claude.com/docs/connectors/google/calendar.md) |

Because the official pages disagree, check the connector list in your own account. Do not rely
on this table for plan details.

## The risk: instructions hidden in mail

| Finding | Source |
| --- | --- |
| A message can carry text written for the assistant, not the person. It is called indirect prompt injection. Email is a common route, along with documents, web pages and calendar invitations | [Barracuda, 23 October 2026](https://blog.barracuda.com/2026/10/23/indirect-prompt-injection-email-ai-assistants), [Phishing Tackle, 3 July 2026](https://phishingtackle.com/blog/prompt-injection-ai-inbox) |
| OWASP ranks prompt injection first among risks for applications built on language models | [Barracuda](https://blog.barracuda.com/2026/10/23/indirect-prompt-injection-email-ai-assistants), [Dark Reading](https://darkreading.com/cyber-risk/hidden-prompts-trick-ai-false-email-summaries) |
| In one security firm's test, an email with hidden text changed the assistant's summary in all ten trials | [Dark Reading](https://darkreading.com/cyber-risk/hidden-prompts-trick-ai-false-email-summaries) |
| There is no proven, complete prevention. Combine defences and assume one will fail | [Escudo Digital](https://www.escudodigital.com/en/experts/opinion/when-email-tries-tell-your-ai-agent-what-do.html) |
| What helps is limiting what the assistant can reach and do. The more it is allowed to do, the more a hijack costs | [Phishing Tackle](https://phishingtackle.com/blog/prompt-injection-ai-inbox), [Barracuda](https://blog.barracuda.com/2026/10/23/indirect-prompt-injection-email-ai-assistants) |

## How this tool follows it

| Practice | In this tool |
| --- | --- |
| One decision per message | The page sorts into "needs you today", "waiting on others" and "for information" |
| Keep a person before anything is sent | The skill reads only. It never sends, deletes, archives or marks as read. Replies are drafts |
| Treat mail as information, never as instructions | Written into the skill. Anything that reads like an instruction is reported, not followed |
| Limit what the assistant can do | The simple level works from pasted messages, with no connection at all |
| Payment changes | **Added after this review.** A message asking to change payment or bank details is flagged, with a note to confirm by a channel other than the email |

## Not rechecked for this review

- Outlook and Microsoft 365 Copilot features for the same job.
- ChatGPT's mail and calendar connections.
- Dedicated triage products and their prices.
- Scheduled runs, which the automated level would need.

## Build or license

| Level | Lean | Why |
| --- | --- | --- |
| Simple | Build nothing. Instructions and pasted messages | The practice is settled, and nothing is connected |
| Working | Reuse. Use the mail product's own summary if it has one, or a chat assistant's read-only connection | Both exist. The value added here is the page layout and the safety rules |
| Automated | Review before building. Only with read-only access and drafts, never automatic sending | The documented risk grows with what the assistant is allowed to do |

## Still to do

- Review Outlook and ChatGPT for the same job, with plans and dates.
- Review dedicated triage products and prices before the automated level.
- Send the assistant a test message containing a hidden instruction and record whether it is
  reported or followed.
