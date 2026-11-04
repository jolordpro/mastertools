---
id: lighting-single-large-area-light-behind-subject-outside-vs-inside
title: One big area light just behind the subject, tilted, gives soft shape and a shoulder highlight; light further outside is mysterious, light on the camera side reveals everything flat
domain: lighting
tags: [one light setup, area light, backlight, outside inside, mystery reveal, bounce light, blender cycles, deep-read]
applies_to: Blender Cycles (principles transfer)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=si7UAgvBd4Y, src:yt-transcripts]
feeds: [coach, motion-critique]
conflicts: none
---
His favourite setup, used for about 80 percent of his work: one large area light behind the subject, a bit to the side, tilted so it does not cast ugly shadows on the background, especially with a wide lens [07:19][13:32]. Position logic: split the line between camera and background; "outside" is between subject and background (silhouette, mysterious), "inside" is between subject and camera (all revealed, flat) [08:22][09:26][11:27]. Behind the subject also gets bounce off the floor, which in Cycles does much of the work; the same setup in Eevee will not match [12:30]. Area light emits over 180 degrees, so a hard seam shows in frame if the light is too close to the side; rotate it [06:49]. Add a subdivision modifier to clear stomach artefacts [07:19].

**Use it:** use the outside-to-inside axis to talk about mood in a lighting review; mind that bounce relies on GI.
