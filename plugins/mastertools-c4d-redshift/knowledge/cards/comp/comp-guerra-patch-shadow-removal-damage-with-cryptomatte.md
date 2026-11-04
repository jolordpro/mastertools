---
id: comp-guerra-patch-shadow-removal-damage-with-cryptomatte
title: After removing shadows, patch damaged foliage by compositing the original vegetation back through Cryptomatte
domain: comp
tags: [cryptomatte, patch, vegetation, shadow removal, hugo guerra, nuke, deep-read]
applies_to: Nuke, Cryptomatte
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NaCJiquNnYY, src:yt-transcripts]
feeds: []
conflicts: none
---
Removing the shadow pass broke the grass and ivy on the stones, which lost quality [06:54]. His fix: use Cryptomatte to pull the vegetation and merge it on top of the CG [07:25]. Keep this as the usual follow-up when a pass-level grade damages thin detail.

**Use it:** If a pass-level grade damages thin elements, mask with Cryptomatte or ID and restore from the beauty rather than re-grading.
