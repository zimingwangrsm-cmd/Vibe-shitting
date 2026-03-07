#!/usr/bin/env python3
"""Render SVG charts for the lead paper from CSV inputs."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "paper" / "figures"


def escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def scale(value: float, min_v: float, max_v: float, out_min: float, out_max: float) -> float:
    if max_v == min_v:
        return out_min
    ratio = (value - min_v) / (max_v - min_v)
    return out_min + ratio * (out_max - out_min)


def render_theory_map() -> None:
    width, height = 1040, 620
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#faf8f2"/>',
        '<text x="64" y="42" font-family="Georgia, serif" font-size="24" fill="#111">Figure 1. Theoretical Framework and Group-Chat Game</text>',
        '<text x="64" y="62" font-family="Arial, sans-serif" font-size="12" fill="#555">Reply latency is modeled as a visible signal inside a heterogeneous multi-person coordination problem.</text>',
        '<rect x="62" y="98" width="250" height="410" rx="12" fill="#efe5d4" stroke="#c9b79d"/>',
        '<rect x="394" y="98" width="252" height="410" rx="12" fill="#f3eee5" stroke="#c9b79d"/>',
        '<rect x="730" y="98" width="248" height="410" rx="12" fill="#efe5d4" stroke="#c9b79d"/>',
        '<text x="88" y="134" font-family="Arial, sans-serif" font-size="18" font-weight="700" fill="#111">Theory stack</text>',
        '<text x="420" y="134" font-family="Arial, sans-serif" font-size="18" font-weight="700" fill="#111">Group-chat game</text>',
        '<text x="756" y="134" font-family="Arial, sans-serif" font-size="18" font-weight="700" fill="#111">Observed outcomes</text>',
    ]

    left_boxes = [
        ("Signaling and reputation", "hidden busyness, diligence, and availability become inferable from delay"),
        ("Chronemics in CMC", "timestamps operate as socioemotional cues rather than empty intervals"),
        ("Communication visibility", "advisor + peers jointly witness order, delay, and tone"),
        ("Volunteer's dilemma", "someone must answer first, but nobody wants the cost too often"),
        ("Expectation states", "status and ownership decide who is actually allowed to wait"),
    ]
    center_boxes = [
        ("Inputs", "group size, sender hierarchy, urgency, visibility"),
        ("Heterogeneity", "first-author junior, procurement steward, postdoc proxy, generic bystander"),
        ("State changes", "someone replied already? ownership explicit? holiday fog active?"),
        ("Choice", "pick a delay that signals diligence without inviting extraction"),
    ]
    right_boxes = [
        ("Perceived diligence", "inverse-U over latency"),
        ("Reliability", "falls when delay looks like disappearance"),
        ("Assignment hazard", "rises when speed looks like free capacity"),
        ("Blame and suspicion", "compressed windows under hierarchy and visibility"),
    ]

    def box(x: int, y: int, w: int, h: int, title: str, body: str, fill: str) -> None:
        parts.extend(
            [
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#b7a58c"/>',
                f'<text x="{x + 16}" y="{y + 28}" font-family="Arial, sans-serif" font-size="15" font-weight="700" fill="#111">{escape(title)}</text>',
                f'<text x="{x + 16}" y="{y + 52}" font-family="Arial, sans-serif" font-size="12" fill="#3f3a33">{escape(body)}</text>',
            ]
        )

    y = 160
    for title, body in left_boxes:
        box(84, y, 206, 58, title, body, "#fbf7ee")
        y += 68

    y = 174
    for title, body in center_boxes:
        box(418, y, 204, 66, title, body, "#fffdf8")
        y += 82

    y = 174
    for title, body in right_boxes:
        box(754, y, 200, 66, title, body, "#fbf7ee")
        y += 82

    for y in [189, 257, 325, 393, 461]:
        parts.append(f'<line x1="290" y1="{y}" x2="394" y2="{y}" stroke="#8b5e34" stroke-width="2.5"/>')
        parts.append(f'<polygon points="394,{y} 382,{y-6} 382,{y+6}" fill="#8b5e34"/>')
    for y in [207, 289, 371, 453]:
        parts.append(f'<line x1="646" y1="{y}" x2="730" y2="{y}" stroke="#8b5e34" stroke-width="2.5"/>')
        parts.append(f'<polygon points="730,{y} 718,{y-6} 718,{y+6}" fill="#8b5e34"/>')

    parts.extend(
        [
            '<text x="420" y="560" font-family="Arial, sans-serif" font-size="12" fill="#555">Key modifiers: first-responder discount, task ownership, holiday fog, and visible audience composition.</text>',
            '</svg>',
        ]
    )
    (FIGURES / "theory_framework_map.svg").write_text("\n".join(parts))


def render_first_responder_discount() -> None:
    width, height = 940, 500
    margin_left, margin_top, chart_w, chart_h = 100, 90, 680, 270
    labels = ["1st reply", "2nd reply", "3rd+", "silent"]
    diligence = [9.2, 5.9, 3.4, 0.0]
    hazard = [8.6, 4.1, 1.7, 0.4]
    step = chart_w / (len(labels) - 1)

    def points(values: list[float]) -> str:
        pts = []
        for i, value in enumerate(values):
            x = margin_left + i * step
            y = scale(value, 0.0, 10.0, margin_top + chart_h, margin_top)
            pts.append(f"{x:.1f},{y:.1f}")
        return " ".join(pts)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#faf8f2"/>',
        '<text x="100" y="40" font-family="Georgia, serif" font-size="24" fill="#111">Figure 4. First-Responder Discount</text>',
        '<text x="100" y="60" font-family="Arial, sans-serif" font-size="12" fill="#555">The first visible reply earns the most diligence credit and the highest downstream extraction risk.</text>',
    ]

    for value in range(0, 11, 2):
        y = scale(value, 0.0, 10.0, margin_top + chart_h, margin_top)
        parts.append(f'<line x1="{margin_left}" y1="{y:.1f}" x2="{margin_left + chart_w}" y2="{y:.1f}" stroke="#e2ddd2" stroke-width="1"/>')
        parts.append(f'<text x="68" y="{y + 4:.1f}" font-family="Arial, sans-serif" font-size="12" fill="#666">{value}</text>')

    parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{margin_top + chart_h}" stroke="#333" stroke-width="2"/>')
    parts.append(f'<line x1="{margin_left}" y1="{margin_top + chart_h}" x2="{margin_left + chart_w}" y2="{margin_top + chart_h}" stroke="#333" stroke-width="2"/>')

    for i, label in enumerate(labels):
        x = margin_left + i * step
        parts.append(f'<text x="{x:.1f}" y="{margin_top + chart_h + 28}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#333">{escape(label)}</text>')

    parts.extend(
        [
            f'<polyline fill="none" stroke="#111" stroke-width="4" points="{points(diligence)}"/>',
            f'<polyline fill="none" stroke="#b35c1e" stroke-width="4" points="{points(hazard)}"/>',
            '<text x="800" y="110" font-family="Arial, sans-serif" font-size="13" fill="#111">Diligence credit</text>',
            '<line x1="760" y1="105" x2="790" y2="105" stroke="#111" stroke-width="4"/>',
            '<text x="800" y="135" font-family="Arial, sans-serif" font-size="13" fill="#b35c1e">Assignment hazard</text>',
            '<line x1="760" y1="130" x2="790" y2="130" stroke="#b35c1e" stroke-width="4"/>',
            '<text x="100" y="435" font-family="Arial, sans-serif" font-size="12" fill="#555">Interpretation: once one acceptable “received” has appeared, later replies become mostly ceremonial.</text>',
            '</svg>',
        ]
    )
    (FIGURES / "first_responder_discount.svg").write_text("\n".join(parts))


def render_role_obligation_matrix() -> None:
    width, height = 960, 540
    margin_left, margin_top, chart_w, chart_h = 120, 90, 660, 320
    roles = [
        ("First-author junior", 2.2, 9.1, "#7a1f1f"),
        ("Procurement steward", 7.1, 8.2, "#8b5e34"),
        ("Experiment operator", 4.0, 8.8, "#3d6e70"),
        ("Postdoc proxy", 6.1, 7.0, "#5d4d8c"),
        ("Generic bystander", 2.4, 4.0, "#6b6b6b"),
        ("Muddy-water fish", 1.2, 2.1, "#4f6d42"),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#faf8f2"/>',
        '<text x="120" y="40" font-family="Georgia, serif" font-size="24" fill="#111">Figure 5. Role Obligation Matrix</text>',
        '<text x="120" y="60" font-family="Arial, sans-serif" font-size="12" fill="#555">The funniest roles often combine high obligation with low veto power.</text>',
        f'<rect x="{margin_left}" y="{margin_top}" width="{chart_w}" height="{chart_h}" fill="#fffdf8" stroke="#d9d0c2"/>',
        f'<line x1="{margin_left + chart_w/2}" y1="{margin_top}" x2="{margin_left + chart_w/2}" y2="{margin_top + chart_h}" stroke="#d4c5ae" stroke-width="1.5" stroke-dasharray="6 6"/>',
        f'<line x1="{margin_left}" y1="{margin_top + chart_h/2}" x2="{margin_left + chart_w}" y2="{margin_top + chart_h/2}" stroke="#d4c5ae" stroke-width="1.5" stroke-dasharray="6 6"/>',
        f'<line x1="{margin_left}" y1="{margin_top + chart_h}" x2="{margin_left + chart_w}" y2="{margin_top + chart_h}" stroke="#333" stroke-width="2"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{margin_top + chart_h}" stroke="#333" stroke-width="2"/>',
        f'<text x="{margin_left + chart_w/2}" y="{margin_top + chart_h + 38}" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" fill="#333">Veto power</text>',
        f'<text x="42" y="{margin_top + chart_h/2}" transform="rotate(-90 42 {margin_top + chart_h/2})" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" fill="#333">Obligation intensity</text>',
        f'<text x="{margin_left + 26}" y="{margin_top + 24}" font-family="Arial, sans-serif" font-size="12" fill="#666">High obligation / low veto = default tragedy</text>',
        f'<text x="{margin_left + chart_w - 182}" y="{margin_top + chart_h - 14}" font-family="Arial, sans-serif" font-size="12" fill="#666">Low obligation / high veto = pleasant habitat</text>',
    ]

    for title, x_value, y_value, color in roles:
        x = scale(x_value, 0.0, 10.0, margin_left, margin_left + chart_w)
        y = scale(y_value, 0.0, 10.0, margin_top + chart_h, margin_top)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{color}" stroke="#111" stroke-width="1.2"/>')
        parts.append(f'<text x="{x + 14:.1f}" y="{y - 10:.1f}" font-family="Arial, sans-serif" font-size="12" fill="#222">{escape(title)}</text>')

    parts.append('</svg>')
    (FIGURES / "role_obligation_matrix.svg").write_text("\n".join(parts))


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
        '<text x="90" y="38" font-family="Georgia, serif" font-size="24" fill="#111">Figure 2. Latency-Diligence Curve</text>',
        '<text x="90" y="58" font-family="Arial, sans-serif" font-size="12" fill="#555">Reply timing balances diligence, reliability, and assignment hazard.</text>',
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
            '<text x="740" y="145" font-family="Arial, sans-serif" font-size="13" fill="#b35c1e">Assignment hazard</text>',
            '<line x1="700" y1="140" x2="730" y2="140" stroke="#b35c1e" stroke-width="4"/>',
        ]
    )
    parts.append("</svg>")
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
        '<text x="210" y="38" font-family="Georgia, serif" font-size="24" fill="#111">Figure 3. Hierarchy-Specific Acceptable Delay Window</text>',
        '<text x="210" y="58" font-family="Arial, sans-serif" font-size="12" fill="#555">Direct hierarchy compresses the reply window; peer-only contexts permit wider drift.</text>',
        f'<line x1="{margin_left}" y1="{margin_top + 6 * (bar_h + gap)}" x2="{margin_left + chart_w}" y2="{margin_top + 6 * (bar_h + gap)}" stroke="#333" stroke-width="2"/>',
    ]

    for t in [0, 30, 60, 120, 180, 240]:
        x = scale(float(t), 0, 240, margin_left, margin_left + chart_w)
        parts.append(f'<line x1="{x:.1f}" y1="{margin_top - 18}" x2="{x:.1f}" y2="{margin_top + 6 * (bar_h + gap) - 4}" stroke="#e2ddd2" stroke-width="1"/>')
        parts.append(f'<text x="{x:.1f}" y="{margin_top + 6 * (bar_h + gap) + 24}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#333">{t}</text>')

    for i, row in enumerate(rows):
        y = margin_top + i * (bar_h + gap)
        x1 = scale(float(row["optimal_window_low_min"]), 0, 240, margin_left, margin_left + chart_w)
        x2 = scale(float(row["optimal_window_high_min"]), 0, 240, margin_left, margin_left + chart_w)
        penalty = float(row["visibility_penalty"])
        fill = "#9d8f7a" if penalty < 2 else "#b35c1e" if penalty < 4 else "#7a1f1f"
        label = row["sender_hierarchy"].replace("_", " ")
        parts.append(f'<text x="{margin_left - 18}" y="{y + 22}" text-anchor="end" font-family="Arial, sans-serif" font-size="13" fill="#222">{escape(label)}</text>')
        parts.append(f'<rect x="{x1:.1f}" y="{y:.1f}" width="{max(6.0, x2 - x1):.1f}" height="{bar_h}" rx="6" fill="{fill}"/>')
        parts.append(f'<text x="{x2 + 8:.1f}" y="{y + 22}" font-family="Arial, sans-serif" font-size="12" fill="#444">{row["optimal_window_low_min"]}-{row["optimal_window_high_min"]} min</text>')

    parts.extend(
        [
            '<text x="210" y="470" font-family="Arial, sans-serif" font-size="12" fill="#333">Color intensity tracks visibility penalty.</text>',
            '</svg>',
        ]
    )
    (FIGURES / "hierarchy_window_chart.svg").write_text("\n".join(parts))


def main() -> None:
    render_theory_map()
    render_first_responder_discount()
    render_role_obligation_matrix()
    render_latency_curve()
    render_hierarchy_chart()
    print("Rendered SVG figures to paper/figures/")


if __name__ == "__main__":
    main()
