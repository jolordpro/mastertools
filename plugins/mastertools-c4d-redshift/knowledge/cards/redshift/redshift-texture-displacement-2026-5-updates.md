---
id: redshift-texture-displacement-2026-5-updates
title: Texture displacement 2026.5 added smooth-normal edge handling (new default), tag-level projections, polygon-selection displacement and UDIM support
domain: redshift
tags: [texture displacement, edge handling, smooth normals, projection, polygon selection, udim, uv context projection]
applies_to: Redshift 2026.5
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dFYep-8B0aU, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
[57:45] Edge handling in the Redshift object tag: smooth normals is the new default and fills the gaps that vertex normals left at hard edges.
[58:47] Material-tag projections now work with texture displacement (before, vertex displacement was needed). UV Context Projection also works but, in the speaker's experience, must be wired to both the noise and the output.
[1:00:18] Different displacements per polygon selection do not mix or add. UDIMs supported.

**Use it:** check displaced cubes and hard-edged meshes for gaps when a scene predates 2026.5.
