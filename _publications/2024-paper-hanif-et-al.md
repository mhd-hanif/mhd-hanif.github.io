---
title: "Real-time Adaptation of Drone Altitude and Object Detection Model for Moving Target Tracking"
collection: publications
category: conferences
permalink: /publication/2024-paper-hanif-et-al
date: 2024-08-28
sortdate: 2024-08-28
venue: "SICE Annual Conference, 2024"
venueshort: "SICE"
authors: "<span class=\"me\">Muhammad Hanif</span>, Takeshi Hatanaka"
note: "pp. 533–538."
teaser: "/images/portf_target_tracking_1.gif"
motion: "/images/motion/portf_target_tracking_1.webp"
thumb: "/images/thumbs/portf_target_tracking_1.jpg"
paperurl: "https://paperhost.org/proceedings/controls/SICE24/files/0252.pdf"
video: "https://youtube.com/playlist?list=PLhkfvyrPMk0y9SuYD3R4zjezj0KI69-Rn"
bibtex: |
  @inproceedings{hanif2024realtime,
    title     = {Real-time Adaptation of Drone Altitude and Object Detection Model for Moving Target Tracking},
    author    = {Hanif, Muhammad and Hatanaka, Takeshi},
    booktitle = {Proceedings of the SICE Annual Conference},
    pages     = {533--538},
    year      = {2024}
  }
---

Persistent coverage control lets a drone patrol a field and keep watch on a target it finds there.
Earlier work handled this with control barrier functions — one constraint keeping coverage of the
field above a performance level, another keeping a detected target inside the drone's sensing range.
It works, but only because the target is assumed to stand still.

Move the target and the assumption breaks.

<figure>
  <img src="{{ '/images/papers/trk-problem.jpg' | relative_url }}" alt="Illustration of the target tracking problem: drones at fixed altitude covering a ground plane with a moving target" loading="lazy">
  <figcaption>Drones patrol the field under persistent coverage control; when one detects the target, it switches from patrolling to keeping the target in view.</figcaption>
</figure>

## Three things that decide whether tracking survives

**Target speed** is the obvious one — computation and motion delays eventually lose a fast target.
The other two are the interesting part, because they pull against each other:

**Detection model.** Six TensorFlow detectors were tested, from MobileNet V1 (30 ms, 21 mAP) to
Faster R-CNN Inception ResNet V2 (620 ms, 37 mAP). Accuracy and latency trade directly, and the most
accurate model is not the best tracker — its latency loses the target anyway.

**Altitude.** Higher widens the field of view, so the target is less likely to slip out of frame.
Higher also shrinks the target in pixels, which hurts detection. The right altitude therefore depends
on which detector is running, and vice versa.

<figure>
  <img src="{{ '/images/papers/trk-performance.jpg' | relative_url }}" alt="Tracking performance against drone altitude, plotted per detection model, at four target velocities" loading="lazy">
  <figcaption>96 experimental runs — six models × four altitudes × four target speeds. Below 0.1 m/s almost everything works. At 0.2 m/s the lightweight models start failing above 1.2 m, and the heaviest model underperforms at every altitude purely on latency.</figcaption>
</figure>

## Adaptation

Since those 96 measurements map each (altitude, model, target speed) triple to a tracking score,
the choice at runtime becomes a small discrete optimisation over 4 × 6 = 24 options: estimate the
target's velocity, then pick the **lowest** altitude whose configuration still clears a performance
threshold. Lowest, because a lower altitude gives more pixels on target — useful for whatever
recognition or decision comes after tracking.

<figure>
  <img src="{{ '/images/papers/trk-architecture.jpg' | relative_url }}" alt="Controller architecture: a target velocity estimator feeding the adaptation rule, alongside the persistent coverage controller" loading="lazy">
  <figcaption>The adaptation rule sits alongside the persistent coverage controller and activates only once a target is detected.</figcaption>
</figure>

## Experiment

Flown on the Tokyo Tech Robot Zoo Sky testbed against a Scamper O-308 ground robot carrying an
A3-size printed car, accelerating from 0.1 to 0.3 m/s over about two minutes.

<figure>
  <img src="{{ '/images/papers/trk-accuracy.jpg' | relative_url }}" alt="Tracking accuracy over time without and with the adaptation algorithm, alongside target velocity, detection model and altitude" loading="lazy">
  <figcaption>Left, fixed configuration: the drone loses the target at about 65 s, as soon as it reaches 0.2 m/s. Right, with adaptation: at the same moment the drone climbs to 1.2 m and switches to a heavier detector, and accuracy stays near 1.</figcaption>
</figure>

<figure>
  <img src="{{ '/images/papers/trk-experiment-without.jpg' | relative_url }}" alt="Snapshots of the experiment without the adaptation algorithm, drone camera view inset" loading="lazy">
  <figcaption>Without adaptation. The camera inset holds a clean detection through 50 s; by 65 s the target is sliding out of frame, and at 80 s the inset shows bare floor.</figcaption>
</figure>

<figure>
  <img src="{{ '/images/papers/trk-experiment-with.jpg' | relative_url }}" alt="Snapshots of the experiment with the adaptation algorithm, showing the drone camera view and the coverage state" loading="lazy">
  <figcaption>With adaptation. The coloured field is the coverage state; the drone stays with the target as it speeds up.</figcaption>
</figure>

The altitude set is discretised here, and target speed is sampled at four values. Extending both to
continuous ranges is the stated next step.

Carried out with support from **Fujitsu Limited**.
