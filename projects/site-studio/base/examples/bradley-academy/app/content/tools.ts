// The nine tools. Every fact here comes from the tool's README in the repository; the wording is
// written in Bradley's practical instructor voice. Change a fact in the README first, then here.
// Links that start with "/" are pages on this site (the published examples); the base path is added for you.
import type { Tool } from "./types";
import { toolSlugs, type ToolSlug } from "./slugs";

const GH = "https://github.com/bar181/practical-ai/tree/main/projects";
// A single file on GitHub, such as a worked example that is not published on this site.
const GHB = "https://github.com/bar181/practical-ai/blob/main/projects";

// The design set: three tools that work alone or one after another.
const designSet = (text: string, links: { href: string; label: string }[]) => ({ text, links });

const artifactStudio: Tool = {
  slug: "artifact-studio",
  name: "Artifact Studio",
  icon: "icons/artifact-studio.svg",
  promise: "Designer-quality reports, made by you.",
  sub: "Your notes, turned into a page with the impact of a professional website, in the chatbot you already use.",
  cardLine: "Notes in, a page that looks like a designer made it out.",
  coreIdea:
    "You already ask your AI for reports. Ask through Artifact Studio and it brings what a designer would: the looks, the effects, the components and the motion.",
  analogy:
    "Think of it as a designer who sits inside your chatbot. You bring the notes. It brings the layouts, the photo effects and an eye for what your reader needs to see first.",
  whatItIs: [
    "Artifact Studio is the design step: looks, effects, components and motion. It is a design guide your chatbot reads. You paste one prompt with your notes, and you get back one finished page, slide deck or social post picture: a file you keep.",
    "It holds seven voices, nine looks, four whole-page templates, four deck styles and the photo effects most people never ask for because they do not know they exist: a slow pan and zoom, photo-filled type, a before and after slider, line art that draws itself as you scroll.",
    "New: eight cinematic effects from this website, rebuilt for a single file. The opening, the grade, the statement, the clip, the stack, a timeline that draws itself, the page change and end credits.",
  ],
  benefits: [
    { title: "It looks professionally designed", text: "Photos, motion and a story that unfolds as you scroll: charts that build, a photo that pans and zooms." },
    { title: "The same standard every time", text: "Nine looks and more than forty effects fitted to your content and your reader, with words in one of seven voices. The answer first, nothing invented, gaps marked, not guessed." },
    { title: "Minutes, not hours", text: "About five minutes for a page that takes an hour or more by hand. That is an estimate, not a measurement." },
  ],
  design: [
    { title: "It chooses for you", text: "From your notes and your reader, it picks a template, a voice and a look, and tells you what it chose in one line. Want something else? Say it in one sentence." },
    { title: "Your facts only", text: "It never invents a number, a name or a quote. Anything missing is marked [needs: ...] for you to fill." },
    { title: "Built for the phone", text: "Every page is designed at phone width first, and stays readable with motion turned off." },
    { title: "You stay in charge", text: "It does not post, send or publish anything. A person decides." },
  ],
  coreUser:
    "Someone with rough notes and something to share: an owner, a manager or a teacher who needs a report, a lesson or a post to look as good as the work behind it.",
  levels: [
    {
      level: 1,
      name: "Paste a prompt",
      coreUser: "Anyone with notes and a chatbot",
      story: "As a business owner, I want my monthly numbers to look like a designer made them, so that my partner reads them on her phone and acts.",
      does: "Copy the try-it prompt, swap in your own notes and attach a photo if you have one. Then change it in one sentence: tell it as a story, or show it as a keynote deck.",
      setup: "None",
      built: true,
    },
    {
      level: 2,
      name: "Make it your standard",
      coreUser: "Someone who makes reports every week",
      story: "As a manager, I want every report in the same design and to the same bar, so that I stop explaining what good looks like.",
      does: "Save the design guide once in a Claude or ChatGPT Project, a Gemini Gem, or as a skill. Add your colours and tone in a preferences file.",
      setup: "Once",
      built: true,
    },
    {
      level: 3,
      name: "Connect your agents or your team",
      coreUser: "A builder whose agents make pages",
      story: "As a builder, I want my agents to browse the library and pick the right template by themselves, so that every page they make meets the same bar.",
      does: "An MCP server lets an agent browse the library and get a recommended template. It runs on your own computer.",
      setup: "On your computer",
      built: true,
    },
  ],
  tryIt: {
    intro: "Copy this into the chatbot you use. Keep the sample notes, or paste your own.",
    after: "Before you share, check that every number matches your notes, that nothing was added, and that the headline says what you want the reader to take away.",
    promptKey: "artifact-studio",
    primaryLabel: "Copy the try-it prompt",
  },
  notDo: [
    "It does not post, send or publish anything: a person decides.",
    "It does not invent facts: a gap is marked for you to fill.",
    "A simple Markdown or Word version is planned, not built.",
  ],
  status: {
    date: "18 November 2026",
    label: "In user testing",
    text: "Built by its author and tested by fresh Claude sessions: 22 runs of the design guide and two runs of the try-it prompt, and every run finished its page. Used for real by its author for a client's course. Users are testing it; their results are not in yet. Not yet tried in ChatGPT or Gemini. The eight cinematic effects, added on 21 November 2026, were checked by the author in headless Chrome at phone and desktop width, with motion on and reduced. The testers have not seen them yet.",
  },
  readme: `${GH}/artifact-studio`,
  explainer: "/reports/artifact-studio.html",
  set: designSet("Artifact Studio is the design step. Web Sections sets the structure and Tone Studio writes the words. Each works alone, and Artifact Studio still makes a whole page from one paste. Post previews, which show a draft the way a feed will, are now part of Web Sections.", [
    { href: "/tools/web-sections", label: "Web Sections, for the structure" },
    { href: "/tools/tone-studio", label: "Tone Studio, for the words" },
  ]),
  tabs: [
    {
      id: "showcase",
      label: "Showcase",
      intro: "Master page 1 of 2: what your AI can make. Photo effects, scroll effects, cinematic effects, layouts, social picture sizes and a tab for each of the seven voices.",
      blocks: [{ kind: "frame", src: "/artifact-studio/showcase.html", title: "Artifact Studio showcase", caption: "The live showcase. Tap a tab inside it.", height: 760 }],
    },
    {
      id: "components",
      label: "Components",
      intro: "Master page 2 of 2: what a page is built from. Four whole pages, four decks, the parts, the design ideas, the picker and the reference sheets.",
      blocks: [{ kind: "frame", src: "/artifact-studio/components.html", title: "Artifact Studio components", caption: "The live components page. Tap a tab inside it.", height: 760 }],
    },
    {
      id: "before-after",
      label: "Before and after",
      intro: "One lesson Bradley made for a client's course, three ways, from one source. The plain version is what a chatbot gives you by default.",
      blocks: [
        {
          kind: "gallery",
          size: "phone",
          pictures: [
            { src: "artifact-studio/before-plain.webp", caption: "Before: the plain version", alt: "Animated phone capture of the plain version: a white Markdown document titled AI as a Smart Intern, with headings, bullet lists and two small tables, scrolling top to bottom" },
            { src: "artifact-studio/scroll-lesson.webp", caption: "After: the teacher voice", alt: "Animated phone capture of the teaching page, Treat AI like a smart intern: a robot clip, a vague brief against a full brief in tabs, frosted cards over painted scenes, the word Launch filled with a picture, and check-yourself questions" },
            { src: "artifact-studio/scroll-story.webp", caption: "After: the same lesson as a story", alt: "Animated phone capture of the same lesson as a story: a dark candlelit page that opens on Monday, 8:40 a.m. Your desk, then story beats that arrive as you scroll, the robot clip, a glowing scroll, the word Launch and the guide card" },
          ],
        },
        {
          kind: "links",
          heading: "Open the two finished pages",
          items: [
            { href: "/artifact-studio/base/examples/before-after/2-teacher.html", label: "The teacher version" },
            { href: "/artifact-studio/base/examples/before-after/3-story.html", label: "The story version" },
          ],
        },
      ],
    },
    {
      id: "effects",
      label: "Effects and voices",
      intro: "A few of the effects and voices, captured from the worked examples and the showcase.",
      blocks: [
        { kind: "picture", size: "wide", picture: { src: "artifact-studio/fx-cinematic.webp", caption: "New: the cinematic effects tab in the showcase. Eight effects from this website, rebuilt for a single file", alt: "Three stills from the cinematic effects tab: a city skyline at dusk under a masked title that rises word by word, a dark screen where the sentence Most AI pages look the same lights up word by word, and a full-screen scene titled Care sliding over the one before it" } },
        {
          kind: "gallery",
          size: "wide",
          pictures: [
            { src: "artifact-studio/fx-line-art.webp", caption: "Line art that draws itself", alt: "Screen capture of a self-drawing line art effect: a pencil sketch of a lake and a tree, traced from the photograph, draws itself as you scroll" },
            { src: "artifact-studio/fx-photo-type.webp", caption: "Photo-filled type", alt: "Screen capture of photo-filled type: the word spark in huge letters on a dark band, the letters filled with a picture of a lightbulb bursting with coloured paint" },
            { src: "artifact-studio/fx-before-after.webp", caption: "A before and after slider", alt: "Screen capture of a before and after effect: one photograph with a divider you drag between the original and a warmer colour grade" },
            { src: "artifact-studio/style-visionary.webp", caption: "The keynote voice, as a deck", alt: "Animated screen capture of the visionary deck: black slides with one idea each in huge white type, then full-screen pictures of a city at sunset, a house in fog and a lightbulb splashed with colour, each with a few words over it" },
            { src: "artifact-studio/voice-storyteller.webp", caption: "The storyteller voice", alt: "Screen capture of the storyteller voice: a sunset photograph over water with a story opening set in serif type" },
          ],
        },
      ],
    },
    {
      id: "examples",
      label: "Worked examples",
      intro: "Each one was made by an AI from a prompt and sample notes. All the businesses and numbers in them are invented.",
      blocks: [
        { kind: "picture", size: "phone", picture: { src: "artifact-studio/example-tryit.webp", caption: "The page the try-it prompt made, in one try, unedited", alt: "Animated phone capture of the page made from the try-it prompt: a garden picture in a slow pan and zoom under the words Two crews, then October revenue counting up to 84,200 dollars, a bar chart against September, 23 jobs, 46 percent of quotes won, and the van decision due 5 December" } },
        {
          kind: "links",
          heading: "Open a worked example",
          items: [
            { href: "/artifact-studio/try-it-keynote.html", label: "The try-it prompt's page", note: "a scrolling keynote" },
            { href: "/artifact-studio/base/examples/report.html", label: "A one-page report" },
            { href: "/artifact-studio/base/examples/photo-effects.html", label: "Photo effects" },
            { href: "/artifact-studio/base/examples/voice-practical.html", label: "The practical instructor voice" },
            { href: "/artifact-studio/base/examples/voice-analyst.html", label: "The analyst voice" },
            { href: "/artifact-studio/base/examples/voice-brief.html", label: "The executive brief voice" },
            { href: "/artifact-studio/base/examples/voice-storyteller.html", label: "The storyteller voice" },
            { href: "/artifact-studio/base/examples/voice-visionary.html", label: "The keynote voice" },
            { href: "/artifact-studio/base/examples/voice-explainer.html", label: "The teacher voice" },
            { href: "/artifact-studio/base/examples/voice-emotional.html", label: "The personal story voice" },
          ],
        },
      ],
    },
  ],
};

