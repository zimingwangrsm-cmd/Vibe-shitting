# Published PDF Revision / 已发布稿 PDF 修复包

Article ID: `b3245a90-8cb1-4275-a5a9-4ac5f3300885`

Live article: `https://shitjournal.org/article/b3245a90-8cb1-4275-a5a9-4ac5f3300885`

## Files

- `read-seen-ignored_submission_zh_revision-fixed.pdf`: 5-page PDF revision with embedded figures.
- `read-seen-ignored_submission_zh_revision-10p.html`: compact HTML diagnostic export.
- `figures_png/`: rasterized figure inputs used by the PDF builder.
- `figures/`: source figure copy for the diagnostic HTML.

## Verification

- `pdfinfo`: 5 A4 pages.
- `pdfimages`: embedded image objects present.
- Online `v=2` PDF downloaded from SHIT matched this local PDF byte-for-byte after replacement.

## Update Log

- 2026-05-10: original published PDF was found to have missing or undersized figures.
- 2026-05-10: generated a fixed embedded-figure PDF and replaced the article attachment through the SHIT edit endpoint.
- 2026-05-10: SHIT API response after replacement: `文章更新成功，已提交预审`; article status changed from `passed` to `checking`.
