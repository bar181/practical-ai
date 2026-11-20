import { useEffect, useState } from "react";
import { Link, NavLink, useLocation } from "react-router";
import { site } from "../content/site";

// The brand, with every word after the first set in italic brass.
const [brandFirst, ...brandRest] = site.brand.split(" ");
const Brand = () => <>{brandFirst} <em>{brandRest.join(" ")}</em></>;

export function Header() {
  const [solid, setSolid] = useState(false);
  const onTool = useLocation().pathname.startsWith("/tools/");
  useEffect(() => {
    const on = () => setSolid(window.scrollY > 40);
    on();
    window.addEventListener("scroll", on, { passive: true });
    return () => window.removeEventListener("scroll", on);
  }, []);
  return (
    <header className="site-header" data-solid={solid || undefined}>
      <div className="wrap header-row">
        <Link to="/" className="wordmark" viewTransition aria-label={`${site.brand}, home`}>
          <span className="wordmark-name"><Brand /></span>
          <span className="wordmark-sub">{site.product}</span>
        </Link>
        <nav aria-label="Main" className="main-nav">
          <Link to="/#all-tools">Tools</Link>
          {onTool ? <a href="#try-it">Try it</a> : <Link to="/#start">Try it</Link>}
          <NavLink to="/about" viewTransition>About</NavLink>
        </nav>
      </div>
    </header>
  );
}

export function Footer() {
  return (
    <footer className="site-footer">
      <div className="wrap">
        <div className="end-credits">
          <p className="end-brand"><Brand /></p>
          <p className="end-role">{site.labels.footerTagline}</p>
          <p className="end-role">Source code</p>
          <p className="end-name"><a href={site.source} rel="noopener">{site.sourceLabel}</a></p>
        </div>
        <div className="footer-grid">
          <p>{site.labels.licence}</p>
          <ul className="footer-links">
            <li><Link to="/about" viewTransition>About {site.labels.author}</Link></li>
            <li><a href={site.linkedin} rel="noopener">LinkedIn</a></li>
            <li><a href={site.source} rel="noopener">The tools on GitHub</a></li>
          </ul>
        </div>
        <p className="footer-small">Built with Site Studio, in React, published by GitHub Pages. For the site owner: <Link to="/image-brief">the image brief</Link>.</p>
      </div>
    </footer>
  );
}