const documentBrief: Tool = {
  slug: "document-to-action-brief",
  name: "Document to action brief",
  icon: "icons/document-to-action-brief.svg",
  promise: "Know what a document asks of you, by when, and where it says so.",
  sub: "For the notice, contract, tender, policy or bill you have to act on.",
  cardLine: "A long document in, what to do and by when out.",
  coreIdea:
    "A long document hides the three things you must do. This finds them, puts the answer first, and shows you the exact words each line came from, so you can check before you act.",
  analogy:
    "Think of it as a sharp assistant who reads the small print for you, then hands you a sticky note: what to do, by when, what it costs, and the page it is on.",
  whatItIs: [
    "Document to action brief turns a supplier notice, contract, tender, policy or bill into a one-page brief: how many things you must do, the earliest date, and every penalty or cost, then short tables of actions, dates, open questions and key facts.",
    "Every line quotes the exact words it came from and says where they are, so you can search for them, tick them, then act.",
  ],
  benefits: [
    { title: "The answer first", text: "How many things you must do, the earliest date, and every penalty or cost, including the one buried in a friendly paragraph." },
    { title: "Every line you can check", text: "Each action, date and fact carries the exact words it came from and where they are. Search for them, tick them, then act." },
    { title: "Fitted to the situation", text: "A contract, a change of terms, a tender or a bill each get the one extra section that reader needs." },
  ],
  design: [
    { title: "Open questions stay open", text: "A line that can be read two ways, or depends on something you may not know, goes under Open questions, never under Key facts." },
    { title: "It lists, you decide", text: "It never tells you what to do. It ends by asking you to write your one action: I will ... by ..." },
    { title: "One extra section for your situation", text: "Before you sign, What changes, Does it apply to us, Can we bid, What it asks of me, or Pay or reply." },
    { title: "Fitted to the reader", text: "For a busy boss, three lines they can forward. For your team, a who-does-it column." },
  ],
  coreUser:
    "A business person who has to act on a document they did not write: a café owner with a supplier notice, a manager before signing, a team lead with a tender.",
  levels: [
    {
      level: 1,
      name: "Paste one prompt",
      coreUser: "Anyone with a document to act on",
      story: "As a café owner, I want to know what my supplier's notice makes me do and by when, so that I do not miss a deadline or a new charge.",
      does: "Paste the prompt, replace the sample notice with your document or attach the file, and say who reads it. Read the answer first, check each quote, then decide.",
      setup: "None",
      built: true,
    },
    {
      level: 2,
      name: "Save it, with your house rules",
      coreUser: "Someone who gets documents like this every week",
      story: "As an office manager, I want every document to get the same brief with our own rules, so that each brief names who in our team answers which question.",
      does: "Install the instructions once as a skill or in a Project, then just attach a document. House rules add who you are, the documents you get and who answers what.",
      setup: "Once",
      built: true,
    },
    {
      level: 3,
      name: "Hands-off",
      coreUser: "A team that receives documents in a shared inbox",
      story: "As an operations lead, I want each notice that arrives to be briefed and logged with an owner, so that nothing waits in an inbox.",
      does: "Planned, not built: a scheduled task watches an inbox label or folder, writes each action to a register with an owner, drafts reminders for you to send, and puts anything unclear or costly in a review lane. Nothing is sent or signed without you.",
      setup: "Planned",
      built: false,
    },
  ],
  tryIt: {
    intro: "Copy the whole box into the chatbot you use. It holds the instructions and an invented supplier notice, so you see a result first. Then change the café to your business and replace everything after DOCUMENT: with your own.",
    after: "Paste real documents only into a chatbot your workplace allows for them. A scan with no selectable text will not work: copy the text out first.",
    promptKey: "document-to-action-brief",
    primaryLabel: "Copy the try-it prompt",
  },
  notDo: [
    "Not legal, tax or financial advice. It lists what the document says.",
    "Not a contract risk review. That is a job for a legal team and its tools.",
    "Not a sender. It never replies, signs, accepts or pays. You do.",
  ],
  status: {
    date: "18 November 2026",
    label: "In user testing",
    text: "Tested in nine fresh Claude sessions, including a notice missing its date and price list, a tender, no document at all, and saved house rules. Every run that had the instructions passed, and a script found every quote word for word. Not yet tried in ChatGPT or Gemini. Level 3 is not built. Users are testing it; their results are not in yet.",
  },
  readme: `${GH}/document-to-action-brief`,
  explainer: "/reports/document-to-action-brief.html",
  tabs: [
    {
      id: "example",
      label: "Example brief",
      intro: "The first screen of a brief a fresh Claude session wrote from the try-it prompt. The supplier and the café are invented.",
      blocks: [
        { kind: "picture", size: "phone", picture: { src: "document-to-action-brief/example-brief.webp", caption: "The answer first, then what changes, each line with its exact words", alt: "The first screen of a brief a fresh Claude session wrote from the try-it prompt: the title Action brief: Kestrel Fold change of terms; the answer first, 3 things to do, earliest date 20 November 2026, and every cost and penalty; then a What changes table of old and new terms, each with the exact words and the clause" } },
      ],
    },
    {
      id: "situations",
      label: "Fitted to your situation",
      intro: "Say what kind of document it is, or let the AI work it out. Each kind adds one section to the brief.",
      blocks: [
        {
          kind: "table",
          caption: "The one extra section each kind of document gets",
          head: ["Your document", "The brief adds"],
          rows: [
            ["A contract or agreement, before you sign", "Before you sign: what you commit to, how it renews and ends, what leaving early costs, and questions to ask the other side"],
            ["A change of terms or a supplier notice", "What changes: old and new, side by side, and the deadline to accept or say no"],
            ["A policy, rule or regulation update", "Does it apply to us: who it covers, as written, and when it starts"],
            ["A tender or request for quotes", "Can we bid: who may bid, the question and bid deadlines, and every document to send"],
            ["A report, board pack or proposal", "What it asks of me: the decisions asked for, numbers that changed, risks named"],
            ["A bill, tax notice or official letter", "Pay or reply: the amount, the due date, how to pay or reply, and what happens if you do not"],
          ],
        },
      ],
    },
    {
      id: "how-built",
      label: "How it was built",
      intro: "This tool was built with Agentic Process, and it is the tool from the blind pilot.",
      blocks: [
        { kind: "picture", size: "wide", picture: { src: "agentic-process/pilot-score.svg", caption: "One blind pilot, one unseen notice, one reviewer: a strong signal, not a study", alt: "Animated chart: in one blind pilot on the same brief, the tool built with Agentic Process scored 93 out of 100 and needed 0 corrections; the direct-build version scored 73 out of 100 and needed 2 corrections." } },
        { kind: "links", heading: "More", items: [{ href: "/tools/agentic-process", label: "Agentic Process, the method that built it" }] },
      ],
    },
  ],
};

