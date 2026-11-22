// Site-wide words: the brand, the home page and About Bradley.
// Facts come from the repository's root README. Change them there first.

export const site = {
  brand: "Bradley Academy",
  product: "Bradley Ross, Agentic Architect and Researcher",
  url: __SITE_URL__,
  source: "https://github.com/bar181/practical-ai",
  sourceLabel: "bar181/practical-ai",
  linkedin: "https://www.linkedin.com/in/bradaross/",
  previewImage: "/media/shared/bradley-ross-avatar.webp",
  // Words used across pages, so a new site changes them here and nowhere else.
  labels: {
    presents: "Practical AI, from Bradley Academy",
    toolsHeading: "Twelve tools. One job each.",
    toolsLead: "Each is a prompt you paste into the chatbot you already use. Open one to see what it does, who it is for, and real examples.",
    author: "Bradley Ross",
    authorKicker: "Meet the instructor",
    authorPhoto: "shared/bradley-ross.jpg",
    // The illustrated avatar, Bradley with a robot assistant: used where the page is about teaching.
    authorAvatar: "shared/bradley-ross-avatar.webp",
    footerTagline: "Agentic systems, research and Practical AI",
    licence: "Free to use, change and share under the Apache 2.0 licence. All examples use invented businesses and data.",
    worksIn: "Free. Works in the chatbot you already use.",
    homeTitle: "Practical AI: free tools for the jobs you repeat",
    seeTools: "See every tool",
    toolsListName: "Every tool",
    sourceLink: "The tools on GitHub",
    builtWith: "Built with Site Studio, in React, published by GitHub Pages.",
    operator: "Bradley Academy is operated by WiseGeo Inc., a federally incorporated Canadian company.",
    levelsHeading: "Three levels: start simple, grow when you are ready",
    projectLink: "The project on GitHub",
    readPrompt: "Read the prompt before you copy it",
    tryCardHeading: "Try it in a minute",
    tryCardText: "Copy the prompt, paste it into the chatbot you already use, and see the result.",
  },
  description:
    "Practical AI, free tools from Bradley Academy: expert work from the AI you already use, on the jobs you repeat. Paste one prompt into Claude, ChatGPT or Gemini to start.",
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
  factsLine: "Twelve free tools. Document to action brief, built with Agentic Process, scored {93} out of 100 in a blind pilot with one reviewer. They come out of courses taught to more than {900} students.",
  starter: {
    heading: "Not sure where to start?",
    text: "Paste this into Claude, ChatGPT or Gemini. Your chatbot reads the tools and makes you a page on how they could help in your work.",
  },
};

// The Practical AI page: the practical guide and the classroom behind the tools.
export const practical = {
  kicker: "Free tools, built from courses taught to more than 900 people, and used today by everyone from business owners to agentic developers.",
  guide: {
    heading: "The practical guide: your first tool in ten minutes",
    intro: "You do not need to learn AI first. Pick one job you already do, and let one tool do the first draft while you stay in charge.",
    steps: [
      { title: "Pick one job you repeat", text: "A weekly report, meeting notes, a document someone sent you. Something you will do again next week.", time: "1 minute" },
      { title: "Paste the tool's prompt", text: "Open the tool below, copy its prompt into Claude, ChatGPT or Gemini, and add your own notes or file.", time: "2 minutes" },
      { title: "Check it like a manager", text: "Read the answer first, then the gaps it marked. Check every number against your notes before you use it.", time: "5 minutes" },
      { title: "Save it as your standard", text: "Keep the instructions in a Project, a Gem or a skill, so next week starts from the same standard, not a blank page.", time: "2 minutes" },
    ],
    checkHeading: "Every tool keeps the same promises",
    check: [
      "The answer comes first, then the detail.",
      "Nothing is invented. Anything missing is marked for you to fill.",
      "Nothing is sent, posted, paid or published without you.",
    ],
  },
  // Agentic office hours: the questions people would bring to office hours, answered by their own AI
  // from the Practical AI repository, through the Practical AI guide (projects/practical-ai-guide/).
  officeHours: {
    heading: "Agentic office hours",
    text: "My office hours run on AI. Copy the prompt into your AI assistant, chatbot or coding tool, then ask it anything about Practical AI. It answers from the tools themselves and names the file it used.",
    prompt: `Read https://raw.githubusercontent.com/bar181/practical-ai/main/projects/practical-ai-guide/base/SKILL.md and follow it.
My job or question: [write it here]`,
    next: "How it works: the Practical AI guide gives your AI an index of every tool. A chat window on this page is planned.",
  },
  classroom: {
    kicker: "From the classroom",
    heading: "Taught first, then turned into tools",
    text: "I have designed 14 courses and taught more than 900 people across over 40 cohorts, from small business owners to teams at leading agentic companies. The method is first principles and core ideas, then you build your own tools. Participants report saving an average of 3.5 hours a week.",
  },
};

