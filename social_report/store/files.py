"""Write rendered Markdown to content/reports/YYYY-MM-DD/<topic>.<lang>.md."""

from __future__ import annotations

from pathlib import Path


def report_dir(base: Path, date_label: str) -> Path:
    d = base / date_label
    d.mkdir(parents=True, exist_ok=True)
    return d


def write_file(base: Path, date_label: str, name: str, content: str) -> Path:
    path = report_dir(base, date_label) / name
    path.write_text(content, encoding="utf-8")
    return path
