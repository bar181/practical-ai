import { SmartLink } from "./SmartLink";

type Result = { big: string; from: string; text: string; note?: string; href?: string };
type Next = { href: string; label: string; note: string };

/** The public results, each linked to the page where its method and limits are written down. */
export function ResultList({ items, className = "result-grid" }: { items: Result[]; className?: string }) {
  return (
    <ul className={className} data-cine="reveal">
      {items.map((r) => (
        <li key={r.big} data-cine-item>
          <p className="result-big">{r.big}</p>
          <p className="result-from">{r.from}</p>
          <p className="result-text">{r.text}</p>
          {r.note ? <p className="result-note">{r.note}</p> : null}
          {r.href ? <p className="result-source"><SmartLink href={r.href}>Method and limits</SmartLink></p> : null}
        </li>
      ))}
    </ul>
  );
}

/** Where a reviewer goes next, in order: the paper, the evidence, the tools. */
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
