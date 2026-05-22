"""Lobsters connector — public hottest.json endpoint, no auth, free.

Lobsters is a tech-focused link aggregator (think small, curated HN). Useful as
a high-signal source for AI Devtools / Web & Frontend topics — almost no memes
or low-effort posts, score reflects real upvotes from a tech-only audience.

config (sources.yaml):
    connector: lobsters
    tag: programming          # optional — restrict to one tag (ai, programming, web, security, etc.)
    min_score: 10             # optional — drop stories below this score (default 0)
    limit: 20                 # optional — soft cap (default 25)

Notes:
- `hottest.json` returns ~25 stories sorted by hotness; `tag` switches to
  `/t/<tag>.json` for the same shape.
- No created-since filter on the server, so we filter client-side against
  the `since` arg passed to `fetch`.
"""

from __future__ import annotations

from datetime import datetime, timezone

import httpx

from .base import Connector
from ..models import Engagement, Post

BASE = "https://lobste.rs"


class LobstersConnector(Connector):
    platform = "lobsters"

    def __init__(self, cfg: dict | None = None) -> None:
        super().__init__(cfg)
        self._client = httpx.Client(
            timeout=float(self.cfg.get("timeout", 10.0)),
            headers={"User-Agent": "social-daily-report/0.1"},
            follow_redirects=True,
        )

    def fetch(self, since: datetime, limit: int = 25) -> list[Post]:
        tag = self.cfg.get("tag")
        min_score = int(self.cfg.get("min_score", 0))
        url = f"{BASE}/t/{tag}.json" if tag else f"{BASE}/hottest.json"

        data = self._client.get(url).json()
        now = datetime.now(timezone.utc)
        posts: list[Post] = []

        for item in data:
            created = _parse_iso(item.get("created_at"))
            if created is None or created < since:
                continue
            score = int(item.get("score", 0))
            if min_score and score < min_score:
                continue

            short_id = item.get("short_id") or ""
            title = item.get("title", "") or ""
            desc = item.get("description_plain") or ""
            text = f"{title}\n\n{desc}".strip() if desc else title

            # `/hottest.json` returns submitter_user as a dict {"username": ...};
            # `/t/<tag>.json` returns the username string directly. Handle both.
            sub_field = item.get("submitter_user")
            if isinstance(sub_field, dict):
                submitter = sub_field.get("username") or "unknown"
            elif isinstance(sub_field, str):
                submitter = sub_field or "unknown"
            else:
                submitter = "unknown"
            tags = item.get("tags") or []

            posts.append(
                Post(
                    id=f"lobsters:{short_id}",
                    platform=self.platform,
                    author=submitter,
                    text=text[:1500],
                    url=item.get("url") or item.get("comments_url") or f"{BASE}/s/{short_id}",
                    created_at=created,
                    fetched_at=now,
                    engagement=Engagement(
                        likes=score,
                        comments=int(item.get("comment_count", 0)),
                        score=float(score),
                    ),
                    raw={"short_id": short_id, "tags": tags, "comments_url": item.get("comments_url")},
                )
            )

        posts.sort(key=lambda p: p.engagement.score, reverse=True)
        return posts[:limit]

    def close(self) -> None:
        self._client.close()


def _parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
