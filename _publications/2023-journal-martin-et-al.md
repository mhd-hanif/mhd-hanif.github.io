---
title: "Predictive Receding-Horizon Multi-Robot Task Allocation Applied to the Mapping of Direct Normal Irradiance in a Thermosolar Power Plant"
collection: publications
category: manuscripts
permalink: /publication/2023-journal-martin-et-al
project: "/portfolio/multi-robot-task-allocation-thermosolar/"
date: 2023-09-01
sortdate: 2023-09-01
venue: "Solar Energy, 2023"
venueshort: "Solar Energy"
authors: "Javier G. Martin, <span class=\"me\">Muhammad Hanif</span>, Takeshi Hatanaka, Jose M. Maestre, Eduardo F. Camacho"
teaser: "/images/portf_la_africana_1.gif"
motion: "/images/motion/portf_la_africana_1.webp"
thumb: "/images/thumbs/portf_la_africana_1.jpg"
paperurl: "https://www.sciencedirect.com/science/article/abs/pii/S0038092X23005443"
featured: true
bibtex: |
  @article{martin2023predictive,
    title   = {Predictive receding-horizon multi-robot task allocation applied to the mapping of direct normal irradiance in a thermosolar power plant},
    author  = {Martin, Javier G. and Hanif, Muhammad and Hatanaka, Takeshi and Maestre, Jose M. and Camacho, Eduardo F.},
    journal = {Solar Energy},
    volume  = {263},
    pages   = {111911},
    year    = {2023}
  }
---

A parabolic-trough solar plant runs heat transfer fluid through long loops of collectors, and the
fluid temperature has to stay inside a band — too cold and performance drops, too hot and you get
maintenance failures. Control acts on the flow. But when a cloud shades part of the field, the
irradiance is no longer uniform, and controlling each loop's flow independently needs a **spatial map
of irradiance across the plant** — plus a prediction of where the shadow goes next.

<figure>
  <img src="{{ '/images/papers/mrta-plant.jpg' | relative_url }}" alt="Aerial view of a parabolic trough collector plant with collectors, manifolds, pass area and power block labelled" loading="lazy">
  <figcaption>A PTC plant. Collectors in loops, manifolds at ground level, and a power block — all of which are obstacles: ground robots must cross manifolds at bridges, and flying over collectors is not permitted.</figcaption>
</figure>

Pyrheliometers are too expensive to scatter across a solar field as a fixed grid. A **robotic sensor
network** gets the same map for far less capital — and unlike a fixed grid it can sample only the
shaded areas, since unshaded irradiance is essentially uniform. The paper's own estimate: one UAV at
20 m/s on a 60 s sampling cycle is roughly equivalent to a grid covering 800 × 600 m with a sensor
every 200 m. Getting that map is worth **6–12% more energy on cloudy days**.

Which turns the problem into task allocation — except the tasks are clouds, and clouds move.

## Approach

The measurement points are the tasks; the UAVs and UGVs are the robots; each robot does one task at a
time and each task needs one robot. Because the tasks move, the allocation has to be **time-extended**:
allocate a sequence over a horizon, apply only the first step, then recompute. Model predictive
control, applied to assignment.

The cost balances distance travelled against task completion time — a per-robot penalty on distance,
weighing battery and wear, against a per-task weight on how long it takes, weighing how much that
cloud matters.

The central difficulty is that predicting where a robot will be depends on the allocation you have
not made yet. An earlier version sidestepped this by assuming robots move toward the tasks' centre of
gravity. This paper instead estimates each task's future position, computes robot-to-task
**interception points** given known velocities, and averages the distances over which task was done
previously.

<figure>
  <img src="{{ '/images/papers/mrta-distances.jpg' | relative_url }}" alt="Diagram of the distance estimates from a robot to each task at successive allocation steps" loading="lazy">
  <figcaption>Distance from robot to task at step <em>k</em>, averaged over which task it might have done at step <em>k−1</em>.</figcaption>
</figure>

The point of all this is that the whole thing collapses into a **linear program**. Comparable
time-extended MRTA methods solve a non-convex problem; an LP scales to plant-sized instances.

Recomputation is **hybrid**: event-triggered whenever a task completes, and synchronous on a timer,
so drift in the cloud-velocity estimate gets corrected without waiting for a completion.

## Results

**Horizon length.** Across 1000 random problems, **K = 3 or 4** is best. Longer is not better — the
LP transformation rests on approximations whose accuracy decays along the horizon, and the underlying
problem is strongly nonlinear.

<figure>
  <img src="{{ '/images/papers/mrta-horizon.jpg' | relative_url }}" alt="Mean cost and computation time against allocation horizon length K" loading="lazy">
  <figcaption>Cost against horizon length. The minimum sits at K = 3–4, and computation time climbs steadily beyond it — so a longer horizon costs more and delivers less.</figcaption>
</figure>

**Against a genetic algorithm.** At K = 4, PMRTA solved 828 of 1000 problems against the GA's 596. Of
the 574 both could solve, PMRTA won 709 times and the GA 118. Overall the paper reports **38.92% more
problems solved** and a win in **85.73%** of cases where both produced an answer.

**Recomputation period.** Shorter is not automatically better, but the hybrid strategy beats
event-triggered alone — including when cloud velocity carries Gaussian noise.

**Task direction.** Performance degrades when tasks move in different directions, which is a
limitation with a convenient property: cloud motion is wind-driven, so real clouds do move together.

## ROS/Gazebo

<figure>
  <img src="{{ '/images/papers/mrta-gazebo.jpg' | relative_url }}" alt="A 100 by 100 metre section of the La Africana thermosolar plant modelled in Gazebo" loading="lazy">
  <figcaption>A 100 × 100 m section of the La Africana plant in Gazebo, with collision models on every obstacle.</figcaption>
</figure>

<figure>
  <img src="{{ '/images/papers/mrta-robots.jpg' | relative_url }}" alt="Gazebo models of the Parrot Bebop 2 quadrotor and the Jackal ground robot" loading="lazy">
  <figcaption>Parrot Bebop 2 at 4 m/s holding 3 m altitude; Jackal at 2 m/s with a laser scanner for local obstacle avoidance.</figcaption>
</figure>

<figure>
  <img src="{{ '/images/papers/mrta-snapshots.jpg' | relative_url }}" alt="Snapshots of the Gazebo simulation with the remaining task operation time shown as a colour bar" loading="lazy">
  <figcaption>Four robots, sixteen moving tasks. The colour bar tracks remaining operation time per task; blue means done.</figcaption>
</figure>

The realistic simulation reproduces the Matlab finding exactly — K = 3 and K = 4 remain optimal — with
obstacle avoidance, battery dynamics and collision models all in play.

## Limitations

The allocation is centralised; distributing it via ADMM is named as future work, as is choosing the
robot count for a given plant size. Everything here is simulation — no real robots yet.

Funded by the ERC project **OCONTSOLAR** (grant 789051) under Horizon 2020.
