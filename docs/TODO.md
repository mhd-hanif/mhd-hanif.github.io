# TODO — content backlog

Working notes. This directory is excluded from the Jekyll build, so nothing
here is published to the site.

See [`CONTENT.md`](../CONTENT.md) for how to add a teaser and how publication
titles are linked, and remember the build step:

```bash
python3 tools/build-teasers.py
```

Legend: **T** teaser · **P** paper link · **V** video · **C** code · **B** BibTeX · **PP** project page · **W** written body

---

## The elaboration pass

Twelve publications were nominated for elaborate pages built from the source
papers. Eight papers have been supplied and are done; four are still waiting on
a PDF.

### Done

| Publication | Project page | Figures |
|---|---|---|
| Efficient Angle-Aware Coverage Control (SICE JCMSI 2024) | Angle-Aware Coverage — rewritten | 5 |
| Angle-Aware Coverage with Camera Rotational Motion Control (SICE JCMSI 2024) | Angle-Aware Coverage | 3 |
| Angle-Aware Full 3D Coverage with ADMM Charging (SICE 2024) | Angle-Aware Coverage | 2 + teaser |
| Real-time Adaptation of Drone Altitude and Detection Model (SICE 2024) | Drone Target Tracking — rewritten | 5 |
| Human Workload Evaluation… VR Interface (HRI 2023) | **new** — VR Swarm Interface | 2 |
| Automatic Diabetic Retinopathy Classification (TENCON 2020) | DR Screening — rewritten | 1 |
| Brain Tumor Classification Using CNN (WC 2018) | Brain Tumour Classifier — rewritten | 3 |
| Design and Development of Tube-Launched UAV (ICIUS 2018) | Folding-Wing UAV — rewritten | 3 |

### Waiting on a paper

- [ ] **Predictive Receding-Horizon MRTA… Thermosolar Power Plant** —
      `2023-journal-martin-et-al` *(Solar Energy, 2023)*
- [ ] **Predictive Receding-Horizon MRTA with Moving Tasks** —
      `2022-paper-martin-et-al` *(ECC, 2022)*
- [ ] **Hierarchical Vessel Autonomous Operation in a Port** —
      `2023-paper-otsuki-et-al` *(IFAC, 2023)*
- [ ] **Hierarchical Multi-Robot Data Sampling… Online Gaussian Process** —
      `2025-paper-suenaga-et-al` *(ECC, 2025)*

The first three already have project pages to hang the content on
(`multi-robot-task-allocation-thermosolar`, `safe-autonomous-ship-control`).
The Gaussian-process paper still has none — see below.

---

## Remaining per-publication gaps

### Coverage-Recon (`2025-journal-hanif-coverage-recon`)
**Done.** Teaser, authors, arXiv, code, video and external project page all set.

### Angle-Aware Coverage with Camera Rotational Motion Control (`2024-journal-lu-et-al`)
T ✅ · P ✅ · V ❌ · C ❌ · B ✅ · PP ✅ · W ✅
- [ ] Add `video:` — the paper has ROS simulation footage
- [ ] Add `code:` if the group has published the JAX implementation

### Efficient Angle-Aware Coverage (`2024-journal-hanif-et-al`)
T ✅ · P ✅ · V ✅ · B ✅ · PP ✅ · W ✅
- [x] ~~`video:` pointed at the ECC 2025 clip~~ — corrected to `vk7a_vR_kTw`,
      the simulation verification video from the project page
- [ ] There is a second video on the project page (`iLEHCmNdHUs`, the testbed
      run). Only one can go in `video:` — the project page embeds both.

### Real-time Adaptation of Drone Altitude (`2024-paper-hanif-et-al`)
T ✅ · P ✅ · V ✅ · B ✅ · PP ✅ · W ✅ — the `video:` link is the YouTube
playlist cited in the paper.

