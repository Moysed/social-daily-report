"""Radar connector — free trending signal via Xquik /api/v1/radar.

Pulls curated trending items from github, hacker_news, reddit, polymarket,
google_trends, wikipedia, trustmrr. Free endpoint — no credit cost.

config (sources.yaml):
    connector: radar
    source: github                # optional — github | hacker_news | reddit |
                                  # polymarket | google_trends | wikipedia | trustmrr
    category: tech                # optional — general | tech | dev | science |
                                  # culture | politics | business | entertainment
    region: global                # optional — US | GB | TH | global (default)
    hours: 24                     # optional — 1..72; lookback window
    limit: 25                     # see also Connector.fetch(limit=...)

env:
    XQUIK_API_KEY     required — same key as the x connector.

Value vs. existing connectors:
    github + polymarket + google_trends + wikipedia are sources we don't have
    elsewhere. hacker_news overlaps with the hackernews connector — prefer
    that one for HN-specific topics.
"""

from __future__ import annotations

import os
import time
from datetime import datetime, timezone

import httpx

from .base import Connector
from ..models import Engagement, Post

BASE = "https://xquik.com/api/v1"
RADAR_PATH = "/radar"

_RETRY_STATUSES = {408, 429, 500, 502, 503, 504}


def _parse_radar_ts(ts) -> datetime | None:
    if ts is None:
        return None
    if isinstance(ts, (int, float)):
        return datetime.fromtimestamp(int(ts), tz=timezone.utc)
    if isinstance(ts, str):
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None


class RadarConnector(Connector):
    platform = "radar"

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
        if not self.api_key:
            raise RuntimeError("XQUIK_API_KEY is not set; cannot call radar via Xquik")

        per_call = max(1, min(int(limit), 100))
        params: dict = {"limit": per_call}
        for key in ("source", "category", "region"):
            val = self.cfg.get(key)
            if val:
                params[key] = val
        hours = self.cfg.get("hours")
        if hours:
            params["hours"] = int(hours)

        max_attempts = int(os.environ.get("XQUIK_MAX_ATTEMPTS", "3"))
        backoff = float(os.environ.get("XQUIK_RETRY_BACKOFF", "1.5"))

        for attempt in range(1, max_attempts + 1):
            resp = self._client.get(BASE + RADAR_PATH, params=params)
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

        for item in data.get("items", []) or []:
            iid = item.get("id") or item.get("sourceId") or item.get("source_id")
            if not iid:
                continue
            # Raw API returns ISO strings (publishedAt); MCP-normalized contract
            # returns unix seconds (published_at). Handle both.
            ts = (
                item.get("published_at")
                or item.get("publishedAt")
                or item.get("created")
                or item.get("createdAt")
            )
            created = _parse_radar_ts(ts)
            if created is None or created < since:
                continue

            source = item.get("source") or "radar"
            title = (item.get("title") or "").strip()
            desc = (item.get("description") or "").strip()
            text = f"{title}\n\n{desc}".strip() if desc else title
            if not text:
                continue

            meta = item.get("metadata") or {}
            source_id = item.get("sourceId") or item.get("source_id") or ""
            author = (
                meta.get("author")
                or source_id.split("_", 1)[-1]
                or source
            )

            score = float(item.get("score") or 0)
            likes = int(
                meta.get("points")
                or meta.get("starsToday")
                or meta.get("stars_today")
                or score
            )
            comments = int(meta.get("numberComments") or meta.get("number_comments") or 0)
            image = item.get("imageUrl") or item.get("image_url")

            posts.append(
                Post(
                    id=f"radar:{iid}",
                    platform=self.platform,
                    author=author,
                    text=text,
                    url=item.get("url") or "",
                    created_at=created,
                    fetched_at=now,
                    engagement=Engagement(
                        likes=likes,
                        comments=comments,
                        score=score,
                    ),
                    media=[image] if image else [],
                    lang=item.get("language"),
                    raw=item,
                )
            )
        return posts

    def close(self) -> None:
        self._client.close()
