import type { ReactNode } from "react";
import { Link } from "react-router";
import { isAppRoute, pageHref } from "../lib/paths";

/** One link component for app routes, published pages on this site, and outside sites. */
export function SmartLink({ href, children, className }: { href: string; children: ReactNode; className?: string }) {
  if (isAppRoute(href)) return <Link to={href} className={className}>{children}</Link>;
  const outside = /^https?:/.test(href);
  return (
    <a href={pageHref(href)} className={className} {...(outside ? { rel: "noopener" } : {})}>
      {children}
    </a>
  );
}
