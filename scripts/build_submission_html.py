#!/usr/bin/env python3
"""Build a styled HTML preview from the submission-ready markdown."""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "paper" / "final" / "read-seen-ignored_submission-ready.md"
TARGET = ROOT / "paper" / "final" / "read-seen-ignored_submission-ready.html"


def render_heading(line: str) -> str:
    level = len(line) - len(line.lstrip("#"))
    text = html.escape(line[level + 1 :].strip())
    return f"<h{level}>{text}</h{level}>"


def render_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`(.+?)`", r"<code>\1</code>", escaped)
    return escaped


def render_table(lines: list[str]) -> str:
    rows = []
    for idx, line in enumerate(lines):
        if idx == 1 and set(line.replace("|", "").replace(" ", "")) == {"-", ":"}:
            continue
        cells = [render_inline(cell.strip()) for cell in line.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return ""
    head = "<tr>" + "".join(f"<th>{c}</th>" for c in rows[0]) + "</tr>"
    body = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows[1:])
    return f"<table><thead>{head}</thead><tbody>{body}</tbody></table>"


def build_body(lines: list[str]) -> str:
    out = []
    i = 0
    inserted_figures = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue

        if stripped.startswith("## Table 1.") and not inserted_figures:
            out.append(
                """
<section class="figure-panel">
  <figure>
    <img src="../figures/latency_diligence_curve.svg" alt="Latency diligence curve"/>
    <figcaption>Figure 1. Latency-Diligence Curve.</figcaption>
  </figure>
  <figure>
    <img src="../figures/hierarchy_window_chart.svg" alt="Hierarchy delay window chart"/>
    <figcaption>Figure 2. Hierarchy-Specific Acceptable Delay Window.</figcaption>
  </figure>
</section>
""".strip()
            )
            inserted_figures = True

        if stripped.startswith("#"):
            out.append(render_heading(stripped))
            i += 1
            continue

        if re.match(r"^\d+\.\s", stripped):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                item = re.sub(r"^\d+\.\s*", "", lines[i].strip())
                items.append(f"<li>{render_inline(item)}</li>")
                i += 1
            out.append("<ol>" + "".join(items) + "</ol>")
            continue

        if stripped.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                item = lines[i].strip()[2:]
                items.append(f"<li>{render_inline(item)}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue

        if stripped.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            out.append(render_table(table_lines))
            continue

        para = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith("#") or nxt.startswith("- ") or nxt.startswith("|") or re.match(r"^\d+\.\s", nxt):
                break
            para.append(nxt)
            i += 1
        out.append(f"<p>{render_inline(' '.join(para))}</p>")
    return "\n".join(out)


def main() -> None:
    lines = SOURCE.read_text().splitlines()
    body = build_body(lines)
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Read, Seen, Ignored</title>
  <style>
    :root {{
      --paper: #fcfaf4;
      --ink: #171717;
      --muted: #5b5b5b;
      --accent: #8b5e34;
      --line: #d9d1c2;
      --panel: #f1ebde;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: linear-gradient(180deg, #efe7d6 0%, #f9f6ef 28%, #fcfaf4 100%);
      color: var(--ink);
      font-family: Georgia, "Times New Roman", serif;
      line-height: 1.72;
    }}
    main {{
      max-width: 920px;
      margin: 0 auto;
      padding: 48px 24px 80px;
    }}
    h1, h2, h3 {{
      font-weight: 700;
      line-height: 1.2;
    }}
    h1 {{
      font-size: 2.2rem;
      margin-bottom: 0.35rem;
    }}
    h2 {{
      margin-top: 2.5rem;
      border-top: 1px solid var(--line);
      padding-top: 1.1rem;
      font-size: 1.45rem;
    }}
    h3 {{
      font-size: 1.15rem;
      margin-top: 1.2rem;
    }}
    p, li {{
      font-size: 1.04rem;
    }}
    code {{
      background: #efe6d7;
      padding: 0.1rem 0.35rem;
      border-radius: 4px;
      font-family: "Courier New", monospace;
      font-size: 0.92rem;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1.2rem 0 1.8rem;
      font-size: 0.96rem;
      background: rgba(255,255,255,0.5);
    }}
    th, td {{
      padding: 0.72rem 0.75rem;
      border: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background: #efe6d7;
    }}
    .figure-panel {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
      margin: 2rem 0;
    }}
    figure {{
      margin: 0;
      padding: 18px;
      background: var(--panel);
      border: 1px solid var(--line);
    }}
    img {{
      width: 100%;
      display: block;
      height: auto;
      background: white;
    }}
    figcaption {{
      margin-top: 0.7rem;
      color: var(--muted);
      font-family: Arial, sans-serif;
      font-size: 0.88rem;
    }}
    .meta {{
      color: var(--muted);
      font-family: Arial, sans-serif;
      font-size: 0.95rem;
      margin-bottom: 1.4rem;
    }}
    .lead {{
      background: rgba(255,255,255,0.55);
      border-left: 4px solid var(--accent);
      padding: 18px 18px 18px 20px;
      margin: 1.2rem 0 1.6rem;
    }}
    @media (min-width: 900px) {{
      .figure-panel {{
        grid-template-columns: 1fr 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <div class="meta">VIBE SHITTING submission-ready HTML preview</div>
    <div class="lead">A print-friendly reading version generated from the Markdown manuscript, with embedded SVG figures for quick review and later export.</div>
    {body}
  </main>
</body>
</html>
"""
    TARGET.write_text(html_doc)
    print(f"Wrote {TARGET}")


if __name__ == "__main__":
    main()
