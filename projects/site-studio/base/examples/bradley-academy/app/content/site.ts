// Site-wide words: the brand, the home page and About Bradley.
// Facts come from the repository's root README. Change them there first.

export const site = {
  brand: "Bradley Academy",
  product: "Practical AI",
  url: "https://bar181.github.io/practical-ai",
  source: "https://github.com/bar181/practical-ai",
  sourceLabel: "bar181/practical-ai",
  linkedin: "https://www.linkedin.com/in/bradaross/",
  description:
    "Free Practical AI tools from Bradley Academy: expert work from the AI you already use, on the jobs you repeat. Paste one prompt into Claude, ChatGPT or Gemini to start.",
};

export const home = {
  title: "Expert work from the AI you already use.",
  lead: "Free tools for the jobs you repeat. Each one is a prompt you paste into Claude, ChatGPT or Gemini, and it makes your AI work like a trained member of your team.",
  // The core idea, in three parts.
  idea: {
    analogy:
      "Think of your AI as a smart intern. Bright and fast, but new to your work. Give it a vague request and you get a vague result. Give it a clear brief, a worked example and a standard to meet, and it does the job well, every time.",
    heading: "Each tool is that brief, written once",
    points: [
      { title: "Quality you can check", text: "Every tool puts the answer first, invents nothing, and marks what is missing for you to fill." },
      { title: "The same standard every time", text: "Save a tool once and every chat starts from it, not from a blank page." },
      { title: "You stay in charge", text: "The AI does what it is good at. Nothing is sent, posted, paid or published without you." },
    ],
  },
  levels: {
    heading: "Start in one minute, grow when you are ready",
    intro: "Every tool comes in up to three levels. Start with the first; nothing to install.",
    steps: [
      { title: "Paste a prompt", text: "Copy one prompt into the chatbot you already use, with your own notes or document. No setup." },
      { title: "Make it your standard", text: "Save the instructions once in a Project, a Gem or as a skill, so every chat already knows them." },
      { title: "Connect it", text: "For teams and builders: a shared database, an agent connection or a coding agent that runs the whole job." },
    ],
  },
  starter: {
    heading: "Not sure where to start?",
    text: "Paste this into Claude, ChatGPT or Gemini. Your chatbot reads the tools and makes you a page on how they could help in your work.",
  },
};

export const about = {
  title: "About Bradley Ross",
  lead: "Bradley Ross is an agentic AI architect and developer for businesses of every size, from start-up to enterprise.",
  facts: [
    { title: "Specialty", text: "Deterministic AI, and advanced AI research into AI with learning transfer abilities." },
    { title: "Harvard CS50", text: "Ten terms as a Teaching Fellow." },
    { title: "Agentics Foundation", text: "Founding Director and Education Director, teaching alongside leading agentic engineers." },
    { title: "Practical AI training", text: "12 courses, over 40 cohorts and more than 900 students." },
  ],
  why:
    "These tools come out of that teaching: what people ask for most, in the form that worked in the room. Bradley Academy is where they live for people who will never open GitHub. The source code stays open at bar181/practical-ai, for builders who want to look inside or make their own.",
  contact: "More information, training or feedback: connect on LinkedIn.",
};
