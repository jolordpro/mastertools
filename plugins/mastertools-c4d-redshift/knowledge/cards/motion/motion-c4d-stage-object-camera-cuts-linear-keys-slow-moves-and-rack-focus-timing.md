---
id: motion-c4d-stage-object-camera-cuts-linear-keys-slow-moves-and-rack-focus-timing
title: Cut between cameras with a Stage object, set camera keys to linear, move slowly, and time the focus switch mid-move
domain: motion
tags: [c4d, stage object, camera animation, linear interpolation, depth of field, aperture, rack focus, motion blur, octane, deep-read]
applies_to: Cinema 4D 2023 + Octane camera tag
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=wAVOwrxLHcA, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Anton (September channel, a self-taught artist then finishing a VFX degree), auto-captions. Stage object: key which camera is active (camera 2 on frame 149, camera 1 on frame 150) to cut inside one render [46:53]. Camera moves: slow and incremental, mostly changing orientation, starting from an interesting frame rather than the sim's start frame [47:56, 48:29]. In F-curves select all and set linear, since default ease makes the move look odd where it hands over to the next camera [50:00]. Depth of field on every shot for a pro look: set aperture (he used 10, then 5, then eased down to 2.5 as too extreme), pick focus by clicking in the viewport, focus on a far point then a closer one [51:04, 53:43]. For a deliberate rack focus, stretch the focus key handle so the switch happens about mid-move [52:39]. Compose with elements in foreground and background [18:36]. Motion blur: add the Octane object tag to the sim parent, enable camera motion blur and set shutter 0.333 at 30 fps (he was unsure of the formula) [57:51].

**Use it:** linear keys at cuts and mid-move rack focus are small review checks for camera animation.
