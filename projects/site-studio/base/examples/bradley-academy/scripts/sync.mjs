// Runs before every build. Copies the pictures and the try-it prompts out of the repository,
// so the site always shows what the project READMEs say. Its output is not committed.
import { cpSync, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const site = join(here, "..");
const repo = join(site, "..", "..", "..", "..", "..");
const projects = [
  "artifact-studio", "agentic-process", "document-to-action-brief", "learnings-database", "rare-find",
  "tone-studio", "web-sections", "meeting-notes-to-actions", "write-in-my-voice", "site-studio",
  "practical-ai-guide",
];

// 1. Pictures: each project's _build/img, and the shared images
const media = join(site, "public", "media");
rmSync(media, { recursive: true, force: true });
// Some projects have no pictures yet; they are skipped.
for (const p of projects) {
  const img = join(repo, "projects", p, "_build", "img");
  if (existsSync(img)) cpSync(img, join(media, p), { recursive: true });
}
cpSync(join(repo, "assets", "images"), join(media, "shared"), { recursive: true });
// Placeholder photographs, made by the repository owner, until the final images in app/content/images.ts arrive.
cpSync(join(repo, "projects", "artifact-studio", "_build", "photos"), join(media, "photos"), { recursive: true });
// Each tool's square icon is the top of its tile (the same square in every tile), with the words cropped away.
mkdirSync(join(media, "icons"), { recursive: true });
for (const p of projects) {
  const tile = readFileSync(join(repo, "assets", "images", "tiles", `${p}.svg`), "utf8");
  const icon = tile.replace(/viewBox="[^"]*"/, 'viewBox="110 34 120 120"').replace(/ role="img" aria-label="[^"]*"/, ' aria-hidden="true"');
  writeFileSync(join(media, "icons", `${p}.svg`), icon);
}

// 2. Prompts: the first code block under the try-it heading of each README
const headings = {
  "artifact-studio": /^## Try it now/m,
  "agentic-process": /^## Try it now/m,
  "document-to-action-brief": /^## Try it now/m,
  "learnings-database": /^## Get started: try it now/m,
  "rare-find": /^## Play in ChatGPT, or any chatbot/m,
  "tone-studio": /^## Try it now/m,
  "web-sections": /^## Try it now/m,
  "meeting-notes-to-actions": /^## Try it now/m,
  "write-in-my-voice": /^## Try it now/m,
  "site-studio": /^## Get started: try it now/m,
  "practical-ai-guide": /^## Get started: try it now/m,
  starter: /^## Start here/m,
};
const prompts = {};
for (const [key, heading] of Object.entries(headings)) {
  const file = key === "starter" ? join(repo, "README.md") : join(repo, "projects", key, "README.md");
  const text = readFileSync(file, "utf8");
  const at = text.search(heading);
  if (at < 0) throw new Error(`No try-it heading in ${file}`);
  const block = text.slice(at).match(/```[a-z]*\n([\s\S]*?)\n```/);
  if (!block) throw new Error(`No prompt under the try-it heading in ${file}`);
  prompts[key] = block[1];
}
const out = join(site, "app", "content", "generated");
mkdirSync(out, { recursive: true });
writeFileSync(join(out, "prompts.json"), JSON.stringify(prompts, null, 2));
console.log(`sync: pictures for ${projects.length} projects, ${Object.keys(prompts).length} prompts`);