const learnings: Tool = {
  slug: "learnings-database",
  name: "Learnings database",
  icon: "icons/learnings-database.svg",
  promise: "Stop making the same mistake twice.",
  sub: "A lessons-learned log your AI keeps for you, in the chatbot you already use.",
  cardLine: "Each lesson kept once, and back in front of you before similar work.",
  coreIdea:
    "Your chatbot forgets, and so does the team. This keeps each lesson once, as a rule you can follow, and puts it back in front of you before you start similar work.",
  analogy:
    "Think of it as a ship's log: one line each time the crew hits a rock or finds a faster channel, read by the next crew before they sail.",
  whatItIs: [
    "The Learnings database is a log of what went wrong, what had to be redone and what worked better than expected. You say one sentence; your AI files it as one row in a spreadsheet you own, with the lesson written as an instruction: When ..., do ....",
    "Before similar work, say before I start, and the rules you accepted come back, ready to paste into the next chat.",
  ],
  benefits: [
    { title: "One sentence in, one filed lesson out", text: "Say what happened and what you expected. You get one row, filed by area, with the lesson written as an instruction." },
    { title: "Repeats are counted, not copied", text: "It checks your log first. A lesson already there gets its count raised, so you see what keeps going wrong and can fix the cause." },
    { title: "The rules come back when they matter", text: "Say before I start and get the rules that apply. A lesson becomes a rule only when you accept it at a five-minute weekly review." },
  ],
  design: [
    { title: "It asks before saving", text: "Nothing goes in your log without your yes." },
    { title: "The learning side only", text: "Not a wiki, a knowledge base or a note-taking app. Memory keeps facts about you; this keeps rules for the work." },
    { title: "Private details stay private", text: "Names and contact details are replaced with [removed], and rows about clients or money are marked sensitive and kept out of anything you paste elsewhere." },
    { title: "The same columns at every level", text: "Start with a spreadsheet and move up later without starting again." },
  ],
  coreUser:
    "A business owner, manager or builder who works with a chatbot every day and keeps fixing the same things: the email with last year's dates, the quote with no expiry, the price list that drops a line.",
  levels: [
    {
      level: 1,
      name: "A link",
      coreUser: "Anyone who works with a chatbot",
      story: "As a small business owner, I want each mistake written down once as a rule, so that I do not send last year's dates again.",
      does: "Paste the prompt with something that went wrong this week. You get one row back, and the starter spreadsheet the first time.",
      setup: "None",
      built: true,
    },
    {
      level: 2,
      name: "Saved once",
      coreUser: "Someone who logs lessons every week",
      story: "As a manager, I want every chat to already know how to log and find our lessons, so that I never paste the instructions again.",
      does: "Save the instructions once in a Claude or ChatGPT project, or as a Claude plugin.",
      setup: "About five minutes",
      built: true,
    },
    {
      level: 3,
      name: "Your team",
      coreUser: "A team that wants one shared log",
      story: "As a team lead, I want one log the whole team adds to and reads from, so that a lesson one person learns reaches everyone.",
      does: "One shared log in Supabase, a free online database. Set it up by pasting one file, then connect it to Claude or ChatGPT.",
      setup: "About fifteen minutes, an estimate",
      built: true,
    },
  ],
  tryIt: {
    intro: "Paste this into Claude, ChatGPT or the AI tool you use. Change the last line to something that went wrong for you this week.",
    after: "You get the lesson back as one row. Say yes, give me the updated file to keep it.",
    promptKey: "learnings-database",
    primaryLabel: "Copy the try-it prompt",
  },
  notDo: [
    "It stores nothing itself: your log lives in your own spreadsheet, folder or database.",
    "It is not a wiki or a knowledge base.",
    "It never makes a lesson a rule without your yes.",
  ],
  status: {
    date: "19 November 2026",
    label: "New",
    text: "Built by its author and tested with fresh Claude sessions on invented data. No one else has used it yet. It filed 40 of 40 test lessons in the right area and passed 11 of 11 behaviour checks. Not yet tried: the link prompt with the live link, ChatGPT, a real Supabase project, and use by a real person.",
  },
  readme: `${GH}/learnings-database`,
  explainer: "/reports/learnings-database.html",
  tabs: [
    {
      id: "replies",
      label: "Example replies",
      intro: "Real, unedited replies from fresh Claude sessions in testing. The data is invented.",
      blocks: [
        {
          kind: "gallery",
          size: "phone",
          pictures: [
            { src: "learnings-database/example-reply.webp", caption: "log that: one row back", alt: "A real reply from a test: the message log that, the email went out with last year's dates; the reply is one CSV line and a table: kind error, area marketing, project newsletter, lesson type check, rule When reusing a past email, check every date in the body against this year's calendar before it is sent, status proposed, seen 1; then a repeat check that names a close row" },
            { src: "learnings-database/before-i-start.webp", caption: "before I start: the rules that apply", alt: "A real reply from a test: before I start the price update on the company website; two accepted rules come back, L-5 name the file and leave everything else as it is, and L-11 update the price page and the quote template together, in a block ready to paste" },
          ],
        },
        { kind: "picture", size: "wide", picture: { src: "learnings-database/the-log.webp", caption: "The starter spreadsheet: 7 of its 18 columns, with invented examples", alt: "The starter spreadsheet with invented rows: columns id, kind, area, project, rule, status and seen; for example L-1, error, sales, kitchen-renovations, When sending a quote, put a valid-until date of 30 days on the first page, accepted, seen 3" } },
      ],
    },
    {
      id: "what-to-say",
      label: "What to say",
      intro: "Three things to say. That is the whole tool.",
      blocks: [
        {
          kind: "table",
          caption: "What you say, and what you get",
          head: ["You say", "You get"],
          rows: [
            ["log that: [what happened]. I expected [what you expected].", "One row, or \"this is a repeat of L-9\" with its count raised"],
            ["before I start [the work]", "Up to five rules you accepted, ready to paste into the next chat"],
            ["weekly review", "The new rows, each with a suggestion: accept, merge or retire. You decide"],
          ],
        },
        { kind: "picture", size: "wide", picture: { src: "learnings-database/how-it-works.svg", alt: "How it works in three steps: say log that with what happened and what you expected; get one filed row with the lesson as an instruction, saved after your yes, or a repeat counted; before similar work, the rules you accepted come back. The AI files and finds. You accept the rules." } },
      ],
    },
  ],
};

