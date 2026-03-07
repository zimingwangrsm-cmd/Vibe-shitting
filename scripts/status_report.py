#!/usr/bin/env python3
"""Check whether each phase contains the required files."""

from __future__ import annotations

from pathlib import Path


REQUIRED = ["summary.md", "decision-log.md", "share-pack.md", "artifacts"]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    phases = sorted((root / "phases").glob("phase-*"))
    if not phases:
        raise SystemExit("No phase folders found")

    missing_any = False
    for phase in phases:
        missing = [name for name in REQUIRED if not (phase / name).exists()]
        if missing:
            missing_any = True
            print(f"[MISSING] {phase.name}: {', '.join(missing)}")
        else:
            print(f"[OK] {phase.name}")

    if missing_any:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
