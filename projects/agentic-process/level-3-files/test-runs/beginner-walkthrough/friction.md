# Beginner walkthrough: friction log

**Who ran it:** an AI session playing a beginner, on 16 November 2026. The persona: an office manager
at a 15-person firm who uses ChatGPT every day for emails but has never made a saved workflow, a
project or a custom instruction. Goals: (a) try the finished example, (b) use it for my own question,
(c) make my own small tool for a weekly job: every Friday I turn a pile of supplier quotes into a
short comparison for my boss.

**Rules of the run:** started at `projects/agentic-process/README.md`; opened only that file and the
files it links to inside `base/` (and files those link to inside `base/`). No chatbot was run and the
web was not searched: where the README says to paste something, I read what I would paste and judged
whether it would work. Links outside `base/` (the spec, the level-3 test logs, Artifact Studio) were
not opened. `base/examples/shared-tracker.md` and `base/examples/unattended-run.md` were not opened:
they are labelled "all nine" and "Level 2 and 3", and this beginner would skip them.

Minutes are my estimate for a real person, not timed.

## What I did

1. Read the README from the top down to the end of "Try it". (3 min)
2. Opened a new ChatGPT chat and looked for how to switch web search on. (2 min)
3. Opened `base/examples/decision-support/AI-INSTRUCTIONS.md` from the link and worked out how to copy all of it. (3 min)
4. Would paste the instructions into ChatGPT and send; judged that it would reply by asking six questions about my business, because no profile is present yet. (1 min)
5. Would copy the bakery sample from the README, paste it and send, then wait for the research. Judged it would work: the sample contains a full profile and a question, and the instructions handle both. (4 min)
6. Opened `base/examples/decision-support/example.md` and compared it with what I would expect to get. (8 min)
7. Read "Now your own question" and opened `base/examples/decision-support/README.md` to see how to keep it. (4 min)
8. Opened `base/examples/decision-support/WORKFLOW.md` from that page. (2 min)
9. Would ask my own question in a plain chat (should we move our office supplies to one supplier?), with the profile left out, and answer the six questions; I would need my boss for yearly sales. (10 min)
10. Would try to make a ChatGPT Project to keep it, with no how-to to follow. (15 min, likely given up)
11. Read "Make your own (the short path)". (2 min)
12. Opened `base/template/` and read its four files; decided I could not fill them in alone. (5 min)
13. Opened `base/PROCESS.md` to understand the nine checks; skimmed and gave up on the detail. (10 min)
14. Opened `base/examples/monday-email.md` to see what the coach hands back on the short path. (6 min)
15. Would copy the coach prompt, change the last line to "My idea: every Friday I turn a pile of supplier quotes into a short comparison for my boss. I want an AI to draft it." and send. (2 min)
16. If ChatGPT could not open the link: would open `base/AI-INSTRUCTIONS.md`, press Raw, copy it, paste it and type the line the README gives. Read the coach in full to judge it. (5 min)
17. Would go through the coach's short path: step 1, steps 2 to 5 in a line each, step 6, step 8. (30 to 45 min)
18. Would run the fresh-chat test myself in a new chat. (10 min)
19. Would save the four files the coach writes out and set them up. (15 min, with the blockers below)

Total: about 2 to 2.5 hours, of which (a) is about 20 minutes.

## Friction

1. **MINOR.** `README.md`, line 24: "Open a new chat in ChatGPT, Claude or Gemini, ideally with web search on." It does not say how to turn web search on in ChatGPT, or what I lose without it. (The instructions do handle it: they list five facts to look up. The README does not tell me that.)

2. **MINOR.** `README.md`, lines 25 to 26: "Paste in the tool's instructions:" The link opens a formatted page. How to copy the whole file (press **Raw**) is only explained 35 lines later, in the coach section (line 61). I would copy the formatted page by selecting it, which mostly works but loses the headings' marks.

3. **MINOR.** `README.md`, line 27: "Then paste this sample question from an invented bakery:" It does not say whether to send the instructions on their own first, or paste both in one message, or what the chatbot will say in between. Sent alone, `decision-support/AI-INSTRUCTIONS.md` line 12 to 13 ("If there is none, ask these six questions in one message") means ChatGPT will start asking me about *my* business. I would wonder whether to answer it or paste the bakery.

4. **MINOR.** `README.md`, line 19: "Try it: a finished tool, in 5 minutes". The result in `example.md` is a long page with eight sources, two tables and a SWOT shown twice. Pasting takes 5 minutes; waiting for the research and reading the result takes 10 to 15.

