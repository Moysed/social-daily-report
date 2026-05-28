"""X List connector — pull tweets from a curated X (Twitter) List by ID.

Root-cause fix for keyword-noise topics (e.g. thai-tech where bare "Typhoon"
pulled Eurofighter + storm + K-drama). Curate the list once on x.com, then
this connector fetches only those handles — zero keyword collisions.

config (sources.yaml):
    connector: x_list
    list_id: "1234567890"            # required — numeric X List ID
    include_replies: false           # optional — default false
    limit: 40                        # see also Connector.fetch(limit=...)

setup:
    1. Create a List at https://x.com/i/lists/create (public or private)
    2. Add Thai-tech handles: @scb_10x, @PathummaLLM, @nectec_th, etc.
    3. Open the list page; the numeric ID is in the URL: /i/lists/<id>
    4. Paste that <id> into sources.yaml under `list_id:`

cost:
    1 credit per tweet returned (~20 per page). Capped at XQUIK_MAX_PER_CALL.

env:
    XQUIK_API_KEY     required — same key as the x connector.
"""

from __future__ import annotations

import os
import time
from datetime import datetime, timezone

import httpx

from .base import Connector
from ..models import Post
from .x import parse_xquik_tweet

BASE = "https://xquik.com/api/v1"

# Transient statuses we'll retry. 404 included because Xquik's list cache
# occasionally cold-misses and reports "not found" for a live list (observed
# 2026-05-28 — list returned 20 tweets on retry seconds later).
_RETRY_STATUSES = {404, 408, 429, 500, 502, 503, 504}


class XListConnector(Connector):
    platform = "x"  # Posts share the x: id namespace — let dedup work across sources.

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
        list_id = self.cfg.get("list_id")
        if not list_id:
            raise ValueError("x_list connector requires `list_id` in sources.yaml")
        if not self.api_key:
            raise RuntimeError("XQUIK_API_KEY is not set; cannot call x_list via Xquik")

        hard_cap = int(os.environ.get("XQUIK_MAX_PER_CALL", "200"))
        per_call = max(1, min(int(limit), hard_cap))

        params: dict = {
            "sinceTime": int(since.timestamp()),
        }
        if self.cfg.get("include_replies"):
            params["includeReplies"] = True

        path = f"/x/lists/{list_id}/tweets"
        now = datetime.now(timezone.utc)
        posts: list[Post] = []
        cursor: str | None = None
        fetched = 0

        max_attempts = int(os.environ.get("XQUIK_MAX_ATTEMPTS", "3"))
        backoff = float(os.environ.get("XQUIK_RETRY_BACKOFF", "1.5"))

        # Lists return ~20 per page; paginate up to per_call total.
        while fetched < per_call:
            page_params = dict(params)
            if cursor:
                page_params["cursor"] = cursor

            resp = None
            for attempt in range(1, max_attempts + 1):
                resp = self._client.get(BASE + path, params=page_params)
                if resp.status_code == 401:
                    raise RuntimeError("Xquik auth failed (401) — check XQUIK_API_KEY")
                if resp.status_code in _RETRY_STATUSES and attempt < max_attempts:
                    time.sleep(backoff * attempt)
                    continue
                break

            if resp.status_code == 404:
                raise RuntimeError(
                    f"Xquik list {list_id} not found after {max_attempts} attempts (404)"
                )
            if resp.status_code == 429:
                raise RuntimeError("Xquik rate-limited (429) — back off and retry")
            resp.raise_for_status()
            data = resp.json()

            page_tweets = data.get("tweets", []) or []
            if not page_tweets:
                break
            for t in page_tweets:
                post = parse_xquik_tweet(t, since=since, now=now, platform=self.platform)
                if post is not None:
                    posts.append(post)
            fetched += len(page_tweets)
            cursor = data.get("nextCursor") or data.get("next_cursor")
            if not cursor or not data.get("hasMore", data.get("has_more")):
                break
        return posts

    def close(self) -> None:
        self._client.close()
