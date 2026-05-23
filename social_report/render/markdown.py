"""Render analysis + posts into bilingual per-topic Markdown (see arch doc §6)."""

from __future__ import annotations

from datetime import datetime, timezone

import yaml

from ..models import Post

GENERATOR = "social-daily-report v0.1"


def build_body(analysis: dict, posts: list[Post], date_label: str, topic_title: str) -> str:
    out: list[str] = [f"# {topic_title} — {date_label}\n"]

    out.append("## TL;DR")
    out += [f"- {b}" for b in analysis.get("tldr", [])] or ["- (none)"]

    for heading, key in (
        ("What happened", "what_happened"),
        ("Why it matters (reasoning)", "why_it_matters"),
        ("Possibility", "possibility"),
        ("Org applicability — NDF DEV", "org_applicability"),
    ):
        value = (analysis.get(key) or "").strip()
        if value:
            out += [f"\n## {heading}", value]

    signals = analysis.get("signals", [])
    if signals:
        out.append("\n## Signals to Watch")
        out += [f"- {s}" for s in signals]

    repos = _github_repos(posts)
    if repos:
        out.append("\n## Repos & Tools to Try")
        out += ["| repo | source | url |", "|---|---|---|"]
        for slug, source, url, title in repos[:12]:
            out.append(f"| **{slug}** — {title} | {source} | <{url}> |")

    out.append("\n## Raw Sources")
    out += ["| platform | author | engagement | url |", "|---|---|---|---|"]
    for p in posts[:30]:
        title = p.text.split("\n", 1)[0][:80].replace("|", "/")
        eng = f"^{p.engagement.likes} c{p.engagement.comments}"
        out.append(f"| {p.platform} | {p.author} | {eng} | [{title}]({p.url}) |")

    return "\n".join(out) + "\n"


_GITHUB_REPO_PATTERN = __import__("re").compile(
    r"https?://github\.com/([\w.-]+)/([\w.-]+?)(?:/(?:tree|blob|releases|issues|pull|actions|wiki)/|\?|#|/?$)",
)
# Subpaths to skip (we want the repo root, not an issue/PR view).
_GITHUB_SKIP_PARTS = {"issues", "pull", "actions", "blob", "tree", "releases", "wiki", "discussions"}


def _github_repos(posts: list[Post]) -> list[tuple[str, str, str, str]]:
    """Extract (owner/repo, source, root_url, title) for posts that point at
    GitHub repos. De-dups by owner/repo, keeps first-seen ordering (which is
    salience/engagement order after dedup)."""
    out: list[tuple[str, str, str, str]] = []
    seen: set[str] = set()
    for p in posts:
        url = p.url or ""
        if "github.com/" not in url:
            continue
        m = _GITHUB_REPO_PATTERN.search(url)
        if not m:
            continue
        owner, repo = m.group(1), m.group(2)
        if owner in _GITHUB_SKIP_PARTS or repo in _GITHUB_SKIP_PARTS:
            continue
        slug = f"{owner}/{repo}"
        if slug in seen:
            continue
        seen.add(slug)
        root = f"https://github.com/{owner}/{repo}"
        # The GitHub Trending RSS title is literally "owner/repo" — strip that
        # leading echo so the table reads "**slug** — description" without
        # printing the slug twice.
        first_line = p.text.split("\n", 1)[0].strip()
        body = p.text.split("\n", 2)[1].strip() if "\n" in p.text else ""
        title = (body or first_line).replace("|", "/").strip()
        if title.lower().startswith(slug.lower()):
            title = title[len(slug):].lstrip(" -:—").strip()
        title = title[:100]
        out.append((slug, p.platform, root, title))
    return out


def _front_matter(
    date_label: str,
    topic_key: str,
    lang: str,
    posts: list[Post],
    analysis: dict,
    tags: list[str],
    model: str,
    translated_by: str | None,
) -> dict:
    other = "th" if lang == "en" else "en"
    fm = {
        "type": "social-topic-report",
        "date": date_label,
        "topic": topic_key,
        "lang": lang,
        "pair": f"{topic_key}.{other}.md",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "generator": GENERATOR,
        "model": model,
        "platforms": sorted({p.platform for p in posts}),
        "regions": ["global"],
        "post_count": len(posts),
        "salience": analysis.get("salience"),
        "sentiment": analysis.get("sentiment"),
        "confidence": analysis.get("confidence"),
        "tags": analysis.get("tags") or tags,
    }
    if lang == "th" and translated_by:
        fm["translated_by"] = translated_by
    return fm


def render_file(front_matter: dict, body: str) -> str:
    fm = yaml.safe_dump(front_matter, sort_keys=False, allow_unicode=True)
    return f"---\n{fm}---\n\n{body}"


def render_report(
    date_label: str,
    topic_key: str,
    topic_cfg: dict,
    analysis: dict,
    posts: list[Post],
    lang: str,
    body: str,
    model: str,
    translated_by: str | None = None,
) -> str:
    fm = _front_matter(
        date_label, topic_key, lang, posts, analysis,
        topic_cfg.get("tags", []), model, translated_by,
    )
    return render_file(fm, body)


def render_index(date_label: str, lang: str, entries: list[dict]) -> str:
    fm = {
        "type": "social-daily-index",
        "date": date_label,
        "lang": lang,
        "generator": GENERATOR,
        "topics": [
            {
                "topic": e["topic"],
                "title": e["title"],
                "salience": e["salience"],
                "file": f"{e['topic']}.{lang}.md",
            }
            for e in entries
        ],
    }
    heading = "Daily Social Report" if lang == "en" else "รายงานโซเชียลรายวัน"
    out = [f"# {heading} — {date_label}\n", "| topic | salience | report |", "|---|---|---|"]
    for e in entries:
        out.append(f"| {e['title']} | {e['salience']} | [{e['topic']}.{lang}.md]({e['topic']}.{lang}.md) |")
    return render_file(fm, "\n".join(out) + "\n")


def merge_index_entries(existing_path, new_entries: list[dict]) -> list[dict]:
    """Merge new entries with whatever is already in an existing index file.

    Partial runs (e.g. `--topic ai-news`) must not erase other topics that were
    written in earlier runs of the same day. Read the prior frontmatter, replace
    entries whose topic key matches a new entry, and keep the rest. Result is
    sorted by salience desc, then topic key for stability.
    """
    from pathlib import Path

    new_by_key = {e["topic"]: e for e in new_entries}
    merged: dict[str, dict] = {}

    p = Path(existing_path)
    if p.exists():
        text = p.read_text(encoding="utf-8")
        if text.startswith("---"):
            try:
                _, fm_text, _ = text.split("---", 2)
                fm = yaml.safe_load(fm_text) or {}
                for t in fm.get("topics", []) or []:
                    key = t.get("topic")
                    if not key:
                        continue
                    merged[key] = {
                        "topic": key,
                        "title": t.get("title") or key,
                        "salience": t.get("salience"),
                    }
            except (ValueError, yaml.YAMLError):
                pass  # malformed index — treat as no prior state

    merged.update(new_by_key)
    return sorted(
        merged.values(),
        key=lambda e: (-(e.get("salience") or 0), e["topic"]),
    )
