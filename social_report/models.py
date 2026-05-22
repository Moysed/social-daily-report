"""Shared data schema. Every connector normalizes its platform into `Post`."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Engagement:
    likes: int = 0
    reposts: int = 0
    comments: int = 0
    score: float = 0.0  # normalized cross-platform 0..1 (optional)


@dataclass
class Post:
    id: str  # f"{platform}:{native_id}" — stable, used as dedup key
    platform: str  # bluesky | reddit | youtube | hackernews | rss | x
    author: str
    text: str
    url: str  # canonical link
    created_at: datetime  # UTC
    fetched_at: datetime  # UTC
    engagement: Engagement = field(default_factory=Engagement)
    author_followers: int | None = None
    media: list[str] = field(default_factory=list)
    lang: str | None = None
    topic_ids: list[str] = field(default_factory=list)
    raw: dict = field(default_factory=dict)
    also_on: list[str] = field(default_factory=list)  # other platforms same story appeared
    dup_count: int = 1  # how many raw posts collapsed into this one
