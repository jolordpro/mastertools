---
id: lookdev-xpu-local-contact-sheet-replaces-farm
title: RenderMan XPU rendered about 6-8 variant stills a minute locally, enough to make a look-dev contact sheet without the farm
domain: lookdev
tags: [renderman, xpu, contact sheet, look dev, scott keating, pdg, variants, vram, deep-read]
applies_to: RenderMan 24 XPU, Houdini 18.5
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=TLJPDt4YpYM, src:yt-transcripts]
feeds: [estimator, redshift]
conflicts: none
---
Keating [16:12-18:17]: a PDG graph baked the asset, converted PNG textures to .tx, built about 15 variants in a loop, rendered one camera per variant locally and assembled a contact sheet for look-dev approval. He measured about 6-8 images a minute (roughly 10 s each), noting other work was running at the time.
XPU gave a near-final image almost instantly after a short GPU load pause [12:36]. Specs from the Q&A: RenderMan recommends 24 GB VRAM for production scenes, compresses geometry on GPU and caches textures, but volumes are limited to single scattering at that point and XPU targets look dev [38:19-38:56]. XPU does not use RIB [42:24].

**Use it:** Batch variant stills as a contact sheet for client picks. Matches the pull-then-compare habit.
