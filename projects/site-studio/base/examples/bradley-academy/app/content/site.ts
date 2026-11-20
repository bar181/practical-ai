// Site-wide words: the brand, the home page and About Bradley.
// Facts come from the repository's root README. Change them there first.

export const site = {
  brand: "Bradley Academy",
  product: "Practical AI",
  url: "https://bar181.github.io/practical-ai",
  source: "https://github.com/bar181/practical-ai",
  sourceLabel: "bar181/practical-ai",
  linkedin: "https://www.linkedin.com/in/bradaross/",
  previewImage: "/media/shared/bradley-ross-avatar.webp",
  // Words used across pages, so a new site changes them here and nowhere else.
  labels: {
    presents: "Bradley Academy presents",
    toolsHeading: "Five tools. One job each.",
    toolsLead: "Each is a prompt you paste into the chatbot you already use. Open one to see what it does, who it is for, and real examples.",
    author: "Bradley Ross",
    authorKicker: "Meet the author",
    authorPhoto: "shared/bradley-ross.jpg",
    footerTagline: "Practical AI tools for the jobs you repeat",
    licence: "Free to use, change and share under the Apache 2.0 licence. All examples use invented businesses and data.",
    worksIn: "Free. Works in the chatbot you already use.",
  },
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
  // The facts, as one line. Each number is from a README; numbers in {braces} are set in brass.
  factsLine: "Five free tools. The one built with Agentic Process scored {93} out of 100 in a blind pilot with one reviewer. All of them grew out of courses taught to more than {900} students.",
  starter: {
    heading: "Not sure where to start?",
    text: "Paste this into Claude, ChatGPT or Gemini. Your chatbot reads the tools and makes you a page on how they could help in your work.",
  },
};

type Step = { step: string; title: string; text: string; link?: { href: string; label: string } };

export const about = {
  title: "Bradley Ross",
  role: "Agentic AI architect and developer, for businesses of every size, from start-up to enterprise.",
  lead: "Bradley Ross is an agentic AI architect and developer for businesses of every size, from start-up to enterprise.",
  specialty: "His specialty is deterministic AI, and advanced research into AI with learning transfer abilities.",
  // One line of work, from open code to the classroom.
  pipeline: <Step[]>[
    {
      step: "Open core",
      title: "AISP, a math-first language for instructions",
      text: "AISP is a specification protocol written in mathematics, so an AI agent reads an instruction the same way every time. Its open core is free under the MIT licence: the specification, a validator and converter, and a Rust crate.",
      link: { href: "https://github.com/bar181/aisp-open-core", label: "AISP open core on GitHub" },
    },
    {
      step: "Research",
      title: "Deterministic AI, and AI that transfers what it learns",
      text: "In his tests, instructions written in plain prose left 40 to 65 percent of their meaning open to interpretation. Written in AISP, under 2 percent. He leads advanced agentic research on deterministic AI and speaks on it as a keynote speaker.",
    },
    {
      step: "Instruction",
      title: "Teaching both ends of the field",
      text: "Practical AI for business people: the tools on this site, and 12 courses delivered to more than 900 students across over 40 cohorts. Advanced agentic engineering for leading engineers, through the Agentics Foundation and Agentic Learning Labs.",
    },
  ],
  credentials: [
    { title: "Harvard", text: "ALM in Digital Media Design, with a 4.0 in every class and a capstone nominated for capstone of the graduating class. A Graduate Programming Certificate. Ten terms as a CS50 Teaching Fellow." },
    { title: "Anthropic", text: "Claude Certified Architect, Professional." },
    { title: "Agentics Foundation", text: "Founding Director and Education Director of a global foundation, now in 60 locations, that helps people build the skills for better jobs." },
    { title: "WiseGeo", text: "Founder, since 2016. WiseGeo helps companies find, build and adopt practical AI." },
    { title: "Twenty-five years", text: "Across finance, software architecture, data science and agentic engineering. A former CMA." },
  ],
  why:
    "These tools come out of that teaching: what people ask for most, in the form that worked in the room. Bradley Academy is where they live for people who will never open GitHub. The source code stays open at bar181/practical-ai, for builders who want to look inside or make their own.",
  contact: "More information, training or feedback: connect on LinkedIn.",
};
