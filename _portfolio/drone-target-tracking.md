---
title: "Drone Coverage Control for Moving Target Tracking"
collection: portfolio
permalink: /portfolio/drone-target-tracking/
order: 3
summary: "Adapting a drone's altitude and its object-detection model in real time, so detection accuracy and field of view stay matched to how the target is moving."
teaser: "/images/portf_target_tracking_1.gif"
thumb: "/images/thumbs/portf_target_tracking_1.jpg"
period: "2023 – 2024"
collaborator: "Fujitsu"
tags:
  - "ROS"
  - "TensorFlow"
  - "Coverage Control"
  - "Object Detection"
paperurl: "https://paperhost.org/proceedings/controls/SICE24/files/0252.pdf"
featured: true
redirect_from:
  - /portfolio/2_drone_target_tracking/
---

Tracking a moving target from the air forces a trade-off. Fly low and the object detector is accurate
but the field of view is narrow; fly high and the drone sees everything but detects little. This project,
carried out in collaboration with **Fujitsu**, enhances drone coverage control for dynamic target tracking by
adapting *both* the drone's altitude and the detection model online.

The controller treats altitude as a decision variable alongside horizontal position, and switches detection
models to match the resulting ground sample distance. The method was implemented in ROS with TensorFlow-based
detectors and presented at the SICE Annual Conference 2024 in Kochi, Japan.
