import type { Route } from "./+types/not-found";
import { Link } from "react-router";
import { site } from "../content/site";

export const meta: Route.MetaFunction = () => [{ title: `Page not found | ${site.brand}` }, { name: "robots", content: "noindex" }];

export default function NotFound() {
  return (
    <section className="band">
      <div className="wrap band-inner">
        <h1>That page is not here</h1>
        <p className="lead">The address may have changed. Every tool is listed on the home page.</p>
        <p><Link className="btn btn-primary" to="/">Go to the home page</Link></p>
      </div>
    </section>
  );
}
