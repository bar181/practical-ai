# Delegation brief template

Fill this in by hand, or let the [`delegation-brief`](SKILL.md) skill fill it from your rough
request. Keep it to one page. When the work comes back, check it with the
[`check-handback`](check-handback/SKILL.md) skill.

```
Task: 
For:                From:                Due: 

Outcome
One sentence: what will be true when this is done.

Why it matters
One or two sentences. "Not given" is fine.

Done when
- [ ] Each line can be answered yes or no by someone who did not do the work
- [ ] 

You have
- Files, links, logins and contacts, and where they are

Must not
- What not to change, delete, send or spend

Out of scope
- What not to do, even if it looks useful

Decide yourself / ask first
- Decide yourself: 
- Ask first: 

When stuck or done
Who to ask, how, and what to hand back: the result, what was checked, anything left open.
```

## Extra section for an AI agent

Add this after "When stuck or done" when Claude Code, Codex, a Cowork task or another agent will do
the work.

```
For the agent
- Work only in: folders, files, branch
- Prove it with: one command or check per "done when" line where possible
- Stop and ask before: deleting, sending, posting, paying, publishing, merging, pushing to a
  shared branch, deploying or releasing, changing or deleting a test, or changing anything
  outside the area above
- Hand back: what changed, the result of each check, and anything you could not do
```

## The "done when" test

Read each line and ask: could someone who did not do the work answer yes or no, by looking at the
result, in under five minutes?

| Fails the test | Passes the test |
| --- | --- |
| The sheet is cleaner | Every product code appears once |
| Fix the login bug | A user with an expired password sees the reset link, not an error |
| Make the deck better | The deck is 10 slides or fewer and slide 2 states the ask |
| ASAP | Due Thursday 3 December, 12:00 |
| The usual format | Saved as a PDF in the Proposals folder, named Client-Date |
| Push to main when done | A pull request is open and not merged |
| Works like the PDF export | Streams the file the way the PDF export does: the download starts within 5 seconds |

## Before you send

- Every question the skill asked is answered or deliberately left open.
- Every (suggested) item is accepted, changed or removed.
- The doer actually has the access listed under "You have".
