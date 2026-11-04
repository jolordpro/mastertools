---
id: redshift-puzzle-matte-needs-object-id-tag-override-and-three-masks-per-matte
title: Redshift Puzzle Matte masks: set Object IDs in the Redshift object tag, switch the matte from Material ID to Object ID, and use one matte per three IDs
domain: redshift
tags: [puzzle matte, object id, material id, aov, mask, bucket, deep-read]
applies_to: Redshift in C4D
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=5hQKHD8fSs8, https://www.youtube.com/watch?v=iqrISqFY3bQ, src:yt-transcripts, https://www.youtube.com/watch?v=s-Cs6cg9JIc]
feeds: [redshift, comp]
conflicts: none
---
Add a Redshift object tag to each object, override Object ID and give each a number [Ross, iqrISqFY3bQ 03:38-04:09]. A new Puzzle Matte defaults to Material ID, so change it to Object ID and put the numbers in the red, green and blue ID slots [04:09-04:40].
One matte holds only three IDs (R, G, B); stack more mattes for more objects [05:12].
Puzzle Matte, and the Object ID pass, show nothing until bucket rendering is on [02:36; 5hQKHD8fSs8 09:21-09:52].
Material ID is not on the material; it is hidden on the output node in the node editor [5hQKHD8fSs8 10:23].
If a matte is empty behind glass, turn on Reflect/Refract IDs so objects behind transparent surfaces register [5hQKHD8fSs8 10:54].

**Use it:** Mask recipe for comp: Object ID per hero element, bucket preview, Reflect/Refract IDs on when a bottle or panel covers things.
Transcript support: Maya 2017 version: red channel material ID 1, matte used as Nuke grade mask rgba.red. (https://www.youtube.com/watch?v=s-Cs6cg9JIc [00:00-02:38])
