---
id: comp-hdr-sdr-single-master-light-separation
title: A single EXR master can serve both SDR and HDR if the approved SDR picture is kept and HDR headroom is used only for added light
domain: comp
tags: [hdr, sdr, single master, emission, glow, exr, tone mapping, openexr]
applies_to: After Effects, OCIO (2D animation case)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-g6JTD8cge4, src:yt-transcripts]
feeds: [comp planner, broadcast]
conflicts: none
---
Imagica [03:41 to 04:44]: keep the finished SDR art unchanged; extend emission, glow and optical effects above SDR white; derive SDR, HDR and non-tone-mapped views from one open EXR master.
SDR derive [06:49]: keep low and mid ranges, compress the added light into the top range, for example keep the picture to about 95 nits of 100 and squeeze the glow above it. Several tone maps were prepared and chosen per shot inside the OCIO config [07:19].

**Use it:** for HDR/SDR deliveries, keep glow and emission on a separable layer so SDR can be derived.
