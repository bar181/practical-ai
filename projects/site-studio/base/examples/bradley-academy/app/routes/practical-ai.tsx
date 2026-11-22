import { Link } from "react-router";
import type { Route } from "./+types/practical-ai";
import prompts from "../content/generated/prompts.json";
import { home, practical, site } from "../content/site";
import { tools } from "../content/tools";
import { CopyButton } from "../components/CopyButton";
import { PromptCard } from "../components/PromptCard";
import { SceneImage } from "../components/Scene";
import { SplitText } from "../components/SplitText";
import { Glyph } from "../components/Glyph";
import { media } from "../lib/paths";
import { pageMeta } from "../lib/meta";

export const meta: Route.MetaFunction = () =>
  pageMeta(site.labels.homeTitle, site.description, "/tools/");

export default function PracticalAI() {
  return (
    <>
      {/* Opening scene */}
      <section className="hero hero-home" aria-labelledby="hero-h">
        <SceneImage id="practical-hero" cine="kenburns" eager className="hero-img" />
        <div className="hero-shade" aria-hidden="true" />
        <div className="letterbox top" data-letterbox aria-hidden="true" />
        <div className="letterbox bottom" data-letterbox aria-hidden="true" />
        <div className="wrap hero-inner">
          <p className="hero-kicker" data-cine-after="0">{site.labels.presents}</p>
          <SplitText as="h1" id="hero-h" className="hero-title" cine="title" text={home.title} />
          <p className="hero-sub" data-cine-after="0">{practical.kicker}</p>
          <p className="hero-lead" data-cine-after="1">{home.lead}</p>
          <div className="actions" data-cine-after="2">
            <a className="btn btn-light" href="#all-tools">{site.labels.seeTools}</a>
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

      {/* The practical guide */}
      <section className="guide" id="guide" aria-labelledby="guide-h">
        <div className="wrap" data-cine="reveal">
          <h2 id="guide-h" data-cine-item>{practical.guide.heading}</h2>
          <p className="reel-lead" data-cine-item>{practical.guide.intro}</p>
          <ol className="guide-steps">
            {practical.guide.steps.map((g, i) => (
              <li key={g.title} data-cine-item>
                <span className="guide-num" aria-hidden="true">{i + 1}</span>
                <h3>{g.title}</h3>
                <p>{g.text}</p>
                <p className="guide-time">{g.time}</p>
              </li>
            ))}
          </ol>
        </div>
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

      {/* First take */}
      <section className="take take-scene" id="start" aria-labelledby="starter-h">
        <SceneImage id="home-start" cine="parallax" className="take-img" />
        <div className="wrap narrow" data-cine="reveal">
          <h2 id="starter-h" data-cine-item>{home.starter.heading}</h2>
          <p className="reel-lead" data-cine-item>{home.starter.text}</p>
          <div data-cine-item><PromptCard prompt={prompts.starter} label="Copy the starter prompt" /></div>
        </div>
      </section>

      {/* Agentic office hours */}
      <section className="credits office-hours" id="office-hours" aria-labelledby="oh-h">
        <div className="wrap credits-inner" data-cine="reveal">
          <img src={media(site.labels.authorAvatar)} alt={`An illustrated ${site.labels.author} with a small robot assistant`} width={180} height={180} className="portrait" data-cine-item />
          <div>
            <h2 id="oh-h" data-cine-item>{practical.officeHours.heading}</h2>
            <p className="reel-lead" data-cine-item>{practical.officeHours.text}</p>
            <div data-cine-item><PromptCard prompt={practical.officeHours.prompt} label="Copy the office hours prompt" /></div>
            <p className="muted" data-cine-item>{practical.officeHours.next} <Link to="/tools/practical-ai-guide" viewTransition>See the guide</Link></p>
          </div>
        </div>
      </section>

      {/* From the classroom */}
      <section className="credits" aria-labelledby="class-h">
        <div className="wrap narrow" data-cine="reveal">
          <p className="credits-small" data-cine-item>{practical.classroom.kicker}</p>
          <h2 id="class-h" data-cine-item>{practical.classroom.heading}</h2>
          <p data-cine-item>{practical.classroom.text}</p>
          <p data-cine-item className="actions">
            <Link to="/about" viewTransition className="btn btn-ghost">About {site.labels.author.split(" ")[0]}</Link>
          </p>
        </div>
      </section>
    </>
  );
}
