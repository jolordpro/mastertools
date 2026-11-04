---
id: redshift-gobo-on-a-spotlight-texture-slot-or-shader-graph
title: Gobos on a Redshift spotlight can go in the texture slot for quick use or a shader graph for offset, tiling and colour control
domain: redshift
tags: [chad-ashley, greyscalegorilla, redshift, c4d, gobo, spotlight, deep-read, polish]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=mDT94FHPg9c, src:yt-transcripts, src:polish-roster]
feeds: [redshift, lookdev]
conflicts: none
---
Chad (Greyscalegorilla): a gobo is something placed in front of a light to throw shadows, from blinds to branches [00:02-00:34]. A new Redshift spotlight is very bright, so turn it down first [01:06-01:37].
Texture method: put the map in the spotlight's texture slot (a link tag via the company's Drop Zone helps); the only position control is rotating the light. Under details, a softness setting lets shadow softness also blur the gobo, and it cannot be separated [01:37-04:42].
Preferred method: add a spotlight material graph, plug the gobo into the colour input, and link the file name through the tag; then offset UV, tile (he used 1.5) and add colour correct for tint or gamma [05:14-08:20]. Caustic maps need a wider cone angle [07:18-07:48].
Caption names for the link tag are garbled; check in-app. Not yet checked against the redshift ledger.

**Use it:** Use the graph route when the gobo needs placement, scale or a tint; use the texture slot for a quick test.
