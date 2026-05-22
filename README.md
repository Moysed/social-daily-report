# Social Daily Report

AI workflow: **social media → Opus analysis → bilingual per-topic Markdown** that each
NDF DEV team member's AI can consume, plus a blog to read it.

> Phase 1 vertical slice: 5 topics × 5 connectors (HN/Bluesky/Reddit/YouTube/RSS), all
> free / no API key. Runs end-to-end with or without an Anthropic key. See full design
> in `ψ/writing/social-daily-report-architecture.md` (in the Almondo-local repo).

## How it works

```
[HN / Bluesky / Reddit / YouTube / RSS]
        │
        ▼
  fetch  →  normalize  →  dedup  →  Opus analysis (EN canonical)
                                       ├─ render  <topic>.en.md   (for AI, token-lean)
                                       └─ Sonnet translate → .th.md   (for humans / blog)
                                    →  content/reports/YYYY-MM-DD/
                                    →  data/reports.db          (archive + run log)
                                    →  MCP server               (other agents query)
```

- **EN = canonical** (source of truth, fed to other AIs). **TH = translation** (human reading).
- No `ANTHROPIC_API_KEY` → **STUB mode**: real fetch, placeholder analysis, no translation.
  Lets you test the plumbing for free before spending tokens.
- Every run is recorded in `data/reports.db` so cross-day salience ("this story carried
  for 3 days") is a SQL query, not a re-fetch.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e .                # base pipeline
pip install -e ".[mcp]"         # + MCP server
```

## Run

```bash
# STUB mode (no key) — proves the pipeline
python -m social_report.cli run --topic ai-devtools

# Dry-run — fetch + normalize + dedup, no LLM, no files (still writes to db)
python -m social_report.cli run --topic ai-devtools --dry-run --top 10

# LIVE mode — real Opus analysis + Thai translation
copy .env.example .env          # then put your key in ANTHROPIC_API_KEY
python -m social_report.cli run
```

Other flags:

- `--platform hackernews` — restrict to one connector (useful when one source is flaky)
- `--date 2026-05-21` — backfill a specific date label
- `--db PATH` / `--no-db` — point at a different SQLite store or skip it entirely
- `--out PATH` — override `content/reports/` output base

Output → `content/reports/YYYY-MM-DD/<topic>.{en,th}.md` + `index.{en,th}.md`,
plus rows in `data/reports.db`.

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

## MCP server (for other agents)

The MCP server exposes the report archive so any teammate's Claude can pull intel
without re-running the pipeline.

Wire it into Claude Code by adding to your project's `.mcp.json` (or user-level config):

```json
{
  "mcpServers": {
    "social-daily-report": {
      "command": "python",
      "args": ["-m", "social_report.mcp_server"],
      "cwd": "D:/Folder Project/social-daily-report"
    }
  }
}
```

Tools exposed:

| Tool | What it does |
|------|--------------|
| `list_topics` | All topic keys with title + focus |
| `list_reports(date?, topic?, lang='en')` | Metadata rows for rendered reports |
| `get_report(date, topic, lang='en')` | Full Markdown body + front-matter for one report |
| `search_posts(query, limit=10, since_days=7)` | FTS5 search across the post archive |
| `get_post(post_id)` | One post by id, including the raw payload |
| `topic_salience(topic, days=14)` | Salience trend (per-day) for a topic |
| `recent_runs(limit=10)` | Last N pipeline runs (status, errors, backend) |

Env overrides: `SOCIAL_REPORT_DB`, `SOCIAL_REPORT_CONTENT`.

Read-only by contract (`PRAGMA query_only = ON`) — the MCP server can't mutate the store.

## Config

`config/sources.yaml` — topics, their focus, and which connectors feed them.
Add a topic, point it at connectors, done.

## Storage

| Path | What | Notes |
|------|------|-------|
| `data/reports.db` | SQLite archive + run log | gitignored, FTS5 enabled, WAL mode |
| `content/reports/YYYY-MM-DD/` | Rendered `.en.md` + `.th.md` | git-tracked, also served via Astro |
| `web/` | Astro blog reading `content/reports/` | dev: `cd web && npm run dev` |

## Roadmap

- [x] Phase 1 slice: 5 connectors × 5 topics, bilingual render
- [x] SQLite store + run log + FTS5 (cross-day salience as SQL)
- [x] MCP server (list/get/search/salience/runs)
- [ ] Astro blog polish (`web/`)
- [ ] Cost: Batch API + prompt caching + model routing
- [ ] Scheduler (Windows Task Scheduler, 07:00 ICT)
- [ ] X via paid provider (Phase 2); IG/FB deferred

## Notes

- Automation uses an **API key** (pay-per-token), not a Claude subscription.
- Model IDs in `social_report/analyze/client.py` (`claude-opus-4-7`, `claude-sonnet-4-6`) —
  override via `OPUS_MODEL` / `SONNET_MODEL` env vars if they change.
