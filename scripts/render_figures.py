#!/usr/bin/env python3
"""Render simple SVG charts for the lead paper from CSV inputs."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "paper" / "figures"


def escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def scale(value: float, min_v: float, max_v: float, out_min: float, out_max: float) -> float:
    if max_v == min_v:
        return out_min
    ratio = (value - min_v) / (max_v - min_v)
    return out_min + ratio * (out_max - out_min)


def render_latency_curve() -> None:
    rows = list(csv.DictReader((FIGURES / "latency_diligence_curve.csv").open()))
    width, height = 960, 540
    margin_left, margin_top, margin_bottom = 90, 70, 80
    chart_w = 760
    chart_h = 320
    x_step = chart_w / (len(rows) - 1)

    def make_points(field: str) -> str:
        pts = []
        for i, row in enumerate(rows):
            x = margin_left + i * x_step
            y = scale(float(row[field]), 0.0, 10.0, margin_top + chart_h, margin_top)
            pts.append(f"{x:.1f},{y:.1f}")
        return " ".join(pts)

    labels = [row["latency_bucket"].replace("_", "-") for row in rows]
    diligence = make_points("perceived_diligence_score")
    reliability = make_points("reliability_score")
    risk = make_points("task_accretion_risk")

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#faf8f2"/>',
        '<text x="90" y="38" font-family="Georgia, serif" font-size="24" fill="#111">Figure 1. Latency-Diligence Curve</text>',
        '<text x="90" y="58" font-family="Arial, sans-serif" font-size="12" fill="#555">Reply timing balances diligence, reliability, and task accretion risk.</text>',
    ]

    for value in range(0, 11, 2):
        y = scale(value, 0.0, 10.0, margin_top + chart_h, margin_top)
        parts.append(f'<line x1="{margin_left}" y1="{y:.1f}" x2="{margin_left + chart_w}" y2="{y:.1f}" stroke="#e2ddd2" stroke-width="1"/>')
        parts.append(f'<text x="58" y="{y + 4:.1f}" font-family="Arial, sans-serif" font-size="12" fill="#666">{value}</text>')

    parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{margin_top + chart_h}" stroke="#333" stroke-width="2"/>')
    parts.append(f'<line x1="{margin_left}" y1="{margin_top + chart_h}" x2="{margin_left + chart_w}" y2="{margin_top + chart_h}" stroke="#333" stroke-width="2"/>')

    for i, label in enumerate(labels):
        x = margin_left + i * x_step
        parts.append(f'<text x="{x:.1f}" y="{margin_top + chart_h + 30}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#333">{escape(label)}</text>')

    parts.extend(
        [
            f'<polyline fill="none" stroke="#111" stroke-width="4" points="{diligence}"/>',
            f'<polyline fill="none" stroke="#3d6e70" stroke-width="4" points="{reliability}"/>',
            f'<polyline fill="none" stroke="#b35c1e" stroke-width="4" points="{risk}"/>',
            '<text x="740" y="95" font-family="Arial, sans-serif" font-size="13" fill="#111">Diligence</text>',
            '<line x1="700" y1="90" x2="730" y2="90" stroke="#111" stroke-width="4"/>',
            '<text x="740" y="120" font-family="Arial, sans-serif" font-size="13" fill="#3d6e70">Reliability</text>',
            '<line x1="700" y1="115" x2="730" y2="115" stroke="#3d6e70" stroke-width="4"/>',
            '<text x="740" y="145" font-family="Arial, sans-serif" font-size="13" fill="#b35c1e">Task risk</text>',
            '<line x1="700" y1="140" x2="730" y2="140" stroke="#b35c1e" stroke-width="4"/>',
        ]
    )
    parts.append('</svg>')
    (FIGURES / "latency_diligence_curve.svg").write_text("\n".join(parts))


def render_hierarchy_chart() -> None:
    rows = list(csv.DictReader((FIGURES / "hierarchy_window_data.csv").open()))
    width, height = 980, 500
    margin_left, margin_top = 210, 80
    chart_w = 670
    bar_h = 34
    gap = 18

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#faf8f2"/>',
        '<text x="210" y="38" font-family="Georgia, serif" font-size="24" fill="#111">Figure 2. Hierarchy-Specific Acceptable Delay Window</text>',
        '<text x="210" y="58" font-family="Arial, sans-serif" font-size="12" fill="#555">Direct hierarchy compresses the reply window; peer-only contexts permit wider drift.</text>',
        f'<line x1="{margin_left}" y1="{margin_top + 6* (bar_h + gap)}" x2="{margin_left + chart_w}" y2="{margin_top + 6* (bar_h + gap)}" stroke="#333" stroke-width="2"/>',
    ]

    for t in [0, 30, 60, 120, 180, 240]:
        x = scale(float(t), 0, 240, margin_left, margin_left + chart_w)
        parts.append(f'<line x1="{x:.1f}" y1="{margin_top - 18}" x2="{x:.1f}" y2="{margin_top + 6*(bar_h+gap)-4}" stroke="#e2ddd2" stroke-width="1"/>')
        parts.append(f'<text x="{x:.1f}" y="{margin_top + 6*(bar_h+gap) + 24}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#333">{t}</text>')

    for i, row in enumerate(rows):
        y = margin_top + i * (bar_h + gap)
        x1 = scale(float(row["optimal_window_low_min"]), 0, 240, margin_left, margin_left + chart_w)
        x2 = scale(float(row["optimal_window_high_min"]), 0, 240, margin_left, margin_left + chart_w)
        penalty = float(row["visibility_penalty"])
        fill = "#9d8f7a" if penalty < 2 else "#b35c1e" if penalty < 4 else "#7a1f1f"
        label = row["sender_hierarchy"].replace("_", " ")
        parts.append(f'<text x="{margin_left - 18}" y="{y + 22}" text-anchor="end" font-family="Arial, sans-serif" font-size="13" fill="#222">{escape(label)}</text>')
        parts.append(f'<rect x="{x1:.1f}" y="{y:.1f}" width="{max(6.0, x2-x1):.1f}" height="{bar_h}" rx="6" fill="{fill}"/>')
        parts.append(f'<text x="{x2 + 8:.1f}" y="{y + 22}" font-family="Arial, sans-serif" font-size="12" fill="#444">{row["optimal_window_low_min"]}-{row["optimal_window_high_min"]} min</text>')

    parts.extend(
        [
            '<text x="210" y="470" font-family="Arial, sans-serif" font-size="12" fill="#333">Color intensity tracks visibility penalty.</text>',
            '</svg>',
        ]
    )
    (FIGURES / "hierarchy_window_chart.svg").write_text("\n".join(parts))


def main() -> None:
    render_latency_curve()
    render_hierarchy_chart()
    print("Rendered SVG figures to paper/figures/")


if __name__ == "__main__":
    main()
