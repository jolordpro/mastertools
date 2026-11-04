---
id: redshift-round-corners-radius-driven-by-scratch-map-via-change-range
title: Round Corners on bad topology: plug into bump, blend with the existing bump additively, and let a scratch map vary the radius
domain: redshift
tags: [round corners, bump blender, scratch, change range, bevel, radius, lionel, maxon, deep-read]
applies_to: Redshift 3.x in C4D R26 (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=TonSU8Ljm5c, src:yt-transcripts]
feeds: [lookdev, redshift]
conflicts: none
---
Real bevels fail on this mesh, so Round Corners goes straight into the bump input [54:59-55:30]. To combine it with the texture bump use Bump Blender: blend weight 0 disables a layer, and Additive mode is needed or the other bump disappears [56:31-57:38].
Feeding a grunge or scratch map into the radius breaks up the edges; the map outputs 0 to 1 which is too much, so a Change Range to about 0 to 0.3-0.4 tightened it [58:10-1:00:13]. The radius is scene-scale dependent.
Asked whether it works in the Standard and Physical renderers, the hosts were unsure [1:08:12-1:08:43].

**Use it:** supports the round-corners and metal-nicks cards; add the Change Range cap and the additive blender rule.
