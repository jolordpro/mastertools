---
id: c4d-redshift-team-render-single-image-since-3-0-14-each-machine-needs-a-licence
title: Redshift 3.0.14 (early 2020) let Team Render split one still across several machines; each machine needs its own Redshift licence
domain: c4d
tags: [team render, single image, distributed, key art, redshift 3.0, winbush, deep-read]
applies_to: Redshift 3.0.14-3.0.16 for C4D (2020)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=KtBZwIaOUnU, src:yt-transcripts]
feeds: [pipeline, estimator]
conflicts: none
---
Use Render, Team Render to Picture Viewer, with the machines ticked [01:34]. Machines turn yellow when initialised and it takes a moment to send the scene [01:34-02:05]. Each rectangle in the picture is one machine contributing to the same image [02:05].
Before this, each machine took a whole frame; now one frame is spread over all of them [02:05-02:38].
Winbush's scene (high-poly, 4k textures, 8k HDR) took 1 min 19 s over six GPUs: a 2080 Ti with a Titan X on one machine, four 1080 Ti on the other [02:38-03:08].
Scene used radiance cache with a point cloud secondary.

**Use it:** Key art and posters: use Team Render to Picture Viewer for big stills on a multi-machine setup, and count one Redshift licence per machine.
