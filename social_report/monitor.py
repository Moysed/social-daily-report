"""Health monitor — ping Discord (or any webhook) when the daily pipeline drifts.

Checks the SQLite `runs` table for three failure modes and posts a single
combined alert if anything is off. Idempotent: posts at most one alert per
call, with the details fields listing every issue found.

Failure modes:

1. **stale** — most recent successful run finished more than `--stale-hours`
   ago (default 25, so a run that misses 07:00 is caught by 09:00 monitor).
2. **consecutive errors** — last `--max-errors` runs all have status='error'
   (default 3 in a row).
3. **no run today** — no row in `runs` with date_label = today AND status='ok'
   (only flagged after `--quiet-until` local hour, default 9, so we don't
   warn before the 07:00 job has had time to run).

Env:
    MONITOR_DISCORD_WEBHOOK     required to actually post; otherwise dry-run prints
    MONITOR_NAME                shown in the alert title (default: 'social-daily-report')

Usage:
    python -m social_report.monitor                 # full check, post if anything off
    python -m social_report.monitor --dry-run       # print to stdout only
    python -m social_report.monitor --status        # always post (heartbeat)
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any
# Windows console can't handle non-ascii — same pattern as cli.py
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = REPO_ROOT / "data" / "reports.db"
NAME = os.environ.get("MONITOR_NAME", "social-daily-report")


def _resolve_local_tz():
    """Try IANA tz via zoneinfo; on Windows w/o tzdata, fall back to fixed offset."""
    tz_name = os.environ.get("MONITOR_TZ", "Asia/Bangkok")
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo(tz_name)
    except Exception:
        # Common case: Windows has no system tzdata. Hardcode ICT for the default.
        if tz_name == "Asia/Bangkok":
            return timezone(timedelta(hours=7), name="ICT")
        # Anything else falls back to UTC with a warning so checks still work.
        print(f"warn: tz '{tz_name}' unresolved; falling back to UTC", file=sys.stderr)
        return timezone.utc


LOCAL_TZ = _resolve_local_tz()


def _now_local() -> datetime:
    return datetime.now(LOCAL_TZ)


def _fetch_runs(db_path: Path, limit: int) -> list[dict[str, Any]]:
    if not db_path.exists():
        return []
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA query_only = ON;")
    try:
        rows = conn.execute(
            "SELECT id, started_at, finished_at, status, date_label, topic_filter, "
            "       backend, error "
            "FROM runs ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    finally:
        conn.close()
    return [dict(r) for r in rows]


def _hours_since(iso_ts: str | None) -> float | None:
    if not iso_ts:
        return None
    try:
        dt = datetime.fromisoformat(iso_ts)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - dt).total_seconds() / 3600.0


def check_health(
    db_path: Path,
    *,
    stale_hours: float = 25.0,
    max_errors: int = 3,
    quiet_until_hour: int = 9,
) -> dict[str, Any]:
    """Run the three checks. Returns a dict with `issues` (list of str) and `runs`."""
    runs = _fetch_runs(db_path, limit=max(10, max_errors + 1))
    issues: list[str] = []

    last_ok = next((r for r in runs if r["status"] == "ok"), None)
    last_finished = next((r for r in runs if r["status"] in ("ok", "error")), None)

    # 1. stale — judged against the last *finished* run regardless of status,
    # since "error" runs still prove the wrapper ran.
    hrs = _hours_since((last_finished or {}).get("finished_at"))
    if last_finished is None:
        issues.append(f"No runs in `{db_path.name}` at all yet.")
    elif hrs is not None and hrs > stale_hours:
        issues.append(
            f"Stale: last finished run was {hrs:.1f}h ago (> {stale_hours}h). "
            f"id={last_finished['id']} status={last_finished['status']}"
        )

    # 2. consecutive errors
    consecutive = 0
    for r in runs:
        if r["status"] == "error":
            consecutive += 1
        elif r["status"] in ("ok", "dry-run"):
            break
    if consecutive >= max_errors:
        last_err = next((r for r in runs if r["status"] == "error"), {})
        issues.append(
            f"{consecutive} consecutive error runs (>= {max_errors}). "
            f"Most recent error: {last_err.get('error') or '<no message>'}"
        )

    # 3. no run today (after quiet-until)
    local_now = _now_local()
    today = local_now.date().isoformat()
    if local_now.hour >= quiet_until_hour:
        ran_today = any(
            r["date_label"] == today and r["status"] == "ok" for r in runs
        )
        if not ran_today:
            issues.append(
                f"No successful run recorded for {today} "
                f"(local hour {local_now.hour:02d} >= {quiet_until_hour:02d})."
            )

    return {
        "issues": issues,
        "checked_at": local_now.isoformat(),
        "last_ok_id": (last_ok or {}).get("id"),
        "last_ok_at": (last_ok or {}).get("finished_at"),
        "last_finished_status": (last_finished or {}).get("status"),
        "recent_runs": runs[:5],
    }


def _post_discord(webhook_url: str, title: str, ok: bool, fields: list[dict[str, str]]) -> int:
    payload = {
        "username": NAME,
        "embeds": [
            {
                "title": title,
                "color": 0x2ECC71 if ok else 0xE74C3C,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "fields": fields,
            }
        ],
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json", "User-Agent": "social-daily-report-monitor/0.1"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        print(f"Discord webhook HTTP {exc.code}: {exc.read()[:200]!r}", file=sys.stderr)
        return exc.code
    except Exception as exc:  # network errors etc.
        print(f"Discord webhook failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return -1


def _format_fields(result: dict[str, Any]) -> list[dict[str, str]]:
    runs_blob = "\n".join(
        f"#{r['id']} {r['status']:<7} {r['date_label']} "
        f"({r.get('topic_filter') or 'all'}, {r.get('backend') or '?'}, "
        f"err={(r.get('error') or '')[:40]})"
        for r in result["recent_runs"]
    ) or "<no runs yet>"
    fields = [
        {"name": "Checked at", "value": result["checked_at"], "inline": True},
        {
            "name": "Last OK",
            "value": f"#{result['last_ok_id']} @ {result['last_ok_at']}"
            if result["last_ok_id"] else "(none)",
            "inline": True,
        },
    ]
    if result["issues"]:
        fields.append({
            "name": f"Issues ({len(result['issues'])})",
            "value": "\n".join(f"- {i}" for i in result["issues"])[:1024],
            "inline": False,
        })
    fields.append({"name": "Recent runs", "value": f"```\n{runs_blob[:900]}\n```", "inline": False})
    return fields


def main() -> int:
    parser = argparse.ArgumentParser(prog="social-report-monitor")
    parser.add_argument("--db", help="SQLite path (default: data/reports.db)")
    parser.add_argument("--stale-hours", type=float, default=25.0)
    parser.add_argument("--max-errors", type=int, default=3)
    parser.add_argument(
        "--quiet-until", type=int, default=9,
        help="Local hour before which we don't flag 'no run today' (default 9)",
    )
    parser.add_argument(
        "--status", action="store_true",
        help="Always post, even when healthy (heartbeat mode)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print payload to stdout, don't POST",
    )
    args = parser.parse_args()

    db_path = Path(args.db) if args.db else DEFAULT_DB_PATH
    result = check_health(
        db_path,
        stale_hours=args.stale_hours,
        max_errors=args.max_errors,
        quiet_until_hour=args.quiet_until,
    )

    healthy = not result["issues"]
    title = f"[{NAME}] {'OK' if healthy else 'ALERT'}"
    fields = _format_fields(result)

    if args.dry_run or (healthy and not args.status):
        print(json.dumps({"title": title, "fields": fields, "result": result}, indent=2, default=str))
        if healthy and not args.status:
            print("\n(healthy, no post — pass --status for heartbeat)", file=sys.stderr)
        return 0

    webhook = os.environ.get("MONITOR_DISCORD_WEBHOOK", "").strip()
    if not webhook:
        print("MONITOR_DISCORD_WEBHOOK not set; would have posted:", file=sys.stderr)
        print(json.dumps({"title": title, "fields": fields}, indent=2), file=sys.stderr)
        return 0 if healthy else 2

    status = _post_discord(webhook, title, ok=healthy, fields=fields)
    if status >= 400:
        return 3
    return 0 if healthy else 2  # exit !=0 on issue so Task Scheduler can flag


if __name__ == "__main__":
    sys.exit(main())
