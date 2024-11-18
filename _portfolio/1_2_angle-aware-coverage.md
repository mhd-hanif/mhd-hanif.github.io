---
title: "Angle-Aware Coverage Control for Large-Scale Map Reconstruction using Drone Networks"
excerpt: "Coverage control algorithm for multiple UAVs to be used in 3D map reconstruction applications. <br/><img src='/images/portf_uaacc_1.gif' style='width:500px;height:auto;border: 2px solid black;'>"
collection: portfolio
---

## Short Summary

This work presents a novel angle-aware coverage control method that integrates **Voronoi-based coverage** as the nominal input into the quadratic programming problem required to solve the original **angle-aware coverage control**, aimed at improving monitoring efficiency in large-scale 3D map reconstruction using drone networks. The approach ensures diverse viewing angles, enhancing 3D map quality. Both simulations in ROS and real-world experiments in a **testbed** validate the method’s effectiveness, especially in large-scale missions where traditional techniques underperform.

<p align="center">
  <img src='/images/portf_aacc_2.png' alt="Angle-Aware Coverage Problem"/>
</p>

## Application
- **Agriculture**: Precision crop mapping.
- **Disaster Management**: Rapid mapping of disaster zones.
- **Urban Mapping**: Detailed mapping of city infrastructure.

## Key Method
The system uses **Voronoi Coverage** for area partitioning, dynamically adjusting drone flight paths to ensure optimal coverage with minimal overlaps, while employing the angle-aware method to capture images from various viewing angles.

## Conclusion
The approach improves both **monitoring efficiency** and **map quality**, significantly reducing drone travel time to unobserved areas in large-scale applications.

**Publication**: 
**Muhammad Hanif**, Takumi Shimizu, Zhiyuan Lu, Masaya Suenaga, and Takeshi Hatanaka. (2024). **"Efficient Angle-Aware Coverage Control for Large-Scale Map Reconstruction using Drone Networks."** *SICE Journal of Control, Measurement, and System Integration*, 17(1): 144-155. [[Paper]](https://www.tandfonline.com/doi/pdf/10.1080/18824889.2024.2346375)


**Video** - Simulation Verification: 

<iframe width="560" height="315" src="https://www.youtube.com/embed/vk7a_vR_kTw?si=7waq0paF_MLRA2tW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<br>

<iframe width="560" height="315" src="https://www.youtube.com/embed/iLEHCmNdHUs?si=zgUnZLTMyZrZkbEn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
