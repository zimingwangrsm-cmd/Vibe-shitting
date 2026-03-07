#!/usr/bin/env python3
"""Create a new phase folder from the project templates."""

from __future__ import annotations

import argparse
from pathlib import Path


def render(text: str, phase_id: str, title_cn: str, title_en: str) -> str:
    return (
        text.replace("{{PHASE_ID}}", phase_id)
        .replace("{{PHASE_TITLE_CN}}", title_cn)
        .replace("{{PHASE_TITLE_EN}}", title_en)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", help="Example: phase-06-second-paper")
    parser.add_argument("title_cn")
    parser.add_argument("title_en")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    templates = root / "templates"
    phase_dir = root / "phases" / args.slug
    artifacts_dir = phase_dir / "artifacts"

    if phase_dir.exists():
        raise SystemExit(f"{phase_dir} already exists")

    phase_dir.mkdir(parents=True)
    artifacts_dir.mkdir()

    summary = render(
        (templates / "phase-template.md").read_text(),
        args.slug,
        args.title_cn,
        args.title_en,
    )
    decision = (templates / "decision-log-template.md").read_text()
    share = (templates / "share-pack-template.md").read_text()

    (phase_dir / "summary.md").write_text(summary)
    (phase_dir / "decision-log.md").write_text(decision)
    (phase_dir / "share-pack.md").write_text(share)
    (artifacts_dir / "README.md").write_text(
        "# Artifacts\n\nStore screenshots, drafts, covers, and exported assets here.\n"
    )

    print(f"Created {phase_dir}")


if __name__ == "__main__":
    main()
