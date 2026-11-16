# Component catalogue

The parts a page can be built from. Each row is a working example in the studio. Pick parts that carry content; never add one for decoration.

Generated from the examples by `_build/build.py`.

## Page components (no photo needed)

| Component | What it is for | How it is made | Grow into |
| --- | --- | --- | --- |
| Big numbers | Three figures large enough to read from across a room. They count up once when they come into view. | A few lines of script | Motion or GSAP, for odometer-style digits |
| Timeline | What happened, or what will happen, in order. The line fills as you scroll past it. | A list and a CSS scroll-driven line | GSAP ScrollTrigger, for stages that animate one by one |
| Process flow | A small diagram that draws itself. It shows how a thing moves from start to finish. | Hand-written SVG | Mermaid for larger diagrams, GSAP for motion along the path |
| Comparison table | Options side by side on the same questions, with the recommended one picked out. | A plain HTML table | shadcn/ui tables, for sorting and filtering |
| Price table | Plans with one switch between monthly and yearly. The numbers change in place. | Buttons and a few lines of script | Magic UI or shadcn/ui pricing blocks |
| Questions and answers | Each question opens on a tap. People read only the ones they came with. | The HTML details element. No script. | Nothing needed |
| Customer quote | One person's words, set large. Use real words from a real customer, with their permission. | Type and a background colour | Nothing needed |
| Tabs | Several short answers in the space of one. Good when readers want different things. | Buttons and a few lines of script | shadcn/ui tabs |
| Bar chart | A handful of values compared. Thin bars, the number at the end of each, nothing else. | Plain HTML and CSS | Observable Plot or Chart.js, once you have more than a few bars |
| Progress ring | One share of a whole. Use it for a single figure that matters more than the rest. | Two SVG circles | Nothing needed |
| Callouts | A note, a warning and a confirmation. Each has an icon and a label as well as a colour, so it reads without the colour. | CSS only | Nothing needed |
| Old way, new way | The change in two lists. The old one is struck through, so the eye lands on the new one. | CSS only | Nothing needed |

## Photo components

| Component | What it is for | How it is made | Grow into |
| --- | --- | --- | --- |
| Pan and zoom | A still photo that moves slowly reads as film. Use it to open a page or to hold a quote. | One CSS animation | GSAP or Motion, for timed sequences of shots |
| Parallax window | The photo moves slower than the page, so the frame feels like a window with depth behind it. | CSS scroll-driven animation, plus a short script for older browsers | GSAP ScrollTrigger, Lenis for smooth scrolling |
| Photo-filled type | One word, large enough that the letters become windows. Good for a chapter break. | CSS background-clip on text | GSAP SplitText, to move each letter on its own |
| Scrolling photo tour | The photo stays put while the text scrolls. Each paragraph moves the camera to the part it talks about. | Sticky positioning and an IntersectionObserver | Scrollama, the step-trigger library used in newsrooms |
| Self-drawing line art | A sketch that draws itself as you scroll, then gives way to the real photo. The treeline, island and trunk were traced from the photo's own pixels. | SVG paths and stroke-dashoffset, tied to scroll | GSAP DrawSVG or Anime.js; Lottie or Rive for animation drawn by a designer |
| Chart from the photo | A chart is a component too. These numbers are measured from the photo, so the chart and the picture tell the same story. | Hand-written SVG, sized to your screen | Observable Plot for quick charts, D3 for custom ones, ECharts for dashboards |
| Before and after | Two versions of one picture with a divider to drag. It makes a change obvious without a word of explanation. | A range slider, a CSS filter and clip-path | Nothing needed. Supply two real photos in place of the filter. |
| Looks and voices | The same photo and the same message, five ways. A look sets the mood; a voice sets how it speaks. Describe both and a page stops sounding generic. | CSS filters, blend modes and the View Transitions API for the cross-fade | A saved style card per look, so every page you make can reuse it |
| Frosted glass card | Facts float over the photo on a pane that blurs what is behind it. The photo stays the star and the text stays readable. | CSS backdrop-filter | Magic UI or Aceternity UI, for ready-made animated cards |
| Bento grid | A summary as a tray of tiles in different sizes. Each tile holds one fact, so the eye can land anywhere. | CSS grid | shadcn/ui and Magic UI, which ship bento layouts |
| Swipe gallery | Cards in a row that snap into place one at a time. On a phone it is the most natural way to browse a set. | CSS scroll snap. No script. | Motion or GSAP, for dragging with momentum |
| Flip postcard | A photo with a second side. Put the picture on the front and the message on the back. | CSS 3D transforms and one line of script | React Bits and Aceternity UI, which ship tilt and 3D cards |
