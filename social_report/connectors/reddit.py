"""Reddit connector — public .json endpoints, no auth, free.

config (sources.yaml):
    connector: reddit
    subreddit: MachineLearning   # required
    query: "agents"              # optional — search within subreddit
    sort: top                    # top | hot | new (default: top)
    time: day                    # hour|day|week|month|year|all (default: day)
    min_score: 30                # optional — drop posts with score below this

Reddit rate-limits anonymous reads; a descriptive User-Agent is required.
"""

from __future__ import annotations

from datetime import datetime, timezone

import httpx

from .base import Connector
from ..models import Engagement, Post

BASE = "https://www.reddit.com"


def _reddit_media(d: dict) -> list[str]:
    """Pull a single representative image URL from a Reddit post.

    Covers image posts (direct + gallery), video posts (preview frame), and
    crossposts. Anything else (text, external links without preview) returns
    an empty list so the renderer falls through to non-thumb cards.
    """
    hint = d.get("post_hint")
    url = d.get("url")
    if hint == "image" and url:
        return [url]
    if hint == "hosted:video":
        preview = (
            (d.get("preview") or {})
            .get("images", [{}])[0]
            .get("source", {})
            .get("url")
        )
        if preview:
            return [preview.replace("&amp;", "&")]
    gallery = d.get("media_metadata") or {}
    for item in gallery.values():
        src = (item or {}).get("s") or {}
        candidate = src.get("u") or src.get("gif")
        if candidate:
            return [candidate.replace("&amp;", "&")]
    preview = (d.get("preview") or {}).get("images") or []
    if preview:
        src = preview[0].get("source", {}).get("url")
        if src:
            return [src.replace("&amp;", "&")]
    return []


class RedditConnector(Connector):
    platform = "reddit"

    def __init__(self, cfg: dict | None = None) -> None:
        super().__init__(cfg)
        self._client = httpx.Client(
            timeout=float(self.cfg.get("timeout", 10.0)),
            headers={"User-Agent": "social-daily-report/0.1 (by /u/social-daily-report)"},
            follow_redirects=True,
        )

    def fetch(self, since: datetime, limit: int = 30) -> list[Post]:
        sub = self.cfg.get("subreddit")
        if not sub:
            raise ValueError("reddit connector requires a `subreddit` in sources.yaml")

        sort = self.cfg.get("sort", "top")
        time = self.cfg.get("time", "day")
        query = self.cfg.get("query")
        min_score = int(self.cfg.get("min_score", 0))

        if query:
            url = f"{BASE}/r/{sub}/search.json"
            params = {"q": query, "restrict_sr": 1, "sort": sort, "t": time, "limit": min(limit, 100)}
        else:
            url = f"{BASE}/r/{sub}/{sort}.json"
            params = {"t": time, "limit": min(limit, 100)}

        data = self._client.get(url, params=params).json()
        now = datetime.now(timezone.utc)
        posts: list[Post] = []

        for child in data.get("data", {}).get("children", []):
            d = child.get("data", {})
            if d.get("stickied"):
                continue
            score = int(d.get("score", 0))
            if min_score and score < min_score:
                continue
            created = datetime.fromtimestamp(d.get("created_utc", 0), tz=timezone.utc)
            if created < since:
                continue

            title = d.get("title", "")
            body = d.get("selftext") or ""
            text = f"{title}\n\n{body}".strip() if body else title

            posts.append(
                Post(
                    id=f"reddit:{d.get('id')}",
                    platform=self.platform,
                    author=d.get("author", "unknown"),
                    text=text,
                    url=BASE + d.get("permalink", ""),
                    created_at=created,
                    fetched_at=now,
                    engagement=Engagement(
                        likes=d.get("ups", 0),
                        comments=d.get("num_comments", 0),
                        score=float(d.get("score", 0)),
                    ),
                    media=_reddit_media(d),
                    raw=d,
                )
            )
        return posts

    def close(self) -> None:
        self._client.close()
