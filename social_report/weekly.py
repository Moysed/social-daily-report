"""Weekly digest — roll up 7 days of per-topic reports into one Markdown.

Pulls the last 7 days of EN reports (ending at the requested date), strips each
TL;DR + Signals, and (optionally) asks Sonnet for a one-paragraph weekly summary
per topic. Output lands at `content/digests/<YYYY-Www>.md` and is consumed by
the Astro `/digest/<week>` page.

Usage:
    python -m social_report.cli digest                       # week ending today
    python -m social_report.cli digest --date 2026-05-24     # week ending that day
    python -m social_report.cli digest --no-llm              # skip Sonnet summarization
    python -m social_report.cli digest --dry-run             # print, don't write
"""

from __future__ import annotations

import os
import sqlite3
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = REPO_ROOT / "data" / "reports.db"
DEFAULT_REPORTS_DIR = REPO_ROOT / "content" / "reports"
DEFAULT_DIGESTS_DIR = REPO_ROOT / "content" / "digests"


def iso_week_label(d: date) -> str:
    """Return 'YYYY-Www' for the ISO week containing d (Mon-Sun)."""
    year, week, _ = d.isocalendar()
    return f"{year}-W{week:02d}"


def week_window(end_date: date) -> tuple[date, date]:
    """7-day window ending (inclusive) at `end_date`."""
    return end_date - timedelta(days=6), end_date


def _strip_frontmatter(md: str) -> str:
    if not md.startswith("---"):
        return md
    parts = md.split("---", 2)
    return parts[2].lstrip("\n") if len(parts) >= 3 else md


def _extract_section(body: str, header_starts: tuple[str, ...]) -> list[str]:
    """Pull bullets from the first matching '## <header>' section in a report body."""
    out: list[str] = []
    in_section = False
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            label = line[3:].lower()
            in_section = any(label.startswith(h) for h in header_starts)
            continue
        if in_section and line.startswith(("-", "*")):
            out.append(line.lstrip("-* ").strip())
    return out


def gather_topic_reports(
    *,
    db_path: Path,
    reports_dir: Path,
    start: date,
    end: date,
) -> dict[str, list[dict[str, Any]]]:
    """Return {topic_key: [{date, title, salience, tldr, signals}, ...]} for the
    7-day window. Sorted by date ascending within each topic."""
    by_topic: dict[str, list[dict[str, Any]]] = {}

    # Prefer the SQLite registry — has salience + canonical paths.
    if db_path.exists():
        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA query_only = ON;")
        try:
            rows = conn.execute(
                """
                SELECT r.date, r.topic_key, r.path, r.salience, r.post_count,
                       t.title AS title
                FROM reports r
                LEFT JOIN topics t ON t.key = r.topic_key
                WHERE r.lang = 'en' AND r.date BETWEEN ? AND ?
                GROUP BY r.date, r.topic_key HAVING MAX(r.id)
                ORDER BY r.date ASC, r.topic_key ASC
                """,
                (start.isoformat(), end.isoformat()),
            ).fetchall()
        finally:
            conn.close()
    else:
        rows = []

    seen: set[tuple[str, str]] = set()
    for row in rows:
        path = Path(row["path"])
        if not path.exists():
            path = reports_dir / row["date"] / f"{row['topic_key']}.en.md"
        if not path.exists():
            continue
        body = _strip_frontmatter(path.read_text(encoding="utf-8"))
        entry = {
            "date": row["date"],
            "title": row["title"] or row["topic_key"],
            "salience": row["salience"],
            "post_count": row["post_count"],
            "tldr": _extract_section(body, ("tl;dr", "tldr", "สรุป")),
            "signals": _extract_section(body, ("signals", "signal")),
        }
        by_topic.setdefault(row["topic_key"], []).append(entry)
        seen.add((row["date"], row["topic_key"]))

    # Filesystem fallback for any (date, topic) the DB missed (e.g. --no-db runs).
    day = start
    while day <= end:
        day_dir = reports_dir / day.isoformat()
        if day_dir.exists():
            for p in sorted(day_dir.glob("*.en.md")):
                if p.name.startswith("index."):
                    continue
                topic_key = p.name.removesuffix(".en.md")
                if (day.isoformat(), topic_key) in seen:
                    continue
                body = _strip_frontmatter(p.read_text(encoding="utf-8"))
                by_topic.setdefault(topic_key, []).append({
                    "date": day.isoformat(),
                    "title": topic_key,
                    "salience": None,
                    "post_count": None,
                    "tldr": _extract_section(body, ("tl;dr", "tldr", "สรุป")),
                    "signals": _extract_section(body, ("signals", "signal")),
                })
        day += timedelta(days=1)

    for topic in by_topic.values():
        topic.sort(key=lambda e: e["date"])
    return by_topic


