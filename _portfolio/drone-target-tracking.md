---
title: "Drone Coverage Control for Moving Target Tracking"
collection: portfolio
permalink: /portfolio/drone-target-tracking/
order: 3
summary: "Adapting a drone's altitude and its object-detection model in real time, so detection accuracy and field of view stay matched to how the target is moving."
teaser: "/images/portf_target_tracking_1.gif"
motion: "/images/motion/portf_target_tracking_1.webp"
thumb: "/images/thumbs/portf_target_tracking_1.jpg"
period: "2023 – 2024"
collaborator: "Fujitsu"
tags:
  - "ROS"
  - "TensorFlow"
  - "Coverage Control"
  - "Object Detection"
featured: true
redirect_from:
  - /portfolio/2_drone_target_tracking/
publications:
  - "/publication/2024-paper-hanif-et-al"
  - "/publication/2022-thesis-hanif-et-al"
---

Persistent coverage control can send a drone to patrol a field and hold watch on whatever it finds
there. Earlier work in the group did exactly that, with control barrier functions keeping coverage
above a performance level and keeping a detected target inside sensing range. It works — as long as
the target stays still.

This project, in collaboration with **Fujitsu**, is about what breaks when it moves.

<figure>
  <img src="{{ '/images/papers/trk-problem.jpg' | relative_url }}" alt="Drones at fixed altitude covering a ground plane containing a moving target" loading="lazy">
  <figcaption>Drones patrol under persistent coverage control and switch to tracking once a target is detected.</figcaption>
</figure>

## The trade-off

Fly low and the detector is accurate but the field of view is narrow, so a moving target slips out of
frame. Fly high and the drone sees everything but the target is too few pixels to detect reliably.
The right altitude therefore depends on which detection model is running — and the models trade
accuracy against latency, from MobileNet V1 at 30 ms to Faster R-CNN Inception ResNet V2 at 620 ms.

The most accurate model is not the best tracker. Its latency loses the target regardless of altitude.

<figure>
  <img src="{{ '/images/papers/trk-performance.jpg' | relative_url }}" alt="Tracking performance against altitude for six detection models at four target velocities" loading="lazy">
  <figcaption>96 runs across six models, four altitudes and four target speeds — enough to map the whole trade-off rather than argue about it.</figcaption>
</figure>

## Adaptation

Those measurements turn the runtime decision into a small discrete optimisation over 24 configurations:
estimate the target's velocity, then choose the **lowest** altitude whose model still clears a
performance threshold. Lowest, because more pixels on target helps whatever recognition comes next.

Implemented in ROS with TensorFlow detectors and flown on the Tokyo Tech Robot Zoo Sky testbed against
a ground robot accelerating from 0.1 to 0.3 m/s. Without adaptation the drone loses the target the
moment it reaches 0.2 m/s; with adaptation it climbs, switches to a heavier detector, and holds
tracking accuracy near 1.

<figure>
  <img src="{{ '/images/papers/trk-experiment-with.jpg' | relative_url }}" alt="Snapshots of the tracking experiment with adaptation enabled, drone camera view inset" loading="lazy">
  <figcaption>The run with adaptation enabled, drone camera inset over the coverage state.</figcaption>
</figure>

Presented at the SICE Annual Conference 2024 in Kochi, Japan.
