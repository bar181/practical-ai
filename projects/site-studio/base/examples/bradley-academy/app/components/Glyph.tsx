import type { ToolSlug } from "../content/slugs";

// One brass line drawing per tool, in the style of a film's title-card ornament.
const paths: Record<string, string> = {
  // A page built from stacked blocks: the sections, in order
  "web-sections": "M12 6h24v36H12zM16 11h16M16 16h16v8H16zM16 28h4v5h-4zM22 28h4v5h-4zM28 28h4v5h-4zM16 37h16",
  // A speech bubble with lines of different lengths: the same facts, in another order
  "tone-studio": "M10 9h28a3 3 0 0 1 3 3v16a3 3 0 0 1-3 3H22l-8 7v-7h-4a3 3 0 0 1-3-3V12a3 3 0 0 1 3-3zM14 16h14M14 21h18M14 26h8",
  // A page with a spark: notes become a designed page
  "artifact-studio": "M13 8h16l8 8v24H13zM29 8v8h8M18 22h14M18 28h10M18 34h12M38 6l1.6 3.4L43 11l-3.4 1.6L38 16l-1.6-3.4L33 11l3.4-1.6z",
  // A document with a tick: what it asks of you
  "document-to-action-brief": "M12 6h18l8 8v28H12zM30 6v8h8M17 20h16M17 26h9M21 34l4 4 9-10",
  // A checklist with one flagged item: the action nobody agreed to
  "meeting-notes-to-actions": "M8 11l3 3 5-6M21 11h17M8 22l3 3 5-6M21 22h17M8 31h7v7H8zM21 35h8M35 30v13M35 30h7l-2 3 2 3h-7",
  // A pen over lines of writing: your draft, in your voice
  "write-in-my-voice": "M8 14h18M8 21h14M8 28h16M8 35h8M24 40v-5l14-14 5 5-14 14zM35 24l5 5",
  // An open log book with a ribbon
  "learnings-database": "M24 12c-5-3-11-4-17-3v29c6-1 12 0 17 3 5-3 11-4 17-3V9c-6-1-12 0-17 3zM24 12v29M31 9v12l3-2 3 2V9",
  // Three linked steps: a job set up properly once
  "agentic-process": "M10 10h10v10H10zM28 28h10v10H28zM28 10h10v10H28zM20 15h8M33 20v8M15 20v13h13",
  // A cut gem
  "rare-find": "M14 10h20l8 10-18 20L6 20zM6 20h36M18 10l-4 10 10 20 10-20-4-10M14 20h20",
};

export function Glyph({ slug, className = "glyph" }: { slug: ToolSlug | string; className?: string }) {
  return (
    <svg className={className} viewBox="0 0 48 48" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      {/* A tool without its own drawing gets a simple framed star */}
      <path d={paths[slug] ?? "M8 8h32v32H8zM24 14l2.6 6.4L33 21l-5 4.4 1.6 6.6L24 28.6 18.4 32l1.6-6.6-5-4.4 6.4-.6z"} />
    </svg>
  );
}
