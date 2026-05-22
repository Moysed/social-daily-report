"""SQLite store — posts archive, run log, report registry.

Single file at `data/reports.db` (gitignored). Stdlib `sqlite3` only.

Tables:
  - posts             : every unique post seen (dedup key = stable id). raw kept
                        as JSON; FTS5 mirror table `posts_fts` for text search.
  - topic_membership  : post_id <-> topic_key (a post can land in many topics).
  - topics            : topic master (title, focus).
  - runs              : one row per `social-report run` invocation.
  - reports           : one row per generated .md (run_id, date, topic, lang).

Tracks `first_seen_at` / `last_seen_at` on posts so cross-day salience
("this story carried over 3 days") is a SQL query, not a re-fetch.
"""

from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from ..models import Post

SCHEMA_VERSION = 1

SCHEMA = """
CREATE TABLE IF NOT EXISTS schema_version (
    version INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS posts (
    id              TEXT PRIMARY KEY,         -- "<platform>:<native_id>"
    platform        TEXT NOT NULL,
    author          TEXT,
    text            TEXT NOT NULL,
    url             TEXT NOT NULL,
    canonical_url   TEXT NOT NULL,
    created_at      TEXT NOT NULL,            -- ISO UTC
    first_seen_at   TEXT NOT NULL,
    last_seen_at    TEXT NOT NULL,
    likes           INTEGER DEFAULT 0,
    reposts         INTEGER DEFAULT 0,
    comments        INTEGER DEFAULT 0,
    score           REAL DEFAULT 0.0,
    lang            TEXT,
    dup_count       INTEGER DEFAULT 1,
    also_on         TEXT DEFAULT '[]',        -- JSON array
    raw             TEXT DEFAULT '{}'         -- JSON dict
);
CREATE INDEX IF NOT EXISTS idx_posts_created   ON posts(created_at);
CREATE INDEX IF NOT EXISTS idx_posts_canonical ON posts(canonical_url);
CREATE INDEX IF NOT EXISTS idx_posts_platform  ON posts(platform);

CREATE VIRTUAL TABLE IF NOT EXISTS posts_fts USING fts5(
    text,
    content='posts',
    content_rowid='rowid'
);

CREATE TRIGGER IF NOT EXISTS posts_fts_ai AFTER INSERT ON posts BEGIN
    INSERT INTO posts_fts(rowid, text) VALUES (new.rowid, new.text);
END;
CREATE TRIGGER IF NOT EXISTS posts_fts_ad AFTER DELETE ON posts BEGIN
    INSERT INTO posts_fts(posts_fts, rowid, text) VALUES('delete', old.rowid, old.text);
END;
CREATE TRIGGER IF NOT EXISTS posts_fts_au AFTER UPDATE ON posts BEGIN
    INSERT INTO posts_fts(posts_fts, rowid, text) VALUES('delete', old.rowid, old.text);
    INSERT INTO posts_fts(rowid, text) VALUES (new.rowid, new.text);
END;

CREATE TABLE IF NOT EXISTS topics (
    key   TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    focus TEXT
);

CREATE TABLE IF NOT EXISTS topic_membership (
    post_id   TEXT NOT NULL,
    topic_key TEXT NOT NULL,
    date      TEXT NOT NULL,                  -- ISO date the membership was observed
    PRIMARY KEY (post_id, topic_key, date),
    FOREIGN KEY (post_id)   REFERENCES posts(id)  ON DELETE CASCADE,
    FOREIGN KEY (topic_key) REFERENCES topics(key) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_membership_topic_date ON topic_membership(topic_key, date);

CREATE TABLE IF NOT EXISTS runs (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at   TEXT NOT NULL,
    finished_at  TEXT,
    status       TEXT NOT NULL,               -- running | ok | error | dry-run
    date_label   TEXT NOT NULL,               -- which day was generated
    topic_filter TEXT,                        -- NULL = all topics
    backend      TEXT,                        -- api | cli | stub
    error        TEXT
);

CREATE TABLE IF NOT EXISTS reports (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id        INTEGER NOT NULL,
    date          TEXT NOT NULL,
    topic_key     TEXT NOT NULL,
    lang          TEXT NOT NULL,              -- en | th
    path          TEXT NOT NULL,
    post_count    INTEGER DEFAULT 0,
    salience      REAL,
    model         TEXT,
    translated_by TEXT,
    FOREIGN KEY (run_id)    REFERENCES runs(id)   ON DELETE CASCADE,
    FOREIGN KEY (topic_key) REFERENCES topics(key)
);
CREATE INDEX IF NOT EXISTS idx_reports_date_topic ON reports(date, topic_key);
"""


