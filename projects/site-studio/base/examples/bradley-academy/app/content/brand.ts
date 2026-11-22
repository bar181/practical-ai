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
    { strong: "15 theorems", rest: "mechanically checkable, in AISP's calculus" },
    { strong: "Published tools", rest: "AISP on npm and crates.io" },
    { strong: "BAR Observatory", rest: "16 Rust crates on crates.io" },
    { strong: "Founding Director", rest: "Agentics Foundation, 60 locations" },
  ],

  statement: "Most AI solves the same problem from scratch every time. My research is about machines that keep what they learn.",

  // Public results only, each with its source.
  results: {
    heading: "Evidence you can check",
    items: [
      { big: "Under 2%", from: "against 40 to 65% in expert prose, per hop", text: "Ambiguity between models on the AISP open-core evidence set, scored by judges from a different model. Method and limits in the paper.", href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md" },
      { big: "72 of 72", from: "two blind models, from two vendors", text: "Gemini and GPT-5.5 read three AISP documents with no glossary or examples and recovered every decision point. A pilot, one run each, with its limits published.", href: "https://github.com/bar181/aisp-open-core/blob/main/evidence/head-to-head-llm-models/test-results-summary.md" },
      { big: "99 of 101", from: "fields matched in an outside reproduction", text: "BAR Observatory reports rebuild byte for byte from an unchanged record. Installed from crates.io alone; the two fields that differ are documented.", href: "https://github.com/bar181/bar-observatory#evidence-verified-not-asserted" },
    ],
  },

  // Where a reviewer goes next, in order.
  next: {
    heading: "Check it yourself",
    items: [
      { href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md", label: "Read the paper", note: "AISP: a proof-carrying symbolic protocol for AI cognition. Seven contributions, the assumptions and the failure modes." },
      { href: "https://github.com/bar181/aisp-open-core/tree/main/evidence", label: "Check the evidence", note: "The ambiguity results and the blind cross-vendor pilot, each with what it does not show." },
      { href: "https://www.npmjs.com/package/aisp-validator", label: "Run the validator", note: "npx aisp-validator validate spec.aisp, or cargo install aisp." },
      { href: "https://github.com/bar181/aisp-open-core/blob/main/AI_GUIDE.md", label: "Give AISP to your agent", note: "AI_GUIDE.md is the specification an agent reads. No fine-tuning." },
      { href: "https://github.com/bar181/bar-observatory", label: "Record your own agent", note: "Install BAR Observatory in Claude Code, then run tests/verify.sh to reproduce the published example." },
    ],
  },

  range: {
    heading: "Where the research goes",
    lead: "The same methods, taught at two levels.",
    items: [
      { who: "Research", text: "Deterministic agents that prove what they did and keep what they learn, built on AISP and BAR Observatory.", link: { href: "/research", label: "Research" } },
      { who: "Engineering teams", text: "Advanced agentic engineering for senior developers and enterprise teams, through the Agentics Foundation and Agentic Learning Labs.", link: { href: "/about", label: "About" } },
      { who: "Small teams", text: "Practical AI for businesses of 10 to 30 people, with agentic office hours: ask the tools any question, any time. More than 900 people taught.", link: { href: "/tools#office-hours", label: "Agentic office hours" } },
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
    heading: "Further results, on request",
    text: "Work on learning and experience transfer continues. Results go to research partners on request, once each one is verified. They are not published here.",
  },
};

export const research = {
  metaTitle: "Research: one reading for every instruction, a receipt for every session",
  metaDescription:
    "Bradley Ross's research: AISP, a proof-carrying symbolic protocol for AI-to-AI communication, and BAR Observatory, a deterministic record and memory of what agents did. The public evidence and its limits.",
  hero: {
    kicker: "Research",
    title: "One reading for every instruction. A receipt for every session.",
    lead: "AISP gives agents a formal language in which every instruction parses one way and carries a checkable evidence block. BAR Observatory records what the agents then did, reproducibly, and lets the next agent ask what was already tried.",
  },
  results: {
    heading: "Public evidence",
    note: "Everything below is public, with its method and its limits. Results on learning and transfer are shared with partners on request.",
    items: [
      { big: "Under 2%", from: "against 40 to 65% in expert prose, per hop", text: "Ambiguity between models. Each document has a decision-point set fixed in advance; 32 completions are scored by a majority of three judges from a different model.", note: "The paper names the gaps: no human agreement score yet, and judges may share biases.", href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md" },
      { big: "72 of 72", from: "two blind models, from two vendors", text: "Gemini and GPT-5.5 read three AISP documents with no glossary, examples or system prompt, and recovered every decision point, interpreting the symbols rather than reciting them.", note: "A pilot: one run per model, textbook concepts, no prose baseline yet.", href: "https://github.com/bar181/aisp-open-core/blob/main/evidence/head-to-head-llm-models/test-results-summary.md" },
      { big: "15 theorems", from: "over 12 typed inference rules", text: "Mechanically checkable theorems in AISP's natural-deduction calculus, including termination and tamper-evidence of content-addressed memory, with a categorical semantics for validation.", href: "https://github.com/bar181/aisp-open-core/blob/main/formal-papers/aisp-protocol.md" },
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
      { name: "Learn", line: "Knowledge kept with its evidence, and carried to new problems", status: "In research, on request" },
    ],
  },
  method: "Next, as the paper states: independent replication on a public benchmark, with decision-point sets registered in advance, judges from other vendors and human agreement scores.",
  speaking: "Keynote speaker on deterministic AI. Founding Director and Education Director of the Agentics Foundation.",
};
