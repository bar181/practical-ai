import { Link, NavLink } from "react-router";
import { site } from "../content/site";

export function Header() {
  return (
    <header className="site-header">
      <div className="wrap header-row">
        <Link to="/" className="wordmark" aria-label={`${site.brand}, home`}>
          <span className="wordmark-mark" aria-hidden="true">BA</span>
          <span className="wordmark-text">
            <span className="wordmark-name">{site.brand}</span>
            <span className="wordmark-sub">{site.product}</span>
          </span>
        </Link>
        <nav aria-label="Main" className="main-nav">
          <NavLink to="/" end>Tools</NavLink>
          <NavLink to="/about">About Bradley</NavLink>
          <a href={site.source} rel="noopener">Source code</a>
        </nav>
      </div>
    </header>
  );
}

export function Footer() {
  return (
    <footer className="site-footer">
      <div className="wrap footer-grid">
        <div>
          <p className="footer-brand">{site.brand}</p>
          <p>Practical AI tools for the jobs you repeat. Free to use, change and share under the Apache 2.0 licence.</p>
        </div>
        <ul className="footer-links">
          <li><Link to="/about">About Bradley Ross</Link></li>
          <li><a href={site.linkedin} rel="noopener">LinkedIn</a></li>
          <li><a href={site.source} rel="noopener">Source code: {site.sourceLabel}</a></li>
        </ul>
      </div>
      <p className="wrap footer-small">All examples use invented businesses and data. Built with Site Studio, in React, published by GitHub Pages.</p>
    </footer>
  );
}
