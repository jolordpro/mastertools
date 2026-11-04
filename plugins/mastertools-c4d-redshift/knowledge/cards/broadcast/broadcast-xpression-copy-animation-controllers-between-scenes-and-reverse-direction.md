---
id: broadcast-xpression-copy-animation-controllers-between-scenes-and-reverse-direction
title: XPression: paste animation controllers into another scene and remap them to a different object; reverse direction plays them backward
domain: broadcast
tags: [ross xpression, ross university, animation controller, copy paste, remap object, reverse direction, key graph editor, scene director, deep-read]
applies_to: Ross XPression (B108, 2026; reverse direction added in 5.5)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=71govSIChlQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Copy channels in the key graph editor: select position or rotation channels on the object, copy, double-click the other controller, select the target object and paste [08:23-10:32]. Offset controllers on the director to stagger the same move on two objects.
Copy a whole controller to another scene: right-click, copy, then paste on a track. If an object with the same name exists, keys attach to it; if not, a destination object list appears so you can pick any object [11:05-13:44]. The same controller can be pasted again to a second object [13:44].
Since 5.5 any clip has a reverse direction option (blue arrow turns yellow and points left), giving an out animation from an in animation [14:15-15:17]. Naming objects consistently across scenes makes the paste automatic.

**Use it:** Name objects consistently across templates so animation controllers carry over without remapping, and build outs by reversing ins.
