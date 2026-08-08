---
title: "Hierarchical Multi-Robot Data Sampling for Environmental State Estimation through Online Gaussian Process"
collection: publications
category: conferences
permalink: /publication/2025-paper-suenaga-et-al
date: 2025-06-24
sortdate: 2025-06-23
venue: "European Control Conference (ECC), 2025"
venueshort: "ECC"
project: "/portfolio/gp-environmental-sampling/"
authors: "Masaya Suenaga, <span class=\"me\">Muhammad Hanif</span>, Kuniaki Uto, Takeshi Hatanaka"
teaser: "/images/papers/gp-teaser.jpg"
thumb: "/images/papers/gp-teaser.jpg"
paperurl: "https://ieeexplore.ieee.org/abstract/document/11187026"
bibtex: |
  @inproceedings{suenaga2025hierarchical,
    title     = {Hierarchical Multi-Robot Data Sampling for Environmental State Estimation through Online Gaussian Process},
    author    = {Suenaga, Masaya and Hanif, Muhammad and Uto, Kuniaki and Hatanaka, Takeshi},
    booktitle = {Proceedings of the 2025 European Control Conference (ECC)},
    year      = {2025}
  }
---

Coverage control is a good way to send a robot team across a field larger than the robots. It carries
two assumptions that quietly do not hold for environmental monitoring.

**Sensors are not continuous.** Coverage control assumes sampling happens everywhere, all the time.
Real instruments take a reading at a point, at an instant — soil nitrogen on farmland, solar
radiation in a thermosolar plant, chlorophyll in water.

**Gradients are short-sighted.** A coverage command follows the gradient of a function, and a
gradient knows nothing about the far side of the field.

<figure>
  <img src="{{ '/images/papers/gp-scene.jpg' | relative_url }}" alt="Robots moving in a polygonal field, sampling a scalar field at discrete points" loading="lazy">
  <figcaption>Robots take a reading at their own position every t<sub>s</sub> seconds, and the scalar field has to be estimated from those points alone.</figcaption>
</figure>

## Estimating the field

A **sparse online Gaussian process** carries the estimate. What makes a GP the right tool here is
that it reports its own uncertainty: the variance σ²(x) says how much the estimate at each point can
be trusted, which is exactly the signal a controller needs. Sparse and online matter for cost — the
model updates recursively as each reading arrives, and discards basis vectors that contribute little,
so memory and computation do not grow without bound.

The control objective follows directly: drive the summed variance across the field down, and do it at
a certified rate rather than eventually. That decay-rate constraint is enforced by a partially
distributed constraint-based controller — the GP update runs centrally, since it depends on every
robot's data, while each robot solves its own QP against its Voronoi share of the variance, plus a
collision-avoidance barrier.

## The deadlock

<figure>
  <img src="{{ '/images/papers/gp-myopic.jpg' | relative_url }}" alt="Four snapshots of the variance map with the constraint-based controller alone, showing a robot stuck in a low-variance region" loading="lazy">
  <figcaption>Constraint-based control alone. Yellow is high variance, green is low. Between 640 s and 1000 s one robot is stuck in an already-well-sampled region while yellow area remains elsewhere.</figcaption>
</figure>

The objective comes off its required decay rate early and the mean squared error never converges. The
controller is doing what a gradient method does: it cannot see a reason to cross a well-sampled
region to reach an unsampled one.

## The fix: two layers

A **high-level planner** works on a coarse partition of the field. Each cell gets a representative
variance and point, and a Markov decision process rewards cells that are both uncertain and close —
`σ²/distance`. Dynamic programming over the Bellman equation gives each robot an ordered list of
cells to visit. That is the long view the QP lacks.

The **low-level controller** is the QP from before, now driven toward the next waypoint as its
nominal input while still enforcing the decay-rate and safety constraints.

Neither layer is sufficient alone, and the paper is explicit about why. Planning alone samples only
at representative points, which are sparse because the DP is expensive — and it certifies nothing
about mission efficiency. The QP alone deadlocks.

<figure>
  <img src="{{ '/images/papers/gp-hierarchical.jpg' | relative_url }}" alt="Four snapshots of the hierarchical controller, showing planned paths in blue reaching the high-variance regions" loading="lazy">
  <figcaption>The hierarchical controller. Blue lines are DP-generated paths, blue dots the cells to visit. The robots reach the yellow regions instead of stalling, and the field ends almost uniformly green.</figcaption>
</figure>

<figure>
  <img src="{{ '/images/papers/gp-estimate.jpg' | relative_url }}" alt="Evolution of the estimated mean function against the ground truth over 640 seconds" loading="lazy">
  <figcaption>Ground truth at left, then the estimate at 120 s, 320 s and 640 s. By 640 s it is close.</figcaption>
</figure>

Three robots over a 120 m × 120 m field, sampling every 10 s, 900 evaluation points. Both controllers
track the required decay rate at first and both eventually violate it — the variance can never reach
zero given sensor noise. The difference is where they settle: the hierarchical controller's mean
squared error converges to nearly zero, while the constraint-based controller's does not, because of
the deadlock.

Supported by JSPS KAKENHI grant 24K00906.
