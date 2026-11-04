---
id: c4d-database-textures-slow-consolidate
title: Textures read straight from the C4D asset database are compressed and make Redshift material edits crawl; consolidate them
domain: c4d
tags: [asset database, texture, consolidate, project asset inspector, slow materials]
applies_to: C4D 2023-2026 with Redshift
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=uKRqHwVr0F4, https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts]
feeds: [coach, CHECKS]
conflicts: none
---
Materials from the asset browser can point into the database; editing a node (a gamma tweak) hangs [14:38, RF]. Pause the render view, open Window > Project Asset Inspector, pick the database assets, Consolidate to the project tex folder; edits become near real time [15:09].
Greyscalegorilla uses Cargo's save-a-copy-into-tex setting for the same reason [45:01, GSG].

**Use it:** scene check: flag texture paths inside an asset database.
