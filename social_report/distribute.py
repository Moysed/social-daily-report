"""Daily distribution — broadcast top stories to chat/social channels.

After the daily pipeline finishes, this picks the highest-salience topic for
the given date and:

  1. Posts a card to Discord webhook   (env: DISTRIBUTE_DISCORD_WEBHOOK)
  2. Posts a card to Slack webhook     (env: DISTRIBUTE_SLACK_WEBHOOK)
  3. Posts a card to MS Teams webhook  (env: DISTRIBUTE_TEAMS_WEBHOOK)
  4. Generates Twitter/LinkedIn copy via Sonnet (if a key is available) and
     dumps it to `content/distribution/YYYY-MM-DD.md` for manual posting.

Webhooks that aren't configured are skipped silently. Designed to be safe to
re-run: posting the same day twice repeats the broadcast (Discord/Slack/Teams
don't dedupe webhook calls — caller's responsibility).

Usage:
    python -m social_report.cli distribute                 # today's top, all channels
    python -m social_report.cli distribute --date today --topic ai-devtools
    python -m social_report.cli distribute --dry-run       # print payloads, no POST
    python -m social_report.cli distribute --top 3         # broadcast top N topics
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = REPO_ROOT / "data" / "reports.db"
DEFAULT_REPORTS_DIR = REPO_ROOT / "content" / "reports"
DEFAULT_OUTBOX_DIR = REPO_ROOT / "content" / "distribution"

SITE = os.environ.get("SITE", "https://social-daily-report.vercel.app").rstrip("/")
NAME = os.environ.get("DISTRIBUTE_NAME", "social-daily-report")


# ---------- data ----------

def top_reports(db_path: Path, date_label: str, n: int = 1) -> list[dict[str, Any]]:
    """Return the highest-salience EN reports for a date.

    Falls back to filesystem scan if the SQLite store is empty/missing — keeps
    distribution working in `--no-db` mode."""
    if db_path.exists():
        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA query_only = ON;")
        try:
            rows = conn.execute(
                """
                SELECT date, topic_key, path, post_count, salience, model
                FROM reports
                WHERE date = ? AND lang = 'en'
                GROUP BY topic_key HAVING MAX(id)
                ORDER BY salience DESC NULLS LAST, post_count DESC
                LIMIT ?
                """,
                (date_label, n),
            ).fetchall()
        finally:
            conn.close()
        if rows:
            return [dict(r) for r in rows]

    # Fallback: scan content/reports/<date>/.
    day_dir = DEFAULT_REPORTS_DIR / date_label
    if not day_dir.exists():
        return []
    out = []
    for p in sorted(day_dir.glob("*.en.md")):
        if p.name.startswith("index."):
            continue
        out.append({
            "date": date_label,
            "topic_key": p.name.removesuffix(".en.md"),
            "path": str(p),
            "post_count": None,
            "salience": None,
            "model": None,
        })
    return out[:n]


def _strip_frontmatter(md: str) -> tuple[dict[str, Any], str]:
    """Cheap YAML front-matter strip — we only need the title-ish fields and body."""
    if not md.startswith("---"):
        return {}, md
    parts = md.split("---", 2)
    if len(parts) < 3:
        return {}, md
    meta_raw = parts[1]
    body = parts[2].lstrip("\n")
    meta: dict[str, Any] = {}
    for line in meta_raw.splitlines():
        if ":" in line and not line.lstrip().startswith("-"):
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body


def _extract_tldr(body: str, max_chars: int = 700) -> str:
    """Pull the TL;DR section or the first paragraph from the report body."""
    lines = body.splitlines()
    bullets: list[str] = []
    in_tldr = False
    for raw in lines:
        line = raw.strip()
        if line.lower().startswith("## tl;dr") or line.lower().startswith("## สรุป"):
            in_tldr = True
            continue
        if in_tldr and line.startswith("## "):
            break
        if in_tldr and line.startswith(("-", "*")):
            bullets.append(line.lstrip("-* ").strip())
    if bullets:
        out = "\n".join(f"• {b}" for b in bullets)
        return out[:max_chars]
    # Fallback: first paragraph
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("|") or line.startswith(("-", "*")):
            continue
        return line[:max_chars]
    return ""


# ---------- platform copy generation ----------

PLATFORM_SPECS = {
    "twitter": {
        "max_chars": 240,  # 280 minus URL + buffer
        "tone": "punchy, no hashtags, no emoji, lowercase ok",
    },
    "linkedin": {
        "max_chars": 600,
        "tone": "professional, one paragraph, no emoji, no hashtags, ends with a hook line",
    },
}


def generate_social_copy(client, topic_title: str, tldr: str, url: str) -> dict[str, str]:
    """Ask the LLM to rewrite the TL;DR for each social platform. Falls back to
    a basic template when the LLM isn't available."""
    out: dict[str, str] = {}
    for platform, spec in PLATFORM_SPECS.items():
        if client and getattr(client, "enabled", False):
            system = (
                f"You write {platform} posts about AI / tech / software news. "
                f"Tone: {spec['tone']}. "
                f"Hard max {spec['max_chars']} chars EXCLUDING the URL. "
                "Output the post text only, no quotes, no preamble."
            )
            user = (
                f"Topic: {topic_title}\n\n"
                f"TL;DR (rewrite into a single {platform} post):\n{tldr}\n\n"
                f"End with this URL on its own line:\n{url}"
            )
            try:
                text = client.analyze(system, user, max_tokens=400).strip()
                out[platform] = text
                continue
            except Exception as exc:
                print(f"  distribute: !! {platform} copy via LLM failed: {exc}", file=sys.stderr)
        # Stub fallback — first line of TL;DR + URL.
        first = tldr.split("\n", 1)[0].lstrip("•- *").strip()
        truncated = first[: spec["max_chars"]].rstrip()
        out[platform] = f"{topic_title}: {truncated}\n{url}"
    return out