### Human Workload Evaluation, VR (`2023-paper-asavasirikulkij-et-al`)
T ✅ · P ✅ · B ✅ · PP ✅ · W ✅
- [x] ~~No project page~~ — `_portfolio/vr-swarm-interface.md` created
- [x] ~~`paperurl` DOI~~ — was `3568294.3580060`; the paper's own ACM reference
      block gives `3568294.3580057`. Corrected.
- [ ] **Unverified:** page range `132–136`. The PDF says only "5 pages" and
      ACM DL is unreachable from this environment. Worth a check.
- [ ] The paper cites four supplementary videos [S1]–[S4]. If they are public,
      link one.

### Hierarchical Vessel Safe Operation (`2025-book-otsuki-et-al`)
T ⚠️ (shared with the IFAC paper) · P ❌ · B ✅ · PP ✅
- [ ] Its own teaser — currently reuses `portf_ship_1.gif`
- [ ] Add `paperurl:` (Springer chapter link)

### Hyperspectral rice papers (`2026-paper-uto-brias`, `2025-paper-uto-epps`)
No teaser, no project page — titles fall back to the papers' own pages.
- [ ] Conference photos as teasers
- [ ] Decide whether the hyperspectral work deserves a `_portfolio/` entry

### Gaussian-process data sampling (`2025-paper-suenaga-et-al`)
No teaser, no project page.
- [ ] Teaser
- [ ] A project page would cover this one — nothing on the site does today

### ECC 2022 moving tasks (`2022-paper-martin-et-al`)
T ⚠️ — reuses `portf_la_africana_1.gif`, same source as the Solar Energy paper.
- [ ] Give one of the two its own art

### Tube-launched UAV (`2018-paper-muzammil-et-al`)
T ⚠️ (static) · P ✅ · PP ✅ · W ✅
- [ ] The project page now carries the launch animation; the card teaser is
      still the static render. Could use a frame from the launch clip.

### B.Sc. thesis (`2018-thesis-hanif-et-al`)
T ⚠️ (static `portf_haug_1.png`) · P ✅ · B ❌ · PP ✅
- [ ] GIF teaser
- [ ] Add BibTeX

---

## Cross-cutting

- [x] ~~Coverage-Recon / ECC 2025 shared teaser~~ — resolved.
- [x] ~~Publications with no project page~~ — down from 4 to 3
      (`2026-paper-uto-brias`, `2025-paper-uto-epps`,
      `2025-paper-suenaga-et-al`). Two new `_portfolio/` entries would clear it:
      one for hyperspectral rice, one for GP environmental sampling.
- [ ] **Shared teasers.** Two pairs remain: vessel chapter / IFAC paper
      (`portf_ship_1.gif`), and ECC 2022 / Solar Energy
      (`portf_la_africana_1.gif`).
- [ ] **Static teasers that could move.** `2018-paper-muzammil-et-al`,
      `2018-thesis-hanif-et-al`.
- [ ] **No teaser at all.** `2026-paper-uto-brias`, `2025-paper-uto-epps`,
      `2025-paper-suenaga-et-al`, `2024-patent-robot-operation-system`,
      `2022-thesis-hanif-et-al`.
- [ ] **Video links.** Several CV entries carry a [Video] tag that the site
      does not reflect — worth reconciling in one pass.
- [ ] **Page weight.** `images/portf_folding_wing_0.gif` and `_1.gif` are ~11 MB
      each. `_1` now has a 773 KB WebP used inline; `_0` is still the raw GIF
      behind its card teaser via `motion/`. The originals could be dropped once
      nothing references them.

## Open questions

- [ ] Real date for the AstraZeneca India talk — currently 15 July 2025,
      inferred from a LinkedIn message dated 2 July.
- [ ] Mathematics olympiad range — site says 2012–2016, the CV PDF says
      2012–2014.
- [ ] "Selected Projects" vs "Featured Publications" — headings differ though
      both are driven by the same `featured: true` flag.
