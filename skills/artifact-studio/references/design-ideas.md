# Design ideas

A short, chosen set of ideas for cards, layouts and colour. Use them when you pick the parts and the look.
Generated from the studio's design tabs by `drafts/artifact-studio/base/source/build.py`. Edit the views, not this file.

## Contents

- Cards
- Layouts
- Colour
- A palette from one brand colour

## Cards

Rules:

- One subject for each card. If you need the word "and" to describe it, make two cards.
- The most important thing first. A reader should get the point from the top third.
- One main action. A second action is quieter. A third belongs on the page the card leads to.
- The same padding and the same order in every card of a row. Rows line up because the cards match.
- No card inside a card, and a light hand with shadows. A border or a soft tint is usually enough.

| Idea | What it is | Rule or use |
| --- | --- | --- |
| Summary card | A title, one line and a way in. The plain card that leads to more detail. Use it for a list of services, articles or projects. | Use for: services, articles, projects, a list of next steps |
| Stat card | One number, what it measures, and how it has changed. The change is written in words and never shown by colour alone. | Use for: reports, dashboards, the top of a proposal |
| Media card | A picture, then a title, a line of detail and one action. Every picture in a row has the same shape, so the titles line up. | Use for: case studies, products, articles, team pages |
| Quote card | What a customer said, who said it and what they are to you. Use only words a real person gave you. These are invented to show the shape. | Use for: landing pages, proposals, the end of a case study |
| Option card | A choice with a price: the name, the price, three things it includes and one button. Mark the one you recommend, and say why in its label. | Use for: proposals, pricing pages, a choice of plans |
| Action card | One thing someone has to do: its state, what it is, when it is due and the button that does it. The state is written out, so it reads without colour. | Use for: customer portals, onboarding, a weekly to-do |

## Layouts

| The reader has to | Use |
| --- | --- |
| Read something through | Single column |
| Scan a long page for the part they need | Headings down the left |
| Do one thing | Corner to corner |
| Weigh two things, or see a picture beside a message | Split screen |
| Browse many things of one kind | Card grid |
| Take in several different things at a glance | Bento grid |

| Idea | What it is | Rule or use |
| --- | --- | --- |
| Single column | One column of text at a comfortable width, with nothing beside it. The layout for anything meant to be read from top to bottom. | Keep lines to about 60 to 75 characters. wider than that and readers lose their place. |
| Headings down the left | On a long page people read the first lines across, then run down the left edge looking for a heading that matters to them. This is often called the F-pattern. Give the left edge something worth finding. | Start every heading and every first sentence with the words that carry the meaning. "refunds: 14 days" beats "information about our approach to refunds". |
| Corner to corner | On a page with few words the eye starts top left, crosses to the top right, drops diagonally and ends bottom right. This is the Z-pattern. Put your name where the eye starts and the button where it ends. | One action, placed where the eye finishes. a long page repeats the shape: picture left then right, section by section. |
| Split screen | Two halves of equal weight: a message and a picture, or two choices. On a phone the halves stack, so decide which comes first. | The halves must be equals. if one is clearly less important, it is a sidebar, and a sidebar should be narrower. |
| Card grid | Rows of matching cards. Nothing is more important than anything else, which is the point: the reader browses and chooses. | Every card the same height, every picture the same shape, the same order inside each. |
| Bento grid | Tiles of different sizes packed into one block, like a lunch box. One tile is clearly the largest. The rest support it. | One dominant tile. keep the same padding and the same corner in every tile, or it looks like a jumble. |

## Colour

Rules:

- Mostly quiet, a little loud. About 60 parts background, 30 parts text and structure, 10 parts accent.
- One accent. It marks what to act on. If it is also used for decoration, it stops meaning anything.
- Greys with a trace of your colour. Pure grey looks dead beside a brand colour. A slight tint makes them belong together.
- Check every pair of text and background. 4.5 to 1 for ordinary text, 3 to 1 for large text, 7 to 1 if you can.
- Never colour alone. If red means late, the word "late" is there too.

| Idea | What it is | Rule or use |
| --- | --- | --- |
| A palette from one colour | Give it the one colour you already have, as a position on the colour wheel from 0 to 359. It returns seven colours with a job each, and checks every pair of text and background. The first one shown is hue 45. | Use for: any page, deck or post. paste the result into your design spec |
| 60, 30, 10 | A rule borrowed from decorating a room. The largest share is calm, the next gives structure, and the smallest draws the eye. Judge it by eye: it is about weight, not a count of pixels. On a dense screen such as a dashboard the calm share is nearer 90. | Use for: landing pages, decks, social pictures |
| One colour in even steps | Nine shades of one colour, from nearly white to nearly black, where each step looks the same size to the eye. Older colour sums make yellow steps look bigger than blue ones. The OKLCH way of writing colour fixes that, and current browsers understand it. | Use for: design specs, charts in one colour, hover and pressed states |
| Colours that go together | Start from your colour and turn the wheel, keeping the lightness and strength the same. Because only the direction changes, the colours feel like a set. One of them is still the accent. The others are for charts, labels and pictures. | Use for: charts, labels, illustrations, a set of social pictures |
| Contrast you can read | Contrast is a ratio between the text and what is behind it, from 1 to 1 (invisible) up to 21 to 1 (black on white). Ordinary text needs 4.5. Two of these four pairs pass. The other two use colours that look fine side by side and still fail as text. | Use for: every page before it goes out |

## A palette from one brand colour

When the person has one brand colour and nothing else, build the rest from its hue. Each role is a fixed lightness and strength in OKLCH, with the hue taken from the brand.

| Role | Lightness | Chroma | Share of the page |
| --- | --- | --- | --- |
| Page background | 0.97 | 0.012 | 60 parts |
| Panels and cards | 0.93 | 0.02 | as needed |
| Borders and rules | 0.86 | 0.025 | as needed |
| Secondary text | 0.48 | 0.03 | 30 parts |
| Main text | 0.22 | 0.03 | as needed |
| Buttons and links | 0.46 | 0.14 | 10 parts |
| Highlights behind text | 0.92 | 0.05 | as needed |

Write each colour as `oklch(lightness chroma hue)` with a hex value beside it. Then check these pairs and list the ratios in the delivery note:

- Main text on the page background: at least 7 to 1
- Secondary text on the page background: at least 4.5 to 1
- Secondary text on panels: at least 4.5 to 1
- White text on a button: at least 4.5 to 1
- Links on the page background: at least 4.5 to 1
- Main text on a highlight: at least 7 to 1

About 60 parts background, 30 parts text and structure, 10 parts accent, judged by eye and not by counting pixels. The accent is for things to act on and nothing else.

With the studio's MCP server connected, `artifact-studio:make_palette` does the sums and the checks.
