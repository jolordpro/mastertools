---
id: comp-normals-light-mask-softness-fake-specular
title: A normals light mask with a softness control makes a fast specular highlight without opening a 3D relight setup
domain: comp
tags: [normals, light mask, specular, softness, relight, nuke, rotation, sampling]
applies_to: Nuke normals toolkit
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=M-iKJu9hYBk, src:yt-transcripts]
feeds: [comp planner]
conflicts: none
---
[07:31 to 08:17] The toolkit's masking node lights by rotation or by sampling a point on the normals, and its softness control broadens the response; raising it a lot gives a specular-like highlight.
He prefers it to a full 3D relight setup, which he calls overkill for most shots.

**Use it:** for quick highlight tweaks on CG passes, use a normals mask first.
