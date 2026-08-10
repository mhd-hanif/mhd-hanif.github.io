---
title: "Impact of Real-time Map Feedback on Coordinated Image Sampling for 3D Reconstruction"
collection: publications
category: conferences
permalink: /publication/2025-paper-hanif-et-al
project: "https://htnk-lab.github.io/map_feedback_coverage/"
date: 2025-06-24
sortdate: 2025-06-24
venue: "European Control Conference (ECC), 2025"
venueshort: "ECC"
authors: "<span class=\"me\">Muhammad Hanif</span>*, Takumi Sumino*, Kuniaki Uto, Daisuke Ichihashi, Kelvin Cheng, Takeshi Hatanaka"
note: "pp. 1372–1379. *These authors contributed equally."
teaser: "/images/portf_mfc_1.gif"
thumb: "/images/thumbs/portf_mfc_1.jpg"
motion: "/images/motion/portf_mfc_1.webp"
paperurl: "https://ieeexplore.ieee.org/document/11187242"
video: "https://www.youtube.com/watch?v=ZhDbBBvplhY"
bibtex: |
  @inproceedings{hanifimpact2025,
    author    = {Hanif, Muhammad and Sumino, Takumi and Uto, Kuniaki and Ichihashi, Daisuke and Cheng, Kelvin and Hatanaka, Takeshi},
    booktitle = {2025 European Control Conference (ECC)},
    title     = {Impact of Real-time Map Feedback on Coordinated Image Sampling for 3D Reconstruction},
    year      = {2025},
    pages     = {1372--1379},
    doi       = {10.23919/ECC65951.2025.11187242}
  }
---

Sampling images efficiently from diverse viewing angles is what determines the quality of a
reconstructed 3D map, and coverage control is a natural fit for coordinating that across a drone team.
With real-time reconstruction now practical, the map can be rebuilt continuously during the flight —
which means it can be fed straight back into motion control.

This paper asks what that feedback is actually worth.

## Approach

The mission is posed as an **angle-aware coverage control problem**: drones capture the field of
interest from multiple angles rather than merely passing over it. Images are processed in real time by
[NeuralRecon](https://zju3dv.github.io/neuralrecon/) to produce an evolving 3D mesh, and mesh changes
across the field update the coverage importance index as the map develops.

A **QP-based controller** certifies sampling performance by constraining the decay rate of the
objective function, so the guarantee holds even as the importance index keeps shifting underneath it.

## Results

Simulations in Unity and ROS2 show the feedback-driven approach producing a more complete and more
accurate 3D map than the equivalent method without map feedback.

This conference paper is extended by the journal version,
[Coverage-Recon]({{ '/publication/2025-journal-hanif-coverage-recon' | relative_url }}), which adds
multi-drone coordination, real-world experiments and a second feedback formulation.

**Media:** [video](https://www.youtube.com/watch?v=ZhDbBBvplhY) ·
[project page](https://htnk-lab.github.io/map_feedback_coverage/) ·
[PDF](https://drive.google.com/file/d/1cVr2KJHH09B3-o6YiOpDrJROsjY942Jk/view?usp=sharing)
