---
id: motion-nabors-easing-by-trigger
title: Pick easing by who triggers the motion: ease-out for user actions, ease-in for system-initiated, near-linear for fades
domain: motion
tags: [motion-tokens, product, rachel-nabors, easing]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2028-10-30
sources: [https://www.youtube.com/watch?v=teQkx1SVq4g, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Rachel Nabors: fast-to-slow reacts quickly to a user; slow-to-fast suits system pop-ups so they do not startle; fades and color changes sit near linear but not truly linear. Keep a bounce on hand but use rarely. She defines custom curves as Sass variables so they carry the brand. Related: motion-three-easing-roles (enter/exit framing).

**Use it:** Name each easing token by trigger as well as direction.
