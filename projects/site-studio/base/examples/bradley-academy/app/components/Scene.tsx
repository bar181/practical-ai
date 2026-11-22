import type { ReactNode } from "react";
import { slot } from "../content/images";
import { media } from "../lib/paths";

/** A full-bleed picture from an image slot, with the effect named by `cine`. */
export function SceneImage({ id, cine, eager, className = "scene-img", name, decorative = true }: { id: string; cine?: string; eager?: boolean; className?: string; name?: string; decorative?: boolean }) {
  const s = slot(id);
  // Most scene pictures set a mood behind words that already say everything, so readers skip them.
  return (
    <div className={className} data-cine={cine}>
      <img
        src={media(s.src)}
        srcSet={s.srcSet?.split(", ").map((x) => media(x)).join(", ")}
        sizes={s.srcSet ? "100vw" : undefined}
        alt={decorative ? "" : s.alt}
        style={{ objectPosition: s.focus, viewTransitionName: name }}
        loading={eager ? "eager" : "lazy"}
        fetchPriority={eager ? "high" : undefined}
        decoding="async"
      />
    </div>
  );
}

/** A small label for a section, as a film would title a chapter. */
export function Chapter({ children }: { children: ReactNode }) {
  return <p className="chapter">{children}</p>;
}
