---
id: redshift-light-samples-isolate-gi-noise
title: Set light samples higher in a default scene so leftover grain can be blamed on GI, not on area lights
domain: redshift
tags: [light samples, area light, gi noise, soft shadows, overrides]
applies_to: Redshift 2026
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
Chad's reason for a 512 light override: much of the noise is from area lights and soft shadows, not GI [1:10:20-1:10:52]. With lights sampled enough, remaining grain tells you to look at GI.

**Use it:** coach: when a render is noisy, test light samples first.
