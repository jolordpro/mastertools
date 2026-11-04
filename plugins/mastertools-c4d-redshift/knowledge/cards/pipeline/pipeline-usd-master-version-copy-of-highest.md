---
id: pipeline-usd-master-version-copy-of-highest
title: Publish a master version that is always a copy of the highest version, so downstream paths never need repointing
domain: pipeline
tags: [pipeline, versioning, master version, publish, usd, prism, file paths, deep-read]
applies_to: Prism
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=CpiumJctktM, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
In the asset import list there is version 1 and a master version; the master is always a copy of the highest version [07:15] [07:46]. If the geometry gets a version 2, anything that imported the master updates without re-reading file paths [07:46].
In shots, importing a USD asset as USD objects keeps a reference, so asset updates flow into the layout scene [16:01].

**Use it:** Check: shot files should point at the master or latest, not hard-coded version paths, unless the shot is frozen on purpose.
