// The motion layer. Pages mark elements with data-cine="..." and this file brings them to life with
// GSAP ScrollTrigger and Lenis smooth scrolling. It loads only in the browser, after the page is
// already readable, and does nothing when the reader asks for reduced motion.
//
//   title      words rise out of a mask when the page opens
//   kenburns   a slow push-in on an image as you scroll past it
//   parallax   an image moves slower than the page (data-speed, default 0.15)
//   reveal     rises and sharpens into view; children with data-cine-item follow in turn
//   words      a statement whose words light up one by one while its sticky text holds still
//   clip       an image wipes open from the centre
//   stack      a deck of full-screen scenes: each recedes as the next slides over it
//   draw       a line grows with scroll progress (data-cine-line inside)
//   count      a number counts up from zero when it arrives (data-to)

type Cleanup = () => void;

let lenis: { raf: (t: number) => void; destroy: () => void; scrollTo: (t: number, o?: object) => void } | null = null;

export function prefersReducedMotion() {
  return typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

const wordsIn = (el: HTMLElement) => el.querySelectorAll<HTMLElement>(".w > span");

/** Starts the motion for the current page. Call again after each route change; returns a cleanup. */
export async function startCinema(root: HTMLElement): Promise<Cleanup> {
  const doc = document.documentElement;
  if (prefersReducedMotion()) {
    doc.classList.remove("cine");
    return () => {};
  }
  const [{ gsap }, { ScrollTrigger }] = await Promise.all([import("gsap"), import("gsap/ScrollTrigger")]);
  gsap.registerPlugin(ScrollTrigger);

  if (!lenis && window.matchMedia("(pointer: fine)").matches) {
    const { default: Lenis } = await import("lenis");
    const l = new Lenis({ lerp: 0.09, wheelMultiplier: 0.95 });
    l.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((t) => l.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    lenis = l;
  }

  const ctx = gsap.context(() => {
    const all = (sel: string) => Array.from(root.querySelectorAll<HTMLElement>(`[data-cine="${sel}"]`));
    const wide = window.matchMedia("(min-width: 900px)").matches;

    for (const el of all("title")) {
      const words = wordsIn(el);
      gsap.set(el, { opacity: 1 });
      gsap.from(words, { yPercent: 110, duration: 1.15, ease: "power4.out", stagger: 0.06, delay: 0.15 });
    }
    for (const el of root.querySelectorAll<HTMLElement>("[data-cine-after]")) {
      gsap.from(el, { opacity: 0, y: 24, duration: 1, ease: "power3.out", delay: 0.55 + Number(el.dataset.cineAfter || 0) * 0.12 });
    }
    for (const el of root.querySelectorAll<HTMLElement>("[data-letterbox]")) {
      gsap.fromTo(el, { scaleY: 1 }, { scaleY: 0, duration: 1.4, ease: "power4.inOut", delay: 0.05 });
    }

    for (const el of all("kenburns")) {
      const img = el.querySelector("img");
      if (!img) continue;
      gsap.fromTo(img, { scale: 1.06, yPercent: 0 }, {
        scale: 1.22, yPercent: 8, ease: "none",
        scrollTrigger: { trigger: el, start: "top top", end: "bottom top", scrub: 1 },
      });
    }
    for (const el of all("parallax")) {
      const speed = Number(el.dataset.speed ?? 0.15);
      const img = el.querySelector("img") ?? el;
      gsap.fromTo(img, { yPercent: -speed * 100 }, {
        yPercent: speed * 100, ease: "none",
        scrollTrigger: { trigger: el, start: "top bottom", end: "bottom top", scrub: 1.2 },
      });
    }
    for (const el of all("reveal")) {
      const items = el.querySelectorAll<HTMLElement>("[data-cine-item]");
      const targets = items.length ? items : [el];
      gsap.from(targets, {
        opacity: 0, y: 24, duration: 0.95, ease: "power3.out", stagger: 0.08,
        scrollTrigger: { trigger: el, start: "top 82%", once: true },
      });
    }
    for (const el of all("words")) {
      // The section is tall and its text is sticky (CSS), so the words light up while it holds still.
      // No GSAP pin: pinning wraps React's elements in extra markup and breaks page changes.
      const words = wordsIn(el);
      gsap.fromTo(words, { opacity: 0.38 }, {
        opacity: 1, ease: "none", stagger: 0.08,
        scrollTrigger: { trigger: el, start: wide ? "top top" : "top 70%", end: wide ? "bottom bottom" : "bottom 40%", scrub: 0.8 },
      });
    }
    for (const el of all("clip")) {
      gsap.fromTo(el, { clipPath: "inset(18% 22% 18% 22% round 24px)" }, {
        clipPath: "inset(0% 0% 0% 0% round 0px)", ease: "none",
        scrollTrigger: { trigger: el, start: "top 90%", end: "top 20%", scrub: 1 },
      });
    }
    for (const stack of all("stack")) {
      const scenes = Array.from(stack.querySelectorAll<HTMLElement>("[data-cine-scene]"));
      scenes.forEach((scene, i) => {
        const next = scenes[i + 1];
        if (!next) return;
        gsap.to(scene.querySelector("[data-cine-scene-inner]") ?? scene, {
          scale: 0.92, filter: "brightness(0.45)", ease: "none",
          scrollTrigger: { trigger: next, start: "top bottom", end: "top top", scrub: true },
        });
      });
    }
    for (const el of all("count")) {
      const to = Number(el.dataset.to ?? el.textContent ?? 0);
      if (!to) continue;
      const state = { v: 0 };
      gsap.to(state, {
        v: to, duration: 1.8, ease: "power2.out",
        onUpdate: () => { el.textContent = String(Math.round(state.v)); },
        scrollTrigger: { trigger: el, start: "top 85%", once: true },
      });
    }
    for (const el of all("draw")) {
      const line = el.querySelector<HTMLElement>("[data-cine-line]");
      if (!line) continue;
      gsap.fromTo(line, { scaleY: 0 }, {
        scaleY: 1, ease: "none", transformOrigin: "top",
        scrollTrigger: { trigger: el, start: "top 70%", end: "bottom 60%", scrub: 0.6 },
      });
    }
  }, root);

  requestAnimationFrame(() => ScrollTrigger.refresh());
  return () => ctx.revert();
}

export function scrollToTopNow() {
  lenis?.scrollTo(0, { immediate: true });
}
