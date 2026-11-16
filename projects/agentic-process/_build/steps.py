"""The nine steps, written once. build.py turns this into base/PROCESS.md and the step cards in base/explainer.html.

Each step has: a purpose, three user stories (one for each level), what to expect, what proves the step is done,
the gate, and one or more prompts to paste. Times are estimates and the pages say so.
"""
COACH_URL = "https://raw.githubusercontent.com/bar181/practical-ai/main/projects/agentic-process/base/AI-INSTRUCTIONS.md"
COACH_FILE = "github.com/bar181/practical-ai: projects/agentic-process/base/AI-INSTRUCTIONS.md"
def pasted_prompt(idea): return f"Follow the build coach pasted above.\n\nMy idea: {idea}"
def coach_prompt(idea): return f"Read the build coach at {COACH_URL} and follow it. If you cannot open it, say so and stop: do not make up a coach of your own.\n\nMy idea: {idea}"
LEVELS = ("Beginner", "Advanced", "Expert")
WHO = ("someone with a job I repeat every week", "a builder working with a coding agent", "a team lead whose agents work unattended")

STEPS = [
 dict(n=1, name="Scope", gist="One user, one job", minutes=5,
  writes="One user, one job, what is out, and the one thing that will make people stop and look",
  purpose="Decide who the tool is for and the one job it does, before anything is built. A tool that does one job gets finished. A tool that does five gets rebuilt.",
  stories=("I want to say the job in one sentence, so that the AI builds that and nothing else.",
           "I want the scope written into the plan, so that the agent has something to refuse extra work against.",
           "I want one user and one job agreed before any agent starts, so that I am not reviewing five half-built features."),
  expect="About 5 minutes. Expect to drop something you wanted: the first answer is usually two or three jobs.",
  proof=("One sentence: who it is for, what goes in and what comes out",
         "Three things the first version will not do",
         "One test: a real input, and what a good result looks like"),
  gate="Can you say the job in one sentence?",
  prompts=(("Prompt to paste", """I want to turn a job I repeat into a small AI tool. Help me scope it.

Ask me up to two questions, one at a time. Then write:
1. The one user.
2. The one job, in one sentence: what goes in and what comes out.
3. Three things the first version will not do.
4. The one thing that would make someone stop and look.
5. One test: a specific input, and what a good result looks like.

If I describe more than one job, make me choose one and put the rest under "Later".

My job: [describe the job you repeat]"""),)),

 dict(n=2, name="Reuse check", gist="Does it already exist?", minutes=10,
  writes="What already does this: built in, free, common practice",
  purpose="Find out whether something you already have, or something free, does the job. The cheapest tool is the one you do not build.",
  stories=("I want to know whether my chatbot already does this, so that I do not spend a week rebuilding a built-in feature.",
           "I want links and dates for what exists, so that I can wrap an existing tool and not start from nothing.",
           "I want the reuse check written down, so that nobody on the team builds what we already pay for."),
  expect="About 10 minutes with web search, longer without. Expect to find something that does part of the job. Often the result is that you build less than you planned.",
  proof=("A short list of what exists, each with a link and the date you looked",
         "One line saying what is still left to build",
         "If nothing is left: a short guide to the existing tool, and you stop here"),
  gate="After what already exists, is there still something to build? If not, stop and write a guide to that thing.",
  prompts=(("Prompt to paste", """Before I build anything, check what already exists for this job: [the one-sentence job from step 1].

Look in this order: features already built into the assistant I use ([name it]), free and open-source tools, and how people who do this well usually do it. Search the web if you can. If you cannot, say so and list what I should look up.

Give me a table: the option, what it covers, what it costs, its limits, a link, and today's date. Do not invent a product or a price.

Then tell me plainly: does something existing do the whole job? If yes, tell me to stop, and write me a short guide to it. If no, say in one line what is left to build."""),)),

 dict(n=3, name="Outside help", gist="Build it or buy it", minutes=5,
  writes="Paid services for whatever is left. Do not pick a provider. Decide only build, buy or by hand for each part",
  purpose="For whatever is left, list the services you could pay for, so that the choice between building and buying is made on purpose.",
  stories=("I want to know what I would have to pay for, so that there are no surprises after I start.",
           "I want the options listed and not ranked, so that I choose with the cost and the way out in view.",
           "I want build-or-buy decided for the first version only, so that we do not sign up for a service before we know the tool is used."),
  expect="About 5 minutes. For most beginner tools the answer is that there is nothing to buy. Write that down and go on.",
  proof=("A list of paid options for what is left, or the words \"nothing to buy\"",
         "For each part of the tool: build it, buy it, or leave it as something done by hand"),
  gate="Do you know what you would build and what you would buy?",
  prompts=(("Prompt to paste", """Here is what is left to build after the reuse check: [paste the one line from step 2].

List any paid services that could do part of it. For each: what it does, the price, the free limit if there is one, and what happens to me if it closes or raises its price. List them evenly. Do not choose one for me, and do not invent a price: write "not confirmed" if you cannot check it.

Then, for each part of the tool, say whether the first version should build it, buy it, or leave it as something I do by hand."""),)),

 dict(n=4, name="Cost", gist="What it costs to run", minutes=5,
  writes="Every dependency of the first version, with its price and its limit",
  purpose="Put a price and a limit on everything the first version depends on. A tool people cannot afford to run is not finished.",
  stories=("I want to know it runs on the plan I already have, so that I can use it tomorrow.",
           "I want every dependency listed with its limit, so that the tool does not stop working in its first busy week.",
           "I want to know who pays, the builder or each user, so that the cost of rolling it out is known before we roll it out."),
  expect="About 5 minutes. Expect the first version to cost nothing new. If it needs something paid, that usually belongs in a later level.",
  proof=("A table: each thing the first version depends on, its price, its limit, and who pays",
         "One line: the first version costs nothing new, or it costs this much"),
  gate="Does the first version cost nothing, or an amount you accept?",
  prompts=(("Prompt to paste", """List everything the first version of this tool depends on: [describe the first version in a sentence, and name the assistant and the plan you use].

For each dependency give: what it is for, its price, its usage limit, and who pays (me, or each person who uses the tool). Write "not confirmed" where you cannot check a price or a limit.

End with one line: does the first version cost nothing new, or how much? If it needs anything paid, suggest how to do without it in the first version."""),)),

 dict(n=5, name="Simplest design", gist="Fewest parts, fixed layout", minutes=5,
  writes="Which assistant, where files live, what stays manual. The folder layout, fixed now",
  purpose="Choose the fewest moving parts that do the job, and fix where every file lives before any file is written.",
  stories=("I want to know where I keep the prompt and where my input comes from, so that I can run it next week without thinking.",
           "I want the folder layout fixed now, so that the agent does not move files later and break every link.",
           "I want every project in the same shape, so that anyone on the team can open any tool and find their way."),
  expect="About 5 minutes. Expect the design to be smaller than you imagined: often one saved prompt and one place to keep it.",
  proof=("Three lines: which assistant, where the files live, and what stays manual",
         "A short list a beginner could copy out: what goes in, what the AI does, what comes out, who checks it",
         "For a project folder: the layout check passes"),
  gate="Could a beginner draw it?",
  prompts=(("Prompt to paste", """Design the simplest version of this tool that does the one job: [the one-sentence job].

Tell me in three lines: which assistant it runs in, where its files live (the instructions, my input, the results), and which steps I still do by hand.

Then draw it as a short list a beginner could copy: what goes in, what the AI does, what comes out, who checks it. Use the fewest parts that work. If you add a part, say what breaks without it.

This layout is now fixed. Tell me if anything later would force it to change."""),)),

 dict(n=6, name="Plan and front door", gist="One page, and the first screen", minutes=10,
  writes="The steps a person follows, the first screen they see, one worked example for each kind of request it handles",
  purpose="Write the one-page plan and the first thing a user will see, before the tool exists. If the front door cannot be written, the tool is not understood yet.",
  stories=("I want one page I can read in two minutes, so that I know what I am about to build and how I will test it.",
           "I want the first screen of the README written first, so that the agent builds toward what a user will actually try.",
           "I want one worked example for each kind of request, so that a reviewer can compare a real result against a known good one."),
  expect="About 10 minutes. Expect to cut. If a section of the plan needs more than five lines, the scope has grown.",
  proof=("The plan template, filled in, on one page",
         "The first screen: a hook, and one thing a person can try in five minutes",
         "One worked example: an input, and the result you would be happy with"),
  gate="Is the beginner version fully described?",
  prompts=(("Prompt to paste", """Write the one-page plan for this tool from what we have decided so far. Use these headings: {PLAN_HEADINGS}. Five lines at most under each. Mark anything you had to assume.

Then write the front door, the first thing a new user reads: one sentence that would make a stranger stop, two sentences on who it is for and what they get, and one thing they can try in five minutes.

Then write one worked example for each kind of request the tool handles differently (most first versions need one): a realistic input and the result I should expect. Say that each example is invented."""),)),

 dict(n=7, name="Review", gist="Someone else explains it back", minutes=5,
  writes="Someone who is not the author reads the plan",
  purpose="Have someone who is not the author read the plan and explain it back. You cannot see your own gaps, because you know what you meant.",
  stories=("I want a second reader before I build, so that I find the confusing part while it is still one line to fix.",
           "I want a fresh session to explain the plan back, so that I learn what my agent will misread.",
           "I want the review recorded with a name and a date, so that \"reviewed\" means something."),
  expect="About 5 minutes. Expect the summary to differ from your plan in one or two places. Those places are the fix list.",
  proof=("The reviewer's summary, in their own words",
         "A list of what was unclear, and what you changed",
         "Who reviewed it and when: a name, or \"a fresh AI session\""),
  gate="Can someone else explain it back to you?",
  prompts=(("Prompt for a new chat with no history", """You have never seen this project. Read the plan below and do three things.

1. Explain it back in five sentences: who it is for, what goes in, what comes out, how it is tested, and what it will not do.
2. List every place where you had to guess. Quote the line.
3. Name the one thing most likely to go wrong when someone builds this.

Do not improve the plan. Only report.

[paste the one-page plan]"""),)),

 dict(n=8, name="Build and test", gist="A stranger tests it", minutes=15,
  writes="The beginner version. Then a test by a fresh AI session that has only your instructions",
  purpose="Build the smallest version that does the job, then hand it to a stranger: a new AI session that has only your instructions. It finds what you cannot.",
  stories=("I want to test my prompt in a new chat, so that I know it works without everything I said earlier.",
           "I want a friction log from a fresh session, so that I fix what tripped it and not what I guess is wrong.",
           "I want several fresh sessions run at once with different requests, so that the faults are found before a person spends time on it."),
  expect="About 15 minutes for the first round. Expect a list of problems even when the job gets done. That list is the test working. Fix first every point that appears in two or more logs, then every blocking point. Then run it again.",
  proof=("The first version: instructions someone can paste, or a folder someone can open",
         "The result the fresh session produced, unedited",
         "Its list of where it had to guess, and a note of what you fixed"),
  gate="Did a fresh session finish the job, and have you read what it tripped on?",
  prompts=(("Prompt to build, in your working chat", """Build the first version of this tool from the plan: [paste the plan].

Build only the beginner version: instructions I can paste into a chat, with the steps to follow, the rules that never bend, and the format of the result. Keep the worked example beside the instructions, not inside them. Leave out everything listed under "what is out".

When you finish, tell me what you decided, what you assumed and what you did not check."""),
           ("Prompt to test, in a new chat with no history", """You have never seen this project. Follow the instructions below exactly as written, using only the input I give you. Do not ask me questions: where you would ask, decide, and note it.

Give me two things.
1. The result.
2. A numbered list of every place the instructions were unclear, contradicted themselves or left you guessing. Quote the line. Mark each one BLOCKING if a different guess would change the result, or MINOR if not.

[paste the instructions]

[paste one real input]"""))),

 dict(n=9, name="Grow", gist="One addition at a time", minutes=0,
  writes="One addition, one change request. What you learned",
  purpose="Add one thing at a time, and only after the level below is in use. Small additions get reviewed. Big ones get waved through.",
  stories=("I want to use the first version for two weeks before I change it, so that I add what I actually missed.",
           "I want each addition as its own small change, so that I can review it in five minutes and undo it if it is wrong.",
           "I want the next level built only when the one below is used, so that we do not maintain features nobody opens."),
  expect="No fixed time: this step repeats. Expect most of your first list of additions to turn out unnecessary once you use the tool.",
  proof=("A list of the next three additions, smallest first",
         "For each addition made: what changed, who approved it, and a new test run",
         "Evidence the current level is in use: who used it, for what, and when"),
  gate="Is the level below in use before you build the next?",
  prompts=(("Prompt to paste", """I have used the first version of my tool [how many] times. Here is what happened: [what worked, what you still did by hand, what annoyed you].

From that, list the next three additions, smallest first. For each: what it changes, what could break, and how I would test it. Do not suggest anything I did not miss while using it.

Then build only the first one. Stop and show me before you start the second."""),)),
]

