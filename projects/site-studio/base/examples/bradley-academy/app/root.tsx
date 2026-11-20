import { isRouteErrorResponse, Links, Meta, Outlet, Scripts, ScrollRestoration } from "react-router";
import type { Route } from "./+types/root";
import "@fontsource-variable/bricolage-grotesque/wght.css";
import "@fontsource/atkinson-hyperlegible-next/400.css";
import "@fontsource/atkinson-hyperlegible-next/700.css";
import "./styles/site.css";
import { Footer, Header } from "./components/Chrome";

export const links: Route.LinksFunction = () => [
  { rel: "icon", href: `${import.meta.env.BASE_URL}favicon.svg`, type: "image/svg+xml" },
];

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="theme-color" content="#1d3b33" />
        <Meta />
        <Links />
      </head>
      <body>
        <a className="skip" href="#main">Skip to the content</a>
        <Header />
        <main id="main">{children}</main>
        <Footer />
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

export default function App() {
  return <Outlet />;
}

export function ErrorBoundary({ error }: Route.ErrorBoundaryProps) {
  const notFound = isRouteErrorResponse(error) && error.status === 404;
  return (
    <section className="band">
      <div className="wrap band-inner">
        <h1>{notFound ? "That page is not here" : "Something went wrong"}</h1>
        <p className="lead">{notFound ? "The address may have changed. Every tool is listed on the home page." : "Reload the page. If it happens again, the home page lists every tool."}</p>
        <p><a className="btn btn-primary" href={import.meta.env.BASE_URL}>Go to the home page</a></p>
      </div>
    </section>
  );
}