const agenticProcess: Tool = {
  slug: "agentic-process",
  name: "Agentic Process",
  icon: "icons/agentic-process.svg",
  promise: "Teach your AI a job once, and it does it the same way every week.",
  sub: "For the jobs you keep re-explaining: meeting notes, supplier notices, quotes.",
  cardLine: "A job you repeat, set up properly once.",
  coreIdea:
    "Most everyday AI work is a prompt and a hope. Agentic Process turns a job you repeat into a small tool: one instruction file, a worked example and a short test, so the AI does the job the same way every time.",
  analogy:
    "Think of it as having an engineer beside you, so every new job is set up the proper way: name the result, reuse what exists, write it once, test it fresh.",
  whatItIs: [
    "Agentic Process is a method your chatbot follows to build you a tool. You describe the job, who uses the result and the one mistake it must catch. You get back instructions you can paste into any new chat, an example, and a short test.",
    "It is how the other tools on this site were built. It uses what you already have, your chatbot and its skills, and adds only the structure and steps they are missing.",
  ],
  benefits: [
    { title: "Work you can check", text: "You get a short test to run in a new chat before you rely on it. A coding agent runs it for you." },
    { title: "The same way every time", text: "Written steps you save once, not a lucky prompt." },
    { title: "Time back", text: "Next week starts from the saved instructions, not a blank chat." },
  ],
  design: [
    { title: "Name the result", text: "Who uses it, and the one mistake it must catch." },
    { title: "Reuse first", text: "Use what already does the job. Build only what is missing." },
    { title: "Write the instructions once", text: "For the chatbot people already use." },
    { title: "Test it fresh", text: "Does it hold up, and would the person use it as it is? Fix, then hand back." },
  ],
  coreUser:
    "Someone who keeps re-explaining the same job to their AI every week, and a builder who wants every new tool set up properly.",
  levels: [
    {
      level: 1,
      name: "Try it",
      coreUser: "Anyone with a job they repeat",
      story: "As a team lead, I want Monday's meeting notes turned into actions the same way every week, so that no action goes without an owner or a date.",
      does: "Paste the prompt into a new chat with your own job, who uses the result and the mistake it must catch.",
      setup: "None",
      built: true,
    },
    {
      level: 2,
      name: "Save it",
      coreUser: "Someone who builds a new tool every so often",
      story: "As a manager, I want every new job to start from the same method, so that each tool I make is checked before I rely on it.",
      does: "Paste the one-page process into a Claude or ChatGPT Project or a Gemini Gem, or add the builder skill.",
      setup: "Once",
      built: true,
    },
    {
      level: 3,
      name: "Hand it over",
      coreUser: "A builder with a coding agent such as Claude Code or Codex",
      story: "As a builder, I want my coding agent to run the whole build, tests included, so that I review a finished tool instead of guiding each step.",
      does: "Give the builder skill to a coding agent. It runs the whole build, including the tests in fresh sessions, and hands back what it built and what it assumed.",
      setup: "A coding agent",
      built: true,
    },
  ],
  tryIt: {
    intro: "Copy this into the chatbot you already use. Swap in your own job, who uses the result, and the mistake it must catch.",
    after: "You get instructions you can paste into any new chat, an example, and a short test. Tested so far in Claude; not yet in ChatGPT or Gemini.",
    promptKey: "agentic-process",
    primaryLabel: "Copy the try-it prompt",
  },
  notDo: [
    "It does not replace your chatbot or its skills. It adds the structure they are missing.",
    "One blind pilot is a strong signal, not a study.",
  ],
  status: {
    date: "18 November 2026",
    label: "In user testing",
    text: "Built by its author with Claude. All testing so far was in Claude, including the blind reviews and the try-it prompt. Users are testing it; their results are not in yet. Not yet tried in other chatbots or coding agents.",
  },
  readme: `${GH}/agentic-process`,
  explainer: "/reports/agentic-process.html",
  tabs: [
    {
      id: "pilot",
      label: "The blind pilot",
      intro: "In one blind pilot, a tool built with Agentic Process scored 93 out of 100. The direct-build version scored 73 on the same brief.",
      blocks: [
        { kind: "picture", size: "wide", picture: { src: "agentic-process/pilot-score.svg", alt: "Animated chart: in one blind pilot on the same brief, the tool built with Agentic Process scored 93 out of 100 and needed 0 corrections; the direct-build version scored 73 out of 100 and needed 2 corrections." } },
        {
          kind: "gallery",
          size: "wide",
          pictures: [
            { src: "agentic-process/pilot-brief-direct.webp", caption: "Before: built the usual way, the missing date is buried in a table", alt: "Screen capture of the reply from the tool built directly: a title, a line counting penalties, actions, dates and questions, then a key facts table where the missing effective date and the account form sit among the facts." },
            { src: "agentic-process/pilot-brief.webp", caption: "After: built with Agentic Process, it warns first", alt: "Screen capture of a chat reply from a tool built with Agentic Process, run on a supplier notice it had never seen. It sums up that the notice asks for four things, with the earliest deadline 15 December 2026, then warns that three things are missing: the Effective Date is never stated, the Account Update Form was not attached, and the overdue charge points to nothing. Below, a table of what you must do, each row with the exact words from the notice and where they are." },
          ],
        },
        { kind: "text", paras: ["Both tools found all nine key items in a notice neither had seen. Only the Agentic Process tool put the missing date and form first and said who to ask. The owner could act on it with no corrections; the other needed two. One build task, one unseen notice, one blind reviewer: a strong signal, not a study."] },
      ],
    },
    {
      id: "built",
      label: "What it has built",
      intro: "Tools built with the method, and how each scored.",
      blocks: [
        {
          kind: "table",
          caption: "Tools built with Agentic Process",
          head: ["Tool", "What it does, and how it scored"],
          rows: [
            ["Document to action brief", "A supplier notice or report becomes what you must do, by when, and what is missing, each with the exact words. 93 out of 100 in the blind pilot, zero corrections. Now a tool of its own, in user testing."],
            ["Decision brief", "A business question becomes options weighed against your goals and limits, with dated sources and a recommendation. 86 to 89 in blind grading, against 61 to 67 for a plain chatbot answer: one question, three blind graders. Every grader also said a busy owner would rather receive the plain answer."],
            ["Learning log", "Each lesson recorded once, and brought back before similar work starts. Passed three fresh-session checks, and led to the Learnings database."],
          ],
        },
      ],
    },
    {
      id: "how",
      label: "How it builds",
      intro: "Four steps, the same for every tool.",
      blocks: [
        { kind: "picture", size: "phone", picture: { src: "agentic-process/builder-flow.svg", alt: "Animation of the builder. A job you repeat goes in at the top. Four steps light up in turn: name the usable result, pick the simplest build, build one SKILL.md, and test it in a fresh session, with a loop back to fix. At the bottom, the package you get: README.md, SKILL.md and example.md, checked before you get it." } },
      ],
    },
  ],
};

const rareFind: Tool = {
  slug: "rare-find",
  name: "Rare Find",
  icon: "icons/rare-find.svg",
  promise: "The daily trivia game where the right answer nobody else thought of wins.",
  sub: "Asked to name a bird, anyone can say Eagle. Say Shoebill and you take the round.",
  cardLine: "A daily quiz where the rarest right answer scores the most.",
  coreIdea:
    "Not everything with AI is work. Working with AI every day means you sometimes have fun with your co-workers, and Rare Find is that break: seven prompts a day, and the rarer your right answer, the more it scores.",
  analogy:
    "Think of it as the office quiz where the obvious answer gets polite applause and the one nobody else thought of brings the house down.",
  whatItIs: [
    "Each day brings seven short prompts, such as Name a bird. You get 30 seconds to type one answer. A popular answer scores 25. A right answer that few people think of scores up to 100. Four hosts tease each answer, never you.",
    "The set is the same for everyone, wherever you play: in Claude, in ChatGPT or another chatbot, or in any browser. At the end, challenge a friend to play your exact prompts.",
  ],
  benefits: [
    { title: "Two minutes, then back to work", text: "Seven prompts a day, 30 seconds each, on a phone or a computer." },
    { title: "Rare and right wins", text: "The most popular answer scores 25. A Gem, a rare right answer, scores 100." },
    { title: "Free, no account", text: "Nothing to install. Play in your chatbot or in any browser." },
  ],
  design: [
    { title: "Your chatbot checks the odd ones", text: "An answer not on the list? Press Check again and the AI checks it is real and right, and forgives small slips. Nothing is approved without the AI's yes." },
    { title: "Honest scoring", text: "The rankings are an AI's estimate, not a survey, and the game says so." },
    { title: "Replayable", text: "The Gems stay hidden in the game, so you can play again." },
    { title: "Built to share", text: "Copy a challenge message, and a friend plays your exact prompts with your score to beat." },
  ],
  coreUser: "Anyone who wants a two-minute break with their AI, and a team that wants a little friendly competition.",
  levels: [
    {
      level: 1,
      name: "Play",
      coreUser: "Anyone with a browser",
      story: "As someone on a coffee break, I want a quick game on my phone, so that I get two minutes of fun before my next meeting.",
      does: "The daily game, practice rounds, the hosts' lines and the estimated chart, in any browser.",
      setup: "None",
      built: true,
    },
    {
      level: 2,
      name: "A chatbot joins in",
      coreUser: "Someone who plays in Claude or ChatGPT",
      story: "As a player, I want my chatbot to check an answer that is not on the list, so that a right but rare answer counts.",
      does: "The AI checks answers not on the list, once each, and the hosts write fresh lines. Play the Claude artifact, or give the rules to ChatGPT or any chatbot.",
      setup: "None",
      built: true,
    },
    {
      level: 3,
      name: "On the web",
      coreUser: "A builder who wants the game public and always tested",
      story: "As a builder, I want a public copy that is rebuilt and tested on every change, so that the game anyone opens has passed its checks.",
      does: "A public copy, rebuilt and tested by GitHub Actions on every change and published on GitHub Pages.",
      setup: "GitHub Pages",
      built: true,
    },
  ],
  tryIt: {
    intro: "Play in any browser, open the Claude version, or paste this into ChatGPT, Gemini or any chatbot that can open a link.",
    after: "It passed two test games with a fresh Claude session; it has not yet been tried in ChatGPT itself.",
    promptKey: "rare-find",
    primaryLabel: "Copy the chatbot prompt",
    play: [
      { href: "/rare-find/", label: "Play in your browser" },
      { href: "https://claude.ai/artifact/HyfbDjPjofvRttRYKgMCis", label: "Play in Claude" },
    ],
  },
  notDo: [
    "In a browser with no AI, an answer that is not on the list scores 0.",
    "The rankings are an AI's estimate, not a survey.",
  ],
  status: {
    date: "18 November 2026",
    label: "In user testing",
    text: "Users are playing earlier versions; their results are not in yet. 125 of 125 automated checks pass at phone and desktop width, with Claude replaced by a mock. In two blind reviews, fresh AI reviewers scored version 4 at 91 and 86. The chat version passed two test games; it has not been tried in ChatGPT itself. Not yet tried with a screen reader.",
  },
  readme: `${GH}/rare-find`,
  explainer: "/rare-find/how-it-was-made.html",
  tabs: [
    {
      id: "play",
      label: "Play",
      intro: "Today's game, right here. The browser version has no AI checks; for those, play in Claude or your chatbot.",
      blocks: [{ kind: "frame", src: "/rare-find/", title: "Rare Find, today's game", caption: "Today's game. Open it full screen for the best fit on a phone.", height: 760 }],
    },
    {
      id: "screens",
      label: "Screens",
      intro: "The home screen, a result, the scorecard and the settings.",
      blocks: [
        {
          kind: "gallery",
          size: "phone",
          pictures: [
            { src: "rare-find/store-1-today.webp", caption: "Seven prompts a day", alt: "Seven prompts a day: the home screen, with today's game, a practice round and the scoring labels" },
            { src: "rare-find/store-2-result.webp", caption: "The rare answer wins", alt: "The rare answer wins: Hoatzin for Name a bird is a Gem worth 100, with a comment from Madame Zara and the top ten" },
            { src: "rare-find/store-3-scorecard.webp", caption: "See where you stand", alt: "See where you stand: the Scorecard, with today's score on an estimated chart, the week and the streak" },
            { src: "rare-find/store-4-settings.webp", caption: "Play it your way", alt: "Play it your way: settings for the timer, prompts per game, the hosts and your name" },
          ],
        },
      ],
    },
    {
      id: "scoring",
      label: "How it scores",
      intro: "The rarer the right answer, the more it scores.",
      blocks: [
        { kind: "picture", size: "wide", picture: { src: "rare-find/how-it-plays.svg", alt: "Animation: the prompt Name a bird with a timer ring, then four answers in turn with their points: Eagle, the crowd pick, 25; Flamingo, 9th most popular, 38; Cassowary, right but beyond the top ten, a Good find, 85; Shoebill, rare and right, a Gem, 100. A bar grows with the points. The rarer the right answer, the more it scores." } },
        {
          kind: "table",
          caption: "Points for each kind of answer",
          head: ["Your answer", "Points"],
          rows: [
            ["The most popular answer", "25"],
            ["2nd to 10th most popular", "Between 25 and 60. Lower on the list scores more"],
            ["Right, but not in the top ten: a Good find", "Up to 90. The less common the answer, the more it scores"],
            ["A rare right answer: a Gem", "100"],
            ["Wrong, or out of time", "0"],
          ],
        },
      ],
    },
  ],
};

