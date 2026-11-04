---
id: pipeline-expanse-usd-assemble-script-builds-animation-look-and-utilities-layers-in-order
title: Expanse's USD assemble script after animation caching: animation layer, look layer, then a utilities layer that fixes whiskers and adds velocities
domain: pipeline
tags: [pipeline, expanse, usd, layers, maya, houdini, solaris, prism, velocity, deep-read]
applies_to: Maya to Houdini Solaris, Prism 2
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
A CG supervisor/TD at Expanse (Oslo; name garbled in captions). On Deadline, after Maya animation caches finish, a script builds three layers [35:06-35:37]. 1) Animation layer, all caches combined. 2) Look layer, shaders and groom: the script finds the assets in the animation layer and assigns the latest look version through the Prism Python API. 3) Utilities layer, cleanup and overrides, sitting above the others. The whisker problem arises because Maya wants a curve width of one while the look layer is lower in the stack; the utilities layer restores correct values [36:07]. Velocities are written in utilities for blur on the hair-deformation procedurals [36:07]. Moving to USD caches from Maya (2024) fixed vertex-order issues and enabled automatic effects layering, so water sims landed in the right layer without manual import [34:04-34:36].

**Use it:** Put every fix-up in the top layer so the animation and look layers stay clean and versions stay swappable.
