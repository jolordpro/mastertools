---
id: redshift-geometry-id-colour-ramp-range-drives-triplanar-offset-rotation-and-gamma
title: One wood shader on many objects: Color User Data geometry ID through ramp and Change Range varies texture offset, rotation and gamma per object
domain: redshift
tags: [user data, geometry id, ramp, change range, triplanar, variation, randomisation, greyscalegorilla, chad, deep-read]
applies_to: Redshift 2.x in C4D (2017 stream)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=MuVzbVhMUvI, src:yt-transcripts]
feeds: [lookdev, coach]
conflicts: none
---
Colour User Data set to Geometry ID colour gives each object a pseudo-random value, which Chad says is not truly random and has no seed, unlike Arnold [35:33-36:33]. He views it through a ramp (grey-scale for his eyes), then a Change Range node: 0 to 150 into triplanar offset [37:04-37:36], about 0 to 10 degrees into rotation [38:08-38:40], and for tone variation a colour-correct gamma of roughly 0.85 to 1.1-1.25 kept subtle [39:44-42:15].
To reshuffle without a seed he adds and redistributes knots in the ramp [40:44-41:45].
A UV grid image in place of the wood makes the offset visible while building [39:12].

**Use it:** coach: answer for identical-looking repeats; pair with the Jitter node card when a seed is wanted.
