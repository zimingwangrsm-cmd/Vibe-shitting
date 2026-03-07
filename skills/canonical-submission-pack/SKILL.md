---
name: canonical-submission-pack
description: Maintain bilingual canonical manuscript packs with synchronized Markdown, HTML previews, metadata, figures, and validation checks. Use when Codex needs to canonicalize EN/ZH paper artifacts, rebuild previews, update submission metadata or README links, or enforce consistency across the submission pack.
---

# Canonical Submission Pack

Use this skill to keep the public paper artifacts coherent.

## Workflow

1. Treat the canonical manuscripts as the source of truth.
   In this repo, the canonical files are:
   - `paper/final/read-seen-ignored_submission_en.md`
   - `paper/final/read-seen-ignored_submission_zh.md`

2. Treat `paper/final/read-seen-ignored_submission-ready.md` as editorial support only.
   Do not promote the working draft back into the public primary artifact unless the project explicitly changes its artifact model.

3. Sync every pack-level file after content changes.
   Review at minimum:
   - `paper/final/submission-metadata.md`
   - `paper/final/submission-checklist.md`
   - `paper/review/shit-fit-review-2026-03-07.md`
   - `paper/review/named-effects-glossary-2026-03-07.md`
   - `README.md`

4. Rebuild previews immediately after manuscript edits.
   Run:
   ```bash
   python scripts/build_submission_html.py
   ```

5. Validate the pack before considering the work complete.
   Run:
   ```bash
   python scripts/check_submission_pack.py
   python scripts/status_report.py
   ```

6. Keep the figure layer wired into the preview layer.
   If you add or rename a figure, update:
   - `scripts/build_submission_html.py`
   - `scripts/check_submission_pack.py`
   - any metadata or README links that expose the figure

7. Keep the public entry points stable.
   README, HTML previews, and metadata should all point to the same canonical story.

## Constraints

- Do not leave EN and ZH manuscripts conceptually out of sync.
- Do not leave metadata pointing at stale titles or old term systems.
- Do not add a new preview artifact without deciding whether it is canonical or auxiliary.

## Resources

- For the file map and standard command loop, read `references/file-map.md`.
