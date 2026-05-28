"""X (Twitter) connector via Xquik — paid, keyed.

Xquik is a Twitter/X scraper API charging ~$0.00015 per tweet returned (1 credit
per tweet). Auth is a simple `x-api-key` header. See https://docs.xquik.com.

config (sources.yaml):
    connector: x
    query: "ai agents lang:en min_faves:50"  # required — supports X search operators
    query_type: Latest                       # Latest (default) | Top
    language: en                             # optional — ISO code; overrides q's lang:
    min_faves: 5                             # optional — engagement gate at source
    verified_only: false                     # optional
    media_type: ""                           # optional — images|videos|gifs|media|links|none
    limit: 50                                # see also Connector.fetch(limit=...)

env:
    XQUIK_API_KEY     required at runtime; safe to leave unset for dry-runs

cost gating:
    Every tweet returned costs 1 credit. The connector caps the request `limit` at
    `XQUIK_MAX_PER_CALL` (default 200, the API hard cap) so a misconfigured topic
    can't burn credits. For larger daily windows, paginate via `cursor` — currently
    capped at one page per call to keep cost predictable.
"""

from __future__ import annotations

import os
import time
from datetime import datetime, timezone

import httpx

from .base import Connector
from ..models import Engagement, Post

BASE = "https://xquik.com/api/v1"
SEARCH_PATH = "/x/tweets/search"

_RETRY_STATUSES = {408, 429, 500, 502, 503, 504}

# Xquik returns createdAt in Twitter's classic v1.1 format
# (e.g. "Fri May 22 03:38:44 +0000 2026") despite docs hinting at ISO 8601.
# We try ISO first to stay forward-compatible, then fall back to the classic form.
_TWITTER_DT_FMT = "%a %b %d %H:%M:%S %z %Y"


def _parse_x_datetime(s: str) -> datetime | None:
    if not s:
        return None
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (TypeError, ValueError):
        pass
    try:
        return datetime.strptime(s, _TWITTER_DT_FMT)
    except (TypeError, ValueError):
        return None


class XConnector(Connector):
    platform = "x"

    def __init__(self, cfg: dict | None = None) -> None:
        super().__init__(cfg)
        self.api_key = os.environ.get("XQUIK_API_KEY", "").strip()
        self._client = httpx.Client(
            timeout=float(self.cfg.get("timeout", 15.0)),
            headers={
                "x-api-key": self.api_key,
                "Accept": "application/json",
                "User-Agent": "social-daily-report/0.1",
            },
        )

    def fetch(self, since: datetime, limit: int = 30) -> list[Post]:
        query = self.cfg.get("query")
        if not query:
            raise ValueError("x connector requires a `query` in sources.yaml")
        if not self.api_key:
            # Surface this cleanly so the CLI can mark the source failed but
            # keep the topic running on other connectors.
            raise RuntimeError("XQUIK_API_KEY is not set; cannot call x.com via Xquik")

        hard_cap = int(os.environ.get("XQUIK_MAX_PER_CALL", "200"))
        per_call = max(1, min(int(limit), hard_cap))

        params: dict = {
            "q": query,
            "limit": per_call,
            "queryType": self.cfg.get("query_type", "Latest"),
            "sinceTime": since.date().isoformat(),
        }
        for key, src_key in (
            ("language", "language"),
            ("minFaves", "min_faves"),
            ("minRetweets", "min_retweets"),
            ("minReplies", "min_replies"),
            ("mediaType", "media_type"),
            ("verifiedOnly", "verified_only"),
            ("fromUser", "from_user"),
            ("toUser", "to_user"),
            ("mentioning", "mentioning"),
        ):
            val = self.cfg.get(src_key)
            if val not in (None, "", False):
                params[key] = val

        max_attempts = int(os.environ.get("XQUIK_MAX_ATTEMPTS", "3"))
        backoff = float(os.environ.get("XQUIK_RETRY_BACKOFF", "1.5"))

        for attempt in range(1, max_attempts + 1):
            resp = self._client.get(BASE + SEARCH_PATH, params=params)
            if resp.status_code == 401:
                raise RuntimeError("Xquik auth failed (401) — check XQUIK_API_KEY")
            if resp.status_code in _RETRY_STATUSES and attempt < max_attempts:
                time.sleep(backoff * attempt)
                continue
            break

        if resp.status_code == 429:
            raise RuntimeError("Xquik rate-limited (429) — back off and retry")
        resp.raise_for_status()
        data = resp.json()

        now = datetime.now(timezone.utc)
        posts: list[Post] = []
        lang_default = self.cfg.get("language")

        for t in data.get("tweets", []) or []:
            post = parse_xquik_tweet(t, since=since, now=now, platform=self.platform, lang_default=lang_default)
            if post is not None:
                posts.append(post)
        return posts

    def close(self) -> None:
        self._client.close()


def parse_xquik_tweet(
    t: dict,
    *,
    since: datetime,
    now: datetime,
    platform: str = "x",
    lang_default: str | None = None,
) -> Post | None:
    """Convert one Xquik tweet dict to a normalized Post. Returns None if invalid or stale."""
    tid = t.get("id")
    if not tid:
        return None
    created = _parse_x_datetime(t.get("createdAt") or t.get("created_at"))
    if created is None or created < since:
        return None

    author = t.get("author") or {}
    handle = author.get("username") or author.get("name") or "unknown"
    text = (t.get("text") or "").strip()
    if not text:
        return None

    url = t.get("url") or f"https://x.com/{handle}/status/{tid}"

    return Post(
        id=f"x:{tid}",
        platform=platform,
        author=handle,
        text=text,
        url=url,
        created_at=created,
        fetched_at=now,
        engagement=Engagement(
            likes=int(t.get("likeCount") or 0),
            reposts=int(t.get("retweetCount") or 0),
            comments=int(t.get("replyCount") or 0),
            score=float(t.get("likeCount") or 0),
        ),
        author_followers=author.get("followers"),
        media=[
            m.get("media_url_https") or m.get("mediaUrl") or m.get("url")
            for m in (t.get("media") or [])
            if (m.get("media_url_https") or m.get("mediaUrl") or m.get("url"))
        ],
        lang=t.get("lang") or lang_default,
        raw=t,
    )
