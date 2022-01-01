import React from "react";
import { Outlet } from "remix";
import type { LinksFunction } from "remix";
import jokesStyle from "../styles/jokes.css";

export const links: LinksFunction = () => [
  { rel: "stylesheet", href: jokesStyle },
];

export default function JokesRute() {
  return (
    <div>
      <h1>Jokes!</h1>
      <main>
        <Outlet />
      </main>
    </div>
  );
}
