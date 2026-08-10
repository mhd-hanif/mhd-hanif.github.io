---
title: "Human Workload Evaluation of Drone Swarm Formation Control using Virtual Reality Interface"
collection: publications
category: conferences
permalink: /publication/2023-paper-asavasirikulkij-et-al
date: 2023-03-13
sortdate: 2023-03-13
venue: "ACM/IEEE International Conference on Human-Robot Interaction (HRI), 2023"
venueshort: "HRI"
authors: "Chanun Asavasirikulkij, <span class=\"me\">Muhammad Hanif</span>"
note: "Companion proceedings, pp. 132–136."
teaser: "/images/vr_drone.gif"
motion: "/images/motion/portf_vr_1.webp"
thumb: "/images/thumbs/portf_vr_1.jpg"
paperurl: "https://dl.acm.org/doi/10.1145/3568294.3580057"
bibtex: |
  @inproceedings{asavasirikulkij2023human,
    title     = {Human Workload Evaluation of Drone Swarm Formation Control using Virtual Reality Interface},
    author    = {Asavasirikulkij, Chanun and Hanif, Muhammad},
    booktitle = {Companion of the 2023 ACM/IEEE International Conference on Human-Robot Interaction},
    pages     = {132--136},
    year      = {2023},
    doi       = {10.1145/3568294.3580057}
  }
---

A VR headset is the obvious way to fly a drone swarm. Drones move in three dimensions and a tablet
does not, so a head-mounted display that shows depth and scale ought to be the better interface —
and a hand-tracked VR controller ought to beat a joystick at expressing a 3D velocity command.

This paper measured that assumption instead of asserting it, and it did not hold.

<figure>
  <img src="{{ '/images/papers/vr-experiment.jpg' | relative_url }}" alt="Real drones in a motion-capture room alongside an operator wearing a VR headset, using a joystick and a VR controller" loading="lazy">
  <figcaption>Real drones, real operators. The same task was performed with a joystick and with a VR controller, both while wearing the headset.</figcaption>
</figure>

## The system

Three drones in a motion-capture room. Only two are reachable by the operator; the third has no
direct input at all and has to keep station from its neighbours alone — which is the realistic case,
since in the field an operator may never have had a link to every drone, or may lose one mid-flight.

Formation is held by **PI-consensus** control on position and P-consensus on orientation, with a
control barrier function enforcing collision avoidance and workspace limits. Common orientation
matters more than it sounds: without it, "forward" means something different to every drone and the
operator cannot give a velocity command at all.

<figure>
  <img src="{{ '/images/papers/vr-system.jpg' | relative_url }}" alt="System diagram linking motion capture, the ROS central controller, Unity, SteamVR and the Oculus Rift S headset" loading="lazy">
  <figcaption>Motion capture feeds a ROS central controller; ROSBridge and ROS# carry state into Unity, and SteamVR drives an Oculus Rift S and reads whichever input device is in use.</figcaption>
</figure>

## What was measured

Operators steered the swarm toward a goal pose regenerated every 20 seconds, seeing only the average
position of the reachable drones. Five participants, none of whom had used the system before, ran
both interfaces and filled in a NASA-TLX questionnaire after each.

| | VR controller | Joystick |
|---|---|---|
| **Overall workload** | 62.67 ± 30.29 | **29.67 ± 12.00** |
| Mental demand | 279.00 | 140.00 |
| Frustration | 192.00 | 24.00 |
| Physical demand | 62.00 | 6.00 |

The VR controller produced visibly **smoother** input — a joystick operator tends to slam the stick
to ±1, and altitude was on a button, so it could only ever be full up or full down. Smoother, and
roughly twice the workload.

## Why

Two concrete reasons, both mechanical rather than perceptual:

**Stopping is hard.** Releasing a joystick stops the swarm. A VR controller has to be carried back to
its reference pose and *held* there, so standing still is an active task.

**The axes are coupled.** An arm pivots at the shoulder, so moving along one axis drags the others
with it. Isolating a single axis fights the geometry of the human body.

The proposed fixes follow from those causes: draw the reference point in the headset so it can be
found again, add a dead zone around it, and show a guidance line for efficient arm movement.

With **n = 5** and no experienced operators this is a preliminary observation, not a verdict on VR
interfaces — but it is a useful reminder that an interface can be more intuitive and more expensive
to use at the same time.
