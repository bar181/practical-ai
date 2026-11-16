"""The Agentic Process course, written once. build.py turns it into base/course.html and the course outline in the README.

A lesson that teaches one of the nine steps names it with step=N: its purpose, prompt, proof and gate then come from
steps.py, so the course and the process cannot drift apart. chat= says where the learner works: "coach" (the chat
from lesson 1.3, kept open) or "new" (a new chat that remembers nothing).

A module's time is worked out, not typed: the lecture, plus its core lessons, plus five minutes for the check.
In class the lessons are the lab. On your own they are the course. Lessons marked optional are not counted.

Slides are (kind, title, body, notes). Kinds: title, points, two (body is left title, left points, right title,
right points), diagram (body names a diagram in pages.py), quote, lab, recap. Notes are what the instructor says,
starting with the minutes for that slide and giving any answers the room should reach. {LAB} in a note becomes the
minutes of the module's core lessons.
"""
from steps import coach_prompt, pasted_prompt

G = "https://github.com/bar181/practical-ai/blob/main/projects/agentic-process/"
MEMORY_OFF = ("The chat must not remember you. In ChatGPT and Gemini, start a Temporary Chat. In Claude, start an "
              "incognito chat. In another chatbot, turn off memory and custom instructions first.")
PRIVACY = "Use invented or anonymised notes unless your workplace allows this chatbot for that kind of data."
GOOD = ("What good looks like: a worked example (an invented Monday email tool)", G + "base/examples/monday-email.md")

COURSE = dict(
 title="Build the right AI tool",
 subtitle="The Agentic Process course",
 purpose="Learn to turn a job you repeat into a small AI tool that someone else can use, and to prove it works before anyone relies on it.",
 audience="Business owners, employees and students who use a chatbot at work. No code is needed. Two optional lessons in Module 5 are for people who build with a coding agent.",
 outcomes=[
  "Say what a tool does in one sentence: one user, one input, one result.",
  "Check what already exists, and decide whether to stop, wrap it or build.",
  "Write a one-page plan and the first screen a user will see, before anything is built.",
  "Test your tool with a stranger, a fresh chat that has only your instructions, and read what it tripped on.",
  "Plan how the tool grows, one addition at a time, and know which level of the process fits your work.",
 ],
 needs=["A chatbot you already use, such as ChatGPT, Claude, Gemini or Copilot", "One job you do on your own every week that starts from a blank page", "About {HOURS} hours, in one day or over five weeks, plus the capstone"],
 honest="This course was written on 16 November 2026 and has not yet been taught. Every time on it is an estimate. The process has been tested by AI sessions, all in Claude, and by nobody else yet.",
)

