# Handoff: apply the calm-editorial redesign + EN/TH UI to this site

Goal: **clarity-first, calm/refined editorial reading**, **auto light/dark**, and a
**two-locale (EN/TH) UI**. Apply the aesthetic to THIS repo's existing structure —
do not rip out the data model or routing.

## Read first
- `../.impeccable.md` (repo root) — design context + non-negotiables. **Source of truth.**
- `web/.design-ref/` — a reference implementation of the exact aesthetic to match:
  `Base.astro`, `Home.astro`, `i18n.ts`, `topics.ts`, `index.astro`, `[...slug].astro`,
  `th-index.astro`. **Copy the look/typography/tokens/i18n approach from these**, but
  adapt to this repo's pages, route, and helpers. They are reference only — delete
  `web/.design-ref/` when done.

## Preserve (do NOT change)
- Route structure `web/src/pages/report/[date]/[topic]/[lang].astro` and the home
  `index.astro` grouping (date → topic → {en,th}).
- `web/src/lib/format.ts` (`prettyTopic`, `prettyDate`, `sentimentEmoji`) and its topic
  titles (`XR / VR / AR`, `Web & Frontend`, etc.) — keep these, do not swap for the
  reference's `topics.ts` map.
- `web/src/content.config.ts` schema/loader unless a change is strictly required.

## Implement
1. **Design system** (from `.impeccable.md` + `.design-ref`): Fraunces (display) +
   Newsreader (body) + Hanken Grotesk (UI) + Noto Serif/Sans Thai; `light-dark()` color
   tokens (warm paper / warm near-black, one restrained accent); fluid `clamp()` scale;
   62–68ch reading measure. Replace the current visual system in `Base.astro`,
   `index.astro`, and `report/[date]/[topic]/[lang].astro`.
2. **Editorial home** (not a card grid): masthead + lead (highest-salience) story +
   numbered topic list + a short legend that teaches `salience`/`confidence`. Adapt the
   reference `Home.astro` to this repo's `byDate`/`Pair` data.
3. **EN/TH UI i18n**: add `web/src/lib/i18n.ts` (port from `.design-ref/i18n.ts`) and a
   site-level language switch. The home should offer both locales (e.g. `/` EN + `/th/`
   TH, or your cleanest equivalent that fits this routing). Localize all chrome:
   masthead, nav, legend, footer, and the report page's "back"/meta labels. Keep report
   *body* rendering as-is (bodies are already bilingual via the `[lang]` route).
4. **A11y/motion**: real contrast in both schemes, visible focus, `prefers-reduced-motion`
   honored, at most one tasteful staggered load reveal (transform/opacity only).

## Constraints
- AI-slop DON'Ts from `.impeccable.md`: no card-grid sameness, glassmorphism, neon-on-dark,
  gradient text, centered-everything, monospace-as-"technical".
- Thai must read well (Noto Serif Thai + comfortable line-height). Test a Thai report page.
- Static only; no client framework. `<style>` blocks are fine.

## Acceptance
1. `npm run build` passes with no schema/type errors.
2. `npm run dev` → home + a topic report (EN and TH) render correctly in both light and
   dark OS schemes; the `/report/[date]/[topic]/[lang]` route still works.
3. UI chrome is fully localized in both EN and TH; language switch works.
4. `web/.design-ref/` deleted. Would NOT pass the "an AI made this" test.
