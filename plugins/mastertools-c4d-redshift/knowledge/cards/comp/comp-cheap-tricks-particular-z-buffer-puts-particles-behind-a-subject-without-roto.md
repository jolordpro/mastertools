---
id: comp-cheap-tricks-particular-z-buffer-puts-particles-behind-a-subject-without-roto
title: Trapcode Particular reads a depth pass in its Z buffer, so particles pass behind a moving subject with no rotoscoping
domain: comp
tags: [particular, z buffer, depth, particles, fireflies, bokeh, 3d camera tracker, deep-read]
applies_to: After Effects, Trapcode Particular
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=-32g9bYyZuc, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Fireflies set-up [42:22-49:52]: track the footage, create a solid with Particular, use Apply Form Defaults and set a grid of 20 by 20 by 5, then size about 3 to 4 px, a little colour and size random, disperse and twist for scatter and a turbulence field on position with evolution speed 10 on a slow-motion clip, fade-in 0. Under Visibility set the Z buffer layer to the depth pass; the Z at black and Z at white values choke how far back the particles are hidden, so some vanish half behind her cloak [43:59-45:05]. Duplicate the system as a foreground layer with the Z buffer off, move it toward camera in Z, make it sparser (5 by 5) and blur it with Universe Bokeh [47:12-48:50]. Optical Glow on both, Supercomp to merge them, and Magic Bullet Looks on top.
Transfers: the same Z-buffer idea applies to any element-vs-subject occlusion when a depth pass exists.

**Use it:** Use for particle ambience on a plate or on a render with a depth AOV.