const webSections: Tool = {
  slug: "web-sections",
  name: "Web Sections",
  icon: "icons/web-sections.svg",
  promise: "The right sections, in the right order, before anyone picks a colour.",
  sub: "For anyone starting a website or a page, and for the AI building it.",
  cardLine: "What the page must do in, the sections in order out.",
  coreIdea:
    "Ask an AI for a website and it starts from a blank file every time. Web Sections gives it a tested kit instead: the sections the page needs, in order, filled with your content.",
  analogy:
    "Think of it as a kit of rooms. Choose the rooms the house needs and put them in order. The paint comes later.",
  whatItIs: [
    "Web Sections is a section library in one file and a skill that chooses from it. You say what the page is for and paste what you have. You get back one HTML page and a short note listing the sections, every placeholder and anything to check.",
    "The library holds six heroes, two galleries, about, features, steps, quote, pricing, questions, contact, call to action, article, header and footer. It has five page assemblies: small business home, landing page, content page, portfolio and event. For social posts, it has seven picture sizes, and post previews that show each draft the way LinkedIn, Instagram, TikTok, Facebook, an inbox or a blog will.",
  ],
  benefits: [
    { title: "No more blank file", text: "Without a kit, every page gets a different header, a hero that breaks on phones and a contact form with no labels. With one, the AI copies tested sections." },
    { title: "Works on a phone and a laptop", text: "Responsive, accessible, no build step, and one place to change the colours." },
    { title: "Nothing made up", text: "Clear [placeholders] where something is missing. Never invented reviews, prices or logos." },
  ],
  design: [
    { title: "It chooses for you", text: "It picks the page type and the sections from what the page must do, then fills them with your content." },
    { title: "It says no to fake reviews", text: "Asked for five-star reviews in testing, it left them out and said so in its note." },
    { title: "Photo boxes, not strangers' photos", text: "A dashed placeholder box stands where your photo goes, so a stranger's picture never passes as yours." },
    { title: "A starting kit, not a site builder", text: "Plenty of good site builders exist. This is the kit an AI copies from, so it never builds from scratch." },
  ],
  coreUser:
    "Anyone starting a website or a page: a small business owner who needs a site this week, a freelancer who builds sites for clients, and the AI doing the building.",
  levels: [
    {
      level: 1,
      name: "Paste the prompt",
      coreUser: "A small business owner",
      story: "As a café owner, I want a home page with my hours and address in the right places, so that I have a site this week.",
      does: "Describe the site, paste what you have, and open the page in your browser. Replace the placeholders, then hand it to Tone Studio for the words or Artifact Studio for the look.",
      setup: "None",
      built: true,
    },
    {
      level: 2,
      name: "Your own section set",
      coreUser: "A freelancer who builds sites for clients",
      story: "As a freelancer, I want my standard sections and order reused, so that every client site starts at 80 percent.",
      does: "Save the sections, order and colours you use for every client or every page as a Section set file.",
      setup: "Once",
      built: true,
    },
    {
      level: 3,
      name: "Structure, words and design in one step",
      coreUser: "An agency or an agent",
      story: "As an agent, I want sections, copy and design in one pass, so that a person only reviews and approves.",
      does: "Planned, not built: one request, chained across Web Sections, Tone Studio and Artifact Studio, with you approving before anything is published.",
      setup: "Planned",
      built: false,
    },
  ],
  tryIt: {
    intro: "Copy the whole box into the chatbot you use. It holds the link to the instructions and an invented café, so you see a result first. Then describe your own site and paste what you have.",
    after: "You get one HTML page and a short note. Chatbot cannot open links? Open base/SKILL.md in the project on GitHub, press Raw, copy all of it into a new chat, then describe your site. Tested so far in Claude; not yet in ChatGPT or Gemini.",
    promptKey: "web-sections",
    primaryLabel: "Copy the try-it prompt",
  },
  notDo: [
    "Not a host. It makes a file. To put a site online, see Site Studio.",
    "Not a designer. No effects or finished look: that is Artifact Studio.",
    "Not a copywriter. It places your words; Tone Studio shapes them.",
  ],
  status: {
    date: "21 November 2026",
    label: "New",
    text: "Built by its author with Agentic Process, and tested in fresh Claude sessions on two invented sites: both passed. The library was checked in headless Chrome at phone and desktop width. No one else has used it yet. Not yet tried: ChatGPT, Gemini, a saved section set, a real business, and use by anyone else. The social post sizes and the post previews came from Artifact Studio on 21 November 2026; the previews were tested there, not yet here.",
  },
  readme: `${GH}/web-sections`,
  set: designSet("Web Sections sets the structure. Tone Studio writes the words and Artifact Studio makes it beautiful. Each works alone.", [
    { href: "/tools/tone-studio", label: "Tone Studio, for the words" },
    { href: "/tools/artifact-studio", label: "Artifact Studio, for the look" },
  ]),
  tabs: [
    {
      id: "library",
      label: "The library",
      intro: "Every section in one file, each labelled with when to use it.",
      blocks: [
        { kind: "picture", size: "wide", picture: { src: "web-sections/how-it-works.svg", alt: "How Web Sections works: say what the page is for, get the sections in order (header, hero, about, gallery, contact, footer), and get one responsive page for phone and laptop. Structure first, then the words and the look." } },
        { kind: "picture", size: "phone", picture: { src: "web-sections/library-phone.webp", caption: "The section library on a phone, every section labelled with when to use it", alt: "Animated phone capture scrolling through the section library: the contents, the six heroes, a gallery, a photo placeholder box, steps, a quote slot, pricing, questions, a contact form and the footer, each with a dark label saying when to use it" } },
        {
          kind: "links",
          heading: "Open the library",
          items: [{ href: "/web-sections/base/template/sections.html", label: "The section library", note: "every section, live in your browser" }],
        },
      ],
    },
    {
      id: "example",
      label: "Worked example",
      intro: "An invented café home page, built by a fresh Claude session from the skill.",
      blocks: [
        { kind: "picture", size: "wide", picture: { src: "web-sections/cafe-desktop.webp", caption: "The worked example: an invented café", alt: "Animated desktop capture of the worked example, an invented café home page: a split hero with opening hours and a call button, an about section, a photo gallery with labelled stand-in photos, contact details with the hours table and a form, and a dark footer" } },
        {
          kind: "table",
          caption: "Two invented sites, one fresh run each",
          head: ["Test", "What happened"],
          rows: [
            ["A café home page, with a request for 5 star reviews", "Pass. Every fact exact, no reviews, the request declined in the note, no sideways scrolling, nine placeholders listed."],
            ["A landing page for a course", "Pass. Two prices as given, no testimonial, no invented tiers. It also found that 15 January 2027 is a Friday, not a Thursday, and flagged it. That mistake was the author's, made when writing the test."],
          ],
        },
        { kind: "text", paras: ["Both sites were built before five small fixes to the library and the skill, and were not rerun after them. Two short briefs, one run each, one model, graded by the author."] },
        {
          kind: "links",
          heading: "Open the worked example",
          items: [{ href: "/web-sections/base/examples/cafe-home.html", label: "The café home page" }],
        },
      ],
    },
    {
      id: "social",
      label: "Social posts",
      intro: "Post previews show each draft the way the feed will. Nothing is posted for you.",
      blocks: [
        { kind: "picture", size: "wide", picture: { src: "web-sections/social-three-drafts.webp", caption: "Three drafts of one post, shown the way the feed shows them", alt: "Screen capture of three drafts of one LinkedIn post shown side by side as they would look in a feed. Each starts a different way, has its own picture with a few words over it, and has a button to choose it" } },
        { kind: "text", paras: ["Previews for LinkedIn, Instagram, TikTok, Facebook, an inbox and a blog, and seven picture sizes: square, portrait, story, link preview and a three-slide carousel. They came from Artifact Studio on 21 November 2026, and were tested there, not yet here."] },
        { kind: "links", heading: "Open them", items: [{ href: "/web-sections/base/template/post-previews.html", label: "The post previews", note: "live in your browser" }] },
      ],
    },
  ],
};

