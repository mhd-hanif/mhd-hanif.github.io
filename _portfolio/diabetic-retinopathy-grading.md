---
title: "Automatic Screening for Diabetic Retinopathy Severity"
collection: portfolio
permalink: /portfolio/diabetic-retinopathy-grading/
order: 9
summary: "Deep learning models for grading diabetic retinopathy severity from retinal fundus images, built on EfficientNet."
teaser: "/images/portf_dr_1.jpg"
thumb: "/images/thumbs/portf_dr_1.jpg"
period: "2018 – 2020"
tags:
  - "TensorFlow"
  - "EfficientNet"
  - "Medical Imaging"
redirect_from:
  - /portfolio/7_dr_grader/
publications:
  - "/publication/2020-paper-lazuardi-et-al"
---

Diabetic retinopathy is a leading cause of preventable blindness, and screening at scale is limited
by the number of clinicians available to read retinal images — a manual read that is also poorly
reproducible between readers. Automatic severity grading offers a way to triage.

The hard version is the five-class problem — no DR, mild, moderate, severe, proliferative. Most
published work at the time either collapsed it to two or three classes, or reached about 75% on five.

## What made the difference

**Preprocessing, more than architecture.** The Kaggle dataset is a real screening archive with wildly
varying image quality. Applying contrast-limited adaptive histogram equalisation to the **green
channel only** beat applying it to all three — green carries most of the retinal vasculature contrast
and the other channels mostly contribute noise. Adding a centre crop to the retina itself pushed
validation accuracy from 64.65% to 67.60% in the preliminary comparison.

**Progressive resizing.** Train at 256 × 256, then continue at 512 × 512. This lifted EfficientNet-B4
by 3.47 percentage points of accuracy against single-size training, and B5 by 1.07 — notably, it
helped the *smaller* model more.

**Focal loss**, because 25,810 of roughly 35,000 images are class 0.

## Results

| Model | QWK | Weighted F1 | Accuracy |
|---|---|---|---|
| Progressive EfficientNet-B4 | 0.7922 | 0.8269 | 83.87% |
| Progressive EfficientNet-B5 | 0.7931 | 0.8265 | 83.89% |

<figure>
  <img src="{{ '/images/papers/dr-confusion.jpg' | relative_url }}" alt="Confusion matrices for EfficientNet-B4 and B5 across five severity classes" loading="lazy">
  <figcaption>Most errors land one class away — the right failure mode for a triage tool. Quadratic weighted kappa is the headline metric for the same reason.</figcaption>
</figure>

B5 did not beat B4 despite 1.58× the parameters, which suggests it is simply overparameterised for
this dataset. At 83.89% on five-class grading, both sit well above the ~75% previously reported with
larger architectures.

Carried out at the Biomedical Research Group, Bandung Institute of Technology, and published at IEEE
TENCON 2020.
