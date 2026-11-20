import type { Route } from "./+types/image-brief";
import { imageSlots } from "../content/images";
import { site } from "../content/site";
import { media } from "../lib/paths";

export const meta: Route.MetaFunction = () => [
  { title: `Image brief | ${site.brand}` },
  { name: "description", content: "Every picture on the Bradley Academy site that is still a placeholder, with what the final picture should show." },
  { name: "robots", content: "noindex" },
];

export default function ImageBrief() {
  const waiting = imageSlots.filter((s) => !s.final).length;
  return (
    <>
      <section className="plain-hero">
        <div className="wrap">
          <h1>Image brief</h1>
          <p className="lead">{waiting} of {imageSlots.length} pictures on this site are placeholders. Each is a picture the owner already made, standing in until the final one is ready. This page lists what each final picture should show.</p>
          <p className="muted-light">To replace one, add the file to <code>public/media/final/</code>, set <code>final</code> for its slot in <code>app/content/images.ts</code>, and rebuild. The slot drops off this list.</p>
        </div>
      </section>
      <section className="section">
        <div className="wrap">
          <ol className="brief-list">
            {imageSlots.map((s) => (
              <li key={s.id} className="brief-item">
                <figure className="brief-thumb">
                  <img src={media(s.final ?? s.placeholder)} alt={s.final ? s.alt : s.placeholderAlt} loading="lazy" />
                  <figcaption>{s.final ? "Final" : "Placeholder"}</figcaption>
                </figure>
                <div>
                  <h2 className="brief-h">{s.page}: {s.where}</h2>
                  <dl className="brief-dl">
                    <div><dt>The final picture shows</dt><dd>{s.brief}</dd></div>
                    <div><dt>Shape and size</dt><dd>{s.size}</dd></div>
                    <div><dt>Prompt</dt><dd><code>{s.prompt}</code></dd></div>
                    <div><dt>Alt text</dt><dd>{s.alt}</dd></div>
                    <div><dt>Slot</dt><dd><code>{s.id}</code></dd></div>
                  </dl>
                </div>
              </li>
            ))}
          </ol>
        </div>
      </section>
    </>
  );
}
