---
title: "Angle-Aware Coverage with Camera Rotational Motion Control"
collection: publications
category: manuscripts
permalink: /publication/2024-journal-lu-et-al
date: 2024-06-01
sortdate: 2024-06-01
venue: "SICE Journal of Control, Measurement, and System Integration, 2024"
venueshort: "SICE JCMSI"
motion: "/images/motion/portf_angle_aware_rotation.webp"
authors: "Zhiyuan Lu, <span class=\"me\">Muhammad Hanif</span>, Takumi Shimizu, Takeshi Hatanaka"
teaser: "/images/portf_angle_aware_rotation.webp"
thumb: "/images/thumbs/portf_angle_aware_rotation.jpg"
note: "pp. 211–221. Open access. Preprint arXiv:2404.13915."
paperurl: "https://www.tandfonline.com/doi/epdf/10.1080/18824889.2024.2351637"
bibtex: |
  @article{lu2024anglewarecamera,
    title   = {Angle-Aware Coverage with Camera Rotational Motion Control},
    author  = {Lu, Zhiyuan and Hanif, Muhammad and Shimizu, Takumi and Hatanaka, Takeshi},
    journal = {SICE Journal of Control, Measurement, and System Integration},
    volume  = {17},
    number  = {1},
    pages   = {211--221},
    year    = {2024},
    doi     = {10.1080/18824889.2024.2351637}
  }
---

Angle-aware coverage control asks drones to observe every point of a scene from many directions. But
in the original formulation the cameras point straight down and never move — the only way to change
the viewing angle is to fly somewhere else. That leaves the easiest degree of freedom on the table.

This paper puts the camera on a gimbal and controls it.

<figure>
  <img src="{{ '/images/papers/aacc-gimbal-scene.jpg' | relative_url }}" alt="A simulated orchard scene with three drones, their view cones highlighted, and the image each drone captures" loading="lazy">
  <figcaption>Three drones covering a scene, with what each camera actually sees below. Controlling where the camera looks — not just where the drone is — is what this paper adds.</figcaption>
</figure>

## What changes

Each drone now carries a **four-dimensional state**: two position coordinates plus the gimbal's
horizontal and vertical angles. That needs a new performance function, because covering a point is
now two conditions rather than one — the point has to fall inside the camera's field of view, *and*
the direction the drone sees it from has to match the viewing angle that point still needs. A
QP-based controller with a control-barrier-like function then constrains the decay rate of the
objective, with a second barrier keeping the gimbal pitch inside its mechanical limits.

## The cost of doing this

Adding camera orientation makes the problem far more expensive than translation alone. In the
original work the drone position that observes a point from a given angle was *uniquely* determined,
which let the five-dimensional field collapse onto a two-dimensional one. With a steerable camera
that mapping no longer exists, so the full 5D field has to be handled directly — and the gradient
computation across all four state variables dominates the runtime.

The answer here is engineering rather than approximation: **JAX**, with JIT compilation and GPU
acceleration.

| | Central controller | Drone controller |
|---|---|---|
| NumPy on CPU | 212 ms | 1206 ms |
| JIT, CPU | 31 ms | 102 ms |
| JIT, GPU | **6 ms** | **22 ms** |

Over a second per step is not a controller. At 22 ms it runs at roughly 10 Hz, which is.

## Results

<figure>
  <img src="{{ '/images/papers/aacc-gimbal-snapshots.jpg' | relative_url }}" alt="Six snapshots of the ROS simulation showing three drones and their view cones as the point cloud changes from purple to red" loading="lazy">
  <figcaption>Three drones over 300 s. Points shift from purple (uncovered) to red (well covered). Early on the drones stay over the field with cameras down; later they move outside it and tilt the gimbal to reach angles they could not otherwise get.</figcaption>
</figure>

That late-stage behaviour — leaving the target area and looking back at it obliquely — is exactly
what a fixed downward camera cannot do.

Comparing against the original controller needs care, since the two optimise different objective
functions and neither objective is a fair yardstick. So the paper counts something physical instead:
simulate photography at 5 Hz, and mark a point covered when it falls in frame *and* is seen from
within π/16 of a direction it still needs.

<figure>
  <img src="{{ '/images/papers/aacc-gimbal-result.jpg' | relative_url }}" alt="Number of uncovered points over time, comparing this controller against the previous one" loading="lazy">
  <figcaption>The previous controller finishes its coverage at about 130 s and then stops — with a large number of points still never seen from a direction they needed, because its fixed camera could not reach those angles. Controlling the gimbal roughly halves the remaining uncovered points.</figcaption>
</figure>

The paper is simulation only; hardware experiments and a comparison in terms of reconstructed 3D
accuracy are left as future work.
