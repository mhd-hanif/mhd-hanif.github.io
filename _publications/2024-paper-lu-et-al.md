---
title: "Angle-Aware Full 3D Coverage Control with ADMM-based Dynamic Assignment of Charging Stations"
collection: publications
category: conferences
permalink: /publication/2024-paper-lu-et-al
project: "/portfolio/angle-aware-coverage/"
date: 2024-08-27
sortdate: 2024-08-27
venue: "SICE Annual Conference, 2024"
venueshort: "SICE"
authors: "Zhiyuan Lu, <span class=\"me\">Muhammad Hanif</span>, Takeshi Hatanaka"
note: "pp. 1119–1124."
teaser: "/images/papers/aacc-admm-teaser.jpg"
thumb: "/images/thumbs/portf_admm_charging.jpg"
paperurl: "https://paperhost.org/proceedings/controls/SICE24/files/0313.pdf"
bibtex: |
  @inproceedings{lu2024admm,
    title     = {Angle-Aware Full 3D Coverage Control with ADMM-based Dynamic Assignment of Charging Stations},
    author    = {Lu, Zhiyuan and Hanif, Muhammad and Hatanaka, Takeshi},
    booktitle = {Proceedings of the SICE Annual Conference},
    pages     = {1119--1124},
    year      = {2024}
  }
---

Angle-aware coverage control assumes the drones stay in the air. Batteries say otherwise: a field
large enough to be worth reconstructing takes longer to cover than a drone can fly, so charging has
to be part of the control problem rather than an interruption to it.

Enforcing a charging constraint is not new. What hurts is *which* station a drone returns to. Fix
the drone-to-station pairing in advance and a drone can end up flying the length of the field to
reach "its" station, wasting exactly the flight time the constraint was meant to protect.

<figure>
  <img src="{{ '/images/papers/aacc-admm-problem.jpg' | relative_url }}" alt="Angle-aware full 3D coverage control: a drone with gimbal camera observing points in the target field" loading="lazy">
  <figcaption>The underlying problem — full 3D angle-aware coverage with a steerable camera, so each drone's state is position plus two gimbal angles.</figcaption>
</figure>

## Approach

This paper assigns stations **dynamically**, through the alternating direction method of multipliers
(ADMM), and folds that assignment into the constraint-based controller from the camera-rotation work.
The QP each drone solves carries four barrier constraints at once:

- coverage performance — the decay rate of the objective stays above γ/n
- battery — the drone can always still reach its assigned station
- gimbal pitch stays within its mechanical limits
- no collision with the nearest drone

Each has a slack variable, so the problem stays feasible even when the specifications conflict.

## Simulation

Built on **ROS 2 Humble** with JAX for JIT compilation and GPU acceleration, four drones modelled on
the DJI Mavic 3E, four charging stations, and takeoff/landing delays added to make the simulator
honest about the cost of going down to charge.

<figure>
  <img src="{{ '/images/papers/aacc-admm-sim.jpg' | relative_url }}" alt="Six snapshots of the ROS 2 simulation showing four drones, their view cones, charging stations as green cylinders, and the field colour-coded by importance" loading="lazy">
  <figcaption>Red is high importance, green is covered. Green cylinders are charging stations — their height and colour show the battery level of the drone currently assigned, and the white line marks the assignment. A reassignment happens between 6 s and 7 s; by 55 s all four drones are on the ground charging; by 400 s the field is nearly green.</figcaption>
</figure>

Against a fixed one-to-one assignment, the dynamic version drives the coverage objective down faster,
for the reason it was designed to: nobody crosses the field to charge.
