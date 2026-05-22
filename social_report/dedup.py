"""Dedup stage -- collapse the same story seen across platforms.

Three passes, cheapest first:
  1. exact id (stable connector key)
  2. canonical URL (same article posted to HN + Reddit + RSS)
  3. near-duplicate title (fuzzy, catches reposts/quotes of one story)

Within a cluster the highest-engagement post wins; the rest are recorded in
`also_on` and counted in `dup_count`, so signal ("3 platforms carried this")
survives without keeping the duplicate rows.

Ported from the ψ/lab build, 2026-05-21.
"""

from __future__ import annotations

import re
from difflib import SequenceMatcher
from urllib.parse import urlsplit, urlunsplit

from .models import Post

_TRACKING = re.compile(r"^(utm_|ref$|ref_|fbclid|gclid|igshid|si$|s$|t$)", re.I)
_NONWORD = re.compile(r"[^a-z0-9ก-๙]+")


def canonical_url(url: str) -> str:
    try:
        s = urlsplit(url.strip())
    except ValueError:
        return url.strip().lower()
    host = s.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    query = "&".join(
        q for q in s.query.split("&") if q and not _TRACKING.match(q.split("=", 1)[0])
    )
    path = s.path.rstrip("/") or "/"
    return urlunsplit((s.scheme.lower() or "https", host, path, query, ""))


def _title_key(text: str) -> str:
    return _NONWORD.sub(" ", text.lower()).strip()


def _merge(primary: Post, dup: Post) -> None:
    primary.dup_count += dup.dup_count
    for plat in [dup.platform, *dup.also_on]:
        if plat != primary.platform and plat not in primary.also_on:
            primary.also_on.append(plat)


def _pick(a: Post, b: Post) -> tuple[Post, Post]:
    """Return (winner, loser) by engagement score, tie-break on likes."""
    if (a.engagement.score, a.engagement.likes) >= (b.engagement.score, b.engagement.likes):
        return a, b
    return b, a


def dedup(posts: list[Post], *, title_threshold: float = 0.86) -> list[Post]:
    # pass 1: exact id
    by_id: dict[str, Post] = {}
    for p in posts:
        if p.id in by_id:
            w, l = _pick(by_id[p.id], p)
            _merge(w, l)
            by_id[p.id] = w
        else:
            by_id[p.id] = p

    # pass 2: canonical URL
    by_url: dict[str, Post] = {}
    for p in by_id.values():
        key = canonical_url(p.url)
        if key in by_url:
            w, l = _pick(by_url[key], p)
            _merge(w, l)
            by_url[key] = w
        else:
            by_url[key] = p

    # pass 3: fuzzy title against kept cluster representatives
    kept: list[Post] = []
    keys: list[str] = []
    for p in sorted(by_url.values(), key=lambda x: x.engagement.score, reverse=True):
        k = _title_key(p.text)
        match = None
        for i, ek in enumerate(keys):
            if abs(len(ek) - len(k)) > max(len(ek), len(k)) * 0.5:
                continue  # length gate -- skip obvious non-matches before ratio
            if SequenceMatcher(None, ek, k).ratio() >= title_threshold:
                match = i
                break
        if match is None:
            kept.append(p)
            keys.append(k)
        else:
            _merge(kept[match], p)  # representative already higher-scored (sorted)
    return kept
