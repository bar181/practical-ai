import type { Route } from "./+types/privacy";
import { site } from "../content/site";
import { pageMeta } from "../lib/meta";

const analytics = Boolean(__GA_ID__);

export const meta: Route.MetaFunction = () =>
  pageMeta(`Privacy | ${site.brand}`, "What this site keeps about you, and what it does not.", "/privacy/");

export default function Privacy() {
  return (
    <section className="plain-hero prose-page" aria-labelledby="privacy-h">
      <div className="wrap narrow">
        <h1 id="privacy-h">Privacy</h1>
        <p className="lead">The short version: this site has no forms and no accounts, and it keeps nothing about you.</p>
        <h2>What it keeps</h2>
        {analytics ? (
          <p>If you say yes when asked, Google Analytics counts your visit: which pages you open, roughly where from, and on what kind of device. It sets cookies only after that yes. If you say no, nothing is counted. Your choice is kept in your own browser.</p>
        ) : (
          <p>Nothing. There is no analytics, no tracking and no cookie.</p>
        )}
        <p>The site is hosted on GitHub Pages, which keeps standard server logs, such as addresses that visit, under GitHub's own privacy statement.</p>
        <h2>Links that leave the site</h2>
        <p>LinkedIn, GitHub and other sites linked from here have their own privacy policies.</p>
        <h2>Who runs it</h2>
        <p>{site.labels.operator} Questions: <a href={site.linkedin} rel="noopener">connect on LinkedIn</a>.</p>
      </div>
    </section>
  );
}
