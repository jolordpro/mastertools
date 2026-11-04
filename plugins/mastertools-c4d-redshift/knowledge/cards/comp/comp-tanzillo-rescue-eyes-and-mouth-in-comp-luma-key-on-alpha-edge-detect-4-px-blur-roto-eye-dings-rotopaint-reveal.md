---
id: comp-tanzillo-rescue-eyes-and-mouth-in-comp-luma-key-on-alpha-edge-detect-4-px-blur-roto-eye-dings-rotopaint-reveal
title: Fixing eyes and mouth when only the comp survives - luma key from the alpha, edge detect plus 4 px blur, two tiny roto eye dings, warm mouth via a rotopaint reveal
domain: comp
tags: [mike-tanzillo, nuke, cryptomatte, luma-key, rotopaint, eye-ding, exr, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=sTCeHUto1IM, src:yt-transcripts, https://www.youtube.com/watch?v=55eY1-LlY3k]
feeds: [comp, post-composite]
conflicts: none
---
Case: a Maya file was lost, so notes (more value in the eye, warmth in the mouth) had to be done on three renders [12:09-19:28].
1. A cryptomatte grabbed the whole character because the body covers the eyeballs with transparency; instead the alpha showed the eyes differ slightly, so a luma key on the alpha isolates them [14:14-15:15].
2. Chew in the janky edge, edge-detect the alpha and add a 4-pixel blur, paste the graded eyes over the original, adjust hue and saturation for flexibility [15:45-16:16].
3. Sample colours around the scene and roto two tiny eye dings [16:53].
4. Mouth warmth: rough roto, grade warmer, tweak the black point, then use a Roto Paint node with the graded copy as second input (becomes bg1) and paint away the top layer to "reveal" [17:24-18:27]; fine for stills, frame by frame for animation.
It works because an EXR with no pure black or pure white keeps pullable values. He checks by sliding exposure up and down; the mouth interior stayed very dark, upper-left corner was crunchy [18:58-19:28].

**Use it:** keep the eye and mouth interior on their own ID mattes in C4D renders so notes do not need this rescue.
Transcript support: U1 staging card; related eye-read fixes: lens tint to the edges, HUD outside, eyes brightened (https://www.youtube.com/watch?v=55eY1-LlY3k [46:19])
