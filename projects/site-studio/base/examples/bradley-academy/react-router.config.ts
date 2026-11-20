import type { Config } from "@react-router/dev/config";
import { toolSlugs } from "./app/content/slugs";

// Every page is rendered to plain HTML at build time, so the site needs no server.
// SITE_BASE is the address path: "/practical-ai/" on GitHub Pages today, "/" on a custom domain later.
export default {
  ssr: false,
  basename: process.env.SITE_BASE ?? "/practical-ai/",
  prerender: ["/", "/about", "/image-brief", ...toolSlugs.map((slug) => `/tools/${slug}`)],
} satisfies Config;
