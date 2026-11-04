---
id: pipeline-usd-layout-with-reference-arcs-not-baked-geometry
title: Agent-built USD layouts should write reference arcs plus transforms with pxr, not use Blender's exporter, and match up axis and meters per unit
domain: pipeline
tags: [[usd, layout, reference, blender, up-axis, metersperunit, pxr], deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bWvxBu_vVes, src:yt-transcripts]
feeds: [coach, CHECKS]
conflicts: none
---
Rahgoshay's layout stage: phase 1 places primitive stand-ins (cones for trees, boxes) in depth bands and sets the camera, cheap for the artist to push around; phase 2 replaces each with a reference to the production asset instead of importing geometry [2:13:35-2:14:39].
He avoided Blender's USD exporter because it bakes geometry and flattens hierarchy; instead PXR Python writes an XForm with a reference arc and transform per object, giving a light USDA with names, transforms and references that opens in Houdini, Maya or Unreal [2:14:39-2:15:41]. Check up axis and meters per unit, or scale breaks [2:15:10]. Lock tool and USD plugin versions rather than updating everything [2:32:19].

**Use it:** Scene-check candidates for any USD handoff: up axis, meters per unit, references not baked meshes.
