---
id: c4d-grow-reveal-in-3d-mograph-selection-field-volume-builder
title: Growth works in 3D too: paint a MoGraph selection on a matrix, drive it with fields, feed an effector's visibility, then wrap in Volume Builder and Measure for growing geometry
domain: c4d
tags: [fields, mograph selection, freeze grow, volume builder, volume mesher, reveal, matrix, hide selected, deep-read]
applies_to: Cinema 4D 2022 (Maxon Ask the Trainer, Apr 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cCCgPVurWjQ, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Setup in a 40x40x40 matrix [11:40-13:44]: MoGraph selection tag with Use Fields on, a spherical field in place of the paint. Add a Plain effector with Position off and Visibility on, and drag the selection into its field list. Hide-selected effectors may need the field inverted [15:26-15:58].
Gotcha that cost the trainer minutes: with a Hide Selected effector, the effector's own Selection tab must be empty; a leftover selection there overrides the field and the setup does nothing [36:58-37:30]. Rebuild: selection kept, Freeze set to Grow, a Random field in the radius subfield (scale about 700 in the demo) [39:03-40:06]. Throw the matrix into Volume Builder then Volume Measure for growing blobby geometry [40:37].
Second trainer's tip: swap the grid for a 3D model as the matrix distribution so the growth builds a real final object from a start point, good for reveals; Redshift can render the volume alone [40:37-41:40].

**Use it:** A field-driven reveal of a logo or model: grow clones inside the object, mesh them with Volume Builder, keep the selection clean on the effector.
