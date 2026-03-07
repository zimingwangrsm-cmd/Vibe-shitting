#!/usr/bin/env python3
"""Build canonical HTML previews for the EN/ZH submission manuscripts."""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINAL = ROOT / "paper" / "final"

DOCUMENTS = [
    {
        "lang": "en",
        "source": FINAL / "read-seen-ignored_submission_en.md",
        "target": FINAL / "read-seen-ignored_submission_en.html",
        "label": "Canonical English Submission Preview",
    },
    {
        "lang": "zh",
        "source": FINAL / "read-seen-ignored_submission_zh.md",
        "target": FINAL / "read-seen-ignored_submission_zh.html",
        "label": "Canonical Chinese Submission Preview",
    },
]

LANDING_TARGET = FINAL / "read-seen-ignored_submission-ready.html"


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


def parse_front_matter(lines: list[str]) -> tuple[str, list[str], list[str], list[str]]:
    title = ""
    author_lines: list[str] = []
    keyword_lines: list[str] = []
    sections: list[list[str]] = []
    current: list[str] = []
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
        if re.fullmatch(r"\*\*.+\*\*", stripped):
            if current:
                sections.append(current)
            current = []
            i += 1
            continue
        current.append(stripped)
        i += 1

    if current:
        sections.append(current)
    if sections:
        author_lines = sections[0]
    if len(sections) > 1:
        keyword_lines = sections[1]
    return title, author_lines, keyword_lines, lines[i:]


def render_front_matter(title: str, author_lines: list[str], keyword_lines: list[str], label: str) -> str:
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
  </div>
  <div class="meta-grid">
    <section class="meta-card">
      <div class="meta-label">Author</div>
      {authors}
    </section>
    <section class="meta-card">
      <div class="meta-label">Keywords</div>
      {keywords}
    </section>
  </div>
  <div class="working-note">{html.escape(label)}</div>
</header>
""".strip()


def render_main_figure_panel() -> str:
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


def render_single_figure(src: str, alt: str, caption: str) -> str:
    return f"""
<section class="inline-figure">
  <figure>
    <img src="{src}" alt="{alt}"/>
    <figcaption>{caption}</figcaption>
  </figure>
