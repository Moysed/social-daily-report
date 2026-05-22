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

## Quickstart on a fresh PC

Clone-and-go: the repo bundles everything except keys + the Claude Code
subscription login. On a new Windows machine:

```powershell
# 1. Prereqs (one time): Python 3.11+, Git, Claude Code, GitHub CLI
#    https://www.python.org   https://claude.com/claude-code   https://cli.github.com

# 2. Clone
gh repo clone Moysed/social-daily-report
cd social-daily-report

# 3. Fill in keys (Xquik + Discord webhook + Anthropic if api backend)
copy .env.example .env
notepad .env

# 4. One-shot bootstrap: venv, install, claude login check, Task Scheduler,
#    optional Discord monitor, optional test run
.\scripts\setup-company-pc.ps1
```

After this the pipeline fires daily at 10:00 local, auto-commits the
generated reports, and pushes to `origin/main` — Vercel picks the push
up and redeploys https://social-daily-report.vercel.app automatically.

## Manual setup (if you don't want Task Scheduler)

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

## Daily scheduling (Windows Task Scheduler)

The pipeline is meant to run unattended at 10:00 local on a host that stays
on 24/7 (e.g. a company PC). All artifacts live in `scripts/`.

### One-shot setup

On the host that will run the pipeline:

```powershell
cd D:\Folder Project\social-daily-report
.\scripts\setup-company-pc.ps1
```

The setup script does the following, idempotently:

1. Verifies Python 3.11+
2. Creates `.venv`, installs `-e .[mcp]`
3. Verifies `claude` CLI and offers to `claude login` if needed
4. Confirms `.env` has `LLM_BACKEND` + the right key(s)
5. Sanity-tests the chosen backend (`claude -p "OK"` for `cli`, or the SDK for `api`)
6. Registers a `SocialDailyReport` Task Scheduler entry from `scripts/social-daily-report.xml`
   (daily 10:00, retry 3× / 15min, wake-to-run, network required, 1h time limit)
7. Optionally test-triggers the pipeline once and logs the run

After setup:

```powershell
# Inspect the task
schtasks /Query /TN SocialDailyReport /V /FO LIST

# Run on demand
schtasks /Run /TN SocialDailyReport

# Disable temporarily
schtasks /Change /TN SocialDailyReport /Disable

# Logs (gitignored)
type logs\2026-05-22.log
```

### Daily wrapper

`scripts/run-daily.ps1` is what the task runs. Resolves the repo from its own
path, activates `.venv`, runs the pipeline for all topics, and tees the output
to `logs/YYYY-MM-DD.log`. The exit code propagates so Task Scheduler flags
failures in its UI.

Can also be invoked manually:

```powershell
.\scripts\run-daily.ps1                          # all topics, today
.\scripts\run-daily.ps1 -Topic ai-devtools       # single topic
.\scripts\run-daily.ps1 -Date 2026-05-21         # backfill a date label
```

### Choosing a backend on the company PC

- **`LLM_BACKEND=cli` (subscription via Claude Code)** — free if Mond's Pro/Max
  is logged in via `claude login`. Best for "Mond's company PC" personal-use
  scenario. The Task Scheduler entry uses `InteractiveToken` so the OAuth
  keychain is reachable; the user must be logged on.
- **`LLM_BACKEND=api` (per-token API key)** — sanctioned for unattended
  automation. Use this when the report becomes a company product.

The CLI backend is great for the POC. For long-term production, switch to API
to dodge the TOS gray area around subscription + automation.

### Monitoring + recovering from expired login

A subscription session token can expire (~30 days). When it does, `claude -p`
starts failing silently and the daily run records a status='error' row in
`runs`. Check periodically:

```bash
# from the host
python -m social_report.cli  # then in another shell:
sqlite3 data/reports.db "SELECT id, started_at, status, error FROM runs ORDER BY id DESC LIMIT 5;"
```

If you see `status='error'` with a CLI auth message, re-`claude login` and the
next scheduled run will pick up the new token. (Future: a tiny monitor that
emails/pings on N consecutive errors — see roadmap.)

## Deploy (Vercel)

The web blog is a static Astro site that reads `../content/reports/`. Deploy
it via Vercel against the GitHub repo:

1. Vercel dashboard → **Add New Project** → import the GitHub repo.
2. **Root Directory**: `web/` (Astro lives in a subdir; the pipeline lives
   at the repo root).
3. Framework Preset auto-detects as **Astro**. Build command `npm run build`,
   output `dist` (already declared in `web/vercel.json`).
4. Set the `SITE` env var to the production URL once Vercel assigns one
   (e.g. `https://social-daily-report.vercel.app`). This drives the
   absolute URLs in `/rss.xml` and `/th/rss.xml`.
5. Every push to `main` redeploys. The daily pipeline (Windows Task
   Scheduler on the host PC) commits new reports → the cron-less deploy
   picks them up automatically.

To trigger a redeploy without a code change, push an empty commit:

```bash
git commit --allow-empty -m "redeploy"
git push
```

## Roadmap

- [x] Phase 1 slice: 5 connectors × 5 topics, bilingual render
- [x] SQLite store + run log + FTS5 (cross-day salience as SQL)
- [x] MCP server (list/get/search/salience/runs)
- [x] X via paid provider (Xquik connector, Phase 2)
- [x] Scheduler (Windows Task Scheduler, 10:00 local)
- [ ] Monitor: email/Discord ping when N consecutive runs fail
- [ ] Astro blog polish (`web/`)
- [ ] Cost: Batch API + prompt caching + model routing
- [ ] IG/FB deferred (no legal public access)

## Notes

- Automation uses an **API key** (pay-per-token), not a Claude subscription.
- Model IDs in `social_report/analyze/client.py` (`claude-opus-4-7`, `claude-sonnet-4-6`) —
  override via `OPUS_MODEL` / `SONNET_MODEL` env vars if they change.
