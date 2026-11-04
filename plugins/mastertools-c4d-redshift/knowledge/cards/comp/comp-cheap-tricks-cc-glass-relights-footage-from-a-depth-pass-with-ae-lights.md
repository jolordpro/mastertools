---
id: comp-cheap-tricks-cc-glass-relights-footage-from-a-depth-pass-with-ae-lights
title: CC Glass uses a depth pass as a bump map, so After Effects point and spot lights can relight footage
domain: comp
tags: [cc glass, relight, depth bump, after effects lights, spotlight, night, deep-read]
applies_to: After Effects
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=-32g9bYyZuc, src:yt-transcripts]
feeds: [comp, lighting]
conflicts: none
---
On the footage layer add CC Glass, set its surface bump map to the depth layer with effects and masks, displacement 0 and height about 100; set the effect light to a point light with its height near 0 and lower the ambient: the depth acts like a normal map and the light rakes across the surface [58:20-59:27]. AE's own lights work too: add a white spotlight close to the image and far to one side, a night-blue point light for fill, and a red spot for a different mood; cone angle makes a helicopter searchlight [59:58-1:01:36]. The host's result is a Mars canyon at night from a day clip.
Transfers: a quick relight preview before asking for a re-render; an estimated depth gives rougher bump than a rendered one.

**Use it:** Treat as a preview-quality relight, not a replacement for rendered light groups.
