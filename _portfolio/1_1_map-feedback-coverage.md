---
title: "Real-time Map Feedback Coverage for 3D Reconstruction using Drone"
excerpt: "Coverage control with real-time mesh feedback using UAVs for 3D reconstruction. <br/><img src='/images/portf_mfc_1.gif' style='width:500px;height:auto;border: 2px solid black;'>"
collection: portfolio
---

## Short Summary

This work introduces a **real-time map feedback coverage control** algorithm designed for drone networks. By integrating feedback from an evolving 3D mesh, the algorithm dynamically adjusts the importance density of the coverage control, ensuring efficient and accurate 3D map reconstruction. Simulations in Unity and ROS2 confirm its superiority over conventional methods, offering enhanced reconstruction quality and adaptability in complex environments.


## Methodology

The algorithm uses **NeuralRecon** to process aerial images into a real-time 3D mesh, which informs the drones' trajectories via a **QP-based controller**, enabling optimal coverage while prioritizing areas with significant mesh changes.


**Publication**: 
**Muhammad Hanif**, Takumi Sumino, Kuniaki Uto, Daisuke Ichihashi, Kelvin Cheng, and Takeshi Hatanaka. (2025). **"Impact of Real-time Map Feedback on Coordinated Image Sampling for 3D Reconstruction."** *European Control Conference 2025*, submitted.



**Video:** Simulation Results:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZhDbBBvplhY?si=bU5Kh3ABTvNUihXW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>