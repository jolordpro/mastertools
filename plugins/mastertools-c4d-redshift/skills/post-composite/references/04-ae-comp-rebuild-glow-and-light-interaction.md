# 04: AE comp rebuild, glow and light interaction

## Layer stack (bottom → top; 32 bpc linear)
1. Plate (the degrained version for derived work), linearized through OCIO.
2. `T_env_light` per light group: **Add**, masked where the person/proxy didn't render.
3. `T_shadow_occ`: **Multiply**, opacity tuned.
4. `T_env_refl`: **Add**, masked by the floor/glass Cryptomatte plus Fresnel (07).
5. Atmosphere (07): Add.
6. CG beauty (rebuilt or straight): Normal/Over, premultiplied, held out by the person matte when behind.
7. Glow from the Emission AOV: **Add**.
8. Lens layer: CA, whole-frame bloom/halation, vignette, redistortion.
9. Regrain.
10. Final grade adjustment layer, then the OCIO output.

## Additive beauty rebuild
- Beauty ≈ Diffuse + Specular + Reflections + Refractions + GI + Emission (+ Volume, SSS, Caustics). Light groups split these per light. **Add** in 32-bpc linear is correct.
- Verify: Difference(rebuild, beauty) ≈ black. A mismatch usually means a missing Caustics pass or RAW/non-RAW confusion.
- Grade per light group with **Exposure (stops)** and channel gains. Avoid Curves/Levels on linear data.

## Glow: tool choice
| Tool | Status | Use |
|---|---|---|
| Native Glow | Adobe | Small accents only. Its falloff looks linear and gives muddy cores. |
| **Deep Glow 2** | Plugin Everything (aescripts), paid | **Default hero glow.** Inverse-square-based falloff, 32 bpc, HDR threshold plus threshold smoothness (reduces flicker), gamma correction, aspect ratio, CA, tint/multicolor, lens dirt. |
| **Optical Glow** | Red Giant, Maxon One | Strong alternative already in Maxon One. Smooth multi-scale falloff with tint and chroma. |
| Universe Glow | Red Giant | Secondary |
| Sapphire S_Glow / S_Glare | Boris FX, paid | S_Glare (reworked in 2026.5) for glints and streaks, only if the lens shows them |
| Starglow / Shine | Red Giant Trapcode | Stylized streaks; Shine for god rays |

## Glow method (energy-plausible) [rule]
1. Source = **Emission AOV only**, so plate highlights aren't double-counted.
2. Multi-scale: sum 4–6 blurs at doubling radii (at 1080p: **2, 6, 18, 54, 160, 480 px**), with weights falling about ×0.5 per octave.
3. Energy check: the integrated brightness of the glow alone should be about **5–15% of the emission's**. If the core looks dimmer after adding glow, it has gone stylized.
4. Match the halo of the plate's own practical (radius and intensity at similar brightness). If the practical barely blooms, keep the glow restrained and put the energy into interactive light.
5. Convolution bloom: AE has no native FFT convolve. Approximate it with a lens-kernel defocus (Sapphire S_AdvancedDefocus or Lenscare custom iris) at low mix, plus a wide Deep Glow tail.
6. Add a separate whole-frame bloom/halation at a very low level, so plate and CG share one lens (06).

## Interactive light on the plate (ranked)
1. **Rendered env-light pass** (03) → Add. Correct falloff and occlusion. **Primary method.**
2. **Red Giant Scene Light** (2027.0, AE-only): relights using AI depth plus normals and AE comp lights, and accepts Redshift depth/normal passes. Runs locally. Good for people with no proxy normals, or for look-dev. **Known issues at release:** Edge Smoothing is broken, and the place-light buttons can freeze AE in non-English languages. Test on a duplicate comp.
3. **P/N relight in AE:** use World Position from the proxy render to build inverse-square distance masks to the animated emitter position (expressions, or ft-PPass2Matte 6.1.0, which supports AE 2026 on Apple Silicon [checked 2026-10-23]).
4. **2D fallback:** tracked feathered gradients blended Add, tinted to the plate. Only for distant spill.

## Light wrap
- For emitters, **reverse light wrap** matters most: emitter light wrapping onto the subject's silhouette edge when the emitter is behind them.
- **Red Giant Supercomp** (AE-only): 17 GPU context-aware tools, including Light Wrap, Reverse Light Wrap, Diffusion, Volume Fog and Optical Glow.
- Manual version: subject matte → Minimax/Matte Choker inner edge → multiply by blurred emission → Add.

## Do / Don't
- DO drive env-light intensity from the render. Don't hand-key flicker unless the emitter itself flickers.
- DO tint spill by the plate's local color.
- DON'T use Screen for light in 32-bpc linear (it isn't additive above 1.0). Use Add.
- DON'T let glow pass over a foreground subject when the emitter is behind them. Keep only a **5–15% residual** veiling glare.
