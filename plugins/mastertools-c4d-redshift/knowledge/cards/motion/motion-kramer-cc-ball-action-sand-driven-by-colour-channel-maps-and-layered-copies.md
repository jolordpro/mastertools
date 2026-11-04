---
id: motion-kramer-cc-ball-action-sand-driven-by-colour-channel-maps-and-layered-copies
title: "Kramer's sand-dissolve in After Effects: CC Ball Action driven by an animated texture's colour channel, channel mixer for transparency, curves for speed, layered copies for density"
domain: motion
tags: [andrew kramer, cc ball action, after effects, sand, particles, channel mixer, curves, dissolve, polish, andrew-kramer, deep-read]
applies_to: After Effects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=5KYo8zFy1Ew, src:yt-transcripts, src:polish-roster]
feeds: []
conflicts: none
---
CC Ball Action turns pixels into little 3D balls, with a size control and a twist [07:57-08:28]. Trick: choose a colour channel as the control map, then animate a gradient texture over the layer; with the red channel selected the twist falls like sand [08:28-09:29].
Problem: there is no transparency. Fix: a Channel Mixer fades the other channels so only red is left, then tint to a sand colour [09:29-10:00]. Curves on the red channel change the velocity (faster or slower peel-off) [10:00-10:30]. To get enough particles, layer copies; then add a burn-out for the cracking edge and a texture on top, plus smoke elements [10:30-11:01].
His summary: simple plug-ins plus glue elements that pull mismatched pieces together; he calls his own result unfinished [11:01-11:32].

**Use it:** When an effect has no transparency or speed control, drive it with a channel from a separate animated map and adjust that map instead.
