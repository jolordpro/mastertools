---
id: comp-delta-keyer-clean-plate-from-footage-when-light-changes
title: When light flickers on a locked-off screen, build the clean plate from the footage itself, then add a garbage matte and spill tweak
domain: comp
tags: [[keying, delta-keyer, clean-plate, garbage-matte, fusion, color-space-transform], deep-read]
applies_to: DaVinci Resolve Fusion (principles apply to Nuke, After Effects)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=zlZCKT-5pLU, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Dean Yurke: a locked-off shot would normally use an empty frame as the clean plate, but changing light means building one from the footage: Clean Plate node, eyedropper on the screen, then fill/grow edges and erode so it keeps as much screen as possible and loses as much person as possible [05:00-06:43]. Feed it to the Delta Keyer's clean plate input (alt-drag shows which input), pick the screen colour, add a garbage matte shape (inverted, soft) avoiding hands [06:43-07:18]. Adjust spill colour a bit (more red, less blue) but not so far that blue leaves the face [07:54]. Check the key over an ugly solid background [07:18].
Before keying, he applies a Color Space Transform from the camera space (Blackmagic 4.6K Film Gen 3 here) and checks the viewer as linear to sRGB, since Unreal works in linear sRGB by default [03:55-04:29].

**Use it:** Check keys over a loud solid colour and convert camera footage out of camera log first.