MODULES = [
 dict(n=1, title="Why process beats prompts", lecture=15,
  purpose="See why an AI that builds fast moves the expensive mistakes earlier, and meet the nine steps that catch them.",
  outcomes=["Explain why a good prompt is not enough to get the right tool", "Name the four stages and what a gate is", "Run the coach on a real job, on the short path"],
  slides=[
   ("title", "Why process beats prompts", ["Module 1 of 5"], "1 min. Welcome. One idea today: when building gets cheap, deciding what to build becomes the expensive part. By the end of this module everyone will have run the process once on a job of their own."),
   ("points", "An AI will build whatever you ask", ["Quickly", "Confidently", "Without asking whether it is the right thing"], "2 min. Ask the room: who has had an answer from an AI that was polished and wrong? Take two examples. Expect: an email in the wrong tone, a report that answered a different question, a formula that looked right and was not. The point: the AI did exactly what it was asked. The asking was the problem."),
   ("diagram", "Where the costly mistakes are made", "cost", "2 min. An illustration, not data. Before AI, most of the effort went into building, so that is where people planned and checked. Now building is quick, so the costly mistakes happen earlier, in deciding: the wrong job, a tool that already existed, a tool only you can use."),
   ("quote", "Think of it as a building site with an inspector", ["You agree the drawing before you pour concrete. Nothing moves to the next stage until the current one is signed off."], "1 min. The picture for the whole course. Come back to it whenever someone is lost. The inspector does not slow the build down. The inspector stops you pouring concrete in the wrong place."),
   ("diagram", "Nine steps, four stages", "stages", "3 min. Decide is steps 1 to 4: is it worth building? Design is 5 to 7: the plan before the build. Build and test is step 8: a stranger tests it. Grow is step 9: one addition at a time. Do not teach each step now. Modules 2 to 5 take one stage each."),
   ("points", "A gate is a question you answer before you go on", ["Step 1: can you say the job in one sentence?", "Step 2: after what already exists, is there still something to build?", "Step 8: did a fresh chat finish the job, and have you read what it tripped on?"], "2 min. Every gate is worded so that yes means go on; no means fix the step. Ask: what would make the step 2 answer no? Expect: a built-in feature or a free tool that already does the whole job. That is a good result: you stop and saved a week."),
   ("two", "Three levels, one process", ("Beginner", ["Any chatbot", "Paste one prompt, the coach", "Leave with a plan, a prompt and a test"], "Advanced and Expert", ["A coding agent and a repository", "One skill folder with its own checks", "Agents that work unattended, with gates"]), "2 min. Most of the room will stay at Beginner, and that is the point: the same nine steps work in a chat window. Module 5 shows the other two levels in optional lessons."),
   ("lab", "Your turn: run the coach", ["Paste the coach prompt into your chatbot", "Change the last line to your job", "Say yes to the short path", "At the plan, stop and ask: What did you assume?"], "Lessons 1.1 to 1.3 are the lab: about {LAB} minutes. Walk the room. If a chatbot cannot open the link, the learner opens the coach on GitHub, copies it, pastes it, and types: Follow the build coach pasted above."),
   ("recap", "Take away", ["Building is cheap. Deciding is not.", "Nine steps, four stages, a gate after each", "The coach runs it in any chatbot"], "1 min. Next module: Decide. Everyone keeps the coach chat open: Modules 2 and 3 continue in it."),
  ],
  lessons=[
   dict(id="1-1", title="The problem: the wrong thing, built well", minutes=8,
    objective="Recognise the three expensive mistakes an AI makes before the first line is written.",
    body=["**The wrong job.** You asked for five things and got a tool that does none of them well.",
          "**It already existed.** A built-in feature or a free tool already did the job.",
          "**Nobody else can use it.** It works in your chat, with everything you said earlier, and breaks for anyone else."],
    do=["Read the three mistakes above.", "Think of one AI result you got this month that was polished and wrong. Write one line on why.", "Decide which of the three mistakes it was."],
    proof=["One line about a real AI result that was polished and wrong", "Which of the three mistakes it was"]),
   dict(id="1-2", title="The North Star and the nine steps", minutes=10,
    objective="Know what the process is for and how its nine steps are grouped.",
    do=["Open the North Star page and read the North Star and the purpose.", "Open the guide and scroll to the diagram of four stages.", "Open step 1's card in the guide and find its purpose, its proof, its prompt and its gate."],
    links=[("The North Star page", "north-star.html"), ("The guide", "explainer.html")],
    proof=["The North Star in your own words, in one sentence", "The four stages, from memory"]),
   dict(id="1-3", title="Your first run: the coach, on the short path", minutes=15,
    objective="Run the process once on a small job of your own, and keep the chat: the next lessons continue in it.",
    do=["Pick one job you do on your own every week that starts from a blank page. " + PRIVACY,
        "Copy the prompt below into your chatbot and change the last line to your job.",
        "Say yes when the coach offers the short path.",
        "Answer its questions. When it shows you the one-page plan, stop there and ask it: What did you assume?",
        "Save the plan and keep this chat open. Lessons 2.1 to 4.1 continue in it."],
    prompt=coach_prompt("[one job you do on your own, in one sentence]"),
    fallback=pasted_prompt("[one job you do on your own, in one sentence]"),
    links=[GOOD],
    proof=["A one-page plan for your own job", "The coach's answer to: What did you assume?"]),
  ],
  quiz=[
   ("Building with AI got much cheaper. Where are the costly mistakes made now?", ["In the code, because AI code is full of bugs", "Before the first line: choosing the job, checking what exists, making it usable by others", "After launch, when users complain"], 1, "Building is quick now, so the costly errors are in deciding what to build."),
   ("What is a gate?", ["A review meeting with your manager at the end of each stage", "A question you answer before you go on, worded so that yes means go on", "A checklist you fill in once the tool is finished"], 1, "Each step ends with a gate question. No means fix the step."),
   ("The coach offers the short path. When is that right?", ["Whenever you are short of time", "When one person turns one kind of input into one result in a chat", "When the job is new to you"], 1, "Shared files, several users or anything paid take all nine steps."),
  ],
  assignment="Run the coach on your own job, on the short path, and save the one-page plan and what it assumed. Keep the chat."),

 dict(n=2, title="Decide: is it worth building?", lecture=15,
  purpose="Before anything is built, name one job, check what already does it, and know what it would cost.",
  outcomes=["Cut a job down to one user and one result", "Run a reuse check in the right order, and stop when something already does the job", "List what the first version depends on and what it costs"],
  slides=[
   ("title", "Decide: is it worth building?", ["Module 2 of 5 · Steps 1 to 4"], "1 min. The cheapest module in the course, and the one that saves most. Every minute here saves an hour later."),
   ("two", "One user, one job", ("Too wide", ["Help me with sales emails, proposals and follow-ups", "Five jobs, so none done well"], "One job", ["Turn my call notes into a follow-up email for that client", "One input, one result, one person"]), "3 min. Ask three people to read their job aloud in one sentence. Listen for 'and': it usually means two jobs. The fix: keep the one they would miss most on Monday; the others go under Next."),
   ("points", "Write down what is out", ["Three things the first version will not do", "The rest go under Next, not into the build", "Name the one thing that makes people stop and look"], "2 min. What is out is what the AI will refuse when someone asks for more later. The wow is the one thing built first. Ask: what is one thing your tool will not do? Expect: send anything on its own, handle more than one kind of input, cover other people's work."),
   ("diagram", "The reuse check, cheapest first", "reuse", "3 min. Look in this order and stop as soon as something does the whole job. Built in: what your chatbot already does. Open source. How people who do this well already do it. Paid providers last. Every option gets a link and the date you looked."),
   ("quote", "Stopping is a win", ["If something already does the whole job, you write a two-line guide to it and you are done. You just saved a week."], "1 min. The hardest idea to sell to people who like building. When it happens in class, celebrate it out loud."),
   ("two", "Build, buy or do by hand", ("For each part", ["Build it", "Buy it", "Leave it as something you do by hand"], "For the first version", ["Usually: build a prompt", "Buy nothing", "Do the checking by hand"]), "2 min. Step 3 is not choosing a supplier. It is deciding, part by part, what the first version does and does not do."),
   ("points", "What it costs to run", ["Every dependency, its price and its limit", "Who pays: you, or each person who uses it", "Expect the first version to cost nothing new"], "2 min. If the first version needs something paid, it usually belongs in a later level. Write 'not confirmed' for any price you could not check."),
   ("lab", "Your turn: steps 1 to 4", ["Scope: one sentence, three things out, one test", "Reuse check: built in first", "Build or buy for each part", "Cost: one line"], "Lessons 2.1 to 2.3 are the lab: about {LAB} minutes, in the coach chat from Module 1. Afterwards ask two people whether their reuse check found something that does the whole job."),
   ("recap", "Take away", ["One user, one job, written in one sentence", "Check what exists before you build", "The first version should cost nothing new"], "1 min. Next module: Design, the plan before the build."),
  ],
  lessons=[dict(id="2-1", step=1, minutes=10, chat="coach"), dict(id="2-2", step=2, minutes=15, chat="coach"), dict(id="2-3", step=(3, 4), minutes=10, title="Outside help and cost", chat="coach")],
  quiz=[
   ("Which job is scoped well enough for step 1?", ["Write all my client emails for me", "Turn my call notes into a follow-up email for that client", "Help me with sales emails and proposals"], 1, "One user, one input, one result. The others are several jobs, or have no clear input."),
   ("Your reuse check finds a free tool that does the whole job. What now?", ["Build your own anyway, so it fits your style exactly", "Stop, and write a short guide to that tool", "Keep searching for a better paid tool"], 1, "Stopping is a win. The gate exists to save you from building what already exists."),
   ("In what order do you look in the reuse check?", ["Paid providers first, because they are the most complete", "Built in, open source, established practice, then providers", "Search the web first, then ask colleagues"], 1, "Cheapest first, and stop as soon as something does the whole job."),
  ],
  assignment="Take your job through steps 1 to 4 and add the results to your plan: the job in one sentence, what is out, what already exists (with links and dates), build or buy, and cost."),

 dict(n=3, title="Design: the plan before the build", lecture=15,
  purpose="Choose the fewest parts, write the plan and the first screen before the tool exists, and have a stranger explain it back.",
  outcomes=["Design the simplest version that does the job", "Write a one-page plan and a front door", "Get a review from a stranger and turn it into a fix list"],
  slides=[
   ("title", "Design: the plan before the build", ["Module 3 of 5 · Steps 5 to 7"], "1 min. Three steps, all on paper. Nothing is built in this module, and that is deliberate."),
   ("points", "The fewest parts that do the job", ["Which assistant it runs in", "Where its files live: instructions, input, results", "What stays manual"], "2 min. Most first versions are one saved prompt and one place to keep it. Ask: where will you keep your prompt next week? Expect: a note, a document, a saved project in their chatbot."),
   ("quote", "Fix the layout before you build", ["Every file you write afterwards points at other files. Moving them later breaks those links, and you pay again each time the shape changes."], "2 min. For a beginner the layout is where the prompt lives and where the input comes from. For a builder it is the folder structure. Either way, decide it now and do not change it."),
   ("diagram", "The one-page plan", "plan", "3 min. Fifteen headings, five lines at most under each. The short path uses the seven highlighted. If a section needs more than five lines, the scope has grown: go back to step 1."),
   ("points", "Write the front door first", ["One sentence a stranger would stop for", "Who it is for and what they get", "One thing they can try in five minutes"], "2 min. If you cannot write the first screen, you do not understand the tool yet. Ask one person to read their front-door sentence aloud. The room says whether they would try it."),
   ("two", "Why you cannot review your own plan", ("You", ["Know what you meant", "Read past the gaps"], "A stranger", ["Has only the page", "Trips on every gap"]), "2 min. The core habit of the course. A new chat that remembers nothing is a free, patient stranger. It cannot read your mind, which is exactly what makes it useful."),
   ("lab", "Your turn: plan, then a stranger reads it", ["Simplest design and the plan, in the coach chat", "Then open a new chat that remembers nothing", "Paste the review prompt and your plan", "Where it had to guess is your fix list"], "Lessons 3.1 to 3.3 are the lab: about {LAB} minutes. Check the review chat really is new: a Temporary Chat in ChatGPT or Gemini, an incognito chat in Claude. Ask one person to read out the first thing the stranger guessed."),
   ("recap", "Take away", ["Fewest parts; fix the layout now", "Plan and front door before the tool", "A stranger reviews it, never you"], "1 min. Next module: Build and test. We build the smallest version and let a stranger break it."),
  ],
  lessons=[dict(id="3-1", step=5, minutes=10, chat="coach"), dict(id="3-2", step=6, minutes=15, chat="coach", links=[GOOD]), dict(id="3-3", step=7, minutes=10, chat="new")],
  quiz=[
   ("Why fix the folder layout before anything is built?", ["So the project looks professional to others", "Every file points at other files; moving them later breaks those links", "Because the AI cannot create folders later"], 1, "You pay for the move again each time the shape changes."),
   ("What do you write before the tool exists?", ["A full list of every feature it might need", "The one-page plan and the first screen a user sees", "The instructions, so you can test them early"], 1, "If the front door cannot be written, the tool is not understood yet."),
   ("Who should review your plan?", ["You, slowly and carefully, the next morning", "Someone who is not the author, such as a new chat that remembers nothing", "The same chat that wrote it, asked to be critical"], 1, "You cannot see your own gaps, because you know what you meant. Nor can the chat that wrote it."),
  ],
  assignment="Finish your one-page plan and front door, run the review prompt in a new chat that remembers nothing, and fix every place it had to guess."),

 dict(n=4, title="Build and test: let a stranger break it", lecture=15,
  purpose="Build the smallest version, hand it to a fresh chat that has only your instructions, and fix what it trips on.",
  outcomes=["Build only the beginner version, with one worked example", "Run a fair fresh-chat test", "Sort a friction log into blocking and minor, and fix in the right order"],
  slides=[
   ("title", "Build and test: let a stranger break it", ["Module 4 of 5 · Step 8"], "1 min. This is where most AI work stops: it works for me, so it works. Today we find out whether it works for someone else."),
   ("points", "Build the smallest version", ["Instructions someone can paste", "The steps, the rules that never bend, the format of the result", "One worked example, kept beside the prompt"], "2 min. Leave out everything under 'what is out'. When the AI finishes, ask it what it decided, what it assumed and what it did not check."),
   ("diagram", "The fresh-chat test", "test", "3 min. A new chat that remembers nothing gets only your instructions and one real input. It does the job and lists every place it had to guess. You do not help it. You read the list before the result."),
   ("two", "Blocking or minor", ("Blocking", ["A different guess would change the result", "Fix it"], "Minor", ["The result would be the same", "Note it; fix it if cheap"]), "2 min. Every point in the log is marked one or the other. This stops people rewriting everything because of one complaint. Example: 'It did not say what tone to use' is blocking for an email tool."),
   ("points", "Fix in this order", ["First: every point that appears in two or more logs", "Then: every blocking point", "Then run a second round"], "2 min. One log can be noise from that request or that session. The same point twice means the instructions are wrong."),
   ("quote", "The author is the worst reader of their own instructions", ["A typical find: one step says stop if the answer is yes, while every other step says go on if yes. The author reads past it every time. A stranger trips on it at once."], "2 min. Ask: what would a stranger trip on in your instructions? Take two guesses, then say: stop guessing and run the test."),
   ("lab", "Your turn: build and test", ["Build the beginner version, in the coach chat", "Open a new chat that remembers nothing", "Paste the test prompt, your instructions and one input", "Mark each point blocking or minor, and fix"], "Lessons 4.1 to 4.3 are the lab: about {LAB} minutes. Make sure every test chat is new: memory or custom instructions can carry the first session over and make the test pass for the wrong reason."),
   ("recap", "Take away", ["Smallest version, one worked example", "A stranger tests it; you do not help", "Fix repeats first, then blockers, then test again"], "1 min. Next module: how the tool grows, and the levels above Beginner."),
  ],
  lessons=[dict(id="4-1", step=8, minutes=15, title="Build the smallest version", part="build", chat="coach"),
           dict(id="4-2", step=8, minutes=15, title="The fresh-chat test", part="test", chat="new"),
           dict(id="4-3", title="Read the friction log and fix", minutes=15,
            objective="Turn a friction log into a short fix list in the right order, and test again.",
            do=["Read the friction log before the result.", "Mark each point BLOCKING (a different guess would change the result) or MINOR.",
                "Fix first every point that appears in two or more logs, then every blocking point. Make the fixes in the coach chat.",
                "Run the test again, in another new chat that remembers nothing.", "Write one line: did round 2 find fewer blocking points?"],
            links=[GOOD],
            proof=["A friction log with each point marked", "The fixes you made", "A second round, and how many blocking points it found"])],
  quiz=[
   ("A fresh chat finishes the job and lists twelve problems. Did the test pass?", ["No: twelve problems means the instructions failed", "Yes: it finished, and the twelve problems are the next hour of work", "Only if fewer than three of them are blocking"], 1, "The list is the test working. The gate asks whether it finished and whether you read the list."),
   ("What makes a point blocking?", ["The tester called it important", "A different guess would change the result", "It appears near the start of the instructions"], 1, "Minor points would not change the result."),
   ("Why must the test chat remember nothing of your session?", ["So the test runs faster", "Otherwise it carries what you said earlier and passes for the wrong reason", "So the provider does not keep your notes"], 1, "A stranger has only your instructions."),
  ],
  assignment="Build your beginner version, run two rounds of the fresh-chat test, and keep both friction logs unedited."),

 dict(n=5, title="Grow, and work at your level", lecture=12,
  purpose="Plan how the tool grows once it is in use, and see how the same steps run with a coding agent and with agents that work unattended.",
  outcomes=["Plan the next addition from real use, not ideas", "Know what the skill folder does for someone with a coding agent (optional lesson)", "Know what gates and an unattended run add, and what a person still approves (optional lesson)"],
  slides=[
   ("title", "Grow, and work at your level", ["Module 5 of 5 · Step 9, Advanced and Expert"], "1 min. Two halves. First, how a tool grows without falling apart. Second, the same process for people who build with coding agents: optional for everyone else."),
   ("points", "One addition at a time", ["Use the first version for two weeks first", "Add only what you actually missed", "One addition, one change you can review in five minutes"], "2 min. Many of the additions people plan turn out to be unnecessary once they use the tool. Small additions get reviewed. Big ones get waved through, and that is how tools break."),
   ("diagram", "The levels", "levels", "2 min. Beginner is the chat window. Advanced is a coding agent with one skill folder that carries its own checks. Expert is agents that run the steps unattended, with gates a script checks. At every level a person approves anything that is merged, posted, sent, paid or published."),
   ("points", "Advanced: one folder, any repository", ["Copy the skill folder into your agent's skills", "The agent stops at each gate and waits for you", "A new project carries its own four checks"], "2 min. For developers in the room. The checks are layout, links, filled (the plan has no blanks) and built (the instructions have no blanks). Everyone else can skip lesson 5.2."),
   ("diagram", "Expert: an unattended run", "unattended", "2 min. The agent runs steps 1 to 6, prepares the tests and stops. A separate session that starts and directs the others, the orchestrator, opens a fresh session for each test. The agent reads the logs, fixes, runs its gates again and hands back. A person reads the hand-back and decides."),
   ("lab", "Capstone: your tool, steps 1 to 8", ["Take one real job through steps 1 to 8", "Hand in the plan, the first version, two friction logs and the note", "Plan step 9: use it for two weeks, then decide"], "2 min to set it. Show the capstone page and its rubric. Lesson 5.1 is the lab now, about {LAB} minutes; 5.2 and 5.3 are optional. Ask learners to send the friction logs: they tell you more than the tool."),
   ("recap", "Take away", ["Grow from use, one addition at a time", "Same steps with a coding agent, plus checks", "Agents can work alone; a person approves"], "1 min. That is the course. The stranger's list is the most useful thing they will make."),
  ],
  lessons=[dict(id="5-1", title="Plan the next addition", minutes=10, step_ref=9,
            objective="Plan how your tool will grow, so that the next change comes from real use and not from ideas.",
            do=["From your two friction logs and what you still did by hand, list three additions, smallest first.", "For each, write what it changes, what could break, and how you would test it.",
                "Put a date in your calendar two weeks from now. Use the tool until then, and build nothing new.",
                "On that date, keep only the additions you actually missed. Build the first one only, as its own small change, with the prompt below."],
            prompt_from_step=9,
            proof=["Three additions, smallest first, each with what could break", "A date two weeks from now to decide"]),
           dict(id="5-2", title="Advanced: the skill folder in your repository", minutes=35, optional=True, track="Advanced",
            objective="Start a project with a coding agent, in your own repository, and run its checks.",
            do=["Copy the skill folder into your agent's skills (for Claude Code, .claude/skills/; create the folder if it is missing).", "Tell the agent: Use the agentic-process skill. Start at step 1. Give it your one-sentence job.", "Answer its questions. It stops at every gate.", "At step 5 it makes the project folder and prints the command that checks it. Run it.", "Expect two checks to fail until later: filled until step 6, built until step 8."],
            links=[("The Advanced level", "https://github.com/bar181/practical-ai/tree/main/projects/agentic-process/level-2-files")],
            proof=["A project folder in your repository", "The check output, with layout and links passing"]),
           dict(id="5-3", title="Expert: gates and unattended agents", minutes=15, optional=True, track="Expert",
            objective="Know how agents run the process alone, and where a person must still decide.",
            do=["Read the worked unattended run: an agent with only the skill folder, in an empty repository.", "Find the moment it stopped for the fresh-session tests, and who ran them.", "Find the gate it added of its own.", "Write the one decision in your work that an agent must never make alone."],
            links=[("The worked unattended run", G + "base/examples/unattended-run.md"), ("The Expert level", "https://github.com/bar181/practical-ai/tree/main/projects/agentic-process/level-3-files")],
            proof=["Where the agent stopped, and why", "One decision that stays with a person"])],
  quiz=[
   ("When should you build the next addition?", ["Straight after the first version, while the ideas are fresh", "After two weeks of use, and only for something you missed", "When you have collected five ideas"], 1, "Grow from use, one addition at a time."),
   ("What does a new project made from the skill folder carry?", ["A copy of the whole Practical AI repository", "Its own checks: layout, links, filled and built", "A licence key for the coding agent"], 1, "So it works in any repository."),
   ("In an unattended run, what must a person still do?", ["Watch the agent the whole time", "Approve anything that is merged, posted, sent, paid or published", "Write the first version by hand"], 1, "Agents can work alone. A person decides."),
  ],
  assignment="Start the capstone: one real job through steps 1 to 8, with step 9 planned."),
]

