---
id: lighting-tanzillo-ask-for-a-grey-shader-scene-to-test-interior-against-exterior
title: If outside and inside end up near the same brightness, test with a grey default-shader scene and look for interior lights lifting it
domain: lighting
tags: [mike-tanzillo, critique, interior, exterior, grey shader, vignette, comp, scene check, deep-read, lighting-critique]
applies_to: Arnold
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=55eY1-LlY3k, src:yt-transcripts]
feeds: [shakedown, elevate]
conflicts: none
---
Mike Tanzillo 55eY1-LlY3k [43:12-46:19]: daylight outside should be far brighter than the room, but both had similar values, which forced heavy comp pushing and vignetting. He asked for the scene with one default grey shader on everything to inspect the light setup, including whether a lot of interior light was lifting the room to match outside.
With it fixed, vignetting would happen naturally. He also thanked the student for sharing the full Photoshop comp, noting how exposing a comp is intimidating.

**Use it:** When comp is rescuing the light balance, ask for the grey clay render and audit interior lights.
