---
title: "VR Interface for Drone Swarm Teleoperation"
collection: portfolio
permalink: /portfolio/vr-swarm-interface/
order: 8
summary: "Flying a drone swarm from inside a VR headset, with formation control holding the shape and a control barrier function keeping it safe — and a measurement of what that interface actually costs the operator."
teaser: "/images/papers/vr-experiment.jpg"
thumb: "/images/papers/vr-experiment.jpg"
period: "2022"
tags:
  - "ROS"
  - "Unity"
  - "Virtual Reality"
  - "Formation Control"
  - "Control Barrier Functions"
  - "Human-Robot Interaction"
publications:
  - "/publication/2023-paper-asavasirikulkij-et-al"
---

One operator, several drones. The appeal of a head-mounted display here is straightforward — drones
move in three dimensions and a tablet screen does not — and a hand-tracked controller should express
a 3D velocity command more naturally than a joystick ever could.

This project built that system on real hardware, then measured whether the appeal survives contact
with an operator.

## The system

Three drones in a motion-capture room. Motion capture feeds a ROS central controller, ROSBridge and
ROS# carry state into Unity, and SteamVR drives an Oculus Rift S while reading whichever input device
the operator is holding.

Crucially, the operator can only reach **two** of the three drones. The third has no direct input and
holds its place from its neighbours alone — the realistic case, since an operator may never have had
a link to every drone in the swarm, or may lose one mid-flight.

<figure>
  <img src="{{ '/images/papers/vr-system.jpg' | relative_url }}" alt="System diagram linking motion capture, the ROS central controller, Unity, SteamVR and the headset" loading="lazy">
  <figcaption>Windows-side Unity and Ubuntu-side ROS do not talk natively, so ROSBridge and ROS# sit between them.</figcaption>
</figure>

## Control

Formation is held by **PI-consensus** on position and P-consensus on orientation, so the swarm moves
as one body under a single velocity command. A **control barrier function** enforces the safety
envelope — no collisions between drones, no leaving the workspace — independently of what the
operator asks for.

Common orientation turns out to be load-bearing. Without it every drone has its own idea of
"forward", and the operator cannot issue a meaningful velocity command at all.

## What it cost the operator

Five participants, none of whom had used the system before, steered the swarm toward goal poses using
a joystick and then a VR controller, both while wearing the headset — the two runs shown at the top
of this page. NASA-TLX questionnaire after each.

The VR controller gave visibly smoother input — a joystick operator tends to slam the stick to its
limits, and altitude sat on a button that could only be full up or full down. It also carried roughly
**twice the workload**: 62.67 ± 30.29 against 29.67 ± 12.00.

Two mechanical reasons, neither of them about perception. Stopping requires actively carrying the
controller back to its reference pose and holding it there, where releasing a joystick is free. And
because an arm pivots at the shoulder, moving along one axis drags the others with it.

Both point at fixes rather than at abandoning the interface: draw the reference point in the headset,
add a dead zone around it, show a guidance line for arm movement.

Done in collaboration with Chanun Asavasirikulkij (Chulalongkorn University) at the Hatanaka
Laboratory, and presented at ACM/IEEE HRI 2023 in Stockholm.
