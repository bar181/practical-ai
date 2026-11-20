import { Link } from "react-router";
import type { Route } from "./+types/tool";
import prompts from "../content/generated/prompts.json";
import { site } from "../content/site";
import { getTool } from "../content/tools";
import type { Tool } from "../content/types";
import { Blocks } from "../components/Blocks";
import { CopyButton } from "../components/CopyButton";
import { PromptCard } from "../components/PromptCard";
import { SmartLink } from "../components/SmartLink";
import { Tabs } from "../components/Tabs";
import { media } from "../lib/paths";
import { pageMeta } from "../lib/meta";

export const meta: Route.MetaFunction = ({ params }) => {
  const t = getTool(params.slug);
  if (!t) return [{ title: `Not found | ${site.brand}` }];
  return pageMeta(`${t.name}: ${t.promise} | ${site.brand}`, `${t.sub} ${t.coreIdea}`.slice(0, 300), `/tools/${t.slug}/`);
};

function About({ t }: { t: Tool }) {
  const prompt = prompts[t.tryIt.promptKey];
  return (
    <div className="wrap about-grid">
      <div className="about-main">
        <section aria-labelledby="idea">
          <h2 id="idea">The core idea</h2>
          <p className="lead-dark">{t.coreIdea}</p>
          <p className="analogy">{t.analogy}</p>
        </section>

        <section aria-labelledby="what">
          <h2 id="what">What it is</h2>
          {t.whatItIs.map((p, i) => <p key={i}>{p}</p>)}
        </section>

        <section aria-labelledby="why">
          <h2 id="why">Why it helps</h2>
          <ul className="points">
            {t.benefits.map((b) => <li key={b.title}><strong>{b.title}</strong><span>{b.text}</span></li>)}
          </ul>
        </section>

        <section aria-labelledby="design">
          <h2 id="design">How it is designed to help</h2>
          <ul className="design-list">
            {t.design.map((d) => <li key={d.title}><h3>{d.title}</h3><p>{d.text}</p></li>)}
          </ul>
        </section>

        <section aria-labelledby="who">
          <h2 id="who">Who it is for</h2>
          <p>{t.coreUser}</p>
        </section>

        <section aria-labelledby="levels">
          <h2 id="levels">Three levels: start simple, grow when you are ready</h2>
          <ol className="levels">
            {t.levels.map((l) => (
              <li key={l.level} className={l.built ? "" : "level-planned"}>
                <p className="level-head">
                  <span className="level-num" aria-hidden="true">{l.level}</span>
                  <span>
                    <span className="level-name">Level {l.level}: {l.name}</span>
                    <span className="level-meta">For {l.coreUser.charAt(0).toLowerCase() + l.coreUser.slice(1)}. Setup: {l.setup.toLowerCase()}.{l.built ? "" : " Not built yet."}</span>
                  </span>
                </p>
                <blockquote className="story">{l.story}</blockquote>
                <p>{l.does}</p>
              </li>
            ))}
          </ol>
        </section>

        <section aria-labelledby="try" id="try-it">
          <h2 id="try">Try it now</h2>
          <p>{t.tryIt.intro}</p>
          {t.tryIt.play ? (
            <div className="actions">
              {t.tryIt.play.map((p) => <SmartLink key={p.href} href={p.href} className="btn btn-dark">{p.label}</SmartLink>)}
            </div>
          ) : null}
          <PromptCard prompt={prompt} label={t.tryIt.primaryLabel} />
          <p className="muted">{t.tryIt.after}</p>
        </section>

        <section aria-labelledby="not">
          <h2 id="not">What it does not do</h2>
          <ul className="plain-list">{t.notDo.map((n) => <li key={n}>{n}</li>)}</ul>
        </section>
      </div>

      <aside className="about-side" aria-label="Status and links">
        <div className="side-card">
          <h2 className="side-h">Status</h2>
          <p className="status-word">{t.status.label}, {t.status.date}</p>
          <p>{t.status.text}</p>
        </div>
        <div className="side-card">
          <h2 className="side-h">Go deeper</h2>
          <ul className="plain-list">
            {t.explainer ? <li><SmartLink href={t.explainer}>The step-by-step explainer</SmartLink></li> : null}
            <li><a href={t.readme} rel="noopener">The project on GitHub</a></li>
            <li><Link to="/">All five tools</Link></li>
          </ul>
        </div>
      </aside>
    </div>
  );
}

export default function ToolPage({ params }: Route.ComponentProps) {
  const t = getTool(params.slug);
  if (!t) throw new Response("Not found", { status: 404 });
  const prompt = prompts[t.tryIt.promptKey];
  const items = [
    { id: "about", label: "About", content: <About t={t} /> },
    ...t.tabs.map((tab) => ({
      id: tab.id,
      label: tab.label,
      content: (
        <div className="wrap example-panel">
          <h2>{tab.label}</h2>
          <p className="section-lead">{tab.intro}</p>
          <Blocks blocks={tab.blocks} />
        </div>
      ),
    })),
  ];
  return (
    <>
      <section className="band tool-band">
        <div className="wrap band-inner">
          <p className="crumb"><Link to="/">All tools</Link></p>
          <div className="tool-title">
            <img src={media(t.icon)} alt="" width={72} height={72} />
            <h1>{t.name}</h1>
          </div>
          <p className="promise">{t.promise}</p>
          <p className="lead">{t.sub}</p>
          <div className="actions">
            {t.tryIt.play ? <SmartLink href={t.tryIt.play[0].href} className="btn btn-primary">{t.tryIt.play[0].label}</SmartLink> : null}
            <CopyButton text={prompt} label={t.tryIt.primaryLabel} className={t.tryIt.play ? "btn btn-quiet" : "btn btn-primary"} />
            <a className="btn btn-quiet" href="#try-it">See the prompt first</a>
          </div>
          <p className="status-line"><span className="status-word">{t.status.label}</span> Free. Works in the chatbot you already use.</p>
        </div>
      </section>
      <Tabs items={items} label={`${t.name}: about and examples`} />
    </>
  );
}
