---
id: c4d-physical-renderer-put-the-diffuse-as-a-lambertian-reflectance-layer-not-the-color-channel
title: C4D Physical renderer (2017) - moving diffuse from the Color channel to a Lambertian reflectance layer cut a still from 40 s to 14 s with GI off
domain: c4d
tags: [physical-renderer, reflectance, lambertian, render-time, gi, greyscalegorilla, legacy-c4d, deep-read]
applies_to: Cinema 4D R18-era Physical renderer (2017; not Redshift)
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=thZ7TRegehk, src:yt-transcripts]
feeds: [estimator, shakedown]
conflicts: none
---
Greyscalegorilla (Nick), uploaded 2017-04-25. Test scene: a textured character with an HDRI and Team Render.
- With GI (QMC primary and secondary) the still took about 40 s. With the Color channel off (no diffuse) it took 11 s, so he blames the Color channel [02:07-03:42].
- Fix: copy the colour shader, add a Lambertian layer in the Reflectance channel, drag it to the bottom of the stack (diffuse always lowest), paste the shader into its texture; for a flat colour, copy colour and paste into the layer colour [03:42-04:46]. Colour channel off, GI off: about 14 s, near identical [04:46-05:19].
- Costs: slightly more colour bleed on the glasses (brighter); compensate by hand [05:19]. He gives it as halving render time for animation [00:01].
- This is the Standard/Physical material model; Redshift works differently.

**Use it:** A legacy-renderer speed rule for any old Physical-render files; not a Redshift setting.
