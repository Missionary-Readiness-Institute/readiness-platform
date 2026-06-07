# AGENTS.md

Guidance for future Codex work in this repository.

## Purpose

This repo is a GitHub Pages / MkDocs Material site for an online missionary readiness training platform. The platform provides practical, biblically faithful, culturally respectful training for independent missionaries, church members, mission sponsors, and small organizations.

Treat the site as a public informational and educational platform, not a private LMS, degree-granting institution, accredited seminary, or credentialing authority.

## Project Principles

- Keep the tone professional, sober, practical, and mission-oriented.
- Avoid hype, manipulation, triumphalism, or exaggerated claims.
- Write for thoughtful Adventist and broader Christian readers, but avoid unnecessary denominational jargon unless context requires it.
- Respect cross-cultural ministry, local churches, local leaders, family safety, child protection, legal compliance, and ethical mission practice.
- Do not present the site as a degree-granting institution.
- Use "certificate of completion" language, not "accredited certification," unless accreditation is actually obtained.
- Prefer plain Markdown.
- Keep navigation clean and beginner-friendly.
- Preserve MkDocs Material compatibility.
- Do not introduce heavy frameworks unless explicitly requested.
- Do not add authentication, databases, or server-side features unless requested.

## Brand Guidance

- Primary name: `Missionary Readiness Institute`.
- Platform descriptor: `Missionary Readiness Platform`.
- Preferred tagline: `Practical training for faithful cross-cultural service.`
- Keep the brand mature, readable, calm, trustworthy, and simple enough for MkDocs Material.
- Use language such as readiness, biblical faithfulness, cross-cultural humility, accountability, safety, local churches, local leaders, responsible support, and certificate of completion.
- Avoid savior-complex language, militarized ministry language, colonial framing, emotional manipulation, exaggerated promises, and accreditation claims.
- See `docs/project/branding-guide.md` for the fuller starter branding guide.

## Technical Guidance

- Use MkDocs Material conventions.
- Keep docs content under `docs/`.
- Keep public policy pages under `docs/policies/`.
- Keep course content under `docs/courses/`.
- Update `mkdocs.yml` navigation whenever new public pages are added.
- Run or describe the relevant local validation command after changes, such as `mkdocs build --strict`.
- Make small, reviewable changes.
- When unsure, add a TODO note rather than inventing unsupported legal, financial, or accreditation claims.

## Repository Layout

- `mkdocs.yml` configures the MkDocs Material site, theme, navigation, and extensions.
- `docs/` contains public Markdown content.
- `docs/courses/` contains course pages, lessons, knowledge checks, and training content.
- `docs/assets/` contains public static assets used by the site.
- `docs/policies/` should contain public policy and compliance pages.
- `docs/project/` contains internal project guidance and templates; it is excluded from the public MkDocs build.
- `local-workspace/` is ignored by git and can hold private chats, notes, source references, graphics experiments, and quiz drafts.
- `reference-design/` is ignored by git and can hold local design references.
- `site/` is generated build output and should not be edited directly.
- `.github/workflows/` contains deployment automation when present.

## Codex Working Rules

- Inspect the repository before editing, including `mkdocs.yml`, relevant files under `docs/`, and the current git status.
- Summarize planned changes before making broad or structural edits.
- Avoid deleting or overwriting user content unless the task explicitly requires it.
- Preserve the existing site structure unless the task requires refactoring.
- Keep changes focused on the user's request.
- Do not edit generated files under `site/`.
- Keep navigation paths in `mkdocs.yml` synchronized with Markdown files.
- If policy, legal, financial, accreditation, safety, or medical specifics are unknown, use clear TODO placeholders instead of inventing details.

## Local Commands

- Install dependencies: `python -m pip install -r requirements.txt`
- Preview locally: `mkdocs serve`
- Build and validate: `mkdocs build --strict`
