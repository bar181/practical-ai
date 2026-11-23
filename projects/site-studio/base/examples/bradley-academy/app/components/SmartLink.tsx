import type { ReactNode } from "react";
import { Link } from "react-router";
import { isAppRoute, pageHref } from "../lib/paths";

/** One link component for app routes, published pages on this site, and outside sites. */
export function SmartLink({ href, children, className, "aria-label": ariaLabel }: { href: string; children: ReactNode; className?: string; "aria-label"?: string }) {
  if (isAppRoute(href)) return <Link to={href} className={className} aria-label={ariaLabel}>{children}</Link>;
  const outside = /^https?:/.test(href);
  return (
    <a href={pageHref(href)} className={className} aria-label={ariaLabel} {...(outside ? { rel: "noopener" } : {})}>
      {children}
    </a>
  );
}
