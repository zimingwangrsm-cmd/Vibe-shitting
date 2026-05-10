#!/usr/bin/env python3
"""Build a SHIT revision HTML with visible figures for the published article."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "paper" / "final" / "read-seen-ignored_submission_zh.html"
TARGET_DIR = ROOT / "dist" / "submission" / "shit_revision_20260510"
TARGET = TARGET_DIR / "read-seen-ignored_submission_zh_revision-10p.html"


REVISION_CSS = """
<style id="published-revision-css">
@page { size: A4; margin: 8mm 9mm 8mm 9mm; }
html, body { background: #fff !important; }
body {
  font-size: 8.8pt !important;
  line-height: 1.22 !important;
  color: #111 !important;
}
main {
  max-width: none !important;
  padding: 0 !important;
  margin: 0 !important;
}
.paper-shell {
  padding: 7px 9px !important;
  margin: 0 0 6px !important;
  border: 1px solid #ddd !important;
  box-shadow: none !important;
  background: #fff !important;
}
.masthead, .working-note {
  font-size: 6.8pt !important;
  margin: 0 !important;
}
.paper-title {
  font-size: 17pt !important;
  line-height: 1.1 !important;
  margin: 3px 0 5px !important;
}
.meta-grid {
  gap: 5px !important;
  margin-top: 3px !important;
}
.meta-card {
  padding: 4px 6px !important;
}
.meta-label, .meta-line, .keyword-line {
  font-size: 7.2pt !important;
  line-height: 1.15 !important;
}
.abstract-card {
  padding: 6px 9px !important;
  margin: 0 0 7px !important;
  border: 1px solid #ddd !important;
  background: #fff !important;
}
.section-title {
  font-size: 12.4pt !important;
  line-height: 1.12 !important;
  margin: 8px 0 4px !important;
  padding: 0 !important;
}
.subsection-title {
  font-size: 10pt !important;
  line-height: 1.15 !important;
  margin: 5px 0 2px !important;
}
p {
  margin: 0 0 3px !important;
  line-height: 1.22 !important;
}
ol, ul {
  margin: 2px 0 4px 16px !important;
  padding: 0 !important;
}
li {
  margin: 0 0 1px !important;
  line-height: 1.18 !important;
}
.inline-figure {
  margin: 5px 0 7px !important;
  padding: 0 !important;
  page-break-inside: avoid !important;
  break-inside: avoid !important;
}
.inline-figure figure {
  margin: 0 !important;
  padding: 3px !important;
  border: 1px solid #ddd !important;
  background: #fff !important;
}
.inline-figure img {
  display: block !important;
  width: 96% !important;
  height: auto !important;
  max-width: 96% !important;
  max-height: none !important;
  margin: 0 auto !important;
  object-fit: contain !important;
}
figcaption {
  font-size: 7pt !important;
  line-height: 1.05 !important;
  margin-top: 2px !important;
}
table {
  font-size: 7.1pt !important;
  line-height: 1.1 !important;
  margin: 3px 0 !important;
}
th, td {
  padding: 1px 2px !important;
}
code {
  font-size: 7.6pt !important;
}
</style>
"""


def main() -> None:
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    html = SOURCE.read_text(encoding="utf-8")
    html = html.replace("../figures/", "figures/")
    html = html.replace("中文投稿预览", "中文投稿修复版 / Published revision")
    html = html.replace("</head>", REVISION_CSS + "\n</head>")
    TARGET.write_text(html, encoding="utf-8")
    print(TARGET)


if __name__ == "__main__":
    main()
