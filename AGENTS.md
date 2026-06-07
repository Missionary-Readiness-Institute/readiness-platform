# AGENTS.md

Guidance for future Codex work in this repository.

## Project Purpose

This repository hosts the public GitHub Pages MkDocs site for Missionary Readiness Institute, a missionary readiness training platform. Treat it as a public informational and educational site, not a private LMS or credentialing system.

## Repository Layout

- `mkdocs.yml` configures the MkDocs Material site, theme, navigation, and extensions.
- `docs/` contains public Markdown pages.
- `docs/courses/` contains starter course pages and outlines.
- `site/` is generated build output and should not be edited directly.
- `.github/workflows/` contains deployment automation when present.

## Tone And Content

- Keep language practical, pastoral, humble, and training-focused.
- Avoid sales-heavy wording, exaggerated claims, or promises of certification.
- Do not invent official legal, medical, counseling, immigration, security, tax, or organizational policy details.
- Use placeholders when organizational facts are unknown, especially contact information, effective dates, legal entity names, and licenses.
- Make clear that readiness decisions remain with churches, sending organizations, and responsible leaders.

## Local Commands

- Install dependencies: `python -m pip install -r requirements.txt`
- Preview locally: `mkdocs serve`
- Build and validate: `mkdocs build --strict`

## Editing Guidance

- Edit source files under `docs/`, `mkdocs.yml`, and supporting root config files.
- Do not edit generated files under `site/`.
- Keep navigation paths in `mkdocs.yml` synchronized with Markdown files.
- Run `mkdocs build --strict` after content or navigation changes when dependencies are available.
