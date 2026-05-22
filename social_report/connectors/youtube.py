"""YouTube connector — channel/playlist RSS feed, no API key, free.

config (sources.yaml):
    connector: youtube
    channel_id: "UCxxxxxxxxxxxxxxxxxxxxxx"   # one of these
    playlist_id: "PLxxxx"
    user: "somehandle"                        # legacy username feed

Uses the public Atom feed at youtube.com/feeds/videos.xml (no Data API key).
View counts come from <media:statistics> when present.
"""

from __future__ import annotations

from datetime import datetime, timezone
from xml.etree import ElementTree as ET

import httpx

from .base import Connector
from ..models import Engagement, Post
from .rss import _parse_date

ATOM = "{http://www.w3.org/2005/Atom}"
MEDIA = "{http://search.yahoo.com/mrss/}"
YT = "{http://www.youtube.com/xml/schemas/2015}"
FEED = "https://www.youtube.com/feeds/videos.xml"


class YouTubeConnector(Connector):
    platform = "youtube"

    def __init__(self, cfg: dict | None = None) -> None:
        super().__init__(cfg)
        self._client = httpx.Client(
            timeout=float(self.cfg.get("timeout", 15.0)),
            headers={"User-Agent": "social-daily-report/0.1"},
            follow_redirects=True,
        )

    def _feed_url(self) -> str:
        if self.cfg.get("channel_id"):
            return f"{FEED}?channel_id={self.cfg['channel_id']}"
        if self.cfg.get("playlist_id"):
            return f"{FEED}?playlist_id={self.cfg['playlist_id']}"
        if self.cfg.get("user"):
            return f"{FEED}?user={self.cfg['user']}"
        raise ValueError("youtube connector requires `channel_id`, `playlist_id`, or `user`")

    def fetch(self, since: datetime, limit: int = 30) -> list[Post]:
        xml = self._client.get(self._feed_url()).text
        root = ET.fromstring(xml)
        now = datetime.now(timezone.utc)
        posts: list[Post] = []

        for e in root.findall(f"{ATOM}entry"):
            created = _parse_date(_text(e, f"{ATOM}published"))
            if created is None or created < since:
                continue

            video_id = _text(e, f"{YT}videoId")
            link_el = e.find(f"{ATOM}link")
            url = link_el.get("href") if link_el is not None else f"https://www.youtube.com/watch?v={video_id}"
            author_el = e.find(f"{ATOM}author")
            author = _text(author_el, f"{ATOM}name") if author_el is not None else "unknown"

            group = e.find(f"{MEDIA}group")
            desc = _text(group, f"{MEDIA}description") if group is not None else ""
            title = _text(e, f"{ATOM}title")
            text = f"{title}\n\n{desc}".strip() if desc else title

            views = 0
            if group is not None:
                stats = group.find(f"{MEDIA}community/{MEDIA}statistics")
                if stats is not None:
                    views = int(stats.get("views", 0) or 0)

            posts.append(
                Post(
                    id=f"youtube:{video_id}",
                    platform=self.platform,
                    author=author,
                    text=text[:1200],
                    url=url,
                    created_at=created,
                    fetched_at=now,
                    engagement=Engagement(likes=views, score=float(views)),
                    media=[url],
                    raw={"video_id": video_id, "views": views},
                )
            )
        posts.sort(key=lambda p: p.engagement.score, reverse=True)
        return posts[:limit]

    def close(self) -> None:
        self._client.close()


def _text(node, tag: str) -> str:
    if node is None:
        return ""
    child = node.find(tag)
    return (child.text or "").strip() if child is not None and child.text else ""