TOTAL_MINUTES = sum(s["minutes"] for s in STEPS)   # steps 1 to 8; step 9 repeats

# How the coach (a chat, base/AI-INSTRUCTIONS.md) and the skill (an agent, level-2-files) do each step.
# The gate question is the same everywhere: STEPS[n]["gate"]. The note says how that reader answers it.
COACH = {
 1: ("Find one user and one job. List what is out. Ask what would make people stop and look. Write one test: a specific input and what a good result looks like", ""),
 2: ("Look for what already does this: features of the assistant they use, free tools, common practice",
     "If the answer is no, stop: hand over a short guide to that thing and the note, in place of the plan. The assistant they already use counts only if one plain sentence typed into it gives a result the person would send unchanged. You cannot know that unseen: go on, and put \"try one plain sentence first\" under Test this next"),
 3: ("For whatever is left, list paid options with what each covers and how it charges. Do not pick a provider: decide only build, buy or by hand for each part", ""),
 4: ("List every dependency of the first version with its price and its limit",
     "With prices not checked, the gate passes only if the first version buys nothing new. Say so"),
 5: ("Say which assistant, where files live, and what stays manual. Propose a folder layout and fix it", ""),
 6: ("Write the steps a user follows, the first thing they see, and one worked example for each kind of request the tool handles differently. Most first versions need one", ""),
 7: ("Ask who will read the plan. Give them the review prompt: paste the plan into a new chat with no history and ask it to explain the plan back and list where it had to guess",
     "Never review your own plan: you know what you meant. Until a person or a new chat has read it, the gate stays open, and the review goes under Test this next"),
 8: ("Write the first version: usually a prompt or a set of instructions, plus one worked example. Then tell the person exactly how to test it in a fresh chat that has only those instructions",
     "In a chat you cannot run the test. Leave this gate open, and put the exact test under Test this next. Never state a test result you did not see"),
 9: ("List the next three additions, smallest first. One at a time",
     "In the first session nothing is in use yet. Leave this gate open"),
}
SKILL = {
 1: ("One user, one job, what is out, the wow, and one test with a specific input and a good result", "The plan's job line is one sentence"),
 2: ("Search in the order under \"Step 2 in detail\" below. Put up to five options in the plan, a longer list in `_build/landscape.md`", "If something does the whole job, stop and write a guide to it. Instructions written for an assistant the user already has count as building, unless one plain sentence already gives a result they would send unchanged"),
 3: ("List paid options for what is left. Do not pick a provider: decide only build, buy or by hand for each part, and write it under \"Build or buy\" in the plan", ""),
 4: ("Every dependency of the first version with its price and limit", ""),
 5: ("Which assistant, where files live, what stays manual. Make the folder from the template (see \"Make the folder\")", "The design is three lines in the plan. In the new folder, `python3 _build/checks/gates.py .` passes layout and links. `filled` fails until step 6"),
 6: ("Fill `base/plan.md`. Write the README's hook, its \"Try it in five minutes\" section and at least one worked example: one for each kind of request the beginner version handles differently. Most first versions have one or two", "The `filled` gate passes: no blanks are left from the template"),
 7: ("A person, or a fresh session given only `base/plan.md`, explains it back", "The reviewer's summary matches the plan. With neither available, the gate stays open: say so and go on to step 8, whose test also reads the plan"),
 8: ("Build the beginner version. Run the fresh-session test (see \"The fresh-session test\")", "The fresh session finished the job. Its friction log has been read and the recurring points fixed"),
 9: ("One addition at a time, each its own change request", "Someone other than the builder has used the level below"),
}
