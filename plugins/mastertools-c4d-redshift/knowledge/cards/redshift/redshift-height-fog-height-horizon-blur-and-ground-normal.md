---
id: redshift-height-fog-height-horizon-blur-and-ground-normal
title: Redshift Environment height fog: height value limits fog to a layer, horizon blur softens its edge, and a ground normal of -1 flips it
domain: redshift
tags: [height fog, ground fog, horizon blur, ground normal, use transform, environment, volume, deep-read]
applies_to: C4D + Redshift, Maxon Redshift channel upload 2018
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vnHKQmvKYH8, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Height 0 fogs everywhere; any other value fogs only at that height, e.g. 50 shows fog at the ground [06:52]. Horizon blur sets how soft the transition is at the far horizon: higher is smoother, lower is tighter; 0.1 was used [07:00-07:32].
Use Transform (on by default) can be switched off to type a ground point and ground normal by axis; -1 on the ground normal reverses the fog into the sky, and an X or Z normal makes a wall of fog [07:53-09:43].
Emission is the fog colour and attenuation must be above 0 to see it [05:53].

**Use it:** height fog recipe for night streets or arenas; remember the fog needs attenuation above 0, which also dims light shafts.
