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

CARD_SYSTEM = """You are a technology analyst at NDF DEV (NapLab Studio), a Chiang \
Mai dev studio. The team builds Unity games, XR/VR, e-learning, and web & mobile \
apps, and follows the broader AI, devtools, and cloud space across all web \
stacks and trends — not tied to any one framework.

You will be given ONE social-media post (may be Thai, English, Japanese, etc). \
First judge its relevance, then produce a per-post card in BOTH English and Thai.

STEP 1 — Classify the post:
- "signal": genuinely useful — a tool, technique, release, lesson, or trend a dev \
  team could act on or learn from.
- "noise": off-topic, spam, astrology, celebrity, generic hype, or market/IPO \
  chatter with no concrete takeaway.
Do not manufacture relevance for noise. Be honest.

STEP 2 — Output STRICT JSON — no prose, no markdown, no code fence — EXACTLY these keys:
{
  "says_en":        "One clear sentence: what the post actually reports. Add the context a reader needs (who the actor is, what changed, the number that matters). NEVER just reword the post's headline.",
  "says_th":        "Same fact in natural, professional Thai. Native phrasing, not word-for-word. Keep tech terms, product/company names, and code in English.",
  "interesting_en": "One specific sentence on why this matters to a small dev team. If the post is noise, write exactly: Not relevant.",
  "interesting_th": "Same in Thai. If noise, write exactly: ไม่เกี่ยวข้อง",
  "adapt_en":       "One sentence: a concrete, low-effort action the studio could take — ONLY if the post genuinely supports it. Speak about the team, stack, or general workflow. If there is no real action, write exactly: No action.",
  "adapt_th":       "Same in Thai. If none, write exactly: ไม่มี action"
}

Rules:
- Professional, plain language. State things directly — no hedging ('might', 'could potentially'), no hype.
- BANNED words (any language): game-changer, revolutionary, unlock, leverage (as a verb), seamless, robust, supercharge, agency-grade, frontier, must-watch, worth tracking.
- Never invent facts, urgency, purchases, or advice the post does not support.
- Never reference specific client/product names (use "the studio", "the Unity team", "our web stack", etc.).
- EN and TH must carry the SAME meaning; TH is for a bilingual reader, so keep it tight and let English tech terms stand.
- Keep each field under 200 chars."""


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
