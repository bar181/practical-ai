// Every large picture on the site has a slot: the page it is on, where, the picture and its alt text.
// The pictures are the owner's own. To change one, put the file in public/media/ (or the source
// project's _build/img/), point `src` at it, describe it in `alt`, and rebuild.

export type ImageSlot = {
  id: string;
  page: string;
  where: string;
  /** Path under media/ to the picture. */
  src: string;
  /** What the picture shows, for anyone who cannot see it. */
  alt: string;
  /** Where the subject should sit, so it survives a phone crop (CSS object-position). */
  focus?: string;
};

export const imageSlots: ImageSlot[] = [
  {
    id: "home-intern",
    page: "Home",
    where: "The smart intern scene, beside the analogy",
    src: "photos/class.jpg",
    alt: "A cartoon robot at a desk in front of a screen of smiling robot faces",
    focus: "40% 50%",
  },
  {
    id: "home-hero",
    page: "Home",
    where: "Full-screen opening scene, behind the headline",
    src: "photos/toronto.jpg",
    alt: "The Toronto skyline at night under a fiery infinity loop, reflected in still water",
    focus: "72% 55%",
  },
  {
    id: "home-standard",
    page: "Home",
    where: "Background of the quality section",
    src: "photos/fog.jpg",
    alt: "A lone figure walking along a flooded path toward a stilt house in the fog",
    focus: "60% 50%",
  },
  {
    id: "home-start",
    page: "Home",
    where: "Behind the starter prompt, near the end of the home page",
    src: "photos/cheetah.jpg",
    alt: "A cheetah",
  },
  {
    id: "tool-artifact-studio",
    page: "Artifact Studio",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/bulb.jpg",
    alt: "A light bulb bursting with splashes of bright paint",
  },
  {
    id: "tool-document-to-action-brief",
    page: "Document to action brief",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/fog.jpg",
    alt: "A misty landscape with a stilt house reflected in the water",
    focus: "35% 50%",
  },
  {
    id: "tool-learnings-database",
    page: "Learnings database",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/sunset.jpg",
    alt: "A sunset over the water beside a rocky shore, with a dog looking out",
    focus: "50% 35%",
  },
  {
    id: "tool-website-audit",
    page: "Website audit",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/home.jpg",
    alt: "A painted house and garden with a family on the path",
  },
  {
    id: "tool-practical-ai-guide",
    page: "Practical AI guide",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/bulb.jpg",
    alt: "A light bulb bursting with splashes of bright paint",
  },
  {
    id: "tool-agentic-process",
    page: "Agentic Process",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/puzzle.jpg",
    alt: "Bright jigsaw puzzle pieces piled together",
  },
  {
    id: "tool-rare-find",
    page: "Rare Find",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/flower.jpg",
    alt: "A violet flower covered in raindrops",
  },
  {
    id: "tool-web-sections",
    page: "Web Sections",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/home.jpg",
    alt: "A painted house and garden with a family on the path",
    focus: "50% 45%",
  },
  {
    id: "tool-tone-studio",
    page: "Tone Studio",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/dancers.jpg",
    alt: "A painting of two dancers in swirling coloured robes",
    focus: "50% 40%",
  },
  {
    id: "tool-meeting-notes-to-actions",
    page: "Meeting notes to actions",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/lake.jpg",
    alt: "A calm lake under a grey sky, with a bare tree on the shore",
  },
  {
    id: "tool-site-studio",
    page: "Site Studio",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/home.jpg",
    alt: "A painted house and garden with a family on the path",
  },
  {
    id: "tool-write-in-my-voice",
    page: "Write and edit in my voice",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/cat.jpg",
    alt: "A wide-eyed tabby cat with its mouth open, as if mid-meow",
    focus: "50% 40%",
  },
  {
    id: "tool-research-brief",
    page: "Research brief with checked sources",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/bulb.jpg",
    alt: "A light bulb bursting with splashes of bright paint",
    focus: "50% 45%",
  },
  {
    id: "tool-decision-support",
    page: "Decision support",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/cheetah.jpg",
    alt: "A cheetah",
  },
  {
    id: "tool-rubric-reviewer",
    page: "Rubric reviewer",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/class.jpg",
    alt: "A cartoon robot at a desk in front of a screen of smiling robot faces",
  },
  {
    id: "tool-weekly-status-update",
    page: "Weekly status update",
    where: "Full-screen opening scene of the tool page, and its card on the home page",
    src: "photos/dog.jpg",
    alt: "A small dog at a laptop keyboard in warm light",
  },
  {
    id: "who-artifact-studio",
    page: "Artifact Studio",
    where: "The Who it is for scene on the tool page",
    src: "photos/portrait.jpg",
    alt: "A watercolour portrait of a woman with curly hair",
    focus: "50% 30%",
  },
  {
    id: "who-document-to-action-brief",
    page: "Document to action brief",
    where: "The Who it is for scene on the tool page",
    src: "photos/home.jpg",
    alt: "A painted house and garden with a family on the path",
    focus: "50% 12%",
  },
  {
    id: "who-learnings-database",
    page: "Learnings database",
    where: "The Who it is for scene on the tool page",
    src: "photos/lake.jpg",
    alt: "A calm lake under a grey sky, with a bare tree on the shore",
    focus: "50% 50%",
  },
  {
    id: "who-website-audit",
    page: "Website audit",
    where: "The Who it is for scene on the tool page",
    src: "photos/puzzle.jpg",
    alt: "Bright jigsaw puzzle pieces piled together",
  },
  {
    id: "who-practical-ai-guide",
    page: "Practical AI guide",
    where: "The Who it is for scene on the tool page",
    src: "photos/sunset.jpg",
    alt: "A sunset over the water beside a rocky shore, with a dog looking out",
  },
  {
    id: "who-agentic-process",
    page: "Agentic Process",
    where: "The Who it is for scene on the tool page",
    src: "photos/dancers.jpg",
    alt: "A painting of two dancers in swirling coloured robes",
    focus: "50% 40%",
  },
  {
    id: "who-rare-find",
    page: "Rare Find",
    where: "The Who it is for scene on the tool page",
    src: "photos/heart.jpg",
    alt: "A watercolour heart",
    focus: "50% 45%",
  },
  {
    id: "who-web-sections",
    page: "Web Sections",
    where: "The Who it is for scene on the tool page",
    src: "photos/dog.jpg",
    alt: "A small dog at a laptop keyboard in warm light",
    focus: "60% 40%",
  },
  {
    id: "who-tone-studio",
    page: "Tone Studio",
    where: "The Who it is for scene on the tool page",
    src: "photos/flower.jpg",
    alt: "A violet flower covered in raindrops",
  },
  {
    id: "who-meeting-notes-to-actions",
    page: "Meeting notes to actions",
    where: "The Who it is for scene on the tool page",
    src: "photos/puppy.jpg",
    alt: "A puppy in a tweed jacket and tie",
    focus: "50% 35%",
  },
  {
    id: "who-site-studio",
    page: "Site Studio",
    where: "The Who it is for scene on the tool page",
    src: "photos/bulb.jpg",
    alt: "A light bulb bursting with splashes of bright paint",
  },
  {
    id: "who-write-in-my-voice",
    page: "Write and edit in my voice",
    where: "The Who it is for scene on the tool page",
    src: "photos/sunset.jpg",
    alt: "A sunset over the water beside a rocky shore, with a dog looking out",
  },
  {
    id: "who-research-brief",
    page: "Research brief with checked sources",
    where: "The Who it is for scene on the tool page",
    src: "photos/puzzle.jpg",
    alt: "Bright jigsaw puzzle pieces piled together",
  },
  {
    id: "who-decision-support",
    page: "Decision support",
    where: "The Who it is for scene on the tool page",
    src: "photos/fog.jpg",
    alt: "A lone figure walking along a flooded path toward a stilt house in the fog",
  },
  {
    id: "who-rubric-reviewer",
    page: "Rubric reviewer",
    where: "The Who it is for scene on the tool page",
    src: "photos/puppy.jpg",
    alt: "A puppy in a tweed jacket and tie",
  },
  {
    id: "who-weekly-status-update",
    page: "Weekly status update",
    where: "The Who it is for scene on the tool page",
    src: "photos/heart.jpg",
    alt: "A watercolour heart",
  },
  {
    id: "about-portrait",
    page: "About Bradley",
    where: "The portrait in the opening scene",
    src: "shared/bradley-ross.jpg",
    alt: "Bradley Ross",
    focus: "50% 30%",
  },
  {
    id: "about-stage",
    page: "About Bradley",
    where: "Background of the research to instruction section",
    src: "photos/toronto.jpg",
    alt: "The Toronto skyline at night under a fiery infinity loop",
    focus: "50% 60%",
  },
  {
    id: "practical-hero",
    page: "Practical AI",
    where: "Full-screen opening scene of the Practical AI page",
    src: "photos/puzzle.jpg",
    alt: "Brightly coloured jigsaw pieces scattered across a dark surface",
    focus: "50% 50%",
  },
  {
    id: "work-hero",
    page: "Work with me",
    where: "Full-screen opening scene of the Work with me page",
    src: "photos/sunset.jpg",
    alt: "Sunset over a calm lake, a rocky shore in the foreground",
    focus: "50% 35%",
  },
];

export const slot = (id: string) => {
  const s = imageSlots.find((x) => x.id === id);
  if (!s) throw new Error(`No image slot "${id}"`);
  // Photos have light WebP copies (scripts/make_webp.py): full width, and 800 pixels for phones.
  const m = s.src.match(/^photos\/(.+)\.jpg$/);
  const srcSet = m ? `photos-webp/${m[1]}-800.webp 800w, photos-webp/${m[1]}.webp 1600w` : undefined;
  return { src: m ? `photos-webp/${m[1]}.webp` : s.src, srcSet, alt: s.alt, focus: s.focus ?? "50% 50%" };
};
