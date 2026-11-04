---
id: motion-pan-time-scales-in-stops-from-the-seven-second-rule
title: Pan judder guide: start at 7 seconds to cross one lens field of view, then double the pan time for each stop more pan angle, narrower field of view; halve it for each stop more resolution or frame rate
domain: motion
tags: [mark-jaeger, judder, pan speed, shutter, frame rate, resolution, focal length, red calculator, deep-read]
applies_to: any camera or CG camera
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=gw3T_UKTPJU, src:yt-transcripts]
feeds: [motion-critique, CHECKS]
conflicts: none
---
Judder comes when the displacement across the frame is too large for the capture rate [00:02]. Film guide: at least 7 s for a pan crossing one horizontal field of view of the lens; it does not guarantee no judder, just a start [01:36-02:07]. Scaling in stops (each stop doubles or halves): pan angle +1 stop = time x2 (60 degrees takes twice 30) [03:09]; resolution +1 stop = time /2 (2K to 4K halves it) [03:09-03:41]; narrower field of view (38 mm to 80 mm) = time x2 [04:13-04:45]; frame rate +1 stop = time /2 (30 to 60 fps) [04:45-05:18]. For combined changes he uses the RED pan calculator [06:21]. His tests: 4K, 25 fps, 1/50 s shutter, 50 mm, 50-degree pan at 10, 13, 17 and 24 s, with 17 s as the calculated safe time; judder dropped as the pan slowed [07:27-07:58]. Fast pans with slower shutter can be the chosen look [06:54].

**Use it:** Use for camera-move QC on tracked or CG cameras: compute a minimum pan time from angle, focal length and frame rate before animating. Extends motion-bill-buckley-pan-slowly-and-match-timeline-to-60hz.
