"""Bluesky connector — public AppView searchPosts, no auth, free.

config (sources.yaml):
    connector: bluesky
    query: "ai agents"     # required — search terms
    sort: top              # top | latest (default: top)
"""

from __future__ import annotations

from datetime import datetime, timezone

import httpx

from .base import Connector
from ..models import Engagement, Post

# Public read-only AppView — no app password needed for search.
# (Use api.bsky.app, not public.api.bsky.app — the latter 403s behind some networks.)
SEARCH_URL = "https://api.bsky.app/xrpc/app.bsky.feed.searchPosts"
POST_LINK = "https://bsky.app/profile/{handle}/post/{rkey}"


class BlueskyConnector(Connector):
    platform = "bluesky"

    def __init__(self, cfg: dict | None = None) -> None:
        super().__init__(cfg)
        self._client = httpx.Client(
            timeout=float(self.cfg.get("timeout", 10.0)),
            headers={"User-Agent": "social-daily-report/0.1"},
        )

    def fetch(self, since: datetime, limit: int = 30) -> list[Post]:
        query = self.cfg.get("query")
        if not query:
            raise ValueError("bluesky connector requires a `query` in sources.yaml")

        params = {
            "q": query,
            "limit": min(limit, 100),
            "sort": self.cfg.get("sort", "top"),
        }
        data = self._client.get(SEARCH_URL, params=params).json()
        now = datetime.now(timezone.utc)
        posts: list[Post] = []

        for item in data.get("posts", []):
            record = item.get("record", {})
            created = _parse_iso(record.get("createdAt"))
            if created is None or created < since:
                continue

            author = item.get("author", {})
            handle = author.get("handle", "unknown")
            rkey = item.get("uri", "").rsplit("/", 1)[-1]

            posts.append(
                Post(
                    id=f"bluesky:{item.get('cid', rkey)}",
                    platform=self.platform,
                    author=handle,
                    text=record.get("text", ""),
                    url=POST_LINK.format(handle=handle, rkey=rkey),
                    created_at=created,
                    fetched_at=now,
                    engagement=Engagement(
                        likes=item.get("likeCount", 0),
                        reposts=item.get("repostCount", 0),
                        comments=item.get("replyCount", 0),
                        score=float(item.get("likeCount", 0)),
                    ),
                    author_followers=None,
                    media=_bluesky_media(item.get("embed") or {}),
                    lang=(record.get("langs") or [None])[0],
                    raw=item,
                )
            )
        return posts

    def close(self) -> None:
        self._client.close()


def _bluesky_media(embed: dict) -> list[str]:
    """Extract a thumbnail URL from a Bluesky embed view (images or external)."""
    images = embed.get("images") or []
    for img in images:
        url = img.get("thumb") or img.get("fullsize")
        if url:
            return [url]
    external = embed.get("external") or {}
    thumb = external.get("thumb")
    if thumb:
        return [thumb]
    # Record-with-media (quote-post wrapper): drill one level deeper.
    media = embed.get("media") or {}
    if media:
        return _bluesky_media(media)
    return []


def _parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
