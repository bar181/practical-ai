# Bradley Academy: the site

The Practical AI tools, for people who will never open GitHub. A React site with every page
pre-rendered, published by GitHub Pages at https://bar181.github.io/practical-ai/.

| Command | What it does |
| --- | --- |
| `npm install` | Installs React, React Router, Vite and the two fonts |
| `npm run dev` | Runs the site at http://localhost:5173/practical-ai/ |
| `npm run build` | Copies the pictures and prompts from the repository, then pre-renders every page into `build/client/` |
| `npm run typecheck` | Checks the TypeScript |

The words are in `app/content/`. The rules for changing them are in the project's
[AGENTS.md](../../../AGENTS.md). Needs Node 22.22 or newer.
