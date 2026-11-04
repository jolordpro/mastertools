---
id: broadcast-avalanche-2022-stop-points-and-sub-timelines
title: On-air graphics need timelines with stop points, 'continue' cues, jump logic and sub-timelines (called 'directors' in broadcast)
domain: broadcast
tags: [unreal fest 2022, epic games, avalanche, andy blondin, bernt bk, timeline, stop point, playout, sub-timeline, deep-read]
applies_to: Unreal Engine 5.1 experimental
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=XAtjoawRN_Y, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Live graphics play to a point, stop while the presenter talks, and continue when an operator cues them. Avalanche added stop points and continues, logic to jump between points, and multiple sub-timelines inside one timeline for different options in the same graphic [27:11-27:50].
A layer bar groups keyframes so they move and scale together [27:50-28:20].

**Use it:** Build a live graphic as intro / hold / out with named cue points rather than one long timeline, so the operator can trigger each part.
