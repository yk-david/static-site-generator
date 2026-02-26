# Static Site Generator

A beginner-friendly Python static site generator that converts Markdown content into a complete HTML site.

## What this project does

- Reads Markdown files from `content/`
- Converts Markdown blocks and inline syntax into HTML
- Injects each page into `template.html`
- Copies assets from `static/`
- Writes the generated site into `docs/`

## Features

- Recursive page generation from nested folders
- Markdown support for:
  - headings
  - paragraphs
  - code blocks
  - blockquotes
  - ordered and unordered lists
  - bold, italic, inline code, links, and images
- Base path rewriting for deployment under a subdirectory

## Requirements

- Python `3.12+`
- WSL/Linux shell (this repo includes `.sh` scripts)

## Quick start (step by step)

### 1) Generate the site

From the project root:

```bash
python3 src/main.py
```

What happens:

- `docs/` is recreated from scratch
- static assets are copied from `static/` to `docs/`
- Markdown files in `content/` are converted to HTML files in `docs/`

### 2) Preview locally

Serve the generated `docs/` directory:

```bash
cd docs && python3 -m http.server 8888
```

Then open:

- <http://localhost:8888>

### 3) Use the helper script (optional)

```bash
bash build.sh
```

This runs:

```bash
python3 src/main.py "/static-site-generator/"
```

Use this when deploying to a subdirectory path (for example GitHub Pages project sites).

## Run tests

```bash
bash test.sh
```

Equivalent direct command:

```bash
python3 -m unittest discover -s src
```

## How generation works

1. `src/main.py` starts the build.
2. `initialize_public()` recreates `docs/`.
3. `copy_static()` recursively copies files from `static/` to `docs/`.
4. `generate_pages_recursive()` walks `content/` recursively.
5. Each Markdown file is converted to an HTML node tree.
6. `template.html` placeholders are replaced:
   - `{{ Title }}`
   - `{{ Content }}`
7. Final HTML pages are written into mirrored paths under `docs/`.

## Content authoring guide

To add a new page:

1. Create a new Markdown file under `content/`.
2. Make sure it has exactly one H1 title (a line starting with `# `).
3. Re-run the generator:

```bash
python3 src/main.py
```

4. Open the matching generated file in `docs/`.

Example:

- source: `content/blog/new-post/index.md`
- output: `docs/blog/new-post/index.html`

## Project structure

```text
.
├── content/         # Markdown source files
├── docs/            # Generated website output
├── src/             # Generator source code + tests
├── static/          # CSS/images copied as-is
├── template.html    # Shared HTML page template
├── main.sh          # Generate + serve helper
├── build.sh         # Build helper with base path
└── test.sh          # Unit test helper
```

## Notes

- Current generation target is `docs/`.
- `main.sh` currently serves `public/`; if you use it as-is, update it or serve `docs/` manually.
