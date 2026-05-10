#!/usr/bin/env python3
"""Build a compact, image-safe PDF revision for the published SHIT article."""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.font_manager import FontProperties


ROOT = Path(__file__).resolve().parents[1]
SOURCE_MD = ROOT / "paper" / "final" / "read-seen-ignored_submission_zh.md"
FIGURE_DIR = ROOT / "paper" / "figures"
OUT_DIR = ROOT / "dist" / "submission" / "shit_revision_20260510"
PNG_DIR = OUT_DIR / "figures_png"
OUT_PDF = OUT_DIR / "read-seen-ignored_submission_zh_revision-fixed.pdf"

PAGE_W = 8.27
PAGE_H = 11.69
MARGIN_X = 0.42
TOP = 11.25
BOTTOM = 0.42
TEXT_W = PAGE_W - 2 * MARGIN_X

BODY_SIZE = 7.15
SMALL_SIZE = 6.2
H2_SIZE = 11.0
H3_SIZE = 8.2
CAPTION_SIZE = 6.4

BODY_LINE = BODY_SIZE / 72 * 1.47
SMALL_LINE = SMALL_SIZE / 72 * 1.32
H2_LINE = H2_SIZE / 72 * 1.32
H3_LINE = H3_SIZE / 72 * 1.28

FIGURE_HEIGHTS = {
    "theory_framework_map": 2.25,
    "latency_diligence_curve": 1.95,
    "hierarchy_window_chart": 2.0,
    "first_responder_discount": 1.9,
    "role_species_windows": 2.0,
    "publication_burden_u_curve": 1.85,
    "role_obligation_matrix": 2.1,
    "red_envelope_shock": 1.95,
}


@dataclass
class TextBlock:
    kind: str
    text: str


@dataclass
class FigureBlock:
    caption: str
    path: Path


def find_cjk_font() -> Path | None:
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return path
    return None