5. **MINOR.** `base/examples/decision-support/example.md`, lines 3 to 7: "(round 3 of testing)" and "Since this run, one line was added to the instructions". Nothing tells me what counts as success when my result differs from this one (and it will: different sources, different numbers). I needed a line such as "you got it right if your result has the options, sources with dates, a recommendation and a check list".

6. **MINOR.** `base/examples/decision-support/AI-INSTRUCTIONS.md`, line 71: "If the person asks for a polished version and Artifact Studio is available in this project". I do not know what Artifact Studio is, or whether I have it.

7. **MINOR.** `README.md`, line 41: "leave it out and the tool asks six questions once." In a plain chat it asks every time, unless I paste the profile back in. `decision-support/README.md`, lines 23 to 24: "Save that profile as a file in the project. It will not ask again." I do not know how to turn text in a chat into a file, or whether a Word document or a note counts.

8. **BLOCKING.** `README.md`, lines 41 to 42: "To keep it, save the instructions as a Claude Project, a ChatGPT Project or a Gemini Gem". Also `decision-support/README.md`, line 19: "Make a project in your chatbot: a Claude Project, a ChatGPT Project or a Gemini Gem." I have never made one. Nothing says where the button is, what my ChatGPT plan must include, or where "the project's instructions" are. Every "how to use it" page (`decision-support/README.md` and `template/README.md`) starts with this step, so keeping any tool depends on it. The only other option given is worse for me (item 9). The Monday email example quietly uses a phone note instead, but the README never offers that as the simple route.

9. **MINOR.** `decision-support/README.md`, line 22: "Add `example.md` as a project file". How to get a file from this page onto my computer is not said. Lines 19 to 20: "Or use a folder your chatbot can read, such as a Drive folder connected to it." I do not know what connecting a Drive folder to ChatGPT means.

10. **MINOR.** `base/examples/decision-support/WORKFLOW.md`, line 25: "| **Last tested** | LASTTESTED |". A placeholder left in the finished example. It makes the "complete tool" look unfinished, and it is the one row I would read to see whether it was tested.

11. **MINOR.** `README.md`, line 90: "**Level 2**: save, share and specify | Someone trained on AI, or a coder | A saved, shared workflow in a chatbot project". But the Base section (line 41) and the template's setup (`template/README.md` line 7) already ask me to save it in a project. I cannot tell whether saving a project is for me or for someone "trained on AI".

12. **MINOR.** `README.md`, line 131: "**Not yet run in ChatGPT, Gemini or Copilot, or by a person**". I use ChatGPT, and "Try it" names ChatGPT first. Honest, but it leaves me unsure the coach will behave in my chatbot, and nothing says what to do if it does not.

13. **MINOR.** `README.md`, lines 46 to 47: "Copy [the four-file template](../../../base/template/)". Copy it where, and how? It is a folder of four files with square-bracket gaps. Filling them in alone needs words I do not know yet (item 15). The coach is the only real route for me, and the README offers it second.

14. **MINOR.** `README.md`, line 52: the coach prompt points at `https://raw.githubusercontent.com/bar181/practical-ai/main/...`, and line 134 says "| The links in this page | Open once this project is merged into the main branch |". I do not know what "merged into the main branch" means. I read it as "the links on this page may be broken today", including the one I am told to paste. The fallback on lines 60 to 62 (press Raw, copy, paste) is clear and would work, which is why this is not blocking.

15. **MINOR.** `README.md`, lines 15 to 17 and 64 to 123: words I did not understand or that are not for me: "North Star", "The spec", "workflow card", "acceptance test", "gate", "repository", "a skill", "a tool server or GitHub" (line 91), "**If you are an AI agent:** follow `AGENTS.md`" (line 98), "run by a coding agent" (line 102), "a draft pull request" (line 109). About half the page is for coders, with no line telling a beginner "you can stop reading here".

16. **MINOR.** `base/PROCESS.md`, 434 lines. Each step has "Advanced" and "Expert" stories ("As a builder working with a coding agent", line 61) and line 396 says "An agent finds the same template in each new project folder as `base/plan.md`." Too dense to use as a beginner; I gave up and went back to the coach.

17. **MINOR.** `base/PROCESS.md`, line 12: "**What you end with: four files.**", but lines 393 to 425 then give "The one-page plan" to "Fill this in as you go", with rows like "The folder layout | [Decide it now and do not change it]" and "The wow". On the short path I cannot tell whether I need this plan as well as the four files.

