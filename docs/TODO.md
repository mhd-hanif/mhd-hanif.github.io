# TODO — content backlog

Working notes. This directory is excluded from the Jekyll build, so nothing
here is published to the site.

See [`CONTENT.md`](../CONTENT.md) for how to add a teaser, and remember the
build step:

```bash
python3 tools/build-teasers.py
```

Legend: **T** teaser · **P** paper link · **V** video · **C** code · **B** BibTeX · **PP** project page

---

## Publications

### 1. Coverage-Recon: Coordinated Multi-Drone Image Sampling with Online Map Feedback
`_publications/2025-journal-hanif-coverage-recon.md` — *IEEE T-CST, under review*

Currently: T ✅ (shared with the ECC paper) · P ❌ · V ✅ · C ❌ · B ✅ · PP ✅ (points at `map-feedback-coverage`)

- [ ] Replace the teaser with a GIF specific to the journal version — it currently
      reuses `portf_mfc_1.gif`, the same source as the ECC 2025 paper
- [ ] Turn the linked project page into a real one rather than a stub: add video,
      BibTeX, paper link and code
- [ ] Add `paperurl:` once it is public
- [ ] Add `code:` if the implementation is released

### 2. Angle-Aware Coverage with Camera Rotational Motion Control
`_publications/2024-journal-lu-et-al.md` — *SICE JCMSI, 2024*

Currently: T ⚠️ (static `portf_aacc_2.png`) · P ✅ · V ❌ · C ❌ · B ✅ · PP ❌

- [ ] Replace the static PNG teaser with a GIF
- [ ] Add `video:`
- [ ] Add `code:`
- [ ] Create a project page for it and link both ways (`project:` here,
      `publications:` on the project)
- [ ] Confirm the existing `paperurl:` still resolves

### 3. Hierarchical Vessel Safe Operation in a Port through CBF, MPC and RRT-like Spatiotemporal Path Planning
`_publications/2025-book-otsuki-et-al.md` — *Springer book chapter, 2025*

Currently: T ⚠️ (shared with the IFAC paper) · P ❌ · V ❌ · C ❌ · B ✅ · PP ✅

- [ ] Give it its own GIF teaser — currently reuses `portf_ship_1.gif`
- [ ] Add `paperurl:` (Springer chapter link)

### 4. Hyperspectral Imaging for Useful Substance Production Using Rice Plants…
`_publications/2026-paper-uto-brias.md` — *3rd BrIAS Conference, 2026*

Currently: no teaser — falls back to the venue label

- [ ] Use a photo from the BrIAS conference as the teaser

### 5. Hyperspectral Data-Based Growth State Estimation of Rice Plants…
`_publications/2025-paper-uto-epps.md` — *EPPS, 2025*

Currently: no teaser — falls back to the venue label

- [ ] Use a photo from EPPS 2025 as the teaser

### 6. Hierarchical Multi-Robot Data Sampling for Environmental State Estimation through Online Gaussian Process
`_publications/2025-paper-suenaga-et-al.md` — *ECC, 2025*

Currently: no teaser

- [ ] Add a GIF teaser

### 7. Angle-Aware Full 3D Coverage Control with ADMM-based Dynamic Assignment of Charging Stations
`_publications/2024-paper-lu-et-al.md` — *SICE Annual Conference, 2024*

Currently: no teaser · P ✅

- [ ] Add a GIF teaser

### 8. Human Workload Evaluation of Drone Swarm Formation Control using Virtual Reality Interface
`_publications/2023-paper-asavasirikulkij-et-al.md` — *ACM/IEEE HRI, 2023*

Currently: no teaser · P ✅

- [ ] Add a GIF teaser

### 9. Predictive Receding-Horizon Multi-Robot Task Allocation with Moving Tasks
`_publications/2022-paper-martin-et-al.md` — *ECC, 2022*

Currently: T ⚠️ (shared with the Solar Energy journal paper) · P ✅

- [ ] Change the teaser — currently reuses `portf_la_africana_1.gif`, the same
      source as the 2023 Solar Energy paper

### 10. Design and Development of Tube-Launched Unmanned Aerial Vehicle
`_publications/2018-paper-muzammil-et-al.md` — *ICIUS, 2018*

Currently: T ⚠️ (static `portf_folding_wing_2.png`) · P ✅ · PP ✅

- [ ] Use a GIF teaser on the project page for the video

### 11. Design and Implementation of Control System in Hybrid Underwater Glider Vehicle in ROS Environment
`_publications/2018-thesis-hanif-et-al.md` — *B.Sc. thesis, 2018*

Currently: T ⚠️ (static `portf_haug_1.png`) · P ✅ · B ❌ · PP ✅

- [ ] Update the teaser to a GIF
- [ ] Add BibTeX

---

## Cross-cutting

- [ ] **Shared teasers.** Five entries currently reuse a teaser from another
      entry, so pairs of cards look near-identical: Coverage-Recon / ECC 2025
      (`portf_mfc_1.gif`), the vessel chapter / IFAC paper (`portf_ship_1.gif`),
      ECC 2022 / Solar Energy (`portf_la_africana_1.gif`). Two of these are
      already differentiated by a hand-picked frame (`portf_mfc_1_alt.jpg`,
      `portf_mfc_1_alt2.jpg`) — the same trick works for the rest if a distinct
      source isn't available.
- [ ] **Static teasers that could be GIFs.** `2024-journal-lu-et-al`,
      `2018-paper-muzammil-et-al`, `2018-thesis-hanif-et-al`.
- [ ] **No teaser at all.** `2026-paper-uto-brias`, `2025-paper-uto-epps`,
      `2025-paper-suenaga-et-al`, `2024-paper-lu-et-al`,
      `2023-paper-asavasirikulkij-et-al`, `2024-patent-robot-operation-system`,
      `2022-thesis-hanif-et-al`.
- [ ] **Video links.** Only three entries have `video:` set. The CV marks
      several more with a [Video] tag — worth reconciling.

## Open questions from earlier

- [ ] Real date for the AstraZeneca India talk — currently 15 July 2025,
      inferred from a LinkedIn message dated 2 July.
- [ ] Mathematics olympiad range — site says 2012–2016, the CV PDF says
      2012–2014.
- [ ] "Selected Projects" vs "Featured Publications" — headings currently differ
      though both are driven by the same `featured: true` flag.
