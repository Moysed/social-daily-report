# Social Daily Report

AI workflow: **social media → Opus analysis → bilingual per-topic Markdown** that each
NDF DEV team member's AI can consume, plus a blog to read it.

> Phase 1 vertical slice: **HackerNews → topic `ai-devtools`**. Runs end-to-end with or
> without an API key. See full design in `ψ/writing/social-daily-report-architecture.md`
> (in the Almondo-local repo).

## How it works

```
HackerNews API  →  normalize (Post)  →  Opus analysis (EN, canonical)
                                          ├─ render  ai-devtools.en.md   (for AI, token-lean)
                                          └─ Sonnet translate → .th.md   (for humans / blog)
                                       →  content/reports/YYYY-MM-DD/
```

- **EN = canonical** (source of truth, fed to other AIs). **TH = translation** (human reading).
- No `ANTHROPIC_API_KEY` → **STUB mode**: real HN fetch, placeholder analysis, no translation.
  Lets you test the plumbing for free before spending tokens.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

## Run

```bash
# STUB mode (no key) — proves the pipeline
python -m social_report.cli run --topic ai-devtools

# LIVE mode — real Opus analysis + Thai translation
copy .env.example .env          # then put your key in ANTHROPIC_API_KEY
python -m social_report.cli run
```

Output → `content/reports/YYYY-MM-DD/<topic>.{en,th}.md` + `index.{en,th}.md`.

### Use your Claude subscription instead of API tokens

Set `LLM_BACKEND=cli` in `.env`. The pipeline then shells out to `claude -p`, which bills
against your **Pro/Max subscription** (when logged in) instead of the API.

```bash
claude login                       # one-time, if not already
# .env:  LLM_BACKEND=cli
python -m social_report.cli run --topic ai-devtools
```

Quick sanity check that the subscription path works:

```bash
claude -p "Reply with only: OK" --model opus --output-format json
```

Caveats:
- Runs only where Claude Code is **logged in** → keep the scheduler local (your machine), not a cloud server.
- Using a subscription for unattended automation is a **gray area** Anthropic is tightening
  (headless/automated use is moving to separate metering). Fine for personal/internal use;
  keep the company product on `LLM_BACKEND=api`. The backend is a one-line switch either way.

## Config

`config/sources.yaml` — topics, their focus, and which connectors feed them.
Add a topic, point it at connectors, done.

## Roadmap

- [x] Phase 1 slice: HackerNews → `ai-devtools`, bilingual render
- [ ] More connectors: Bluesky, Reddit, YouTube, RSS (all free)
- [ ] More topics: game-dev, xr, web-frontend, edtech, ai-productivity, global-tech
- [ ] SQLite store + run log, dedup across days
- [ ] Cost: Batch API + prompt caching + model routing
- [ ] Astro blog reading `content/reports/`
- [ ] MCP server (`report_get`, `report_index`, `report_search`, `topic_timeline`)
- [ ] Scheduler (Windows Task Scheduler, 07:00 ICT)
- [ ] X via paid provider (Phase 2); IG/FB deferred

## Notes

- Automation uses an **API key** (pay-per-token), not a Claude subscription.
- Model IDs in `social_report/analyze/client.py` (`claude-opus-4-7`, `claude-sonnet-4-6`) —
  override via `OPUS_MODEL` / `SONNET_MODEL` env vars if they change.
