import type { ElementType } from "react";

/**
 * Text that the motion layer can animate word by word. Screen readers and search engines read the
 * whole sentence from a hidden copy; the animated words are hidden from them. React owns every
 * span, so nothing is rewritten behind its back.
 */
export function SplitText({ text, as: Tag = "p", className, cine, id }: { text: string; as?: ElementType; className?: string; cine?: string; id?: string }) {
  const parts = text.split(/(\s+)/);
  return (
    <Tag className={className} data-cine={cine} id={id}>
      <span className="sr-only">{text}</span>
      <span aria-hidden="true">
        {parts.map((p, i) => (p.trim() ? <span key={i} className="w"><span>{p}</span></span> : p))}
      </span>
    </Tag>
  );
}
