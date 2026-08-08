---
title: "Automatic Diabetic Retinopathy Classification with EfficientNet"
collection: publications
category: conferences
permalink: /publication/2020-paper-lazuardi-et-al
date: 2020-11-16
sortdate: 2020-11-16
venue: "IEEE Region 10 Conference (TENCON), 2020"
venueshort: "TENCON"
authors: "Rachmadio Noval Lazuardi, Nyoman Abiwinanda, Tafwida Hesaputra Suryawan, <span class=\"me\">Muhammad Hanif</span>, Astri Handayani"
note: "pp. 756–760."
teaser: "/images/portf_dr_1.jpg"
thumb: "/images/thumbs/portf_dr_1.jpg"
paperurl: "https://ieeexplore.ieee.org/document/9293941"
bibtex: |
  @inproceedings{lazuardi2020automatic,
    title     = {Automatic diabetic retinopathy classification with EfficientNet},
    author    = {Lazuardi, Rachmadio Noval and Abiwinanda, Nyoman and Suryawan, Tafwida Hesaputra and Hanif, Muhammad and Handayani, Astri},
    booktitle = {2020 IEEE Region 10 Conference (TENCON)},
    pages     = {756--760},
    year      = {2020},
    publisher = {IEEE}
  }
---

Diabetic retinopathy is a leading cause of blindness in adults, and screening for it means an
ophthalmologist reading fundus photographs one at a time — slow, and poorly reproducible between
readers. Automating the grading is attractive for exactly that reason.

The hard version of the task is the five-class one: no DR, mild, moderate, severe, proliferative.
Most published work at the time either collapsed it to two or three classes or topped out around
75% accuracy on five.

## Approach

**EfficientNet** as the backbone, B4 and B5, pretrained on ImageNet and fine-tuned. The choice is
about parameter efficiency — compound scaling gets high accuracy without the parameter count of the
architectures earlier work had reached for.

**Preprocessing** matters more than it looks. The Kaggle dataset is a real screening archive, with
wildly varying image quality. Contrast-limited adaptive histogram equalisation was tested on each
colour channel separately:

| CLAHE channel | Train | Validation |
|---|---|---|
| R | 67.98% | 63.60% |
| G | 68.40% | 64.65% |
| B | 67.64% | 64.70% |
| R+G+B | 67.94% | 63.90% |
| **G + centre crop** | **71.50%** | **67.60%** |

Equalising only the green channel beats equalising all three — green carries most of the retinal
vasculature contrast, and the other two mostly add noise. Cropping to the retina itself adds
another few points.

**Progressive resizing**: train at 256 × 256 first, then continue at 512 × 512, 100 epochs total,
with focal loss to cope with a dataset where 25,810 of ~35,000 images are class 0.

## Results

| Model | QWK | Weighted F1 | Accuracy |
|---|---|---|---|
| Progressive EfficientNet-B4 | 0.7922 | 0.8269 | 83.87% |
| Progressive EfficientNet-B5 | 0.7931 | 0.8265 | 83.89% |

Accuracy alone would be misleading on a dataset this imbalanced, so quadratic weighted kappa is the
headline metric — it also has the right shape for the problem, since grading errors between adjacent
severities matter less than errors across the whole scale.

<figure>
  <img src="{{ '/images/papers/dr-confusion.jpg' | relative_url }}" alt="Confusion matrices for EfficientNet-B4 and EfficientNet-B5 across the five diabetic retinopathy severity classes" loading="lazy">
  <figcaption>Most mispredictions land one class away — which is the failure mode you want from a triage tool.</figcaption>
</figure>

Two results worth keeping:

**Progressive resizing helped, and helped the smaller model more** — +3.47% accuracy on B4 against
+1.07% on B5, compared with training at one image size.

**B5 did not beat B4**, despite 1.58× the parameters, which suggests B5 is simply overparameterised
for this dataset. Bigger was not better here.

At 83.89% on five-class classification, this sits well above the ~75% that Pratt et al. and Lam et al.
reported with larger architectures.
