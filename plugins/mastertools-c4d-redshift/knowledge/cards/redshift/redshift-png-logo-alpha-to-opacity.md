---
id: redshift-png-logo-alpha-to-opacity
title: A PNG logo with transparent background needs a color splitter with alpha plugged into opacity
domain: redshift
tags: [logo, png, alpha, opacity, color splitter, decal, texture]
applies_to: Redshift 2026
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=t9hy0YCq0I8, src:yt-transcripts]
feeds: [shakedown, redshift]
conflicts: none
---
Texture node into a color splitter, Alpha output into material opacity, so only the logo shows [1:35:01-1:35:32]. To combine the logo with an existing texture, use the same alpha as the Color Layer mask [1:35:32]. If the background does not vanish, the file has no real alpha [1:35:01].

**Use it:** scene check: logo texture with alpha but opacity unconnected; the coach shows the setup.
