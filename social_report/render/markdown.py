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


def build_top_posts(
    posts: list[Post],
    cards: dict[str, dict] | None = None,
    lang: str = "en",
) -> str:
    """Top Posts HTML — appended after translation so HTML doesn't confuse the
    translator. `cards` maps post.id → {says_en, says_th, interesting_en, ...}
    when per-post LLM analysis is available; falls back to a slimmer card."""
    picks = pick_top_posts(posts)
    if not picks:
        return ""
    cards = cards or {}
    lines = _render_top_posts(picks, cards, lang)
    return "\n".join(lines) + "\n"


def pick_top_posts(posts: list[Post], limit: int = 8) -> list[Post]:
    """Public picker so the CLI can run per-post LLM analysis on the exact set
    that will be rendered (avoids paying for posts that get dropped)."""
    picks: list[Post] = []
    seen: set[str] = set()
    for p in posts:
        if len(picks) >= limit:
            break
        if p.url in seen:
            continue
        if _is_x_post(p) and p.engagement.likes < _X_EMBED_MIN_LIKES:
            continue
        if p.media or _is_x_post(p):
            picks.append(p)
            seen.add(p.url)
    return picks


def _is_x_post(p: Post) -> bool:
    return p.platform == "x"


def _top_thumbnail(posts: list[Post]) -> str | None:
    """First post with a usable media URL — used as the topic card image."""
    for p in posts[:30]:
        if p.media:
            return p.media[0]
    return None


_X_EMBED_MIN_LIKES = 5  # avoid embedding zero-engagement X chatter (esp. XR's noisy 'AR/VR' query)

_HEADING_TOP_POSTS = {"en": "Top Posts", "th": "โพสต์เด่น"}
_LABEL_SAYS = {"en": "What it says", "th": "เนื้อหา"}
_LABEL_INTERESTING = {"en": "Why interesting", "th": "ทำไมน่าสนใจ"}
_LABEL_ADAPT = {"en": "How NDF DEV adapts", "th": "ใช้กับ NDF DEV ยังไง"}
_LABEL_VIEW_ON = {"en": "View on", "th": "เปิดบน"}


def _esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
         .replace("<", "&lt;")
         .replace(">", "&gt;")
         .replace('"', "&quot;")
    )


def _card_field(card: dict, key_base: str, lang: str, fallback: str = "") -> str:
    val = (card or {}).get(f"{key_base}_{lang}") or (card or {}).get(f"{key_base}_en") or fallback
    return val.strip()


def _render_top_posts(picks: list[Post], cards: dict[str, dict], lang: str) -> list[str]:
    heading = _HEADING_TOP_POSTS.get(lang, _HEADING_TOP_POSTS["en"])
    label_says = _LABEL_SAYS.get(lang, _LABEL_SAYS["en"])
    label_interesting = _LABEL_INTERESTING.get(lang, _LABEL_INTERESTING["en"])
    label_adapt = _LABEL_ADAPT.get(lang, _LABEL_ADAPT["en"])
    label_view = _LABEL_VIEW_ON.get(lang, _LABEL_VIEW_ON["en"])

    out: list[str] = ["", f"## {heading}", "", '<div class="post-stream">']
    for p in picks:
        card = cards.get(p.id, {})
        excerpt = _esc(p.text.split("\n", 1)[0][:200])
        says = _esc(_card_field(card, "says", lang, p.text.split("\n", 1)[0][:200]))
        interesting = _esc(_card_field(card, "interesting", lang))
        adapt = _esc(_card_field(card, "adapt", lang))

        media_block = _build_media_block(p)
        eng_str = f"♥ {p.engagement.likes} · 💬 {p.engagement.comments}"

        parts = [
            f'<article class="ndf-card platform-{_esc(p.platform)}">',
            f'  <header class="ndf-card-head">',
            f'    <span class="ndf-author">@{_esc(p.author)}</span>',
            f'    <span class="ndf-platform">{_esc(p.platform)}</span>',
            f'    <span class="ndf-engagement">{_esc(eng_str)}</span>',
            f'  </header>',
            media_block,
            f'  <div class="ndf-card-body">',
            f'    <p class="ndf-quote">“{excerpt}”</p>',
            f'    <dl class="ndf-fields">',
        ]
        if says:
            parts += [f'      <dt>{_esc(label_says)}</dt>', f'      <dd>{says}</dd>']
        if interesting:
            parts += [f'      <dt>{_esc(label_interesting)}</dt>', f'      <dd>{interesting}</dd>']
        if adapt:
            parts += [f'      <dt class="ndf-adapt-label">{_esc(label_adapt)}</dt>',
                      f'      <dd class="ndf-adapt">{adapt}</dd>']
        parts += [
            '    </dl>',
            f'    <a class="ndf-source" href="{_esc(p.url)}" target="_blank" rel="noopener">'
            f'{_esc(label_view)} {_esc(p.platform)} →</a>',
            '  </div>',
            '</article>',
        ]
        out.append("\n".join(parts))
    out.append('</div>')
    return out


def _build_media_block(p: Post) -> str:
    """Two flavors: X embed (widgets.js handles it) for X posts; image figure
    for everything else with media. Returns empty string when neither applies."""
    if _is_x_post(p):
        return (
            f'  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true">'
            f'<a href="{_esc(p.url)}">View @{_esc(p.author)} on X</a>'
            f'</blockquote>'
        )
    if p.media:
        return (
            f'  <a class="ndf-card-media" href="{_esc(p.url)}" target="_blank" rel="noopener">'
            f'<img src="{_esc(p.media[0])}" alt="" loading="lazy" referrerpolicy="no-referrer" />'
            f'</a>'
        )
    return ''


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
    thumb = _top_thumbnail(posts)
    if thumb:
        fm["thumbnail"] = thumb
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
