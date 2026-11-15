# Biosignatures and Habitability

Status date: November 15, 2026.

## Concepts

- **Habitability ≠ inhabited**
  - The working requirements are liquid water, an energy source and the elements CHNOPS. Places that have all three are candidates, not detections.
- **Biosignature**
  - A substance, pattern or structure that life could produce. It only becomes evidence after non-biological routes have been ruled out *in that specific environment*.
- **CoLD scale (Green et al., *Nature* 2021)**
  1. Detect a possible signal
  2. Rule out contamination / instrument artefacts
  3. Show biology could produce it in that environment
  4. Rule out non-biological sources
  5. Find an additional, independent signal
  6. Rule out alternative hypotheses
  7. Confirm predictions with follow-up observations
- The placements in `png/cold_scale_generated.png` are my own working reading of the literature, not an official ranking.

## Case Studies

### K2-18 b — DMS/DMDS in a sub-Neptune atmosphere
- 2023 and April 2025 (Madhusudhan et al.): JWST spectra interpreted as showing dimethyl sulfide and/or dimethyl disulfide. On Earth, DMS comes from marine microbes. The authors proposed a "Hycean" ocean world.
- Pushback:
  - A NASA-led joint reanalysis (preprint, July 2025) found no conclusive DMS and showed that non-biological chemistry can make DMS in hydrogen-rich atmospheres.
  - *The Astronomical Journal*, October 2025: the MIRI signal is dominated by instrument systematics (red noise), and most retrievals with their preferred binning do not favour DMS/DMDS.
- What is robust: methane and CO₂ are detected.
- **Status: contested signal (CoLD 1).**

### Mars — Sapphire Canyon "leopard spots"
- Redox-mineral reaction fronts next to organic matter in 3.5-billion-year-old lake mudstone (*Nature*, 2025-09-10).
- Called a potential biosignature. The key remaining step is ruling out low-temperature non-biological reactions, which really needs Earth labs.
- **Status: strongest Mars candidate so far, CoLD 1 (moving toward 2–3 if samples return).**

### Venus — phosphine (2020)
- A reported phosphine line in the cloud deck. Later reanalyses questioned the calibration and suggested sulfur dioxide or non-biological explanations.
- **Status: disputed.**

### TRAPPIST-1 e — does a habitable-zone Earth-size planet have air?
- JWST NIRSpec/PRISM, 4 transits analysed (DREAMS collaboration; Espinoza et al. and Glidden et al., *ApJL* 990, Sept 2025).
- Results:
  - A primordial hydrogen atmosphere is ruled out, and a CO₂-dominated (Venus/Mars-like) atmosphere is unlikely.
  - The best fit is an **N₂-rich atmosphere with trace CH₄**, *but* a bare rock still cannot be rejected.
  - Starspots on the host star contaminate the spectra. A new program pairs back-to-back transits of TRAPPIST-1 e and the airless TRAPPIST-1 b to subtract the star's signal.
  - ~15 more transits are planned.
- **Status: habitability test in progress; no biosignature claim.**

### Enceladus — plume chemistry
- Organics, salts and phosphates in ocean spray show the ocean is habitable (energy + chemistry). That is not a life signal in itself.
- **Status: strong habitability evidence; no biosignature claim.**

## Lessons (my working notes)

1. Extraordinary claims need **independent instruments**, not just re-binning the same data.
2. **Context matters.** The same molecule can be biological on Earth and non-biological on a hydrogen-rich world.
3. Missions should be designed for steps 2–4 of CoLD, not just step 1. Mars sample return and the Habitable Worlds Observatory are aimed at this.

## Sources

- Astronomy.com, NASA-led K2-18 b reanalysis (2025):
  https://www.astronomy.com/science/new-study-revisits-signs-of-life-on-k2-18-b/
- Astrobiology.com / *The Astronomical Journal*, "K2-18b does not meet the standards of evidence for life" (2025-10-09):
  https://astrobiology.com/2025/10/09/sub-neptune-exoplanet-k2-18b-does-not-meet-the-standards-of-evidence-for-life/
- National Geographic, experts on the K2-18 b claim:
  https://www.nationalgeographic.com/science/article/alien-planet-signs-life-biosignature-exoplanet
- NASA, Sapphire Canyon potential biosignature (2025-09-10):
  https://nasa.gov/news-release/nasa-says-mars-rover-discovered-potential-biosignature-last-year
- Green et al. 2021, "Call for a framework for reporting evidence for life beyond Earth", *Nature* 598: https://doi.org/10.1038/s41586-021-03804-9
- NASA, Webb looks at TRAPPIST-1 e: https://science.nasa.gov/missions/webb/nasa-webb-looks-at-earth-sized-habitable-zone-exoplanet-trappist-1-e
- AAS Nova, Glidden et al. 2025 (doi:10.3847/2041-8213/adf62e): https://aasnova.org/?p=14537
- Paper analyses: [`../papers/hurowitz-2025-sapphire-canyon.md`](../papers/hurowitz-2025-sapphire-canyon.md), [`../papers/k2-18b-2025-debate.md`](../papers/k2-18b-2025-debate.md), [`../papers/trappist-1e-2025-jwst.md`](../papers/trappist-1e-2025-jwst.md)
- Background: https://en.wikipedia.org/wiki/Phosphine_in_the_atmosphere_of_Venus · https://en.wikipedia.org/wiki/Biosignature