def _canonical_url(url: str) -> str:
    # Re-export the dedup helper to keep the store self-contained at the call site.
    from ..dedup import canonical_url
    return canonical_url(url)


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    cur = conn.execute("SELECT version FROM schema_version LIMIT 1;")
    row = cur.fetchone()
    if row is None:
        conn.execute("INSERT INTO schema_version (version) VALUES (?)", (SCHEMA_VERSION,))
    conn.commit()


@contextmanager
def opened(db_path: Path):
    conn = connect(db_path)
    try:
        init_db(conn)
        yield conn
    finally:
        conn.close()


# ---------- writes ----------

def upsert_topic(conn: sqlite3.Connection, key: str, title: str, focus: str = "") -> None:
    conn.execute(
        """
        INSERT INTO topics (key, title, focus) VALUES (?, ?, ?)
        ON CONFLICT(key) DO UPDATE SET title = excluded.title, focus = excluded.focus
        """,
        (key, title, focus),
    )


def upsert_post(conn: sqlite3.Connection, p: Post) -> None:
    """Insert new post or refresh engagement + last_seen_at on an existing one."""
    now = _utcnow()
    conn.execute(
        """
        INSERT INTO posts (
            id, platform, author, text, url, canonical_url,
            created_at, first_seen_at, last_seen_at,
            likes, reposts, comments, score, lang,
            dup_count, also_on, raw
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            last_seen_at = excluded.last_seen_at,
            likes        = MAX(posts.likes, excluded.likes),
            reposts      = MAX(posts.reposts, excluded.reposts),
            comments     = MAX(posts.comments, excluded.comments),
            score        = MAX(posts.score, excluded.score),
            dup_count    = excluded.dup_count,
            also_on      = excluded.also_on
        """,
        (
            p.id, p.platform, p.author, p.text, p.url, _canonical_url(p.url),
            p.created_at.isoformat(), now, now,
            p.engagement.likes, p.engagement.reposts, p.engagement.comments, p.engagement.score,
            p.lang, p.dup_count, json.dumps(p.also_on), json.dumps(p.raw, default=str),
        ),
    )


def record_membership(conn: sqlite3.Connection, post_id: str, topic_key: str, date_label: str) -> None:
    conn.execute(
        "INSERT OR IGNORE INTO topic_membership (post_id, topic_key, date) VALUES (?, ?, ?)",
        (post_id, topic_key, date_label),
    )


def start_run(
    conn: sqlite3.Connection,
    date_label: str,
    topic_filter: str | None,
    backend: str,
    dry_run: bool = False,
) -> int:
    status = "dry-run" if dry_run else "running"
    cur = conn.execute(
        """
        INSERT INTO runs (started_at, status, date_label, topic_filter, backend)
        VALUES (?, ?, ?, ?, ?)
        """,
        (_utcnow(), status, date_label, topic_filter, backend),
    )
    conn.commit()
    return int(cur.lastrowid)


def finish_run(conn: sqlite3.Connection, run_id: int, status: str = "ok", error: str | None = None) -> None:
    conn.execute(
        "UPDATE runs SET finished_at = ?, status = ?, error = ? WHERE id = ?",
        (_utcnow(), status, error, run_id),
    )
    conn.commit()


def record_report(
    conn: sqlite3.Connection,
    *,
    run_id: int,
    date: str,
    topic_key: str,
    lang: str,
    path: Path,
    post_count: int,
    salience: float | None,
    model: str | None,
    translated_by: str | None = None,
) -> int:
    cur = conn.execute(
        """
        INSERT INTO reports (run_id, date, topic_key, lang, path, post_count, salience, model, translated_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (run_id, date, topic_key, lang, str(path), post_count, salience, model, translated_by),
    )
    return int(cur.lastrowid)
