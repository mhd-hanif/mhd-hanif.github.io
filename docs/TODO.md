# TODO — content backlog

Working notes. This directory is excluded from the Jekyll build, so nothing
here is published to the site.

See [`CONTENT.md`](../CONTENT.md) for how to add a teaser and how projects and
publications link to each other, and remember the build step:

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
| Predictive Receding-Horizon MRTA… Thermosolar (Solar Energy 2023) | MRTA Thermosolar — rewritten | 5 |
| Predictive Receding-Horizon MRTA with Moving Tasks (ECC 2022) | MRTA Thermosolar | — |
| Hierarchical Multi-Robot Data Sampling… Online GP (ECC 2025) | **new** — GP Environmental Sampling | 4 + teaser |

The ECC 2022 paper is written as the predecessor of the journal version — the
journal paper states exactly what it added, so the relationship is sourced even
without the ECC PDF.

### Waiting on a paper

- [ ] **Hierarchical Vessel Autonomous Operation in a Port** —
      `2023-paper-otsuki-et-al` *(IFAC, 2023)*. Has a project page already
      (`safe-autonomous-ship-control`) to hang the content on.

That is the last of the twelve.

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
T ✅ · P ✅ · B ✅ · PP ✅ · W ✅
- [x] ~~No teaser~~ — a frame from the hierarchical run
- [x] ~~No project page~~ — `_portfolio/gp-environmental-sampling.md` created
- [x] ~~Add `paperurl:`~~ — IEEE Xplore document 11187026
- [ ] **BibTeX has no `doi:` or page range.** IEEE conference DOIs use the
      document number as the suffix, so this one is almost certainly
      `10.23919/ECC65951.2025.11187026` — matching the pattern of the other
      ECC 2025 entry on this site (`…2025.11187242`, document 11187242). It was
      left out rather than inferred, because a wrong DOI in BibTeX propagates
      into other people's bibliographies. Confirm on the Xplore page and add it,
      along with the page range.

### ECC 2022 moving tasks (`2022-paper-martin-et-al`)
T ⚠️ — reuses `portf_la_africana_1.gif`, same source as the Solar Energy paper.
W ✅ (written as the predecessor of the journal version).
- [ ] Give one of the two its own art. The journal paper's Gazebo and
      La Africana figures are now on the journal page, so the shared GIF is
      less conspicuous — but they are still the same image.

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
- [x] ~~Publications with no project page~~ — down from 4 to 2, both
      hyperspectral rice (`2026-paper-uto-brias`, `2025-paper-uto-epps`). One
      new `_portfolio/` entry would clear it.
- [ ] **Shared teasers.** Two pairs remain: vessel chapter / IFAC paper
      (`portf_ship_1.gif`), and ECC 2022 / Solar Energy
      (`portf_la_africana_1.gif`).
- [ ] **Static teasers that could move.** `2018-paper-muzammil-et-al`,
      `2018-thesis-hanif-et-al`.
- [ ] **No teaser at all.** `2026-paper-uto-brias`, `2025-paper-uto-epps`,
      `2024-patent-robot-operation-system`. Cards falling back to a bare venue
      label are down from 6 to 3.
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
