---
title: "Efficient Angle-Aware Coverage Control for Large-Scale Map Reconstruction using Drone Networks"
collection: publications
category: manuscripts
permalink: /publication/2024-journal-hanif-et-al
date: 2024-05-01
sortdate: 2024-05-01
venue: "SICE Journal of Control, Measurement, and System Integration, 2024"
venueshort: "SICE JCMSI"
authors: "<span class=\"me\">Muhammad Hanif</span>, Takumi Shimizu, Zhiyuan Lu, Masaya Suenaga, Takeshi Hatanaka"
teaser: "/images/portf_uaacc_1.gif"
motion: "/images/motion/portf_uaacc_1.webp"
thumb: "/images/thumbs/portf_uaacc_1.jpg"
note: "pp. 144–155. Open access."
paperurl: "https://www.tandfonline.com/doi/pdf/10.1080/18824889.2024.2346375"
video: "https://www.youtube.com/watch?v=vk7a_vR_kTw"
featured: true
bibtex: |
  @article{hanif2024angleaware,
    title   = {Efficient Angle-Aware Coverage Control for Large-Scale Map Reconstruction using Drone Networks},
    author  = {Hanif, Muhammad and Shimizu, Takumi and Lu, Zhiyuan and Suenaga, Masaya and Hatanaka, Takeshi},
    journal = {SICE Journal of Control, Measurement, and System Integration},
    volume  = {17},
    number  = {1},
    pages   = {144--155},
    year    = {2024},
    doi     = {10.1080/18824889.2024.2346375}
  }
---

Reconstructing a field in 3D from the air needs images of every point taken from *several* viewing
angles — one angle reconstructs badly, several reconstruct well. Angle-aware coverage control makes
that a control problem: the drones fly a five-dimensional virtual field of viewpoints, three spatial
dimensions plus the horizontal and vertical angle a point is seen from, and every cell of it carries
an importance index that decays as cameras cover it.

<figure>
  <img src="{{ '/images/papers/aacc-problem.jpg' | relative_url }}" alt="The angle-aware coverage problem: a drone at position p_i observing a target field B from horizontal angle theta_h and vertical angle theta_v" loading="lazy">
  <figcaption>The problem. A drone flying at fixed altitude observes points in the target field <em>B</em> from a horizontal angle θ<sub>h</sub> and a vertical angle θ<sub>v</sub> — the two extra dimensions that make the coverage problem five-dimensional.</figcaption>
</figure>

## The problem this paper fixes

The existing controller has a blind spot on large fields. Because the objective function never
evaluates *how far away* an unobserved point is, distant points carry no more urgency than nearby
ones. Small unobserved patches end up scattered across the field, and the drone spends its remaining
flight time crossing the field to pick them off one at a time — wasteful in both time and battery.
On a small testbed this barely shows. On a large field it dominates.

An obvious fix — writing distance directly into the objective — was tried and failed: the drones
stopped exploring and stuck to fixed positions.

## The fix

Rather than change the objective, the paper changes the **nominal input** of the QP. Classical
Voronoi coverage supplies a move-to-centroid term that pulls each drone toward the weighted centroid
of its own Voronoi cell, so distance enters through where the drone *wants* to go while the
angle-aware constraint on the decay rate of the objective still governs what it is *allowed* to do.

<figure>
  <img src="{{ '/images/papers/aacc-architecture.jpg' | relative_url }}" alt="Control architecture: a central computer updates importance indices, and each drone runs Voronoi-based coverage control feeding a QP-based controller" loading="lazy">
  <figcaption>A central computer updates the importance indices, since they depend on every drone's history. Everything after that — the Voronoi nominal input and the QP solve — runs on each drone.</figcaption>
</figure>

## Results

<figure>
  <img src="{{ '/images/papers/aacc-comparison.jpg' | relative_url }}" alt="Colour maps of the importance index over time for the previous controller and the proposed controller" loading="lazy">
  <figcaption>Importance index over time, previous controller (left of each pair) against this one (right). The previous controller leaves scattered unobserved patches; this one sweeps the field in an orderly front.</figcaption>
</figure>

In ROS simulation the difference is consistent:

| Scenario | Previous controller | This controller |
|---|---|---|
| Single drone, large field | J ≈ 0 at ~1300 s | **~900 s** |
| Three drones, large field | ~470 s | **~330 s** |
| Single drone, physical testbed | ~180 s | **~150 s** |

The multi-drone case matters because it answers the obvious objection — that simply adding drones
would shrink each drone's territory enough to hide the problem. It does shrink it, and the advantage
holds anyway.

<figure>
  <img src="{{ '/images/papers/aacc-testbed.jpg' | relative_url }}" alt="The Tokyo Tech Robot Zoo Sky testbed and the schematic of the experimental system" loading="lazy">
  <figcaption>The hardware: Parrot Bebop 2 drones in the Tokyo Tech Robot Zoo Sky testbed, OptiTrack motion capture at 120 fps, laptops as distributed computation nodes because the Bebop's onboard chip accepts only basic velocity input.</figcaption>
</figure>

The testbed is only 2.2 m × 2.2 m, so the field was made *effectively* larger by dropping the drones
to 30% of the simulated altitude — narrowing each field of view enough to preserve the ratio between
what a drone sees and the size of the field. The gap narrows at that scale, as expected, but it does
not close.

Faster completion is also a battery argument, which is the constraint that actually limits these
missions in the field.
