// Addresses on this site. The base path ("/practical-ai/" today, "/" on a custom domain) is added here,
// so content files can write "/rare-find/" and the link still works wherever the site is hosted.
const BASE = import.meta.env.BASE_URL; // always ends with "/"

/** A picture in public/media. */
export const media = (src: string) => `${BASE}media/${src}`;

/** Routes the React app renders. Everything else under "/" is a published page outside the app. */
export const isAppRoute = (href: string) => href === "/" || ["/about", "/research", "/tools", "/privacy"].some((p) => href === p || href.startsWith(`${p}#`)) || href.startsWith("/tools/");

/** A full address for a page outside the app, or an outside link left as it is. */
export const pageHref = (href: string) => (href.startsWith("/") ? `${BASE}${href.slice(1)}` : href);