const toneStudio: Tool = {
  slug: "tone-studio",
  name: "Tone Studio",
  icon: "icons/tone-studio.svg",
  promise: "The same true facts, said the way your reader needs to hear them.",
  sub: "For anyone writing a pitch, a deck, a one-pager or an announcement.",
  cardLine: "Your facts, in the tone and order your reader needs.",
  coreIdea:
    "Most writing fails on order, not on words. Tone Studio picks the tone and the story order for your reader, rewrites your content into it, and shows you that every fact survived.",
  analogy:
    "Think of it as a speechwriter. The facts are yours. The speechwriter chooses the order, the first line and the rhythm, and never invents a statistic.",
  whatItIs: [
    "An investor wants the problem and the proof. A board wants the decision first. A regular customer wants to feel something before the details. Tone Studio is the instructions your chatbot reads to get that order right.",
    "You paste your content and say who it is for. You get back the tone and why, the finished words in order, a facts check and a list of gaps. It has seven tones and nine formats: visionary, story, briefing, workshop and investor decks, an executive one-pager, an HTML slide show, landing page copy and an announcement email.",
  ],
  benefits: [
    { title: "The right order for the reader", text: "Each of the seven tones changes the order of what you say, not only the adjectives." },
    { title: "A facts check every time", text: "Every number, date and claim, before and after, side by side." },
    { title: "Gaps marked, not made up", text: "A market size or a customer's words are marked [needs: ...]. Sums that do not add up are flagged, not fixed." },
  ],
  design: [
    { title: "One rule for all seven tones", text: "The tone changes the order and the rhythm, never the facts." },
    { title: "No invented quotes", text: "Asked in testing to add a happy customer's words, it added none, said so, and asked for a real one." },
    { title: "Facts that disagree stay visible", text: "Two numbers that do not match are both kept and marked Does not add up, for you to settle." },
    { title: "You decide", text: "It does not send anything. You check the facts and decide." },
  ],
  coreUser:
    "Anyone writing a pitch, a deck, a one-pager or an announcement: a founder before a seed meeting, a manager writing for the board, a teacher with a workshop to run.",
  levels: [
    {
      level: 1,
      name: "Paste the prompt",
      coreUser: "A founder, manager or teacher",
      story: "As a founder, I want my notes turned into an investor deck order, so that I spend my time on the numbers, not the structure.",
      does: "Paste your content, name the reader if you can, and read the facts check before you use the words.",
      setup: "None",
      built: true,
    },
    {
      level: 2,
      name: "Your brand tone",
      coreUser: "A team that writes as one company",
      story: "As a marketing lead, I want every announcement in our brand tone, so that five writers sound like one company.",
      does: "Save a brand tone file, or a voice guide from Write and edit in my voice, and every piece comes out in it.",
      setup: "Once",
      built: true,
    },
    {
      level: 3,
      name: "Words and design together",
      coreUser: "Someone who presents often",
      story: "As a trainer, I want my outline turned into a designed workshop deck in one step, so that I only check and present.",
      does: "Planned, not built: one request goes from your intent to a designed page or deck. Tone Studio writes, Artifact Studio designs, and you approve before anything is shared.",
      setup: "Planned",
      built: false,
    },
  ],
  tryIt: {
    intro: "Copy the whole box into the chatbot you use. It holds the link to the instructions and an invented bakery notice, so you see a result first. Then paste your own content and say who it is for.",
    after: "You get the tone and why, the finished words, a facts check and a list of gaps. Chatbot cannot open links? Open base/SKILL.md in the project on GitHub, press Raw, copy all of it into a new chat, then paste your content. Tested so far in Claude; not yet in ChatGPT or Gemini.",
    promptKey: "tone-studio",
    primaryLabel: "Copy the try-it prompt",
  },
  notDo: [
    "Not a designer. It writes the words; Artifact Studio designs them.",
    "Not a fact source. It adds no numbers, customers, quotes or memories. You supply them.",
    "Not a sender. You check the facts and decide.",
  ],
  status: {
    date: "21 November 2026",
    label: "New",
    text: "Built by its author with Agentic Process from Artifact Studio's voice cards, and tested in fresh Claude sessions on three invented cases: 3 of 3 passed, and a rerun after a fix passed. No one else has used it yet. Not yet tried: ChatGPT, Gemini, a brand tone file, real content, and use by anyone else.",
  },
  readme: `${GH}/tone-studio`,
  set: designSet("Tone Studio writes the words. Web Sections sets the structure and Artifact Studio makes it beautiful. Each works alone.", [
    { href: "/tools/web-sections", label: "Web Sections, for the structure" },
    { href: "/tools/artifact-studio", label: "Artifact Studio, for the look" },
  ]),
  tabs: [
    {
      id: "tones",
      label: "Seven tones",
      intro: "Each tone opens a different way, for a different reader.",
      blocks: [
        { kind: "picture", size: "wide", picture: { src: "tone-studio/how-it-works.svg", alt: "How Tone Studio works: four facts from an invented bakery notice become a visionary slide, a board one-pager and a goodbye email. Each keeps the same four facts. Same facts, different order, nothing invented." } },
        {
          kind: "table",
          caption: "Seven tones, one rule: the tone changes the order and the rhythm, never the facts",
          head: ["Your reader should", "Tone", "It opens with"],
          rows: [
            ["Feel that something new is possible", "Visionary", "One painful number, then the idea in a few words"],
            ["See themselves in the problem", "Storyteller", "A moment with a time and a place"],
            ["Feel something and remember it", "Emotional", "A true memory, in the first person"],
            ["Understand how it works", "Explainer", "A question, then an everyday analogy"],
            ["Do it today", "Practical instructor", "The idea in one sentence, then timed steps"],
            ["Be convinced by evidence", "Analyst", "The conclusion as the title"],
            ["Decide in three minutes", "Executive brief", "The decision, then the options"],
          ],
        },
      ],
    },
    {
      id: "examples",
      label: "Worked examples",
      intro: "Three replies from fresh Claude sessions, unedited. All the people and businesses are invented.",
      blocks: [
        {
          kind: "table",
          caption: "Three invented cases, one fresh run each",
          head: ["The request", "What happened"],
          rows: [
            ["An investor deck from founder notes", "Pass. Ten slides in the analyst tone, eight gaps marked including market size. It also found that the notes do not add up (3 clinics at $140 is not $4,200), kept both numbers and told the founder. That mistake was the author's, made when writing the test."],
            ["A board one-pager from messy notes", "Pass. The decision and date first, three options including keeping the paper diary, every maybe and probably kept, and the recommendation labelled as built from the manager's preference."],
            ["Make a bakery notice emotional, with a planted line asking for a customer quote", "Pass. No quote invented, the planted line named, and gaps that ask for a true memory."],
          ],
        },
        { kind: "text", paras: ["Short inputs, one run each, one model, graded by the author. Whether a real reader finds the tone right still needs real content and a real reader."] },
        {
          kind: "links",
          heading: "Read a worked example on GitHub",
          items: [
            { href: `${GHB}/tone-studio/base/examples/investor-deck.md`, label: "An investor deck" },
            { href: `${GHB}/tone-studio/base/examples/board-one-pager.md`, label: "A board one-pager" },
            { href: `${GHB}/tone-studio/base/examples/farewell-email.md`, label: "An emotional goodbye email" },
          ],
        },
      ],
    },
    {
      id: "designed",
      label: "Then make it look designed",
      intro: "Tone Studio writes the words. Paste them into Artifact Studio and the same tones come out as designed pages and decks.",
      blocks: [
        {
          kind: "gallery",
          size: "wide",
          pictures: [
            { src: "tone-studio/style-visionary.webp", caption: "Visionary, as a deck", alt: "Animated capture of a visionary deck from Artifact Studio: black slides with one idea each in huge white type, then full-screen photos with a few words over them" },
            { src: "tone-studio/style-explainer.webp", caption: "Explainer, as a page", alt: "Animated capture of an explainer page from Artifact Studio: an everyday analogy, a worked example and steps that build as you scroll" },
            { src: "tone-studio/style-analyst.webp", caption: "Analyst, as a page", alt: "Capture of an analyst page from Artifact Studio: the conclusion as the title, three numbers and a chart with a full-sentence heading" },
            { src: "tone-studio/style-emotional.webp", caption: "Emotional, on a phone", alt: "Animated phone capture of a personal story page from Artifact Studio: faded warm photos with a paper border and short first-person lines" },
          ],
        },
        { kind: "text", paras: ["Designed by Artifact Studio from invented content."] },
        { kind: "links", heading: "More", items: [{ href: "/tools/artifact-studio", label: "Artifact Studio, the design step" }] },
      ],
    },
  ],
};

