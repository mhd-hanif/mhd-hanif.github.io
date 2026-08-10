---
title: "Coverage-Recon: Coordinated Multi-Drone Image Sampling with Online Map Feedback"
collection: publications
category: manuscripts
permalink: /publication/2025-journal-hanif-coverage-recon
project: "https://htnk-lab.github.io/coverage-recon/"
date: 2025-10-21
sortdate: 2025-10-21
venue: "IEEE Transactions on Control Systems Technology, 2025"
venueshort: "IEEE T-CST"
authors: "<span class=\"me\">Muhammad Hanif</span>, Reiji Terunuma, Takumi Sumino, Kelvin Cheng, Takeshi Hatanaka"
note: "arXiv:2510.18347. Extends our ECC 2025 conference paper."
status: "Under review"
teaser: "/images/portf_coverage_recon.webp"
thumb: "/images/thumbs/portf_coverage_recon.jpg"
motion: "/images/motion/portf_coverage_recon.webp"
paperurl: "https://arxiv.org/pdf/2510.18347"
code: "https://github.com/htnk-lab/coverage-recon"
video: "https://www.youtube.com/watch?v=M1L07WQFRPI"
featured: true
featured_order: 1
bibtex: |
  @article{hanif2025coverage,
    title   = {Coverage-Recon: Coordinated Multi-Drone Image Sampling with Online Map Feedback},
    author  = {Hanif, Muhammad and Terunuma, Reiji and Sumino, Takumi and Cheng, Kelvin and Hatanaka, Takeshi},
    journal = {arXiv preprint arXiv:2510.18347},
    year    = {2025}
  }
---

Reconstructing a scene in 3D from a drone team is only as good as the images the team collects, and
good images means covering every keypoint from a range of viewing angles. Coverage control is a
scalable way to coordinate that. What has changed recently is that reconstruction can now run *while
the drones are still flying* — so the map itself can steer the flight.

**Coverage-Recon closes that loop.** Drones follow a QP-based, angle-aware coverage controller that
guarantees multi-view capture and safety. Their images are fused online by
[NeuralRecon](https://zju3dv.github.io/neuralrecon/) into an evolving mesh. Localised changes in that
mesh are read as reconstruction uncertainty and fed back to reshape the coverage importance index, so
the team keeps returning to the regions the map has not yet resolved.

## Angle-aware coverage control

Each drone controls its position *and* its camera orientation — yaw and pitch — giving a five-dimensional
input that scans a five-dimensional virtual field of viewpoints. Every location in that field carries an
importance index: high when unobserved, decaying as the cameras cover it from enough angles.

## Online map feedback

Mesh changes between successive NeuralRecon updates identify under-reconstructed regions. Areas with
large updates are treated as high-importance and raise the coverage index there. The QP-based controller
then routes drones back to those regions while certifying sampling performance — it constrains the decay
rate of the objective — and maintaining safety through control barrier functions.

## Results

Unity–ROS2 simulations and real-world indoor experiments both show more complete and more accurate
reconstructions than the same pipeline without online feedback, and than prior coverage strategies.
Scaling the team from one to two to four drones accelerates convergence of the global objective,
so larger teams finish the mission sooner.

Two feedback variants are evaluated — a 3D-grid formulation and one based on M3C2 mesh distance.

**Media:** [simulation video](https://www.youtube.com/watch?v=M1L07WQFRPI) ·
[experiment video](https://www.youtube.com/watch?v=vX7Z6vx1rc8) ·
[project page](https://htnk-lab.github.io/coverage-recon/) ·
[code](https://github.com/htnk-lab/coverage-recon)
