"""How to use Agentic Process: a visual guide and course about this project, written once.

build.py turns it into base/course.html. The nine steps themselves come from steps.py, so the course cannot drift
from the process. The test numbers come from _build/runs/README.md: keep them in step with it.
Every status here says who has tried the thing. Every time is an estimate until a person is timed.
"""
G = "https://github.com/bar181/practical-ai/blob/main/projects/agentic-process/"
T = "https://github.com/bar181/practical-ai/tree/main/projects/agentic-process/"
FORM = "https://github.com/bar181/practical-ai/issues/new?template=i-built-one.yml"
MEMORY_OFF = "a Temporary Chat in ChatGPT or Gemini, an incognito chat in Claude, or any chat with memory and custom instructions turned off"

COURSE = dict(
 title="How to use Agentic Process",
 subtitle="A visual guide and short course",
 purpose="How this project works, why each of its nine steps exists, and how to run it yourself: in a chat window, with a coding agent, or from a spec you already have.",
 who="Anyone using this project, its author included: a business owner or student with a chatbot, a builder with a coding agent, a team lead whose agents work unattended.",
 read=25, run=60,
 honest="Written on 16 November 2026. Every time is an estimate: nobody has been timed yet. Every test so far was an AI session in Claude.",
)

# Chapter 1: what it is, and why
WHY = dict(
 mistakes=[("The wrong job", "Ask for five things and get a tool that does none of them well.", 1),
           ("It already existed", "A built-in feature or a free tool already did the job.", 2),
           ("Only you can use it", "It works in your chat, with everything you said earlier, and breaks for anyone else.", 8)],
 get=[("A one-page plan", "Fifteen headings, five lines each at most. Seven on the short path."),
      ("Instructions anyone can paste", "With one worked example kept beside them."),
      ("A test you can rerun", "A fresh chat, your instructions, one input, and its list of guesses.")],
 # (round, average blocking points per coach test run), from _build/runs/README.md
 coach=[("Round 1", 4.5), ("Round 2", 3.5), ("Round 3", 2.5)],
 # (audit, average of the beginner, builder and teacher scores), from _build/runs/README.md
 audits=[("First", 59), ("Second", 63), ("Third", 65), ("Fourth", 74)],
)

# Chapter 3: run it. (title, who, starts at, status, steps). Steps are (text, code or None).
PATHS = [
 dict(key="chat", title="In any chatbot", level="Beginner", start=1, needs="A chatbot you already use. Nothing to install.",
  status="Tested: six runs by fresh AI sessions, in Claude. Not yet run in ChatGPT, Gemini or Copilot.",
  steps=[("Copy the coach prompt below into your chatbot. Change the last line to your job.", "COACH"),
         ("Say yes to the short path if one person turns one kind of input into one result. Otherwise take all nine steps.", None),
         ("Answer its questions. It stops at every gate and waits for you.", None),
         ("At the plan, ask it: What did you assume? Fix what is wrong.", None),
         ("For the test, open " + MEMORY_OFF + ". Paste the test prompt the coach gives you, your instructions and one invented input.", None),
         ("Read its list of guesses before the result. Fix repeats first, then blocking points. Test once more.", None)]),
 dict(key="agent", title="With a coding agent", level="Advanced", start=1, needs="A coding agent such as Claude Code, and a git repository.",
  status="Tested: two runs by a second agent, one of them unattended in an empty repository.",
  steps=[("Copy the skill folder into your agent's skills, from the repository root:", "mkdir -p .claude/skills && cp -r projects/agentic-process/level-2-files/agentic-process .claude/skills/"),
         ("Tell the agent:", "Use the agentic-process skill. Start at step 1. My job: [one sentence]"),
         ("At step 5 it makes the project folder:", "python3 projects/agentic-process/level-2-files/agentic-process/new_project.py <slug> \"<Title>\""),
         ("Run the gates whenever you like. filled fails until step 6 and built until step 8, by design:", "python3 projects/<slug>/_build/checks/gates.py projects/<slug>"),
         ("For step 8, start the fresh-run tests yourself, one new session for each kind of request.", None)]),
 dict(key="spec", title="From a spec you already have", level="Advanced", start=7, needs="A plan in workshop/plans/ or a draft in workshop/drafts/, and a coding agent.",
  status="Not tried yet. This is how the project tests itself on its own next tool.",
  steps=[("Make the project folder for the plan:", "python3 projects/agentic-process/level-2-files/agentic-process/new_project.py <slug> \"<Title>\""),
         ("Tell the agent:", "Use the agentic-process skill. The plan is in workshop/plans/<slug>/README.md. Check it against the gates for steps 1 to 6 and list what is missing. Then do steps 7 and 8, Beginner level only. Stop at every gate and wait for me."),
         ("Run the two fresh-chat tests yourself. Fix only what blocks.", None),
         ("Keep one note: where Agentic Process tripped you. That note is the next fix list for this project.", None),
         ("Tell us in two minutes with the form at the end of this course.", None)]),
]

