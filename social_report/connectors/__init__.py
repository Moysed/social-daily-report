from .base import Connector
from .bluesky import BlueskyConnector
from .hackernews import HackerNewsConnector
from .reddit import RedditConnector
from .rss import RSSConnector
from .x import XConnector
from .youtube import YouTubeConnector

# Registry — map config `connector:` keys to classes.
REGISTRY: dict[str, type[Connector]] = {
    "hackernews": HackerNewsConnector,
    "bluesky": BlueskyConnector,
    "reddit": RedditConnector,
    "youtube": YouTubeConnector,
    "rss": RSSConnector,
    "x": XConnector,
}


def make_connector(name: str, cfg: dict | None = None) -> Connector:
    try:
        return REGISTRY[name](cfg)
    except KeyError as exc:
        raise ValueError(
            f"Unknown connector '{name}'. Available: {sorted(REGISTRY)}"
        ) from exc
