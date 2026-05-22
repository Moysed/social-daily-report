"""CLI entry point.

    python -m social_report.cli run                          # all topics, today
    python -m social_report.cli run --topic ai-devtools
    python -m social_report.cli run --date 2026-05-20
    python -m social_report.cli run --dry-run                # skip LLM, show what would happen
    python -m social_report.cli run --platform hackernews    # only this connector per topic
    python -m social_report.cli run --top 10                 # preview top posts after dedup
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

# Windows consoles default to cp1252; post text contains unicode (em-dash, Thai, etc.)
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

import yaml
from dotenv import load_dotenv

from .analyze.client import OPUS_MODEL, SONNET_MODEL, make_llm_client
from .analyze.pipeline import analyze_topic
from .connectors import make_connector
from .dedup import dedup
from .normalize import normalize
from .render.markdown import build_body, render_index, render_report
from .store.files import write_file

REPO_ROOT = Path(__file__).resolve().parents[1]
STUB_TH_NOTE = (
    "> _Thai translation disabled — set `ANTHROPIC_API_KEY` to enable (STUB mode)._\n\n"
)


def _resolve_date(value: str | None) -> date:
    if value in (None, "today"):
        return date.today()
    if value == "yesterday":
        return date.today() - timedelta(days=1)
    return date.fromisoformat(value)


def _fetch_topic(topic_key: str, topic_cfg: dict, since: datetime, platform_filter: str | None):
    """Fetch -> normalize -> dedup for one topic. Returns posts list."""
    posts = []
    for src in topic_cfg.get("sources", []):
        if platform_filter and src["connector"] != platform_filter:
            continue
        conn = make_connector(src["connector"], src)
        try:
            fetched = conn.fetch(since, src.get("limit", 30))
            posts.extend(fetched)
            print(f"  {topic_key}: +{len(fetched)} from {src['connector']}")
        except Exception as exc:  # one bad source shouldn't kill the topic
            print(f"  {topic_key}: !! {src['connector']} failed: {exc}")
        finally:
            conn.close()

    raw_n = len(posts)
    posts = normalize(posts)
    norm_n = len(posts)
    posts = dedup(posts)
    if raw_n != len(posts):
        print(f"  {topic_key}: {raw_n} fetched -> {norm_n} normalized -> {len(posts)} unique")
    posts.sort(key=lambda p: p.engagement.likes, reverse=True)
    return posts


def run(args: argparse.Namespace) -> None:
    load_dotenv(REPO_ROOT / ".env")
    cfg = yaml.safe_load((REPO_ROOT / "config" / "sources.yaml").read_text(encoding="utf-8"))

    day = _resolve_date(args.date)
    date_label = day.isoformat()
    since = datetime.now(timezone.utc) - timedelta(hours=cfg.get("lookback_hours", 48))

    out_base = Path(args.out) if args.out else REPO_ROOT / "content" / "reports"

    if args.dry_run:
        print(f"[social-daily-report] {date_label} | mode: DRY-RUN (no LLM, no files)\n")
        client = None
    else:
        client = make_llm_client(cwd=str(REPO_ROOT))
        mode = f"LIVE ({client.backend})" if client.enabled else f"STUB ({client.backend} unavailable)"
        print(f"[social-daily-report] {date_label} | mode: {mode}\n")

    topics = cfg["topics"]
    if args.topic:
        topics = {args.topic: topics[args.topic]}

    index_entries: list[dict] = []

    for topic_key, topic_cfg in topics.items():
        posts = _fetch_topic(topic_key, topic_cfg, since, args.platform)

        if args.dry_run:
            print(f"\n===== {topic_key} -- top {min(args.top, len(posts))} of {len(posts)} =====")
            for p in posts[: args.top]:
                cross = f" +{','.join(p.also_on)}" if p.also_on else ""
                print(f"  {p.engagement.likes:>5}pts [{p.platform}{cross}]  {p.text[:80]}")
            continue

        analysis = analyze_topic(client, topic_cfg, date_label, posts)

        # English = canonical
        en_body = build_body(analysis, posts, date_label, topic_cfg["title"])
        en_md = render_report(date_label, topic_key, topic_cfg, analysis, posts, "en", en_body, OPUS_MODEL)
        p_en = write_file(out_base, date_label, f"{topic_key}.en.md", en_md)

        # Thai = translation for human reading
        if client.enabled and posts:
            th_body = client.translate(en_body)
            translated_by = SONNET_MODEL
        else:
            th_body = STUB_TH_NOTE + en_body
            translated_by = None
        th_md = render_report(
            date_label, topic_key, topic_cfg, analysis, posts, "th", th_body, OPUS_MODEL, translated_by
        )
        p_th = write_file(out_base, date_label, f"{topic_key}.th.md", th_md)

        print(f"  -> {p_en.name}, {p_th.name}  ({len(posts)} posts, salience {analysis.get('salience')})")
        index_entries.append(
            {"topic": topic_key, "title": topic_cfg["title"], "salience": analysis.get("salience")}
        )

    if args.dry_run:
        print(f"\nDry-run done. {len(topics)} topics inspected.")
        return

    write_file(out_base, date_label, "index.en.md", render_index(date_label, "en", index_entries))
    write_file(out_base, date_label, "index.th.md", render_index(date_label, "th", index_entries))

    print(f"\nDone. Reports in: {out_base / date_label}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="social-report")
    sub = parser.add_subparsers(dest="cmd", required=True)
    run_p = sub.add_parser("run", help="fetch -> analyze -> render reports")
    run_p.add_argument("--date", help="today | yesterday | YYYY-MM-DD", default="today")
    run_p.add_argument("--topic", help="run a single topic key (default: all)")
    run_p.add_argument("--platform", help="restrict to one connector (e.g. hackernews)")
    run_p.add_argument("--dry-run", action="store_true", help="skip LLM and file writes; preview posts only")
    run_p.add_argument("--top", type=int, default=10, help="how many posts to preview in --dry-run")
    run_p.add_argument("--out", help="output base dir (default: content/reports)")
    run_p.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
