#!/usr/bin/env python3
"""Validate that the canonical submission pack is complete and self-consistent."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINAL = ROOT / "paper" / "final"
FIGURES = ROOT / "paper" / "figures"

REQUIRED_FILES = [
    FINAL / "read-seen-ignored_submission_en.md",
    FINAL / "read-seen-ignored_submission_zh.md",
    FINAL / "read-seen-ignored_submission_en.html",
    FINAL / "read-seen-ignored_submission_zh.html",
    FINAL / "read-seen-ignored_submission-ready.html",
    FINAL / "submission-metadata.md",
    FINAL / "submission-checklist.md",
    ROOT / "paper" / "review" / "shit-fit-review-2026-03-07.md",
    ROOT / "paper" / "figures" / "visual-explainer-plan.md",
]

REQUIRED_FIGURES = [
    FIGURES / "theory_framework_map.svg",
    FIGURES / "latency_diligence_curve.svg",
    FIGURES / "hierarchy_window_chart.svg",
    FIGURES / "first_responder_discount.svg",
    FIGURES / "role_obligation_matrix.svg",
]

FORBIDDEN_PATTERNS = [
    "Full references:",
    "完整参考文献见：",
]


def check_exists() -> bool:
    ok = True
    for path in REQUIRED_FILES + REQUIRED_FIGURES:
        if not path.exists():
            print(f"[MISSING] {path.relative_to(ROOT)}")
            ok = False
    return ok


def check_canonical_manuscripts() -> bool:
    ok = True
    for name in ["read-seen-ignored_submission_en.md", "read-seen-ignored_submission_zh.md"]:
        path = FINAL / name
        text = path.read_text()
        if "## References" not in text and "## 参考文献" not in text:
            print(f"[MISSING_SECTION] {path.relative_to(ROOT)} lacks a references section")
            ok = False
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in text:
                print(f"[FORBIDDEN_POINTER] {path.relative_to(ROOT)} still contains: {pattern}")
                ok = False
    return ok


def check_metadata() -> bool:
    text = (FINAL / "submission-metadata.md").read_text()
    required_snippets = [
        "read-seen-ignored_submission_en.md",
        "read-seen-ignored_submission_zh.md",
        "read-seen-ignored_submission_en.html",
        "read-seen-ignored_submission_zh.html",
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
        check_canonical_manuscripts(),
        check_metadata(),
    ]
    if all(checks):
        print("[OK] canonical submission pack")
        return
    raise SystemExit(1)


if __name__ == "__main__":
    main()
