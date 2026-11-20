import type { Route } from "./+types/about";
import { about, site } from "../content/site";
import { media } from "../lib/paths";
import { pageMeta } from "../lib/meta";

export const meta: Route.MetaFunction = () =>
  pageMeta(`About Bradley Ross | ${site.brand}`, `${about.lead} Creator of the Practical AI tools.`, "/about/");

export default function About() {
  return (
    <>
      <section className="band">
        <div className="wrap band-inner about-hero">
          <img src={media("shared/bradley-ross.jpg")} alt="Bradley Ross" width={160} height={160} className="portrait portrait-lg" />
          <div>
            <h1>{about.title}</h1>
            <p className="lead">{about.lead}</p>
            <p><a className="btn btn-primary" href={site.linkedin} rel="noopener">Connect on LinkedIn</a></p>
          </div>
        </div>
      </section>
      <section className="section">
        <div className="wrap narrow">
          <dl className="facts">
            {about.facts.map((f) => (
              <div key={f.title}><dt>{f.title}</dt><dd>{f.text}</dd></div>
            ))}
          </dl>
          <h2>Why these tools</h2>
          <p>{about.why}</p>
          <p>{about.contact}</p>
        </div>
      </section>
    </>
  );
}
