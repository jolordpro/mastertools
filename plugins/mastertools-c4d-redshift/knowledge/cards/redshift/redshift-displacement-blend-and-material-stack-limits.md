---
id: redshift-displacement-blend-and-material-stack-limits
title: Displacement can blend up to four layers, but stacked materials hit a 63-parameter limit
domain: redshift
tags: [displacement blender, material stacking, closures, 63 parameters, additive, mask, shader error]
applies_to: Redshift 2026.8 (version inferred from stream date)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KoL7OAANlJ8, src:yt-transcripts, https://www.youtube.com/watch?v=74lleTzTfC4]
feeds: [redshift, shakedown]
conflicts: none
---
New in 2026.8: texture displacement can be blended with a displacement blender (base plus layers 0 to 2, so up to four) [31:05]. Blend weight 0 means none, 1 replaces the base; additive mode sums displacements; a ramp or noise mask picks regions [31:37-32:40].
Material stacking with Add Material also works, but the trainer says a limit of 63 mixed parameters (nine per material, so about six to seven materials) applies [34:18]. Past it, Redshift reports no legal combination of shader nodes [34:59].

**Use it:** a scene check can count stacked or blended materials and warn before the limit; the coach names the 63-parameter cause when that error appears.
Transcript support: Stack limit explained as 63 parameters; error text is "legal combination of shader nodes"; about six materials hit it. (https://www.youtube.com/watch?v=74lleTzTfC4 [29:02-35:29])
