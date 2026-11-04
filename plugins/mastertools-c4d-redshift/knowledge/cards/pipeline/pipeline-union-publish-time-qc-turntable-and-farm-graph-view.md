---
id: pipeline-union-publish-time-qc-turntable-and-farm-graph-view
title: Run QC and a turntable preview at publish time, and monitor the publish graph live on the farm
domain: pipeline
tags: [union vfx, publish qc, turntable, preview render, pdg, deadline, imagemagick, wrong camera, deep-read]
applies_to: PDG, Deadline
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=nUXfEdZ-7Xs, src:yt-transcripts]
feeds: [CHECKS, shakedown]
conflicts: none
---
At publish, Union's PDG graph renders a preview turntable (with an HDRI choice), collects geometry statistics and overlays them on frames with ImageMagick, producing a QuickTime [22:19-23:52]. Options include scale conversion, decimated LOD generation, and USD/USDA/Alembic output [25:58].
The farm manager cannot show a PDG graph, so jobs split into sub-jobs for rough status; the log exposes the PDG data layer server, which a Houdini session can attach to and show the graph running [22:50, 29:06].
Result: wrong cameras or animation caches are caught at publish before reaching the render farm [31:10].

**Use it:** Pre-render gate: automatic stats and a preview clip on every publish.