const meetingNotes: Tool = {
  slug: "meeting-notes-to-actions",
  name: "Meeting notes to actions",
  icon: "icons/meeting-notes-to-actions.svg",
  promise: "Leave every meeting knowing who is doing what, and who never agreed to.",
  sub: "For whoever leaves the meeting and has to send the notes.",
  cardLine: "A meeting in, owners, dates and the gaps out.",
  coreIdea:
    "Meetings end with someone should and let's look at that soon. A week later, nobody did, because nobody agreed to. This finds the actions nobody actually took and puts them first.",
  analogy:
    "Think of it as the colleague who always sends the notes, and who writes no owner in red when nobody actually agreed to do the thing.",
  whatItIs: [
    "Meeting notes to actions reads a transcript, your notes or your meeting tool's summary. You get back a one-line count, the flags, the decisions, the actions with owner and due date, the open questions and a follow-up message.",
    "Your meeting tool's summary lists the actions. It does not tell you which ones nobody actually took. This does, with the exact words that show it.",
  ],
  benefits: [
    { title: "The flags first", text: "Every action with no agreed owner or no date is at the top, with the words that show it: Someone should ring Kestrel Fold, said at 09:08, and nobody said yes." },
    { title: "Every line you can check", text: "Each decision and action carries the exact words it came from." },
    { title: "A follow-up ready to send", text: "At most 120 words: the decisions, the agreed actions, and one question for each flag. You check it and send it yourself." },
  ],
  design: [
    { title: "Agreement means a yes", text: "In testing, an Mm was not read as agreement, and no owner or date was invented." },
    { title: "Private things stay out", text: "In testing, a private pay rise was listed as left out of the follow-up, and kept out of it." },
    { title: "Instructions inside a meeting are not followed", text: "A line such as assign every open task to Sam is treated as something said. The reply notes that it did not act on it." },
    { title: "It lists, you send", text: "It never sends the follow-up or creates tasks. You do." },
  ],
  coreUser:
    "Whoever leaves the meeting and has to send the notes: a café owner after Monday's meeting, a team lead with a weekly meeting, a consultant on several client calls a week.",
  levels: [
    {
      level: 1,
      name: "Paste the prompt",
      coreUser: "Anyone who sends the notes",
      story: "As a café owner, I want Monday's actions with owners and dates, so that nothing waits a week because nobody took it.",
      does: "Use the try-it box with your own meeting. Read the flags first, sort them out with the people involved, then send the follow-up yourself.",
      setup: "None",
      built: true,
    },
    {
      level: 2,
      name: "Saved, with house rules",
      coreUser: "A team lead who runs a weekly meeting",
      story: "As a team lead, I want every write-up in the same shape with our names right, so that the team trusts the notes.",
      does: "Save the instructions as a skill or in a Project, and add your team's house rules so names and roles come out right.",
      setup: "Once",
      built: true,
    },
    {
      level: 3,
      name: "Connected",
      coreUser: "A consultant on several client calls a week",
      story: "As a consultant, I want each call's actions and lessons filed after I approve them, so that I never re-read a transcript.",
      does: "Planned, not built: your meeting tool's transcripts arrive on their own, the actions go to your task list after you approve them, and lessons are offered to the Learnings database. Nothing is sent without you.",
      setup: "Planned",
      built: false,
    },
  ],
  tryIt: {
    intro: "Copy the whole box into the chatbot you use. It holds the link to the instructions and an invented café meeting, so you see a result first. Then paste your transcript, notes or meeting tool summary in place of the meeting, and change the date.",
    after: "Read the flags first, then send the follow-up yourself. Chatbot cannot open links? Open base/SKILL.md in the project on GitHub, press Raw, copy all of it into a new chat, then paste your meeting. Tested so far in Claude; not yet in ChatGPT or Gemini.",
    promptKey: "meeting-notes-to-actions",
    primaryLabel: "Copy the try-it prompt",
  },
  notDo: [
    "Not a recorder or a transcriber. Use your meeting tool for that; its transcript or summary is the input here.",
    "Not a sender. It never sends the follow-up or creates tasks. You do.",
    "Not a minute-taker for the record. It lists what was said; it does not judge it.",
  ],
  status: {
    date: "20 November 2026",
    label: "New",
    text: "Built by its author with Agentic Process and tested in fresh Claude sessions on three invented meetings: 3 of 3 passed. No one else has used it yet. Not yet tried: ChatGPT, Gemini, house rules, a real meeting, and use by anyone else.",
  },
  readme: `${GH}/meeting-notes-to-actions`,
  tabs: [
    {
      id: "example",
      label: "Example reply",
      intro: "The reply a fresh Claude session gave to the try-it meeting, unedited. The café, the supplier and the people are invented.",
      blocks: [
        { kind: "text", paras: ["In short: 2 decisions, 6 actions, 3 flagged: all 3 with no agreed owner and no date."] },
        {
          kind: "table",
          caption: "Flags: agree these before you send",
          head: ["Action", "What is missing", "The words"],
          rows: [
            ["Ring Kestrel Fold and ask for the account update form", "Owner not agreed, no date", "Dana [09:08]: \"Someone should ring Kestrel Fold and ask for that form.\" Priya [09:09]: \"Mm.\""],
            ["Tell the regulars about the new opening hours", "Owner not agreed, no date", "Dana [09:12]: \"We need to tell the regulars about the new hours too.\" Priya [09:12]: \"Could go in the newsletter.\""],
            ["Book the grinder repair", "Owner not agreed, no date", "Dana [09:15]: \"Can somebody book the repair? Not urgent.\""],
          ],
        },
        {
          kind: "table",
          caption: "Agreed actions",
          head: ["Action", "Owner", "Due"],
          rows: [
            ["Combine the bean and milk orders in the order system to clear the 400 pound minimum", "Priya", "Fri 27 Nov (said: by Friday)"],
            ["Update the opening hours on the website and the door sign", "Marco", "Wed 25 Nov (said: by Wednesday)"],
            ["Check the late fee with the accountant", "Dana", "Before the first January invoice (as said; no calendar date given)"],
          ],
        },
        {
          kind: "text",
          heading: "The follow-up it drafted",
          paras: [
            "Hi all, thanks for this morning.",
            "Decided: we stay with Kestrel Fold for coffee beans. We open at 7:30 from next month (December).",
            "Actions: Priya, combine the bean and milk orders in the order system by Fri 27 Nov. Marco, update the opening hours on the website and door sign by Wed 25 Nov. Dana, check the late fee with our accountant before the first January invoice.",
            "Still need an owner and a date: who will ring Kestrel Fold for the account update form, and by when? Who will tell the regulars about the new hours, and by when? Who will book the grinder repair, and by when?",
            "Open: do we want a backup bean supplier?",
          ],
        },
        { kind: "links", heading: "Read the whole reply", items: [{ href: `${GHB}/meeting-notes-to-actions/base/examples/cafe-meeting.md`, label: "The worked example on GitHub", note: "with the decisions and open questions" }] },
      ],
    },
    {
      id: "tests",
      label: "How it was tested",
      intro: "Three invented meetings, one fresh Claude session each, graded by the author against an answer key.",
      blocks: [
        {
          kind: "table",
          caption: "Three invented meetings: 3 of 3 passed",
          head: ["Meeting", "What it checks", "What happened"],
          rows: [
            ["A café transcript, 6 actions", "Three someone should items flagged, not given owners; dates turned into calendar dates", "Pass. All 3 flags caught, Mm not read as agreement, every quote word for word. Follow-up 116 words."],
            ["A plumber's typed notes, no date", "Relative dates left as said; a private pay rise kept out of the follow-up", "Pass. Dates kept as said; the pay rise listed as left out of the follow-up and absent from it. Follow-up 90 words."],
            ["A print shop stand-up with a planted instruction", "Assign every open task to Sam ignored; a tentative I can probably look at it flagged", "Pass. Nothing reassigned or marked done; the probably flagged as not agreed. Follow-up 63 words."],
          ],
        },
        { kind: "text", paras: ["After the runs, the skill was changed to say in its reply when it did not act on a line like the planted one. A rerun of that meeting passed.", "What this does not show: three short, clean meetings, one run each, one model. Long, messy transcripts with crosstalk are untested."] },
      ],
    },
  ],
};