18. **MINOR.** `base/examples/monday-email.md`, line 17: "its plan headings have changed since", and line 29: "## 1. The plan (one page)". The only short-path example hands back a plan, a prompt kept in "one note on your phone" (line 49) and a note. That is not the four files and the project the README promises (lines 7 to 10), so I cannot see what the coach will actually give me.

19. **MINOR.** `README.md`, line 66: "Take all nine when the tool is shared, uses shared files, or costs money." and `base/AI-INSTRUCTIONS.md`, lines 61 to 62: "Use all nine steps if they say no, or if the tool needs shared files, more than one person using it, or anything paid." My quotes come in by email to a shared inbox and the comparison goes to my boss. I cannot tell whether that is "shared files", so I do not know which path I am on. (Line 62 to 63 says readers of the result do not count, which helps with my boss, not with the inbox.)

20. **MINOR.** `base/AI-INSTRUCTIONS.md`, lines 27 to 28: "If several people are involved and nobody is named, the user is the person who acts on the result: the one who approves it or sends it." My boss acts on the comparison; I make it. My message says "I turn", so the coach will probably pick me, but a different reading would shape the tool for my boss.

21. **BLOCKING.** `base/AI-INSTRUCTIONS.md`, lines 46 to 47: "one acceptance test (a real input and what the result must contain)", and lines 35 to 36: "the test from step 1 is the example in step 6 and the one you hand over", but line 102: "Examples use invented data and say so." For my job the "real input" is real supplier quotes with names and prices. Do I paste real ones, which then end up in `example.md` and in a project my colleagues might see, or invent quotes? The coach says both. A different guess changes what I put in the files and who sees our prices.

22. **MINOR.** `README.md`, line 10: "It is free and works in the chatbot you already use." Nothing on this page or in the coach says whether it is fine to paste supplier prices or other company data into ChatGPT, or to check my ChatGPT data settings first. An office manager would either worry and stop, or not think about it.

23. **MINOR.** `base/AI-INSTRUCTIONS.md`, lines 29 to 31: "choose the design that works either way (pasting into the chat usually does)", and `template/WORKFLOW.md` line 10: "**Inputs** | [What they start with]". My quotes are PDFs and email attachments. Nothing tells me whether I can attach them or must copy the text out of each one, which for a pile of quotes is most of the work.

24. **MINOR.** `base/AI-INSTRUCTIONS.md`, lines 56 to 57: "in a temporary chat or with memory turned off, so nothing from this session carries over." I have never touched ChatGPT's memory settings and do not know where a temporary chat is. The coach is told to give exact test steps, so it may explain, but the README does not.

25. **BLOCKING.** `README.md`, lines 59 to 60: the coach "tests them in a fresh chat, keeps that result as the worked example". `base/AI-INSTRUCTIONS.md`, line 77: "In a chat you cannot run the test. Leave this gate open, and put the exact test under Test this next." So the coach does not test anything: I do, after the session. Nothing tells me to bring the fresh chat's result back to the coach chat, how to decide "what blocked it" (coach line 57: "Fix what blocked it"), or that I must paste the result into `example.md` myself. Expected outcome: I leave with three files and an empty example, believing the tool was tested.

26. **MINOR.** `base/AI-INSTRUCTIONS.md`, lines 37 to 38: "In a chat with no access to files, write each file out in full under its path. The person creates them." I do not know what "under its path" means or how to make a `.md` file. Nobody says a Word document or a Google Doc would do.

27. **MINOR.** `README.md`, line 44: "## Make your own (the short path)" gives no time. `base/PROCESS.md`, line 33: "Steps 1 to 8 add up to about 60 minutes the first time." That is for all nine; the short path, which I am on, has no estimate, so I cannot tell whether to start on a Tuesday afternoon or wait for a quiet day.

## Verdict

- **(a) Get the finished example's result: yes.** The decision-support instructions plus the bakery sample are complete and self-consistent; ChatGPT with web search would produce a brief of the same shape, though not word for word, and nothing says what counts as a match (items 3, 5).
- **(b) Run my own question: partly.** Once, in a plain chat, yes: the six questions work. Keeping it fails, because "make a project", "save the profile as a file" and "add example.md as a project file" have no how-to for someone who has never done them (items 7, 8, 9).
- **(c) Start my own supplier-comparison tool: partly.** The coach prompt (or its Raw fallback) would start a sensible short-path session and get me a workflow card and draft instructions, but I would have to guess whether to use real or invented quotes, and the test and the worked example are left to me with no steps for bringing them back (items 21, 25).

Blocking: 3. Minor: 24.
