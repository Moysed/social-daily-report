# Social Daily Report — Redesign Spec ("The Front Page")

> Source of truth for the full-site visual reinvention. Direction chosen by Mond
> 2026-05-29: **The Front Page** (NYT / FT / Guardian editorial DNA) — full
> reinvent, whole site. This doc drives every redesign dispatch phase. Read it
> before touching any component.

---

## 0. Why this direction

Synthesized from competitive research across three lenses (digest products —
Axios/Espresso/Morning Brew; editorial homepages — NYT/FT/Guardian/Atlantic;
modern static patterns — Linear/Stripe/Vercel/Pagefind). The single most
consistent "this was NOT made by AI" signal is **ink + hairlines + one accent +
dramatic type-scale hierarchy** — emphasis built from *size and whitespace*, not
boxes, shadows, or color. That is "The Front Page."

The previous design leaned on shadowed/bordered tiles (`.lead-tile`, `.tile`
grid). The reinvent replaces tile-thinking with **typographic blocks divided by
a three-tier hairline system** and an **asymmetric column grid**.

---

## 1. Principles (non-negotiable)

1. **Hairlines, not cards.** No drop shadows. No filled card backgrounds. No
   rounded "tile" containers. Separation comes from ruled lines (3 weights) and
   whitespace. (NYT, FT)
2. **Asymmetry + a strong left edge.** A dominant lead that genuinely dominates;
   secondaries that genuinely shrink. Never a row of 3 equal cards. (NYT,
   Guardian)
3. **Dramatic type-scale contrast.** The lead headline is *much* bigger than
   everything else. Quiet, confident hierarchy. (Atlantic, FT)
4. **One accent, reserved.** Ember-rust appears ONLY for: lead section marker,
   active states (filter/TOC/calendar-selected), links, section-divider ticks,
   positive-sentiment pill, "new"/unread dot, drop cap, pull-quote mark. Never
   on headlines, never as a background fill. Everything else is ink-on-paper.
5. **Each typeface stays in its lane.** Cross-use is a bug:
   - **Fraunces** (serif display) → headlines only.
   - **Newsreader** (serif body) → body copy, deks.
   - **Space Grotesk** (grotesque sans) → kickers/eyebrows, topic labels, nav,
     UI, bylines, captions. Set uppercase + ~0.06em tracking + small for
     metadata.
   - **JetBrains Mono** → numerals & identifiers only: dates, reading time,
     source/post counts, salience figures, run IDs, RSS. Never prose.
6. **Color from data, not chrome.** With few/no real photos, visual variety
   comes from the type scale, the rules, and mono data-viz (salience
   sparklines) — not stock imagery or gradients.
7. **Teach the metrics.** salience/confidence/sentiment must be legible to a
   first-time reader (labels, not bare floats). Keep the existing "Activity /
   Evidence" friendly labels; add inline sparkline trend context.
8. **Bilingual parity.** EN measure 60–70ch; Thai measure shorter (~45–55ch),
   Noto Serif/Sans Thai, line-height ~1.86. Thai must never look like an
   afterthought.
9. **Calm motion only.** No parallax, no blur-in-on-scroll, no glassmorphism, no
   pulsing badges. Restrained: native view-transition fade, CSS scroll-progress
   bar. Everything behind `prefers-reduced-motion`.

### Hard NOs (update `.impeccable.md` to match)
card-grid sameness · glassmorphism / `backdrop-filter` blur · neon-on-dark ·
gradient text · centered-everything hero · multiple accent colors · green/red
sentiment (use amber/slate) · emoji in headlines · drop-shadows · infinite
scroll · body-sticky TOC.

---

## 2. The three-tier hairline system

This is the structural backbone. Define as tokens, use everywhere instead of
borders/boxes.

| Token | Weight | Color | Use |
|-------|--------|-------|-----|
| `--rule-major` | 3px solid (or 1px double) | `--ink` | Above each top-level section / masthead underline |
| `--rule-section` | 1px solid | `--line` | Between teasers in a section, column gutter rule |
| `--rule-faint` | 1px solid | `--hairline` | Inside a teaser, metadata separators |

Accent variant: `--rule-lead` = 3px solid `--accent` — used ONLY on the lead
block's top edge (keeps today's lead as the one ember moment up top).

Column gutter on the asymmetric grid is a vertical `--rule-section` (the `│` in
the mockups), not a gap alone.

---

## 3. Tokens (evolve, don't restart)

