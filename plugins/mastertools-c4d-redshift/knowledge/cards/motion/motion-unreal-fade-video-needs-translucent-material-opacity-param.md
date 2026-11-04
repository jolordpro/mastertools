---
id: motion-unreal-fade-video-needs-translucent-material-opacity-param
title: To fade or tint a video or alpha clip in Unreal, make the material translucent, expose opacity, and keyframe the instance in Sequencer
domain: motion
tags: [unreal, sequencer, material instance, opacity, alpha channel, translucent, patrick-wongbo, deep-read]
applies_to: Unreal Engine 4.25
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=WLdmYnkFoK4, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Steps shown by Patrick Wongbo [44:14-57:41]: set blend mode to translucent (or masked) so an opacity pin appears; plug the clip's alpha into opacity or nothing happens (the top mistake with alpha videos) [47:51]; multiply by a scalar parameter for fade; make a material instance and expose opacity (and a colour multiplier for tint). In Sequencer add a static-mesh-component track and pick the material parameter; Sequencer builds a dynamic material instance for you. Trap: assign the correct material to the mesh BEFORE adding the track, otherwise Sequencer keeps making dynamic instances of the old one and the keys pop between two materials [55:05]. Closing and reopening Sequencer also cleared it [54:04].

**Use it:** Use as the checklist when a fade does nothing in an Unreal comp: blend mode, alpha wired, parameter exposed, right material assigned first.
