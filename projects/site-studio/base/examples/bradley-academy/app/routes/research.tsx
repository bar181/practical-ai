import { Link } from "react-router";
import type { Route } from "./+types/research";
import { brand, contact, research } from "../content/brand";
import { Lattice } from "../components/Art";
import { NextSteps, ResultList } from "../components/Evidence";
import { SmartLink } from "../components/SmartLink";
import { SplitText } from "../components/SplitText";
import { pageMeta } from "../lib/meta";

export const meta: Route.MetaFunction = () => pageMeta(research.metaTitle, research.metaDescription, "/research/");

export default function Research() {
  return (
    <>
      <section className="hero hero-page hero-lattice" aria-labelledby="research-h">
        <Lattice />
        <div className="hero-shade" aria-hidden="true" />
        <div className="wrap hero-inner">
          <p className="hero-kicker" data-cine-after="0">{research.hero.kicker}</p>
          <SplitText as="h1" id="research-h" className="hero-title hero-title-page" cine="title" text={research.hero.title} />
          <p className="hero-lead" data-cine-after="1">{research.hero.lead}</p>
          <div className="actions" data-cine-after="2">
            <a className="btn btn-light" href={contact.paper.href} rel="noopener">{contact.paper.label}</a>
            <a className="btn btn-ghost" href="#early-access">Further results</a>
          </div>
        </div>
      </section>

      <section className="results" aria-labelledby="results-h">
        <div className="wrap">
          <h2 id="results-h" className="results-h" data-cine="reveal">{research.results.heading}</h2>
          <p className="results-note" data-cine="reveal">{research.results.note}</p>
          <ResultList items={research.results.items} className="result-grid result-grid-4" />
        </div>
      </section>

      <NextSteps id="next-h" heading={brand.next.heading} items={brand.next.items} />

      <section className="program" aria-labelledby="layers-h">
        <div className="wrap">
          <h2 id="layers-h" className="results-h" data-cine="reveal">{research.layers.heading}</h2>
          <ol className="stages" data-cine="reveal">
            {research.layers.items.map((s, i) => (
              <li key={s.name} className={`stage ${s.status === "Open source" ? "stage-public" : ""}`} data-cine-item>
                <span className="stage-num" aria-hidden="true">{i + 1}</span>
                <h3>{s.name}</h3>
                <p>{s.line}</p>
                <p className="stage-status"><span className="status-word">{s.status}</span></p>
              </li>
            ))}
          </ol>
          <p className="method" data-cine="reveal">{research.method}</p>
        </div>
      </section>

      <section className="open-work" aria-labelledby="open-h">
        <div className="wrap open-row" data-cine="reveal">
          <h2 id="open-h" className="open-h" data-cine-item>{brand.openSource.heading}</h2>
          <ul data-cine-item>
            {brand.openSource.items.slice(0, 2).map((o) => (
              <li key={o.href}><SmartLink href={o.href}>{o.label}</SmartLink><span>{o.note}</span></li>
            ))}
          </ul>
          <p className="muted speaking" data-cine-item>{research.speaking}</p>
        </div>
      </section>

      <section className="take early" id="early-access" aria-labelledby="early-h">
        <div className="wrap narrow" data-cine="reveal">
          <h2 id="early-h" data-cine-item>{brand.earlyAccess.heading}</h2>
          <p className="reel-lead" data-cine-item>{brand.earlyAccess.text}</p>
          <p className="actions" data-cine-item><a className="btn btn-light" href={contact.earlyAccess.href} rel="noopener">{contact.earlyAccess.label}</a></p>
          <p className="early-note" data-cine-item>{contact.earlyNote}</p>
        </div>
      </section>
    </>
  );
}