CAPSTONE = dict(
 title="Capstone",
 name="Your tool, steps 1 to 8",
 purpose="Take one real job of your own through steps 1 to 8, hand in a first version a stranger has tested, and plan step 9.",
 deliver=["The one-page plan, every heading filled", "The first version: instructions someone can paste, with one worked example", "Two friction logs from fresh-chat tests, unedited", "A note with four headings: Decided. Assumed. Not checked. Test this next.", "Step 9 planned: three additions, smallest first, and the date you will decide"],
 stop="If your reuse check finds something that already does the whole job, that passes steps 1 to 4: hand in the reuse table and a two-line guide to that tool, then take a second job through the steps for the rest.",
 alone="Taking this on your own? Mark it yourself with the rubric, or paste your hand-in and the rubric into a new chat and ask it to mark each row and say why.",
 rubric=[("Scope", "One user and one job in one sentence; three things out", 15),
         ("Reuse check", "At least three options with links and dates; a clear stop, wrap or build", 15),
         ("Build or buy, and cost", "A decision for each part; every dependency with its price or \"not confirmed\"", 5),
         ("Plan and front door", "Every heading filled; a front door a stranger would try", 15),
         ("Fresh-chat test", "Two rounds in chats that remember nothing, logs unedited, each point marked blocking or minor", 25),
         ("Fixes", "Repeats fixed first, then blockers; round 2 shows fewer blocking points", 15),
         ("Honesty", "The note says what was assumed and what was not checked", 10)],
)

