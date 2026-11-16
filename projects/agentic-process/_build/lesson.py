"""The 30-minute lesson, written once. build.py turns it into base/TEACH-IN-30-MINUTES.md (the teacher's plan)
and base/training.html (the slides to present, with a lesson timer and the teacher's notes).

Each segment has a start and end minute, what the teacher does, says, and what learners do, and its slides.
A slide is (label, title, body, note). body is a list of lines; a line starting with "1." is a numbered list item,
"- " a checklist item, "> " a quotation, "PROMPT" puts the coach prompt on the slide.
"""
from steps import coach_prompt, pasted_prompt, COACH_FILE
COACH_PROMPT = coach_prompt("[one job you do on your own, in one sentence]")
PASTED_PROMPT = pasted_prompt("[one job you do on your own, in one sentence]")
CHECKS = [
 ("The reuse check finds a free tool that does the whole job. What now?", "Stop, and write a short guide to that tool. The second gate exists to save you from building what already exists."),
 ("Why fix the folder layout before anything is built?", "Every file points at other files. Moving them later breaks those links, and you pay for the move each time the shape changes."),
 ("A fresh session finishes the job and lists twelve problems. Did the test pass?", "Yes. It finished, and the twelve problems are the next hour of work: first the ones in two or more logs, then the blocking ones."),
]
REVIEW_PROMPT = ("You have never seen this project. Read the plan below. Explain it back in five sentences, then list every "
                 "place where you had to guess, quoting the line. Do not improve the plan. Only report.\n\n[paste your plan so far]")

