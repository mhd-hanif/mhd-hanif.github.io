---
title: "Predictive Receding-Horizon Multi-Robot Task Allocation with Moving Tasks"
collection: publications
category: conferences
permalink: /publication/2022-paper-martin-et-al
date: 2022-07-12
sortdate: 2022-07-12
venue: "European Control Conference (ECC), 2022"
venueshort: "ECC"
authors: "Javier G. Martin, <span class=\"me\">Muhammad Hanif</span>, Takeshi Hatanaka, Jose M. Maestre, Eduardo F. Camacho"
note: "pp. 2030–2035."
teaser: "/images/portf_la_africana_1.gif"
motion: "/images/motion/portf_la_africana_1.webp"
thumb: "/images/thumbs/portf_la_africana_1.jpg"
paperurl: "https://ieeexplore.ieee.org/abstract/document/9838127"
bibtex: |
  @inproceedings{martin2022predictive,
    title     = {Predictive receding-horizon multi-robot task allocation with moving tasks},
    author    = {Martin, Javier G. and Hanif, Muhammad and Hatanaka, Takeshi and Maestre, Jose M. and Camacho, Eduardo F.},
    booktitle = {2022 European Control Conference (ECC)},
    pages     = {2030--2035},
    year      = {2022},
    publisher = {IEEE}
  }
---

The first version of the predictive receding-horizon task allocation method, presented on an academic
case study.

The setting is a robotic sensor network measuring irradiance across a thermosolar plant, where the
things being measured — cloud shadows — keep moving. That makes the assignment **time-extended**: you
cannot allocate once, because by the time a robot arrives the task has gone somewhere else. The
answer is to borrow the structure of model predictive control: predict how tasks evolve, allocate a
sequence over a horizon, apply only the first step, then recompute.

What makes it scale is that the problem is transformed into a **linear program**. Other time-extended
MRTA formulations solve a non-convex problem, which puts plant-sized instances out of reach.

## What came next

This paper was extended into the *Solar Energy* journal version,
[Predictive Receding-Horizon Multi-Robot Task Allocation Applied to the Mapping of Direct Normal
Irradiance in a Thermosolar Power Plant]({{ '/publication/2023-journal-martin-et-al' | relative_url }}),
which adds:

- a **hybrid event-based/synchronous** recalculation strategy, replacing the purely event-triggered
  version here — which matters once cloud velocity is uncertain
- a more compact formulation of the **energetic constraints**
- better prediction of robot-to-task distances across horizon steps
- **realistic simulation** in ROS and Gazebo, on a model of the La Africana plant

Compared directly on 1000 random problems, the journal version solves more of them (776 against 744)
and achieves a better mean cost on those both can solve — 1384.2 against 1562.1.
