---
id: redshift-toon-scalar-user-data-gives-each-object-its-own-noise-scale
title: One toon material can scale its noise per object by reading a scalar user data called scale from each object
domain: redshift
tags: [redshift toon, scalar user data, noise scale, user data interface, one material, helloluxx, deep-read]
applies_to: C4D + Redshift 2 toon material (2024 upload, helloluxx)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=3Z6Td_LTpH0, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
Problem: with the noise source set to object, the ground and car show different noise sizes; separate materials per object are called a bad workflow [06:45-07:16]. Fix: add a user data float 'scale' (slider, step 0.1, default 1) to one object, copy its user data interface and paste onto the others [07:47-08:49]. In the node editor add Scalar User Data named scale and wire it into the noise input scale [08:49-09:19].
Then set per-object values: background 70, floor 5, car left at 1 [09:19-09:50]. Detect Separate Meshes in the contour can fix hard clipped edges on a foreground silhouette but needs this scale fix [06:13-07:16].

**Use it:** supports `redshift-scalar-user-data-drives-metalness` with a toon use; scene check: noise looks different per object, look for object-source noise.
