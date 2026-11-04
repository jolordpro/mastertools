---
id: clutter-peripheral
title: Clutter, peripheral vision, crowding and gist
type: science
aliases: [visual clutter, busy image, glanceability, at a glance, readability at a glance, crowding, peripheral vision, gist, thumbnail test, squint test, Feature Congestion, Rosenholtz]
tags: [rosenholtz, mit, evidence-strong, measurable, broadcast]
related: [attention-saliency, negative-space, fluency-complexity, hierarchy-focal-point, broadcast-standards, metric-recipes]
evidence: strong. Peripheral vision keeps summary statistics; clutter measures predict search difficulty.
updated: 2026-10-20
---

# Clutter, peripheral vision and gist

## Quick answer
- Outside the center of gaze, vision keeps only local summaries, so detail blurs into texture. `[E-strong]`
- A display is cluttered when a new item could no longer pop out. `[E-strong]`
- Test every graphic at thumbnail size or blurred. If the message survives, it is glanceable. `[Practice]`

## Definition
- **Peripheral vision**: everything outside the roughly 2° of sharp central vision.
- **Crowding**: nearby items in the periphery merge.
- **Clutter**: excess or disorganized items that hurt search and reading.
- **Gist**: the scene's meaning grasped in one glance.

## Evidence
- Balas, Nakano & Rosenholtz 2009: summary statistics explain crowding. `[E-strong]`
- Rosenholtz et al. 2012: the same model predicts visual search difficulty, using about 1,000 local statistics per patch. `[E-strong]`
- Rosenholtz, Li & Nakano 2007: Feature Congestion beat Subband Entropy at matching human clutter rankings; color variability matters. `[E-strong]`
- Rosenholtz 2016 (*Annual Review of Vision Science*): review of peripheral capabilities and limits.
- Rosenholtz 2025 (*Behavioral and Brain Sciences*): many supposed attention limits reflect peripheral representation. `[E-mixed, under debate]`
- Cutting & Armstrong 2016: clutter in film frames impairs emotion recognition. `[E-strong]`

## Techniques
- `[Practice]` Squint test or thumbnail at about 10% size: does the value structure and focal point survive?
- `[Practice]` Reduce the number of distinct colors, sizes and orientations near the focal point.
- `[Practice]` Push secondary detail to lower contrast so it becomes texture.
- `[Practice]` Give the focal element its own empty zone.

## By medium
- Photography: simplify backgrounds by aperture, angle and timing.
- Design: fewer type sizes; consistent alignment reduces orientation variability.
- Film: emotional close-ups favor clean backgrounds.
- Broadcast: a lower third or score bug is read in peripheral vision while eyes stay on play. It must be low clutter and high contrast. `[Infer]`
- Social thumbnails: judged at tiny size in a scrolling feed. Gist must survive.

## How to measure
- Feature Congestion (MIT-licensed Python port exists; see `tools-models`).
- Subband Entropy as a second opinion.
- Edge density; number of segmented regions.
- Thumbnail test: downscale to 10%, blur, then rerun saliency; check the focal peak still wins.

## Failure modes
- Every element at the same contrast.
- Detailed texture right behind small text.
- Many small elements spread evenly with no dominant mass.

## Critique questions
- Does the message survive one glance at thumbnail size?
- Could a new element pop out here, or would it drown?
- Is the clutter around the focal point or away from it?

## Terms
- clutter, Feature Congestion, Subband Entropy, crowding, summary statistics, gist, glanceability, squint test, thumbnail test

## Sources
- Balas et al. 2009; Rosenholtz et al. 2007, 2012; Rosenholtz 2016, 2025; Cutting & Armstrong 2016.
