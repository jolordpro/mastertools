---
id: ai-models-guerra-beeble-pbr-passes-prep-and-limits
title: For Beeble PBR passes, export footage underexposed at 2K; the passes flicker and need heavy deflicker, and its relight tool is not usable
domain: ai-models
tags: [beeble, pbr passes, normals, base colour, deflicker, copycat, hugo guerra, deep-read]
applies_to: Beeble, Nuke CopyCat
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=NaCJiquNnYY, src:yt-transcripts]
feeds: []
conflicts: none
---
Footage for ML tools should be exposed down because they dislike overexposure, and brought to 2K since most tools cannot take 6K [24:29]. He used Beeble for normals, roto, base colour with no shadows, depth, specular and roughness [25:32-26:36], but they are low-res and flicker [25:32]. CopyCat did deflicker some, but 8 hours on an RTX 3090 (24 GB) removed only part; days would be needed [28:41, 42:47]. His try with Resolve or Furnace did not match CopyCat [42:15]. Beeble's lighting tool gave harsh results; dividing its colour by the raw plate gave a usable B/W light pass that could then be upscaled and deflickered [29:14-30:17]. A normals pass from every plate is now routine for him [48:35].

**Use it:** For an AI pass of live footage, plan for resolution and flicker cleanup, and test one shot before promising. Complements ai-models-beeble-studio-switchlight-3-pbr-passes.
