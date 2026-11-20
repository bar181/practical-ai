import { reactRouter } from "@react-router/dev/vite";
import { defineConfig } from "vite";
import { siteBase } from "./site.config";

export default defineConfig({
  base: siteBase,
  plugins: [reactRouter()],
});
