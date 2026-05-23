"""Per-post card generation.

For each post chosen to appear in the "Top Posts" section, ask the LLM for a
3-field summary (what it says, what's interesting, how NDF DEV could adapt it),
in both English and Thai. One JSON call per post, parallel across posts.

Cached on Post.id within a single CLI run to keep partial-topic re-renders
idempotent without DB plumbing.
"""

from __future__ import annotations

import concurrent.futures as cf
import json
import re
from typing import Iterable

from ..models import Post

CARD_SYSTEM = """You are a tech analyst at NDF DEV (NapLab Studio), a Chiang Mai \
dev studio. Stack: Unity games, XR/VR, e-learning, Next.js + Supabase web apps.

You will be given ONE social-media post (may be Thai, English, Japanese, etc). \
Read it and produce a per-post card in BOTH English and Thai.

Output STRICT JSON — no prose, no markdown, no code fence — with EXACTLY these keys:
{
  "says_en":        "1 sentence, plain English. What the post is actually about. Translate if needed.",
  "says_th":        "Same content in natural Thai. Keep tech terms in English.",
  "interesting_en": "1 sentence. Why this matters to a small dev team. Be specific, not generic.",
  "interesting_th": "Same in Thai.",
  "adapt_en":       "1-2 sentences. How NDF DEV (the studio) could adopt or learn from this — speak about the team, stack, or general workflow. Do NOT name specific client projects or product names. If not applicable, say 'Not directly applicable.' honestly.",
  "adapt_th":       "Same in Thai."
}

Rules:
- Be concrete. No hedging, no 'might consider', no 'could potentially'.
- Never reference specific client/product names (use "the studio", "the Unity team", "our web stack", etc.).
- If the post is noise / off-topic / spam: still produce honest fields. Use 'Not directly applicable.' for adapt.
- Never invent facts not in the post.
- Keep each field under 220 chars."""


def _build_user(topic_title: str, post: Post) -> str:
    return (
        f"Topic: {topic_title}\n"
        f"Platform: {post.platform}\n"
        f"Author: @{post.author}\n"
        f"Engagement: {post.engagement.likes} likes / {post.engagement.comments} comments\n"
        f"URL: {post.url}\n"
        f"---\n"
        f"{post.text[:1200]}\n"
        f"---\n"
        f"Produce the JSON card now."
    )


_JSON_FENCE = re.compile(r"```(?:json)?\s*([\s\S]*?)\s*```", re.IGNORECASE)


def _parse(raw: str) -> dict:
    raw = raw.strip()
    m = _JSON_FENCE.search(raw)
    if m:
        raw = m.group(1).strip()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # try first {...} block
        start = raw.find("{")
        end = raw.rfind("}")
        if start >= 0 and end > start:
            try:
                data = json.loads(raw[start : end + 1])
            except json.JSONDecodeError:
                return {}
        else:
            return {}
    if not isinstance(data, dict):
        return {}
    return data


def _empty_card(post: Post) -> dict:
    text = (post.text or "").strip().split("\n", 1)[0][:140]
    return {
        "says_en": text or "(no text)",
        "says_th": text or "(ไม่มีข้อความ)",
        "interesting_en": "",
        "interesting_th": "",
        "adapt_en": "",
        "adapt_th": "",
    }


def _analyze_one(client, topic_title: str, post: Post) -> dict:
    """Single-post LLM call. On any failure, return a minimal fallback card."""
    if not client or not getattr(client, "enabled", False):
        return _empty_card(post)
    try:
        raw = client._translate(CARD_SYSTEM, _build_user(topic_title, post), 800)  # noqa: SLF001
    except Exception:
        return _empty_card(post)
    data = _parse(raw)
    if not data:
        return _empty_card(post)
    # Backfill any missing keys
    fallback = _empty_card(post)
    return {k: (data.get(k) or fallback[k]) for k in fallback.keys()}


def analyze_top_posts(
    client,
    topic_title: str,
    posts: Iterable[Post],
    *,
    max_workers: int = 4,
) -> dict[str, dict]:
    """Return {post.id: card_dict} for the given posts, generated in parallel.

    `posts` should already be filtered to the picked set (typically ≤ 8).
    """
    picks = list(posts)
    if not picks:
        return {}
    out: dict[str, dict] = {}
    workers = min(max_workers, len(picks))
    with cf.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_analyze_one, client, topic_title, p): p for p in picks}
        for fut in cf.as_completed(futures):
            p = futures[fut]
            try:
                out[p.id] = fut.result()
            except Exception:
                out[p.id] = _empty_card(p)
    return out
