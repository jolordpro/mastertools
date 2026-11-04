---
id: pipeline-agora-bake-animation-to-versioned-clips
title: Bake animation into versioned clips that the main edit references, so crashes stay isolated and versions can be swapped per character
domain: pipeline
tags: [agora studio, baked animation, clips, versioning, constraints, motion blur ghosting, unreal, deep-read]
applies_to: Unreal Engine 5.5-5.7
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hc6xf-3uDX8, src:yt-transcripts]
feeds: []
conflicts: none
---
Animation lives in per-shot files holding every version and its layers, and only baked animation clips are used in the main edit [24:50-25:21]. Unreal 5.5 animation crashed the edit with constraint problems, and isolation made the animators' file a playground with no ripple effect on others [25:51]. Clips carry version metadata, so a broken one is traced, versions can be changed from a drop-down when a director wants to go back, and versions can be mixed per character [26:21-27:23]. Baking also removed motion-blur ghosting caused by live constraints and gave smoother playback [27:54-28:54].

**Use it:** Use versioned baked clips as the hand-off between animation and lighting; ghosting on fast action is a clue to live constraints.
