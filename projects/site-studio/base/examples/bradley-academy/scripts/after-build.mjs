// Runs after the build: a 404 page for GitHub Pages, a sitemap and robots.txt.
import { copyFileSync, cpSync, existsSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { toolSlugs } from "../app/content/slugs.ts";
import { siteBase, siteUrl } from "../site.config.ts";

const client = join(dirname(fileURLToPath(import.meta.url)), "..", "build", "client");
// With a base path such as "/practical-ai/", React Router writes the pre-rendered pages into a folder of
// that name and the app shell into index.html. The published folder is already served at the base path,
// so move the pages up, and keep the shell as 404.html: GitHub Pages serves it for any unknown address,
// and the app then shows its not-found page.
const base = siteBase.replace(/^\/|\/$/g, "");
const nested = base ? join(client, base) : "";
if (nested && existsSync(nested)) {
  copyFileSync(join(client, "index.html"), join(client, "404.html"));
  cpSync(nested, client, { recursive: true });
  rmSync(nested, { recursive: true });
} else if (existsSync(join(client, "__spa-fallback.html"))) {
  copyFileSync(join(client, "__spa-fallback.html"), join(client, "404.html"));
}

const paths = ["/", "/research/", "/tools/", "/about/", "/privacy/", ...toolSlugs.map((s) => `/tools/${s}/`)];
writeFileSync(
  join(client, "sitemap.xml"),
  `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${paths
    .map((p) => `  <url><loc>${siteUrl}${p}</loc></url>`)
    .join("\n")}\n</urlset>\n`,
);
writeFileSync(join(client, "robots.txt"), `User-agent: *\nAllow: /\nSitemap: ${siteUrl}/sitemap.xml\n`);
console.log(`after-build: 404.html, sitemap.xml with ${paths.length} pages, robots.txt`);
