---
title: "Angle-Aware Coverage Control for Large-Scale Map Reconstruction"
collection: portfolio
permalink: /portfolio/angle-aware-coverage/
order: 2
summary: "Coverage control that treats viewing angle as part of the state, so a drone team collects the images a 3D reconstruction actually needs — extended to large fields, steerable cameras and battery-limited missions."
teaser: "/images/portf_uaacc_1.gif"
motion: "/images/motion/portf_uaacc_1.webp"
thumb: "/images/thumbs/portf_uaacc_1.jpg"
period: "2022 – 2025"
tags:
  - "ROS"
  - "ROS2"
  - "Multi-UAV"
  - "Coverage Control"
  - "Control Barrier Functions"
  - "JAX"
featured: true
video: "https://www.youtube.com/watch?v=vk7a_vR_kTw"
redirect_from:
  - /portfolio/1_2_angle-aware-coverage/
publications:
  - "/publication/2025-thesis-hanif-phd"
  - "/publication/2024-journal-hanif-et-al"
  - "/publication/2024-journal-lu-et-al"
  - "/publication/2024-paper-lu-et-al"
---

A 3D reconstruction is only as good as the images it is built from. A point on a surface seen from
one direction reconstructs badly; seen from several, it reconstructs well. So the question for a
drone team is not *where should we fly* but *which viewpoints do we still need* — and coverage
control is a scalable way to answer it.

**Angle-aware coverage control** makes that literal. Instead of covering a 2D plane, the drones cover
a **five-dimensional virtual field**: three spatial coordinates for the point being observed, plus
the horizontal and vertical angle it is seen from. Every cell of that field carries an importance
index, high while unobserved and decaying as cameras cover it from enough distinct directions. A
QP-based controller constrains the decay rate of the resulting objective, so sampling performance is
certified rather than hoped for.

<figure>
  <img src="{{ '/images/papers/aacc-problem.jpg' | relative_url }}" alt="A drone at position p_i observing points in the target field B from horizontal angle theta_h and vertical angle theta_v" loading="lazy">
  <figcaption>The two extra dimensions — θ<sub>h</sub> and θ<sub>v</sub> — are what separate this from ordinary coverage control.</figcaption>
</figure>

This project is the thread of work extending that idea in three directions.

## Making it work on large fields

The original controller has a scaling flaw. Its objective never evaluates *how far* an unobserved
point is, so distant points get no priority, and the field ends up speckled with small unobserved
patches that the drone crosses the whole map to collect one at a time. Barely visible on a testbed;
dominant on a real site.

The fix was to leave the objective alone and change the **nominal input** of the QP instead. A
classical Voronoi move-to-centroid term pulls each drone toward the weighted centroid of its own
cell, so distance enters through where a drone wants to go, while the angle-aware constraint still
governs what it may do.

<figure>
  <img src="{{ '/images/papers/aacc-comparison.jpg' | relative_url }}" alt="Colour maps of the importance index over time, previous controller against the proposed one" loading="lazy">
  <figcaption>Previous controller left of each pair, this one right. Scattered patches versus an orderly sweep.</figcaption>
</figure>

Single drone on a large field: ~1300 s down to ~900 s. Three drones: 470 s down to 330 s. Validated
in ROS and flown on the Tokyo Tech Robot Zoo Sky testbed with Parrot Bebop 2 drones under OptiTrack
motion capture.

## Making the camera move

In the original formulation the cameras point straight down and never move, so the only way to change
a viewing angle is to fly somewhere else — leaving the cheapest degree of freedom unused.

Putting the camera on a **gimbal** and controlling it gives each drone a four-dimensional state:
two position coordinates plus two gimbal angles. Covering a point becomes two conditions rather than
one — it has to be in frame, *and* seen from a direction it still needs.

<figure>
  <img src="{{ '/images/papers/aacc-gimbal-snapshots.jpg' | relative_url }}" alt="Six snapshots of three drones with view cones over a point cloud shifting from purple to red" loading="lazy">
  <figcaption>Late in the run the drones leave the target area and tilt their cameras back at it — a manoeuvre a fixed downward camera cannot perform. It roughly halves the points never seen from an angle they needed.</figcaption>
</figure>

The cost is computational. With a steerable camera the 5D field no longer collapses onto a 2D one, so
the full problem has to be solved directly. **JAX**, with JIT compilation and GPU acceleration,
brought the per-step time from 1206 ms to 22 ms — the difference between an idea and a controller.

## Making the mission persist

A field worth reconstructing takes longer to cover than a battery lasts, so charging belongs inside
the control problem. Fixing which station each drone returns to wastes the flight time the constraint
was meant to protect; assigning stations **dynamically** through ADMM does not.

<figure>
  <img src="{{ '/images/papers/aacc-admm-sim.jpg' | relative_url }}" alt="Four drones covering a field with charging stations shown as green cylinders, over 400 seconds" loading="lazy">
  <figcaption>Green cylinders are charging stations; their height and colour track the battery of the drone assigned to them. Simulated in ROS 2 with takeoff and landing delays included, so the cost of going down to charge is honest.</figcaption>
</figure>

## Where it goes next

The natural continuation is closing the loop with the reconstruction itself — using the evolving 3D
map as a feedback signal to tell the fleet where it is still unresolved. That became a separate
project: [Multi-Drone Image Sampling with Online Map Feedback]({{ '/portfolio/map-feedback-coverage/' | relative_url }}).

## Applications

Precision agriculture and crop inspection, rapid mapping of disaster zones, construction-site
progress monitoring, and urban infrastructure survey — anywhere the reconstruction has to be good
enough to measure from, not just to look at.

## Video

<iframe src="https://www.youtube.com/embed/vk7a_vR_kTw" title="Angle-aware coverage control — simulation verification" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe src="https://www.youtube.com/embed/iLEHCmNdHUs" title="Angle-aware coverage control — testbed experiment" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
