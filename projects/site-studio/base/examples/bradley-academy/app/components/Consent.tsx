import { useEffect, useState } from "react";
import { Link } from "react-router";

// Analytics, only when SITE_GA_ID is set at build time, and only after the visitor says yes.
// The choice is kept in this browser; nothing loads before it.
const KEY = "ba-analytics";

function loadAnalytics(id: string) {
  if (document.getElementById("ga-tag")) return;
  const w = window as unknown as { dataLayer: unknown[]; gtag: (...a: unknown[]) => void };
  w.dataLayer = w.dataLayer || [];
  w.gtag = function gtag() { w.dataLayer.push(arguments); };
  w.gtag("js", new Date());
  w.gtag("config", id, { anonymize_ip: true });
  const s = document.createElement("script");
  s.id = "ga-tag";
  s.async = true;
  s.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(id)}`;
  document.head.appendChild(s);
}

export function Consent() {
  const id = __GA_ID__;
  const [ask, setAsk] = useState(false);
  useEffect(() => {
    if (!id) return;
    let choice: string | null = null;
    try { choice = localStorage.getItem(KEY); } catch { /* storage blocked: ask each visit */ }
    if (choice === "yes") loadAnalytics(id);
    else if (choice !== "no") setAsk(true);
  }, [id]);
  if (!id || !ask) return null;
  const decide = (yes: boolean) => {
    try { localStorage.setItem(KEY, yes ? "yes" : "no"); } catch { /* fine */ }
    if (yes) loadAnalytics(id);
    setAsk(false);
  };
  return (
    <div className="consent" role="region" aria-label="Analytics choice">
      <p>May this site count your visit with Google Analytics? It sets cookies only if you say yes. <Link to="/privacy" viewTransition>Privacy</Link></p>
      <p className="consent-actions">
        <button type="button" className="btn btn-light btn-sm" onClick={() => decide(true)}>Yes, count my visit</button>
        <button type="button" className="btn btn-ghost btn-sm" onClick={() => decide(false)}>No thanks</button>
      </p>
    </div>
  );
}
