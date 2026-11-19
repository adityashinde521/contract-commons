# Contract Commons

An Ethereum-focused smart contracts course for computer science, business informatics and law
students. Learners build contracts in Remix and Foundry, use the graphical tools professionals use
(OpenZeppelin, thirdweb, Safe, Aragon, EAS, Tenderly, Phalcon, Dune, L2BEAT), and analyse every
contract from three sides: code, business process and law.

- 13 modules, 56 lessons and labs, every lesson in the same five steps: Problem → Concept → Build → Apply → Ship
- Quizzes on 54 units, a placement check and a 20-question final exam
- Learning paths: smart contract developer, legal-tech analyst, blockchain product analyst
- Progress, quiz scores and a lab log saved in the learner’s browser (no accounts, no server)
- Every lab runs on the Sepolia test network or reads public data. No real money is used.

## Use it offline

Run `npm install` and `npm run build` once. Then open `dist/index.html` in any browser by double-clicking it.
Everything (fonts, search, quizzes, progress) works from disk without internet or a web server.
Only the links to outside tools (Remix, Etherscan, Safe and so on) need a connection.

## Run it

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # static site in dist/
```

All links in the build are relative, so the `dist/` folder can be copied to any static host or sub-path as it is.

## Where things are

| Path | What |
|---|---|
| `src/content/lessons/*.md` | One file per lesson or lab. Frontmatter (title, module, kind, minutes, problem) plus `## Problem`, `## Concept`, `## Build` or `## Try it`, `## Apply`, `## Ship` sections in HTML. |
| `src/data/modules.json` | Module order, summaries, sources, and the lesson order inside each module |
| `src/data/quizzes.json` | Quiz questions per lesson (`q` question, `o` options, `a` index of the answer, `e` explanation) |
| `src/data/glossary.json`, `src/data/placement.json` | Glossary terms and the placement check |
| `src/content/pages/*.md` | About, setup and safety, teamwork, capstone, project formats, instructor notes |
| `src/styles/tokens.css`, `src/styles/components.css` | Design tokens and components from the Contract Commons design system |
| `src/styles/site.css` | Layout and lesson-content styles |
| `public/app.js` | Client script: progress, quizzes, lab log, search, dashboard, placement |
| `design/design-system/` | The design system (tokens, component guidelines and previews) as built in Claude Design |
| `design/mockups/` | The three approved mockups (landing, dashboard, lesson) |
| `docs/curriculum.md` | Module map and the university syllabi it was checked against |
| `tools/` | Scripts used to convert the earlier single-page course into lessons |

## Add or edit a lesson

1. Create `src/content/lessons/<slug>.md` with the frontmatter used by the other files.
2. Add `<slug>` to the right module’s `lessons` list in `src/data/modules.json`.
3. Optional: add questions under `<slug>` in `src/data/quizzes.json`.
4. Run `npm run build`. The build fails if frontmatter is missing or invalid.

## Status and checks

Facts about upgrades, regulation, incidents and tools were checked against public sources up to
November 2026. Hosted tools change their labels; test each tool lab before a semester. Legal notes
are teaching prompts for German and EU law, not legal advice.

Prepared by Aditya Shinde.
