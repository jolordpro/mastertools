---
id: lookdev-moonlight-from-daylight-in-comp-desaturate-dim-multiply-blue
title: Day-for-night from a light group: desaturate to zero, drop gain to about 0.2, multiply by a blue-ish colour
domain: lookdev
tags: [day for night, moonlight, light group, desaturate, multiply blue, gain, deep-read]
applies_to: any compositor
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=IjFXi2axl-8, src:yt-transcripts]
feeds: [elevate]
conflicts: none
---
Process [08:19-08:50]: on the sun group, saturation 0 and gain about 0.2 for the level; then a multiply with a bluish second input for the tint. Dim the environment group at the same time (saturation 0.5, gain about 0.4) so the room reads as night [08:19]. This only works when the light is rendered separately; grading the finished frame also dims the practical lantern. The video is a Blender course ad in places [04:40].

**Use it:** a quick lighting-variant technique for pitch alternates (day, dusk, night) from one render; values are the speaker's starting points, not rules.
