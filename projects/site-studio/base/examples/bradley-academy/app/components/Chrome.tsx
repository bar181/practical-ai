import { useEffect, useRef, useState } from "react";
import { Link, NavLink, useLocation } from "react-router";
import { site } from "../content/site";

// The brand, with every word after the first set in italic brass.
const [brandFirst, ...brandRest] = site.brand.split(" ");
const Brand = () => <>{brandFirst} <em>{brandRest.join(" ")}</em></>;

const navLinks = [
  { to: "/research", label: "Research" },
  { to: "/tools", label: "Practical AI" },
  { to: "/about", label: "About" },
];

export function Header() {
  const [solid, setSolid] = useState(false);
  const menu = useRef<HTMLDetailsElement>(null);
  const { pathname } = useLocation();
  useEffect(() => {
    const on = () => setSolid(window.scrollY > 40);
    on();
    window.addEventListener("scroll", on, { passive: true });
    return () => window.removeEventListener("scroll", on);
  }, []);
  // Close the phone menu after a route change.
  useEffect(() => { if (menu.current) menu.current.open = false; }, [pathname]);
  useEffect(() => {
    const close = (focus: boolean) => {
      const m = menu.current;
      if (!m?.open) return;
      m.open = false;
      if (focus) m.querySelector("summary")?.focus();
    };
    const onKey = (e: KeyboardEvent) => { if (e.key === "Escape") close(true); };
    const onDown = (e: PointerEvent) => { if (menu.current && !menu.current.contains(e.target as Node)) close(false); };
    const onFocus = (e: FocusEvent) => { if (menu.current && !menu.current.contains(e.target as Node)) close(false); };
    document.addEventListener("keydown", onKey);
    document.addEventListener("pointerdown", onDown);
    document.addEventListener("focusin", onFocus);
    return () => { document.removeEventListener("keydown", onKey); document.removeEventListener("pointerdown", onDown); document.removeEventListener("focusin", onFocus); };
  }, []);
  return (
    <header className="site-header" data-solid={solid || undefined}>
      <div className="wrap header-row">
        <Link to="/" className="wordmark" viewTransition aria-label={`${site.brand}, home`}>
          <span className="wordmark-name"><Brand /></span>
          {pathname === "/" ? null : <span className="wordmark-sub">{site.product}</span>}
        </Link>
        <nav aria-label="Main" className="main-nav">
          {navLinks.map((l) => <NavLink key={l.to} to={l.to} viewTransition>{l.label}</NavLink>)}
          <Link className="btn btn-light btn-sm" to="/research#early-access" viewTransition>Research partners</Link>
        </nav>
        <details className="menu" ref={menu}>
          <summary aria-label="Menu"><span className="menu-icon" aria-hidden="true" />Menu</summary>
          <nav aria-label="Main, phone" className="menu-panel">
            {navLinks.map((l) => <NavLink key={l.to} to={l.to} viewTransition>{l.label}</NavLink>)}
            <Link className="btn btn-light" to="/research#early-access" viewTransition>Research partners</Link>
          </nav>
        </details>
      </div>
    </header>
  );
}

export function Footer() {
  const onTools = useLocation().pathname.startsWith("/tools");
  return (
    <footer className="site-footer">
      <div className="wrap">
        <div className="end-credits">
          <p className="end-brand"><Brand /></p>
          <p className="end-role">Bradley Ross, Agentic Architect and Researcher</p>
          <p className="end-role">{site.labels.footerTagline}</p>
          {onTools ? <><p className="end-role">Source code</p>
          <p className="end-name"><a href={site.source} rel="noopener">{site.sourceLabel}</a></p></> : null}
        </div>
        <div className="footer-grid">
          {onTools ? <p>{site.labels.licence}</p> : <p>Based in Toronto, working on US Eastern time.</p>}
          <ul className="footer-links">
            <li><Link to="/research" viewTransition>Research</Link></li>
            <li><Link to="/tools" viewTransition>Practical AI</Link></li>
            <li><Link to="/about" viewTransition>About</Link></li>
            <li><Link to="/privacy" viewTransition>Privacy</Link></li>
            <li><a href={site.linkedin} rel="noopener">LinkedIn</a></li>
            <li><a href={site.source} rel="noopener">{site.labels.sourceLink}</a></li>
          </ul>
        </div>
        <p className="footer-small">{site.labels.operator} {site.labels.builtWith}</p>
      </div>
    </footer>
  );
}
