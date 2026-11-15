# Artifact studio: landscape review

What already exists for making a page look good, checked before building more. Every entry was
checked on 2026-11-14 unless it says otherwise. Tools in this area change quickly, so follow the
link before relying on a line.

## Summary

- **Reuse first.** Browsers now do scroll effects and cross-fades without a library, and design
  skills for chat assistants already exist. The simple level should lean on both.
- **The advanced level is a wiring job, not a build.** The standard animation, chart and component
  libraries are free.
- **Nothing found does the whole job.** No tool was found that lets a non-designer pick a page
  type, a look and a voice in plain words. That gap is what the studio is for.

## Built into browsers

| Feature | State | Source |
| --- | --- | --- |
| Scroll-driven animations (`animation-timeline`) | In Chrome 115, Safari 26 and Firefox 159. Counted as newly available across browsers since late October 2026. Older browsers need a script fallback. | [web.dev, October 2026](https://web.dev/blog/web-platform-10-2026) |
| View transitions within one page | In all three engines. Counted as newly available across browsers in 2025. | [Chrome for Developers](https://developer.chrome.com/blog/view-transitions-in-2025) |
| Scroll snap, sticky positioning, `backdrop-filter`, `background-clip: text` | Long established. Not rechecked for this review. | From general knowledge |

## Skills and plugins for chat assistants

| Item | What it does | Source |
| --- | --- | --- |
| frontend-design, web-artifacts-builder, theme-factory | Anthropic's skills for design judgement, multi-part artifacts and ready-made themes | [anthropics/skills](https://github.com/anthropics/skills) |
| scrollytelling (community) | Asks which scroll pattern and which animation library to use before building | [skills.sh](https://skills.sh/doodledood/claude-code-plugins/scrollytelling) |
| elite-gsap (community) | GSAP recipes: ScrollTrigger, SplitText, SVG | [skills.sh](https://skills.sh/rshvr/elite-web-design/elite-gsap) |
| animated-component-libraries (community) | Covers Magic UI and React Bits | [skills.sh](https://skills.sh/freshtechbro/claudedesignskills/animated-component-libraries) |

Community skills are unreviewed. None has been installed or tested for this review. Read one
before installing it.

## Free libraries

| Library | Use | Licence | Source |
| --- | --- | --- | --- |
| GSAP | Scroll and timeline animation; includes ScrollTrigger, SplitText, DrawSVG | Free for commercial use under GSAP's own no-charge licence. Not open source. | [GSAP on GitHub](https://github.com/greensock/GSAP) |
| Motion | Animation for React, Vue and plain JavaScript | MIT | [OpenReplay comparison](https://blog.openreplay.com/motion-vs-gsap/) |
| Anime.js | Small animation library, strong on SVG | MIT | [Smashing Apps guide](https://www.smashingapps.com/best-free-javascript-animation-libraries-in-2026/) |
| Scrollama | Step triggers for scrollytelling, built on IntersectionObserver | MIT | [Scrollama on GitHub](https://github.com/russellsamora/scrollama) |
| Lenis | Smooth scrolling | Not checked | [Lenis on GitHub](https://github.com/darkroomengineering/lenis) |
| Observable Plot | Charts in a few lines | ISC | [LightningChart comparison](https://lightningchart.com/blog/best-d3-js-alternatives-in-2026/) |
| D3 | Custom charts | ISC | [Monterail comparison](https://www.monterail.com/blog/javascript-libraries-data-visualization) |
| Apache ECharts | Large catalogue of interactive charts | Apache 2.0 | Same |
| Chart.js | Standard charts | MIT | Same |
| shadcn/ui | Accessible components copied into a project | Not checked | [shadcn/ui](https://ui.shadcn.com/) |
| Magic UI | 150+ animated components | MIT | [DesignRevision](https://designrevision.com/alternatives/magic-ui) |
| Aceternity UI | Dark, dramatic animated components | Not checked | [Aceternity UI](https://ui.aceternity.com/) |
| React Bits | 110+ animated components | Not checked | [PkgPulse comparison](https://www.pkgpulse.com/guides/react-bits-vs-aceternity-magic-ui-2026) |

**Conflict to note.** One article describes GSAP as MIT licensed. GSAP's own README says it uses a
"no charge" standard licence, and another guide says it may not be forked into a competing
product. This review follows the README.

## Pages worth studying

| Page | Why | Source |
| --- | --- | --- |
| The Pudding | Pinned chart with scrolling text, across a whole catalogue | [pudding.cool](https://pudding.cool/) |
| Snow Fall, The New York Times (2012) | One of the first scrollytelling features | [Shorthand's list](https://shorthand.com/the-craft/scrollytelling-examples/) |
| Apple AirPods Pro | Product animation tied to scroll position | [The Plus Addons](https://theplusaddons.com/blog/scrollytelling/) |
| If the Moon Were Only 1 Pixel | Scale explained by scrolling | [Maglr's list](https://www.maglr.com/blog/best-scrollytelling-examples) |
| Awwwards | Daily winners; entries are tagged with the tools used | [awwwards.com](https://www.awwwards.com/) |
| Codrops | Experimental effects with source code | From general knowledge, not rechecked |

The pages themselves were not opened for this review. The descriptions come from the list articles
linked beside them.

## Build or license

| Level | Lean | Why |
| --- | --- | --- |
| Demo and simple | Build nothing new. Sentences, style cards and the browser. | Everything in the component gallery is plain HTML, CSS and a little script. |
| Working | Reuse. Wrap Anthropic's design skills with the studio's cards. | A skill that applies a look and a voice is small. Rewriting design judgement is not. |
| Automated | Reuse libraries. Review providers for video and audio add-ons, without selecting one here. | Video and audio cannot be done without an outside service. |

## Still to do

- Open and review each inspiration page and each community skill directly.
- Check the licences marked "Not checked".
- Test the twelve component sentences in fresh chats and record the results.
