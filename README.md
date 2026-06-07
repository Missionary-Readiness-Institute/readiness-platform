# Missionary Readiness Institute Readiness Platform

Public website and starter training platform for Missionary Readiness Institute.

The site is built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). It is designed for GitHub Pages and currently contains public institute pages, starter policy pages, and foundational missionary readiness course outlines.

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
