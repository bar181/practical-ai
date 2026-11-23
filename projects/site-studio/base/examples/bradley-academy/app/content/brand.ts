// The words for Bradley's own pages: the home page and Research.
// A personal profile, not a services page: Bradley first (25 years building software, data
// prediction, agentic research), then the systems he built with evidence a reader can inspect,
// then teaching at every level and his public roles. Services are on WiseGeo.
// Every number below is public, in github.com/bar181/aisp-open-core or github.com/bar181/bar-observatory
// (read 22 November 2026), and links to its method and limits. Unpublished research results
// (learning and transfer) stay off the site: Bradley shares them with partners on request, once
// each is verified (his decision, 22 November 2026). Do not add them back without his approval.
// Position: senior agentic engineer and research lead (Bradley, 22 November 2026). He also allows
// "agentic architect". US spelling.

export const contact = {
  linkedin: { href: "https://www.linkedin.com/in/bradaross/", label: "Connect on LinkedIn" },
  earlyAccess: { href: "https://www.linkedin.com/in/bradaross/", label: "Connect on LinkedIn" },
  earlyNote: "Already connected? Send a short note on your group and your interest.",
  paper: { href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md", label: "Read the AISP paper" },
};

export const brand = {
  metaTitle: "Bradley Ross, senior agentic engineer and research lead",
  metaDescription:
    "Bradley Ross: 25 years architecting and building software, from MVP to global production. Specialist in data prediction and advanced data science. Creator of AISP and BAR Observatory, and a teacher at every level.",

  hero: {
    kicker: "Senior agentic engineer and research lead",
    title: "Bradley Ross",
    lead: "A Harvard University graduate with twenty-five years architecting and building software for companies, from the first MVP to global production. My specialty is data prediction and advanced data science. Today I lead research in deterministic AI and build agentic systems on it.",
    primary: { href: "#systems", label: "See what I have built" },
  },

  proof: [
    { strong: "Harvard University", rest: "ALM graduate, 4.0 GPA" },
    { strong: "25 years", rest: "software architect and developer" },
    { strong: "MVP to global production", rest: "from start-up to enterprise" },
    { strong: "Data prediction", rest: "and advanced data science" },
    { strong: "Creator", rest: "of AISP and BAR Observatory" },
  ],

  career: {
    heading: "Twenty-five years of production software",
    lead: "I have architected and built software for companies for twenty-five years, from a first MVP to systems in production around the world. Data has been the thread throughout: prediction, large-scale analytical automation and advanced data science, long before agents.",
    points: [
      { title: "Architecture and delivery", text: "From the first release to global, production-grade systems, for companies from start-up to enterprise." },
      { title: "Data prediction", text: "My specialty: predictive models and advanced data science, built into systems people rely on." },
      { title: "Agentic engineering", text: "The same discipline, applied to agents: deterministic by design, with a record of what they did." },
    ],
  },

  // The systems, each with determinism evidence from its public repository.
  systems: {
    heading: "Systems I have built",
    lead: "Two open systems from my research. Each makes agents behave the same way every time, and each comes with evidence you can inspect.",
    items: [
      {
        name: "AISP",
        kind: "Research, open core under the MIT licence",
        line: "A proof-carrying protocol for AI-to-AI instructions, written in 512 symbols from formal mathematics, with a fixed grammar and an evidence block in every document.",
        evidence: [
          { big: "One parse", from: "for every well-formed document", text: "The grammar is deterministic: every AISP document parses to exactly one syntax tree. The specification states it in its own notation.", code: "⊢deterministic:∀D:∃!AST.parse(D)→AST", href: "https://github.com/bar181/aisp-open-core/blob/main/AI_GUIDE.md" },
          { big: "Same story", from: "from one specification, two models from two vendors", text: "Opus 4.5 and GPT-5.2 each wrote a story from one AISP specification. The plot, the character arc and the quotable line matched; the writing style did not. The write-up scores the alignment at 98%.", note: "One specification, one run per model.", href: "https://github.com/bar181/aisp-open-core/tree/main/evidence/creative-short-story" },
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
          { big: "Byte for byte", from: "the same record, the same report", text: "Reports rebuild identically from an unchanged record. Installed from crates.io alone, an outside reproduction matched 99 of 101 fields; the two that differ are documented as expected to vary.", href: "https://github.com/bar181/bar-observatory#evidence-verified-not-asserted" },
          { big: "60 errors", from: "the agent's own summary never mentioned", text: "Surfaced by BAR Observatory in one real captured session, and still queryable by a person or an agent.", href: "https://github.com/bar181/bar-observatory#why-developers-use-it" },
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
      text: "The skills, prompts and examples I build from what I teach. Thirteen tools, each with a worked example and its test results, free to reuse under the Apache 2.0 licence.",
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
    text: "Research partners work with the commercial-grade AISP, including the full Pocket architecture and mass-parallel machine learning on CPU, and see results on learning and transfer before publication, once each is verified. Not open to the public.",
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
    title: "One reading for every instruction. A receipt for every session.",
    lead: "Deterministic AI: agents that read an instruction one way, act the same way every time, and leave a record that rebuilds byte for byte. AISP is the language for the first; BAR Observatory is the record.",
  },
  results: {
    heading: "Determinism, with evidence",
    note: "Public results from the open core and BAR Observatory, each linked to its source. Results on learning and transfer are shared with research partners.",
    items: [
      { big: "One parse", from: "for every well-formed AISP document", text: "AISP's grammar is deterministic: a document parses to exactly one syntax tree, and the specification states it in its own notation.", code: "⊢deterministic:∀D:∃!AST.parse(D)→AST", href: "https://github.com/bar181/aisp-open-core/blob/main/AI_GUIDE.md" },
      { big: "Same story", from: "from one specification, two models", text: "Opus 4.5 and GPT-5.2 each wrote a story from one AISP specification. Plot, character arc and the quotable line matched; style did not. Scored at 98% semantic alignment in the write-up.", note: "One specification, one run per model.", href: "https://github.com/bar181/aisp-open-core/tree/main/evidence/creative-short-story" },
      { big: "Six of six", from: "ambiguities removed from a game's rules", text: "A six-rule prose specification of tic-tac-toe holds six ambiguities, from turn order to the end state. The AISP version removes all six by construction.", note: "A case study in the AISP paper.", href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md" },
      { big: "Byte for byte", from: "the same record, the same report", text: "BAR Observatory reports rebuild identically. Installed from crates.io alone, an outside reproduction matched 99 of 101 fields; the two that differ are documented as expected to vary.", href: "https://github.com/bar181/bar-observatory#evidence-verified-not-asserted" },
      { big: "60 errors", from: "the agent's own summary never mentioned", text: "Surfaced by BAR Observatory in one real captured session, and still queryable by a person or an agent.", href: "https://github.com/bar181/bar-observatory#why-developers-use-it" },
      { big: "72 of 72", from: "weighted points, for each of two blind models", text: "Gemini and GPT-5.5 read three AISP documents with no glossary, examples or system prompt, and recovered every decision point.", note: "A pilot: one run per model, on a test both reached the maximum of.", href: "https://github.com/bar181/aisp-open-core/blob/main/evidence/head-to-head-llm-models/test-results-summary.md" },
      { big: "15 theorems", from: "14 at protocol level, 1 at document level", text: "Stated in the AISP paper (version 3.0) over 12 typed inference rules, including that binding is total and deterministic, and that search terminates. The AISP 5.1 specification carries the 14 protocol-level theorems.", href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md" },
      { big: "Under 2%", from: "ambiguity per hop, against 40 to 65% in expert prose", text: "Measured on the AISP open-core evidence set: 32 completions per document, scored by a majority of three judges from a different model.", note: "Judged by models, without a human agreement score yet.", href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md" },
    ],
  },
  layers: {
    heading: "The system",
    items: [
      { name: "Specify", line: "AISP: one formal reading for every instruction", status: "Open source" },
      { name: "Prove", line: "BAR Observatory: a byte-identical receipt for every session", status: "Open source" },
      { name: "Remember", line: "Cross-run memory over MCP: the next agent asks what was tried", status: "Open source" },
      { name: "Learn", line: "The Pocket architecture: knowledge kept with its evidence, carried to new problems", status: "Commercial grade" },
      { name: "Scale", line: "Mass-parallel machine learning on CPU", status: "Commercial grade" },
    ],
  },
  method: "The open core is MIT licensed: the specification, the paper, a converter and validator on npm, and a Rust crate on crates.io. The commercial grade is for research partners.",
  speaking: "Keynote speaker on deterministic AI. Founding Director and Education Director of the Agentics Foundation.",
};