Keep the existing OKLCH palette and `light-dark()` system in `Base.astro` — it's
already warm-paper/graphite and good. Changes:

### 3.1 Type scale — widen the dynamic range
The current scale tops out modestly. The Front Page needs a bigger jump between
the lead headline and everything else. Adjust the top steps:

```
--step--1: clamp(0.8rem, 0.77rem + 0.15vw, 0.9rem);   /* meta / eyebrow */
--step-0:  clamp(1.05rem, 1rem + 0.25vw, 1.18rem);     /* body */
--step-1:  clamp(1.3rem, 1.18rem + 0.6vw, 1.7rem);     /* dek / secondary head */
--step-2:  clamp(1.7rem, 1.4rem + 1.3vw, 2.6rem);      /* tertiary head */
--step-3:  clamp(2.3rem, 1.8rem + 2.4vw, 4rem);        /* section / 2nd lead */
--step-lead: clamp(3rem, 2.1rem + 4.4vw, 6.4rem);      /* THE lead headline */
```
`--step-lead` is new and is the dramatic moment. Lead headline = Fraunces 650,
line-height 0.98, letter-spacing -0.01em, max-width ~16ch.

### 3.2 Measure tokens
```
--measure-prose: 66ch;   /* EN body */
--measure-prose-th: 52ch; /* :lang(th) override */
--measure-dek: 56ch;
```

### 3.3 Grid
```
--max: 78rem;            /* page max */
--grid-lead: minmax(0, 7fr) minmax(0, 5fr);  /* lead column : rail */
```
Mobile: single column, everything stacks, rules become horizontal.

### 3.4 Eyebrow recipe (use as a utility class `.eyebrow`)
```
font-family: var(--font-ui);
text-transform: uppercase;
letter-spacing: 0.06em;
font-size: var(--step--1);
font-weight: 600;
color: var(--soft-ink);   /* ember only when it's the lead/active */
```

---

## 4. Component specs + mockups

### 4.1 Site masthead (Base.astro `.site-bar`)

Editorial nameplate, not an app bar. Brand left in Fraunces; dated/utility right
in mono+sans. A `--rule-major` under it.

```
┌────────────────────────────────────────────────────────────────────┐
│ Social Daily Report                      Thu 29 May 2026 · ⌘K  EN|TH ☾│
╞══════════════════════════════════════════════════════════════════════╡  ← --rule-major
```
- Brand: Fraunces ~step-1, ink.
- Right cluster (Space Grotesk + mono date): live date (mono), ⌘K search trigger
  (new — see 4.6), locale switch EN|TH, theme toggle (keep existing SVGs).
