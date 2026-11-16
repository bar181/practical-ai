# Delivery note

Page: `out.html` (one file, 393 KB, no network requests, system fonts). Checked in headless Chrome at 320, 390 and 1440 pixels wide, with scripts off and with reduced motion on. Not checked on a real phone or in Safari or Firefox.

## Chose

- **Kind of thing:** a page to be read, because you asked for three treatments in sequence, not slides or a post.
- **Parts:** the three you named, followed exactly and in your order. 1) Slow pan and zoom on the opening picture (32 seconds each way, with a "Pause the motion" tick box). 2) One word in huge letters filled with the picture; the picture drifts inside the letters as you scroll. 3) A flip card: the picture as a postcard that turns over on tap, on the button, or with the space bar. That is three moving parts, the guide's maximum.
- **Recipe:** one-page report. No recipe in the guide fits a picture-led page, and the guide's rule for that case is "use the one-page report". It contributes only the title and the two-sentence summary. Every other report section is listed under Missing.
- **Voice:** analyst, because the guide says to take the recipe's first voice when none is named. In practice this gave: the point as the title, the answer in two sentences, full-sentence headings, a quiet page. Your request overrides the voice's "one picture at most, at the top" and its charts.
- **Look:** colours taken from your picture, which the guide ranks above the voice's default look. Six tokens:
  - Colours measured in the picture: `#30232a` 30%, `#572f2b` 27%, `#834132` 18%, `#1e1012` 12%, `#c2603d` 8%, `#f6a35d` 4%.
  - Text `#1e1012` (the darkest). Background `#f4edf0` (a paler step of the largest, `#30232a`). Panel `#fcf8f9`. Rule lines `#cdbcc4`. Secondary text `#572f2b`. Accent `#e98746` (the most vivid colour in the water), used only on the two controls.
  - Contrast: text on background 16.0 to 1. Secondary text on background 9.9 to 1. Text on panel 17.5 to 1. Text on the accent button 7.1 to 1. The accent against the background is only 2.3 to 1, so both controls carry a dark outline and the tick box shows a drawn tick.
- **Preferences applied:** none. No preferences file came with the request.
- **Front-end design skill:** not loaded. The test rules limit me to the named files.

## Assumed

- **The word is "SKY".** You did not say which word. I could not ask, so I picked a word that only describes what the picture shows, and a short one so the letters are as large as the screen allows (about 170 pixels tall on a phone). The file is named `toronto.jpg`, but your message does not name the place, so the page does not either. Changing the word means editing two lines (the `<text>` and the `<title>` in the SVG). A longer word still fits the width, but its letters get squeezed unless the size is retuned.
- **The back of the postcard carries your own sentence**, word for word: "Any picture works: a place, a product, a person who has agreed to be shown." It is the only line in your notes that reads as content. If it was meant as a note to me and not as words for the page, the back should be blank or carry your message.
- **The title and summary** ("One picture, shown three ways" and the two sentences under it) are my wording. They only restate your request. No fact was added.
- **Audience and job.** Unknown. I assumed the reader is someone you want to show these three picture effects to, on a phone, and that the page's one job is to show them. There is no call to action.
- **The opening shot moves on its own, on a timer.** The guide says to tie movement to scrolling, but a documentary pan that only moves when the reader scrolls would not be an opening shot. The scroll-tied rule is applied to the word section instead.
- **The pan direction.** On a phone the shot travels left to right across the skyline while pushing in. On a wide screen it tilts down from the cloud to the skyline. The picture is square, so which axis has room depends on the screen.
- **Alt text** describes only what can be seen (a skyline in silhouette, a tall tower, a low sun, still water, a cloud shaped like an infinity sign). It names no place and does not say sunrise or sunset.
- **Controls are tick boxes styled as buttons**, not `button` elements, so the pause and the postcard both work with scripts off.

## Missing

- The word you want in the huge letters.
- A message, a name and an address for the back of the postcard, if you want it to read like a sent card. The stamp box and address lines are empty on purpose.
- Where the picture is and when it was taken, if you want a caption.
- Who the page is for and what they should do after seeing it.
- Everything else the one-page report recipe expects, none of which was supplied and none of which is on the page: period, reader, three or four numbers with their change, a trend chart, a breakdown table, what changed, what happens next. The analyst voice's method, limits and next steps with owner and date are absent for the same reason.

## Check before sharing

- You have the right to share this picture. Your notes mention "a person who has agreed to be shown"; this picture shows no person, so no consent is needed for this one.
- The word. "SKY" is my placeholder choice, not yours.
- The postcard's back. Make sure that sentence is what you want a reader to find there.
- Open it on a real phone. The huge letters use whichever heavy system typeface the device has (Impact, Avenir Next Condensed, Roboto Condensed or a fallback), so their shape differs from device to device. They always fill the width.
- Bright parts of the picture inside the letters are close in lightness to the pale page, so a letter edge can soften for a moment as the picture drifts. The word is also given to screen readers in text.
- On a short page like this one, the picture inside the letters travels about two thirds of its full range on a phone, because the page ends before the word can scroll off the top.
- The picture carried no location data (I checked: no EXIF block). It is embedded three times, twice at full size and once smaller for the postcard.
- How you send it. A bare HTML file opens as code on many phones. Share it as a hosted page or a preview.
- Nothing has been posted, sent or published.
