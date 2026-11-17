# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).



## [Unreleased] - 2026-11-17 (homepage and tracker)
### Changed
- Homepage catalogs grouped into themed blocks with one-line blurbs; the Browse menu uses the same groups.
- Bigger hero search with suggested searches.
### Added
- Weekly GitHub Action (`update-tracker.yml`) that fetches the newest papers for each live-tracker stream from OpenAlex, adds a 'Latest research' section to the tracker page, updates the tracker date and rebuilds the site.

## [Unreleased] - 2026-11-17
### Added
- In-site reader (`wiki/read.html`): every Wikipedia link now opens the full article inside this site, with images, contents and links that stay in the site; pages we have our own article for open those instead.
### Fixed
- Portrait photos no longer crop off people's heads: crops favour the top of the image and tall portraits are shown whole on article pages.
## [Unreleased] - 2026-11-15
### Added
- More animations: scroll-reveal for cards, charts and sections; count-up hero statistics; 3D tilt on cards; reveal failsafe so content is never hidden.
### Changed
- Generator hardening (numeric subtitles), hero animation scoped per site.

## [3.2.0] - 2026-11-15 — In-depth entries, research panels, auto-sound, larger layout

### Added
- **In depth** section on every catalog entry (full Wikipedia article in collapsible sections) and a **Research & studies** panel (OpenAlex papers with free PDFs)
- Sounds auto-load with 'What it sounds like' notes
- 20 more exoplanets, 16 stars and 20 missions; sound descriptions for every entry (Mars wind, Titan descent, Sputnik beeps, NASA sonifications)

### Changed
- Fluid, larger layout for tablets and wide screens

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
