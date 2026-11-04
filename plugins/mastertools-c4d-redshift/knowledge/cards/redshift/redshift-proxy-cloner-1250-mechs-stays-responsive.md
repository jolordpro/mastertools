---
id: redshift-proxy-cloner-1250-mechs-stays-responsive
title: About 1250 proxy mechs in a MoGraph cloner stayed interactive in 2017, where non-proxy clones would stall the viewport
domain: redshift
tags: [proxy, cloner, instances, scene weight, push apart, greyscalegorilla, chad, deep-read]
applies_to: Redshift 2.x, C4D (2017 stream)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=MuVzbVhMUvI, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
Cloner in Object mode (he changes the default away from Grid) on a disc, instances on, align-to-clone off: 350 mechs loaded fast, then 800, then 1250 with no strain [09:19-12:32]. He says he has taken a high-res asset to about 2500 copies and found it fine, but did not try it live.
Push Apart effector (duration about 120, radius 150 to 190 in his scene) spread them; Random effector moved X and Z only and rotated about 15 degrees [10:26-11:28].
His explanation: Cinema 4D only holds bounding boxes while Redshift loads the heavy meshes, whereas ordinary clones of dense geometry make C4D die.

**Use it:** estimator: a proxy crowd costs render memory at render time, not viewport time; treat the 2017 counts as an order of magnitude only.
