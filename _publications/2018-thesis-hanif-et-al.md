---
title: "Design and Implementation of Control System in Hybrid Underwater Glider Vehicle in ROS Environment"
collection: publications
category: thesis
permalink: /publication/2018-thesis-hanif-et-al
date: 2018-07-01
sortdate: 2018-07-01
venue: "B.Sc. Thesis, Bandung Institute of Technology, 2018"
venueshort: "B.Sc."
authors: "<span class=\"me\">Muhammad Hanif</span>"
note: "Department of Electrical Engineering. Advisors: Prof. Bambang Riyanto and Dr. Egi Hidayat."
teaser: "/images/thumbs/thesis-itb.jpg"
thumb: "/images/thumbs/thesis-itb.jpg"
paperurl: "https://www.researchgate.net/publication/380214406_DESAIN_IMPLEMENTASI_SISTEM_KONTROL_PADA_WAHANA_HYBRID_UNDERWATER_GLIDER_BERBASIS_ROS"
---

Indonesia is 64.85% ocean by area, and much of that territory goes unsurveyed because sustained
data collection at depth is slow, expensive and risky for people. A vehicle that can both *loiter
efficiently* and *manoeuvre on demand* is the useful shape for that problem — which is what the
**Hybrid Underwater Glider (HUG) "Arnadyaksa"**, developed by the LSKK research group at ITB, is
built to be. It combines the two modes of underwater travel usually treated separately: AUV
thruster propulsion, responsive but power-hungry, and glider buoyancy-driven motion, very efficient
but slow.

This thesis designs and implements the **control system** responsible for the vehicle's movement and
attitude in both modes.

<figure>
  <img src="{{ '/images/papers/haug-vehicle.jpg' | relative_url }}" alt="The yellow torpedo-shaped HUG Arnadyaksa vehicle with tail fins, resting on a stand" loading="lazy">
  <figcaption>HUG Arnadyaksa — a hybrid of an autonomous underwater vehicle and an underwater glider.</figcaption>
</figure>

## Approach

The control system is built from four controllers — **surge, pitch, buoyancy engine, and yaw** — on
a **cascaded PID** structure. Pitch and buoyancy control are sequenced by a **finite state machine**
that takes pitch angle and depth as inputs to produce the sawtooth dive-and-climb profile of glider
mode; yaw and surge take over the movement mechanism in AUV mode.

Everything runs on **ROS** on a single-board computer. The buoyancy engine — a linear actuator
driving a piston and reservoir, paired with a moving mass for pitch trim — later became the subject
of an [Indonesian patent]({{ '/publication/2021-patent-buoyancy-engine' | relative_url }}).

<figure>
  <img src="{{ '/images/papers/haug-internals.jpg' | relative_url }}" alt="The opened vehicle showing labelled internals: processor, moving mass module, linear actuator, piston and reservoir, thruster and servo rudder" loading="lazy">
  <figcaption>Inside the hull: processor, moving mass, and the linear actuator, piston and reservoir that make up the buoyancy engine.</figcaption>
</figure>

## Validation

Testing went in three stages, each closing more of the gap to the real vehicle: **software-in-the-loop**
simulation visualised in RViz, then **hardware-in-the-loop (HILS)** with the real electronics in the
loop, then **pool testing** of the physical vehicle — buoyancy and pitch trimming, glider-mode dives,
and AUV depth holding.

<figure>
  <img src="{{ '/images/papers/haug-pool-test.jpg' | relative_url }}" alt="The vehicle submerged in a glass-walled test pool during trials" loading="lazy">
  <figcaption>Pool trials at ITB. Trimming first, then AUG-mode gliding and AUV depth holding.</figcaption>
</figure>

The control system performed the commanded operations across both modes as designed.

Full project detail: [Hybrid Autonomous Underwater Glider]({{ '/portfolio/hybrid-autonomous-underwater-glider/' | relative_url }}).
