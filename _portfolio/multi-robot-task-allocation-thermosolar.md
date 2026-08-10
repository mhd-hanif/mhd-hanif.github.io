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
featured_order: 4
redirect_from:
  - /portfolio/4_multi_robot_task_allocation_thermo/
publications:
  - "/publication/2023-journal-martin-et-al"
  - "/publication/2022-paper-martin-et-al"
  - "/publication/2022-thesis-hanif-et-al"
---

A parabolic-trough solar plant heats fluid by running it through long loops of collectors, and that
fluid has to stay inside a temperature band — too cold costs performance, too hot causes failures.
The control system manages flow to hold it there. That works while irradiance is uniform. Put a
cloud over part of the field and it is not, and holding each loop at temperature needs a **map of
irradiance across the plant**, plus a forecast of where the shadow is heading.

<figure>
  <img src="{{ '/images/papers/mrta-plant.jpg' | relative_url }}" alt="Aerial view of a parabolic trough collector plant with collectors, manifolds and power block labelled" loading="lazy">
  <figcaption>Collectors in loops, manifolds at ground level, power block. Also a map of obstacles: ground robots cross manifolds only at bridges, and flying over collectors is not allowed.</figcaption>
</figure>

Pyrheliometers cost too much to scatter across a solar field as a fixed grid. A **robotic sensor
network** buys the same map for far less — and it can sample only the shaded areas, where a fixed
grid would spend most of its sensors measuring uniform, unshaded irradiance. One UAV at 20 m/s on a
60 s cycle covers roughly what a grid over 800 × 600 m with a sensor every 200 m would. The map is
worth **6–12% more energy on cloudy days**.

Which makes it a task allocation problem where the tasks are clouds, and clouds move.

## The method

Measurement points are the tasks, UAVs and UGVs are the robots, one robot per task at a time. Because
the tasks move, the allocation has to be time-extended — and the way to do that is to borrow the
shape of model predictive control: predict how the tasks evolve, allocate a sequence over a horizon,
apply only the first step, recompute.

The hard part is that predicting where a robot will be depends on the allocation you have not chosen
yet. The method estimates each task's future position, computes robot-to-task interception points
from known velocities, and averages over which task might have come before.

All of it reduces to a **linear program**, which is what makes it usable at plant scale. Comparable
time-extended methods solve a non-convex problem and do not scale that far.

## Results

Short horizons win. Across 1000 random problems the best cost comes at **K = 3 or 4** — longer
horizons degrade, because the approximations behind the LP lose accuracy the further ahead they
reach.

Against a genetic algorithm baseline, the predictive method solved **38.92% more problems**, and won
in **85.73%** of the cases where both found a solution.

<figure>
  <img src="{{ '/images/papers/mrta-gazebo.jpg' | relative_url }}" alt="A section of the La Africana thermosolar plant modelled in Gazebo" loading="lazy">
  <figcaption>A 100 × 100 m section of the La Africana plant, rebuilt in Gazebo with collision models throughout.</figcaption>
</figure>

<figure>
  <img src="{{ '/images/papers/mrta-snapshots.jpg' | relative_url }}" alt="Snapshots of the Gazebo simulation showing four robots servicing sixteen moving tasks" loading="lazy">
  <figcaption>Four robots, sixteen moving tasks; the colour bar tracks remaining operation time per task.</figcaption>
</figure>

The ROS/Gazebo simulation — Parrot Bebop 2 UAVs at 4 m/s, Jackal UGVs at 2 m/s with laser-based
obstacle avoidance, real battery dynamics — reproduces the Matlab result exactly.

One property is worth naming because it looks like a weakness and is not: performance drops when
tasks move in *different* directions. Cloud motion is wind-driven, so on a real plant they move
together.

## Context

Work with the **University of Seville** under Prof. J. M. Maestre and Prof. E. F. Camacho, funded by
the ERC project **OCONTSOLAR**. Published at ECC 2022 and extended in *Solar Energy* (2023); my
M.Eng. thesis covers the related real-time multi-target allocation and tracking problem.
