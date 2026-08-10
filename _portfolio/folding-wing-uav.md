---
title: "Tube-Launched Folding-Wing UAV"
collection: portfolio
permalink: /portfolio/folding-wing-uav/
order: 13
summary: "A compact fixed-wing UAV that stows in a tube and deploys without a runway, with a coordinated relay system to extend communication range. Best Design, Indonesia Aerial Robotics Competition 2017."
teaser: "/images/portf_folding_wing_0.gif"
motion: "/images/motion/portf_folding_wing_0.webp"
thumb: "/images/thumbs/portf_folding_wing_0.jpg"
period: "2015 – 2017"
tags:
  - "Avionics"
  - "Pixhawk"
  - "Fixed-Wing"
  - "Relay Network"
featured: true
featured_order: 5
redirect_from:
  - /portfolio/9_3_folding-wing-uav/
publications:
  - "/publication/2018-paper-muzammil-et-al"
---

Most fixed-wing UAVs are awkward before they are useful. They fill a vehicle in transport. They need
a runway or a dedicated launcher that has to be carried in, set up and taken down. And assembling one
on site costs time you may not have — which in difficult terrain is the whole problem.

Built for the Indonesia National Aerial Robotics Competition 2017, this was one of Indonesia's first
autonomous folding-wing UAVs. It took **Best Design** and **1st Runner-Up**.

<figure>
  <img src="{{ '/images/portf_folding_wing_5.jpg' | relative_url }}" alt="The tube-launched folding-wing UAV" loading="lazy">
</figure>

## The idea

Make the aircraft fit in a tube and fly straight out of it.

A **tandem wing** is what makes that possible — it buys lifting surface without any single long span,
so the whole aircraft collapses into a cylinder roughly 5 inches across. Torsional springs deploy the
wings on exit, and the aircraft transitions to autonomous flight at about 25 m/s.

<figure>
  <img src="{{ '/images/papers/tlu-folding.jpg' | relative_url }}" alt="The UAV in folded, transition and expanded configuration with dimensions marked" loading="lazy">
  <figcaption>Folded, mid-transition, expanded.</figcaption>
</figure>

Multiple aircraft can be launched at once from a pneumatic launcher, with no runway anywhere in the
process. A coordinated relay system extends communication range by using the aircraft themselves as
relays — the limitation that bites hardest in hilly terrain.

<figure>
  <picture>
    <source srcset="{{ '/images/motion/portf_folding_wing_1.webp' | relative_url }}" type="image/webp" media="(prefers-reduced-motion: no-preference)">
    <img src="{{ '/images/thumbs/portf_folding_wing_1.jpg' | relative_url }}" alt="The UAV launching from the pneumatic tube and deploying its wings" loading="lazy">
  </picture>
  <figcaption>Launch and wing deployment.</figcaption>
</figure>

## My part

I built the **avionics system** — a Pixhawk flight controller on a 4S 6200 mAh LiPo, brushless DC
propulsion, and two separate radio links so flight data and pilot command never contend. Power
distribution between the autopilot and the actuators is deliberately split, keeping back-EMF from the
servos off the flight controller.

<figure>
  <img src="{{ '/images/papers/tlu-layout.jpg' | relative_url }}" alt="Cutaway of the internal layout showing payload, battery, system box, speed controller, folding mechanism and motor" loading="lazy">
  <figcaption>Everything stacks along the tube axis, which is the real constraint on where anything can go.</figcaption>
</figure>

## Flight testing

<figure>
  <img src="{{ '/images/papers/tlu-flight.jpg' | relative_url }}" alt="The tandem-wing UAV in flight over a field" loading="lazy">
</figure>

From the flight controller logs: 100 km/h maximum airspeed, 150 m/min climb rate, roughly 45 km/h
stall at 3 kg, about 160 m maximum relative altitude, and a longest autonomous flight of 26 minutes.

Autonomous mode flew badly at first — the guidance was unstable. The logs showed target bearing and
actual nav bearing diverging sharply, because the aircraft is far more agile than the stock navigation
parameters assume. Retuning them fixed it. The unconventional configuration caused the problem and
the flight data is what made it visible.

<figure>
  <img src="{{ '/images/portf_folding_wing_6.jpg' | relative_url }}" alt="The team at the Indonesia National Aerial Robotics Competition" loading="lazy">
  <figcaption>The team, with Aksantara UAV at ITB.</figcaption>
</figure>

## Video

<iframe src="https://www.youtube.com/embed/NfwVMHj_P-g" title="Tube-launched folding-wing UAV" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Related reading

Rosid, N. H., Lukman, E. I., Fadlillah, M. A., & Moelyadi, M. A. (2018). Aerodynamic Characteristics
of Tube-Launched Tandem Wing Unmanned Aerial Vehicle. *Journal of Physics: Conference Series*,
1005(1), 012015. [IOPscience](https://iopscience.iop.org/article/10.1088/1742-6596/1005/1/012015/pdf)
