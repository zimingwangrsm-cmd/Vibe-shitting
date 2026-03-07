# Canonical Pack File Map

## Active manuscript

- `paper/final/read-seen-ignored_submission-ready.md`

## Generated preview

- `paper/final/read-seen-ignored_submission-ready.html`

## Pack support files

- `paper/final/submission-metadata.md`
- `paper/final/submission-checklist.md`
- `paper/review/shit-fit-review-2026-03-07.md`
- `paper/review/named-effects-glossary-2026-03-07.md`
- `paper/figures/visual-explainer-plan.md`
- `paper/figures/banana-prompt-pack.md`
- `PROJECT_STRUCTURE.md`
- `social/xiaohongshu/README.md`

## Standard command loop

```bash
python scripts/build_submission_html.py
python scripts/check_submission_pack.py
python scripts/status_report.py
```

## Typical sync targets after a rewrite

- title change
- affiliation change
- keyword change
- renamed concept
- new figure
- changed current-phase link in `README.md`