SEGMENTS = [
 dict(start=0, end=3, name="The hook",
  do="Show the first slide", say="\"An AI will build whatever you ask. It will also build the wrong thing, quickly and with confidence. Today is about the order of work that stops that.\"",
  learners="Listen",
  slides=[("By the end", "You will have a one-page plan for an AI tool of your own.",
           ["And the one test that finds its faults before anyone else does."],
           "Promise one thing they will leave with. Ask: who has asked an AI to build something, and got something close but wrong? Hands up. That is today."),
          ("The problem", "Your AI can build almost anything. That is the problem.",
           ["It builds fast, with confidence, and it does not ask whether it is the right thing."],
           "Pause on this one. The point is that speed is not the risk. Building the wrong thing well is the risk.")]),
 dict(start=3, end=7, name="The picture",
  do="Show the inspector slide", say="\"Think of a building site with an inspector. Nothing moves to the next stage until the current one is signed off. Our sign-off is a question called a gate.\"",
  learners="Say one job they repeat, in one sentence, to the person beside them",
  slides=[("Think of it as", "A building site with an inspector.",
           ["You agree the drawing before you pour concrete. You frame before you choose curtains. Each stage is signed off before the next."],
           "Give the picture before the steps. Come back to it whenever someone is lost. The puppy is the inspector: friendly, brief, nothing gets past."),
          ("Turn to your neighbour", "Say one job you repeat, in one sentence.",
           ["One user. One thing goes in. One thing comes out."],
           "One minute each. Listen for people describing three jobs. Ask them which one they would miss most on Monday.")]),
 dict(start=7, end=10, name="The nine steps",
  do="Show the four stages, then the step card", say="\"Nine steps in four stages. Every step has a purpose, a proof you are done, a prompt to paste, and a gate: the question you answer before you move on.\"",
  learners="Write down which step they usually skip",
  slides=[("Nine steps, four stages", "Decide. Design. Build and test. Grow.",
           ["1. Decide: scope, reuse check, outside help, cost.", "1. Design: simplest design, plan and front door, review.",
            "1. Build and test: the smallest version, tested by a stranger.", "1. Grow: one addition at a time."],
           "Read each stage once. Do not explain each step: the guide does that. Ask them to note which one they usually skip. Most say the reuse check or the test."),
          ("Every step has", "A purpose. A proof. A prompt. A gate.",
           ["- Purpose: why the step exists.", "- Proof: what you are holding when it is done.",
            "- Prompt: what to paste into your chatbot.", "- Gate: the question you answer before you go on."],
           "If you have the guide open on a second screen, open step 1 and show the four parts. The gate for step 1 is: can you say the job in one sentence?")]),
 dict(start=10, end=22, name="Your turn: the coach",
  do="Share the prompt. Walk the room", say="\"Paste it in. Change the last line to your job. Say yes to the short path: it does steps 1, 6 and 8 in full and the rest in a line each, Stop when it shows you the plan.\"",
  learners="Run the coach on their own idea, on the short path, until it shows them the one-page plan",
  slides=[("Your turn", "Paste this. Change the last line to your job.",
           ["PROMPT", "Say yes to the short path. Stop when it shows you the plan. Twelve minutes."],
           "Stop talking. Start a twelve-minute timer. Walk the room. If the coach does not offer the short path, the job is too big for today: the learner picks the part they do on their own. The full nine steps take about an hour. If a chatbot says it cannot open the link, show the next slide."),
          ("Link will not open?", "Paste the coach yourself.",
           ["1. On GitHub, open " + COACH_FILE + ".", "1. Press Raw. Select all. Copy. Paste it into the chat.", "1. Then type: Follow the build coach pasted above. My idea: and your job."],
           "Some chatbots cannot open links. This takes one minute. If the room has many, put the coach's text in a shared document before the lesson.")]),
 dict(start=22, end=26, name="Your turn: a stranger reads it",
  do="Share the review prompt", say="\"You cannot see your own gaps, because you know what you meant. This is step 7: hand your plan to a stranger, a new chat that has never seen it. The short path folds this into the test at step 8. In class we do it now, because it is the habit that matters most.\"",
  learners="Open a new chat, paste the review prompt and their plan so far, and read what it had to guess",
  slides=[("A stranger reads it", "Open a new chat. Paste this, then your one-page plan.",
           ["> " + REVIEW_PROMPT.split("\n\n")[0], "Read where it had to guess. Keep that list."],
           "This is step 7 in miniature. The new chat must have no history: a new conversation, not the same one. Ask one person to read out the first thing it guessed.")]),
 dict(start=26, end=30, name="Check and close",
  do="Ask the three questions, then show the card", say="\"What will you do first when you are back at your desk?\"",
  learners="Answer aloud. Write the next step on their plan",
  slides=[("Check yourself", "Three questions.",
           ["- " + q for q, a in CHECKS],
           "Answers. " + " ".join(f"{i}. {a}" for i, (q, a) in enumerate(CHECKS, 1))),
          ("Keep this", "One job. Check what exists. Fix the layout. Let a stranger test it.",
           ["The guide, the coach and every prompt: github.com/bar181/practical-ai, in projects/agentic-process"],
           "End on the card. Homework: go back to the coach chat, type carry on to step 8, run the fresh-chat test it gives you, and send the plan and what the new chat had to guess.")]),
]

WATCH = [
 ("A learner describing three jobs", "The scope is too wide", "\"Which one would you miss most on Monday? That one. The others go under Next.\""),
 ("The coach found an existing tool", "The process worked", "\"Good. You just saved a week. Write the guide to that tool.\""),
 ("A learner skipping the questions to get to the build", "The usual habit", "\"The inspector does not let you choose curtains yet.\""),
 ("A chatbot that cannot open the link", "Common", "Show the next slide: paste the coach, then \"Follow the build coach pasted above.\""),
 ("A learner whose job involves a team or shared files", "The coach takes all nine steps, about an hour", "\"Pick a part you do on your own for today. The team version can wait for another day.\""),
 ("The coach offers the short path", "A small job, in a chat", "\"Say yes. You will still do steps 1, 6 and 8 in full.\""),
]

assert SEGMENTS[0]["start"] == 0 and SEGMENTS[-1]["end"] == 30
assert all(a["end"] == b["start"] for a, b in zip(SEGMENTS, SEGMENTS[1:])), "segments must follow on without gaps"
