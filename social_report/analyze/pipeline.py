"""Orchestrate analysis for one topic: posts -> analysis dict (English)."""

from __future__ import annotations

import json

from .client import BaseLLM
from .prompts import ANALYSIS_SYSTEM, build_analysis_user
from ..models import Post


def analyze_topic(
    client: BaseLLM,
    topic_cfg: dict,
    date_label: str,
    posts: list[Post],
) -> dict:
    if not client.enabled or not posts:
        return _stub_analysis(topic_cfg, posts)

    user = build_analysis_user(
        topic_cfg.get("title", "Topic"),
        topic_cfg.get("focus", ""),
        date_label,
        posts,
    )
    raw = client.analyze(ANALYSIS_SYSTEM, user)
    try:
        return _parse_json(raw)
    except (ValueError, json.JSONDecodeError):
        data = _stub_analysis(topic_cfg, posts)
        data["what_happened"] = "Model output was not valid JSON. Falling back to stub.\n\n" + raw[:1000]
        return data


def _parse_json(text: str) -> dict:
    t = text.strip()
    if t.startswith("```"):
        t = t.split("```", 2)[1]
        t = t[4:] if t.lower().startswith("json") else t
    start, end = t.find("{"), t.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("no JSON object found")
    return json.loads(t[start : end + 1])


def _stub_analysis(topic_cfg: dict, posts: list[Post]) -> dict:
    top = [p.text.split("\n", 1)[0][:120] for p in posts[:3]]
    return {
        "tldr": top or ["No posts fetched."],
        "what_happened": "STUB MODE (no ANTHROPIC_API_KEY). Top items by engagement listed in Raw Sources.",
        "why_it_matters": "Set ANTHROPIC_API_KEY to enable Opus reasoning.",
        "possibility": "",
        "org_applicability": "",
        "signals": [],
        "salience": 0.5 if posts else 0.0,
        "sentiment": "neutral",
        "confidence": 0.0,
        "tags": topic_cfg.get("tags", []),
    }
