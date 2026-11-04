---
id: redshift-camera-motion-blur-needs-the-cameras-own-checkbox
title: Redshift camera motion blur needs the motion-blur box on the Redshift camera itself; a moving camera then blurs a still object
domain: redshift
tags: [camera motion blur, redshift camera, motion blur, static object, deformation blur, deep-read]
applies_to: Redshift 3.x in C4D S22 (2020)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=tsx8Isq6m-s, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Derek Kirk [07:54-08:46]: with the camera swooping over a static sphere the ball is blurred as long as Motion Blur is checked on the Redshift camera; untick it to render without camera blur. Deformation blur (animated displacer, no transform) is a separate switch in the render settings Motion Blur tab [08:46-09:28]; see redshift-deformation-blur-default-off for the cost.

**Use it:** If a camera move looks too sharp, check the camera's own blur setting before the global one.
