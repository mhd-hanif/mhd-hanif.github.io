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

**DONE.** Teaser now the multi-drone system animation from the official project
page; authors corrected to the journal author list; arXiv paper, code, video and
external project page linked; body written from the project page.

### 2. Angle-Aware Coverage with Camera Rotational Motion Control
`_publications/2024-journal-lu-et-al.md` — *SICE JCMSI, 2024*

Currently: T ✅ (`angle_aware_illustration`, from the Coverage-Recon repo) · P ✅ · V ❌ · C ❌ · B ✅ · PP ✅

- [x] ~~Replace the static PNG teaser with a GIF~~
- [x] ~~Link it to a project page both ways~~ — now a child of
      *Angle-Aware Coverage*
- [ ] Add `video:`
- [ ] Add `code:`
- [ ] Confirm the existing `paperurl:` still resolves

### 3. Hierarchical Vessel Safe Operation in a Port through CBF, MPC and RRT-like Spatiotemporal Path Planning
`_publications/2025-book-otsuki-et-al.md` — *Springer book chapter, 2025*

Currently: T ⚠️ (shared with the IFAC paper) · P ❌ · V ❌ · C ❌ · B ✅ · PP ✅

- [ ] Give it its own GIF teaser — currently reuses `portf_ship_1.gif`
- [ ] Add `paperurl:` (Springer chapter link)

### 4. Hyperspectral Imaging for Useful Substance Production Using Rice Plants…
`_publications/2026-paper-uto-brias.md` — *3rd BrIAS Conference, 2026*

Currently: no teaser — falls back to the venue label · PP ❌

- [ ] Use a photo from the BrIAS conference as the teaser
- [ ] Decide whether the hyperspectral work deserves its own project page —
      without one the title just leads to this paper's own page

### 5. Hyperspectral Data-Based Growth State Estimation of Rice Plants…
`_publications/2025-paper-uto-epps.md` — *EPPS, 2025*

Currently: no teaser — falls back to the venue label · PP ❌

- [ ] Use a photo from EPPS 2025 as the teaser
- [ ] Same project-page question as the BrIAS paper above

### 6. Hierarchical Multi-Robot Data Sampling for Environmental State Estimation through Online Gaussian Process
`_publications/2025-paper-suenaga-et-al.md` — *ECC, 2025*

Currently: no teaser · PP ❌

- [ ] Add a GIF teaser
- [ ] No project page — a Gaussian-process environmental-sampling project would
      cover this one

### 7. Angle-Aware Full 3D Coverage Control with ADMM-based Dynamic Assignment of Charging Stations
`_publications/2024-paper-lu-et-al.md` — *SICE Annual Conference, 2024*

Currently: no teaser · P ✅ · PP ✅

- [ ] Add a GIF teaser

### 8. Human Workload Evaluation of Drone Swarm Formation Control using Virtual Reality Interface
`_publications/2023-paper-asavasirikulkij-et-al.md` — *ACM/IEEE HRI, 2023*

Currently: no teaser · P ✅ · PP ❌

- [ ] Add a GIF teaser
- [ ] No project page — the VR swarm-interface work has none on the site yet

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

- [x] ~~Coverage-Recon / ECC 2025 shared teaser~~ — resolved: Coverage-Recon now
      uses its own animation, ECC keeps `portf_mfc_1`.
- [ ] **Shared teasers.** Two entries still reuse a teaser from another entry:
      the vessel chapter / IFAC paper (`portf_ship_1.gif`), and ECC 2022 /
      Solar Energy (`portf_la_africana_1.gif`). The map-feedback cluster is
      resolved — all three now have their own art.
- [ ] **Static teasers that could be GIFs.** `2018-paper-muzammil-et-al`,
      `2018-thesis-hanif-et-al`.
- [ ] **No teaser at all.** `2026-paper-uto-brias`, `2025-paper-uto-epps`,
      `2025-paper-suenaga-et-al`, `2024-paper-lu-et-al`,
      `2023-paper-asavasirikulkij-et-al`, `2024-patent-robot-operation-system`,
      `2022-thesis-hanif-et-al`.
- [ ] **Video links.** Only three entries have `video:` set. The CV marks
      several more with a [Video] tag — worth reconciling.
- [ ] **Publications with no project page.** Clicking their title lands on the
      paper's own page, which is the intended fallback but the thinnest one:
      `2026-paper-uto-brias`, `2025-paper-uto-epps`, `2025-paper-suenaga-et-al`,
      `2023-paper-asavasirikulkij-et-al`. Two new `_portfolio/` entries — one
      for the hyperspectral rice work, one for VR swarm interfaces — would
      cover all four.

## Open questions from earlier

- [ ] Real date for the AstraZeneca India talk — currently 15 July 2025,
      inferred from a LinkedIn message dated 2 July.
- [ ] Mathematics olympiad range — site says 2012–2016, the CV PDF says
      2012–2014.
- [ ] "Selected Projects" vs "Featured Publications" — headings currently differ
      though both are driven by the same `featured: true` flag.
