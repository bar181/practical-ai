import type { Route } from "./+types/not-found";
import { Link } from "react-router";
import { site } from "../content/site";

export const meta: Route.MetaFunction = () => [{ title: `Page not found | ${site.brand}` }, { name: "robots", content: "noindex" }];

/**
 * The not-found message. The root also shows it as the page's fallback, so the 404.html that GitHub
 * Pages serves for an unknown address says so before any script runs.
 */
export function NotFoundMessage() {
  return (
    <section className="plain-hero" aria-labelledby="nf-h">
      <div className="wrap">
        <h1 id="nf-h">That page is not here</h1>
        <p className="lead">The address may have changed. Every tool is listed on the home page.</p>
        <p className="actions"><Link className="btn btn-light" to="/">Go to the home page</Link></p>
      </div>
    </section>
  );
}

export default function NotFound() {
  return <NotFoundMessage />;
}
