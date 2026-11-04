---
id: c4d-phong-square-area-weighted
title: If Phong shading breaks after a parametric Bevel, switch the Phong algorithm to Square Area Weighted
domain: c4d
tags: [phong, bevel, shading artifact, square area weighted, normals]
applies_to: Cinema 4D 2025
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=wsF5c_UnE40, src:yt-transcripts]
feeds: [shakedown, lookdev-bevel]
conflicts: none
---
Bevelling every edge of a text object wrecked the Phong shading with the default Uniform style; Square Area Weighted fixed it with no edge breaks [27:14]. His rule: if Phong looks wrong, try that first.

**Use it:** Suggest it as the first fix when a bevelled mesh shows smeared or over-rounded shading.
