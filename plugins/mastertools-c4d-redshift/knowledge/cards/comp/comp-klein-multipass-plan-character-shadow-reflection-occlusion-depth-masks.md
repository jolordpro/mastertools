---
id: comp-klein-multipass-plan-character-shadow-reflection-occlusion-depth-masks
title: Klein's 2011 multipass plan: render the character alone, with separate shadow, reflection, occlusion, depth and mask passes, composite in 32-bit AE and tint shadows by mask
domain: comp
tags: [maya, after effects, multipass, render layers, occlusion, depth pass, shadow pass, 32-bit, andrew klein, deep-read]
applies_to: Maya + After Effects (2011)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=6ZJbww8fUcA, src:yt-transcripts]
feeds: [post-composite]
conflicts: none
---
Andrew Klein's series outline (only the overview video) [00:34-07:17]: separate layers so only the character renders on alpha over a separate background [00:34-01:05]; a depth pass set correctly for blur and fog [01:36]; masks for colour change, sky cutouts and god rays [02:08]; an ambient occlusion pass, with variants for transparent objects and for cutting alphas [02:38]; a pass for the character's cast shadow and one for its reflections only [03:10-03:40]; dynamic file prefixes for batch naming [03:40]. Comp in After Effects at 32 bits per channel, because exposure moves need the extra range [04:44]. Grade by painting gradients and extra colour over the layered passes, using masks to tint the shadow areas blue, and finish with specular overlay and vignette [05:44-06:46].

**Use it:** Older but still sound pass list for a character-on-plate comp; pairs with the four-pass-category card.
