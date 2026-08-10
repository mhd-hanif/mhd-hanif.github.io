---
title: "Multi-Drone Image Sampling with Online Map Feedback"
collection: portfolio
permalink: /portfolio/map-feedback-coverage/
order: 1
summary: "Coverage control for drone teams that closes the loop with the 3D reconstruction itself — the evolving mesh tells the fleet where the map is still unresolved, and the controller flies them back there."
teaser: "/images/portf_coverage_recon.webp"
thumb: "/images/thumbs/portf_coverage_recon.jpg"
motion: "/images/motion/portf_coverage_recon.webp"
period: "2023 – 2025"
tags:
  - "ROS2"
  - "Unity"
  - "Coverage Control"
  - "3D Reconstruction"
  - "NeuralRecon"
  - "Control Barrier Functions"
code: "https://github.com/htnk-lab/coverage-recon"
video: "https://www.youtube.com/watch?v=M1L07WQFRPI"
featured: true
featured_order: 1
redirect_from:
  - /portfolio/1_1_map-feedback-coverage/
publications:
  - "/publication/2025-journal-hanif-coverage-recon"
  - "/publication/2025-paper-hanif-et-al"
  - "/publication/2025-domestic-sumino-msc"
  - "/publication/2025-thesis-hanif-phd"
---

Reconstructing a scene in 3D from the air is limited less by the reconstruction algorithm than by the
images it is given. A keypoint seen from one angle reconstructs badly; seen from several, it
reconstructs well. So the real question is how a team of drones should move in order to *collect the
right images* — and coverage control is a scalable way to answer it.

Until recently that had to be decided in advance, because the map only existed after the flight. Now
that reconstruction runs in real time, the map can be built while the drones are still flying, which
makes it available as a feedback signal. This project is about using it.

## The loop

**Angle-aware coverage control.** Each drone controls its position *and* its camera orientation — yaw
and pitch — a five-dimensional input scanning a five-dimensional virtual field of viewpoints. Every
location in that field carries an importance index: high while unobserved, decaying as cameras cover
it from enough distinct angles.

**Online map feedback.** Images stream to [NeuralRecon](https://zju3dv.github.io/neuralrecon/), which
fuses them into an evolving mesh. Comparing the mesh between updates localises where it is still
changing — and a region that keeps changing is a region that is not yet resolved. Those areas have
their importance index raised.

**A QP-based controller** turns that shifting index into motion. It certifies sampling performance by
constraining the decay rate of the coverage objective, and enforces safety through control barrier
functions, so the guarantees survive the importance index moving underneath them.

## Validation

Simulated in **Unity and ROS2**, and flown in a **real-world indoor experiment**. Both show more
complete and more accurate reconstructions than the same pipeline without feedback, and than earlier
coverage strategies including lawn-mower sweeps.

Scaling the team from one to two to four drones accelerates convergence of the global objective, so
larger teams finish sooner rather than merely dividing the work.

## Outputs

The work ran from a conference paper at **ECC 2025** to a journal manuscript, **Coverage-Recon**, now
under review at *IEEE Transactions on Control Systems Technology*, which adds multi-drone
coordination, hardware experiments and a second feedback formulation based on M3C2 mesh distance
alongside the original 3D-grid method.

Official project pages, with the full video set:
[Coverage-Recon](https://htnk-lab.github.io/coverage-recon/) ·
[ECC 2025 version](https://htnk-lab.github.io/map_feedback_coverage/)
