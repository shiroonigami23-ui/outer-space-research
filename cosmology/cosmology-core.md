# Cosmology Core

Status date: November 15, 2026.

## Concepts

- **Cosmic microwave background (CMB)**
  - Light released ~380,000 years after the Big Bang, when the universe cooled enough for atoms to form. Its tiny temperature ripples (~1 part in 100,000) seeded all later structure.
- **ΛCDM energy budget (Planck 2018)**
  - Dark energy ≈ 68.5%, dark matter ≈ 26.5%, ordinary (baryonic) matter ≈ 4.9%.
- **Redshift z**
  - Expansion stretches light: 1 + z = (size of universe now) / (size when the light left). Higher z means further back in time.
- **Baryon acoustic oscillations (BAO)**
  - Sound waves in the early plasma left a preferred spacing (~150 Mpc today) between galaxies. Measuring it at many redshifts gives a "standard ruler" for the expansion history.

## Live Debate 1: Is dark energy changing?

- **What DESI reported (2025-03-19, DR2)**
  - Three years of data covering nearly 15 million galaxies and quasars, the largest 3D map yet.
  - DESI on its own is consistent with ΛCDM. Combined with CMB and supernova data, it prefers an evolving dark energy at **2.8–4.2σ**, depending on which supernova sample is used.
- **How to read the plot** (`png/dark_energy_evolution_generated.png`)
  - Uses the common w0–wa parameterisation: w(a) = w0 + wa(1 − a).
  - With w0 ≈ −0.75, wa ≈ −0.86, dark-energy density rises slightly then falls as you look back. In other words, today's dark energy would be *weaker* than its recent peak.
  - The curve is illustrative, not a fit I made.
- **Why caution**
  - 5σ is the discovery threshold, and the signal depends on how supernova datasets are calibrated.

## Live Debate 2: The Hubble tension

![Hubble tension](png/hubble_tension_generated.png)

- Early-universe inference (CMB + ΛCDM) gives H0 ≈ 67 km/s/Mpc. Local distance-ladder measurements (Cepheids + Type Ia supernovae) give ≈ 73 km/s/Mpc.
- **SH0ES (Riess et al.):** JWST re-observed Cepheids, more than 1,000 across several hosts, with ~2% distance precision. Crowding errors in Hubble photometry are now hard to blame. Values: ~73.2, and 72.6 cross-checked with carbon stars and red giants.
- **CCHP (Freedman et al., *ApJ* 2025):** TRGB + JWST gives **70.39 km/s/Mpc**, which the team says is consistent with ΛCDM. Their own Cepheid subset gives 72.04. Critics (e.g. Riess, Scolnic) argue the sample is small and selected from the tail, and that 70.4 sits *in the middle* of the tension rather than resolving it.
- **My read:** the tension is now mostly about *which local calibrator to trust* (Cepheids vs TRGB/JAGB), not about Hubble photometry. Independent methods (lensing time delays, TDCOSMO; gravitational-wave sirens) are the tie-breakers.
- Either there is unrecognised systematic error, or there is new physics. Evolving dark energy alone does not obviously fix it.

## Live Debate 3: Too many early galaxies?

- **MoM-z14**: spectroscopically confirmed at z = 14.44 (~280 Myr after the Big Bang), about 240 light-years across. Paper: Naidu et al., *Open Journal of Astrophysics*, 2026.
- The bright z > 10 population is >100× more abundant than pre-JWST consensus models predicted.
- Leading explanations: bursty star formation, top-heavy stellar populations, or less dust. None of these requires breaking ΛCDM yet.

## Next Data to Watch

- DESI final-year analyses.
- **Euclid DR1** (first major cosmology release, scheduled late Oct 2026, ~2,000 deg²): watch for weak-lensing constraints on dark energy and gravity. The March 2025 quick release already showed ~500 strong-lens candidates and a 380,000-galaxy morphology catalogue.
- Rubin LSST supernova and weak-lensing samples (survey started 2026-06-30).
- New JWST record attempts at z > 15.

## Sources

- DESI DR2 results, Ohio State News (2025-03-19):
  https://news.osu.edu/new-desi-results-strengthen-hints-that-dark-energy-may-evolve
- UT Dallas, "Evidence mounts for evolving dark energy" (2025-03-19):
  https://news.utdallas.edu/science-technology/desi-results-dark-energy-2025
- IFAE, DESI DR2 BAO summary:
  https://cosmolya.ifae.es/post/2025-desi-dr2-bao/
- Live Science, MoM-z14:
  https://www.livescience.com/space/astronomy/previously-unimaginable-james-webb-telescope-breaks-own-record-again-discovering-farthest-known-galaxy-in-the-universe
- Naidu et al., "A Cosmic Miracle" (OJAp 2026): https://doi.org/10.33232/001c.156033
- Physics World, CCHP 70.39 and reactions: https://physicsworld.com/a/cosmic-conflict-continues-new-data-fuel-the-hubble-tension-debate/
- Live Science, Freedman vs Riess: https://www.livescience.com/space/cosmology/one-of-the-universe-s-biggest-paradoxes-could-be-even-weirder-than-we-thought-james-webb-telescope-study-reveals
- Euclid DR1 schedule (EAS 2026 symposium): https://eas.unige.ch/EAS_meeting/session.jsp?id=S10
- Paper analyses: [`../papers/desi-2025-dr2-dark-energy.md`](../papers/desi-2025-dr2-dark-energy.md), [`../papers/naidu-2026-mom-z14.md`](../papers/naidu-2026-mom-z14.md), [`../papers/freedman-2025-cchp-h0.md`](../papers/freedman-2025-cchp-h0.md)
- Background: https://en.wikipedia.org/wiki/Lambda-CDM_model · https://en.wikipedia.org/wiki/Hubble%27s_law#Hubble_tension
