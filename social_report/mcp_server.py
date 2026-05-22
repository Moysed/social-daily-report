"""MCP server — serve the social-daily-report store to other agents.

Exposes the SQLite `data/reports.db` archive + the rendered Markdown reports
in `content/reports/` as MCP tools. Designed so every teammate's Claude can
pull the day's intel without re-fetching or re-summarizing.

Transport: stdio (default). Wire into Claude Code via a `.mcp.json` entry:

    {
      "mcpServers": {
        "social-daily-report": {
          "command": "python",
          "args": ["-m", "social_report.mcp_server"],
          "cwd": "D:/Folder Project/social-daily-report"
        }
      }
    }

Run `pip install -e ".[mcp]"` first.
"""

from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = REPO_ROOT / "data" / "reports.db"
DEFAULT_REPORTS_DIR = REPO_ROOT / "content" / "reports"

# Allow env override so the server can run against a copy of the db.
DB_PATH = Path(os.environ.get("SOCIAL_REPORT_DB", DEFAULT_DB_PATH))
REPORTS_DIR = Path(os.environ.get("SOCIAL_REPORT_CONTENT", DEFAULT_REPORTS_DIR))

mcp = FastMCP("social-daily-report")


def _conn() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"SQLite store not found at {DB_PATH}. "
            "Run `social-report run` at least once, or set SOCIAL_REPORT_DB."
        )
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA query_only = ON;")  # MCP is read-only by contract
    return conn


def _rows(cursor: sqlite3.Cursor) -> list[dict[str, Any]]:
    return [dict(r) for r in cursor.fetchall()]


# ---------- tools ----------


@mcp.tool()
def list_topics() -> list[dict]:
    """List all topic keys with their title and focus.

    Use this first to discover what topics the store covers. Topic keys
    (e.g. 'ai-devtools') are the canonical identifiers used by other tools.
    """
    with _conn() as conn:
        return _rows(conn.execute("SELECT key, title, focus FROM topics ORDER BY key"))


@mcp.tool()
def list_reports(date: str | None = None, topic: str | None = None, lang: str = "en") -> list[dict]:
    """List rendered reports as metadata rows (no body).

    Args:
        date: ISO date 'YYYY-MM-DD'. Omit to list across all dates.
        topic: topic key (e.g. 'ai-devtools'). Omit for all topics.
        lang: 'en' (canonical, AI-readable) or 'th' (human translation).

    Returns the latest report per (date, topic, lang). Use `get_report` to fetch
    the body once a row catches your eye.
    """
    sql = (
        "SELECT date, topic_key, lang, path, post_count, salience, model, translated_by, "
        "       MAX(id) AS report_id "
        "FROM reports WHERE lang = ?"
    )
    params: list[Any] = [lang]
    if date:
        sql += " AND date = ?"
        params.append(date)
    if topic:
        sql += " AND topic_key = ?"
        params.append(topic)
    sql += " GROUP BY date, topic_key, lang ORDER BY date DESC, topic_key"
    with _conn() as conn:
        return _rows(conn.execute(sql, params))


@mcp.tool()
def get_report(date: str, topic: str, lang: str = "en") -> dict:
    """Fetch the full Markdown body (with front-matter) for one report.

    Args:
        date: ISO date 'YYYY-MM-DD'.
        topic: topic key (e.g. 'ai-devtools').
        lang: 'en' (canonical) or 'th'.

    Returns: {'path', 'post_count', 'salience', 'model', 'markdown', 'translated_by'}.
    The `.en.md` is the AI-canonical version — prefer it unless the user explicitly
    wants Thai.
    """
    with _conn() as conn:
        row = conn.execute(
            """
            SELECT path, post_count, salience, model, translated_by
            FROM reports
            WHERE date = ? AND topic_key = ? AND lang = ?
            ORDER BY id DESC LIMIT 1
            """,
            (date, topic, lang),
        ).fetchone()
    if row is None:
        raise ValueError(f"No report for date={date} topic={topic} lang={lang}.")
    path = Path(row["path"])
    if not path.exists():
        # fallback: maybe the path was stored relative or against a different repo root
        candidate = REPORTS_DIR / date / f"{topic}.{lang}.md"
        if candidate.exists():
            path = candidate
        else:
            raise FileNotFoundError(f"Report file not found: {row['path']}")
    return {
        "path": str(path),
        "post_count": row["post_count"],
        "salience": row["salience"],
        "model": row["model"],
        "translated_by": row["translated_by"],
        "markdown": path.read_text(encoding="utf-8"),
    }


