// The order tools appear in, everywhere on the site: the design set together, everyday jobs next,
// the game, then the builder's method last.
export const toolSlugs = [
  // The design set: structure, then words, then the look
  "web-sections",
  "tone-studio",
  "artifact-studio",
  // Then put it online
  "site-studio",
  "website-audit",
  // Everyday jobs
  "document-to-action-brief",
  "meeting-notes-to-actions",
  "write-in-my-voice",
  "research-brief",
  "decision-support",
  "rubric-reviewer",
  "learnings-database",
  // Ask about any of them
  "practical-ai-guide",
  "rare-find",
  // For builders
  "agentic-process",
] as const;

export type ToolSlug = (typeof toolSlugs)[number];