- Sticky on scroll? No (editorial mastheads don't follow). The report page gets
  its own slim progress bar instead (4.5).

### 4.2 Homepage — "today" front page

The core reinvention. Replaces `.brief-masthead` + `.lead-tile` + `.tile-grid`.

```
TODAY · 29 MAY · 12 REPORTS · ~9 MIN TO SCAN ALL          3 new since you looked
══════════════════════════════════════════════════════════════════════════════  --rule-major
                                                    │
AI DEVTOOLS                          · 4 min  ↑      │  AI RESEARCH        · 3 min
                                                    │  ─────────────────────────  --rule-section
  Anthropic ships agentic            (lead          │  Smaller Fraunces headline
  build pipeline                      headline,     │  sits in the rail, step-3.
  ─ enormous Fraunces, step-lead     │              │  Newsreader dek, one line.
                                     │              │  · 840 posts · salience .71
  WHY IT MATTERS — one Newsreader    │              ├───────────────────────────  --rule-section
  sentence on the org payoff.        │              │  XR / VR / AR       · 2 min
                                     │              │  ─────────────────────────
  • bold lead-in. short clause.      │              │  Headline row, step-3.
  • bold lead-in. short clause.      │              │  Dek line, soft ink.
                                     │              │  · 410 posts · salience .64
  ▁▂▅▇█▇█  · 1.2k posts · 14 sources │              ├───────────────────────────
  Read report →            ● unread  │              │  WEB & FRONTEND    · 3 min
                                     │ ← gutter rule│  ... (rail continues, each
══════════════════════════════════════════════════╧═══  topic a hairline-separated row)
```

Anatomy:
- **Brief line** (top): mono+eyebrow. `TODAY · {date} · {n} REPORTS · ~{sum}
  MIN`. Right-aligned: the "X new since you looked" line (localStorage, Phase 3a
  already ships unread — extend to the count). This is Espresso "finishability".
- **Lead block** (left, ~7fr): `--rule-lead` (ember 3px) top edge. Eyebrow =
  topic label + `· {min} read` + trend glyph. Then `--step-lead` Fraunces
  headline (the dramatic moment). Then a `WHY IT MATTERS` eyebrow + one-sentence
  Newsreader dek. Then 2–3 TL;DR bullets with **bold lead-in clauses** (Axios).
  Then a meta foot: inline salience sparkline + `· {post_count} posts ·
  {sources} sources`, the Read CTA, and the unread dot. Thumbnail OPTIONAL and
  small — type leads, not image.
- **Rail** (right, ~5fr): the other 11 topics as **hairline-separated teaser
  rows**, NOT cards. Each row: eyebrow (topic + `· {min}`) → `--step-3` Fraunces
  headline link → one-line dek → mono meta (`· {posts} · salience {x}`). A
  `--rule-section` between rows. Rows shrink — no two look identically weighted;
  the top rail item may be slightly larger.
- The whole front page is one asymmetric grid with a vertical gutter rule.
- Mobile: lead first (full width), then rail rows stack below, all separated by
  horizontal `--rule-section`. No image-left/prose-right.

> Replaces the "3 equal tiles" feel entirely. The grid auto-fill tile system is
> removed.

### 4.3 Section grouping (optional, Phase 2)

12 topics is a lot for one flat rail. Group under 3–4 plain eyebrow headers
(TLDR.tech pattern), e.g. `AI & RESEARCH`, `WEB & XR`, `LOCAL / THAI TECH`,
`LEARNING`. Header = eyebrow style + a `--rule-major`. Mapping table lives in
`format.ts` next to `TOPIC_TITLES`. Keep it data-driven so new topics slot in.

### 4.4 Trending this week (Phase 3a shipped — restyle to Front Page)

Already computed in frontmatter (`trendingTopics`). Restyle from the current
list into a hairline-ruled rail block, placed after the front page / before the
calendar. Each row: rank (mono) · topic link (Fraunces step-2) · activity pill ·
`{daysAppeared} days` · tiny sparkline. `--rule-faint` between rows.

```
TRENDING THIS WEEK
──────────────────────────────────────────────  --rule-section
1  AI Devtools      ▁▂▅▇█▇█  high · 6 days
2  AI Research      ▃▄▃▅▆▅▇  high · 5 days
3  Multimodal AI    ▇▆▄▃▂▂▁  med  · 4 days
──────────────────────────────────────────────
```

### 4.5 Report reading page

Apply Atlantic/Stratechery reading craft. Current structure: nav breadcrumb →
hero (kicker, headline, TL;DR card, instruments grid, platforms, credit, share)
→ article → sticky share bar.

Redesign:
```
← Social Daily Report / AI Devtools
══════════════════════════════════════════════════════════  --rule-major

AI DEVTOOLS · 29 MAY 2026                          ← eyebrow (sans+mono)

Anthropic ships agentic build pipeline             ← Fraunces step-3..lead
────────────────────────────────────────────────  --rule-section
847 words · 6-min read · 14 sources · salience .82 ↑   EN | ไทย   ← metadata strip (mono)
────────────────────────────────────────────────  --rule-faint

┌─ KEY POINTS ─────────────────────────────┐      ← TL;DR promoted to a
│ • bold lead-in. ...                       │        hairline-ruled box (not filled)
│ • bold lead-in. ...                       │        atop the body
└───────────────────────────────────────────┘

WHY IT MATTERS — one-sentence org payoff (NDF DEV).  ← labeled eyebrow + dek

[D]rop-cap opens the body. Newsreader, 66ch    │ ON THIS PAGE        ← sticky rail TOC
measure, soft ink. Indented paragraphs for a   │ ─────────────
printed feel. Pull quotes set inline, larger,  │ › The news          ← active = ember
heavier, with an ember mark — no box.          │   Signals
                                               │   The numbers
## SIGNALS                                     │   Sources
...                                            │
## THE NUMBERS                                 │  (collapses to a top
salience .82 ↑  ▁▂▅▇█  · sentiment ◗ positive  │   block on mobile)
confidence .76  · 1.2k posts · 14 sources      │
## SOURCES                                     │
[1] superscript-chip citations → list          │
────────────────────────────────────────────────
prev edition ←  · 27 May · 29 May →   share: X · LINE · copy   ← prev/next + share
```

Key moves:
- **Metadata strip** (mono) directly under headline: word count · reading time ·
  sources · salience+trend · EN|ไทย toggle. One quiet line.
- **KEY POINTS box** = the existing TL;DR, promoted, hairline-ruled (not the
  current filled card). Axios "why it matters."
- **Labeled structure** inside the report (consistent every day): `WHY IT
  MATTERS` → `SIGNALS` → `THE NUMBERS` → `SOURCES`. These map to the report's
  markdown `##` sections + the instruments. Style headings as small-caps
  eyebrows. (Semaform/Axios) — NOTE: this depends on the Python report template
  emitting these sections; if not, render what exists and style headings — do
  NOT change the Python pipeline in a web phase.
- **Drop cap** (Fraunces, ember, 2–3 lines) opens the body. Inline pull quotes.
- **Side-rail sticky TOC** with active-section highlight (IntersectionObserver —
  not the Chrome-only CSS scrollspy). Collapses to a non-fixed top block on
  mobile. Replaces/upgrades the current TOC.
- **Reading-progress bar**: 2px ember, CSS `animation-timeline: scroll(root
  block)` — no JS, reduced-motion guarded.
- **Citations**: render `[refs]` as numbered superscript chips → `SOURCES` list,
  instead of stripping them.
- **Prev/Next edition** nav (new) — **same-topic, across days**. Decided
  2026-05-29: prev/next walk to the previous/next date that has a report for
  *this same topic* (e.g. AI Devtools 29 May → its prior run 27 May → 25 May),
  NOT the next chronological day regardless of topic. This lets a reader track
  one topic's thread over time — the high-value path. Compute at build: for each
  report, find the nearest older and nearest newer date in `byDate` that also has
  this topic (skip days where the topic is absent). Hide an arrow when there is
  no neighbor (e.g. no "next" on the latest run). Always include a third,
  always-present link **"↑ {date} front page"** back to that day's homepage view
  (`/#${date}` hash) so the reader can jump from the topic thread back to the
  full day. Label shape: `← {prevDate}   {topic} · {thisDate}   {nextDate} →`,
  with the front-page link beneath/aside. Dates in mono.
- Keep ReportShare (Phase 2). The sticky share bar can fold into the prev/next
  foot on desktop; keep the mobile sticky bar.

### 4.6 Search — real Pagefind command palette (Phase 2, biggest gap)

Today the homepage is `data-pagefind-ignore` and "search" is only a client
haystack filter. Build a real search:
- **Trigger**: ⌘K / Ctrl-K, `/` to focus, click the masthead search affordance.
- **Panel**: a SOLID paper panel (NOT glass/blur — that's the AI-slop tell),
  ember `<mark>` highlights, hairline-ruled result rows.
- **Engine**: Pagefind JS API (`pagefind.debouncedSearch(q, {}, 300)`),
  `showSubResults: true` (heading-level hits inside a report), excerpt with
  baked `<mark>`. Keep the existing JSON keyword scorer as the dev fallback.
- **Facets**: promote topic chips to real `pagefind.filters()` (needs
  `data-pagefind-filter="topic"` / `"date"` on report pages — build-time attr,
  no schema change).
- **Empty state**: recent searches (localStorage, last 5) + top topics + "browse
  archive" — never a dead end.

```
┌─ ⌘K ──────────────────────────────────────────────┐
│ ⌕  agentic build|                                  │
│ ───────────────────────────────────────────────── │
│ AI DEVTOOLS · 29 May · 4 min                       │
│   …Anthropic ships <mark>agentic build</mark>…     │
│   › matches in: The news · Signals                 │
│ ───────────────────────────────────────────────── │
│ AI RESEARCH · 27 May · 3 min                       │
│   …new <mark>agentic</mark> eval suite…            │
│ ───────────────────────────────────────────────── │
│ FILTER  [topic ▾]  [date ▾]        12 results      │
└────────────────────────────────────────────────────┘
```

### 4.7 Calendar archive + homepage date navigation (keep, retune)

Already on-brand (single-accent intensity heatmap, mono numerals). The homepage
already swaps day-views in-DOM via `data-cal-day` (no network). Retune + add
explicit day navigation:

- **Prev/Next day arrows on the brief line** (new). Next to `TODAY · {date} · …`
  add `← {prevDate}` / `{nextDate} →` that swap to the neighbouring day-view
  (reuse the existing `showDay()` swap). Neighbours = adjacent entries in the
  sorted `dates[]` (any topic; the homepage is the whole-day view). Hide an arrow
  with no neighbour. Dates in mono.
- **URL hash sync** (`#2026-05-27`) so day views are shareable/back-buttonable.
  On load, if a `#date` hash matches a known day, show it; wire prev/next +
  calendar clicks to update the hash (pushState/replaceState). This is also the
  target of the report page's "↑ front page" link (§4.5).
- `aria-current="date"` on the selected calendar cell.
- Optional: unread cue per day (Phase 3a decided to skip — leave skipped).
- Add prev/next-month controls if the archive grows long.

> Two distinct date-navigations, don't conflate: the **homepage** prev/next moves
> between whole DAYS (all topics); the **report page** prev/next (§4.5) moves
> between runs of the SAME topic across days. Both use mono dates and the same
> arrow affordance, but their semantics differ by context.

### 4.8 Performance pass (Phase "3b" — folds into redesign)

This is the deferred Lighthouse work; do it as part of the rebuild since we're
touching `Base.astro` anyway:
- **Self-host + subset fonts**, drop the Google Fonts `<link>`. `@fontsource/*`
  already in deps. Add `size-adjust` fallback `@font-face`; `font-display:
  optional` for the serif display/body to kill CLS. Latin + Thai `unicode-range`
  subsets.
- **Eager LCP**: lead headline is text (good); if lead thumbnail kept, set
  `loading="eager" fetchpriority="high"` + explicit width/height. All other
  images stay lazy with explicit dimensions.
- **`content-visibility:auto`** + `contain-intrinsic-size` on hidden day-views
  and long report sections (all days are in the DOM).
- **Native `@view-transition { navigation: auto }`** (CSS only, no ClientRouter)
  + `transition:name` shared-element morph card→report. Reduced-motion guarded.

---

## 5. Files touched (per area)

- `web/src/layouts/Base.astro` — tokens (type scale, rules, measure, grid),
  masthead nameplate, font self-hosting, view-transition, ⌘K trigger.
- `web/src/components/Home.astro` — the front-page lead+rail rebuild, trending
  restyle, section grouping, unread count line, calendar retune, search panel
  mount.
- `web/src/components/Search.astro` (new) — the ⌘K Pagefind palette.
- `web/src/components/ReportShare.astro` — fold into report foot (keep mobile
  sticky).
- `web/src/pages/report/[date]/[topic]/[lang].astro` — metadata strip, KEY
  POINTS box, labeled sections, drop cap, rail TOC, progress bar, citations,
  prev/next edition.
- `web/src/lib/format.ts` — reading-time helper (EN words/200, Thai chars/350),
  section-group map, citation parser.
- `web/src/lib/i18n.ts` — new keys (eyebrow labels, "X new since", KEY POINTS,
  WHY IT MATTERS, SOURCES, search UI, prev/next).
- `web/astro.config.mjs` — Pagefind options (subResults, filters).
- `web/src/content.config.ts` — NO schema change (filters via build-time attrs).
- `.impeccable.md` — rewrite the DON'Ts/DOs to match this spec.
- Python pipeline (`social_report/`) — UNTOUCHED in all web phases.

---

## 6. Dispatch phasing

Each phase = one Sonnet dispatch, verified by `build && preview` before the next.
Phases are ordered so the site is shippable after each.

- **R0 — Foundation** (Base.astro): new tokens (type scale incl. `--step-lead`,
  3-tier rule system, measure, grid), `.eyebrow` utility, masthead nameplate,
  font self-hosting + perf (subset, `font-display`, view-transition). No layout
  rebuild yet — just the design-system substrate + the perf win. Site still
  works, looks lightly refreshed.
- **R1 — Homepage front page**: rebuild lead+rail asymmetric grid replacing
  lead-tile/tile-grid; per-card reading-time + bold-lead-in TL;DR; trending
  restyle; "X new since" count; section grouping. The headline phase.
- **R2 — Report reading page**: metadata strip, KEY POINTS box, labeled
  sections, drop cap + pull quotes, rail TOC (IO), CSS progress bar, citation
  chips, prev/next edition.
- **R3 — Search palette**: ⌘K Pagefind modal, facets, recent searches, empty
  state; un-ignore the homepage for indexing where appropriate.
- **R4 — Polish**: calendar retune (aria-current, hash sync), motion pass
  (view-transition shared-element), full light/dark + 375px + a11y sweep, update
  `.impeccable.md`.

Acceptance every phase: `npm run build` clean · `npm run preview` EN+TH ·
light/dark · 375px mobile · no regression to Pagefind/OG/RSS/share · Thai renders
correctly. No commit/push unless Mond asks. Python pipeline untouched.
