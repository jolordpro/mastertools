---
id: redshift-ipr-starter-settings
title: Greyscalegorilla's starter set for fast Redshift look dev: CPU and hybrid off, low quality, 128 progressive passes, bucket 256, under-sampling 3
domain: redshift
tags: [preferences, ipr, progressive passes, bucket size, hybrid, undersampling, unified sampling, preset]
applies_to: Redshift in C4D (2023)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=le17-h6tUD0, src:yt-transcripts, https://www.youtube.com/watch?v=LcxjkHFS-2k]
feeds: [redshift, coach]
conflicts: none
---
Preferences: GPUs on; CPU rendering and hybrid rendering off; material previews only when the renderer is idle; IPR auto start off [00:31-01:34].
Render settings: bucket quality Low, progressive passes 128, GI on, combined and trace depths default, bucket size 256 (up to 512 possible) [02:04-03:40].
In the render view set View, Under-sampling to 3 for interactivity; progressive is for look dev, bucket mode for final frames [07:48-08:49].
Save the set as a preset so it need not be redone [04:11-04:42].

Ledger agrees: §4 "Progressive Passes applies to Production Progressive and Live only" and final delivery through Bucket.

**Use it:** the coach can offer this as a baseline draft preset and the draft step can store it as a named preset.
Transcript support: Chad (2017): progressive for look dev, bucket for client frames; progressive passes about 128; also turn off material preview auto-refresh [36:19] (https://www.youtube.com/watch?v=LcxjkHFS-2k [06:13-07:47])
