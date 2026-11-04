---
id: redshift-motion-blur-shutter-position-center-end-start-frame
title: Redshift (C4D S22 era) motion blur shutter position: use Center Frame; Start and End Frame shift the blur and drop it on the first frame
domain: redshift
tags: [motion blur, shutter position, center frame, end frame, start frame, shutter efficiency, loop, deep-read]
applies_to: Redshift 3.x in Cinema 4D S22 (2020)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=tsx8Isq6m-s, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Derek Kirk [01:10-04:19]: enable Motion Blur in Redshift render settings; only shutter position and shutter efficiency matter. Efficiency 1 (default) is fine; 0.5 is closer to a real camera, small difference. Center Frame blends motion from the previous and next frame and keeps the object where it is, the look he uses nearly always. End Frame uses only the previous frame's motion, so frame 0 has no blur; Start Frame is the opposite and uses the next frame. Change only to patch frames or fix a loop whose first frame lacks the blur the last has [09:28-10:31]. Test on a linear (no ease) move.

**Use it:** Use Center Frame as default; if a loop pops at the seam, suspect shutter position first. Check the shutter against the current docs.