type Step = { step: string; title: string; text: string; link?: { href: string; label: string } };

export const about = {
  title: "Bradley Ross",
  role: "Agentic Architect and Researcher, from ten-person businesses to enterprise teams and research labs.",
  lead: "Bradley Ross is an agentic architect, researcher and educator, working with funded startups, research labs and engineering teams.",
  specialty: "My specialty is deterministic AI, and research into AI that keeps what it learns and carries it into new problems.",
  // One line of work, from open code to the classroom.
  kicker: "About",
  pathHeading: "From open code, to research, to the classroom",
  pathLead: "One line of work. What I build in the open becomes what I research, and what I research becomes what I teach.",
  pathButton: "From research to the classroom",
  credentialsHeading: "Credentials",
  record: {
    heading: "The path here",
    lead: "Twenty-five years, from the numbers to the machines that work with them.",
    steps: [
      { when: "Finance", title: "Accountant", text: "A management accountant (CMA) first: numbers, controls and audit trails." },
      { when: "At 27", title: "Self-taught programmer", text: "Taught myself to program, then automated analysis at large scale." },
      { when: "Data", title: "Data science", text: "Moved into data science and earlier forms of AI." },
      { when: "2016", title: "Founded WiseGeo", text: "Targeted marketing tools and customer data platforms, then practical AI for companies." },
      { when: "2026", title: "Harvard ALM, Digital Media Design", text: "Completed in May 2026, alongside ten terms as a Harvard CS50 Teaching Fellow." },
      { when: "Now", title: "Agentic architecture and research", text: "Deterministic agentic systems for teams, and research into AI that keeps what it learns. Claude Certified Architect, Professional." },
    ],
  },
  whyHeading: "Connect",
  contactButton: "Connect on LinkedIn",
  metaDescription: "Bradley Ross is an Agentic Architect and Researcher. His specialty is deterministic AI and research into AI that keeps what it learns. Creator of AISP, BAR Observatory and the Practical AI tools.",
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
      text: "On the AISP open-core evidence set, ambiguity between models fell from 40 to 65 percent in expert prose to under 2 percent per hop. BAR Observatory, a deterministic flight recorder and memory for agent sessions, records what agents then did. I lead advanced agentic research on deterministic AI and speak on it as a keynote speaker.",
      link: { href: "https://github.com/bar181/bar-observatory", label: "BAR Observatory on GitHub" },
    },
    {
      step: "Instruction",
      title: "Teaching both ends of the field",
      text: "Practical AI for business people: the tools on this site, and 14 courses delivered to more than 900 students across over 40 cohorts. Advanced agentic engineering for leading engineers, through the Agentics Foundation and Agentic Learning Labs.",
    },
  ],
  credentials: [
    { title: "Harvard", text: "ALM in Digital Media Design, with a 4.0 in every class and a capstone nominated for capstone of the graduating class. A Graduate Programming Certificate. Ten terms as a CS50 Teaching Fellow." },
    { title: "Anthropic", text: "Claude Certified Architect, Professional." },
    { title: "Agentics Foundation", text: "Founding Director and Education Director of a global foundation, now in 60 locations, that helps people build the skills for better jobs." },
    { title: "WiseGeo", text: "Founder, since 2016. WiseGeo helps companies find, build and adopt practical AI. Bradley Academy is operated by WiseGeo Inc., a federally incorporated Canadian company." },
    { title: "Twenty-five years", text: "Across finance, software architecture, data science and agentic engineering. A former CMA." },
  ],
  why: "Founding Director of the Agentics Foundation, a global community of more than 100,000 agentic developers, researchers and builders. Unpublished results are shared with my connections and research partners on request, once each is verified. Connect on LinkedIn with a short note.",
  contact: "More information, training or feedback: connect on LinkedIn.",
};