</section>
""".strip()


def build_body(lines: list[str]) -> str:
    out = []
    i = 0
    abstract_wrapped = False
    inserted_main_panel = False

    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            i += 1
            continue

        if stripped.startswith("## ") and not abstract_wrapped:
            heading_html = render_heading(stripped)
            i += 1
            block_lines = []
            while i < len(lines) and not lines[i].strip().startswith("## "):
                block_lines.append(lines[i])
                i += 1
            block_body = build_body(block_lines)
            out.append(f'<section class="abstract-card">{heading_html}{block_body}</section>')
            abstract_wrapped = True
            continue

        if not inserted_main_panel and stripped.startswith("## 4."):
            out.append(render_main_figure_panel())
            inserted_main_panel = True

        if stripped.startswith("### 4.3"):
            out.append(
                render_single_figure(
                    "../figures/first_responder_discount.svg",
                    "First-responder discount chart",
                    "Figure 4. First-Responder Discount.",
                )
            )

        if stripped.startswith("### 4.4"):
            out.append(
                render_single_figure(
                    "../figures/role_obligation_matrix.svg",
                    "Role obligation matrix",
                    "Figure 5. Role Obligation Matrix.",
                )
            )

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


def render_doc(title: str, front: str, body: str, lang: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="{lang}">
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
    .inline-figure {{
      margin: 1.8rem 0 1.6rem;
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


def build_document(config: dict[str, object]) -> None:
    source = config["source"]
    target = config["target"]
    lines = Path(source).read_text().splitlines()
    title, author_lines, keyword_lines, body_lines = parse_front_matter(lines)
    front = render_front_matter(title, author_lines, keyword_lines, str(config["label"]))
    body = build_body(body_lines)
    doc = render_doc(title, front, body, str(config["lang"]))
    Path(target).write_text(doc)


def build_landing_page() -> None:
    landing = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Read, Seen, Ignored Submission Pack</title>
  <style>
    :root {
      --ink: #171717;
      --muted: #5e594f;
      --line: #d7cebf;
      --panel: rgba(255,255,255,0.85);
      --accent: #8b5e34;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      background:
        radial-gradient(circle at top left, rgba(173, 131, 71, 0.10), transparent 28%),
        linear-gradient(180deg, #efe6d4 0%, #f5efe4 26%, #f9f6ef 100%);
      color: var(--ink);
      font-family: Georgia, "Times New Roman", serif;
    }
    main {
      max-width: 920px;
      margin: 0 auto;
      padding: 48px 20px 80px;
    }
    .shell {
      background: var(--panel);
      border: 1px solid var(--line);
      box-shadow: 0 20px 50px rgba(52, 45, 32, 0.08);
      padding: 30px 34px;
    }
    .eyebrow {
      font-family: Arial, sans-serif;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      font-size: 0.8rem;
      color: var(--muted);
      border-bottom: 2px solid var(--ink);
      padding-bottom: 12px;
      margin-bottom: 18px;
    }
    h1 {
      margin: 0 0 12px;
      font-size: clamp(2rem, 4vw, 3rem);
      line-height: 1.1;
    }
    p {
      font-size: 1.04rem;
      line-height: 1.7;
    }
    .grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
      margin-top: 22px;
    }
    .card {
      display: block;
      text-decoration: none;
      color: inherit;
      background: #fbf7ee;
      border: 1px solid var(--line);
      padding: 18px 20px;
    }
    .card strong {
      display: block;
      font-size: 1.08rem;
      margin-bottom: 6px;
    }
    .meta {
      margin-top: 18px;
      padding-top: 14px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-family: Arial, sans-serif;
      font-size: 0.92rem;
    }
    code {
      background: #efe6d7;
      padding: 0.1rem 0.35rem;
      border-radius: 4px;
      font-family: "Courier New", monospace;
      font-size: 0.92rem;
    }
    @media (min-width: 760px) {
      .grid { grid-template-columns: 1fr 1fr; }
    }
  </style>
</head>
<body>
  <main>
    <section class="shell">
      <div class="eyebrow">VIBE SHITTING Submission Pack</div>
      <h1>Read, Seen, Ignored</h1>
      <p>This landing page points to the canonical final artifacts. The English and Chinese manuscripts are the only submission-authoritative texts. The older bilingual file remains an internal editorial synthesis.</p>
      <div class="grid">
        <a class="card" href="read-seen-ignored_submission_en.html">
          <strong>English canonical preview</strong>
          Submission-ready HTML built from <code>read-seen-ignored_submission_en.md</code>.
        </a>
        <a class="card" href="read-seen-ignored_submission_zh.html">
          <strong>Chinese canonical preview</strong>
          Submission-ready HTML built from <code>read-seen-ignored_submission_zh.md</code>.
        </a>
        <a class="card" href="read-seen-ignored_submission_en.md">
          <strong>English canonical manuscript</strong>
          Self-contained Markdown submission file with inlined references.
        </a>
        <a class="card" href="read-seen-ignored_submission_zh.md">
          <strong>Chinese canonical manuscript</strong>
          Self-contained Markdown submission file with inlined references.
        </a>
      </div>
      <div class="meta">Internal editorial synthesis: <code>read-seen-ignored_submission-ready.md</code></div>
    </section>
  </main>
</body>
</html>
"""
    LANDING_TARGET.write_text(landing)


def main() -> None:
    for config in DOCUMENTS:
        build_document(config)
        print(f"Wrote {config['target']}")
    build_landing_page()
    print(f"Wrote {LANDING_TARGET}")


if __name__ == "__main__":
    main()
