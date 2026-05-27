"""Orchestrate analysis for one topic: posts -> analysis dict (English)."""

from __future__ import annotations

import json
import logging
import re
import time

from .client import BaseLLM
from .prompts import ANALYSIS_SYSTEM, build_analysis_user
from ..models import Post

_log = logging.getLogger(__name__)

# Retries on malformed-JSON response (truncation / bad output).
_PARSE_MAX_ATTEMPTS = 3   # 1 initial + 2 retries
_PARSE_BACKOFFS = [1, 2]  # seconds before attempt 2, 3
# Bump max_tokens on retries in case the initial response was cut short.
_RETRY_MAX_TOKENS = 6000


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

    raw: str | None = None
    parsed: dict | None = None
    for attempt in range(1, _PARSE_MAX_ATTEMPTS + 1):
        max_tokens = 4000 if attempt == 1 else _RETRY_MAX_TOKENS
        raw = client.analyze(ANALYSIS_SYSTEM, user, max_tokens=max_tokens)
        parsed = _parse_json_lenient(raw)
        if parsed is not None:
            break
        if attempt < _PARSE_MAX_ATTEMPTS:
            _log.warning(
                "JSON parse failed (attempt %d/%d) for topic %r — retrying in %ds",
                attempt, _PARSE_MAX_ATTEMPTS,
                topic_cfg.get("title", "?"),
                _PARSE_BACKOFFS[attempt - 1],
            )
            time.sleep(_PARSE_BACKOFFS[attempt - 1])

    if parsed is None:
        _log.error(
            "All %d JSON parse attempts failed for topic %r; using stub",
            _PARSE_MAX_ATTEMPTS, topic_cfg.get("title", "?"),
        )
        data = _stub_analysis(topic_cfg, posts)
        data["what_happened"] = (
            f"LLM returned malformed JSON after {_PARSE_MAX_ATTEMPTS} attempts — see logs.\n\n"
            + (raw or "")[:1000]
        )
        data["why_it_matters"] = "Re-run this topic; the model output was truncated or malformed."
        return data

    # Merge parsed onto stub so missing keys (truncated output) still render cleanly.
    base = _stub_analysis(topic_cfg, posts)
    for k, v in parsed.items():
        if v not in (None, "", []):
            base[k] = v
    return base


def _parse_json_lenient(text: str) -> dict | None:
    """Try several extraction + repair strategies. Returns None if nothing parses."""
    for candidate in _json_candidates(text):
        try:
            obj = json.loads(candidate)
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError:
            continue
    return None


def _json_candidates(text: str) -> list[str]:
    t = text.strip()
    # Strip markdown code fence if present (```json ... ``` or ``` ... ```).
    if t.startswith("```"):
        parts = t.split("```")
        for part in parts[1::2]:
            inner = part.lstrip()
            if inner.lower().startswith("json"):
                inner = inner[4:].lstrip()
            inner = inner.strip().rstrip("`").strip()
            if inner.startswith("{"):
                t = inner
                break

    start = t.find("{")
    if start == -1:
        return []

    body = t[start:]
    candidates: list[str] = []

    # 1. Greedy: from first { to last } as-is.
    end = body.rfind("}")
    if end > 0:
        candidates.append(body[: end + 1])

    # 2. Same slice, but strip trailing commas before } or ].
    if end > 0:
        candidates.append(_strip_trailing_commas(body[: end + 1]))

    # 3. Truncation repair: balance open strings/brackets, then strip trailing commas.
    candidates.append(_strip_trailing_commas(_balance_json(body)))

    return candidates


def _balance_json(s: str) -> str:
    """Close any unterminated strings and unmatched { or [ to make `s` parseable."""
    stack: list[str] = []
    in_string = False
    escape = False
    last_complete_value_idx = -1  # index of last char that ended a top-level value safely

    for c in s:
        if escape:
            escape = False
            continue
        if in_string:
            if c == "\\":
                escape = True
            elif c == '"':
                in_string = False
            continue
        if c == '"':
            in_string = True
        elif c in "{[":
            stack.append(c)
        elif c in "}]":
            if stack:
                stack.pop()

    repaired = s
    if in_string:
        repaired += '"'
    while stack:
        opener = stack.pop()
        repaired += "}" if opener == "{" else "]"
    return repaired


_TRAILING_COMMA_RE = re.compile(r",(\s*[}\]])")


def _strip_trailing_commas(s: str) -> str:
    prev = None
    out = s
    while prev != out:
        prev = out
        out = _TRAILING_COMMA_RE.sub(r"\1", out)
    return out


def _stub_analysis(topic_cfg: dict, posts: list[Post]) -> dict:
    top = [p.text.split("\n", 1)[0][:120] for p in posts[:3]]
    return {
        "tldr": top or ["No posts fetched."],
        "what_happened": "STUB MODE — LLM disabled or no posts. Top items by engagement listed in Raw Sources.",
        "why_it_matters": "Set ANTHROPIC_API_KEY (or LLM_BACKEND=cli) to enable full reasoning.",
        "possibility": "",
        "org_applicability": "",
        "signals": [],
        "salience": 0.5 if posts else 0.0,
        "sentiment": "neutral",
        "confidence": 0.0,
        "tags": topic_cfg.get("tags", []),
    }
