import { SmartLink } from "./SmartLink";

/** kind says what sort of claim it is (formal property, experimental finding, engineering result);
 *  limits says what it does not show. */
type Result = { big: string; from: string; text: string; kind?: string; limits?: string; note?: string; href?: string; code?: string };
type Next = { href: string; label: string; note: string };

/** Public results, each linked to the page where it is written down. A result may quote one line of
 *  AISP verbatim (code), shown in the AISP fonts. */
export function ResultList({ items, className = "result-grid" }: { items: Result[]; className?: string }) {
  return (
    <ul className={className} data-cine="reveal">
      {items.map((r) => (
        <li key={r.big} data-cine-item>
          {r.kind ? <p className="result-kind">{r.kind}</p> : null}
          <p className="result-big">{r.big}</p>
          <p className="result-from">{r.from}</p>
          {r.code ? <p className="result-code"><code>{r.code}</code></p> : null}
          <p className="result-text">{r.text}</p>
          {r.limits ? <p className="result-note"><strong>Limits:</strong> {r.limits}</p> : null}
          {r.note ? <p className="result-note">{r.note}</p> : null}
          {r.href ? <p className="result-source"><SmartLink href={r.href} aria-label={`Public evidence for ${r.big}`}>Public evidence</SmartLink></p> : null}
        </li>
      ))}
    </ul>
  );
}

/** Where a reader goes next, in order. */
export function NextSteps({ id, heading, items }: { id: string; heading: string; items: Next[] }) {
  return (
    <section className="next-steps" aria-labelledby={id}>
      <div className="wrap" data-cine="reveal">
        <h2 id={id} className="results-h" data-cine-item>{heading}</h2>
        <ol className="next-list" data-cine-item>
          {items.map((n) => (
            <li key={n.href}>
              <SmartLink href={n.href}>{n.label}</SmartLink>
              <span>{n.note}</span>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}
