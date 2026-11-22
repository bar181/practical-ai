import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
  index("routes/home.tsx"),
  route("tools/:slug", "routes/tool.tsx"),
  route("research", "routes/research.tsx"),
  route("tools", "routes/practical-ai.tsx"),
  route("privacy", "routes/privacy.tsx"),
  route("about", "routes/about.tsx"),
  route("*", "routes/not-found.tsx"),
] satisfies RouteConfig;
