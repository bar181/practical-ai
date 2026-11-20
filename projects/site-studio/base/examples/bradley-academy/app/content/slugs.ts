// The order tools appear in, everywhere on the site.
export const toolSlugs = [
  "artifact-studio",
  "document-to-action-brief",
  "learnings-database",
  "agentic-process",
  "rare-find",
] as const;

export type ToolSlug = (typeof toolSlugs)[number];
