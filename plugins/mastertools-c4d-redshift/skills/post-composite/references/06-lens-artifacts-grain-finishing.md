# 06: Lens artifacts, grain and finishing

## Defocus / DOF
- Match the CG's softness to plate objects at the same depth.
- Tools:
  - **Frischluft Lenscare** (paid): depth-driven blur, custom iris. AE 26.x support unconfirmed: last news 2025, Mac builds were rolled back in 2023 [checked 2026-10-23]. Test before relying on it.
  - **Sapphire S_AdvancedDefocus** (2026.5): physically accurate bokeh, cat's-eye, CA, lens dirt. Good on bright emitters.
  - Red Giant **Universe Bokeh** fed by Depth Generator or Redshift Z.
  - AE **Camera Lens Blur** (native, 32 bpc, depth layer).
  - **Rendered DOF in Redshift** (2027.0 adds camera Auto Focus).
- Rule: if an **emissive element is noticeably defocused, render the DOF**. 2D defocus of emission produces the wrong bokeh energy.

## Chromatic aberration
- Sample a high-contrast edge near the corners. If there's a 1–2 px lateral fringe, apply radial CA to the **CG and glow only** (not the plate).
- Tools: Red Giant **Chromatic Displacement**, Deep Glow 2's CA, Universe, Sapphire.

## Flares and ghosts: only if the plate's practicals produce them
- If the plate shows none, add **none**. Unmotivated flares are a classic tell.
- **Red Giant Real Lens Flares**: ray-traced. 2026.5 added zoom and aspherical lenses. 2027.0 added custom animated "Schmutz" dirt and light-source types (**LED, fluorescent**, HMI, tungsten, sodium vapor, fire).
- Video Copilot **Optical Flares** (mature, little development; AE 26.x support unconfirmed [checked 2026-10-23]). **Sapphire S_LensFlare** (Pro Lens Flare Packs in 2026.0/2026.5).
- Red Giant **Knoll Light Factory was discontinued in March 2023** (last shipped in VFX 2023.2.0). Use Real Lens Flares. Only KLF EZ / Knoll Light Transition remain [checked 2026-10-23].

## Halation, bloom and vignette
- Apply a subtle **whole-frame bloom** so plate highlights and CG share it.
- Halation (red-orange fringe on highlight edges) only if the plate shows it.
- Vignette: measure the plate's corner-vs-center falloff on similar tones and apply it to the CG if the CG was rendered without one. **Never double-vignette the plate.**

## Motion blur
- Preferred: **3D motion blur rendered in Redshift**. 2D vector blur arcs badly on rotation and orbits.
- Alternative: Redshift motion vectors → **RSMB Pro Vectors** (RE:Vision, paid; 7.0.0 supports AE 2022–2026 [checked 2026-10-23]). A Redshift Motion Vector AOV turns off motion blur in the beauty, so render it from a separate Take. AE Pixel Motion Blur is optical flow, meant for plate elements.
- Match the shutter against the moving subject's blur length.

## Grain and compression
1. **Degrain** a plate copy with **Neat Video 6** (6.1 supports AE 2026; 8/16/32 bpc). Profile it on a flat area. Use the degrained plate for roto and anything blurred or relit.
2. "Least touch" approach: comp the CG over the **original** plate and use the degrained plate only for derived passes, when the plate itself is mostly untouched.
3. **Regrain** the CG and any modified plate areas, **matched per channel**. Video grain is often stronger in blue and in shadows. Tools: Red Giant Magic Bullet **Film / Renoiser**, Sapphire S_Grain, native Match Grain / Add Grain (slow; **8/16 bpc only** [checked 2026-10-27], so they drop a 32-bpc chain), or difference grain (original − degrained, valid only where the image is unchanged).
4. Compression texture: perfectly clean CG chroma looks too sharp on 4:2:2 ProRes. Apply about 1 px of horizontal chroma blur to the CG.
- AE **Remove Grain**: **8/16 bpc only**, per Adobe's effect page [checked 2026-10-27]. Keep it out of a float chain. Prefer Neat Video.

## Final grade unification
- **Blacks:** the CG must not go below the plate's black floor. Sample the darkest plate area and lift the CG to match (Levels or Colorista Lift on the CG precomp).
- **Saturation:** emitters are the classic oversaturated element. Desaturate the halo toward the plate's palette, and let the core go toward white as it brightens.
- **Highlight rolloff** (Strategy A): soft-clip CG emission above ~0.9 so it rolls to white like the plate's practicals, with no single-channel clipping. Use Magic Bullet Looks/Colorista or a 32-bpc curve.
- **Unify:** finish with a subtle whole-frame grade (Lumetri or Magic Bullet Looks/Colorista). Keep it minimal if a colorist follows.
