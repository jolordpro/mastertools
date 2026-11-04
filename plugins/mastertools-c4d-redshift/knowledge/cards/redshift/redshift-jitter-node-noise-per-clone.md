---
id: redshift-jitter-node-noise-per-clone
title: Clones share one noise pattern; feed the MoGraph Jitter float into the noise offset (Float Max above clone count)
domain: redshift
tags: [jitter node, noise offset, cloner, texture variation, float max, mograph]
applies_to: Cinema 4D 2025 + Redshift
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KnfiJy2ND2o, src:yt-transcripts, https://www.youtube.com/watch?v=u6j9yrpgRhU]
feeds: [lookdev sheet]
conflicts: none
---
The same noise appears on every clone [35:33]. Use the Jitter node float output into the offset [34:02]; Float Max must exceed the clone count (100 clones, at least 100) to get distinct patterns [36:35]. Works with texture maps too. Solo a node in the C4D node editor to preview it [31:56].

**Use it:** Check cloned scenes for repeated procedural patterns and offer the node fix.
Transcript support: Jitter hue about 20 degrees varies watercolor colour per object (https://www.youtube.com/watch?v=u6j9yrpgRhU [17:48-21:00])