# ---------- webhook posters ----------

def _http_post_json(url: str, payload: dict, *, label: str) -> int:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", "User-Agent": f"{NAME}/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        body = exc.read()[:200]
        print(f"  distribute: {label} HTTP {exc.code}: {body!r}", file=sys.stderr)
        return exc.code
    except Exception as exc:
        print(f"  distribute: {label} failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return -1


def post_discord(webhook: str, *, title: str, tldr: str, url: str, color: int = 0x5865F2) -> int:
    """Post a Discord embed for one topic."""
    payload = {
        "username": NAME,
        "embeds": [{
            "title": title,
            "url": url,
            "description": tldr[:4000],
            "color": color,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }],
    }
    return _http_post_json(webhook, payload, label="discord")


def post_slack(webhook: str, *, title: str, tldr: str, url: str) -> int:
    """Slack incoming webhook payload (works for Block Kit-compatible endpoints)."""
    payload = {
        "text": f"*{title}*\n{tldr}\n{url}",
        "blocks": [
            {"type": "header", "text": {"type": "plain_text", "text": title[:150]}},
            {"type": "section", "text": {"type": "mrkdwn", "text": tldr[:2900]}},
            {"type": "context", "elements": [{"type": "mrkdwn", "text": f"<{url}|Read on Social Daily Report>"}]},
        ],
    }
    return _http_post_json(webhook, payload, label="slack")


def post_teams(webhook: str, *, title: str, tldr: str, url: str) -> int:
    """MS Teams legacy Incoming Webhook — MessageCard schema."""
    payload = {
        "@type": "MessageCard",
        "@context": "https://schema.org/extensions",
        "summary": title[:60],
        "themeColor": "5865F2",
        "title": title,
        "text": tldr.replace("\n", "  \n")[:3500],
        "potentialAction": [{
            "@type": "OpenUri",
            "name": "Read on Social Daily Report",
            "targets": [{"os": "default", "uri": url}],
        }],
    }
    return _http_post_json(webhook, payload, label="teams")


# ---------- outbox ----------

def write_outbox(outbox_dir: Path, date_label: str, broadcasts: list[dict[str, Any]]) -> Path:
    """Persist generated social copy + webhook results to content/distribution/YYYY-MM-DD.md."""
    outbox_dir.mkdir(parents=True, exist_ok=True)
    path = outbox_dir / f"{date_label}.md"
    lines: list[str] = [
        "---",
        "type: distribution-record",
        f"date: {date_label}",
        f"generated_at: {datetime.now(timezone.utc).isoformat()}",
        f"generator: {NAME}",
        "---",
        "",
        f"# Daily distribution — {date_label}",
        "",
        "Auto-generated record of what went to Discord/Slack/Teams + ready-to-post",
        "copy for Twitter and LinkedIn.",
        "",
    ]
    for b in broadcasts:
        lines.append(f"## {b['topic_title']}  (`{b['topic_key']}`)")
        lines.append("")
        lines.append(f"- Salience: {b.get('salience') if b.get('salience') is not None else 'n/a'}")
        lines.append(f"- Posts: {b.get('post_count') if b.get('post_count') is not None else 'n/a'}")
        lines.append(f"- Report URL: {b['url']}")
        lines.append("")
        lines.append("### TL;DR (broadcast body)")
        lines.append("")
        lines.append(b["tldr"])
        lines.append("")
        for platform in ("twitter", "linkedin"):
            copy = b["social_copy"].get(platform)
            if not copy:
                continue
            lines.append(f"### {platform.capitalize()} copy")
            lines.append("")
            lines.append("```text")
            lines.append(copy)
            lines.append("```")
            lines.append("")
        lines.append("### Webhook results")
        lines.append("")
        for ch, status in b["webhook_status"].items():
            ok = "ok" if status and 200 <= status < 300 else ("skipped" if status is None else f"FAIL({status})")
            lines.append(f"- {ch}: {ok}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


# ---------- orchestration ----------

def report_url(date_label: str, topic_key: str, lang: str = "en") -> str:
    return f"{SITE}/report/{date_label}/{topic_key}/{lang}"


def _topic_title(topic_key: str, db_path: Path) -> str:
    if not db_path.exists():
        return topic_key
    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute("SELECT title FROM topics WHERE key = ?", (topic_key,)).fetchone()
    finally:
        conn.close()
    return (row[0] if row else topic_key) or topic_key


def distribute(
    *,
    date_label: str,
    db_path: Path = DEFAULT_DB_PATH,
    reports_dir: Path = DEFAULT_REPORTS_DIR,
    outbox_dir: Path = DEFAULT_OUTBOX_DIR,
    topic_filter: str | None = None,
    top: int = 1,
    dry_run: bool = False,
    client=None,
    idempotent: bool = False,
) -> list[dict[str, Any]]:
    """Run the full distribution flow. Returns the broadcast records.

    When `idempotent=True`, exits early if the outbox already has a record file
    for this date — avoids reposting Discord/Slack/Teams on a re-run of the
    same day."""
    if idempotent and not dry_run:
        existing = outbox_dir / f"{date_label}.md"
        if existing.exists():
            print(f"distribute: already broadcast for {date_label} ({existing.name}); skip")
            return []
    if topic_filter:
        # Single topic — short-circuit the salience query.
        report_path = reports_dir / date_label / f"{topic_filter}.en.md"
        if not report_path.exists():
            print(f"distribute: no report for {date_label}/{topic_filter}", file=sys.stderr)
            return []
        targets = [{
            "date": date_label,
            "topic_key": topic_filter,
            "path": str(report_path),
            "post_count": None,
            "salience": None,
        }]
    else:
        targets = top_reports(db_path, date_label, n=max(1, top))
        if not targets:
            print(f"distribute: no reports for {date_label}", file=sys.stderr)
            return []

    discord_webhook = os.environ.get("DISTRIBUTE_DISCORD_WEBHOOK", "").strip()
    slack_webhook = os.environ.get("DISTRIBUTE_SLACK_WEBHOOK", "").strip()
    teams_webhook = os.environ.get("DISTRIBUTE_TEAMS_WEBHOOK", "").strip()

    broadcasts: list[dict[str, Any]] = []
    for t in targets:
        report_path = Path(t["path"])
        if not report_path.exists():
            # Fallback to canonical content/reports/<date>/<topic>.en.md
            report_path = reports_dir / date_label / f"{t['topic_key']}.en.md"
        if not report_path.exists():
            print(f"distribute: missing file {report_path}", file=sys.stderr)
            continue
        md = report_path.read_text(encoding="utf-8")
        _, body = _strip_frontmatter(md)
        tldr = _extract_tldr(body)
        url = report_url(date_label, t["topic_key"], "en")
        title = _topic_title(t["topic_key"], db_path)

        social_copy = generate_social_copy(client, title, tldr, url)
        record_title = f"{title} — {date_label}"

        webhook_status: dict[str, int | None] = {}

        if dry_run:
            print(f"\n--- dry-run · {record_title} ---")
            print(f"URL: {url}")
            print(f"TL;DR:\n{tldr}\n")
            for k, v in social_copy.items():
                print(f"[{k}]\n{v}\n")
            webhook_status = {"discord": None, "slack": None, "teams": None}
        else:
            webhook_status["discord"] = (
                post_discord(discord_webhook, title=record_title, tldr=tldr, url=url)
                if discord_webhook else None
            )
            webhook_status["slack"] = (
                post_slack(slack_webhook, title=record_title, tldr=tldr, url=url)
                if slack_webhook else None
            )
            webhook_status["teams"] = (
                post_teams(teams_webhook, title=record_title, tldr=tldr, url=url)
                if teams_webhook else None
            )

        broadcasts.append({
            "topic_key": t["topic_key"],
            "topic_title": title,
            "url": url,
            "tldr": tldr,
            "social_copy": social_copy,
            "salience": t.get("salience"),
            "post_count": t.get("post_count"),
            "webhook_status": webhook_status,
        })

    if broadcasts and not dry_run:
        out_path = write_outbox(outbox_dir, date_label, broadcasts)
        print(f"\ndistribute: wrote {out_path.relative_to(REPO_ROOT) if out_path.is_relative_to(REPO_ROOT) else out_path}")

    return broadcasts


def _today_iso() -> str:
    return date.today().isoformat()
