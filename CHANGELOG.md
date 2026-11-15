# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

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
