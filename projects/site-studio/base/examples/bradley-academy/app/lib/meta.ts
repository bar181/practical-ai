import { site } from "../content/site";

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