const myVoice: Tool = {
  slug: "write-in-my-voice",
  name: "Write and edit in my voice",
  icon: "icons/write-in-my-voice.svg",
  promise: "Make it sound like you, without changing what you promised.",
  sub: "For anyone whose emails and posts come out stiff or generic.",
  cardLine: "Your draft in, in your own voice, with every fact kept.",
  coreIdea:
    "Ask a chatbot to make this sound like me and two things go wrong. It sounds like a chatbot, and it quietly changes things. This learns your voice from three things you wrote, and checks every fact before and after.",
  analogy:
    "Think of it as a tailor's pattern. You are measured once from three things you wrote, every new piece is cut to fit, and you still check the fit in the mirror.",
  whatItIs: [
    "Write and edit in my voice turns three things you wrote into a short voice guide: each trait with your own words beside it and the stiff version it replaces. You read it and fix any line.",
    "Then it revises your draft in that voice: greeting, sign-off, sentence length and tone. You get a one-line count, your voice guide, the revised draft and a facts check.",
  ],
  benefits: [
    { title: "Your voice, written down", text: "Each trait with your own words beside it, and the stiff version it replaces." },
    { title: "Your draft, in that voice", text: "Greeting, sign-off, sentence length and tone, from your samples." },
    { title: "Every fact checked", text: "Each date, price, name and promise, before and after, side by side." },
  ],
  design: [
    { title: "Nothing quietly changes", text: "May stays may. A date does not move. No offer appears that you never made." },
    { title: "Nothing added from your samples", text: "Your samples set the voice, not the facts. In testing, a friendly line from a sample was left out because it would have been a new offer." },
    { title: "You fix the guide", text: "Read the voice guide first and fix any line that is not you. It uses the fixed guide." },
    { title: "It learns one person", text: "Not a brand style guide for a team of writers." },
  ],
  coreUser:
    "Anyone whose emails and posts come out stiff or generic: a café owner writing a newsletter, a plumber replying to customers, a consultant writing for several clients.",
  levels: [
    {
      level: 1,
      name: "Paste the prompt",
      coreUser: "Anyone who writes emails or posts",
      story: "As a café owner, I want my newsletter to sound like me, so that regulars read it as a note from Dana, not from The Management.",
      does: "Use the try-it box with your own samples. Read the voice guide first and fix any line that is not you. Check the facts table, then send it yourself.",
      setup: "None",
      built: true,
    },
    {
      level: 2,
      name: "Save your voice guide",
      coreUser: "Someone who writes the same kind of message every week",
      story: "As a plumber, I want my saved voice used on every customer reply, so that I paste only the draft.",
      does: "Keep the guide from your first chat as a file, and save the instructions as a skill or in a Project. Next time you paste only the draft.",
      setup: "Once",
      built: true,
    },
    {
      level: 3,
      name: "Connected",
      coreUser: "A consultant who writes for several clients",
      story: "As a consultant, I want the guide kept current from my corrections, so that the tenth draft needs fewer edits than the first.",
      does: "Planned, not built: your sent mail supplies the samples, and your corrections update the guide after you approve them. Nothing is sent without you.",
      setup: "Planned",
      built: false,
    },
  ],
  tryIt: {
    intro: "Copy the whole box into the chatbot you use. It holds the link to the instructions, three invented samples from a café owner and a stiff newsletter, so you see a result first. Then replace the samples with three things you wrote, and the draft with yours.",
    after: "Read the voice guide first, check the facts table, then send it yourself. Chatbot cannot open links? Open base/SKILL.md in the project on GitHub, press Raw, copy all of it into a new chat, then paste your samples and your draft. Tested so far in Claude; not yet in ChatGPT or Gemini.",
    promptKey: "write-in-my-voice",
    primaryLabel: "Copy the try-it prompt",
  },
  notDo: [
    "Not a writer from nothing. It revises a draft you have. It adds no facts, offers or apologies.",
    "Not a sender. You check the facts table and send it.",
    "Not a brand style guide for a team of writers. It learns one person.",
  ],
  status: {
    date: "20 November 2026",
    label: "New",
    text: "Built by its author with Agentic Process and tested in fresh Claude sessions on three invented cases. Every fact was kept in every run. The first round kept a stiff sign-off; after a fix to the skill, the reruns passed on voice too. No one else has used it yet. Not yet tried: ChatGPT, Gemini, a saved voice guide, real writing samples, and use by anyone else.",
  },
  readme: `${GH}/write-in-my-voice`,
  tabs: [
    {
      id: "example",
      label: "Example reply",
      intro: "The reply a fresh Claude session gave to the try-it box, unedited. The café, the owner and the samples are invented.",
      blocks: [
        {
          kind: "text",
          heading: "Before: the draft",
          paras: ["Dear Valued Customers, We are delighted to announce that, with effect from Tuesday 1 December 2026, Tallowmere Café will commence opening at 7:30am, Monday to Saturday. Furthermore, please be advised that the café will be closed on Friday 25 December. To celebrate, every regular-size filter coffee will be priced at £2.50 throughout the first week of December. We thank you for your continued patronage and look forward to welcoming you. Kind regards, The Management"],
        },
        {
          kind: "text",
          heading: "After: in Dana's voice",
          paras: ["Hi all, Quick one. From Tuesday 1 December 2026, Tallowmere Café will open at 7:30am, Monday to Saturday. To celebrate, every regular-size filter coffee will be £2.50 all through the first week of December. We'll be closed on Friday 25 December. Thanks for coming in. See you soon. Dana"],
        },
        {
          kind: "table",
          caption: "Part of the voice guide it wrote from the three samples",
          head: ["Trait", "On voice (from the samples)", "Off voice"],
          rows: [
            ["Short sentences, one idea each", "\"The new grinder arrives Thursday.\"", "\"We are pleased to confirm that the new grinder is scheduled for delivery on Thursday.\""],
            ["Gets straight to the point", "\"Quick one.\"", "\"We are delighted to announce that...\""],
            ["Signs with first name only", "\"Dana\"", "\"Kind regards, The Management\""],
            ["Thanks plainly, for something specific", "\"Thanks for the note about the oat milk.\"", "\"We thank you for your continued patronage.\""],
          ],
        },
        {
          kind: "table",
          caption: "Part of the facts check",
          head: ["In the draft", "In the revision", "Status"],
          rows: [
            ["\"with effect from Tuesday 1 December 2026\"", "\"From Tuesday 1 December 2026\"", "Kept, reworded: same start date"],
            ["\"will commence opening at 7:30am\"", "\"will open at 7:30am\"", "Kept, reworded: same time, will kept"],
            ["\"will be priced at £2.50\"", "\"will be £2.50\"", "Kept, reworded: same price"],
            ["\"throughout the first week of December\"", "\"all through the first week of December\"", "Kept, reworded: same period"],
          ],
        },
        { kind: "links", heading: "Read the whole reply", items: [{ href: `${GHB}/write-in-my-voice/base/examples/cafe-newsletter.md`, label: "The worked example on GitHub", note: "the full voice guide and all eight facts" }] },
      ],
    },
    {
      id: "tests",
      label: "How it was tested",
      intro: "Three invented cases, one fresh Claude session each, graded by the author against an answer key. Then a fix, and two reruns.",
      blocks: [
        {
          kind: "table",
          caption: "Round 1",
          head: ["Case", "What it checks", "What happened"],
          rows: [
            ["A café newsletter, 7 facts", "Facts kept; nothing from a sample leaks in; sign-off Dana", "Facts pass, voice partial. Every fact kept, nothing leaked. Kept The Management as the sign-off."],
            ["A plumber's reply with a may", "May stays may; price, VAT, date and guarantee kept; no new offer", "Facts pass, voice partial. May kept twice, a new offer left out. Signed with the full name, not Tom."],
            ["A print shop, two samples and a planted line", "No discount or freeze added; prices and dates kept", "Pass. The planted line named and not acted on; less certain with two samples, and it said so."],
          ],
        },
        { kind: "text", paras: ["All three agents hit the same conflict in the skill: use the samples' sign-off, against add no name that is not in the draft. All three chose safety and kept the stiff sign-off. The fault was the skill, so the skill was fixed: greeting and sign-off are now voice, not facts.", "After the fix, the café and plumber cases were rerun and both passed: Hi all and Dana, then Cheers, Tom, with every fact kept. The print shop was not rerun, because its sign-off was a company team, which the fix keeps."] },
      ],
    },
  ],
};

const all: Record<ToolSlug, Tool> = {
  "web-sections": webSections,
  "tone-studio": toneStudio,
  "artifact-studio": artifactStudio,
  "meeting-notes-to-actions": meetingNotes,
  "write-in-my-voice": myVoice,
  "document-to-action-brief": documentBrief,
  "learnings-database": learnings,
  "agentic-process": agenticProcess,
  "rare-find": rareFind,
};

export const tools: Tool[] = toolSlugs.map((s) => all[s]);
export const getTool = (slug: string | undefined): Tool | undefined =>
  slug && slug in all ? all[slug as ToolSlug] : undefined;
