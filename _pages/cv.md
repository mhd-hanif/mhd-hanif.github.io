---
layout: page
title: "Curriculum Vitae"
permalink: /cv/
description: "Curriculum vitae of Muhammad Hanif — robotics control engineer, Ph.D. in Systems and Control Engineering."
redirect_from:
  - /resume/
---

<p class="contact-actions" style="margin-top:0">
  <a class="btn btn-solid" href="{{ '/files/CV_Hanif.pdf' | relative_url }}" target="_blank" rel="noopener">Download full CV (PDF)</a>
</p>

## Education

**Ph.D. in Systems and Control Engineering** — Institute of Science Tokyo, Japan
*Oct 2022 – Sept 2025* · Advisor: Prof. Takeshi Hatanaka
Dissertation: *Multi-Drone Coordinated Image Sampling for 3D Map Reconstruction through Efficient and
Scene-Adaptive Coverage Control*

**M.Eng. in Systems and Control Engineering** — Tokyo Institute of Technology, Japan
*Oct 2020 – Sept 2022* · Advisor: Prof. Takeshi Hatanaka
Thesis: *Real-Time Optimization for Dynamic Multi-Target Allocation & Tracking with Heterogeneous
Robot Systems*

**B.Sc. in Electrical Engineering** — Bandung Institute of Technology, Indonesia
*Aug 2014 – Jul 2018* · GPA 3.75/4.00 · Advisors: Prof. Bambang Riyanto and Dr. Egi Hidayat
Thesis: *Design and Implementation of Control System in Hybrid Underwater Glider Vehicle in ROS
Environment*

## Research & Industry Experience

**Robotics Control Engineer** — DeepX, Inc., Tokyo, Japan · *Nov 2025 – Present*
Designing coordinated planning algorithms for autonomous excavation with multiple autonomous shovels,
for safe and efficient multi-agent operation in soil excavation tasks.

**Research Assistant, Hatanaka Laboratory** — Institute of Science Tokyo / Tokyo Institute of
Technology · *May 2021 – Sept 2025*

- **Coordinated multi-drone image sampling and coverage control for 3D reconstruction.** Coverage
  control and image sampling algorithms for UAVs, simulated in ROS/ROS2 and Unity and tested in both a
  controlled testbed and an agricultural farm.
- **Multi-robot task allocation for equipment inspection** (with Yokogawa Electric). A Unity and ROS2
  simulator for multi-robot task allocation in a factory environment.
- **Drone coverage control for moving target tracking** (with Fujitsu). Real-time adaptation of drone
  altitude and detection model for dynamic target tracking.
- **Safe autonomous ship control in a port** (with Kawasaki Heavy Industries). Combined MPC and control
  barrier function approach with safety certificates.
- **Predictive multi-robot task allocation for radiation monitoring** (with the University of Seville).
  High-level control of heterogeneous UAV/UGV teams for solar irradiance monitoring in a thermosolar plant.

**Simulation Software Engineer Intern** — FBTriangle, Tokyo, Japan · *Jan 2025 – Mar 2025*
Coverage control for simulating optimal defensive formations in ice hockey.

**Drone Engineer** — IROS Tech, Bandung, Indonesia · *Apr 2019 – May 2020*
Autonomous path planning for UAV mapping and surveillance, including 3D photogrammetry for inspection.

**Research Assistant** — Bandung Institute of Technology · *Aug 2016 – Apr 2019*
Advanced Robotics Research Laboratory (hybrid underwater glider), Biomedical Research Group (diabetic
retinopathy and brain tumour classifiers), CentrUMS (HALE UAV), and the Aksantara drone research team
(folding-wing and hybrid VTOL UAVs).

**Software Developer Intern** — Aero Terra Scan, Bandung, Indonesia · *Jun 2017 – Aug 2017*
Back-end for a UAV ground control system in C#.

## Publications

See the [publications page]({{ '/publications/' | relative_url }}) for the full list, including journal
articles, conference papers, book chapters, theses and patents.

## Awards & Recognition

<ul class="row-list">
{% for aw in site.data.awards %}
  <li class="row-item">
    <span class="row-date">{{ aw.date }}</span>
    <span class="row-body">
      <span class="row-title as-text">{{ aw.name }}</span>
      {% if aw.text %}<span class="row-meta">{{ aw.text }}</span>{% endif %}
    </span>
  </li>
{% endfor %}
</ul>

## Technical Skills

**Languages** — English (C1), Japanese (N3), Arabic (intermediate), Indonesian (native)
**Programming** — C/C++, C#, Python, MATLAB, JavaScript, LaTeX
**Software** — Linux, Windows, ROS/ROS2, PyTorch, TensorFlow, CUDA, OpenCV, Git, Visual Studio, Unity,
Gazebo, Eagle, Altium Designer, Mission Planner, ArduPilot
**Hardware** — Raspberry Pi, Arduino, BeagleBone, UDOO, Pixhawk, ArduPilot, DJI Mavic, Parrot Bebop
**Current focus** — 3D AI for robotics: neural radiance fields, 3D Gaussian splatting and neural
implicit methods for real-time reconstruction in control and perception loops

## Professional Service

<ul class="row-list">
{% for s in site.data.service %}
  <li class="row-item">
    <span class="row-date">{{ s.years }}</span>
    <span class="row-body">
      <span class="row-title as-text">{{ s.role }}</span>
      {% if s.org %}<span class="row-meta">{{ s.org }}</span>{% endif %}
    </span>
  </li>
{% endfor %}
</ul>
