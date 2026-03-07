#!/usr/bin/env python3
"""Validate that the active submission pack is complete and internally coherent."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINAL = ROOT / "paper" / "final"
FIGURES = ROOT / "paper" / "figures"

REQUIRED_FILES = [
    ROOT / "PROJECT_STRUCTURE.md",
    FINAL / "read-seen-ignored_submission-ready.md",
    FINAL / "read-seen-ignored_submission-ready.html",
    FINAL / "submission-metadata.md",
    FINAL / "submission-checklist.md",
    ROOT / "paper" / "review" / "shit-fit-review-2026-03-07.md",
    ROOT / "paper" / "figures" / "visual-explainer-plan.md",
    ROOT / "paper" / "figures" / "banana-prompt-pack.md",
    ROOT / "social" / "xiaohongshu" / "README.md",
]

REQUIRED_FIGURES = [
    FIGURES / "theory_framework_map.svg",
    FIGURES / "latency_diligence_curve.svg",
    FIGURES / "hierarchy_window_chart.svg",
    FIGURES / "first_responder_discount.svg",
    FIGURES / "role_obligation_matrix.svg",
    FIGURES / "role_species_windows.svg",
    FIGURES / "publication_burden_u_curve.svg",
    FIGURES / "red_envelope_shock.svg",
]


def check_exists() -> bool:
    ok = True
    for path in REQUIRED_FILES + REQUIRED_FIGURES:
        if not path.exists():
            print(f"[MISSING] {path.relative_to(ROOT)}")
            ok = False
    return ok


def check_main_manuscript() -> bool:
    path = FINAL / "read-seen-ignored_submission-ready.md"
    text = path.read_text()
    ok = True
    required_snippets = [
        "## Abstract",
        "## 中文摘要",
        "## References",
        "## Context Materials for Meme and Scene Language",
    ]
    for snippet in required_snippets:
        if snippet not in text:
            print(f"[MISSING_SECTION] {path.relative_to(ROOT)} lacks {snippet}")
            ok = False
    return ok


def check_metadata() -> bool:
    text = (FINAL / "submission-metadata.md").read_text()
    required_snippets = [
        "read-seen-ignored_submission-ready.md",
        "read-seen-ignored_submission-ready.html",
        "../archive/2026-03-retired-snapshots/",
    ]
    ok = True
    for snippet in required_snippets:
        if snippet not in text:
            print(f"[MISSING_METADATA] submission-metadata.md lacks {snippet}")
            ok = False
    return ok


def main() -> None:
    checks = [
        check_exists(),
        check_main_manuscript(),
        check_metadata(),
    ]
    if all(checks):
        print("[OK] active submission pack")
        return
    raise SystemExit(1)


if __name__ == "__main__":
    main()