INSTRUCTOR = dict(
 how="In class, each module is the lecture, then its lessons as the lab, then the three-question check. On their own, learners take the lessons in order. Lessons 2.1 to 4.1 continue in the coach chat from lesson 1.3; the two tests, in lessons 3.3 and 4.2, need a new chat that remembers nothing.",
 formats=[("One day", "Modules 1 to 5 back to back, with three short breaks; the capstone due two weeks later"),
          ("Five weeks", "One module a week, about an hour each; the assignment between sessions; the capstone due two weeks after week 5. Step 9 is planned, not marked"),
          ("A 30-minute taster", "Module 1's slides 1 to 6, then lesson 1.3 on the short path, then the review prompt from lesson 3.3 in a new chat")],
 before=["Ask each learner to bring one job they do on their own every week that starts from a blank page", "Post the coach prompt in the class chat so nobody types it from the screen", "Check how to start a chat that remembers nothing in the chatbots your learners use", "Rehearse from paper: print a module page and every slide prints with its notes"],
 present="Put the slides full screen on the projector, and press Presenter window to open the notes, the next slide and a timer on your own screen. Both windows move together. Each note starts with the minutes for that slide.",
 watch=[("A learner describing three jobs", "\"Which one would you miss most on Monday? That one. The others go under Next.\""),
        ("The reuse check found an existing tool", "\"Good. You just saved a week. Write the guide to that tool.\""),
        ("A chatbot that cannot open the link", "Open the coach on GitHub, copy all of it, paste it, then: Follow the build coach pasted above."),
        ("A job that involves a team or shared files", "\"Pick the part you do on your own for today.\""),
        ("A fresh-chat test that passes too easily", "Check the new chat really remembers nothing: a Temporary Chat in ChatGPT or Gemini, an incognito chat in Claude."),
        ("Real client data in a prompt", "\"Use invented or anonymised notes unless your workplace allows this chatbot for that data.\"")],
)


def module_minutes(m):
    """The lecture, plus the core lessons, plus five minutes for the check. Returns (total, core lessons)."""
    core = sum(L['minutes'] for L in m['lessons'] if not L.get('optional'))
    return m['lecture'] + core + 5, core


def total_minutes():
    return sum(module_minutes(m)[0] for m in MODULES)
