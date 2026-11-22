// Where the site lives. Change these lines for your own site, or set the environment variables when
// you build. A project site on GitHub Pages: "/repository-name/". Your own domain: "/".
export const siteBase = process.env.SITE_BASE ?? "/practical-ai/";
export const siteUrl = (process.env.SITE_URL ?? "https://bar181.github.io/practical-ai").replace(/\/$/, "");

// Off until set. SITE_GA_ID is a Google Analytics 4 measurement ID (G-...): the site then asks each
// visitor first and loads analytics only after a yes. SITE_GSC is the Search Console HTML-tag token.
export const analyticsId = process.env.SITE_GA_ID ?? "";
export const searchConsoleToken = process.env.SITE_GSC ?? "";
