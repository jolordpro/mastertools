---
id: redshift-clouds-object-controls
title: Redshift Clouds (low and high altitude) render only in the render view, and wind speed animates better than offset
domain: redshift
tags: [clouds, sun and sky, wind speed, density, scattering, render view, 2026.8]
applies_to: Redshift 2026.8
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KoL7OAANlJ8, src:yt-transcripts, https://www.youtube.com/watch?v=74lleTzTfC4]
feeds: [redshift, coach]
conflicts: none
---
Two layers: low altitude (fully procedural noise) and new high altitude (texture based, so extreme scale or density shows repeats) [38:36-39:39, 48:35]. Add from Objects with a dome and HDRI, or Create Clouds in the Sun and Sky rig [38:06]. Sun and Sky also has time and location, day and night [1:12:58].
Look: density (thick means darker), coverage, shape (puffy versus wispy), altitude, thickness, two noise scales, seed. Dark clouds: lower density, raise scattering scale, direct and ambient lighting scale [44:57-47:02].
Animate wind speed, not offset: speed changes cloud skew and phase, offset just slides them [43:24]. Clouds do not show in the viewport, only the render view [47:32]. The trainer could not hide clouds from camera rays and keep them in reflections [52:54-54:40].

**Use it:** when a sky shot needs clouds, the coach lists these controls and the dark-cloud fix; the scene check treats the clouds object as a render-view-only item for look-dev drafts.
Transcript support: Second upload; trainer tried the Redshift tag and the volumetric clouds option to hide clouds from camera rays but keep reflections and neither worked. (https://www.youtube.com/watch?v=74lleTzTfC4 [37:41-55:10])
