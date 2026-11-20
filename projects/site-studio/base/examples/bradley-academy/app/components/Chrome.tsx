import { useEffect, useState } from "react";
import { Link, NavLink } from "react-router";
import { site } from "../content/site";

export function Header() {
  const [solid, setSolid] = useState(false);
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
          <span className="wordmark-name">Bradley <em>Academy</em></span>
          <span className="wordmark-sub">{site.product}</span>
        </Link>
        <nav aria-label="Main" className="main-nav">
          <Link to="/#tools">Tools</Link>
          <Link to="/#start">Try it</Link>
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
          <p className="end-brand">Bradley <em>Academy</em></p>
          <p className="end-role">Practical AI tools for the jobs you repeat</p>
          <p className="end-role">Source code</p>
          <p className="end-name"><a href={site.source} rel="noopener">{site.sourceLabel}</a></p>
        </div>
        <div className="footer-grid">
          <p>Free to use, change and share under the Apache 2.0 licence. All examples use invented businesses and data.</p>
          <ul className="footer-links">
            <li><Link to="/about" viewTransition>About Bradley Ross</Link></li>
            <li><a href={site.linkedin} rel="noopener">LinkedIn</a></li>
            <li><a href={site.source} rel="noopener">The tools on GitHub</a></li>
          </ul>
        </div>
        <p className="footer-small">Built with Site Studio, in React, published by GitHub Pages. For the site owner: <Link to="/image-brief">the image brief</Link>.</p>
      </div>
    </footer>
  );
}
