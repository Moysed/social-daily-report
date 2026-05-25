"""CLI entry point.

    python -m social_report.cli run                          # all topics, today
    python -m social_report.cli run --topic ai-devtools
    python -m social_report.cli run --date 2026-05-20
    python -m social_report.cli run --dry-run                # skip LLM, show what would happen
    python -m social_report.cli run --platform hackernews    # only this connector per topic
    python -m social_report.cli run --top 10                 # preview top posts after dedup
    python -m social_report.cli run --no-db                  # skip SQLite store writes
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
from .analyze.post_cards import analyze_top_posts
from .connectors import make_connector
from .dedup import dedup
from .normalize import normalize
from .render.markdown import (
    build_body,
    build_top_posts,
    merge_index_entries,
    pick_top_posts,
    render_index,
    render_report,
)
from .store import db as store
from .store.files import write_file

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB_PATH = REPO_ROOT / "data" / "reports.db"
STUB_TH_NOTE_NO_LLM = (
    "> _การแปลภาษาไทยถูกปิดไว้ — ตั้งค่า `LLM_BACKEND=cli` (Claude Code subscription) "
    "หรือ `ANTHROPIC_API_KEY` เพื่อเปิดใช้งาน._\n\n"
)
STUB_TH_NOTE_FAILED = (
    "> _การแปลภาษาไทยรอบนี้ล้มเหลว (timeout หรือ error) — แสดงต้นฉบับภาษาอังกฤษแทน._\n\n"
)
# Back-compat alias for any external import.
STUB_TH_NOTE = STUB_TH_NOTE_NO_LLM


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
        backend_label = "stub"
    else:
        client = make_llm_client(cwd=str(REPO_ROOT))
        mode = f"LIVE ({client.backend})" if client.enabled else f"STUB ({client.backend} unavailable)"
        backend_label = client.backend if client.enabled else "stub"
        print(f"[social-daily-report] {date_label} | mode: {mode}\n")

    topics = cfg["topics"]
    if args.topic:
        topics = {args.topic: topics[args.topic]}

    db_path = Path(args.db) if args.db else DEFAULT_DB_PATH
    use_db = not args.no_db

    if use_db:
        conn = store.connect(db_path)
        store.init_db(conn)
        for tk, tc in topics.items():
            store.upsert_topic(conn, tk, tc.get("title", tk), tc.get("focus", ""))
        conn.commit()
        run_id = store.start_run(
            conn, date_label, args.topic, backend_label, dry_run=args.dry_run
        )
        print(f"  [db] run #{run_id} -> {db_path.relative_to(REPO_ROOT) if db_path.is_relative_to(REPO_ROOT) else db_path}")
    else:
        conn = None
        run_id = None

    index_entries: list[dict] = []
    error: str | None = None

    try:
        for topic_key, topic_cfg in topics.items():
            posts = _fetch_topic(topic_key, topic_cfg, since, args.platform)

            if use_db:
                for p in posts:
                    store.upsert_post(conn, p)
                    store.record_membership(conn, p.id, topic_key, date_label)
                conn.commit()

            if args.dry_run:
                print(f"\n===== {topic_key} -- top {min(args.top, len(posts))} of {len(posts)} =====")
                for p in posts[: args.top]:
                    cross = f" +{','.join(p.also_on)}" if p.also_on else ""
                    print(f"  {p.engagement.likes:>5}pts [{p.platform}{cross}]  {p.text[:80]}")
                continue

            analysis = analyze_topic(client, topic_cfg, date_label, posts)

            # English = canonical. Top Posts HTML is appended *after* translation
            # so the X embeds / image cards don't get reshaped by the translator.
            en_body = build_body(analysis, posts, date_label, topic_cfg["title"])

            # Per-post LLM cards — only for posts we actually plan to render.
            picks = pick_top_posts(posts)
            cards: dict[str, dict] = {}
            if picks and client.enabled:
                print(f"  {topic_key}: cards for {len(picks)} posts...", end="", flush=True)
                cards = analyze_top_posts(client, topic_cfg["title"], picks)
                print(" done")

            en_top = build_top_posts(posts, cards, "en")
            th_top = build_top_posts(posts, cards, "th")

            # Thai = translation of the prose body only.
            if client.enabled and posts:
                try:
                    th_body = client.translate(en_body)
                    translated_by = SONNET_MODEL
                except Exception as exc:
                    print(f"  {topic_key}: !! translate failed ({exc}); falling back to English with notice")
                    th_body = STUB_TH_NOTE_FAILED + en_body
                    translated_by = None
            else:
                th_body = STUB_TH_NOTE_NO_LLM + en_body
                translated_by = None

            if en_top:
                en_body = en_body.rstrip() + "\n\n" + en_top
            if th_top:
                th_body = th_body.rstrip() + "\n\n" + th_top

            en_md = render_report(date_label, topic_key, topic_cfg, analysis, posts, "en", en_body, OPUS_MODEL)
            p_en = write_file(out_base, date_label, f"{topic_key}.en.md", en_md)
            th_md = render_report(
                date_label, topic_key, topic_cfg, analysis, posts, "th", th_body, OPUS_MODEL, translated_by
            )
            p_th = write_file(out_base, date_label, f"{topic_key}.th.md", th_md)

            salience = analysis.get("salience")
            print(f"  -> {p_en.name}, {p_th.name}  ({len(posts)} posts, salience {salience})")
            index_entries.append(
                {"topic": topic_key, "title": topic_cfg["title"], "salience": salience}
            )

            if use_db:
                store.record_report(
                    conn, run_id=run_id, date=date_label, topic_key=topic_key,
                    lang="en", path=p_en, post_count=len(posts), salience=salience, model=OPUS_MODEL,
                )
                store.record_report(
                    conn, run_id=run_id, date=date_label, topic_key=topic_key,
                    lang="th", path=p_th, post_count=len(posts), salience=salience,
                    model=OPUS_MODEL, translated_by=translated_by,
                )
                conn.commit()

        if not args.dry_run:
            day_dir = out_base / date_label
            for lang in ("en", "th"):
                merged = merge_index_entries(day_dir / f"index.{lang}.md", index_entries)
                write_file(out_base, date_label, f"index.{lang}.md", render_index(date_label, lang, merged))
            print(f"\nDone. Reports in: {day_dir}")
        else:
            print(f"\nDry-run done. {len(topics)} topics inspected.")

    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        if use_db and conn is not None:
            final_status = "dry-run" if args.dry_run else ("error" if error else "ok")
            store.finish_run(conn, run_id, status=final_status, error=error)
            conn.close()


def distribute_cmd(args: argparse.Namespace) -> None:
    """Broadcast top stories of a date to Discord/Slack/Teams + dump social copy."""
    load_dotenv(REPO_ROOT / ".env")
    from . import distribute as dist

    day = _resolve_date(args.date)
    date_label = day.isoformat()

    client = None
    if not args.no_llm and not args.dry_run:
        try:
            client = make_llm_client(cwd=str(REPO_ROOT))
            if not client.enabled:
                print("distribute: LLM unavailable; falling back to template copy")
                client = None
        except Exception as exc:
            print(f"distribute: LLM init failed ({exc}); template copy only")
            client = None

    dist.distribute(
        date_label=date_label,
        db_path=Path(args.db) if args.db else dist.DEFAULT_DB_PATH,
        reports_dir=Path(args.reports) if args.reports else dist.DEFAULT_REPORTS_DIR,
        outbox_dir=Path(args.outbox) if args.outbox else dist.DEFAULT_OUTBOX_DIR,
        topic_filter=args.topic,
        top=args.top,
        dry_run=args.dry_run,
        client=client,
        idempotent=args.idempotent,
    )


def digest_cmd(args: argparse.Namespace) -> None:
    """Build a weekly digest from the last 7 days of reports."""
    load_dotenv(REPO_ROOT / ".env")
    from . import weekly

    day = _resolve_date(args.date)

    client = None
    if not args.no_llm and not args.dry_run:
        try:
            client = make_llm_client(cwd=str(REPO_ROOT))
            if not client.enabled:
                print("digest: LLM unavailable; using concat fallback")
                client = None
        except Exception as exc:
            print(f"digest: LLM init failed ({exc}); concat fallback")
            client = None

    weekly.run_digest(
        end_date=day,
        db_path=Path(args.db) if args.db else weekly.DEFAULT_DB_PATH,
        reports_dir=Path(args.reports) if args.reports else weekly.DEFAULT_REPORTS_DIR,
        digests_dir=Path(args.digests) if args.digests else weekly.DEFAULT_DIGESTS_DIR,
        dry_run=args.dry_run,
        client=client,
    )


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
    run_p.add_argument("--db", help="SQLite path (default: data/reports.db)")
    run_p.add_argument("--no-db", action="store_true", help="skip SQLite store writes entirely")
    run_p.set_defaults(func=run)

    dist_p = sub.add_parser(
        "distribute",
        help="broadcast top stories to Discord/Slack/Teams + dump social copy",
    )
    dist_p.add_argument("--date", default="today", help="today | yesterday | YYYY-MM-DD")
    dist_p.add_argument("--topic", help="force a specific topic instead of the top-salience pick")
    dist_p.add_argument("--top", type=int, default=1, help="broadcast top N topics (default 1)")
    dist_p.add_argument("--dry-run", action="store_true", help="print payloads instead of POSTing")
    dist_p.add_argument("--no-llm", action="store_true", help="skip Sonnet copy generation (template only)")
    dist_p.add_argument("--db", help="SQLite path (default: data/reports.db)")
    dist_p.add_argument("--reports", help="reports dir (default: content/reports)")
    dist_p.add_argument("--outbox", help="distribution record dir (default: content/distribution)")
    dist_p.add_argument(
        "--idempotent",
        action="store_true",
        help="skip if a distribution record already exists for this date",
    )
    dist_p.set_defaults(func=distribute_cmd)

    dig_p = sub.add_parser(
        "digest",
        help="render a weekly digest from the last 7 days of reports",
    )
    dig_p.add_argument("--date", default="today", help="week ending: today | YYYY-MM-DD")
    dig_p.add_argument("--no-llm", action="store_true", help="skip Sonnet synthesis (concat fallback)")
    dig_p.add_argument("--dry-run", action="store_true", help="print to stdout, don't write")
    dig_p.add_argument("--db", help="SQLite path (default: data/reports.db)")
    dig_p.add_argument("--reports", help="reports dir (default: content/reports)")
    dig_p.add_argument("--digests", help="digest output dir (default: content/digests)")
    dig_p.set_defaults(func=digest_cmd)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
