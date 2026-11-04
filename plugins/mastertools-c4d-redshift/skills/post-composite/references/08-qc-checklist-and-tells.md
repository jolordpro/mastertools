# 08: QC checklist and tells

## Supervisor checklist (run in order)
1. **Black level:** the CG's darkest values must be no darker or bluer than the plate floor at similar depth.
2. **Energy:** compare the emitter core with the brightest unclipped practical. If the emitter is brighter, its spill and reflections must be correspondingly stronger.
3. **Falloff:** spill falls off roughly with inverse square and is occluded by architectural detail (frames, rails).
4. **Light on subjects:** present when the emitter is near, on the correct side, and occluded when the emitter is behind.
5. **Edges:** no chatter, halos or dark rims (premultiplication errors), and motion blur handled.
6. **Grain parity:** at 200%, check each channel. Grain size and strength must match in midtones and shadows.
7. **Motion blur parity** with the plate's shutter.
8. **Temporal stability:** no glow-threshold flicker (use Deep Glow threshold smoothness), no denoiser shimmer, no boiling AI mattes or depth.
9. **Lens parity:** defocus, CA and vignette consistent with neighboring plate objects.
10. **Haze/depth:** the CG lifted by the same haze as the plate at the same depth.
11. **Color:** vectorscope (CG never far beyond the plate's saturation) and waveform (CG peaks against the practical and window peaks).
12. **Views:** the delivery view plus a check view (±2 stops, a contrasty check LUT, alpha views). **Flip the frame horizontally** to see it fresh. Watch at speed and looped.
13. **Round trip:** difference of untouched regions against the source = black.

## Tells → fixes
| Tell | Fix |
|---|---|
| Glow with a muddy grey core / linear halo | Deep Glow 2 or Optical Glow from Emission in 32 bpc |
| No reflection in a glossy floor or glass | Render `T_env_refl` |
| Light doesn't touch the set | Env-light pass |
| CG too saturated for the grade | Desaturate the halo, whiten the core |
| CG blacks deeper than plate blacks | Lift to the plate floor |
| Clean CG over a grainy plate | Regrain per channel |
| Glow spills over a subject in front of it | Hold out the glow, keep 5–15% veiling |
| Unmotivated lens flares | Remove |
| Sharp CG in a soft region | Match defocus |
| Hard single-channel clipping (e.g. a cyan blowout) | Soft rolloff to white |
| CG floats while the plate drifts | Apply the measured 2D track to the CG precomp |
| Plate light changes over the shot, CG light stays fixed | Animate CG exposure / interactive light to the measured curve (10) |
| CG straight lines stay straight while plate lines bow | Redistort the CG (02) |
