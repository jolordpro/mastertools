---
id: pipeline-one-render-engine-across-all-packages
title: Artjail keeps one render engine across Maya, Houdini and Nuke so materials move one to one and debugging stays fast
domain: pipeline
tags: [ross denner, artjail, cg garage, render engine, v-ray, look development, materials, small studio, deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=uMmdYi4xP0Y, src:yt-transcripts]
feeds: [redshift, plan]
conflicts: none
---
Ross Denner (head of 3D, Artjail) says he wants all assets and rendering in a single engine. A lookdev artist builds materials in Maya, they go to Houdini and render one to one, and an effects artist can reuse the same shaders for volumes; the same engine works with Nuke and Unreal [46:34-47:35].
For a studio with one or two TDs, a quick sanity check is easy: if it should work in the engine and does not, there is a deeper problem [47:07-47:35]. Hybrid CPU and GPU rendering means any box can serve any artist [48:39].
He also says render-engine choice is like religion and that a 4K frame in three or four minutes is already impressive [49:10]. Note: this is a vendor's podcast (Chaos V-Ray) and he is a V-Ray user, so weigh the opinion.
Transfers to Redshift: one engine through C4D, Houdini and Maya reduces shader translation.