def convert_figures() -> None:
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    for svg in FIGURE_DIR.glob("*.svg"):
        target = PNG_DIR / f"{svg.stem}.png"
        if target.exists() and target.stat().st_mtime >= svg.stat().st_mtime:
            continue
        profile = Path("/tmp") / f"lo-shit-svg-{svg.stem}"
        subprocess.run(
            [
                "libreoffice",
                "--headless",
                f"-env:UserInstallation=file://{profile}",
                "--convert-to",
                "png",
                "--outdir",
                str(PNG_DIR),
                str(svg),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


def clean_inline_markdown(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = text.replace("*", "")
    return text.strip()


def visual_len(text: str) -> float:
    total = 0.0
    for ch in text:
        if ch in "ilI.,;:!| ":
            total += 0.36
        elif ord(ch) < 128:
            total += 0.56
        else:
            total += 1.0
    return total


def wrap_text(text: str, max_units: float) -> list[str]:
    text = clean_inline_markdown(text)
    if not text:
        return []
    lines: list[str] = []
    current = ""
    current_units = 0.0
    for token in re.findall(r"[A-Za-z0-9_./:+-]+|[\u4e00-\u9fff]|[^\s]", text):
        unit = visual_len(token)
        needs_space = bool(current) and re.match(r"[A-Za-z0-9_./:+-]+$", token) and re.search(r"[A-Za-z0-9_./:+-]$", current)
        extra = 0.4 if needs_space else 0.0
        if current and current_units + unit + extra > max_units:
            lines.append(current)
            current = token
            current_units = unit
        else:
            if needs_space:
                current += " "
            current += token
            current_units += unit + extra
    if current:
        lines.append(current)
    return lines


def parse_blocks() -> list[TextBlock | FigureBlock]:
    blocks: list[TextBlock | FigureBlock] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(TextBlock("para", " ".join(line.strip() for line in paragraph)))
            paragraph = []

    for raw in SOURCE_MD.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        image = re.match(r"!\[(.*?)\]\((.*?)\)", line.strip())
        heading = re.match(r"^(#{1,3})\s+(.*)$", line.strip())

        if image:
            flush_paragraph()
            caption = image.group(1).strip()
            rel_path = image.group(2).replace("../figures/", "")
            blocks.append(FigureBlock(caption, PNG_DIR / f"{Path(rel_path).stem}.png"))
            continue

        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            kind = "title" if level == 1 else f"h{level}"
            blocks.append(TextBlock(kind, clean_inline_markdown(heading.group(2))))
            continue

        if not line.strip():
            flush_paragraph()
            continue

        stripped = line.strip()
        if stripped.startswith("|") or stripped.startswith("- ") or re.match(r"^\d+\.\s", stripped):
            flush_paragraph()
            blocks.append(TextBlock("small", stripped))
            continue

        paragraph.append(stripped)

    flush_paragraph()
    return blocks


class PdfLayout:
    def __init__(self, pdf: PdfPages, font: FontProperties | None) -> None:
        self.pdf = pdf
        self.font = font
        self.bold = FontProperties(fname=font.get_file(), weight="bold") if font and font.get_file() else font
        self.page_no = 0
        self.fig = None
        self.ax = None
        self.y = TOP
        self.new_page()

    def new_page(self) -> None:
        if self.fig is not None:
            self.footer()
            self.pdf.savefig(self.fig)
            plt.close(self.fig)
        self.page_no += 1
        self.fig = plt.figure(figsize=(PAGE_W, PAGE_H), facecolor="white")
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, PAGE_W)
        self.ax.set_ylim(0, PAGE_H)
        self.ax.axis("off")
        self.y = TOP

    def footer(self) -> None:
        assert self.ax is not None
        self.ax.plot([MARGIN_X, PAGE_W - MARGIN_X], [0.28, 0.28], color="#d7cfc0", linewidth=0.45)
        self.ax.text(
            PAGE_W - MARGIN_X,
            0.16,
            f"已读、不回、稍后回复 / 第 {self.page_no} 页",
            ha="right",
            va="bottom",
            fontsize=5.2,
            color="#7b6d59",
            fontproperties=self.font,
        )

    def ensure(self, needed: float) -> None:
        if self.y - needed < BOTTOM:
            self.new_page()

    def draw_lines(
        self,
        lines: list[str],
        *,
        size: float,
        line_height: float,
        color: str = "#16130f",
        font: FontProperties | None = None,
        x: float = MARGIN_X,
        indent: float = 0.0,
    ) -> None:
        assert self.ax is not None
        for line in lines:
            self.ensure(line_height * 1.2)
            self.ax.text(
                x + indent,
                self.y,
                line,
                ha="left",
                va="top",
                fontsize=size,
                color=color,
                fontproperties=font or self.font,
            )
            self.y -= line_height

    def text_block(self, block: TextBlock) -> None:
        if block.kind == "title":
            lines = wrap_text(block.text, 38)
            self.ensure(len(lines) * 0.32 + 0.2)
            self.draw_lines(lines, size=15.0, line_height=0.30, color="#22160d", font=self.bold)
            self.y -= 0.14
            return

        if block.kind == "h2":
            lines = wrap_text(block.text, 56)
            self.ensure(len(lines) * H2_LINE + 0.15)
            self.y -= 0.03
            self.draw_lines(lines, size=H2_SIZE, line_height=H2_LINE, color="#7f2e12", font=self.bold)
            self.y -= 0.04
            return

        if block.kind == "h3":
            lines = wrap_text(block.text, 70)
            self.ensure(len(lines) * H3_LINE + 0.08)
            self.draw_lines(lines, size=H3_SIZE, line_height=H3_LINE, color="#4a3828", font=self.bold)
            self.y -= 0.02
            return

        if block.kind == "small":
            lines = wrap_text(block.text, 88)
            self.draw_lines(lines, size=SMALL_SIZE, line_height=SMALL_LINE, color="#27231f", indent=0.06)
            return

        lines = wrap_text(block.text, 76)
        self.draw_lines(lines, size=BODY_SIZE, line_height=BODY_LINE)
        self.y -= 0.035

    def figure_block(self, block: FigureBlock) -> None:
        assert self.ax is not None
        if not block.path.exists():
            self.text_block(TextBlock("small", f"[Figure missing: {block.caption}]"))
            return

        stem = block.path.stem
        target_h = FIGURE_HEIGHTS.get(stem, 1.55)
        img = Image.open(block.path).convert("RGBA")
        ratio = img.width / max(img.height, 1)
        target_w = min(TEXT_W * 0.94, target_h * ratio)
        if target_w < TEXT_W * 0.66:
            target_w = min(TEXT_W * 0.78, target_h * ratio)
        x = (PAGE_W - target_w) / 2
        needed = target_h + 0.33
        self.ensure(needed)
        y_top = self.y
        self.ax.add_patch(
            plt.Rectangle(
                (x - 0.08, y_top - target_h - 0.07),
                target_w + 0.16,
                target_h + 0.14,
                fill=False,
                linewidth=0.55,
                edgecolor="#d4c6ac",
            )
        )
        self.ax.imshow(img, extent=(x, x + target_w, y_top - target_h, y_top), zorder=2)
        self.y -= target_h + 0.09
        caption_lines = wrap_text(block.caption, 88)
        self.draw_lines(caption_lines, size=CAPTION_SIZE, line_height=CAPTION_SIZE / 72 * 1.25, color="#6b4b2f")
        self.y -= 0.09

    def finish(self) -> None:
        if self.fig is not None:
            self.footer()
            self.pdf.savefig(self.fig)
            plt.close(self.fig)
            self.fig = None


def build_pdf() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    convert_figures()
    font_path = find_cjk_font()
    font = FontProperties(fname=str(font_path)) if font_path else None
    with PdfPages(OUT_PDF) as pdf:
        layout = PdfLayout(pdf, font)
        for block in parse_blocks():
            if isinstance(block, FigureBlock):
                layout.figure_block(block)
            else:
                layout.text_block(block)
        layout.finish()
    print(OUT_PDF)


if __name__ == "__main__":
    build_pdf()
