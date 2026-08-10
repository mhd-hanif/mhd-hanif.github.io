---
title: "Multi-Drone Coordinated Image Sampling for 3D Map Reconstruction through Efficient and Scene-Adaptive Coverage Control"
collection: publications
category: thesis
permalink: /publication/2025-thesis-hanif-phd
date: 2025-07-01
sortdate: 2025-07-01
venue: "Ph.D. Dissertation, Institute of Science Tokyo, 2025"
venueshort: "Ph.D."
authors: "<span class=\"me\">Muhammad Hanif</span>"
note: "Department of Systems and Control Engineering. Advisor: Prof. Takeshi Hatanaka."
teaser: "/images/thumbs/thesis-science-tokyo.jpg"
thumb: "/images/thumbs/thesis-science-tokyo.jpg"
paperurl: "/files/PhD_Thesis_Hanif.pdf"
---

A 3D reconstruction is only as good as the images it is built from — a point seen from one direction
reconstructs poorly, seen from several it reconstructs well. **Angle-aware coverage control** makes
that explicit by treating viewing angle as part of the coverage problem. But the existing strategy
carries two fundamental problems, and this dissertation is organised around fixing them.

First, it is **inefficient on large fields**: drones travel long distances to pick off small unsampled
patches. Second, and more fundamentally, the **measurement granularity has to be fixed in advance** —
even though how densely you need to sample depends on the scene, which is exactly what you don't know
before flying.

## Contribution one — efficiency

The fix for the first problem is to leave the angle-aware objective alone and change what the QP is
*aiming* for: a **Voronoi-based coverage law** becomes the nominal input to the quadratic program. That
keeps the viewpoint diversity angle-aware coverage exists to provide, while giving drones a reason to
head for distant unobserved regions — the thing the original formulation had no way to express.

## Contribution two — scene-adaptivity

The second problem needs feedback from the reconstruction itself. Images stream into
**[NeuralRecon](https://zju3dv.github.io/neuralrecon/)**, which builds an evolving 3D mesh during the
flight; changes in that mesh are quantified and used to update the coverage **importance index**, so
regions where the map is still unresolved pull drones back toward them. The objective is therefore
shifting underneath the controller as it runs — handled with a **QP-based controller** that constrains
the objective's decay rate while enforcing collision avoidance and workspace limits.

## Validation

Simulated in **Unity and ROS 2**, and flown on real UAVs both indoors and outdoors. The efficient
controller improves monitoring efficiency at large scale; the scene-adaptive method produces more
complete and more accurate maps than the equivalent approach without feedback.

The map-feedback line of work is published separately as
[Coverage-Recon]({{ '/publication/2025-journal-hanif-coverage-recon' | relative_url }}). Full technical
detail on the project page:
[Angle-Aware Coverage Control for 3D Map Reconstruction]({{ '/portfolio/angle-aware-coverage/' | relative_url }}).
