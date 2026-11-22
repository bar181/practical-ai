import { site } from "../content/site";

/** Structured data (schema.org) about Bradley, for search engines and AI assistants. Facts from About. */
export const personJsonLd = {
  "script:ld+json": {
    "@context": "https://schema.org",
    "@type": "Person",
    name: "Bradley Ross",
    jobTitle: "Agentic Architect and Researcher",
    url: `${site.url}/`,
    image: `${site.url}/media/shared/bradley-ross.jpg`,
    sameAs: [site.linkedin, "https://github.com/bar181"],
    worksFor: { "@type": "Organization", name: "WiseGeo Inc." },
    alumniOf: { "@type": "CollegeOrUniversity", name: "Harvard University" },
    knowsAbout: ["Agentic AI", "Deterministic AI", "AISP", "AI education"],
  },
};

/** Title, description and link-preview tags for one page. */
export function pageMeta(title: string, description: string, path: string) {
  const url = `${site.url}${path}`;
  const image = `${site.url}${site.previewImage}`;
  return [
    { title },
    { name: "description", content: description },
    { tagName: "link", rel: "canonical", href: url },
    { property: "og:type", content: "website" },
    { property: "og:site_name", content: site.brand },
    { property: "og:title", content: title },
    { property: "og:description", content: description },
    { property: "og:url", content: url },
    { property: "og:image", content: image },
    { name: "twitter:card", content: "summary" },
  ];
}
