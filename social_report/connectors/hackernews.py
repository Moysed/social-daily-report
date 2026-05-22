"""HackerNews connector — official Firebase API, no auth, free."""

from __future__ import annotations

from datetime import datetime, timezone

import httpx

from .base import Connector
from ..models import Engagement, Post

HN_BASE = "https://hacker-news.firebaseio.com/v0"
HN_ITEM_LINK = "https://news.ycombinator.com/item?id={id}"


class HackerNewsConnector(Connector):
    platform = "hackernews"

    def __init__(self, cfg: dict | None = None) -> None:
        super().__init__(cfg)
        timeout = float(self.cfg.get("timeout", 10.0))
        self._client = httpx.Client(timeout=timeout, headers={"User-Agent": "social-daily-report/0.1"})

    def fetch(self, since: datetime, limit: int = 30) -> list[Post]:
        ids = self._client.get(f"{HN_BASE}/topstories.json").json()[:limit]
        now = datetime.now(timezone.utc)
        posts: list[Post] = []

        for story_id in ids:
            item = self._client.get(f"{HN_BASE}/item/{story_id}.json").json()
            if not item or item.get("type") != "story":
                continue
            created = datetime.fromtimestamp(item.get("time", 0), tz=timezone.utc)
            if created < since:
                continue

            title = item.get("title", "")
            extra = item.get("text") or ""
            text = f"{title}\n\n{extra}".strip() if extra else title

            posts.append(
                Post(
                    id=f"hackernews:{item['id']}",
                    platform=self.platform,
                    author=item.get("by", "unknown"),
                    text=text,
                    url=item.get("url") or HN_ITEM_LINK.format(id=item["id"]),
                    created_at=created,
                    fetched_at=now,
                    engagement=Engagement(
                        likes=item.get("score", 0),
                        comments=item.get("descendants", 0),
                        score=float(item.get("score", 0)),
                    ),
                    raw=item,
                )
            )
        return posts

    def close(self) -> None:
        self._client.close()
