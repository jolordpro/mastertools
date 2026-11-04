---
id: c4d-clone-density-scale-hide-reset
title: Guaranteed minimum clone spacing: scale clones by a field, hide neighbours with Push Apart, then reset the scale
domain: c4d
tags: [matrix object, push apart, hide, clone density, scatter, field, reefector]
applies_to: Cinema 4D 2025
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=wsF5c_UnE40, src:yt-transcripts]
feeds: [scene builder, coach]
conflicts: none
---
Scatter 5,000-10,000 matrix points on a plane [21:02]. Plane effector scales points by a spline-radius field (x5); Push Apart in Hide mode then removes any point within its radius, and that radius is multiplied by each clone scale, so points near the spline hide neighbours 5x further [22:36]. A Reefector resets scale [23:36]. Order is scale, hide, reset. Cloner then clones onto the matrix, leaving a few hundred trees instead of thousands [19:29]. Edit the field or its curve to reshape density [24:07].

**Use it:** Use as a recipe for scatter scenes: it lowers instance count and gives a known minimum distance.
