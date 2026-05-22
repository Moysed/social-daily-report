"""RSS / Atom connector — any public feed, no auth, free.

config (sources.yaml):
    connector: rss
    feed_url: "https://example.com/feed.xml"   # one feed
  or
    feeds: ["https://a.com/rss", "https://b.com/atom"]

Handles RSS 2.0 (<item>) and Atom (<entry>) via stdlib ElementTree —
no extra dependency. Engagement is unknown for feeds, so posts sort by recency.
"""

from __future__ import annotations

from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree as ET

import httpx

from .base import Connector
from ..models import Post

ATOM = "{http://www.w3.org/2005/Atom}"


class RSSConnector(Connector):
    platform = "rss"

    def __init__(self, cfg: dict | None = None) -> None:
        super().__init__(cfg)
        self._client = httpx.Client(
            timeout=float(self.cfg.get("timeout", 15.0)),
            headers={"User-Agent": "social-daily-report/0.1"},
            follow_redirects=True,
        )

    def _feeds(self) -> list[str]:
        if self.cfg.get("feeds"):
            return list(self.cfg["feeds"])
        if self.cfg.get("feed_url"):
            return [self.cfg["feed_url"]]
        raise ValueError("rss connector requires `feed_url` or `feeds` in sources.yaml")

    def fetch(self, since: datetime, limit: int = 30) -> list[Post]:
        posts: list[Post] = []
        for feed_url in self._feeds():
            try:
                xml = self._client.get(feed_url).text
                posts.extend(parse_feed(xml, self.platform, since))
            except (httpx.HTTPError, ET.ParseError):
                continue
        posts.sort(key=lambda p: p.created_at, reverse=True)
        return posts[:limit]

    def close(self) -> None:
        self._client.close()


def parse_feed(xml: str, platform: str, since: datetime) -> list[Post]:
    """Parse RSS 2.0 or Atom into Posts created at/after `since`."""
    root = ET.fromstring(xml)
    now = datetime.now(timezone.utc)
    posts: list[Post] = []

    # Atom: <feed><entry>... ; RSS: <rss><channel><item>...
    entries = root.findall(f".//{ATOM}entry") or root.findall(".//item")
    for e in entries:
        if e.tag.endswith("entry"):
            title = _text(e, f"{ATOM}title")
            link = _atom_link(e)
            created = _parse_date(_text(e, f"{ATOM}published") or _text(e, f"{ATOM}updated"))
            author = _text(e.find(f"{ATOM}author"), f"{ATOM}name") if e.find(f"{ATOM}author") is not None else ""
            summary = _text(e, f"{ATOM}summary") or _text(e, f"{ATOM}content")
            native_id = _text(e, f"{ATOM}id") or link
        else:
            title = _text(e, "title")
            link = _text(e, "link")
            created = _parse_date(_text(e, "pubDate"))
            author = _text(e, "{http://purl.org/dc/elements/1.1/}creator") or _text(e, "author")
            summary = _text(e, "description")
            native_id = _text(e, "guid") or link

        if created is None or created < since:
            continue

        text = title if not summary else f"{title}\n\n{_strip(summary)}".strip()
        posts.append(
            Post(
                id=f"{platform}:{native_id}",
                platform=platform,
                author=author or "unknown",
                text=text,
                url=link,
                created_at=created,
                fetched_at=now,
                raw={"feed_entry": True},
            )
        )
    return posts


def _text(node, tag: str) -> str:
    if node is None:
        return ""
    child = node.find(tag)
    return (child.text or "").strip() if child is not None and child.text else ""


def _atom_link(entry) -> str:
    for link in entry.findall(f"{ATOM}link"):
        if link.get("rel", "alternate") == "alternate" and link.get("href"):
            return link.get("href")
    link = entry.find(f"{ATOM}link")
    return link.get("href", "") if link is not None else ""


def _parse_date(value: str) -> datetime | None:
    if not value:
        return None
    try:  # RFC 822 (RSS pubDate)
        dt = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        try:  # ISO 8601 (Atom)
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def _strip(html: str, cap: int = 600) -> str:
    """Crude tag strip — feeds embed HTML; analysis only needs the gist."""
    out, depth = [], 0
    for ch in html:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth = max(0, depth - 1)
        elif depth == 0:
            out.append(ch)
    return "".join(out).strip()[:cap]
