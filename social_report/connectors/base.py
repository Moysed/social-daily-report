"""Connector ABC — one implementation per platform, shared interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime

from ..models import Post


class Connector(ABC):
    platform: str

    def __init__(self, cfg: dict | None = None) -> None:
        # Per-source config from sources.yaml (query, subreddit, feed_url, ...).
        self.cfg: dict = cfg or {}

    @abstractmethod
    def fetch(self, since: datetime, limit: int = 30) -> list[Post]:
        """Return posts created at/after `since`, normalized to `Post`."""

    def close(self) -> None:
        """Optional cleanup (close HTTP clients, etc.)."""
