---
id: pipeline-agora-rig-blueprint-with-attached-fx-and-animator-feedback
title: Wrap a character's control rigs and attached assets in one blueprint; build the next rig from animator feedback rather than copying Maya
domain: pipeline
tags: [agora studio, control rig blueprint, rig updates, animator feedback, quality of life, dynamics, bake to fcurves, deep-read]
applies_to: Unreal Engine 5.6/5.7
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hc6xf-3uDX8, src:yt-transcripts]
feeds: []
conflicts: none
---
First they put control rigs in the sequencer; now a blueprint holds the character's rigs plus related assets such as thruster FX or a robot's gun, which can be toggled and refined by FX later; rig updates ripple across all sequences [41:21-42:22]. Copying the Maya rig in Unreal was workable but not how Unreal works [42:55]. Animators gave a ranked list of fixes (control visibility, pickability, hierarchy, intuitive IK/FK and bend controls, localized mouth corners, built-in spine IK, gimbal head) that the riggers took for the next episode [42:55-44:28]. Live dynamics (hair, earrings, clothes) can be tweaked and then baked to fcurves for frame-level polish [30:26-30:56]. Work in progress for the next episode: gravity and wind-noise defaults in the dynamics, a breathing function with speed and amplitude, and eye darts for the one robot with pupils [44:58-46:33].

**Use it:** Gather an animator wish list at the end of each episode or project and give it to rigging before the next.
