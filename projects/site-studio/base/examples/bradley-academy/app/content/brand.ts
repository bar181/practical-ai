// The words for Bradley's own pages: the home page and Research.
// A personal profile, not a services page: a vision and a few proof points. Early access to the
// research is by invitation, for Bradley's connections and partners only, through LinkedIn.
// Every fact comes from Bradley.
// Title: Agentic Architect and Researcher. Bradley also allows "agentic engineer" (his decision,
// 22 November 2026, for a global audience). US spelling.

export const contact = {
  linkedin: { href: "https://www.linkedin.com/in/bradaross/", label: "Connect on LinkedIn" },
  earlyAccess: { href: "https://www.linkedin.com/in/bradaross/", label: "Connect on LinkedIn" },
  earlyNote: "Already connected? Send a short note on your group and your interest.",
};

export const brand = {
  metaTitle: "Bradley Ross, Agentic Architect and Researcher | Bradley Academy",
  metaDescription:
    "Bradley Ross: agentic AI research into deterministic AI that keeps what it learns, and teaching from ten-person teams to enterprise developers.",

  hero: {
    kicker: "Bradley Ross, Agentic Architect and Researcher",
    title: "Agentic systems that behave the same way every time.",
    lead: "Research, agentic systems and teaching, from a ten-person team's first AI workflow to frontier labs.",
  },

  // Stated facts. No adoption or user counts.
  proof: [
    { strong: "Claude Certified Architect", rest: "Professional, Anthropic" },
    { strong: "Creator of AISP", rest: "a mathematical specification language" },
    { strong: "CS50 Teaching Fellow", rest: "ten terms at Harvard" },
    { strong: "Founding Director", rest: "Agentics Foundation, 60 locations" },
    { strong: "Keynote speaker", rest: "on deterministic AI" },
    { strong: "25 years", rest: "finance, software, data, agentic AI" },
  ],

  statement: "Most AI solves the same problem from scratch every time. My research is about machines that keep what they learn.",

  results: {
    heading: "Selected results",
    items: [
      { big: "Under 2%", from: "against 40 to 60% in human prose", text: "Ambiguity in agent instructions written in AISP, a mathematical specification language." },
      { big: "17 vs 62", from: "failures before reaching the goal", text: "Milestone 1, experience transfer: a learning system built on AISP, against a machine learning baseline." },
      { big: "37 of 40", from: "after 8 chained sessions, from 38 of 40", text: "Long-term memory: knowledge kept in AISP lost 1 task in 40 across eight new sessions." },
    ],
  },

  range: {
    heading: "One practice, every level",
    lead: "Grounded in small business. Trusted by advanced teams.",
    items: [
      { who: "Small teams", text: "Practical AI for businesses of 10 to 30 people, with agentic office hours: ask the tools any question, any time. More than 900 people taught.", link: { href: "/tools#office-hours", label: "Agentic office hours" } },
      { who: "Engineering teams", text: "Advanced agentic engineering for senior developers and enterprise teams, through the Agentics Foundation and Agentic Learning Labs.", link: { href: "/about", label: "About" } },
      { who: "Research", text: "Deterministic, learning AI built on AISP and a mathematics-first method.", link: { href: "/research", label: "Research" } },
    ],
  },

  openSource: {
    heading: "Open work",
    items: [
      { href: "https://github.com/bar181/aisp-open-core", label: "AISP open core", note: "specification language, validator, Rust crate" },
      { href: "https://github.com/bar181/bar-observatory", label: "BAR Observatory", note: "deterministic receipts for agent sessions" },
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
    heading: "Early access, by invitation",
    text: "Research previews go to my connections and research partners ahead of publication. They are not open to the general public.",
  },
};

export const research = {
  metaTitle: "Research: deterministic AI that keeps what it learns | Bradley Ross",
  metaDescription:
    "Bradley Ross's research: deterministic agents built on AISP, a mathematical specification language, that prove what they did and carry experience to new problems.",
  hero: {
    kicker: "Research",
    title: "Deterministic AI that keeps what it learns.",
    lead: "Built on AISP, a mathematical specification language, so agents read every instruction one way, prove what they did, and carry experience to new problems.",
  },
  results: {
    heading: "Milestones",
    note: "An ongoing development process. Each result comes from an internal, pre-registered study and is updated as the work continues.",
    items: [
      { big: "Under 2%", from: "against 40 to 60% in human prose", text: "Instruction ambiguity. AISP gives every instruction one formal reading, so two agents act on it the same way." },
      { big: "17 vs 62", from: "failures before reaching the goal", text: "Milestone 1, experience transfer. A learning system built on AISP averaged 17 failures before reaching the goal; the machine learning baseline needed 62." },
      { big: "37 of 40", from: "after 8 chained sessions, from 38 of 40", text: "Long-term memory, the elevator game. Like the 12 days of Christmas, each new session adds complex work and must still recall everything before it. After eight chained sessions, knowledge kept in AISP had lost 1 task in 40.", note: "For comparison, elite prose instructions at 10% ambiguity would keep about 43% after eight handoffs (0.9 to the power of 8). A projection, not a measurement." },
      { big: "6 of 6", from: "up from 0 of 6, with no errors of meaning", text: "AISP grammar. In the latest trial every failure was formatting; a deterministic normalizer closed the gap without a model." },
      { big: "250,000", from: "domain-general, in one grammar", text: "Units of knowledge written in AISP, so agents reuse what is known instead of re-deriving it." },
    ],
  },
  layers: {
    heading: "The system",
    items: [
      { name: "Specify", line: "AISP: one formal reading for every instruction", status: "Open source" },
      { name: "Gate", line: "Checks in Rust and a database the agent cannot edit", status: "In use" },
      { name: "Prove", line: "Deterministic receipts for every session", status: "Open source" },
      { name: "Learn", line: "Knowledge kept in AISP, with its evidence", status: "In research" },
      { name: "Transfer", line: "Experience carried to new problems", status: "Milestone 1" },
    ],
  },
  method: "Every study is pre-registered: predictions are sealed before results are opened, each batch changes one thing, and the rollback rule is written in advance.",
  speaking: "Keynote speaker on deterministic AI. Founding Director and Education Director of the Agentics Foundation.",
};