def average_salience(entries: list[dict[str, Any]]) -> float | None:
    vals = [e["salience"] for e in entries if e.get("salience") is not None]
    return sum(vals) / len(vals) if vals else None


def summarize_topic(client, topic_title: str, entries: list[dict[str, Any]]) -> str:
    """Ask Sonnet for a 1-paragraph weekly synthesis. Falls back to concatenated bullets."""
    if not entries:
        return ""
    flat_tldr = []
    for e in entries:
        for b in e["tldr"][:3]:
            flat_tldr.append(f"[{e['date']}] {b}")
    flat_signals = []
    for e in entries:
        for s in e["signals"][:2]:
            flat_signals.append(f"[{e['date']}] {s}")

    if client and getattr(client, "enabled", False):
        system = (
            "You write weekly news digests for a software/AI/XR/edutech studio. "
            "Synthesize the daily bullets into ONE compact paragraph (max ~110 words) "
            "highlighting what carried across days, the single biggest event, and the "
            "implication for a dev team. No bullets, no headers — prose only. "
            "Do not invent facts; if a thread isn't clearly recurring, don't say it is."
        )
        user = (
            f"Topic: {topic_title}\n\n"
            f"Daily TL;DRs across the week (date in brackets):\n"
            + "\n".join(flat_tldr)
            + ("\n\nDaily signals:\n" + "\n".join(flat_signals) if flat_signals else "")
        )
        try:
            return client.analyze(system, user, max_tokens=400).strip()
        except Exception as exc:
            print(f"  digest: !! Sonnet summary failed for {topic_title}: {exc}", file=sys.stderr)

    # Fallback: most recent date's TL;DR concatenated.
    recent = entries[-1]
    if recent["tldr"]:
        return " ".join(f"[{recent['date']}] {b}" for b in recent["tldr"][:4])
    return f"{len(entries)} reports this week."


def render_digest(
    *,
    week_label: str,
    start: date,
    end: date,
    by_topic: dict[str, list[dict[str, Any]]],
    summaries: dict[str, str],
) -> str:
    now = datetime.now(timezone.utc).isoformat()
    head = [
        "---",
        "type: weekly-digest",
        f'week: "{week_label}"',
        f'start: "{start.isoformat()}"',
        f'end: "{end.isoformat()}"',
        f'generated_at: "{now}"',
        "generator: social-daily-report-weekly",
        f"topic_count: {len(by_topic)}",
        "---",
        "",
        f"# Weekly digest — {week_label}",
        "",
        f"_Window: {start.isoformat()} → {end.isoformat()} (7 days)_",
        "",
    ]
    # Sort topics by avg salience desc, then name.
    def sort_key(item):
        topic_key, entries = item
        avg = average_salience(entries) or 0
        return (-avg, topic_key)

    body: list[str] = []
    for topic_key, entries in sorted(by_topic.items(), key=sort_key):
        title = entries[0]["title"]
        avg = average_salience(entries)
        avg_str = f"{avg:.2f}" if avg is not None else "n/a"
        body.append(f"## {title}  (`{topic_key}`)")
        body.append("")
        body.append(f"_Days: {len(entries)} · avg salience: {avg_str}_")
        body.append("")
        summary = summaries.get(topic_key, "")
        if summary:
            body.append(summary)
            body.append("")
        body.append("### Day-by-day signals")
        body.append("")
        for e in entries:
            body.append(f"**{e['date']}** — salience {e['salience'] if e['salience'] is not None else 'n/a'}")
            for b in e["tldr"][:3]:
                body.append(f"- {b}")
            body.append("")
    return "\n".join(head + body)


def run_digest(
    *,
    end_date: date,
    db_path: Path = DEFAULT_DB_PATH,
    reports_dir: Path = DEFAULT_REPORTS_DIR,
    digests_dir: Path = DEFAULT_DIGESTS_DIR,
    dry_run: bool = False,
    client=None,
) -> Path | None:
    start, end = week_window(end_date)
    by_topic = gather_topic_reports(
        db_path=db_path, reports_dir=reports_dir, start=start, end=end
    )
    if not by_topic:
        print(f"digest: no reports in {start} → {end}", file=sys.stderr)
        return None

    summaries: dict[str, str] = {}
    for topic_key, entries in by_topic.items():
        title = entries[0]["title"]
        summaries[topic_key] = summarize_topic(client, title, entries)

    week_label = iso_week_label(end_date)
    md = render_digest(
        week_label=week_label,
        start=start, end=end,
        by_topic=by_topic, summaries=summaries,
    )

    if dry_run:
        print(md)
        return None

    digests_dir.mkdir(parents=True, exist_ok=True)
    path = digests_dir / f"{week_label}.md"
    path.write_text(md, encoding="utf-8")
    print(f"digest: wrote {path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path}")
    return path
