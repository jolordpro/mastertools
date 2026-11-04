---
id: redshift-matrix-scatter-object-tag-particles
title: Matrix Scatter with a Redshift Object Tag renders optimised spheres, points or custom objects as particles, not geometry, so counts can be high
domain: redshift
tags: [matrix scatter, particles, dust, optimized spheres, object tag, instances]
applies_to: Cinema 4D 2025 + Redshift
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KnfiJy2ND2o, src:yt-transcripts, https://www.youtube.com/watch?v=0GD6OeiB6dk]
feeds: [scene builder]
conflicts: none
---
Set the matrix mode to Object and pick the surface; in the object tag Particles option choose optimised spheres, points or a custom object, and raise the count (2,000 shown) [58:08-59:42]. It does not add geometry to the Render View. Displacement is a better route if the mesh itself should change [59:42].

**Use it:** Prefer for dust or specks over cloner geometry; mind that it is not in the viewport.
Transcript support: Custom objects dropped in separately; matrix pitch -90 to stand grass up; counts 10k to 100k (https://www.youtube.com/watch?v=0GD6OeiB6dk [09:24-10:27])
