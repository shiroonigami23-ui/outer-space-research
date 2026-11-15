# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

## [3.0.0] - 2026-11-15 — Encyclopedia website

### Added
- Multi-page site generator `scripts/build_site.py` with mega-menu navigation, instant search (press `/`), mobile tab bar, collapsible site map, back-to-top, dark/light theme
- 33 articles across Journey of the Universe, Stars & the Sun, Black Holes & Exotic Physics, Planets & Life, Exploration and Research Now
- 12 cross-linked catalogs (537 entries) including all 88 constellations
- Research Papers catalog with built-in PDF reader; `fetch-papers.yml` mirrors openly licensed PDFs into `assets/papers/`
- Animated SVG charts and a Statistics page; animated starfield hero
- Live Wikimedia photos and Wikipedia overviews; sounds and sonifications from Wikimedia Commons
- Live tracker as a collapsible bar on every page; paper analyses exported to PDF

### Removed
- All cross-links to the under-water repository (the hubs are now separate)

## [2.0.0] - 2026-11-15 — Research hub

### Added
- Tracks: `small-bodies/` (3I/ATLAS), `black-holes-gw/` (GW250114), `heliophysics/` (Parker Solar Probe)
- `papers/`: 8 structured deep reads + reading list
- `labs/transit-lab.html`: exoplanet transit simulator
- `index.html` GitHub Pages hub homepage, `GLOSSARY.md`
- 6 new generated figures (interstellar objects, 3I orbit, GW area law, chirp, Sun approach records, Hubble tension)

### Changed
- Cosmology: Hubble-tension section (SH0ES vs CCHP) and Euclid DR1
- Astrobiology: TRAPPIST-1 e JWST results
- Tracker: 6 new streams (rows 10–15)
- README, ROADMAP, ARCHITECTURE updated

## [1.1.0] - 2026-11-15

### Added
- Five research tracks with gallery READMEs and dated, sourced notes: `stellar/`, `planetary/`, `cosmology/`, `exploration/`, `astrobiology/`
- `LATEST-ONGOING-RESEARCH-TRACKER.md` with status board, details and the first monthly digest (Nov 2026)
- `labs/orbital-mechanics-lab.html`: interactive Hohmann-transfer lab (Δv, transfer time, phase angle, synodic period; Earth→Mars, Venus↔Earth, Earth→Jupiter, LEO→GEO presets)
- `scripts/generate_figures.py`: 12 generated figures + `gifs/hohmann_transfer.gif`
- `scripts/check_links.py` and `.github/workflows/validate.yml` CI
- `IMAGE-SOURCES.md` attribution file and lab screenshot

### Changed
- README rewritten around the tracks, tracker snapshot and lab; roadmap Phase 2 marked done
- `docs/ARCHITECTURE.md` and `docs/ROADMAP.md` updated for the new structure

## [1.0.1] - 2026-11-13

### Documentation
- Rewrote README with badges, preview, feature & tech-stack tables, architecture diagram and roadmap
- Added `docs/ARCHITECTURE.md` (components, data flow, design decisions)
- Added `docs/ROADMAP.md` (milestones and long-term vision)
- Added real project visuals (demo GIFs / screenshots), SSH / GitHub CLI / ZIP / Codespaces access options and a `.devcontainer`

## [1.0.0] - 2026-03-25

### Added
- Connection model
- Sync workflow
- Hub README
