---
id: pipeline-union-usdz-for-transport-but-not-yet-primary
title: USDZ bundles an asset and its textures into one zip file for transport, but renderers could not yet read textures inside it
domain: pipeline
tags: [union vfx, usdz, usdzip, archive, textures, transport, client handoff, deep-read]
applies_to: USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=nUXfEdZ-7Xs, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Schneider [13:02-14:04]: USDZ is a zip-based archive; the usdzip tool gathers textures under the root file and rewrites references inside, so one file freezes the textures at publish time for sending to clients or another studio. Limit (2023): renderers could not resolve textures inside the archive, so it could not be the primary format; he hoped to switch within 6-12 months [32:12]. Maya's exporter also could not move USD proxy shapes yet [32:44].

**Use it:** Use USDZ for external delivery; keep loose USD internally.
