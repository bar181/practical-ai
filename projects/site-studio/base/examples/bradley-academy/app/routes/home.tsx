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
      {/* Opening scene: Bradley, and what he does */}
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
          <SplitText as="h1" id="hero-h" className="hero-title hero-name" cine="title" text={brand.hero.title} />
          <p className="hero-lead" data-cine-after="1">{brand.hero.lead}</p>
          <div className="actions" data-cine-after="2">
            {brand.hero.actions.map((a, i) => (
              <SmartLink key={a.href} href={a.href} className={i === 0 ? "btn btn-light" : "btn btn-ghost"}>{a.label}</SmartLink>
            ))}
          </div>
        </div>
      </section>

      {/* The record, one line */}
      <section className="proof" aria-label="The record">
        <ul className="wrap proof-list">
          {brand.proof.map((p) => (
            <li key={p.strong}><strong>{p.strong}</strong><span>{p.rest}</span></li>
          ))}
        </ul>
      </section>

      {/* Three differentiators */}
      <section className="career" aria-labelledby="career-h">
        <div className="wrap">
          <div className="section-head" data-cine="reveal">
            <h2 id="career-h" data-cine-item>{brand.career.heading}</h2>
            <p className="reel-lead" data-cine-item>{brand.career.lead}</p>
          </div>
          <ul className="career-grid" data-cine="reveal">
            {brand.career.points.map((c) => (
              <li key={c.title} data-cine-item>
                <h3>{c.title}</h3>
                <p>{c.text}</p>
                <p className="career-link"><SmartLink href={c.link.href}>{c.link.label}</SmartLink></p>
              </li>
            ))}
          </ul>
        </div>
      </section>

      {/* Systems he has built, each with its evidence */}
      <section id="systems" className="systems" aria-labelledby="systems-h">
        <div className="wrap">
          <div className="section-head" data-cine="reveal">
            <h2 id="systems-h" data-cine-item>{brand.systems.heading}</h2>
            <p className="reel-lead" data-cine-item>{brand.systems.lead}</p>
          </div>
          {brand.systems.items.map((sys) => (
            <article key={sys.name} className="system" aria-labelledby={`sys-${sys.name.replace(/\W+/g, "-")}`}>
              <div className="system-head">
                <p className="system-kind">{sys.kind}</p>
                <h3 id={`sys-${sys.name.replace(/\W+/g, "-")}`} className="system-name">{sys.name}</h3>
                <p className="system-line">{sys.line}</p>
                <p className="system-links">
                  {sys.links.map((l) => <SmartLink key={l.href} href={l.href}>{l.label}</SmartLink>)}
                </p>
              </div>
              <ResultList items={sys.evidence} className="result-grid result-grid-2" />
            </article>
          ))}
        </div>
      </section>

      {/* The vision, word by word */}
      <section className="statement statement-brand" data-cine="words" aria-labelledby="vision-h">
        <div className="wrap statement-inner">
          <h2 id="vision-h" className="sr-only">The research</h2>
          <SplitText className="statement-text" text={brand.statement} />
        </div>
      </section>

      {/* AISP in its own notation, after the evidence */}
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

      {/* Teaching at every level, and Practical AI */}
      <section className="range" aria-labelledby="teach-h">
        <div className="wrap">
          <div className="section-head" data-cine="reveal">
            <h2 id="teach-h" data-cine-item>{brand.teaching.heading}</h2>
            <p className="reel-lead" data-cine-item>{brand.teaching.lead}</p>
          </div>
          <ul className="range-grid" data-cine="reveal">
            {brand.teaching.levels.map((r) => (
              <li key={r.who} data-cine-item>
                <SmartLink href={r.link.href} className="range-tile">
                  <strong>{r.who}</strong>
                  <span>{r.text}</span>
                  <span className="range-go">{r.link.label}</span>
                </SmartLink>
              </li>
            ))}
          </ul>
          <div className="practical-block" data-cine="reveal">
            <h3 data-cine-item>{brand.teaching.practical.heading}</h3>
            <p data-cine-item>{brand.teaching.practical.text}</p>
            <ul className="practical-actions" data-cine-item>
              {brand.teaching.practical.actions.map((a) => (
                <li key={a.href}><SmartLink href={a.href}>{a.label}</SmartLink><span>{a.note}</span></li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      {/* Roles and collaborations */}
      <section className="network" aria-labelledby="network-h">
        <div className="wrap">
          <h2 id="network-h" className="network-h" data-cine="reveal">{brand.network.heading}</h2>
          <ul className="roles" data-cine="reveal">
            {brand.network.items.map((n) => (
              <li key={n.org} data-cine-item>
                <p className="role-org">{n.org}</p>
                <p className="role-name">{n.role}</p>
                <p className="role-text">{n.text}{"link" in n && n.link ? <> <SmartLink href={n.link.href}>{n.link.label}</SmartLink></> : null}</p>
              </li>
            ))}
          </ul>
        </div>
      </section>

      {/* For research partners */}
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
