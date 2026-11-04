---
id: broadcast-pq-vs-gamma-led-signal-1-point-0-is-100-nits
title: Epic recommends PQ for LED walls: scene 1.0 maps to 100 nits and values above are kept; with gamma, 1.0 is wall peak and anything above clips
domain: broadcast
tags: [[pq, st2084, gamma, eotf, led-wall, exposure, nits, unreal], deep-read]
applies_to: Unreal Engine 4.27
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bh5wD1YapJo, src:yt-transcripts]
feeds: [CHECKS, coach]
conflicts: none
---
Epic [03:42-07:25]: Unreal's scene is linear; encoding for the processor (PQ / ST 2084, or gamma such as 2.2, 2.35, 2.4, 1.8) is the EOTF. PQ fixes a known brightness per code value, so the wall panels are responsible for producing it; gamma is relative, so the processor needs a peak-brightness control. Default mapping: 1.0 equals 100 nits, and values well over 1.0 are encoded, letting the scene stay fully HDR. If dim, raise exposure in nDisplay config actor, Color Grading, Entire Cluster, exposure compensation, or post-process colour correction (all linear) [06:21-06:53]. With gamma, 1.0 targets peak wall brightness and anything above is clipped, and the exposure needed differs from PQ's [06:53-07:25].

**Use it:** Wall-content briefs state PQ or gamma and the nits target for 1.0; graphics designed for broadcast white need a stated mapping to the wall.
