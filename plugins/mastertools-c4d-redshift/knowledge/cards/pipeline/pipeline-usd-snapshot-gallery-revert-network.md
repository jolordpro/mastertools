---
id: pipeline-usd-snapshot-gallery-revert-network
title: Solaris snapshots store the image and the network state so you can revert to any look
domain: pipeline
tags: [solaris, snapshot gallery, revert, non destructive, look comparison, sidefx, deep-read]
applies_to: Houdini Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=TLJPDt4YpYM, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Keating [25:00-26:33]: with many layered overrides, take a snapshot after each change; it appears in a gallery with its render. Clicking 'revert to this snapshot' restores the network and starts rendering it again. The gallery is saved with the hip file [28:19-28:49].
Trade-off he states: full control through overrides, protected by the ability to go back.

**Use it:** A per-look snapshot habit for comparing lighting variations with the client.
