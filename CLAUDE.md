# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A reveal.js presentation for an MBA lecture at Politecnico di Milano — *"Agents in action"* by Francesco Gianferrari Pini (Quantyca). The lecture covers LLMs, conversational agents, closed vs open models, tools, and context engineering.

## Running the presentation

```bash
cd lezione-mba
python server.py   # serves on http://localhost:8000/presentation.html
```

`server.py` is a no-cache HTTP server — always serves fresh files. Open `presentation.html` in a browser. The repo-root `index.html` is just a meta-refresh redirect to `lezione-mba/presentation.html`; it is not an alternate entry point.

## Architecture

The presentation is fully static HTML + reveal.js (loaded from CDN). No build step.

- `lezione-mba/presentation.html` — entry point; dynamically fetches and injects all slide files via `Promise.all(fetch(...))`, then initializes Reveal.js
- `lezione-mba/slides/slideN-name.html` — one `<section>` per file, containing a single slide
- `lezione-mba/svg/` — standalone SVG diagrams embedded into slides
- `lezione-mba/styles.css` — all custom CSS; dark theme with CSS variables
- `lezione-mba/img/` — images (e.g., Memento poster)

**Slide loading order** is controlled by the `slideFiles` array in `presentation.html`. Slides render in array order regardless of file names — the array may re-order slides relative to their numeric filenames (e.g. `slide14` and `slide15` currently precede `slide13`). Section-divider files (`slide-div-sec1.html` … `slide-div-sec4.html`) are interspersed in this array and do not carry a slide number in their filename.

**External dependencies** (CDN, no install needed):
- reveal.js 5.1.0
- Font Awesome 6.5.1 — used in slides via `<i class="fa-solid fa-...">` icons
- Google Fonts: Inter, JetBrains Mono

## Adding a new slide

1. Create `lezione-mba/slides/slideN-name.html` with a single `<section>` element
2. Append the filename to the `slideFiles` array in `presentation.html`
3. Update the spec file for the relevant section

## Spec files

The slide spec lives in `spec/`, one file per section. Filenames contain a **space before the number** — quote them when passing to shell tools:
- `spec/slide-specs-section 1.md` — Section 1: LLM fundamentals
- `spec/slide-specs-section 2.md` — Section 2: conversational agents
- `spec/slide-specs-section 3.md` — Section 3: closed vs open models
- `spec/slide-specs-section 4.md` — Section 4: tools, context, sub-agents, agentic loop
- `spec/slide-specs-section 5.md` — Section 5: tool types catalog (API tools, MCP, browser use, code execution, Deep Research)

**Always update the spec and `presentation.html` together** — they are the single source of truth for slide content and order. Slides are numbered from 1. When editing a slide, also update the matching entry in the relevant `spec/slide-specs-section N.md`.

## Slide conventions

- Each slide file contains exactly one `<section>` element
- Section-divider slides use `class="section-divider" data-state="is-section-divider"` on the `<section>`
- Typography and color use CSS variables defined in `styles.css`; do not hardcode values that duplicate variables

Key CSS variables:
```
--primary-color: #00b4d8    /* cyan accent — use for highlights, SVG accents */
--secondary-color: #e77f67  /* warm accent — use sparingly */
--text-color: #e8e8e8
--muted-color: #8892a0
--line-color: #2a2a4a
--mono-font: "JetBrains Mono", monospace
--slide-padding: 60px
--slide-padding-top: 40px
--content-gap: 25px
--box-radius: 8px
```

- SVG diagrams are monochromatic with a single accent color (`--primary-color: #00b4d8`); avoid multiple accent colors in a single SVG

## Visual verification with Playwright

Playwright is installed locally (Python 1.58, CLI 1.59 via `npx`). Use it to verify slide rendering instead of relying on HTML diffs alone — layout/overflow bugs only show up in a real browser.

Typical flow: start `python server.py` in `lezione-mba/`, then drive a headless Chromium via `python -c "from playwright.sync_api import ...; ..."` to navigate to `http://localhost:8000/presentation.html#/<slide-index>` and take a screenshot. Read the screenshot back to check layout, overflow, SVG alignment, etc.

Use it after non-trivial slide edits or CSS changes before declaring the task done.
