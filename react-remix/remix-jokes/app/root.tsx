import React from "react";
import { Links, LiveReload, Outlet } from "remix";
import type { LinksFunction } from "remix";

import globalCss from "../app/styles/global.css";
import globalMediumCss from "../app/styles/global-medium.css";
import globalLargeCss from "../app/styles/global-large.css";

export const links: LinksFunction = () => [
  { rel: "stylesheet", href: globalCss },
  {
    rel: "stylesheet",
    href: globalMediumCss,
    media: "screen and (min-width: 640px)",
  },
  {
    rel: "stylesheet",
    href: globalLargeCss,
    media: "screen and (min-width: 1024px)",
  },
];

export default function App() {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <Links />
        <title>Remix: So great, it's funny!</title>
      </head>
      <body>
        <Outlet />
        {process.env.NODE_ENV === "development" ? <LiveReload /> : null}
      </body>
    </html>
  );
}
