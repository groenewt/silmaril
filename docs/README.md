# Silmaril GitHub Pages

A prescriptive computational economics framework built on the 2025 Nobel-winning insights of Mokyr, Aghion, and Howitt.

## Structure

- `index.html` — Main landing page
- `assets/css/main.css` — Stylesheet
- `assets/js/main.js` — Minimal interactions
- `_config.yml` — Jekyll configuration

## Deploying

This site is designed for GitHub Pages. To deploy:

1. Create a repository named `groenewt.github.io` (or enable Pages on an existing repo)
2. Push these files to the `main` branch (or `gh-pages` branch)
3. Enable GitHub Pages in repository settings

## Local Development

```bash
# If you have Jekyll installed
bundle exec jekyll serve

# Or simply open index.html in a browser
# (The site uses minimal Jekyll features and renders fine as static HTML)
```

## Content

The site presents:

1. **The Nobel 2025 Foundation** — How Mokyr's propositional knowledge, Aghion & Howitt's creative destruction model, and the institutional prerequisites for growth inform the framework

2. **The Three Tiers** — Bronze (empirical), Silver (strategic simulation), Gold (formal semantics)

3. **Live Demonstrations** — Agent-based game theory with LLM agents, census data EDA, mechanism design experiments

4. **The Category-Theoretic Why** — Why this mathematics, why now, and how it relates the descriptive work of the 2025 laureates to prescriptive mechanism design

5. **The Formal Substrate** — The Silmaril Encyclopedia volumes on functorial transport (Vol. 20) and evidence/provenance (Vol. 28), grounding the framework in typed, inhabitable, refusal-aware formal structure

## GIF Assets

The site references GIFs from existing repositories:
- `ollama_games` — Game theory simulations
- `bronze__acs_eda` — Census data flows
- `Icarus-` — Hypergraph evolution

Ensure these repos have GIF assets in their `docs/images/` directories, or update the paths in `index.html`.
