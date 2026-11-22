// The words for Bradley's own pages: the home page and Research.
// A personal profile, not a services page: the contribution first, then evidence a reader can check.
// Every number below is public, in github.com/bar181/aisp-open-core or github.com/bar181/bar-observatory
// (read 22 November 2026), and links to its method and limits. Unpublished research results
// (learning and transfer) stay off the site: Bradley shares them with partners on request, once
// each is verified (his decision, 22 November 2026). Do not add them back without his approval.
// Title: Agentic Architect and Researcher. Bradley also allows "agentic engineer" (his decision,
// 22 November 2026, for a global audience). US spelling.

export const contact = {
  linkedin: { href: "https://www.linkedin.com/in/bradaross/", label: "Connect on LinkedIn" },
  earlyAccess: { href: "https://www.linkedin.com/in/bradaross/", label: "Connect on LinkedIn" },
  earlyNote: "Already connected? Send a short note on your group and your interest.",
  paper: { href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md", label: "Read the AISP paper" },
};

export const brand = {
  metaTitle: "Bradley Ross, Agentic Architect and Researcher",
  metaDescription:
    "Bradley Ross created AISP, a proof-carrying symbolic protocol for AI-to-AI communication, and BAR Observatory, a deterministic flight recorder and memory for agent sessions. Open source, with the evidence.",

  hero: {
    kicker: "Bradley Ross, Agentic Architect and Researcher",
    title: "Agents that read every instruction one way, and prove what they did.",
    lead: "I created AISP, a proof-carrying symbolic protocol for AI-to-AI communication, and BAR Observatory, a deterministic flight recorder and memory for agent sessions. Both are open source, with the evidence beside them.",
  },

  // The work, not credentials. Credentials are on About.
  proof: [
    { strong: "Creator of AISP", rest: "paper, specification and tools, MIT licence" },
    { strong: "15 theorems", rest: "in the AISP paper's calculus" },
    { strong: "Published tools", rest: "AISP on npm and crates.io" },
    { strong: "BAR Observatory", rest: "16 Rust crates on crates.io" },
    { strong: "Founding Director", rest: "Agentics Foundation, 60 locations" },
  ],

  statement: "Most AI solves the same problem from scratch every time. My research is about machines that keep what they learn.",

  // Public results only, each with its source.
  results: {
    heading: "Selected results",
    items: [
      { big: "Under 2%", from: "against 40 to 65% in expert prose, per hop", text: "Ambiguity between models on the AISP open-core evidence set, scored by judges from a different model. Method and limits in the paper.", href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md" },
      { big: "72 of 72", from: "weighted points, for each of two blind models", text: "Gemini and GPT-5.5 read three AISP documents with no glossary or examples and recovered every decision point. A pilot: one run per model, on a test both models maxed out.", href: "https://github.com/bar181/aisp-open-core/blob/main/evidence/head-to-head-llm-models/test-results-summary.md" },
      { big: "99 of 101", from: "fields matched in an outside reproduction", text: "BAR Observatory reports rebuild byte for byte from an unchanged record. Installed from crates.io alone; the two fields that differ are documented.", href: "https://github.com/bar181/bar-observatory#evidence-verified-not-asserted" },
    ],
  },

  // Where a reader goes next, in order.
  next: {
    heading: "Explore AISP",
    items: [
      { href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md", label: "Read the paper", note: "AISP: a proof-carrying symbolic protocol for AI cognition. Seven contributions, the assumptions and the failure modes." },
      { href: "https://github.com/bar181/aisp-open-core/tree/main/evidence", label: "Check the evidence", note: "The ambiguity results and the blind cross-vendor pilot." },
      { href: "https://www.npmjs.com/package/aisp-validator", label: "Run the validator", note: "npx aisp-validator validate spec.aisp, or cargo install aisp." },
      { href: "https://github.com/bar181/aisp-open-core/blob/main/AI_GUIDE.md", label: "Give AISP to your agent", note: "AI_GUIDE.md is the specification an agent reads. No fine-tuning." },
      { href: "https://github.com/bar181/bar-observatory", label: "Record your own agent", note: "Install BAR Observatory in Claude Code and see what your agent really did, session by session." },
    ],
  },

  range: {
    heading: "Research, and teaching it",
    lead: "I teach what I research: to engineers building agents, and to business teams adopting them, as I did for ten terms as a Harvard CS50 Teaching Fellow.",
    items: [
      { who: "Research", text: "Deterministic agents that prove what they did and keep what they learn, built on AISP and BAR Observatory.", link: { href: "/research", label: "Research" } },
      { who: "Engineering teams", text: "Advanced agentic engineering for senior developers and enterprise teams, through the Agentics Foundation and Agentic Learning Labs.", link: { href: "/about", label: "About" } },
      { who: "Business teams", text: "Practical AI for businesses of 10 to 30 people, with agentic office hours: ask the tools any question, any time. More than 900 people taught.", link: { href: "/tools#office-hours", label: "Agentic office hours" } },
    ],
  },

  openSource: {
    heading: "Open work",
    items: [
      { href: "https://github.com/bar181/aisp-open-core", label: "AISP open core", note: "paper, specification, converter and validator, Rust crate" },
      { href: "https://github.com/bar181/bar-observatory", label: "BAR Observatory", note: "deterministic receipts and cross-run memory for agent sessions" },
      { href: "https://github.com/bar181/practical-ai", label: "Practical AI", note: "tools for everyday work" },
    ],
  },

  // The network, stated plainly. The community size is from agentics.org (checked 22 Nov 2026);
  // the 60 locations are from Bradley.
  network: {
    heading: "Network",
    text: "Founding Director of the Agentics Foundation, a global community of more than 100,000 agentic developers, researchers and builders, with chapters in 60 locations.",
    link: { href: "https://agentics.org", label: "agentics.org" },
  },

  earlyAccess: {
    heading: "For research partners",
    text: "Research partners work with the commercial-grade AISP, including the full Pocket architecture and mass-parallel machine learning on CPU, and see results on learning and transfer before publication, once each is verified. Not open to the public.",
  },
};

export const research = {
  metaTitle: "Research: one reading for every instruction, a receipt for every session",
  metaDescription:
    "Bradley Ross's research: AISP, a proof-carrying symbolic protocol for AI-to-AI communication, and BAR Observatory, a deterministic record and memory of what agents did. The public evidence and its limits.",
  hero: {
    kicker: "Research",
    title: "One reading for every instruction. A receipt for every session.",
    lead: "AISP gives agents a language of 512 mathematical symbols in which every instruction parses one way and carries its own evidence. BAR Observatory records what the agents then did, and lets the next agent ask what was already tried.",
  },
  results: {
    heading: "Selected results",
    note: "Selected public results from the open core. Results on learning and transfer are shared with research partners.",
    items: [
      { big: "Under 2%", from: "against 40 to 65% in expert prose, per hop", text: "Ambiguity between models, on the AISP open-core evidence set. Each document has a decision-point set fixed in advance; 32 completions are scored by a majority of three judges from a different model.", href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md" },
      { big: "72 of 72", from: "weighted points, for each of two blind models", text: "Gemini and GPT-5.5 read three AISP documents with no glossary, examples or system prompt, and recovered every decision point, interpreting the symbols rather than reciting them. A pilot: one run per model, and a test that does not rank models because both reached the maximum.", href: "https://github.com/bar181/aisp-open-core/blob/main/evidence/head-to-head-llm-models/test-results-summary.md" },
      { big: "15 theorems", from: "14 at protocol level, 1 at document level", text: "Stated in the AISP paper (version 3.0) over 12 typed inference rules, with selected proofs, including search termination and tamper-evidence of content-addressed memory. The AISP 5.1 specification carries the 14 protocol-level theorems.", href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md" },
      { big: "99 of 101", from: "fields matched in an outside reproduction", text: "BAR Observatory, installed from crates.io alone, rebuilt the published report. The two fields that differ are documented as expected to vary.", href: "https://github.com/bar181/bar-observatory#evidence-verified-not-asserted" },
      { big: "60 errors", from: "that the agent's own summary never mentioned", text: "Surfaced by BAR Observatory across seven real captured sessions, each still queryable by a person or an agent.", href: "https://github.com/bar181/bar-observatory#why-developers-use-it" },
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
