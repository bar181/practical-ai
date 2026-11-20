import { useEffect, useRef, useState, type KeyboardEvent, type ReactNode } from "react";

export type TabItem = { id: string; label: string; content: ReactNode };

/**
 * Tabs that keep their place in the address (#tab-id), so a tab can be linked to.
 * Before the page's script runs, every panel shows one after another, so nothing is hidden
 * from a reader or a search engine without script.
 */
export function Tabs({ items, label }: { items: TabItem[]; label: string }) {
  const [active, setActive] = useState(items[0].id);
  const [ready, setReady] = useState(false);
  const buttons = useRef<(HTMLButtonElement | null)[]>([]);

  useEffect(() => {
    // An address like #try-it may point inside a panel: open that panel, then scroll to the place.
    const goTo = (id: string) => {
      if (!id) return false;
      if (items.some((t) => t.id === id)) { setActive(id); return true; }
      const target = document.getElementById(id);
      const panel = target?.closest<HTMLElement>("[role=tabpanel]");
      if (!target || !panel) return false;
      setActive(panel.id.replace(/^panel-/, ""));
      requestAnimationFrame(() => requestAnimationFrame(() => target.scrollIntoView({ block: "start" })));
      return true;
    };
    const fromHash = () => goTo(decodeURIComponent(window.location.hash.slice(1)));
    const onClick = (e: MouseEvent) => {
      const a = (e.target as HTMLElement).closest?.("a[href^='#']");
      if (!a) return;
      const id = a.getAttribute("href")!.slice(1);
      if (goTo(id)) { e.preventDefault(); window.history.replaceState(null, "", `#${id}`); }
    };
    fromHash();
    setReady(true);
    window.addEventListener("hashchange", fromHash);
    document.addEventListener("click", onClick);
    return () => { window.removeEventListener("hashchange", fromHash); document.removeEventListener("click", onClick); };
  }, [items]);

  // Tell the tab row whether more tabs sit off either edge, so it can fade that edge.
  const list = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const el = list.current;
    if (!el) return;
    const mark = () => {
      const start = el.scrollLeft > 4;
      const end = el.scrollLeft + el.clientWidth < el.scrollWidth - 4;
      el.dataset.more = start && end ? "both" : start ? "start" : end ? "end" : "";
    };
    mark();
    el.addEventListener("scroll", mark, { passive: true });
    window.addEventListener("resize", mark);
    return () => { el.removeEventListener("scroll", mark); window.removeEventListener("resize", mark); };
  }, []);

  // Selection by activation: arrow keys move focus, Enter, Space or a tap selects. Selecting changes
  // the address and the panel height, so it should not happen just by moving focus.
  function choose(id: string) {
    setActive(id);
    const url = id === items[0].id ? window.location.pathname : `#${id}`;
    window.history.replaceState(null, "", url);
    requestAnimationFrame(() => {
      // Scroll effects measured the page with this panel hidden; ask them to measure again.
      window.dispatchEvent(new Event("resize"));
      // If the reader was deep in the last panel, start the new one at its top, just under the tab row.
      const strip = document.querySelector<HTMLElement>(".tab-strip");
      const panel = document.getElementById(`panel-${id}`);
      if (!strip || !panel) return;
      const below = strip.getBoundingClientRect().bottom;
      if (panel.getBoundingClientRect().top < below) window.scrollTo({ top: window.scrollY + panel.getBoundingClientRect().top - below });
    });
  }

  useEffect(() => {
    const el = buttons.current[items.findIndex((t) => t.id === active)];
    // Keep the selected tab visible in a scrolled tab row, without scrolling the page.
    el?.scrollIntoView({ block: "nearest", inline: "nearest", container: "nearest" } as ScrollIntoViewOptions);
  }, [active, items]);

  function onKey(e: KeyboardEvent<HTMLDivElement>) {
    const i = buttons.current.findIndex((b) => b === document.activeElement);
    if (i < 0) return;
    const next = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: items.length - 1 }[e.key];
    if (next === undefined) return;
    e.preventDefault();
    buttons.current[(next + items.length) % items.length]?.focus();
  }

  return (
    <div className="tabs" data-ready={ready || undefined}>
      <div className="tab-strip js-only">
        <div className="wrap">
          <div role="tablist" aria-label={label} className="tablist" onKeyDown={onKey} ref={list}>
            {items.map((t, i) => (
              <button
                key={t.id}
                ref={(el) => { buttons.current[i] = el; }}
                role="tab"
                type="button"
                id={`tab-${t.id}`}
                aria-controls={`panel-${t.id}`}
                aria-selected={t.id === active}
                tabIndex={t.id === active ? 0 : -1}
                onClick={() => choose(t.id)}
              >
                {t.label}
              </button>
            ))}
          </div>
        </div>
      </div>
      {items.map((t) => (
        <section
          key={t.id}
          role="tabpanel"
          id={`panel-${t.id}`}
          aria-labelledby={`tab-${t.id}`}
          hidden={ready && t.id !== active}
          className="tab-panel"
        >
          {t.content}
        </section>
      ))}
    </div>
  );
}
