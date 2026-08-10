---
# Hidden while the underlying US patent application is still under review and
# not publicly available. Delete this line (or set it to true) to restore it,
# along with the same line in _publications/2024-patent-robot-operation-system.md.
published: false
title: "Multi-Robot Task Allocation for Equipment Inspection"
collection: portfolio
permalink: /portfolio/equipment-inspection-task-allocation/
order: 6
summary: "A Unity and ROS2 simulator for multi-robot task allocation in a factory environment, covering scheduling, path planning and collision avoidance for long-horizon inspection routes."
period: "2023 – 2024"
collaborator: "Yokogawa Electric"
tags:
  - "ROS2"
  - "Unity"
  - "C#"
  - "Path Planning"
publications:
  - "/publication/2024-patent-robot-operation-system"
---

Routine equipment inspection in a plant is a long-horizon scheduling problem as much as a robotics one:
robots have to cover every inspection point within a time window, avoid each other, and respect the layout of
the facility.

In collaboration with **Yokogawa Electric**, I built a Unity and ROS2 simulator for evaluating multi-robot
task allocation strategies in a factory environment. The system integrates facility management data and
scheduling constraints, and pre-computes motion paths against environmental constraints so that assignments
are feasible before robots are committed to them.

The resulting robot operation system is the subject of a US patent application filed in October 2024.