# Chapter 4: automation and the levels. (level, who runs it, what checks it, status)
LADDER = [
 ("Base", "You, in any chatbot", "The coach asks each gate question; a fresh chat tests the result", "Tested by AI sessions in Claude"),
 ("Level 2: a coding agent", "An agent with the skill folder, stopping at each gate for you", "Four gates a script runs: layout, links, filled, built", "Tested: two agent runs"),
 ("Level 2: on a schedule", "A scheduler you already have (a Claude Code routine, a ChatGPT or Codex scheduled task, or an issue assigned to a coding agent) runs the skill on a spec and opens a draft pull request", "The same gates, plus the four-heading note in the pull request", "Planned, not built"),
 ("Level 3: unattended agents", "An agent runs steps 1 to 6 and prepares the tests; fresh sessions run them; the agent fixes and hands back", "Gates in gates.json, the fresh-run rules, the scorecard", "Tested: one unattended run"),
 ("Level 3: from Slack or a tool server", "A message or a call starts the same scheduled run", "The same gates", "Not built"),
]
GATES = [("layout", "The folder follows the agreed shape", 5), ("links", "No broken link", 5),
         ("filled", "The plan has no blanks", 6), ("built", "The instructions have no blanks", 8)]

# Chapter 5: your first tool
FIRST = ["One real job of yours, taken through steps 1 to 8", "The one-page plan, every heading filled",
         "Instructions anyone can paste, with one worked example beside them", "Two fresh-chat tests, logs unedited, each point marked blocking or minor",
         "A note with four headings: Decided. Assumed. Not checked. Test this next."]

# Two questions per chapter: (question, options, right index, why)
CHECKS = {
 1: [("What does Agentic Process put in front of the build?", ["A faster way to write prompts", "Nine cheap checks, each ending in a gate question", "A paid tool that writes the code"], 1, "Building is quick now; the costly mistakes happen before it."),
     ("What do the test numbers on this page measure?", ["Time saved by real users", "Points that tripped fresh AI sessions, falling as the project was fixed", "How many people used the project"], 1, "They are AI sessions in Claude, not people. Nobody has been timed.")],
 2: [("Your reuse check finds a free tool that does the whole job. What now?", ["Build your own anyway", "Stop: write a two-line guide to that tool", "Go on to step 3"], 1, "Stopping at step 2 is a win."),
     ("Who reviews your plan at step 7?", ["You, the next morning", "A new chat that remembers nothing", "The chat that wrote it"], 1, "The author reads past their own gaps.")],
 3: [("You already have a plan in workshop/plans/. Where do you start?", ["Step 1, from scratch", "Check it against gates 1 to 6, then steps 7 and 8", "Step 9"], 1, "The spec path reuses the plan and starts at the review."),
     ("Why must the test chat remember nothing?", ["It runs faster", "Otherwise it passes because of what you said earlier", "It is cheaper"], 1, "A stranger has only your instructions.")],
 4: [("Which gate is meant to fail until step 8?", ["layout", "links", "built"], 2, "built checks the instructions, which exist only at step 8."),
     ("In any automated run, who merges?", ["The agent, once the gates pass", "A person, after reading the hand-back", "The scheduler"], 1, "A person approves anything merged, posted, sent, paid or published.")],
}

# Notes for whoever presents it. Times add to about 45 minutes, then the lab.
NOTES = {
 1: "8 min. Open with the inspector picture and the three mistakes. Ask: who has had an AI answer that was polished and wrong? Then the two charts: say plainly they are AI sessions, not people.",
 2: "15 min. Scroll slowly; the diagram moves with you. For each step say the why, not the how. Stop at step 2 and step 8: those two save the most.",
 3: "12 min. Show one path live: paste the coach prompt into a chatbot on the projector and answer the first two questions. Then the lab: everyone runs the path that fits them, about 60 minutes.",
 4: "8 min. The ladder: read the status column aloud. Only the first, second and fourth rows have been tried.",
 5: "2 min. Set the first tool as homework, and ask everyone to fill in the form when they finish.",
}
