#!/usr/bin/env python3
"""Build a styled working-paper HTML preview from the submission-ready markdown."""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "paper" / "final" / "read-seen-ignored_submission-ready.md"
TARGET = ROOT / "paper" / "final" / "read-seen-ignored_submission-ready.html"


def strip_md(text: str) -> str:
    return text.replace("**", "").strip()


def render_heading(line: str) -> str:
    level = len(line) - len(line.lstrip("#"))
    text = html.escape(line[level + 1 :].strip())
    classes = {
        1: ' class="paper-title"',
        2: ' class="section-title"',
        3: ' class="subsection-title"',
    }
    return f"<h{level}{classes.get(level, '')}>{text}</h{level}>"


def render_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`(.+?)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"(?<!\*)\*(.+?)\*(?!\*)", r"<em>\1</em>", escaped)
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


def extract_front_matter(lines: list[str]) -> tuple[str, str, list[str], list[str], list[str]]:
    title = ""
    chinese_title = ""
    author_lines: list[str] = []
    keyword_lines: list[str] = []
    state = ""
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()
        if i == 0 and stripped.startswith("# "):
            title = stripped[2:].strip()
            i += 1
            continue
        if stripped.startswith("## "):
            break
        if not stripped:
            i += 1
            continue
        if stripped == "**Author / 作者**":
            state = "author"
            i += 1
            continue
        if stripped == "**Keywords / 关键词**":
            state = "keywords"
            i += 1
            continue
        if stripped.startswith("**") and stripped.endswith("**") and not chinese_title:
            chinese_title = strip_md(stripped)
            i += 1
            continue
        if state == "author":
            author_lines.append(stripped)
        elif state == "keywords":
            keyword_lines.append(stripped)
        elif not chinese_title:
            chinese_title = strip_md(stripped)
        i += 1

    return title, chinese_title, author_lines, keyword_lines, lines[i:]


def render_front_matter(title: str, chinese_title: str, author_lines: list[str], keyword_lines: list[str]) -> str:
    authors = "".join(f"<div class=\"meta-line\">{render_inline(line)}</div>" for line in author_lines)
    keywords = "".join(f"<div class=\"keyword-line\">{render_inline(line)}</div>" for line in keyword_lines)
    return f"""
<header class="paper-shell">
  <div class="masthead">
    <div>VIBE SHITTING Working Paper Series</div>
    <div>No. 01 / March 2026</div>
  </div>
  <div class="title-block">
    <h1 class="paper-title">{html.escape(title)}</h1>
    <div class="paper-subtitle">{render_inline(chinese_title)}</div>
  </div>
  <div class="meta-grid">
    <section class="meta-card">
      <div class="meta-label">Author / 作者</div>
      {authors}
    </section>
    <section class="meta-card">
      <div class="meta-label">Keywords / 关键词</div>
      {keywords}
    </section>
  </div>
  <div class="working-note">
    Submission-ready preview with embedded SVG figures and working-paper styling for review, export, and social sharing.
  </div>
</header>
""".strip()


def figure_panel() -> str:
    return """
<section class="figure-panel">
  <figure>
    <img src="../figures/theory_framework_map.svg" alt="Theory framework map"/>
    <figcaption>Figure 1. Theoretical Framework and Group-Chat Game.</figcaption>
  </figure>
  <figure>
    <img src="../figures/latency_diligence_curve.svg" alt="Latency diligence curve"/>
    <figcaption>Figure 2. Latency-Diligence Curve.</figcaption>
  </figure>
  <figure>
    <img src="../figures/hierarchy_window_chart.svg" alt="Hierarchy delay window chart"/>
    <figcaption>Figure 3. Hierarchy-Specific Acceptable Delay Window.</figcaption>
  </figure>
</section>
""".strip()


def build_body(lines: list[str], allow_figures: bool = True) -> str:
    out = []
    i = 0
    inserted_figures = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue

        if stripped in {"## Abstract", "## 中文摘要"}:
            heading_html = render_heading(stripped)
            i += 1
            block_lines = []
            while i < len(lines) and not lines[i].strip().startswith("## "):
                block_lines.append(lines[i])
                i += 1
            block_body = build_body(block_lines, allow_figures=False)
            out.append(f'<section class="abstract-card">{heading_html}{block_body}</section>')
            continue

        if allow_figures and not inserted_figures and stripped.startswith("## 4. Results"):
            out.append(figure_panel())
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
    title, chinese_title, author_lines, keyword_lines, body_lines = extract_front_matter(lines)
    body = build_body(body_lines)
    front = render_front_matter(title, chinese_title, author_lines, keyword_lines)

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      --paper: #f9f6ef;
      --shell: #fffdf9;
      --ink: #171717;
      --muted: #5e594f;
      --accent: #8b5e34;
      --line: #d7cebf;
      --panel: #f0e8da;
      --soft: #f6f1e8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background:
        radial-gradient(circle at top left, rgba(173, 131, 71, 0.10), transparent 28%),
        linear-gradient(180deg, #efe6d4 0%, #f5efe4 26%, #f9f6ef 100%);
      color: var(--ink);
      font-family: Georgia, "Times New Roman", serif;
      line-height: 1.72;
    }}
    main {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 40px 20px 80px;
    }}
    .paper-shell {{
      background: rgba(255,255,255,0.82);
      border: 1px solid var(--line);
      box-shadow: 0 20px 50px rgba(52, 45, 32, 0.08);
      padding: 30px 34px 28px;
      margin-bottom: 28px;
    }}
    .masthead {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      font-family: Arial, sans-serif;
      font-size: 0.82rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
      padding-bottom: 14px;
      border-bottom: 2px solid var(--ink);
    }}
    .title-block {{
      padding: 22px 0 18px;
    }}
    .paper-title {{
      margin: 0;
      font-size: clamp(2rem, 4vw, 3.2rem);
      line-height: 1.1;
      text-wrap: balance;
    }}
    .paper-subtitle {{
      margin-top: 10px;
      font-size: 1.12rem;
      color: var(--muted);
    }}
    .meta-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
      margin-top: 10px;
    }}
    .meta-card {{
      background: var(--soft);
      border: 1px solid var(--line);
      padding: 16px 18px;
    }}
    .meta-label {{
      font-family: Arial, sans-serif;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-size: 0.76rem;
      color: var(--muted);
      margin-bottom: 8px;
    }}
    .meta-line, .keyword-line {{
      font-size: 1rem;
    }}
    .working-note {{
      margin-top: 16px;
      padding-top: 14px;
      border-top: 1px solid var(--line);
      font-family: Arial, sans-serif;
      font-size: 0.92rem;
      color: var(--muted);
    }}
    section, table, p, ul, ol {{
      margin-left: auto;
      margin-right: auto;
    }}
    h2, h3 {{
      font-weight: 700;
      line-height: 1.22;
    }}
    .section-title {{
      margin-top: 2.6rem;
      margin-bottom: 0.8rem;
      padding-top: 1rem;
      border-top: 1px solid var(--line);
      font-size: 1.5rem;
    }}
    .subsection-title {{
      font-size: 1.14rem;
      margin-top: 1.28rem;
      margin-bottom: 0.5rem;
    }}
    p, li {{
      font-size: 1.04rem;
    }}
    strong {{
      font-weight: 700;
    }}
    em {{
      font-style: italic;
    }}
    code {{
      background: #efe6d7;
      padding: 0.1rem 0.35rem;
      border-radius: 4px;
      font-family: "Courier New", monospace;
      font-size: 0.92rem;
    }}
    .abstract-card {{
      background: rgba(255,255,255,0.78);
      border: 1px solid var(--line);
      border-left: 5px solid var(--accent);
      padding: 18px 20px 8px;
      margin: 0 0 22px;
    }}
    .abstract-card .section-title {{
      margin-top: 0;
      padding-top: 0;
      border-top: none;
      font-size: 1.25rem;
    }}
    .figure-panel {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 22px;
      margin: 2.2rem 0;
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
      margin-top: 0.75rem;
      color: var(--muted);
      font-family: Arial, sans-serif;
      font-size: 0.88rem;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1.2rem 0 1.8rem;
      font-size: 0.96rem;
      background: rgba(255,255,255,0.58);
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
    @media (min-width: 860px) {{
      .meta-grid {{
        grid-template-columns: 1fr 1fr;
      }}
    }}
    @media (min-width: 960px) {{
      .figure-panel {{
        grid-template-columns: 1.18fr 1fr 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main>
    {front}
    <article class="paper-shell">
      {body}
    </article>
  </main>
</body>
</html>
"""
    TARGET.write_text(html_doc)
    print(f"Wrote {TARGET}")


if __name__ == "__main__":
    main()
