import { Link } from "react-router";
import type { Route } from "./+types/home";
import prompts from "../content/generated/prompts.json";
import { about, home, site } from "../content/site";
import { tools } from "../content/tools";
import { CopyButton } from "../components/CopyButton";
import { PromptCard } from "../components/PromptCard";
import { media } from "../lib/paths";
import { pageMeta } from "../lib/meta";

export const meta: Route.MetaFunction = () =>
  pageMeta(`${site.brand}: Practical AI tools for the jobs you repeat`, site.description, "/");

export default function Home() {
  return (
    <>
      <section className="band hero">
        <div className="wrap band-inner">
          <h1>{home.title}</h1>
          <p className="lead">{home.lead}</p>
          <div className="actions">
            <a className="btn btn-primary" href="#tools">See the five tools</a>
            <CopyButton text={prompts.starter} label="Copy the starter prompt" className="btn btn-quiet" />
          </div>
        </div>
      </section>

      <section className="section" id="tools" aria-labelledby="tools-h">
        <div className="wrap">
          <h2 id="tools-h">Five tools, one job each</h2>
          <ul className="tool-grid">
            {tools.map((t) => (
              <li key={t.slug}>
                <Link to={`/tools/${t.slug}`} className="tool-card">
                  <img src={media(t.icon)} alt="" width={64} height={64} />
                  <span className="tool-card-text">
                    <span className="tool-card-name">{t.name}</span>
                    <span className="tool-card-promise">{t.promise}</span>
                    <span className="tool-card-line">{t.cardLine}</span>
                    <span className="status-word">{t.status.label}</span>
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </section>

      <section className="section section-alt" aria-labelledby="idea-h">
        <div className="wrap two-col">
          <div>
            <h2 id="idea-h">{home.idea.heading}</h2>
            <p className="analogy">{home.idea.analogy}</p>
          </div>
          <ul className="points">
            {home.idea.points.map((p) => (
              <li key={p.title}><strong>{p.title}</strong><span>{p.text}</span></li>
            ))}
          </ul>
        </div>
      </section>

      <section className="section" aria-labelledby="levels-h">
        <div className="wrap">
          <h2 id="levels-h">{home.levels.heading}</h2>
          <p className="section-lead">{home.levels.intro}</p>
          <ol className="level-steps">
            {home.levels.steps.map((s, i) => (
              <li key={s.title}>
                <span className="level-num" aria-hidden="true">{i + 1}</span>
                <h3>Level {i + 1}: {s.title}</h3>
                <p>{s.text}</p>
              </li>
            ))}
          </ol>
        </div>
      </section>

      <section className="section section-alt" aria-labelledby="starter-h">
        <div className="wrap narrow">
          <h2 id="starter-h">{home.starter.heading}</h2>
          <p className="section-lead">{home.starter.text}</p>
          <PromptCard prompt={prompts.starter} label="Copy the starter prompt" />
        </div>
      </section>

      <section className="section" aria-labelledby="maker-h">
        <div className="wrap maker">
          <img src={media("shared/bradley-ross.jpg")} alt="Bradley Ross" width={120} height={120} className="portrait" />
          <div>
            <h2 id="maker-h">Made by Bradley Ross</h2>
            <p>{about.lead} These tools come out of his teaching: what people ask for most, in the form that worked in the room.</p>
            <p><Link to="/about">About Bradley</Link></p>
          </div>
        </div>
      </section>
    </>
  );
}
