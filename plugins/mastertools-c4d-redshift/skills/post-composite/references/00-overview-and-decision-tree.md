# 00: Overview and decision tree

## Standard pipeline (summary)
1. Plate QC. Make a degrained copy (Neat Video), then analyze the lens and camera (02, 10).
2. Camera layout in C4D (fSpy or C4D Camera Calibrator, plus a proxy box fit). Build proxy geometry and camera-project the plate onto it (03).
3. Redshift: CG emitters as mesh lights in light groups. Render Takes for beauty, env-light, reflections, shadows/occlusion and utility passes (03).
4. Write EXRs in ACEScg. In AE (OCIO, ACEScg working space, 32 bpc): additive rebuild → glow → interactive light → reflections → atmosphere → holdouts → lens FX → regrain → grade → output (04–07).
5. QC (08).

## Reading a shot: what to log
- Format: resolution, fps, codec, bit depth, chroma subsampling, color tags (primaries, transfer, matrix), legal or full range, duration and frame count.
- Display-referred and already graded (typical for ProRes Rec.709)? Then the pipeline must **not regrade it**.
- Camera: locked, drifting, handheld, or moving with parallax.
- Perspective: the number of vanishing points. With one VP, pitch and roll come straight from the VP. Focal length needs the camera report, or a second VP from converging verticals (02).
- Brightest *unclipped* practical light (LED strip, lamp, specular). **This is the energy reference for CG.** Clipped windows and sky carry no scene-linear information.
- Glossy or reflective surfaces (floors, glass, metal, water) the CG must reflect in. Missing reflections are the **#1 tell**.
- People or objects the CG passes in front of or behind: these need holdouts, plus light on them.
- Haze or veiling glare that increases with depth.
- Lens character: distortion, DOF, chromatic aberration, vignette, flares/ghosts, halation, bloom around practicals.
- Grain and noise level by channel and by shadows vs midtones.

## Decision tree
1. **Is the camera locked?** Track 3–4 high-contrast static features.
   - Drift under ~0.25 px → treat as locked. Use a static CG camera.
   - Sub-pixel to a few px of 2D drift → keep the static 3D camera and planar-track the drift onto the CG precomp.
   - Visible parallax → do a 3D solve (Mocha Pro 2026, SynthEyes, or AE 3D Camera Tracker as fallback) and export to C4D.
2. **Lens distortion visible?** Look for bowing straight lines near the frame edges.
   - Yes → undistort for layout → render the CG undistorted with overscan → **redistort the CG** (never the plate).
   - No → skip, but still match vignette and edge softness.
3. **Does the CG pass behind a person or object?** Yes → you need a temporally stable matte (05) and a proxy in C4D for shadows and light occlusion.
4. **Is the plate going to a colorist after VFX?**
   - Yes → deliver in the plate's own encoding, with no look baked in, and verify the round trip.
   - No → you own the grade, so do a final unification grade in AE.
5. **Which version line?** Mid-project → stay on the current version and match the OCIO config. Fresh start → C4D 2027.0 with AE 26.5, both on ACES 2.0.
6. **Linearization strategy:** see 01 (Strategy A, display-linear, is the default; Strategy B is scene-linear via an inverse output transform).

## Worked example: emissive orbiting ring in a glossy, backlit hallway
- Plate: 1920×1080, 23.976p, ProRes 422 HQ 10-bit 4:2:2, Rec.709, ~4.7 s (~113 frames), one-point perspective. Measured 2026-10-23: about 3 px of 2D drift (mostly vertical), no parallax.
- The window at the end **and the core of the ceiling LED strip are clipped** (measured). The LED strip's floor streak still gives the reflection shape. The brightest unclipped emitter is the red EXIT sign (92% of the clip ceiling), so energy is judged against it and against the strip's unclipped falloff.
- Glossy floor and dark glass panels: the ring must reflect in both.
- A backlit person walking away: the ring's light wraps onto their camera-facing side, and the ring is held out when it goes behind them.
- Recipe: Redshift mesh-light ring (`LG_ringA/B`), a hallway proxy with the plate projected onto it, a person proxy, and Takes `T_ring_beauty / T_env_light / T_env_refl / T_shadow_occ / T_utility`. Then the AE OCIO comp, Deep Glow 2 from Emission, Object Matte plus Mocha holdout, depth-matched haze, and Neat Video degrain/regrain.

## New in 2026 and worth using
- AE **Object Matte** (26.2+; propagation cached to disk in 26.5).
- Red Giant **Depth Generator** (2026.1+) and **Scene Light** (2027.0, which accepts Redshift depth and normal passes).
- **Mocha Pro 2026** Refine Solve.
- Redshift 2027.0 camera **Auto Focus**.
