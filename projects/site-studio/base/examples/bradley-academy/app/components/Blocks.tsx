import type { Block, Picture } from "../content/types";
import { media, pageHref } from "../lib/paths";
import { SmartLink } from "./SmartLink";

function Pic({ p }: { p: Picture }) {
  const img = <img src={media(p.src)} alt={p.alt} loading="lazy" decoding="async" />;
  // A picture of a live page opens that page: the picture and its caption are one tap target.
  if (p.href) {
    return (
      <figure className="pic pic-link">
        <SmartLink href={p.href}>
          {img}
          <span className="pic-open">{p.caption ? <strong>{p.caption}</strong> : null}<span>Open the live page</span></span>
        </SmartLink>
      </figure>
    );
  }
  return (
    <figure className="pic">
      {img}
      {p.caption ? <figcaption>{p.caption}</figcaption> : null}
    </figure>
  );
}

/** Draws the example blocks a tool's tabs are made of. */
export function Blocks({ blocks }: { blocks: Block[] }) {
  return (
    <>
      {blocks.map((b, i) => {
        switch (b.kind) {
          case "text":
            return (
              <div key={i} className="prose">
                {b.heading ? <h3>{b.heading}</h3> : null}
                {b.paras.map((p, j) => <p key={j}>{p}</p>)}
              </div>
            );
          case "picture":
            return <div key={i} className={`pics pics-${b.size ?? "wide"} pics-one`}><Pic p={b.picture} /></div>;
          case "gallery":
            return <div key={i} className={`pics pics-${b.size ?? "wide"}`}>{b.pictures.map((p) => <Pic key={p.src} p={p} />)}</div>;
          case "frame":
            return (
              <figure key={i} className="frame">
                <iframe src={pageHref(b.src)} title={b.title} loading="lazy" style={{ height: `min(${b.height}px, 80svh)` }} />
                <figcaption>
                  {b.caption} <a href={pageHref(b.src)}>Open it full screen</a>
                </figcaption>
              </figure>
            );
          case "table":
            return (
              <div key={i} className="table-wrap" tabIndex={0} role="region" aria-label={b.caption}>
                <table>
                  <caption>{b.caption}</caption>
                  <thead><tr>{b.head.map((h) => <th key={h} scope="col">{h}</th>)}</tr></thead>
                  <tbody>{b.rows.map((r, j) => <tr key={j}>{r.map((c, k) => k === 0 ? <th key={k} scope="row">{c}</th> : <td key={k} data-label={b.head[k]}>{c}</td>)}</tr>)}</tbody>
                </table>
              </div>
            );
          case "steps":
            return (
              <ol key={i} className="steps">
                {b.items.map((s) => <li key={s.title}><strong>{s.title}.</strong> {s.text}</li>)}
              </ol>
            );
          case "links":
            return (
              <div key={i} className="link-list">
                <h3>{b.heading}</h3>
                <ul>
                  {b.items.map((l) => (
                    <li key={l.href}><SmartLink href={l.href}>{l.label}</SmartLink>{l.note ? <span className="muted">: {l.note}</span> : null}</li>
                  ))}
                </ul>
              </div>
            );
        }
      })}
    </>
  );
}
