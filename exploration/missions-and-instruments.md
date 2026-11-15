# Missions and Instruments

Status date: November 15, 2026. "Target" dates are agency plans, not guarantees.

## Human spaceflight

### Artemis II (NASA + CSA) — completed
- Launched 2026-04-01 from LC-39B; splashed down off San Diego on 2026-04-10 (8:07 pm EDT).
- Crew: Reid Wiseman (commander), Victor Glover (pilot), Christina Koch and Jeremy Hansen (CSA).
- Free-return lunar flyby, not an orbit or a landing. It set a new distance record for humans: 406,771 km (252,756 mi) from Earth.
- After the Artemis I heat-shield char loss, re-entry used a steeper, shorter profile to limit heating.

### Artemis III / IV (NASA) — planned
- In February 2026 NASA turned Artemis III into a **crewed low-Earth-orbit test**. Orion rendezvous and docks with SpaceX Starship HLS and/or Blue Origin Blue Moon Mk 2 test articles. Target: mid/summer 2027, about two weeks long.
- **Artemis IV** becomes the first crewed landing (south polar region), target 2028.

### Gaganyaan (ISRO) — in progress
- Plan: three uncrewed flights (G1–G3, carrying the half-humanoid robot Vyommitra), then crewed H1.
- G1 has slipped repeatedly (Dec 2024 → Mar 2026 → H2 2026). It is now targeted for **Q4 2026**, with launch trackers listing NET November 2026. Crew-module/service-module separation ground tests were completed in October 2026.
- First crewed flight: 2027 (government statements say 2027–28).

## Robotic science

| Mission | Agency | Status (15 Nov 2026) | Key dates |
|---|---|---|---|
| Europa Clipper | NASA | Cruise, healthy | Earth flyby 2026-12-03 · Jupiter Apr 2030 |
| Tianwen-2 | CNSA | At Kamoʻoalewa | Arrived Jul 2026 · leaves Apr 2027 · capsule Nov 2027 |
| Perseverance | NASA | Extended mission, Jezero | Sapphire Canyon result published 2025-09-10 |
| JWST | NASA/ESA/CSA | Operating | MoM-z14 record (z = 14.44) |
| Chandrayaan-4 | ISRO | Development | First Indian lunar sample return, ~2027–28 |
| Chandrayaan-5 / LUPEX | ISRO + JAXA | Design (approved 2025-03-10) | ISRO lander + JAXA rover, ~2028 |

## Survey observatories

- **Vera C. Rubin Observatory (LSST)**: the 10-year survey began on 2026-06-29/30 (local/UTC). It produces ~10 TB of images and up to ~7 million change alerts per night. The open alert stream is also a real-world benchmark for time-series ML.

## Orbital mechanics worked example

Earth → Mars Hohmann transfer (circular, coplanar orbits; computed in `scripts/generate_figures.py`):

| Quantity | Value |
|---|---|
| Δv₁ (leave Earth's orbit) | 2.95 km/s |
| Δv₂ (match Mars' orbit) | 2.65 km/s |
| Transfer time | ≈ 259 days |

Real missions add Earth escape and Mars capture burns and use launch windows every ~26 months (the synodic period). Try it in the [orbital-mechanics lab](../labs/orbital-mechanics-lab.html).

## Sources

- Engadget, Artemis II splashdown (2026-04-10):
  https://engadget.com/science/space/the-artemis-ii-astronauts-are-back-after-a-10-day-journey-around-the-moon-033800654.html
- Jamaica Gleaner / AP, distance record:
  https://jamaica-gleaner.com/article/news/20260410/moon-flyby-ocean-splashdown-artemis-ii-crew-returns-home
- Aerospace America, Artemis III mid-2027 docking test:
  https://aerospaceamerica.aiaa.org/nasa-eyeing-year-end-tanking-test-and-summer-2027-launch-for-artemis-iii/
- Scientific American, Artemis III landers and Artemis IV landing:
  https://www.scientificamerican.com/article/nasas-artemis-iii-will-pit-spacex-against-blue-origin
- The Week, Gaganyaan separation tests (2026-10-17):
  https://www.theweek.in/news/sci-tech/2026/10/17/are-we-closer-to-uncrewed-gaganyaan-launch-mission-clears-key-test.amp.html
- Space Launch Now, Gaganyaan-1 schedule history:
  https://spacelaunchnow.app/launch/lvm-3-gaganyaan-1
- ISRO, Chandrayaan-5 / LUPEX technical interface meet:
  https://www.isro.gov.in/ISRO%5FEN/ISRO_JAXA_CH5_Technical_Interface_Meet.html
- Rubin LSST start, IFAE (2026-06-30):
  https://www.ifae.es/news/2026/06/30/action-nsfdoe-vera-c.-rubin-observatory-begins-the-greatest-cosmic-movie-ever-made/
