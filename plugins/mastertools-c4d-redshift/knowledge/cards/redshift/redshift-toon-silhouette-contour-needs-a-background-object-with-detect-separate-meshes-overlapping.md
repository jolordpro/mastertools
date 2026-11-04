---
id: redshift-toon-silhouette-contour-needs-a-background-object-with-detect-separate-meshes-overlapping
title: Thick toon outline on the silhouette only appears when an object behind has a contour with Detect Separate Meshes set to overlapping; too close and the weight varies
domain: redshift
tags: [redshift toon, contour, detect separate meshes, overlapping, background object, silhouette, tone map, cre8-or-die, deep-read]
applies_to: C4D + Redshift toon (2025 upload, CRE8-or-DIE)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=xaJ2pdIeLKA, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
The docs' background contour is not a setting: it needs every object, above all the background, to use contours [01:08-01:40]. With the background plane hidden the thick outline vanished; with it, the silhouette gets a chunky line [02:13-03:15].
Open the background object's own toon material, contour > Detect Separate Meshes > overlapping (intersecting also exists): any mesh overlapping it gets the contour; colour it red to see what happens, then match the subject's line colour [03:46-04:48]. When the subject leaves the background in frame, the line is lost [03:15].
Gotcha: a background very close to the model, still not intersecting, gives thick lines in some angles and thin in others at 20 thickness; move it back [06:21-06:52]. He avoids tone maps (hard gradient lines) and uses solid colour with a dome HDR for soft gradients [05:19].

**Use it:** the toon check: contours need a background mesh with overlapping on, set a safe gap behind the subject.
