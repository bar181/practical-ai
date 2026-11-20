import type { ToolSlug } from "../content/slugs";

// One brass line drawing per tool, in the style of a film's title-card ornament.
const paths: Record<ToolSlug, string> = {
  // A page with a spark: notes become a designed page
  "artifact-studio": "M13 8h16l8 8v24H13zM29 8v8h8M18 22h14M18 28h10M18 34h12M38 6l1.6 3.4L43 11l-3.4 1.6L38 16l-1.6-3.4L33 11l3.4-1.6z",
  // A document with a tick: what it asks of you
  "document-to-action-brief": "M12 6h18l8 8v28H12zM30 6v8h8M17 20h16M17 26h9M21 34l4 4 9-10",
  // An open log book with a ribbon
  "learnings-database": "M24 12c-5-3-11-4-17-3v29c6-1 12 0 17 3 5-3 11-4 17-3V9c-6-1-12 0-17 3zM24 12v29M31 9v12l3-2 3 2V9",
  // Three linked steps: a job set up properly once
  "agentic-process": "M10 10h10v10H10zM28 28h10v10H28zM28 10h10v10H28zM20 15h8M33 20v8M15 20v13h13",
  // A cut gem
  "rare-find": "M14 10h20l8 10-18 20L6 20zM6 20h36M18 10l-4 10 10 20 10-20-4-10M14 20h20",
};

export function Glyph({ slug, className = "glyph" }: { slug: ToolSlug; className?: string }) {
  return (
    <svg className={className} viewBox="0 0 48 48" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <path d={paths[slug]} />
    </svg>
  );
}
