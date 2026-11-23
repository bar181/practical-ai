import { Link } from "react-router";
import { aispIntro, aispSource, type Excerpt } from "../content/aisp";
import { SmartLink } from "./SmartLink";

/** A verbatim excerpt of the AISP specification, then how to read its key lines. */
export function AispCode({ excerpt, reading = true }: { excerpt: Excerpt; reading?: boolean }) {
  return (
    <figure className="aisp-fig" aria-labelledby={`aisp-${excerpt.id}`}>
      <h3 id={`aisp-${excerpt.id}`} className="aisp-title">{excerpt.title}</h3>
      <p className="aisp-text">{excerpt.text}</p>
      <pre className="aisp-code" tabIndex={0} aria-label={`AISP: ${excerpt.title}`}>
        <code>{excerpt.code.map((l, i) => <span key={i} className={/^\s*;;/.test(l) ? "aisp-comment" : undefined}>{l || " "}{"\n"}</span>)}</code>
      </pre>
      {reading ? (
        <dl className="aisp-reading">
          {excerpt.reading.map((r) => (
            <div key={r.code}>
              <dt><code>{r.code}</code></dt>
              <dd>{r.plain}</dd>
            </div>
          ))}
        </dl>
      ) : null}
    </figure>
  );
}

/** The 512 symbols: eight categories of 64. */
export function SigmaGrid() {
  return (
    <div className="sigma">
      <p className="sigma-big"><span className="sigma-mark" aria-label={aispIntro.sigma.big}><span className="aisp-glyphs" aria-hidden="true">Σ</span><sub aria-hidden="true">512</sub></span><span className="sigma-text">{aispIntro.sigma.text}</span></p>
      <ul className="sigma-grid">
        {aispIntro.categories.map((c) => (
          <li key={c.name}>
            <span className="sigma-glyph aisp-glyphs" aria-hidden="true">{c.glyph}</span>
            <span className="sigma-name">{c.name} <span className="sr-only">({c.glyph})</span></span>
            <span className="sigma-role">{c.role}</span>
            <span className="sigma-range">symbols {c.range}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export function SourceNote({ more }: { more?: boolean }) {
  return (
    <p className="aisp-source">
      Verbatim from <SmartLink href={aispSource.href}>{aispSource.label}</SmartLink>, the open core.
      {more ? <> <Link to="/research#aisp-h" viewTransition>Inside AISP</Link></> : null}
    </p>
  );
}
