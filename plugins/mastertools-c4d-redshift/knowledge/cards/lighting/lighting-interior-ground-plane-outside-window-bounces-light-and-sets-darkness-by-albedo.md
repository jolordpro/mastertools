---
id: lighting-interior-ground-plane-outside-window-bounces-light-and-sets-darkness-by-albedo
title: Interior trick: a large bright plane outside the window bounces light into the room; its albedo sets how dark the room gets
domain: lighting
tags: [interior, window, bounce plane, daylight, sun size, white balance, reference match, deep-read]
applies_to: Octane (any GI renderer)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=NdqK0UJYvYY, src:yt-transcripts]
feeds: [elevate]
conflicts: none
---
When the ceiling stayed dark he added a big plane on the ground outside the window; sun and sky light it and it bounces back into the room, and changing its albedo darkens or lightens the room [26:36]. He matched a reference photo on a second screen, dragging the sun in the kernel's sky sphere until the bounce pattern matched, raised sun size to soften wall shadows, and nudged camera white balance towards blue to keep it from over-warming [23:41, 24:13]. Balance sun, sky and exposure together: more sun means lower exposure [28:54]. Post: Octane glare for light bloom, vignette lowered [29:25]. Marble and floor were tuned by lowering glossiness gamma, not by new maps [25:19].

**Use it:** a window-plane bounce card is a quick fill for dark interior areas; matching a reference side by side is the check.
