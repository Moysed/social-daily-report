"""Normalize stage — light cleanup + low-signal filter before dedup.

Connectors already emit `Post`, so this is small: collapse whitespace, force UTC,
clamp the cross-platform score, drop empties and obvious junk.
"""

from __future__ import annotations

import re
from datetime import timezone

from .models import Post

_WS = re.compile(r"\s+")


def _clean_text(text: str) -> str:
    return _WS.sub(" ", text or "").strip()


def normalize(posts: list[Post], *, min_text_len: int = 8) -> list[Post]:
    out: list[Post] = []
    for p in posts:
        p.text = _clean_text(p.text)
        if len(p.text) < min_text_len or not p.url:
            continue
        if p.created_at.tzinfo is None:
            p.created_at = p.created_at.replace(tzinfo=timezone.utc)
        else:
            p.created_at = p.created_at.astimezone(timezone.utc)
        p.engagement.score = max(0.0, min(1.0, p.engagement.score))
        out.append(p)
    return out
