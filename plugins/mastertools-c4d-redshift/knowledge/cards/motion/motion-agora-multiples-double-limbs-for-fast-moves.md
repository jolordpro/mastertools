---
id: motion-agora-multiples-double-limbs-for-fast-moves
title: Multiples: duplicate arms or legs on the same rig and offset them to sell fast moves, like a smear built from extra limbs
domain: motion
tags: [multiples, smear, double arms, stylized animation, skeletal mesh copy, control rig, agora studio, deep-read]
applies_to: Unreal Engine 5.6
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=hc6xf-3uDX8, src:yt-transcripts]
feeds: []
conflicts: none
---
Remy (animation supervisor at Agora) used doubled arms on very fast spins so the viewer follows the motion and to push stylization [32:29]. Steps: copy the skeletal mesh, poly-cut it down to just the limbs (same skeleton and skinning) [33:00-33:30], drop the copy into the sequencer, paste the control rig with its animation onto it, then offset the extra limbs [34:02]. Do it after the base animation is nearly done [34:34]. The doubling differs from smear, which deforms geometry.

**Use it:** A stylization trick for motion-design character shots: it is an animation-level fix and needs the final base animation first.
