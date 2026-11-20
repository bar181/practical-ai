// Where the site lives. Change these two lines for your own site, or set SITE_BASE and SITE_URL
// when you build. A project site on GitHub Pages: "/repository-name/". Your own domain: "/".
export const siteBase = process.env.SITE_BASE ?? "/practical-ai/";
export const siteUrl = (process.env.SITE_URL ?? "https://bar181.github.io/practical-ai").replace(/\/$/, "");