@mcp.tool()
def search_posts(query: str, limit: int = 10, since_days: int = 7) -> list[dict]:
    """Full-text search the post archive (SQLite FTS5).

    Args:
        query: FTS5 match query (supports phrases "...", prefix foo*, AND/OR/NOT).
        limit: max rows. Default 10, hard cap 100.
        since_days: window. Default 7 days. Use 0 to search the whole archive.

    Returns top posts by recency, with platform, score, URL, and a 240-char text snippet.
    """
    limit = max(1, min(int(limit), 100))
    since = (
        (datetime.now(timezone.utc) - timedelta(days=since_days)).isoformat()
        if since_days > 0
        else None
    )
    sql = (
        "SELECT p.id, p.platform, p.author, substr(p.text, 1, 240) AS snippet, p.url, "
        "       p.created_at, p.likes, p.score, p.dup_count, p.also_on "
        "FROM posts_fts f JOIN posts p ON p.rowid = f.rowid "
        "WHERE posts_fts MATCH ?"
    )
    params: list[Any] = [query]
    if since:
        sql += " AND p.created_at >= ?"
        params.append(since)
    sql += " ORDER BY p.created_at DESC LIMIT ?"
    params.append(limit)
    with _conn() as conn:
        return _rows(conn.execute(sql, params))


@mcp.tool()
def get_post(post_id: str) -> dict:
    """Fetch one post by id (format '<platform>:<native_id>') including the raw payload."""
    with _conn() as conn:
        row = conn.execute(
            "SELECT id, platform, author, text, url, canonical_url, created_at, "
            "       first_seen_at, last_seen_at, likes, reposts, comments, score, "
            "       lang, dup_count, also_on, raw "
            "FROM posts WHERE id = ?",
            (post_id,),
        ).fetchone()
    if row is None:
        raise ValueError(f"Post not found: {post_id}")
    return dict(row)


@mcp.tool()
def topic_salience(topic: str, days: int = 14) -> list[dict]:
    """Salience trend for a topic over the last N days.

    Args:
        topic: topic key (e.g. 'ai-devtools').
        days: window (default 14).

    Returns one row per date: {'date', 'salience', 'post_count'}. Higher salience
    means the topic was more dense / important that day. Use to spot week-over-week
    trends or hot streaks.
    """
    since = (datetime.now(timezone.utc) - timedelta(days=days)).date().isoformat()
    with _conn() as conn:
        return _rows(
            conn.execute(
                """
                SELECT date, MAX(salience) AS salience, MAX(post_count) AS post_count
                FROM reports
                WHERE topic_key = ? AND lang = 'en' AND date >= ?
                GROUP BY date ORDER BY date
                """,
                (topic, since),
            )
        )


@mcp.tool()
def recent_runs(limit: int = 10) -> list[dict]:
    """Show the last N pipeline runs (started_at, finished_at, status, errors).

    Use to confirm the pipeline ran today, or to diagnose stale/missing reports.
    Status values: 'running', 'ok', 'error', 'dry-run'.
    """
    limit = max(1, min(int(limit), 100))
    with _conn() as conn:
        return _rows(
            conn.execute(
                """
                SELECT id, started_at, finished_at, status, date_label, topic_filter, backend, error
                FROM runs ORDER BY id DESC LIMIT ?
                """,
                (limit,),
            )
        )


def main() -> None:
    # FastMCP.run() defaults to stdio transport; logs go to stderr.
    print(f"[social-daily-report-mcp] db={DB_PATH}", file=sys.stderr)
    mcp.run()


if __name__ == "__main__":
    main()
