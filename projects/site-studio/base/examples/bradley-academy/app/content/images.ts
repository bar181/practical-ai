// Every large picture on the site has a slot. Each slot shows a placeholder today: a picture the
// repository owner already made. The Image brief page (/image-brief) lists every slot with what the
// final picture should show, its size and a prompt, so the placeholders can be replaced one by one.
// To replace one: add the file to public/media/final/, set `final` below, and rebuild.

export type ImageSlot = {
  id: string;
  page: string;
  where: string;
  /** Path under media/ to the picture shown today. */
  placeholder: string;
  /** Path under media/ to the final picture, once it exists. */
  final?: string;
  /** What the final picture should show. */
  brief: string;
  /** Shape and smallest size. */
  size: string;
  /** A prompt for an image tool, under 25 words. */
  prompt: string;
  /** Alt text for the final picture. */
  alt: string;
  /** Alt text for the placeholder, while it is shown. */
  placeholderAlt: string;
  /** Where the subject should sit, so it survives a phone crop (CSS object-position). */
  focus?: string;
};

export const imageSlots: ImageSlot[] = [
  {
    id: "home-hero",
    page: "Home",
    where: "Full-screen opening scene, behind the headline",
    placeholder: "photos/toronto.jpg",
    brief: "A night city skyline at dusk with a warm, glowing light trail tracing a loop above it: the feeling of steady, expert work done overnight.",
    size: "16:9, at least 2400 by 1350 pixels, plus a 4:5 crop for phones. Keep the lower third dark for the headline",
    prompt: "Cinematic dusk skyline, warm glowing light trail looping overhead, deep crimson and amber tones, reflective water, dark lower third, film grain",
    alt: "A city skyline at dusk under a glowing loop of light",
    placeholderAlt: "The Toronto skyline at night under a fiery infinity loop, reflected in still water",
    focus: "72% 55%",
  },
  {
    id: "home-intern",
    page: "Home",
    where: "The smart intern scene, beside the analogy",
    placeholder: "photos/class.jpg",
    brief: "A friendly robot intern at a desk with a clear written brief in front of it, warm desk lamp light, calm and capable.",
    size: "3:2, at least 1800 by 1200 pixels",
    prompt: "Friendly robot intern at a wooden desk reading a one-page brief under a warm lamp, cinematic shallow depth of field, crimson accents",
    alt: "A robot intern at a desk, reading a clear brief under a warm lamp",
    placeholderAlt: "A cartoon robot at a desk in front of a screen of smiling robot faces",
    focus: "40% 50%",
  },
  {
    id: "home-standard",
    page: "Home",
    where: "Background of the quality section",
    placeholder: "photos/fog.jpg",
    brief: "A single person walking a clear path through fog toward a lit building: clarity and a standard you can follow.",
    size: "16:9, at least 2400 by 1350 pixels",
    prompt: "Lone figure walking a clear stone path through morning fog toward a softly lit building, cinematic, muted crimson and ivory palette",
    alt: "A person walking a clear path through fog toward a lit building",
    placeholderAlt: "A lone figure walking along a flooded path toward a stilt house in the fog",
    focus: "60% 50%",
  },
  {
    id: "tool-artifact-studio",
    page: "Artifact Studio",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    placeholder: "photos/bulb.jpg",
    brief: "Plain notes on a desk turning into a beautifully designed page that glows on a laptop screen.",
    size: "16:9, at least 2400 by 1350 pixels, plus a 4:5 crop for phones",
    prompt: "Handwritten notes on a dark desk transforming into a glowing designed report on a laptop, light particles, cinematic, crimson and amber",
    alt: "Handwritten notes turning into a designed page on a laptop screen",
    placeholderAlt: "A light bulb bursting with splashes of bright paint",
  },
  {
    id: "tool-document-to-action-brief",
    page: "Document to action brief",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    placeholder: "photos/fog.jpg",
    brief: "A thick contract on a desk with one short sticky note on top listing three actions and a date, lit by a single lamp.",
    size: "16:9, at least 2400 by 1350 pixels, plus a 4:5 crop for phones",
    prompt: "Thick printed contract on a dark desk, one bright sticky note on top with three ticks and a date, single lamp, cinematic",
    alt: "A thick contract with a sticky note listing three actions and a date",
    placeholderAlt: "A misty landscape with a stilt house reflected in the water",
    focus: "35% 50%",
  },
  {
    id: "tool-learnings-database",
    page: "Learnings database",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    placeholder: "photos/sunset.jpg",
    brief: "An open ship's logbook on a chart table at golden hour, a calm harbour through the window.",
    size: "16:9, at least 2400 by 1350 pixels, plus a 4:5 crop for phones",
    prompt: "Open leather ship's logbook on a chart table, golden hour light, calm harbour through a porthole, cinematic, warm amber tones",
    alt: "An open ship's logbook on a chart table at golden hour",
    placeholderAlt: "A sunset over the water beside a rocky shore, with a dog looking out",
    focus: "50% 35%",
  },
  {
    id: "tool-agentic-process",
    page: "Agentic Process",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    placeholder: "photos/puzzle.jpg",
    brief: "An engineer and a person side by side at a workbench, assembling a small machine from labelled parts, warm workshop light.",
    size: "16:9, at least 2400 by 1350 pixels, plus a 4:5 crop for phones",
    prompt: "Two people at a warm workshop bench assembling a small labelled machine together, blueprint behind them, cinematic, crimson and brass tones",
    alt: "Two people at a workbench assembling a small machine from labelled parts",
    placeholderAlt: "Bright jigsaw puzzle pieces piled together",
  },
  {
    id: "tool-rare-find",
    page: "Rare Find",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    placeholder: "photos/flower.jpg",
    brief: "A single rare gem glowing among plain pebbles, caught in a spotlight: the rare right answer.",
    size: "16:9, at least 2400 by 1350 pixels, plus a 4:5 crop for phones",
    prompt: "One glowing violet gem among plain grey pebbles under a single spotlight, dark stage, cinematic macro, crimson rim light",
    alt: "A glowing gem among plain pebbles in a spotlight",
    placeholderAlt: "A violet flower covered in raindrops",
  },
  {
    id: "about-portrait",
    page: "About Bradley",
    where: "The portrait in the opening scene",
    placeholder: "shared/bradley-ross.jpg",
    brief: "A professional portrait of Bradley Ross, shoulders up, warm key light from one side, dark background. The current photo is 360 pixels wide, too small for a full-screen scene.",
    size: "4:5, at least 1600 by 2000 pixels",
    prompt: "A real photograph, not generated: professional portrait, shoulders up, warm side light, dark crimson-black background, relaxed and confident",
    alt: "Bradley Ross",
    placeholderAlt: "Bradley Ross",
    focus: "50% 30%",
  },
  {
    id: "about-stage",
    page: "About Bradley",
    where: "Background of the research to instruction section",
    placeholder: "photos/toronto.jpg",
    brief: "Bradley teaching a room of professionals, a screen behind him: a real photo from a workshop or keynote.",
    size: "16:9, at least 2400 by 1350 pixels",
    prompt: "A real photograph, not generated: Bradley presenting to a room of professionals, slides behind him, warm stage light",
    alt: "Bradley Ross teaching a room of professionals",
    placeholderAlt: "The Toronto skyline at night under a fiery infinity loop",
    focus: "50% 60%",
  },
];

export const slot = (id: string) => {
  const s = imageSlots.find((x) => x.id === id);
  if (!s) throw new Error(`No image slot "${id}"`);
  return { src: s.final ?? s.placeholder, alt: s.final ? s.alt : s.placeholderAlt, focus: s.focus ?? "50% 50%", isPlaceholder: !s.final };
};
