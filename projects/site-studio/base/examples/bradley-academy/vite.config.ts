import { reactRouter } from "@react-router/dev/vite";
import { defineConfig } from "vite";
import { analyticsId, searchConsoleToken, siteBase, siteUrl, wisegeoUrl } from "./site.config";

export default defineConfig({
  base: siteBase,
  plugins: [reactRouter()],
  // Build-time settings the pages read (see site.config.ts).
  define: {
    __SITE_URL__: JSON.stringify(siteUrl),
    __GA_ID__: JSON.stringify(analyticsId),
    __GSC_TOKEN__: JSON.stringify(searchConsoleToken),
    __WISEGEO_URL__: JSON.stringify(wisegeoUrl),
  },
});
