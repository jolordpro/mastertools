---
id: comp-dof-in-post-by-default-in-camera-for-glass-and-extreme-depth
title: Chad Ashley: roughly half his DOF is post (Lenscare on a depth AOV); he does it in camera for glass or extreme foreground and background
domain: comp
tags: [chad-ashley, depth of field, z depth, lenscare, post dof, min depth, ledger-check, deep-read]
applies_to: Redshift 2.x, Fusion/Nuke/After Effects (2018)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ARykOD6lG3c, src:yt-transcripts]
feeds: [comp, coach]
conflicts: comp-depth-aov-setup-rs
---
Rule: if it can be faked in post he fakes it, for control; in camera when there is glass, or a tight shot with something extreme in the foreground and the background. He puts it about 50/50 [42:25-43:31].
Depth AOV as he remembers it: filter type Min Depth, because the Z pass must not be anti-aliased and needs a little extra edge; he says to update the post if wrong [13:35-14:07, 38:15-38:46]. In the comp Redshift depth is white far, black near, so invert, auto-range, then pick the sharp zone; 16-bit half depth is brighter than white [39:17-39:48, 41:22]. Iris: six facets with a slight anamorphic squeeze [39:48-40:20].
Fringes on foreground edges come from a filtered Z pass or from asking fake DOF to do too much [46:09-46:40].
Ledger check: comp-depth-aov-setup-rs says Center Sample for non-antialiased depth; this speaker recalls Min Depth, unsure.

**Use it:** Do not copy his filter name into the check; use the existing Center Sample card and keep the post-vs-camera rule.
