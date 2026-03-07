#!/usr/bin/env python3
"""Create a Xiaohongshu post draft from the template."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="Example: 04")
    parser.add_argument("slug", help="Example: method-protocol")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    template = (root / "templates" / "xhs-post-template.md").read_text()
    content = (
        template.replace("{{POST_NUMBER}}", args.number)
        .replace("{{POST_SLUG}}", args.slug)
    )
    target = root / "social" / "xiaohongshu" / f"post-{args.number}-{args.slug}.md"

    if target.exists():
        raise SystemExit(f"{target} already exists")

    target.write_text(content)
    print(f"Created {target}")


if __name__ == "__main__":
    main()
