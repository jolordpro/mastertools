---
id: comp-octane-blender-openimagedenoise-leaves-the-denoised-aovs-black
title: In Octane for Blender, Open Image Denoise denoises the beauty but the other denoised AOVs come out black, so a compositor-bound export needs the Octane compositor rebuild
domain: pipeline
tags: [egomotion-academy, octane, blender, open image denoise, aov, black passes, export, deep-read]
applies_to: Octane for Blender (2025)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=NlDrXkb37lg, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Octane's own AI denoiser gives denoised beauty and denoised AOVs together; with Open Image Denoise (prefilter auxiliary AOVs on) the beauty looks far better but the other denoised AOVs are black [04:13-05:49]. He says that is a problem for sending passes to After Effects, Nuke or Fusion, and his fix is the Octane compositor rebuild [05:49-06:20]. Version-specific; test before trusting.

**Use it:** A render-settings check: confirm which denoised AOVs are really non-black before delivering passes.
