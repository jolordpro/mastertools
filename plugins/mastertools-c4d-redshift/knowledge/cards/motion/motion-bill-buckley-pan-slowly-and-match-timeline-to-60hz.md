---
id: motion-bill-buckley-pan-slowly-and-match-timeline-to-60hz
title: Pans judder on 60 Hz screens at 24p; a pan across a normal scene should take about 7-8 s, 30p fits 60 Hz evenly, and 24p footage can sit on a 30p timeline at 125%
domain: motion
tags: [bill buckley, panning, jitter, 24p, 30p, 3:2 pulldown, shutter, red pan calculator, camera move, deep-read]
applies_to: any (video, 60 Hz delivery)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=M9zFxw4FJ0k, src:yt-transcripts, https://www.youtube.com/watch?v=gw3T_UKTPJU]
feeds: [[motion-critique, coach]]
conflicts: none
---
Bill Buckley (camera tutor, single creator, low). 3:2 pulldown spreads 5 frames over every 4 of a 60 Hz timeline; judder appears in pans, tilts and orbits, not pushes [01:44-03:16]. 120 Hz screens divide 24 evenly (5) so look better [03:48]. Fix 1: shoot and edit 30p, since 60/30 = 2 [04:19]. Fix 2: put existing 24p on a 30p timeline at 125% speed (25p at 120%), not for talking-head audio [04:51-05:53]. Motion blur depends on shutter alone, not frame rate; he uses 1/50 at 30p for more blur than the 180-degree 1/60 [05:53-06:56]. Pan speed rule: about 7-8 s across a normal scene; slower frame rate needs slower pans; RED's pan-speed calculator for a 20 mm lens at 24 fps over 90 degrees gave 10-11 s, at 30 fps about 9 s, 45 degrees at 30 fps about 5 s [06:56-09:07]. Bad combinations: 60 fps footage on 24p timeline throws away 36 frames (60/24 = 2.5); 24 fps on 30p or 60p timeline always judders in pans; 30p into 24p works if slowed to 80% [11:48-14:31].

**Use it:** Camera move check in C4D: pans should be slower than instinct at 24 fps; if the delivery path is 60 Hz, test the pan there. Pan-time figures are his tutor rules, not a standard.
