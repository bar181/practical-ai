import { useEffect } from "react";
import { isRouteErrorResponse, Links, Meta, Outlet, Scripts, ScrollRestoration, useLocation } from "react-router";
import type { Route } from "./+types/root";
import "@fontsource-variable/bodoni-moda/wght.css";
import "@fontsource-variable/bodoni-moda/wght-italic.css";
import "@fontsource/atkinson-hyperlegible-next/400.css";
import "@fontsource/atkinson-hyperlegible-next/700.css";
import "./styles/site.css";
import { Footer, Header } from "./components/Chrome";
import { prefersReducedMotion, startCinema } from "./lib/cinema";
import { freezeAnimatedImages } from "./lib/still";
import { NotFoundMessage } from "./routes/not-found";

export const links: Route.LinksFunction = () => [
  { rel: "icon", href: `${import.meta.env.BASE_URL}favicon.svg`, type: "image/svg+xml" },
];

// Runs before the page paints: marks the page for motion, unless the reader asked for less.
// If the motion script never arrives, CSS shows everything anyway after a moment.
const motionFlag = `document.documentElement.classList.add('js');try{if(!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('cine')}catch(e){}`;

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="theme-color" content="#1b0d11" />
        <script dangerouslySetInnerHTML={{ __html: motionFlag }} />
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
  const { pathname } = useLocation();
  useEffect(() => {
    let stop: (() => void) | undefined;
    let alive = true;
    const main = document.getElementById("main");
    if (!main) return;
    // A reader who asked for less motion sees each animated capture as a still of its first frame.
    const thaw = prefersReducedMotion() ? freezeAnimatedImages(main) : undefined;
    startCinema(main).then((s) => (alive ? (stop = s) : s()));
    return () => { alive = false; stop?.(); thaw?.(); };
  }, [pathname]);
  return <Outlet />;
}

// The page shell (404.html on GitHub Pages) is only ever served for an address with no page, so its
// fallback is the not-found message: it reads without script, and the app shows the same once it runs.
export function HydrateFallback() {
  return <NotFoundMessage />;
}

export function ErrorBoundary({ error }: Route.ErrorBoundaryProps) {
  const notFound = isRouteErrorResponse(error) && error.status === 404;
  return (
    <section className="plain-hero">
      <div className="wrap">
        <h1>{notFound ? "That page is not here" : "Something went wrong"}</h1>
        <p className="lead">{notFound ? "The address may have changed. Every tool is on the home page." : "Reload the page. If it happens again, the home page lists every tool."}</p>
        <p><a className="btn btn-light" href={import.meta.env.BASE_URL}>Go to the home page</a></p>
      </div>
    </section>
  );
}
