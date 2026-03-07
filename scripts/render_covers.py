#!/usr/bin/env python3
"""Render SVG covers for the repo and Xiaohongshu posts."""

from __future__ import annotations

import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COVERS = ROOT / "assets" / "covers"


def draw_repo_hero() -> None:
    width, height = 1600, 520
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs>",
        '  <linearGradient id="hero-bg" x1="0" x2="1" y1="0" y2="1">',
        '    <stop offset="0%" stop-color="#f5ecdc"/>',
        '    <stop offset="100%" stop-color="#e6d7bf"/>',
        "  </linearGradient>",
        "</defs>",
        '<rect width="100%" height="100%" fill="url(#hero-bg)"/>',
        '<rect x="56" y="56" width="1488" height="408" fill="none" stroke="#171717" stroke-width="4"/>',
        '<rect x="56" y="56" width="250" height="40" fill="#171717"/>',
        '<text x="78" y="83" font-family="Arial, sans-serif" font-size="18" font-weight="700" fill="#f5efe2">VIBE SHITTING</text>',
        '<line x1="78" y1="146" x2="1520" y2="146" stroke="#b98645" stroke-width="6"/>',
        '<text x="86" y="238" font-family="Georgia, serif" font-size="82" font-weight="700" fill="#111">Read, Seen, Ignored</text>',
        '<text x="86" y="320" font-family="Arial, sans-serif" font-size="34" fill="#4f4a42">A SHIT-style paper on advisor group-chat reply latency.</text>',
        '<text x="86" y="374" font-family="Arial, sans-serif" font-size="28" fill="#5a5348">Chinese manuscript, English manuscript, figures, and share pack.</text>',
        '<text x="86" y="438" font-family="Arial, sans-serif" font-size="24" fill="#222">VIBE SHITTING / GitHub paper archive</text>',
        "</svg>",
    ]
    (COVERS / "repo-hero.svg").write_text("\n".join(svg))


def draw_cover(filename: str, eyebrow: str, title: str, subtitle: str) -> None:
    width, height = 1600, 900
    title_lines = textwrap.wrap(title, width=14)
    subtitle_lines = textwrap.wrap(subtitle, width=24)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs>",
        '  <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">',
        '    <stop offset="0%" stop-color="#f2eadb"/>',
        '    <stop offset="100%" stop-color="#e7dbc6"/>',
        "  </linearGradient>",
        "</defs>",
        '<rect width="100%" height="100%" fill="url(#bg)"/>',
        '<rect x="82" y="82" width="1436" height="736" fill="none" stroke="#1c1c1c" stroke-width="4"/>',
        '<rect x="82" y="82" width="260" height="44" fill="#1c1c1c"/>',
        f'<text x="100" y="111" font-family="Arial, sans-serif" font-size="20" font-weight="700" fill="#f5efe2">{eyebrow}</text>',
        '<line x1="100" y1="198" x2="1500" y2="198" stroke="#b98645" stroke-width="6"/>',
    ]

    y = 290
    for line in title_lines:
        svg.append(f'<text x="100" y="{y}" font-family="Georgia, serif" font-size="92" font-weight="700" fill="#131313">{line}</text>')
        y += 104

    y += 28
    for line in subtitle_lines:
        svg.append(f'<text x="100" y="{y}" font-family="Arial, sans-serif" font-size="34" fill="#4f4a42">{line}</text>')
        y += 52

    svg.extend(
        [
            '<text x="100" y="824" font-family="Arial, sans-serif" font-size="26" fill="#222">VIBE SHITTING / Build in public a SHIT-style paper</text>',
            '<text x="100" y="860" font-family="Arial, sans-serif" font-size="24" fill="#5a5348">沧生 / GitHub + Xiaohongshu public process archive</text>',
            "</svg>",
        ]
    )
    (COVERS / filename).write_text("\n".join(svg))


def main() -> None:
    draw_repo_hero()
    draw_cover(
        "post-01-origin-cover.svg",
        "POST 01 / ORIGIN",
        "我决定公开造一篇 SHIT 期刊论文",
        "用 vibe coding，把每一步都存进 GitHub。",
    )
    draw_cover(
        "post-02-style-study-cover.svg",
        "POST 02 / STYLE",
        "SHIT 期刊好笑，不是因为它脏",
        "它真正厉害的是把荒谬写得像真的。",
    )
    draw_cover(
        "post-03-topic-vote-cover.svg",
        "POST 03 / VOTE",
        "第一篇写什么，你们来投",
        "我想把它真的做成一篇 SHIT 风格论文。",
    )
    draw_cover(
        "post-04-proposal-cover.svg",
        "POST 04 / PROPOSAL",
        "这玩意现在已经不是梗了，是提案了",
        "我真的给它补了一整套假方法论。",
    )
    draw_cover(
        "post-05-paper-draft-cover.svg",
        "POST 05 / DRAFT",
        "论文正文我已经写出来了",
        "现在它真的越来越像能投的东西。",
    )
    print("Rendered covers to assets/covers/")


if __name__ == "__main__":
    main()
