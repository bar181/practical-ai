import { Link } from "react-router";
import type { Route } from "./+types/home";
import prompts from "../content/generated/prompts.json";
import { about, home, site } from "../content/site";
import { tools } from "../content/tools";
import { CopyButton } from "../components/CopyButton";
import { PromptCard } from "../components/PromptCard";
import { SceneImage } from "../components/Scene";
import { SplitText } from "../components/SplitText";
import { Glyph } from "../components/Glyph";
import { media } from "../lib/paths";
import { pageMeta } from "../lib/meta";

export const meta: Route.MetaFunction = () =>
  pageMeta(site.labels.homeTitle, site.description, "/");

export default function Home() {
  return (
    <>
      {/* Opening scene */}
      <section className="hero hero-home" aria-labelledby="hero-h">
        <SceneImage id="home-hero" cine="kenburns" eager className="hero-img" />
        <div className="hero-shade" aria-hidden="true" />
        <div className="letterbox top" data-letterbox aria-hidden="true" />
        <div className="letterbox bottom" data-letterbox aria-hidden="true" />
        <div className="wrap hero-inner">
          <p className="hero-kicker" data-cine-after="0">{site.labels.presents}</p>
          <SplitText as="h1" id="hero-h" className="hero-title" cine="title" text={home.title} />
          <p className="hero-lead" data-cine-after="1">{home.lead}</p>
          <div className="actions" data-cine-after="2">
            <a className="btn btn-light" href="#tools">{site.labels.seeTools}</a>
            <CopyButton text={prompts.starter} label="Copy the starter prompt" className="btn btn-ghost" />
          </div>
        </div>
        <a className="scroll-cue" href="#intern" aria-label="Scroll to the story"><span /></a>
      </section>

      {/* Every tool, one tap away */}
      <nav className="tool-strip" id="all-tools" aria-label={site.labels.toolsListName}>
        <ul className="wrap">
          {tools.map((t) => (
            <li key={t.slug}>
              <Link to={`/tools/${t.slug}`} viewTransition>
                <Glyph slug={t.slug} className="glyph glyph-sm" />
                <span><strong>{t.name}</strong><span>{t.cardLine}</span></span>
              </Link>
            </li>
          ))}
        </ul>
      </nav>

      {/* The idea, word by word */}
      <section className="statement" id="intern" data-cine="words" aria-labelledby="intern-h">
        <div className="wrap statement-inner">
          <h2 id="intern-h" className="sr-only">The idea behind every tool</h2>
          <SplitText className="statement-text" text={home.idea.analogy} />
        </div>
      </section>

      {/* The answer: each tool is the brief */}
      <section className="split" aria-labelledby="brief-h">
        <div className="wrap split-inner">
          <div className="split-media">
            <SceneImage id="home-intern" cine="clip" className="clip-img" />
          </div>
          <div className="split-copy" data-cine="reveal">
            <h2 id="brief-h" data-cine-item>{home.idea.heading}</h2>
            <ul className="ticks">
              {home.idea.points.map((p) => (
                <li key={p.title} data-cine-item><strong>{p.title}</strong><span>{p.text}</span></li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      {/* One scene per tool */}
      <section className="reel" id="tools" aria-labelledby="tools-h">
        <div className="wrap reel-head" data-cine="reveal">
          <h2 id="tools-h" data-cine-item>{site.labels.toolsHeading}</h2>
          <p className="reel-lead" data-cine-item>{site.labels.toolsLead}</p>
        </div>
        <ol className="stack" data-cine="stack" aria-label={site.labels.toolsListName}>
          {tools.map((t, i) => (
            <li key={t.slug} className="stack-scene" data-cine-scene>
              <Link to={`/tools/${t.slug}`} viewTransition className="stack-inner" data-cine-scene-inner aria-labelledby={`stack-${t.slug}-name stack-${t.slug}-promise`}>
                <SceneImage id={`tool-${t.slug}`} className="stack-img" name={`tool-${t.slug}`} />
                <span className="stack-shade" aria-hidden="true" />
                <span className="stack-dim" aria-hidden="true" />
                <span className="stack-copy">
                  <span className="stack-top">
                    <Glyph slug={t.slug} />
                    <span className="stack-count" aria-hidden="true">{i + 1} of {tools.length}</span>
                  </span>
                  <SplitText as="span" className="stack-name" text={t.name} id={`stack-${t.slug}-name`} />
                  <span className="stack-promise" id={`stack-${t.slug}-promise`}>{t.promise}</span>
                  <span className="stack-line">{t.cardLine}</span>
                  <span className="stack-foot">
                    <span className="status-word">{t.status.label}</span>
                    <span className="stack-open">Open {t.name}</span>
                  </span>
                </span>
              </Link>
            </li>
          ))}
        </ol>
      </section>

      {/* The standard */}
      <section className="standard" aria-labelledby="levels-h">
        <SceneImage id="home-standard" cine="parallax" className="standard-img" />
        <div className="standard-shade" aria-hidden="true" />
        <div className="wrap standard-inner" data-cine="draw">
          <div data-cine="reveal">
            <h2 id="levels-h" data-cine-item>{home.levels.heading}</h2>
            <p className="reel-lead" data-cine-item>{home.levels.intro}</p>
          </div>
          <div className="timeline-wrap">
          <span className="timeline-line" data-cine-line aria-hidden="true" />
          <ol className="timeline">
            {home.levels.steps.map((s, i) => (
              <li key={s.title} data-cine="reveal">
                <span className="timeline-num" aria-hidden="true">{i + 1}</span>
                <h3 data-cine-item>Level {i + 1}: {s.title}</h3>
                <p data-cine-item>{s.text}</p>
              </li>
            ))}
          </ol>
          </div>
        </div>
      </section>

      {/* By the numbers */}
      <section className="numbers" aria-labelledby="numbers-h">
        <div className="wrap">
          <h2 id="numbers-h" className="sr-only">By the numbers</h2>
          <p className="facts-line" data-cine="reveal">
            {home.factsLine.split(/(\{\d+\})/).map((part, k) => {
              const n = part.match(/^\{(\d+)\}$/);
              return n ? <b key={k}>{n[1]}</b> : part;
            })}
          </p>
        </div>
      </section>

      {/* First take */}
      <section className="take take-scene" id="start" aria-labelledby="starter-h">
        <SceneImage id="home-start" cine="parallax" className="take-img" />
        <div className="wrap narrow" data-cine="reveal">
          <h2 id="starter-h" data-cine-item>{home.starter.heading}</h2>
          <p className="reel-lead" data-cine-item>{home.starter.text}</p>
          <div data-cine-item><PromptCard prompt={prompts.starter} label="Copy the starter prompt" /></div>
        </div>
      </section>

      {/* Credits */}
      <section className="credits" aria-labelledby="maker-h">
        <div className="wrap credits-inner" data-cine="reveal">
          <img src={media(site.labels.authorPhoto)} alt={site.labels.author} width={180} height={180} className="portrait" data-cine-item />
          <div>
            <p className="credits-small" data-cine-item>{site.labels.authorKicker}</p>
            <h2 id="maker-h" data-cine-item>{site.labels.author}</h2>
            <p data-cine-item>{about.role} {about.specialty}</p>
            <p data-cine-item><Link to="/about" viewTransition className="btn btn-ghost">About {site.labels.author.split(" ")[0]}</Link></p>
          </div>
        </div>
      </section>
    </>
  );
}
