---
title: "Hierarchical Vessel Autonomous Operation in a Port with Safety Certificates: Combined MPC and CBF Approach"
collection: publications
category: conferences
permalink: /publication/2023-paper-otsuki-et-al
date: 2023-07-09
sortdate: 2023-07-09
venue: "IFAC World Congress, 2023"
venueshort: "IFAC WC"
authors: "Satoshi Otsuki, Naoki Hatta, <span class=\"me\">Muhammad Hanif</span>, Takeshi Hatanaka, Kenichi Nakashima"
note: "IFAC-PapersOnLine 56(2), pp. 3138–3145."
teaser: "/images/portf_ship_1.gif"
motion: "/images/motion/portf_ship_1.webp"
thumb: "/images/thumbs/portf_ship_1.jpg"
paperurl: "https://www.sciencedirect.com/science/article/pii/S2405896323018554"
bibtex: |
  @article{otsuki2023hierarchical,
    title   = {Hierarchical Vessel Autonomous Operation in a Port with Safety Certificates: Combined MPC and CBF Approach},
    author  = {Otsuki, Satoshi and Hatta, Naoki and Hanif, Muhammad and Hatanaka, Takeshi and Nakashima, Kenichi},
    journal = {IFAC-PapersOnLine},
    volume  = {56},
    number  = {2},
    pages   = {3138--3145},
    year    = {2023}
  }
---

Bringing a vessel into a port is not one control problem but three, and they want different things.
Out in the approach it is congested and you need smooth, predictive collision avoidance. At the
breakwater the navigable channel narrows and the Port Regulations Act decides who goes first. At the
quay it is docking. A single control scheme does not cover all three.

There is a second tension underneath that. **MPC** is good at long-horizon, rule-compliant plans, but
a vessel is slow, underactuated and has no brake — so if the prediction of another ship is wrong, the
plan is wrong too late to fix. **CBF** reacts instantly to a small boat appearing from a blind spot,
but it is myopic: it commands abrupt speed changes and can settle into deadlock.

## Architecture

The proposal is to stop choosing between them and split them across two layers.

The **control layer** always runs a CBF-based quadratic program on a kinematic vessel model, keeping a
750 m clearance from every other vessel and from the breakwaters and shore. Because it sits below the
planner, it certifies safety *even when the navigation layer's prediction is wrong*. Relative degree is
handled by controlling a biased point ahead of the hull under a unicycle model with input–output
feedback linearisation, rather than reaching for a high-order CBF — which would have needed the other
vessels' acceleration, something you cannot measure.

The **navigation layer** switches with the phase. Phases 1 and 3 use nonlinear MPC — path following by
Line-of-Sight guidance in the approach, fixed waypoints for docking. Phase 2 adds **hybrid MPC** on top,
because "wait for the other ship or go first" is a genuinely discrete decision; it is encoded as binary
variables with a no-trespassing region around the breakwater entrance.

## Results

In a head-on encounter, CBF-only avoids collision but with abrupt speed changes; MPC-only **fails to
avoid** once the other vessel accelerates at 0.004 m/s² and breaks the prediction. The combined scheme
avoids the collision *and* keeps the velocity profile mild — each layer covering the other's failure
mode. It also clears all 22 scenarios of the **Imazu** collision-avoidance benchmark.

For Phase 2, adding a **linear temporal logic** constraint — the vessel may cross into the restricted
zone at most twice over the horizon, since it does not reverse — cuts the mixed-integer solve to about
**0.5 s**, fast enough to run for real.

The full approach-to-moor operation was then simulated in **Tokyo Bay**, with the surrounding traffic
driven by a week of real AIS data.

This work is extended in the Springer book chapter
[Hierarchical Vessel Safe Operation in a Port]({{ '/publication/2024-book-otsuki-et-al' | relative_url }}),
which adds RRT-like spatiotemporal path planning.
