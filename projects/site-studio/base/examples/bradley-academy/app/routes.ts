import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
  index("routes/home.tsx"),
  route("tools/:slug", "routes/tool.tsx"),
  route("about", "routes/about.tsx"),
  route("image-brief", "routes/image-brief.tsx"),
  route("*", "routes/not-found.tsx"),
] satisfies RouteConfig;
