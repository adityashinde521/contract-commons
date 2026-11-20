# Contract Commons

The design system for Contract Commons, an Ethereum-focused smart contracts course for computer science, business informatics and law students. It was built from the three approved web mockups (landing page, learner dashboard, lesson/lab page). Light theme only for now.

## Voice and content

- Plain English, short sentences, active voice. Write for a law student who has never coded and a CS student who has never read a statute, at the same time.
- Every lesson follows the same five steps: **Problem → Concept → Build → Apply → Ship**. Number them only because the order matters.
- Every build step has an **Expected:** result. Tell people what they should see, not only what to click.
- Name real tools by their real names (Remix, MetaMask, Safe, Tenderly). Never invent figures; sample data is labelled "Sample data".
- Safety is part of the voice: testnet only, no real money, never share a recovery phrase.

## Colour

- **Ground and surfaces.** `ground` behind everything, `surface` for cards, `surface-muted` for blocks inside a card. Borders are `line`; secondary buttons use `line-strong`.
- **Brand.** `brand-900` is the identity colour: hero bands, primary buttons, the logo tile. On `brand-900`, text is `on-brand` / `on-brand-muted` and the main call to action is `brand-300` with `brand-ink` text. `brand-700` is for links and eyebrows on light grounds; `brand-500` for progress and done states.
- **Disciplines.** Each discipline has a tint and a strong colour: computer science `cs-100`/`cs-600`, business informatics `bi-100`/`bi-600`, law `law-100`/`law-600` (`law-50` for legal text panels). Use them for chips, icon tiles and the three lenses (technology, business, law) in the Apply step. Never use them for state.
- **State.** Done = `brand-50`/`brand-500`. Current = `pending-100`/`pending-500`/`pending-700`. Warning = `warn-100`/`warn-700`. Error and revert = `danger-100`/`danger-700`.
- **Code.** `code-bg`, `code-ink`, `code-comment`, `code-string`.
- All text pairs meet 4.5:1. `muted-2` is the lightest text colour allowed on `surface` and `ground`.

## Type

- **Plus Jakarta Sans** (Google Fonts) for everything, weights 400–800. Headings are 800 with slight negative tracking.
- **JetBrains Mono** for code, addresses, hashes, transaction IDs and step numbers in lesson headers.
- Scale: `display-xl` 56, `display` 40, `h1` 34, `h2` 24, `h3` 19, `body-lg` 17, `body` 16, `small` 14, `label` 13 (uppercase, 0.08em), `code` 13.

## Shape and space

- Radii grow with the size of the object: `radius-md` 12 for buttons and inputs, `radius-lg` 18 for grid cards, `radius-xl` 22 for lesson sections, `radius-2xl` 28 for heroes. Chips are `radius-pill`.
- Spacing steps 4 · 8 · 12 · 16 · 20 · 24 · 32 · 48 · 88. Card padding `space-6`; landing sections are `space-22` apart.
- Cards are flat: a `line` border, no shadow. Shadows (`shadow-float`, `shadow-toast`) are only for product cards and toasts that float on `brand-900`.
- Touch targets are at least 44px high.

## Iconography

- Simple stroke icons, 2px stroke, round caps, drawn at 18–22px, inside an icon tile (`radius-md`) tinted by discipline. No emoji. No logo: the brand mark is a document glyph in `brand-100` on a `brand-900` tile.

## Components

Button, Chip, Card, Stat tile, Progress, Lesson steps, Callout, Discipline tabs, State stepper and Code block. Their styles live in `components/bundle.css` as `cc-*` classes; the courseware website uses the same file.
