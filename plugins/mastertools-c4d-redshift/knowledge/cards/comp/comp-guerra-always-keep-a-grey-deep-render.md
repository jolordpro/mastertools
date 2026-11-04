---
id: comp-guerra-always-keep-a-grey-deep-render
title: Always render at least a grayscale deep pass: it lets rain, drops and other elements be occluded correctly later
domain: comp
tags: [deep render, deep compositing, occlusion, rain, hugo guerra, nuke, deep-read]
applies_to: Nuke deep, any renderer
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=NaCJiquNnYY, src:yt-transcripts]
feeds: []
conflicts: none
---
Because he had deep data from the CG, every added water droplet was occluded properly by stones and cement [16:46]. He advises everyone to keep at least a deep render; it need not be coloured, a grayscale one is enough because you can recolour it [17:17]. It also helps position elements [17:17].

**Use it:** Add 'grayscale deep or Z-pass for later insertion' to a render-output checklist for shots likely to take late FX.
