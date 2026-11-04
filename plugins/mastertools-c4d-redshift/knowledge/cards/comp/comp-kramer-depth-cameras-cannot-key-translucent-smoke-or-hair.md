---
id: comp-kramer-depth-cameras-cannot-key-translucent-smoke-or-hair
title: "Kramer: depth capture does not solve translucent smoke, thin hair or fume edges; that needs software that understands the image, not more pixels"
domain: comp
tags: [polish, andrew-kramer, depth, z depth, translucency, keying, roto, witness camera, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=gNh9r-VbSVg, src:yt-transcripts, src:polish-roster]
feeds: [polish-coach]
conflicts: none
---
Shown a huge depth-capturing camera, Kramer asks what depth value a pixel of thin translucent smoke has, and the same for transparent hair [1:13:19-1:13:50]. His view: edges and semi-transparency are a software and understanding problem, not a hardware one [1:13:50-1:14:20]. Depth still helps compositing, for example pushing smoke around a person, and a witness camera beside the main one is a known way to collect depth and parallax data [1:15:53-1:16:24]. He expects rotoscoping to be automated through AR work [1:12:18]. (2018.)

**Use it:** Do not plan to separate hair, smoke or glass with a depth pass alone; render a proper alpha or volume AOV for those.
