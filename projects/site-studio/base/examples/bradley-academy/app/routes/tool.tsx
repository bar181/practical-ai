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
import { SceneImage } from "../components/Scene";
import { SplitText } from "../components/SplitText";
import { Glyph } from "../components/Glyph";
import { pageMeta } from "../lib/meta";

export const meta: Route.MetaFunction = ({ params }) => {
  const t = getTool(params.slug);
  if (!t) return [{ title: `Not found | ${site.brand}` }];
  return pageMeta(`${t.name}: ${t.promise} | ${site.brand}`, `${t.sub} ${t.coreIdea}`.slice(0, 300), `/tools/${t.slug}/`);
};

function About({ t }: { t: Tool }) {
  const prompt = prompts[t.tryIt.promptKey];
  return (
    <>
    <div className="wrap about-grid">
      <div className="about-main">
        <section aria-labelledby="idea" data-cine="reveal">
          <h2 id="idea" data-cine-item>The core idea</h2>
          <p className="lead-dark" data-cine-item>{t.coreIdea}</p>
          <p className="analogy" data-cine-item>{t.analogy}</p>
        </section>

        <section aria-labelledby="what" data-cine="reveal">
          <h2 id="what" data-cine-item>What it is</h2>
          {t.whatItIs.map((p, i) => <p key={i} data-cine-item>{p}</p>)}
        </section>

        <section aria-labelledby="why" data-cine="reveal">
          <h2 id="why" data-cine-item>Why it helps</h2>
          <ul className="ticks">
            {t.benefits.map((b) => <li key={b.title} data-cine-item><strong>{b.title}</strong><span>{b.text}</span></li>)}
          </ul>
        </section>

        <section aria-labelledby="design" data-cine="reveal">
          <h2 id="design" data-cine-item>How it is designed to help</h2>
          <ul className="design-list">
            {t.design.map((d) => <li key={d.title} data-cine-item><h3>{d.title}</h3><p>{d.text}</p></li>)}
          </ul>
        </section>

      </div>
      <aside className="about-side" aria-label="Try it">
        <div className="try-card">
          <h2>{site.labels.tryCardHeading}</h2>
          <p>{site.labels.tryCardText}</p>
          <CopyButton text={prompt} label={t.tryIt.primaryLabel} />
          <p className="hero-link"><a href="#try-it">{site.labels.readPrompt}</a></p>
        </div>
      </aside>
    </div>

    <section aria-labelledby="who" className="who-scene">
      <SceneImage id={`who-${t.slug}`} cine="clip" className="clip-scene" />
      <div className="wrap who-copy" data-cine="reveal">
        <h2 id="who" data-cine-item>Who it is for</h2>
        <p data-cine-item>{t.coreUser}</p>
      </div>
    </section>

    <div className="wrap about-grid about-grid-2">
      <div className="about-main">
        <section aria-labelledby="levels" data-cine="draw" className="levels-section">
          <h2 id="levels">{site.labels.levelsHeading}</h2>
          <div className="timeline-wrap">
          <span className="timeline-line" data-cine-line aria-hidden="true" />
          <ol className="levels">
            {t.levels.map((l) => (
              <li key={l.level} className={l.built ? "" : "level-planned"} data-cine="reveal">
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
          </div>
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
      <Side t={t} />
    </div>
    </>
  );
}

function Side({ t }: { t: Tool }) {
  return (
    <aside className="about-side" aria-label="Status and links">
        <div className="side-card">
          <h2 className="side-h">Status</h2>
          <p className="status-word">{t.status.label}, {t.status.date}</p>
          <p>{t.status.text}</p>
        </div>
        {t.set ? (
          <div className="side-card">
            <h2 className="side-h">Part of a set</h2>
            <p>{t.set.text}</p>
            <ul className="plain-list">
              {t.set.links.map((l) => <li key={l.href}><SmartLink href={l.href}>{l.label}</SmartLink></li>)}
            </ul>
          </div>
        ) : null}
        <div className="side-card">
          <h2 className="side-h">Go deeper</h2>
          <ul className="plain-list">
            {t.explainer ? <li><SmartLink href={t.explainer}>The step-by-step explainer</SmartLink></li> : null}
            <li><a href={t.readme} rel="noopener">{site.labels.projectLink}</a></li>
            <li><Link to="/#all-tools">All the tools</Link></li>
          </ul>
        </div>
    </aside>
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
      <section className="hero hero-tool" aria-labelledby="tool-h">
        <SceneImage id={`tool-${t.slug}`} cine="kenburns" eager className="hero-img" name={`tool-${t.slug}`} />
        <div className="hero-shade" aria-hidden="true" />
        <div className="letterbox top" data-letterbox aria-hidden="true" />
        <div className="letterbox bottom" data-letterbox aria-hidden="true" />
        <div className="wrap hero-inner">
          <p className="crumb" data-cine-after="0"><Link to="/" viewTransition>All tools</Link></p>
          <div className="tool-title" data-cine-after="0">
            <Glyph slug={t.slug} />
            <h1 id="tool-h">{t.name}</h1>
          </div>
          <SplitText className="hero-title hero-title-tool" cine="title" text={t.promise} />
          <p className="hero-lead" data-cine-after="1">{t.sub}</p>
          <div className="actions" data-cine-after="2">
            {t.tryIt.play ? <SmartLink href={t.tryIt.play[0].href} className="btn btn-light">{t.tryIt.play[0].label}</SmartLink> : null}
            <CopyButton text={prompt} label={t.tryIt.primaryLabel} className={t.tryIt.play ? "btn btn-ghost" : "btn btn-light"} />
          </div>
          <p className="hero-link" data-cine-after="2"><a href="#try-it">{site.labels.readPrompt}</a></p>
          <p className="status-line" data-cine-after="3"><span className="status-word">{t.status.label}</span> {site.labels.worksIn}</p>
        </div>
      </section>
      <Tabs items={items} label={`${t.name}: about and examples`} />
    </>
  );
}
