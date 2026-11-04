---
id: lighting-octane-washed-ambient-hdri-plus-targeted-area-lights-with-falloff-map
title: Washed-out white HDRI as ambient only, then targeted area lights with a falloff map for the shaping; set ACES at the start
domain: lighting
tags: [octane, aces, hdri, area light, target tag, falloff, camera visibility, light group, c4d, deep-read]
applies_to: Octane in Cinema 4D 2023
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=wAVOwrxLHcA, src:yt-transcripts, https://www.youtube.com/watch?v=mNcq8GD1mfI]
feeds: [elevate]
conflicts: none
---
Anton (September channel, a self-taught artist then finishing a VFX degree), auto-captions. Pick the colour space (ACES) at the very start so lighting is built in it, path tracing on [16:31]. Two HDRI strategies: a directional-light HDRI rotated until shadows fall right, or a washed gradient white studio HDRI used only as ambient while area lights do the shaping [20:39, 21:10]. He likes washed-out white renders because they are clean and let colour be added later [25:17]. Rotate the light's target by adding a Target tag aimed at a null at scene centre, so lights always aim at the sim [22:43]. Untick camera visibility so close lights are not seen; duplicate and offset the lights [23:45]. Add a Cinema 4D falloff map in the light's distribution (vector, 90 degrees) for varied light across the scene, then a power around 50 [24:46]. Group the lights under a null and keyframe the group for subtle light movement without touching targets [56:20]. Dark shadows in the middle: rotate HDRI, raise its strength, or lift shadows later in Resolve [41:56].

**Use it:** the target-null habit and ambient-only HDRI are quick set-ups for product-style C4D shots.
Transcript support: Falloff map distribution at 90 degrees for a softbox-like area light on the car. (https://www.youtube.com/watch?v=mNcq8GD1mfI [05:19])
