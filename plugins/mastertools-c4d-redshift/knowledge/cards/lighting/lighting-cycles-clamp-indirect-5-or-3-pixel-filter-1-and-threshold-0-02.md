---
id: lighting-cycles-clamp-indirect-5-or-3-pixel-filter-1-and-threshold-0-02
title: Cycles tweaks for interiors: clamp indirect to 3-5 (default 10), never clamp direct, pixel filter 1 px, noise threshold 0.02
domain: lighting
tags: [clamping, fireflies, pixel filter, noise threshold, transparent bounces, persistent data, deep-read]
applies_to: Blender Cycles 3.x
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dLZEmfqob7k, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Numbers rileyb3d changes most, with a warning that no value is universal: noise threshold default 0.01, sometimes doubled to 0.02 for speed [08:27]. Light-path transparency raised to 24 because of glass and curtain layers, with little time cost [08:57]. Clamping: do not clamp direct light (breaks intensities); indirect default is 10 and he sets 5 or even 3 to kill indirect fireflies, testing each [08:57]. Film pixel filter default 1.5 px, he uses 1 px for a crisper image (look, not speed) [09:29]. Persistent data only helps when displacement or particles make scene load slow, and not for one still [10:00].

**Use it:** clamp indirect only (not direct) as a firefly fix and say the tradeoff, since it dims real highlights.
