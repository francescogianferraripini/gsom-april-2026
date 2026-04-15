# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A reveal.js presentation for an MBA lecture at Politecnico di Milano — *"Agents in action"* by Francesco Gianferrari Pini (Quantyca). The lecture covers LLMs, conversational agents, closed vs open models, tools, and context engineering.

## Running the presentation

```bash
cd lezione-mba
python server.py   # serves on http://localhost:8000/presentation.html
```

`server.py` is a no-cache HTTP server — always serves fresh files. Open `presentation.html` in a browser.

## Architecture

The presentation is fully static HTML + reveal.js (loaded from CDN). No build step.

- `lezione-mba/presentation.html` — entry point; dynamically fetches and injects all slide files via `Promise.all(fetch(...))`, then initializes Reveal.js
- `lezione-mba/slides/slideN-name.html` — one `<section>` per file, containing a single slide
- `lezione-mba/svg/` — standalone SVG diagrams embedded into slides
- `lezione-mba/styles.css` — all custom CSS; dark theme with CSS variables (`--primary-color`, `--text-color`, etc.)
- `lezione-mba/img/` — images (e.g., Memento poster)

**Slide loading order** is controlled by the `slideFiles` array in `presentation.html`. Slides render in array order regardless of file names.

## Adding a new slide

1. Create `lezione-mba/slides/slideN-name.html` with a single `<section>` element
2. Append the filename to the `slideFiles` array in `presentation.html`
3. Update the spec file for the relevant section

## Spec files

The slide spec lives in `spec/`:
- `spec/slide-specs-section 1.md` — slides 1–10 (Section 1: LLM fundamentals)
- `spec/slide-specs-section-2.md` — slides 11–18+ (Section 2: conversational agents)

**Always update the spec and `presentation.html` together** — they are the single source of truth for slide content and order. Slides are numbered from 1.

## Slide conventions

- Each slide file contains exactly one `<section>` element
- Section-divider slides use `class="section-divider" data-state="is-section-divider"` on the `<section>`
- Typography uses CSS variables defined in `styles.css`; do not hardcode font sizes or colors that duplicate variables
- SVG diagrams are monochromatic with a single accent color (`--primary-color: #00b4d8`); avoid multiple accent colors in a single SVG
