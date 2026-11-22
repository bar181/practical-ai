import { Link } from "react-router";
import type { Route } from "./+types/about";
import { about, site } from "../content/site";
import { SceneImage } from "../components/Scene";
import { SplitText } from "../components/SplitText";
import { pageMeta, personJsonLd } from "../lib/meta";

export const meta: Route.MetaFunction = () =>
  [...pageMeta(`About ${about.title} | ${site.brand}`, about.metaDescription, "/about/"), personJsonLd];

export default function About() {
  return (
    <>
      <section className="hero hero-about" aria-labelledby="about-h">
        <div className="hero-shade hero-shade-about" aria-hidden="true" />
        <div className="letterbox top" data-letterbox aria-hidden="true" />
        <div className="letterbox bottom" data-letterbox aria-hidden="true" />
        <div className="wrap about-hero">
          <div className="about-portrait" data-cine-after="0">
            <SceneImage id="about-portrait" eager className="portrait-frame" decorative={false} />
          </div>
          <div className="about-hero-copy">
            <p className="hero-kicker" data-cine-after="0">{about.kicker}</p>
            <SplitText as="h1" id="about-h" className="hero-title" cine="title" text={about.title} />
            <p className="hero-lead" data-cine-after="1">{about.role}</p>
            <p className="hero-lead hero-lead-dim" data-cine-after="2">{about.specialty}</p>
            <div className="actions" data-cine-after="3">
              <a className="btn btn-light" href={site.linkedin} rel="noopener">{about.contactButton}</a>
              <a className="btn btn-ghost" href="#path">{about.pathButton}</a>
            </div>
          </div>
        </div>
      </section>

      <section className="path" id="path" aria-labelledby="path-h">
        <SceneImage id="about-stage" cine="parallax" className="standard-img" />
        <div className="standard-shade" aria-hidden="true" />
        <div className="wrap" data-cine="draw">
          <div data-cine="reveal">
            <h2 id="path-h" data-cine-item>{about.pathHeading}</h2>
            <p className="reel-lead" data-cine-item>{about.pathLead}</p>
          </div>
          <div className="timeline-wrap">
            <span className="timeline-line" data-cine-line aria-hidden="true" />
            <ol className="timeline timeline-wide">
              {about.pipeline.map((p, i) => (
                <li key={p.step} data-cine="reveal">
                  <span className="timeline-num" aria-hidden="true">{i + 1}</span>
                  <p className="timeline-step" data-cine-item>{p.step}</p>
                  <h3 data-cine-item>{p.title}</h3>
                  <p data-cine-item>{p.text}</p>
                  {p.link ? <p data-cine-item><a href={p.link.href} rel="noopener">{p.link.label}</a></p> : null}
                </li>
              ))}
            </ol>
          </div>
        </div>
      </section>

      <section className="credentials" aria-labelledby="cred-h">
        <div className="wrap" data-cine="reveal">
          <h2 id="cred-h" data-cine-item>{about.credentialsHeading}</h2>
          <dl className="credit-roll">
            {about.credentials.map((c) => (
              <div key={c.title} data-cine-item>
                <dt>{c.title}</dt>
                <dd>{c.text}</dd>
              </div>
            ))}
          </dl>
        </div>
      </section>

      <section className="take" aria-labelledby="why-h">
        <div className="wrap narrow" data-cine="reveal">
          <h2 id="why-h" data-cine-item>{about.whyHeading}</h2>
          <p className="reel-lead" data-cine-item>{about.why}</p>
          <p data-cine-item className="actions">
            <a className="btn btn-light" href={site.linkedin} rel="noopener">{about.contactButton}</a>
            <Link className="btn btn-ghost" to="/research#early-access" viewTransition>Request results</Link>
          </p>
        </div>
      </section>
    </>
  );
}
