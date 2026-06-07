# Missionary Readiness Institute

Public website and emerging training platform for Missionary Readiness Institute.

The site is built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). It is designed for GitHub Pages and currently contains public institute pages, policy drafts, a course catalog, foundational course materials, and static visual assets.

The platform is not an accredited school, seminary, mission board, sending agency, full LMS, or certification ecosystem. It is a lightweight public training resource for practical missionary readiness.

## Local Development

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Preview the site:

```bash
mkdocs serve
```

Build and validate:

```bash
mkdocs build --strict
```

## Deployment

The GitHub Actions workflow in `.github/workflows/deploy.yml` builds the MkDocs site and deploys the generated `site/` artifact to GitHub Pages when changes are pushed to `main`.

Generated files under `site/` are ignored and should not be edited directly.

## Local-Only Workspace

Local planning files, source references, private notes, and draft graphics can be kept under `local-workspace/`. That folder is ignored by git and should not be used for public site content.
