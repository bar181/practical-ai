import { Link } from "react-router";
import type { Route } from "./+types/home";
import { brand, contact } from "../content/brand";
import { AispCode, SigmaGrid, SourceNote } from "../components/Aisp";
import { ResultList } from "../components/Evidence";
import { aispIntro, foundation } from "../content/aisp";
import { SceneImage } from "../components/Scene";
import { SmartLink } from "../components/SmartLink";
import { SplitText } from "../components/SplitText";
import { pageMeta, personJsonLd } from "../lib/meta";
import { media } from "../lib/paths";
import { site } from "../content/site";

export const meta: Route.MetaFunction = () => [...pageMeta(brand.metaTitle, brand.metaDescription, "/"), personJsonLd];

export default function Home() {
  return (
    <>
      {/* Opening scene */}
      <section className="hero hero-brand" aria-labelledby="hero-h">
        <SceneImage id="home-hero" cine="kenburns" eager className="hero-img" />
        <div className="hero-shade" aria-hidden="true" />
        <div className="letterbox top" data-letterbox aria-hidden="true" />
        <div className="letterbox bottom" data-letterbox aria-hidden="true" />
        <div className="wrap hero-inner">
          <p className="hero-kicker hero-id" data-cine-after="0">
            <img src={media(site.labels.authorPhoto)} alt="" width={56} height={56} className="hero-face" />
            <span>{brand.hero.kicker}</span>
          </p>
          <SplitText as="h1" id="hero-h" className="hero-title" cine="title" text={brand.hero.title} />
          <p className="hero-lead" data-cine-after="1">{brand.hero.lead}</p>
          <div className="actions" data-cine-after="2">
            <a className="btn btn-light" href={contact.paper.href} rel="noopener">{contact.paper.label}</a>
            <Link className="btn btn-ghost" to="/research" viewTransition>See the evidence</Link>
          </div>
        </div>
      </section>

      {/* The work, one line. Credentials are on About */}
      <section className="proof" aria-label="The work">
        <ul className="wrap proof-list">
          {brand.proof.map((p) => (
            <li key={p.strong}><strong>{p.strong}</strong><span>{p.rest}</span></li>
          ))}
        </ul>
      </section>

      {/* The vision, word by word */}
      <section className="statement statement-brand" data-cine="words" aria-labelledby="vision-h">
        <div className="wrap statement-inner">
          <h2 id="vision-h" className="sr-only">The research</h2>
          <SplitText className="statement-text" text={brand.statement} />
        </div>
      </section>

      {/* AISP in its own notation */}
      <section className="aisp" aria-labelledby="aisp-home-h">
        <div className="wrap">
          <div className="section-head" data-cine="reveal">
            <h2 id="aisp-home-h" data-cine-item>{aispIntro.heading}</h2>
            <p className="reel-lead" data-cine-item>{aispIntro.lead}</p>
          </div>
          <div className="aisp-pair">
            <SigmaGrid />
            <AispCode excerpt={foundation} />
          </div>
          <SourceNote more />
        </div>
      </section>

      {/* The proof: three public numbers, each linked to its source */}
      <section className="results" aria-labelledby="results-h">
        <div className="wrap">
          <h2 id="results-h" className="results-h" data-cine="reveal">{brand.results.heading}</h2>
          <ResultList items={brand.results.items} />
          <p className="results-more" data-cine="reveal"><Link to="/research" viewTransition>All the public evidence</Link></p>
        </div>
      </section>


      {/* The range: from a ten-person team to a lab */}
      <section className="range" aria-labelledby="range-h">
        <div className="wrap">
          <div className="section-head" data-cine="reveal">
            <h2 id="range-h" data-cine-item>{brand.range.heading}</h2>
            <p className="reel-lead" data-cine-item>{brand.range.lead}</p>
          </div>
          <ul className="range-grid" data-cine="reveal">
            {brand.range.items.map((r) => (
              <li key={r.who} data-cine-item>
                <Link to={r.link.href} viewTransition className="range-tile">
                  <strong>{r.who}</strong>
                  <span>{r.text}</span>
                  <span className="range-go">{r.link.label}</span>
                </Link>
              </li>
            ))}
          </ul>
          <p className="work-with" data-cine="reveal">{brand.workWith.text} <a href={site.wisegeo} rel="noopener">{brand.workWith.label}</a></p>
        </div>
      </section>

      {/* Open work */}
      <section className="open-work" aria-labelledby="open-h">
        <div className="wrap open-row" data-cine="reveal">
          <h2 id="open-h" className="open-h" data-cine-item>{brand.openSource.heading}</h2>
          <ul data-cine-item>
            {brand.openSource.items.map((o) => (
              <li key={o.href}><SmartLink href={o.href}>{o.label}</SmartLink><span>{o.note}</span></li>
            ))}
          </ul>
        </div>
      </section>

      {/* Network: one quiet line */}
      <section className="network" aria-labelledby="network-h">
        <div className="wrap open-row" data-cine="reveal">
          <h2 id="network-h" className="open-h" data-cine-item>{brand.network.heading}</h2>
          <p className="network-text" data-cine-item>
            {brand.network.text} <SmartLink href={brand.network.link.href}>{brand.network.link.label}</SmartLink>
          </p>
        </div>
      </section>

      {/* Further results, on request */}
      <section className="take take-scene early" aria-labelledby="early-h">
        <SceneImage id="work-hero" cine="parallax" className="take-img" />
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
