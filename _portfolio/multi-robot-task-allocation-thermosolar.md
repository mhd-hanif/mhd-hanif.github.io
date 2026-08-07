---
title: "Predictive Multi-Robot Task Allocation for Radiation Monitoring"
collection: portfolio
permalink: /portfolio/multi-robot-task-allocation-thermosolar/
order: 5
summary: "UAV and UGV teams dispatched across a thermosolar plant to map direct normal irradiance, with a receding-horizon allocation that anticipates where measurements will matter next."
teaser: "/images/portf_la_africana_1.gif"
motion: "/images/motion/portf_la_africana_1.webp"
thumb: "/images/thumbs/portf_la_africana_1.jpg"
period: "2021 – 2023"
collaborator: "University of Seville"
tags:
  - "ROS"
  - "Gazebo"
  - "Python"
  - "Task Allocation"
featured: true
redirect_from:
  - /portfolio/4_multi_robot_task_allocation_thermo/
publications:
  - "/publication/2023-journal-martin-et-al"
  - "/publication/2022-paper-martin-et-al"
  - "/publication/2022-thesis-hanif-et-al"
---

A thermosolar plant's output depends on direct normal irradiance, which drifts across the field as
clouds move. Measuring it well means putting sensors in the right place *before* the interesting thing
happens, not after.

Working with the **University of Seville** under Prof. J. M. Maestre, this project implemented a high-level
allocation method for a heterogeneous team of UAVs and UGVs. The allocation runs over a receding horizon and
predicts how the irradiance field will evolve, dispatching robots to the cells where a measurement will most
reduce uncertainty. It was validated in ROS and Gazebo against the La Africana plant layout.

The work was published in *Solar Energy* (2023) and at the European Control Conference 2022.
