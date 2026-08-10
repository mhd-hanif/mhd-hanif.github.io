---
title: "Safe Autonomous Ship Operation in a Port"
collection: portfolio
permalink: /portfolio/safe-autonomous-ship-control/
order: 4
summary: "Hierarchical control for autonomous vessels manoeuvring inside a port, combining model predictive control with control barrier function safety certificates."
teaser: "/images/portf_ship_1.gif"
motion: "/images/motion/portf_ship_1.webp"
thumb: "/images/thumbs/portf_ship_1.jpg"
period: "2022 – 2024"
collaborator: "Kawasaki Heavy Industries"
tags:
  - "MATLAB"
  - "Simulink"
  - "MPC"
  - "Control Barrier Functions"
featured: true
featured_order: 3
redirect_from:
  - /portfolio/3_safe%20autonomous_ship_control/
publications:
  - "/publication/2024-book-otsuki-et-al"
  - "/publication/2023-paper-otsuki-et-al"
---

Ports are cluttered, constrained and unforgiving: a vessel has to reach its berth while respecting
channel geometry, other traffic and its own sluggish dynamics. This project, with **Kawasaki Heavy
Industries**, designed a hierarchical scheme that separates *where to go* from *how to stay safe*.

An RRT-like spatiotemporal planner proposes a path through the port. Model predictive control tracks it
over a receding horizon. A control barrier function sits underneath both as a safety certificate, filtering
any command that would carry the vessel outside the safe set — so safety does not depend on the planner or
the tracker behaving well.

The work appeared at the IFAC World Congress 2023 and was extended into a Springer book chapter.
