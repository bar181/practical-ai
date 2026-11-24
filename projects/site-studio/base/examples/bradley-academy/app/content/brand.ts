// The words for Bradley's own pages: the home page and Research.
// A personal profile, not a services page: Bradley first (25 years building software, data
// prediction, agentic research), then the systems he built with evidence a reader can inspect,
// then teaching at every level and his public roles. Services are on WiseGeo.
// Research boundary: github.com/bar181/aisp-open-core and github.com/bar181/bar-observatory are
// public, so anything in them may be used, with a link and its limits. Nothing beyond them: no
// proprietary architecture, learning processes, orchestration, optimisation, formulas, thresholds,
// settings or unpublished results. That work is discussed with research partners, never here.
// Position: senior agentic engineer and research lead (Bradley, 22 November 2026). He also allows
// "agentic architect". US spelling.

export const contact = {
  linkedin: { href: "https://www.linkedin.com/in/bradaross/", label: "Connect on LinkedIn" },
  earlyAccess: { href: "https://www.linkedin.com/in/bradaross/", label: "Connect on LinkedIn" },
  earlyNote: "Research partners: send a short note on your group and your interest. For anything else, connect on LinkedIn.",
  paper: { href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md", label: "Read the AISP paper" },
  partnerLine: "Additional research capabilities and technical findings are available for discussion with qualified research partners.",
};

export const brand = {
  metaTitle: "Bradley Ross, senior agentic engineer and research lead",
  metaDescription:
    "Bradley Ross: 25 years architecting and building software, from MVP to global production. Specialist in data prediction and advanced data science. Creator of AISP and BAR Observatory, and a teacher at every level.",

  hero: {
    kicker: "Senior agentic engineer and research lead",
    title: "Bradley Ross",
    lead: "A Harvard University graduate with twenty-five years architecting and building software for companies, from the first MVP to global production. My specialty is data prediction and advanced data science. Today I lead research in deterministic AI and build agentic systems on it.",
    actions: [
      { href: "/research", label: "Explore research" },
      { href: "/tools", label: "Try free AI tools" },
      { href: "https://www.linkedin.com/in/bradaross/", label: "Connect on LinkedIn" },
    ],
  },

  proof: [
    { strong: "Harvard University", rest: "ALM graduate, 4.0 GPA" },
    { strong: "25 years", rest: "software architect and developer" },
    { strong: "MVP to global production", rest: "from start-up to enterprise" },
    { strong: "Data prediction", rest: "and advanced data science" },
    { strong: "Creator", rest: "of AISP and BAR Observatory" },
  ],

  // Three differentiators, each with where to go next.
  career: {
    heading: "What I bring",
    lead: "Twenty-five years of production software, research in agentic AI, and teaching at every level. Each is backed by work you can open.",
    points: [
      { title: "Production software and data", text: "Twenty-five years architecting and building software for companies, from the first MVP to global production, with a specialty in predictive analytics and data systems.", link: { href: "/about", label: "Career and credentials" } },
      { title: "Agentic AI research and engineering", text: "Research lead in deterministic AI, and the engineer behind AISP and BAR Observatory: two open systems for agents that are easier to predict and inspect.", link: { href: "/research", label: "The research" } },
      { title: "Teaching and open source", text: "Ten terms as a Harvard CS50 Teaching Fellow, courses from practical AI to advanced agentic development, and open-source tools built from what I teach.", link: { href: "/tools", label: "Practical AI" } },
    ],
  },

  // The systems, each with public evidence, its kind and its limits.
  systems: {
    heading: "Systems I have built",
    lead: "Two open systems from my research. Both aim at agents that are easier to predict and inspect. Each result below links to its public evidence and says what it does not show.",
    items: [
      {
        name: "AISP",
        kind: "Open core, MIT licence",
        line: "A proof-carrying protocol for AI-to-AI instructions, written in 512 symbols from formal mathematics, with a fixed grammar and an evidence block in every document.",
        evidence: [
          { big: "One parse", kind: "Formal property", from: "for every well-formed document", text: "AISP's grammar is deterministic: a well-formed document parses to exactly one syntax tree. The specification states it in its own notation.", code: "⊢deterministic:∀D:∃!AST.parse(D)→AST", limits: "A property of the grammar. It does not guarantee what a model does with the document.", href: "https://github.com/bar181/aisp-open-core/blob/main/AI_GUIDE.md" },
          { big: "Same story", kind: "Experimental finding", from: "from one specification, two models", text: "Opus 4.5 and GPT-5.2 each wrote a story from one AISP specification. The plot, the character arc and the quotable line matched; the writing style did not.", limits: "One specification, one run per model, scored in the published write-up rather than by independent reviewers.", href: "https://github.com/bar181/aisp-open-core/tree/main/evidence/creative-short-story" },
        ],
        links: [
          { href: "https://github.com/bar181/aisp-open-core", label: "The code" },
          { href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md", label: "The paper" },
          { href: "https://www.npmjs.com/package/aisp-validator", label: "The validator" },
        ],
      },
      {
        name: "BAR Observatory",
        kind: "Open source, 16 Rust crates on crates.io",
        line: "A local-first flight recorder and memory for Claude Code: it records what an agent did, reports it without AI, and lets the next agent ask what was already tried.",
        evidence: [
          { big: "Byte for byte", kind: "Engineering result", from: "the same record, the same report", text: "Reports rebuild identically from an unchanged record. Installed from crates.io alone, an outside reproduction matched 99 of 101 fields; the two that differ are documented as expected to vary.", limits: "Shown on the published example record.", href: "https://github.com/bar181/bar-observatory#evidence-verified-not-asserted" },
        ],
        links: [
          { href: "https://github.com/bar181/bar-observatory", label: "The code" },
          { href: "https://github.com/bar181/bar-observatory/blob/main/tests/verify.sh", label: "Reproduce it" },
        ],
      },
    ],
  },

  statement: "Most AI solves the same problem from scratch every time. My research is about machines that keep what they learn.",

  // Teaching at every level, with Practical AI as the open-source part of it.
  teaching: {
    heading: "Teaching, at every level",
    lead: "I teach what I build, from business teams using AI for the first time to engineers building advanced agents: 14 courses, more than 900 people, over 40 cohorts.",
    levels: [
      { who: "Business teams", text: "Practical AI: a first tool in the chatbot they already use, then a saved standard, then a connected workflow.", link: { href: "/tools", label: "Practical AI" } },
      { who: "Developers", text: "Ten terms as a Harvard CS50 Teaching Fellow, and pair programming with AI for master's students.", link: { href: "/about", label: "About" } },
      { who: "Advanced agentic engineers", text: "Advanced agentic engineering for senior developers and enterprise teams, through the Agentics Foundation, where I am Education Director, and Agentic Learning Labs.", link: { href: "https://agentics.org", label: "agentics.org" } },
    ],
    practical: {
      heading: "Practical AI: my open-source teaching work",
      text: "The skills, prompts and examples I build from what I teach. Sixteen tools, each with a worked example and its test results, free to reuse under the Apache 2.0 licence.",
      actions: [
        { href: "/tools", label: "Browse the tools", note: "One job each, from meeting notes to website audits." },
        { href: "/tools/meeting-notes-to-actions", label: "Try one now", note: "Copy one prompt into Claude, ChatGPT or Gemini." },
        { href: "https://github.com/bar181/practical-ai", label: "Inspect the code", note: "Every skill, example and test result on GitHub." },
        { href: "/llms.txt", label: "Give your AI the index", note: "llms.txt: one file that tells an AI assistant where everything is." },
      ],
    },
  },

  // Public roles, named.
  network: {
    heading: "Roles and collaborations",
    items: [
      { role: "ALM graduate, and CS50 Teaching Fellow for ten terms", org: "Harvard University", text: "ALM in Digital Media Design, completed May 2026: a 4.0 in every class, and a capstone nominated for capstone of the graduating class. Also a Graduate Programming Certificate." },
      { role: "Founding Director, Treasurer and Education Director", org: "Agentics Foundation", text: "A global community of more than 100,000 agentic developers, researchers and builders, with chapters in 60 locations.", link: { href: "https://agentics.org", label: "agentics.org" } },
      { role: "Instructor", org: "Agentic Learning Labs", text: "Advanced agentic engineering for senior developers and enterprise teams." },
      { role: "Keynote speaker", org: "Deterministic AI", text: "Talks on agents that behave the same way every time." },
    ],
  },

  earlyAccess: {
    heading: "For research partners",
    text: "Additional research capabilities and technical findings are available for discussion with qualified research partners.",
  },

  // Where a reader goes next, in order (Research page).
  next: {
    heading: "Explore AISP",
    items: [
      { href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md", label: "Read the paper", note: "AISP: a proof-carrying symbolic protocol for AI cognition. Seven contributions, the assumptions and the failure modes." },
      { href: "https://github.com/bar181/aisp-open-core/tree/main/evidence", label: "Check the evidence", note: "The cross-model story, the blind pilot, the tic-tac-toe baseline and the ambiguity results." },
      { href: "https://www.npmjs.com/package/aisp-validator", label: "Run the validator", note: "npx aisp-validator validate spec.aisp, or cargo install aisp." },
      { href: "https://github.com/bar181/aisp-open-core/blob/main/AI_GUIDE.md", label: "Give AISP to your agent", note: "AI_GUIDE.md is the specification an agent reads. No fine-tuning." },
      { href: "https://github.com/bar181/bar-observatory", label: "Record your own agent", note: "Install BAR Observatory in Claude Code and see what your agent really did, session by session." },
    ],
  },

  openSource: {
    heading: "Open work",
    items: [
      { href: "https://github.com/bar181/aisp-open-core", label: "AISP open core", note: "paper, specification, converter and validator, Rust crate" },
      { href: "https://github.com/bar181/bar-observatory", label: "BAR Observatory", note: "deterministic receipts and cross-run memory for agent sessions" },
      { href: "https://github.com/bar181/practical-ai", label: "Practical AI", note: "open-source teaching work" },
    ],
  },
};

export const research = {
  metaTitle: "Research: one reading for every instruction, a receipt for every session",
  metaDescription:
    "Bradley Ross's research: AISP, a proof-carrying symbolic protocol for AI-to-AI communication, and BAR Observatory, a deterministic record and memory of what agents did. The public evidence and its limits.",
  hero: {
    kicker: "Research",
    title: "Agents you can predict and inspect.",
    lead: "My research is deterministic AI: agents that read an instruction one way and leave a record of what they did. AISP, released as an open core, is a language for the first. BAR Observatory, open source, is the record.",
  },
  results: {
    heading: "Selected public results",
    note: "Each result says what kind of claim it is, links to its public evidence, and gives its limits.",
    items: [
      { big: "One parse", kind: "Formal property", from: "for every well-formed AISP document", text: "AISP's grammar is deterministic: a well-formed document parses to exactly one syntax tree.", code: "⊢deterministic:∀D:∃!AST.parse(D)→AST", limits: "A property of the grammar, not a guarantee of model behaviour.", href: "https://github.com/bar181/aisp-open-core/blob/main/AI_GUIDE.md" },
      { big: "15 theorems", kind: "Formal property", from: "stated in the AISP paper", text: "The paper states 14 protocol-level theorems and one document-level theorem over 12 typed inference rules, with selected proofs.", limits: "A submission draft, not yet peer reviewed.", href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md" },
      { big: "Same story", kind: "Experimental finding", from: "from one specification, two models", text: "Opus 4.5 and GPT-5.2 each wrote a story from one AISP specification. Plot, character arc and the quotable line matched; style did not.", limits: "One specification, one run per model, scored in the published write-up.", href: "https://github.com/bar181/aisp-open-core/tree/main/evidence/creative-short-story" },
      { big: "72 of 72", kind: "Experimental finding", from: "weighted points, for each of two blind models", text: "Gemini and GPT-5.5 read three AISP documents with no glossary, examples or system prompt, and recovered every decision point.", limits: "A pilot: one run per model, on a test both reached the maximum of, so it does not rank models.", href: "https://github.com/bar181/aisp-open-core/blob/main/evidence/head-to-head-llm-models/test-results-summary.md" },
      { big: "Byte for byte", kind: "Engineering result", from: "the same record, the same report", text: "BAR Observatory reports rebuild identically. An outside reproduction, installed from crates.io alone, matched 99 of 101 fields; the two that differ are documented.", limits: "Shown on the published example record.", href: "https://github.com/bar181/bar-observatory#evidence-verified-not-asserted" },
    ],
    objective: { kind: "Research objective", title: "Agents that keep what they learn", text: "The longer aim: agents that keep what they learn and carry it into new problems. No results are claimed here." },
  },
  layers: {
    heading: "The work, and what is public",
    items: [
      { name: "Specify", line: "AISP: a formal language for agent instructions", status: "Open source" },
      { name: "Prove", line: "BAR Observatory: a reproducible record of each session", status: "Open source" },
      { name: "Remember", line: "BAR Observatory: the next agent can ask what was already tried", status: "Open source" },
      { name: "Learn", line: "Agents that keep what they learn", status: "Research objective" },
    ],
  },
  method: "The open core is MIT licensed: the specification, the paper draft, a converter and validator on npm, and a Rust crate on crates.io. Additional research capabilities and technical findings are available for discussion with qualified research partners.",
  speaking: "Keynote speaker on deterministic AI. Founding Director and Education Director of the Agentics Foundation.",
};
