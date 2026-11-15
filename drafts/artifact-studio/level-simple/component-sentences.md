# Component sentences

Twelve sentences, one per component in the [component gallery](../level-demo/). Copy a sentence, attach your own photo, and paste both into a chat assistant.

**Status: untested.** Each sentence describes what the gallery does. Nobody has yet pasted them into a fresh chat and recorded what came back. Until that test is run, treat them as starting points and expect a second message to adjust the result.

| Component | Effort | Made in the gallery with | Grow into |
| --- | --- | --- | --- |
| [Pan and zoom](#pan-and-zoom) | Easy. One sentence. | One CSS animation | GSAP or Motion, for timed sequences of shots |
| [Parallax window](#parallax-window) | Easy. One sentence. | CSS scroll-driven animation, plus a short script for older browsers | GSAP ScrollTrigger, Lenis for smooth scrolling |
| [Photo-filled type](#photo-filled-type) | Easy. One sentence. | CSS background-clip on text | GSAP SplitText, to move each letter on its own |
| [Scrolling photo tour](#scrolling-photo-tour) | Moderate. You say where to look; expect one round of nudging the zooms. | Sticky positioning and an IntersectionObserver | Scrollama, the step-trigger library used in newsrooms |
| [Self-drawing line art](#self-drawing-line-art) | Harder. The assistant has to analyse the photo. Ask for a looser sketch if the first one is off. | SVG paths and stroke-dashoffset, tied to scroll | GSAP DrawSVG or Anime.js; Lottie or Rive for animation drawn by a designer |
| [Chart from the photo](#chart-from-the-photo) | Moderate. The chart is easy; ask the assistant to show how it measured. | Hand-written SVG, sized to your screen | Observable Plot for quick charts, D3 for custom ones, ECharts for dashboards |
| [Before and after](#before-and-after) | Easy. One sentence. | A range slider, a CSS filter and clip-path | Nothing needed. Supply two real photos in place of the filter. |
| [Looks and voices](#looks-and-voices) | Easy. Name the look and the voice in the same sentence. | CSS filters, blend modes and the View Transitions API for the cross-fade | A saved style card per look, so every page you make can reuse it |
| [Frosted glass card](#frosted-glass-card) | Easy. One sentence. | CSS backdrop-filter | Magic UI or Aceternity UI, for ready-made animated cards |
| [Bento grid](#bento-grid) | Easy. List the tiles you want. | CSS grid | shadcn/ui and Magic UI, which ship bento layouts |
| [Swipe gallery](#swipe-gallery) | Easy. One sentence. | CSS scroll snap. No script. | Motion or GSAP, for dragging with momentum |
| [Flip postcard](#flip-postcard) | Easy. One sentence. | CSS 3D transforms and one line of script | React Bits and Aceternity UI, which ship tilt and 3D cards |

## Pan and zoom

A still photo that moves slowly reads as film. Use it to open a page or to hold a quote.

> Fill the frame with my photo and zoom in very slowly toward the island, like a documentary shot. Loop it back out.

Seen in: Documentary title cards and photo essays.

## Parallax window

The photo moves slower than the page, so the frame feels like a window with depth behind it.

> Put my photo in a wide window and move it slower than the page as I scroll. Float a small caption card over it that moves the other way.

Seen in: Product pages that tie movement to the scroll.

## Photo-filled type

One word, large enough that the letters become windows. Good for a chapter break.

> Write one huge word on a dark band and fill the letters with my photo. Slide the photo sideways inside the letters as I scroll.

Seen in: Magazine covers and award-site title screens.

## Scrolling photo tour

The photo stays put while the text scrolls. Each paragraph moves the camera to the part it talks about.

> Pin my photo while I scroll. I will give you seven short paragraphs. For each one, zoom the photo to the part it describes.

Seen in: The Pudding, and the New York Times feature Snow Fall.

## Self-drawing line art

A sketch that draws itself as you scroll, then gives way to the real photo. The treeline, island and trunk were traced from the photo's own pixels.

> Trace the main shapes in my photo as a simple line drawing. Draw the lines as I scroll, far things first, then fade the real photo in underneath.

Seen in: Explainer intros and Codrops demos.

## Chart from the photo

A chart is a component too. These numbers are measured from the photo, so the chart and the picture tell the same story.

> Measure how bright my photo is from top to bottom and chart it as a line with a soft fill. Put a strip of the real colours under the axis. Label only the highest and lowest points, and let me touch the chart to read the rest.

Seen in: The Pudding's data stories.

## Before and after

Two versions of one picture with a divider to drag. It makes a change obvious without a word of explanation.

> Show my photo as shot and with a warm sunset grade, as one picture with a divider I can drag from side to side.

Seen in: Renovation portfolios and satellite image comparisons.

## Looks and voices

The same photo and the same message, five ways. A look sets the mood; a voice sets how it speaks. Describe both and a page stops sounding generic.

One sentence per look. Each names the look and the voice together.

| Look | Voice | Sentence |
| --- | --- | --- |
| As shot | The patient teacher. Inspired by David Malan. Analogy first, then an example, then the detail. | Keep my photo as shot. Voice: a patient teacher. Open with an everyday analogy, then one worked example, then the detail. |
| Ink | The keynote. Inspired by Steve Jobs. One idea per screen and almost no text. | Make my photo high-contrast black and white. Voice: a keynote. One idea per screen, very short sentences, huge type. |
| Dusk | The storyteller. Inspired by Don Miller. A hook, a hero, a twist and an ending that stays with you. | Grade my photo like dusk, warm at the top and deep blue at the bottom. Voice: a storyteller. Start with a hook, give it a twist, end on a line that lingers. |
| Faded film | The pitch. Inspired by Don Draper. First person, emotional, about the feeling and never the feature. | Make my photo look like faded film, soft and slightly brown. Voice: an emotional pitch in the first person, about the feeling and never the feature. |
| Blueprint | The practical instructor. A best guess at Bradley Ross. Core concept first, one analogy, then steps you can use today. | Turn my photo into a two-colour blueprint in navy and pale blue. Voice: a practical instructor. Core concept first, one analogy, then steps I can follow today. |

Seen in: Photo app filters and brand style guides.

## Frosted glass card

Facts float over the photo on a pane that blurs what is behind it. The photo stays the star and the text stays readable.

> Float the key facts in a frosted glass card over my photo. Keep the card over the sky so dark text stays readable.

Seen in: Phone lock screens and weather apps.

## Bento grid

A summary as a tray of tiles in different sizes. Each tile holds one fact, so the eye can land anywhere.

> Summarise this as a bento grid: one tall photo tile, three big-number tiles, a colour palette tile and a small chart tile.

Seen in: Product launch summaries.

## Swipe gallery

Cards in a row that snap into place one at a time. On a phone it is the most natural way to browse a set.

> Crop six details from my photo and show them as cards I can swipe sideways, snapping one card at a time. Give each a two-word title and one line.

Seen in: App store listings and social carousels.

## Flip postcard

A photo with a second side. Put the picture on the front and the message on the back.

> Make my photo a postcard with a white border. When I tap it, flip it over in 3D and show a short handwritten-style note, a stamp and address lines on the back.

Seen in: Invitations, team pages and product cards.
