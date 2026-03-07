---
name: canonical-submission-pack
description: Maintain the active manuscript pack with synchronized Markdown, HTML preview, metadata, figures, archive boundaries, and validation checks. Use when Codex needs to keep the current paper artifact model coherent after content or structure changes.
---

# Canonical Submission Pack

Use this skill to keep the public paper artifacts coherent.

## Workflow

1. Treat the active manuscript as the source of truth.
   In this repo, the active file is:
   - `paper/final/read-seen-ignored_submission-ready.md`

2. Treat the active HTML preview as the primary rendered artifact.
   Keep `paper/final/read-seen-ignored_submission-ready.html` in sync with the working manuscript.

3. Sync every pack-level file after content changes.
   Review at minimum:
   - `paper/final/submission-metadata.md`
   - `paper/final/submission-checklist.md`
   - `paper/review/shit-fit-review-2026-03-07.md`
   - `PROJECT_STRUCTURE.md`
   - `social/xiaohongshu/README.md`
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

- Do not leave metadata pointing at stale titles or old term systems.
- Do not leave archived files mixed into the active layer.
- Do not add a new preview artifact without deciding whether it is active or archived.

## Resources

- For the file map and standard command loop, read `references/file-map.md`.
