---
title: "Real-Time Optimization for Dynamic Multiple Target Allocation and Tracking with Heterogeneous Robotic Systems"
collection: publications
category: thesis
permalink: /publication/2022-thesis-hanif-et-al
date: 2022-08-01
sortdate: 2022-08-01
venue: "M.Eng. Thesis, Tokyo Institute of Technology, 2022"
venueshort: "M.Eng."
authors: "<span class=\"me\">Muhammad Hanif</span>"
note: "Department of Systems and Control Engineering."
teaser: "/images/thumbs/thesis-tokyo-tech.jpg"
thumb: "/images/thumbs/thesis-tokyo-tech.jpg"
paperurl: "https://www.researchgate.net/publication/380214397_Real-Time_Optimization_for_Dynamic_Multiple_Target_Allocation_Tracking_with_Heterogeneous_Robotic_Systems"
---

Sending a team of robots after targets that move is really two problems, and this thesis takes on
both. First, **who should go where** — allocation, when the tasks themselves are in motion. Second,
**how to not lose them** — visual tracking, once a robot arrives. Both are posed as real-time
optimization problems over **heterogeneous** UAV and UGV teams.

## Part one — dynamic target allocation

Motivated by radiation monitoring over the **La Africana** mega-solar plant in Spain, where the
"tasks" are moving cloud shadows. Allocating to a moving task is only correct if it accounts for
where that task will *be*, so the method estimates task and robot position evolution, computes
robot-to-task interception points, and allocates over a **predictive receding horizon** — commit the
first step, then recompute.

The whole thing is relaxed into an equivalent **linear program**, which is what keeps it cheap enough
to run online; energetic feasibility of each robot is folded into the same optimization. Validated in
MATLAB and then in **ROS/Gazebo** on a model of the real plant, with 4 robots servicing 16 tasks.

Carried out with the **University of Seville** (Prof. J. M. Maestre and J. G. Martin), and published
at [ECC 2022]({{ '/publication/2022-paper-martin-et-al' | relative_url }}) and in
[*Solar Energy* (2023)]({{ '/publication/2023-journal-martin-et-al' | relative_url }}). More on the
[project page]({{ '/portfolio/multi-robot-task-allocation-thermosolar/' | relative_url }}).

## Part two — dynamic target tracking

Prior work in the group used control barrier functions to hold a detected target in a drone's field
of view — which works while the target stays still. This part, motivated by collaboration with
**Fujitsu**, asks what breaks when it moves, and finds the answer is a three-way coupling between
**altitude, detection model, and target speed**.

Fly low and the detector is accurate but the field of view is too narrow to keep up; fly high and the
target is too few pixels to detect. And the *most* accurate model is not the best tracker — at ~600 ms
of latency the delay loses the target at any altitude.

Mapping that trade-off took **96 experiments** — six TensorFlow detection models (30 ms to 620 ms),
four altitudes (0.8–2.0 m), four target speeds (0–0.3 m/s) — flown on the Tokyo Tech Sky testbed with a
Parrot Bebop 2 tracking a ground robot under OptiTrack. Those measurements turn the runtime choice into
a small discrete optimization: estimate target velocity, then pick the altitude and detector that clear
a performance threshold.

This line of work continued into
[SICE 2024]({{ '/publication/2024-paper-hanif-et-al' | relative_url }}) — see the
[project page]({{ '/portfolio/drone-target-tracking/' | relative_url }}).
