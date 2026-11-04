---
id: c4d-2027-scatter-clusters-count-and-empty-patches
title: Scatter clusters group object types into Voronoi patches; a cluster count above the object count leaves empty gaps
domain: c4d
tags: [scatter, cluster, voronoi, scatter tag, probability, variation, mograph]
applies_to: C4D 2027.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
[38:46] The Cluster tab replaces pure randomness with patches of one object type. Count equal to the types gives one patch each; lower mixes the leftover types; higher leaves empty patches, so 4 types in 11 or 20 clusters read as sparse flower beds [40:50 to 41:53].
Smoothness and border breakup hide the Voronoi look [39:48]. A scatter tag on each object sets its probability (0% empties it) and overrides variation, filter and cluster ID [46:01 to 47:01].
Add random rotation (full spin, a few degrees tilt) and scale on top to kill repetition [44:27].

**Use it:** use for grass, flower and debris fields: set count equal to types, then add empties for density control.
