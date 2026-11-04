---
id: motion-judder-is-uneven-frame-time-from-3-2-pulldown-or-dropped-frames
title: Judder is uneven frame time (24p on 60 Hz repeats frames 3, 2, 3, 2), not the same thing as low-frame-rate stutter
domain: motion
tags: [judder, stutter, 3:2 pulldown, 24p, 60 hz, apple tv, frame drops, motion interpolation, deep-read]
applies_to: TVs (RTINGS)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CuEZIJDEQyo, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Cedric (RTINGS) defines judder as some frames staying on screen longer than others; stutter is a low but constant rate [00:08-00:38]. 24 fps on a 60 Hz display shows odd frames three times and even frames two times, so the movement jerks; phones, tablets and a PC on a non-multiple-of-24 refresh have it [00:38-01:09]. Test: a 24 fps clip with a square at each position for one frame per second, long exposure photo; uneven brightness means judder [01:09-01:41]. Many TVs pass with a 24p input but fail when the source sends 60p (Apple TV always outputs 60 Hz) because the TV must detect and reverse the pulldown [01:41-02:45]. Sony example: Motion Flow to True Cinema and Cine Motion high [02:45]. A second cause: frame drops from motion interpolation on fast movement or slow TV apps [02:45-03:17].

**Use it:** when preview playback of 24p renders looks jerky, check the playback refresh rate before blaming the animation; delivery of 24p should stay at a 24p container.
