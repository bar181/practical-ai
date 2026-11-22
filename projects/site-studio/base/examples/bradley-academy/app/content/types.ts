import type { ToolSlug } from "./slugs";

/** One level of a tool: who it is for, their user story, and what the level does. */
export type Level = {
  level: 1 | 2 | 3;
  name: string;
  coreUser: string;
  story: string;
  does: string;
  setup: string;
  built: boolean;
};

/** A picture from the repository. `src` is relative to the site's media folder. */
export type Picture = { src: string; alt: string; caption?: string; width?: number; height?: number };

export type Block =
  | { kind: "text"; heading?: string; paras: string[] }
  | { kind: "picture"; picture: Picture; size?: "phone" | "wide" }
  | { kind: "gallery"; pictures: Picture[]; size?: "phone" | "wide" }
  | { kind: "frame"; src: string; title: string; caption: string; height: number }
  | { kind: "table"; caption: string; head: string[]; rows: string[][] }
  | { kind: "steps"; heading?: string; items: { title: string; text: string }[] }
  | { kind: "links"; heading: string; items: { href: string; label: string; note?: string }[] };

/** A tab after "About" on a tool page: real examples of the tool. */
export type Tab = { id: string; label: string; intro: string; blocks: Block[] };

export type Tool = {
  slug: ToolSlug;
  name: string;
  /** Path under media/ to the tool's square icon, cut from its tile by scripts/sync.mjs. */
  icon: string;
  /** One line from the visitor's side. */
  promise: string;
  sub: string;
  /** Plain words for the home page card. */
  cardLine: string;
  coreIdea: string;
  analogy: string;
  whatItIs: string[];
  benefits: { title: string; text: string }[];
  design: { title: string; text: string }[];
  coreUser: string;
  levels: Level[];
  tryIt: { intro: string; after: string; promptKey: ToolSlug; primaryLabel: string; play?: { href: string; label: string }[] };
  notDo: string[];
  status: { date: string; label: string; text: string };
  readme: string;
  explainer?: string;
  /** For a tool that is one of a set: a short note and links to the others. */
  set?: { text: string; links: { href: string; label: string }[] };
  /** Show, don't tell: two or three picture cards in the About, right after the core idea. */
  show?: { heading: string; cards: { picture: Picture; title: string; text: string }[] };
  /** A linked list in the About, such as Tone Studio's seven tones, each linking to its example. */
  list?: { heading: string; intro?: string; items: { title: string; text: string; href: string }[] };
  tabs: Tab[];
};
