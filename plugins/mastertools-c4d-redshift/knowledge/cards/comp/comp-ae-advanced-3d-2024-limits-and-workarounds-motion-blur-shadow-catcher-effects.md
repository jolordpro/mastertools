---
id: comp-ae-advanced-3d-2024-limits-and-workarounds-motion-blur-shadow-catcher-effects
title: AE Advanced 3D (May 2024): no motion blur, no shadows-only catcher, no effects on 3D layers; each has a workaround
domain: comp
tags: [after effects, advanced 3d, environment light, hdri, glb, shadow catcher, motion blur, calculations effect, camera tracker, deep-read]
applies_to: After Effects with Advanced 3D renderer, 2024 beta/early release
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ks9TXSxSUGs, src:yt-transcripts]
feeds: []
conflicts: none
---
Premiere Gal (a tutorial host, low confidence; version specific, recheck on current AE). Models: use GLB over OBJ since it carries materials and textures [01:10]. Light: add an Environment Light, put the HDR at the bottom of the comp and select it as source; rotate to match the plate; use Draft 3D while moving around, raise render quality and shadow resolution only near the end [02:45, 04:20]. Limits and tricks: motion blur missing, so put CC Force Motion Blur on an adjustment layer [04:50]. No 'accept shadows only': duplicate everything but the footage, precomp as 'Shadows only', make the ground solid white (diffuse 100%, not shiny), cast shadows on the model, then multiply the precomp over the plate; also check 'Fit to scene' for the shadow box and shrink it to save time [09:01, 10:04]. No 2D effects on 3D layers: a solid with the Calculations effect set to copy from the 3D layer acts as a stand-in that takes Lumetri, blur or light wrap [11:06]. Placement: 3D camera track, set ground plane and origin, create camera and null, copy the null's position to the model [06:25]. He ends by saying Element 3D or Blender give more realistic results [13:43].

**Use it:** the multiply shadow-only precomp and the Calculations stand-in apply to any AE comp where a CG layer cannot take effects.
