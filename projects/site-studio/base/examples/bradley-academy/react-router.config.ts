import type { Config } from "@react-router/dev/config";
import { toolSlugs } from "./app/content/slugs";
import { siteBase } from "./site.config";

// Every page is rendered to plain HTML at build time, so the site needs no server.
// The address path is set in site.config.ts.
export default {
  ssr: false,
  basename: siteBase,
  prerender: ["/", "/about", "/image-brief", ...toolSlugs.map((slug) => `/tools/${slug}`)],
} satisfies Config;
