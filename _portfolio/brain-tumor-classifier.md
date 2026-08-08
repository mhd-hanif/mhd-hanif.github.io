---
title: "CNN-based Brain Tumor Classifier"
collection: portfolio
permalink: /portfolio/brain-tumor-classifier/
order: 10
summary: "A convolutional neural network that classifies brain tumours from MRI into three types — glioma, meningioma and pituitary tumour."
teaser: "/images/portf_bt_1.png"
thumb: "/images/thumbs/portf_bt_1.jpg"
period: "2018"
tags:
  - "CNN"
  - "Keras"
  - "OpenCV"
  - "Medical Imaging"
redirect_from:
  - /portfolio/8_brain_tumor_classifier/
publications:
  - "/publication/2019-paper-abiwinanda-et-al"
---

Conventional computer-aided diagnosis for brain tumours runs in three stages: find the tumour mass,
segment it, then classify what you segmented. Every stage is a place to go wrong, and the segmentation
step in particular has no universal solution across tumour location, shape and intensity.

This project tested whether the segmentation step is necessary at all.

<figure>
  <img src="{{ '/images/papers/bt-classes.jpg' | relative_url }}" alt="Example T1-weighted contrast-enhanced MRI slices for glioma, meningioma and pituitary tumours" loading="lazy">
  <figcaption>The three most common tumour types, from a public dataset of 3,064 T1-weighted contrast-enhanced MRI images.</figcaption>
</figure>

## Approach

Five CNN architectures, all far simpler than AlexNet or VGG16, trained end to end on raw 64 × 64
images with no region-based preprocessing. Filter counts, pooling kernels and hidden-layer widths
were held fixed so that only **depth** varied — the comparison isolates one variable.

<figure>
  <img src="{{ '/images/papers/bt-architectures.jpg' | relative_url }}" alt="Five CNN architectures of increasing depth" loading="lazy">
  <figcaption>Depth is the only thing that changes between them.</figcaption>
</figure>

## Result

The winner was **architecture 2** — two convolution/ReLU/maxpool blocks and one 64-neuron hidden
layer — at 98.51% training and 84.19% validation accuracy.

It won for the right reason rather than the obvious one: it was the only architecture whose
validation loss fell consistently across epochs. The others showed validation loss climbing while
training accuracy improved, which is overfitting, and a useful reminder that on a few thousand
medical images the headline accuracy figure means very little on its own. Widening the winner to 64
and 128 filters did not help either — capacity was not the binding constraint.

84.19% sits inside the 71.39–94.68% band that conventional region-based pipelines reach on the same
dataset, without needing to find the tumour before classifying it.

Carried out at the Biomedical Research Group, Bandung Institute of Technology, and published at the
World Congress on Medical Physics and Biomedical Engineering 2018.
