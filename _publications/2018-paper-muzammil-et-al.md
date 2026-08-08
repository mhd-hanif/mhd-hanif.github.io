---
title: "Design and Development of Tube-Launched Unmanned Aerial Vehicle"
collection: publications
category: conferences
permalink: /publication/2018-paper-muzammil-et-al
date: 2018-08-01
sortdate: 2018-08-01
venue: "International Conference on Intelligent Unmanned Systems (ICIUS), 2018"
venueshort: "ICIUS"
authors: "Ahmad Fadlillah Muzammil, Nurhayyan Halim Rosid, <span class=\"me\">Muhammad Hanif</span>, Naufalino Fadel, Nathan, Tobias S., Tegar S., M. Agoes Moelyadi, Agus Budiyono"
teaser: "/images/portf_folding_wing_2.png"
thumb: "/images/thumbs/portf_folding_wing_2.jpg"
paperurl: "https://www.researchgate.net/profile/Nurhayyan_Rosid/publication/327573471_Design_and_Development_of_Tube-Launched_Unmanned_Aerial_Vehicle/links/5b978d3d92851c78c41c78f2/Design-and-Development-of-Tube-Launched-Unmanned-Aerial-Vehicle.pdf"
bibtex: |
  @inproceedings{muzammil2018design,
    title     = {Design and Development of Tube-Launched Unmanned Aerial Vehicle},
    author    = {Muzammil, Ahmad Fadlillah and Rosid, Nurhayyan Halim and Hanif, Muhammad and Fadel, Naufalino and Moelyadi, M. Agoes and Budiyono, Agus},
    booktitle = {International Conference on Intelligent Unmanned Systems (ICIUS)},
    year      = {2018}
  }
---

Most fixed-wing UAVs are awkward before they are useful. They take up space in transport, they need
a runway or a dedicated launcher that has to be set up and taken down on site, and assembling one
costs time you may not have.

The premise here: make the aircraft fit in a **5-inch tube** and fly straight out of it.

<figure>
  <img src="{{ '/images/papers/tlu-folding.jpg' | relative_url }}" alt="The UAV in folded, transition and expanded configurations, with principal dimensions marked" loading="lazy">
  <figcaption>Folded, mid-transition, expanded. A tandem wing is what makes this work — it buys lifting surface without a single long span, so the whole aircraft collapses into a cylinder.</figcaption>
</figure>

Launched from a pneumatic tube, the wings deploy under torsional springs and the aircraft transitions
to autonomous flight at roughly **25 m/s**.

## Design

| | |
|---|---|
| Configuration | Tandem wing, folding |
| MTOW | 4 kg |
| Wingspan | 1.508 m (wing), 1.318 m (canard) |
| Cruise speed | 25 m/s |
| Operating altitude | 60–200 m |
| Endurance | up to 30 min |
| Airfoil | NACA 8408 (wing and canard), NACA 0010 (vertical stabiliser) |

The airframe combines CFRP wings, GFRP fuselage and tail, aluminium spars and folding mechanism, and
high-density foam to hold the shape. Airframe alone is half the weight budget; avionics take another
quarter.

<figure>
  <img src="{{ '/images/papers/tlu-layout.jpg' | relative_url }}" alt="Cutaway of the UAV internal layout showing payload, battery, system box, speed controller, folding mechanism and motor" loading="lazy">
  <figcaption>Internal layout. Everything has to stack along the tube axis, which is the real constraint on where anything goes.</figcaption>
</figure>

## Analysis

Stability was estimated in **XFLR5**, and the root-locus analysis shows the aircraft stable in both
longitudinal and lateral modes — two dutch roll modes, roll damping and spiral laterally; phugoid and
short-period longitudinally. Aerodynamic characteristics came from **ANSYS CFX**, solving RANS to get
the lift curve and drag polar.

Avionics are built on a **Pixhawk** flight controller with a 4S 6200 mAh LiPo, brushless DC
propulsion, and two separate radio frequencies for flight data and pilot command. Power distribution
between autopilot and actuators is deliberately split to keep back-EMF off the flight controller.

## Flight testing

<figure>
  <img src="{{ '/images/papers/tlu-flight.jpg' | relative_url }}" alt="The tandem-wing UAV in flight over a field during flight testing" loading="lazy">
  <figcaption>In the air. Every design requirement was met and flight was stable.</figcaption>
</figure>

Measured from the flight controller's data logs:

- maximum airspeed **100 km/h**
- climb rate up to **150 m/min**
- stall speed roughly **45 km/h** at 3 kg take-off weight
- maximum relative altitude about **160 m**
- longest autonomous flight **26 minutes**, from 16.7 V down to 14.8 V

Autonomous mode initially flew badly — guidance was unstable. The logs showed why: the aircraft is
agile enough that target bearing and actual nav bearing diverged sharply, which the stock navigation
parameters were never tuned for. Retuning them fixed it. The unconventional configuration was the
cause, and the flight data was what made it visible.

Built with the **Aksantara UAV** research group and funded by ITB.
