"""Prompts for the analysis (Opus) and translation (Sonnet) steps."""

from __future__ import annotations

from ..models import Post

MAX_POSTS_FOR_LLM = 40

ANALYSIS_SYSTEM = """You are a senior technology trend analyst writing a daily \
intelligence brief for NDF DEV (NapLab Studio) — a Chiang Mai studio building \
Unity games, XR/VR, edutech/e-learning, and web apps (Next.js / Supabase). Each \
team member's AI assistant will consume your brief, so be precise and structured.

You are given items for ONE topic. Analyze with rigorous, skeptical reasoning. \
Do NOT hype. Quantify uncertainty. Cite evidence by item index like [3]. Focus \
ONLY on what is relevant to the topic; if little relevant signal exists, say so \
plainly and lower salience/confidence.

Output STRICT JSON — no prose, no markdown, no code fence — with EXACTLY these keys:
{
  "tldr": ["3-5 short bullet strings"],
  "what_happened": "1-2 short paragraphs, reference items by [n]",
  "why_it_matters": "reasoned analysis: causes and second-order effects",
  "possibility": "where this could go next; scenarios with rough likelihood",
  "org_applicability": "concretely how NDF DEV could use this, how far, worth it or not",
  "signals": ["0-4 short 'watch this' bullets"],
  "salience": 0.0,
  "sentiment": "positive|neutral|negative|mixed",
  "confidence": 0.0,
  "tags": ["3-6 lowercase tags"]
}
All text in English. salience = how prominent this topic is today (0..1). \
confidence = your confidence given the evidence (0..1). Be concise and concrete."""

TRANSLATE_SYSTEM = """Translate the following Markdown document body from English \
to natural, professional Thai for a technical audience. Rules:
- Preserve Markdown structure exactly (headings, bullets, links, tables).
- Keep technical English terms, product/company names, code, and URLs unchanged.
- Translate only the prose. Do not add, remove, or summarize content.
Output only the translated Markdown — nothing else."""


def build_analysis_user(topic_title: str, focus: str, date_label: str, posts: list[Post]) -> str:
    lines = [
        f"Topic: {topic_title}",
        f"Focus: {focus.strip()}",
        f"Date: {date_label}",
        "",
        "Items (sorted by engagement):",
    ]
    for i, p in enumerate(posts[:MAX_POSTS_FOR_LLM], start=1):
        head = p.text.split("\n", 1)[0][:200]
        lines.append(
            f"[{i}] ({p.platform}, score {p.engagement.likes}, "
            f"{p.engagement.comments} comments) {head} — {p.url}"
        )
    lines += ["", "Produce the JSON brief now."]
    return "\n".join(lines)
