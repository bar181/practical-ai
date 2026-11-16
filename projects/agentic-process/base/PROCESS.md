<!-- Written by _build/build.py from _build/steps.py. Change the source, not this file. -->
# The nine steps in detail

Nine steps from an idea to a tool someone else can try. Each step ends at a gate: a plain
question you must be able to answer before you go on. For every step this page gives the purpose,
a user story for each level, what to expect, what proves the step is done, and a prompt to paste.

**Think of it as** building a deck in the garden. Decide what it is for. Check whether a kit
already exists. Price the wood. Pick the spot. Draw it. Have someone check the drawing. Build the
smallest platform you can stand on. Extend it only once you are using it.

**Two ways to use this page.** Paste the [build coach](AI-INSTRUCTIONS.md) into a chatbot and it
walks you through all nine. Or take the steps one at a time with the prompts below.

## The steps at a glance

| # | Step | You write down | The gate | Time |
| --- | --- | --- | --- | --- |
| 1 | [**Scope**](#1-scope) | One user, one job, what is out, and the one thing that will make people stop and look | Can you say the job in one sentence? | about 5 min |
| 2 | [**Reuse check**](#2-reuse-check) | What already does this: built in, free, common practice | After what already exists, is there still something to build? If not, stop and write a guide to that thing. | about 10 min |
| 3 | [**Outside help**](#3-outside-help) | Paid services for whatever is left. Do not pick a provider. Decide only build, buy or by hand for each part | Do you know what you would build and what you would buy? | about 5 min |
| 4 | [**Cost**](#4-cost) | Every dependency of the first version, with its price and its limit | Does the first version cost nothing, or an amount you accept? | about 5 min |
| 5 | [**Simplest design**](#5-simplest-design) | Which assistant, where files live, what stays manual. The folder layout, fixed now | Could a beginner draw it? | about 5 min |
| 6 | [**Plan and front door**](#6-plan-and-front-door) | The steps a person follows, the first screen they see, one worked example for each kind of request it handles | Is the beginner version fully described? | about 10 min |
| 7 | [**Review**](#7-review) | Someone who is not the author reads the plan | Can someone else explain it back to you? | about 5 min |
| 8 | [**Build and test**](#8-build-and-test) | The beginner version. Then a test by a fresh AI session that has only your instructions | Did a fresh session finish the job, and have you read what it tripped on? | about 15 min |
| 9 | [**Grow**](#9-grow) | One addition, one change request. What you learned | Is the level below in use before you build the next? | repeats |

Steps 1 to 8 add up to about 60 minutes the first time. Every time on this page is an estimate: nobody
has yet been timed.

**A small job can take the short path:** steps 1, 6 and 8 in full, steps 2 to 5 in a line each, step 7 folded into the test, and step 9 left open.
The coach offers it when the job is one person turning one kind of input into one result in a chat.

## Who does what

| Step | The AI does | You do |
| --- | --- | --- |
| 1 to 4 | Asks the questions, searches for what exists, lists costs | Answer honestly. Say no to anything outside the one job |
| 5 to 6 | Drafts the design, the plan and the first screen | Cut it down. Fix the layout and do not change it later |
| 7 | Plays the reviewer if no person is free, in a fresh session | Find a real person if you can |
| 8 | Builds, and runs the fresh-session test | Read what the test tripped on. Decide what to fix |
| 9 | Makes each addition | Approve each one. Use the tool yourself |

## 1. Scope

**Purpose.** Decide who the tool is for and the one job it does, before anything is built. A tool that does one job gets finished. A tool that does five gets rebuilt.

**User stories**

- **Beginner.** As someone with a job I repeat every week, I want to say the job in one sentence, so that the AI builds that and nothing else.
- **Advanced.** As a builder working with a coding agent, I want the scope written into the plan, so that the agent has something to refuse extra work against.
- **Expert.** As a team lead whose agents work unattended, I want one user and one job agreed before any agent starts, so that I am not reviewing five half-built features.

**What to expect.** About 5 minutes. Expect to drop something you wanted: the first answer is usually two or three jobs.

**Proof you are done**

- One sentence: who it is for, what goes in and what comes out
- Three things the first version will not do
- One test: a real input, and what a good result looks like

**The gate.** Can you say the job in one sentence?

**Prompt to paste**

```
I want to turn a job I repeat into a small AI tool. Help me scope it.

Ask me up to two questions, one at a time. Then write:
1. The one user.
2. The one job, in one sentence: what goes in and what comes out.
3. Three things the first version will not do.
4. The one thing that would make someone stop and look.
5. One test: a specific input, and what a good result looks like.

If I describe more than one job, make me choose one and put the rest under "Later".

My job: [describe the job you repeat]
```

## 2. Reuse check

**Purpose.** Find out whether something you already have, or something free, does the job. The cheapest tool is the one you do not build.

**User stories**

- **Beginner.** As someone with a job I repeat every week, I want to know whether my chatbot already does this, so that I do not spend a week rebuilding a built-in feature.
- **Advanced.** As a builder working with a coding agent, I want links and dates for what exists, so that I can wrap an existing tool and not start from nothing.
- **Expert.** As a team lead whose agents work unattended, I want the reuse check written down, so that nobody on the team builds what we already pay for.

**What to expect.** About 10 minutes with web search, longer without. Expect to find something that does part of the job. Often the result is that you build less than you planned.

**Proof you are done**

- A short list of what exists, each with a link and the date you looked
- One line saying what is still left to build
- If nothing is left: a short guide to the existing tool, and you stop here

**The gate.** After what already exists, is there still something to build? If not, stop and write a guide to that thing.

*In a chat with the coach:* If the answer is no, stop: hand over a short guide to that thing and the note, in place of the plan. The assistant they already use counts only if one plain sentence typed into it gives a result the person would send unchanged. Ask them to try one now. If they cannot, go on, and put "try one plain sentence first" under Test this next.

**Prompt to paste**

```
Before I build anything, check what already exists for this job: [the one-sentence job from step 1].

Look in this order: features already built into the assistant I use ([name it]), free and open-source tools, and how people who do this well usually do it. Search the web if you can. If you cannot, say so and list what I should look up.

Give me a table: the option, what it covers, what it costs, its limits, a link, and today's date. Do not invent a product or a price.

Then tell me plainly: does something existing do the whole job? If yes, tell me to stop, and write me a short guide to it. If no, say in one line what is left to build.
```

## 3. Outside help

**Purpose.** For whatever is left, list the services you could pay for, so that the choice between building and buying is made on purpose.

**User stories**

- **Beginner.** As someone with a job I repeat every week, I want to know what I would have to pay for, so that there are no surprises after I start.
- **Advanced.** As a builder working with a coding agent, I want the options listed and not ranked, so that I choose with the cost and the way out in view.
- **Expert.** As a team lead whose agents work unattended, I want build-or-buy decided for the first version only, so that we do not sign up for a service before we know the tool is used.

**What to expect.** About 5 minutes. For most beginner tools the answer is that there is nothing to buy. Write that down and go on.

**Proof you are done**

- A list of paid options for what is left, or the words "nothing to buy"
- For each part of the tool: build it, buy it, or leave it as something done by hand

**The gate.** Do you know what you would build and what you would buy?

**Prompt to paste**

```
Here is what is left to build after the reuse check: [paste the one line from step 2].

List any paid services that could do part of it. For each: what it does, the price, the free limit if there is one, and what happens to me if it closes or raises its price. List them evenly. Do not choose one for me, and do not invent a price: write "not confirmed" if you cannot check it.

Then, for each part of the tool, say whether the first version should build it, buy it, or leave it as something I do by hand.
```

## 4. Cost

**Purpose.** Put a price and a limit on everything the first version depends on. A tool people cannot afford to run is not finished.

**User stories**

- **Beginner.** As someone with a job I repeat every week, I want to know it runs on the plan I already have, so that I can use it tomorrow.
- **Advanced.** As a builder working with a coding agent, I want every dependency listed with its limit, so that the tool does not stop working in its first busy week.
- **Expert.** As a team lead whose agents work unattended, I want to know who pays, the builder or each user, so that the cost of rolling it out is known before we roll it out.

**What to expect.** About 5 minutes. Expect the first version to cost nothing new. If it needs something paid, that usually belongs in a later level.

**Proof you are done**

- A table: each thing the first version depends on, its price, its limit, and who pays
- One line: the first version costs nothing new, or it costs this much

**The gate.** Does the first version cost nothing, or an amount you accept?

*In a chat with the coach:* With prices not checked, the gate passes only if the first version buys nothing new. Say so.

**Prompt to paste**

```
List everything the first version of this tool depends on: [describe the first version in a sentence, and name the assistant and the plan you use].

For each dependency give: what it is for, its price, its usage limit, and who pays (me, or each person who uses the tool). Write "not confirmed" where you cannot check a price or a limit.

End with one line: does the first version cost nothing new, or how much? If it needs anything paid, suggest how to do without it in the first version.
```

## 5. Simplest design

**Purpose.** Choose the fewest moving parts that do the job, and fix where every file lives before any file is written.

**User stories**

- **Beginner.** As someone with a job I repeat every week, I want to know where I keep the prompt and where my input comes from, so that I can run it next week without thinking.
- **Advanced.** As a builder working with a coding agent, I want the folder layout fixed now, so that the agent does not move files later and break every link.
- **Expert.** As a team lead whose agents work unattended, I want every project in the same shape, so that anyone on the team can open any tool and find their way.

**What to expect.** About 5 minutes. Expect the design to be smaller than you imagined: often one saved prompt and one place to keep it.

**Proof you are done**

- Three lines: which assistant, where the files live, and what stays manual
- A short list a beginner could copy out: what goes in, what the AI does, what comes out, who checks it
- For a project folder: the layout check passes

**The gate.** Could a beginner draw it?

**Prompt to paste**

```
Design the simplest version of this tool that does the one job: [the one-sentence job].

Tell me in three lines: which assistant it runs in, where its files live (the instructions, my input, the results), and which steps I still do by hand.

Then draw it as a short list a beginner could copy: what goes in, what the AI does, what comes out, who checks it. Use the fewest parts that work. If you add a part, say what breaks without it.

This layout is now fixed. Tell me if anything later would force it to change.
```

## 6. Plan and front door

**Purpose.** Write the one-page plan and the first thing a user will see, before the tool exists. If the front door cannot be written, the tool is not understood yet.

**User stories**

- **Beginner.** As someone with a job I repeat every week, I want one page I can read in two minutes, so that I know what I am about to build and how I will test it.
- **Advanced.** As a builder working with a coding agent, I want the first screen of the README written first, so that the agent builds toward what a user will actually try.
- **Expert.** As a team lead whose agents work unattended, I want one worked example for each kind of request, so that a reviewer can compare a real result against a known good one.

**What to expect.** About 10 minutes. Expect to cut. If a section of the plan needs more than five lines, the scope has grown.

**Proof you are done**

- The plan template, filled in, on one page
- The first screen: a hook, and one thing a person can try in five minutes
- One worked example: an input, and the result you would be happy with

**The gate.** Is the beginner version fully described?

**Prompt to paste**

```
Write the one-page plan for this tool from what we have decided so far. Use these headings: the job, the user, what is out, the wow, what already exists, build or buy, cost, the design, the folder layout, the steps, the front door, the test, who reviewed it, gates, next three additions. Five lines at most under each. Mark anything you had to assume.

Then write the front door, the first thing a new user reads: one sentence that would make a stranger stop, two sentences on who it is for and what they get, and one thing they can try in five minutes.

Then write one worked example for each kind of request the tool handles differently (most first versions need one): a realistic input and the result I should expect. Say that each example is invented.
```

## 7. Review

**Purpose.** Have someone who is not the author read the plan and explain it back. You cannot see your own gaps, because you know what you meant.

**User stories**

- **Beginner.** As someone with a job I repeat every week, I want a second reader before I build, so that I find the confusing part while it is still one line to fix.
- **Advanced.** As a builder working with a coding agent, I want a fresh session to explain the plan back, so that I learn what my agent will misread.
- **Expert.** As a team lead whose agents work unattended, I want the review recorded with a name and a date, so that "reviewed" means something.

**What to expect.** About 5 minutes. Expect the summary to differ from your plan in one or two places. Those places are the fix list.

**Proof you are done**

- The reviewer's summary, in their own words
- A list of what was unclear, and what you changed
- Who reviewed it and when: a name, or "a fresh AI session"

**The gate.** Can someone else explain it back to you?

*In a chat with the coach:* Never review your own plan: you know what you meant. Until a person or a new chat has read it, the gate stays open, and the review goes under Test this next.

**Prompt for a new chat with no history**

```
You have never seen this project. Read the plan below and do three things.

1. Explain it back in five sentences: who it is for, what goes in, what comes out, how it is tested, and what it will not do.
2. List every place where you had to guess. Quote the line.
3. Name the one thing most likely to go wrong when someone builds this.

Do not improve the plan. Only report.

[paste the one-page plan]
```

## 8. Build and test

**Purpose.** Build the smallest version that does the job, then hand it to a stranger: a new AI session that has only your instructions. It finds what you cannot.

**User stories**

- **Beginner.** As someone with a job I repeat every week, I want to test my prompt in a new chat, so that I know it works without everything I said earlier.
- **Advanced.** As a builder working with a coding agent, I want a friction log from a fresh session, so that I fix what tripped it and not what I guess is wrong.
- **Expert.** As a team lead whose agents work unattended, I want several fresh sessions run at once with different requests, so that the faults are found before a person spends time on it.

**What to expect.** About 15 minutes for the first round. Expect a list of problems even when the job gets done. That list is the test working. Fix first every point that appears in two or more logs, then every blocking point. Then run it again.

**Proof you are done**

- The first version: instructions someone can paste, or a folder someone can open
- The result the fresh session produced, unedited
- Its list of where it had to guess, and a note of what you fixed

**The gate.** Did a fresh session finish the job, and have you read what it tripped on?

*In a chat with the coach:* In a chat you cannot run the test. Leave this gate open, and put the exact test under Test this next. Never state a test result you did not see.

**Prompt to build, in your working chat**

```
Build the first version of this tool from the plan: [paste the plan].

Build only the beginner version: instructions I can paste into a chat, with the steps to follow, the rules that never bend, and the format of the result. Keep the worked example beside the instructions, not inside them. Leave out everything listed under "what is out".

When you finish, tell me what you decided, what you assumed and what you did not check.
```

**Prompt to test, in a new chat with no history**

```
You have never seen this project. Follow the instructions below exactly as written, using only the input I give you. Do not ask me questions: where you would ask, decide, and note it.

Give me two things.
1. The result.
2. A numbered list of every place the instructions were unclear, contradicted themselves or left you guessing. Quote the line. Mark each one BLOCKING if a different guess would change the result, or MINOR if not.

[paste the instructions]

[paste one real input]
```

## 9. Grow

**Purpose.** Add one thing at a time, and only after the level below is in use. Small additions get reviewed. Big ones get waved through.

**User stories**

- **Beginner.** As someone with a job I repeat every week, I want to use the first version for two weeks before I change it, so that I add what I actually missed.
- **Advanced.** As a builder working with a coding agent, I want each addition as its own small change, so that I can review it in five minutes and undo it if it is wrong.
- **Expert.** As a team lead whose agents work unattended, I want the next level built only when the one below is used, so that we do not maintain features nobody opens.

**What to expect.** No fixed time: this step repeats. Expect most of your first list of additions to turn out unnecessary once you use the tool.

**Proof you are done**

- A list of the next three additions, smallest first
- For each addition made: what changed, who approved it, and a new test run
- Evidence the current level is in use: who used it, for what, and when

**The gate.** Is the level below in use before you build the next?

*In a chat with the coach:* In the first session nothing is in use yet. Leave this gate open.

**Prompt to paste**

```
I have used the first version of my tool [how many] times. Here is what happened: [what worked, what you still did by hand, what annoyed you].

From that, list the next three additions, smallest first. For each: what it changes, what could break, and how I would test it. Do not suggest anything I did not miss while using it.

Then build only the first one. Stop and show me before you start the second.
```

## The one-page plan

Fill this in as you go. Copy it into a document, or ask your chatbot to fill it in from your
answers. An agent finds the same template in each new project folder as `base/plan.md`.

```
Plan: [name of the tool]

Fill this in as you go through the nine steps. One page. If a section needs more than five
lines, the scope is too big.

**Think of it as:** [one everyday comparison]

**North Star:** [one sentence: who can do what, that they could not do before]

| Heading | Write here |
| --- | --- |
| The job | [One sentence] |
| The user | [One kind of person] |
| What is out | [The things you will not do in the first version] |
| The wow | [The one thing that makes people stop and look. Build it first] |
| What already exists | [Up to five options, each with a link and the date you looked. A longer list goes in `_build/landscape.md`] |
| Build or buy | [For each part of the first version: build it, buy it, or leave it as something done by hand] |
| Cost | [Each dependency, its price and its limit] |
| The design | [Which assistant, where files live, what stays manual] |
| The folder layout | [Decide it now and do not change it] |
| The steps | [What a user does, in order] |
| The front door | [The first thing a user sees, and the one thing they can try in five minutes] |
| The test | [A specific input, and what a good result looks like] |
| Who reviewed it | [A name, or "a fresh AI session", and the date] |
| Gates | [One line for each step so far: the gate, and pass, fail or open] |
| Next three additions | [Smallest first. One at a time] |
```

## Five rules that save the most time

1. **Name the wow first.** Decide the one thing that makes people stop, and build it first.
2. **Fix the layout before you build.** Moving files later breaks every link that points at them.
3. **Test in a fresh session early.** A stranger finds what the author cannot see.
4. **Say what a result really is.** A page built by hand is a reference. A page a chat made is an example.
5. **One addition, one change request.** Small changes get reviewed. Big ones get waved through.
