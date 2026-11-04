# 10: Scene analysis signals → recommendations

How `scripts/analyze_plate.py` measures a plate, what each number means, how far to trust it, and which recommendation it triggers. Thresholds marked [rule] were calibrated on 2026-10-23 against two real plates (ProRes 422 HQ 1080p hallway; H.264 UHD low-key hallway) and the synthetic `selftest.py` (15 checks with known answers). They are starting points. Tune per show.

## Contents
1. Running it
2. Measurements: method, threshold, trust
3. Signal → recommendation rules
4. Known limits (read before trusting a silence)
5. Report format

## 1. Running it
```
python3 scripts/analyze_plate.py PLATE --out DIR      # ~35 s for 113 frames of 1080p ProRes
python3 scripts/selftest.py                           # proves the detectors still work; expect 15/15
```
Outputs: `plate_analysis.json` (every number, method, threshold), `contact_sheet.jpg`, `overlay.jpg` (VP, lines, clipped areas, practicals, streaks, panels, subject boxes, CA tiles), `maps.jpg` (subject coverage, sharpness heat, haze curve, bloom curves), and a one-screen summary on stdout.

Always open `overlay.jpg` and `contact_sheet.jpg` and confirm candidates by eye. The script proposes; the frames decide.

## 2. Measurements

The script decodes to 16-bit 4:4:4 and does its own Y'CbCr→R'G'B' with the tagged matrix. Values are **legal-range normalized**: 0 = code 64, 1 = code 940 (10-bit). Sub-blacks read negative and super-whites read above 1. Nothing is clamped.

| Signal | Method | Threshold | Trust |
|---|---|---|---|
| Format, range | ffprobe tags + a Y code histogram | below-black / above-white % | High |
| Camera | LK tracks with forward-backward check, RANSAC affine per frame (direct and chained) | locked < 0.25 px; 2D drift ≤ 4 px [rule] | High. Confirmed on the main plate by phase correlation of two regions |
| Parallax | Homography residual p90 over a 12-frame baseline | > 0.5 px [rule] | Medium. Needs camera motion to show |
| Vanishing points | LSD segments → RANSAC VP; verticals tested for convergence | VP inliers | High for 1-VP corridors |
| Focal length | From the depth VP + the vertical VP: f² = −(v1−c)·(v2−c). Reports hFOV, mm for S35 and FF, pitch, roll | needs a vertical VP | Medium. A guess until the camera report confirms it |
| Lens distortion | Edge-following tracer on long lines near the frame edge; per-line bow → k1, weighted by each line's noise | edge bow > 0.75 px and ≥ 2.5σ [rule] | Medium. `note` warns when one line carries > 70% of the weight |
| Clip ceiling | Per-channel histogram **hump** at the top (graded plates clip into a pile-up, not at the max code). The noise tail above the hump is ignored | prominence 1.5, level ≥ 0.85 | High. Fixed two failed earlier methods |
| Energy reference | Bright blobs below the ceiling, with contrast to their surroundings. Reports % of ceiling and aspect | ≥ 0.55 and +0.10 over surroundings | Candidates only. Speculars on glass and metal show up too. Pick the true emitter on the overlay |
| Black floor | Luma P0.1 / P1, darkest RGB, near-black tint | none | High |
| Palette | Mean chroma per luma band, hue name, chroma p99 ceiling | neutral if sat < 0.10 | High |
| Gloss | Bright streaks: vertical (±15°) or along a VP line (±4°), on the floor below the horizon, not on the subject, symmetric. **Paired** = sits under a bright source | aspect ≥ 3 [rule] | GLOSSY needs ≥ 1 paired streak. Unpaired only = "possible" (carpet and rails cause these) |
| Dark panels | Large dark connected areas, subject excluded, nothing > 25% of the frame | `low_key` flag on dark plates | Medium |
| Haze | Dark level along **one** dark surface from near to far (ring fallback) | far − near lift > 0.025 [rule] | Medium. A gradient in the surface's own light also reads as haze. Check the frame |
| Grain | Temporal MAD per channel and luma band on static pixels, plus a spatial white-noise estimate and autocorrelation | invalid if below 1 code (compressed) | High on ProRes. On H.264 use the spatial numbers |
| Moving subject | Drift-compensated median background, gated by optical flow (speed > 0.15 px/frame, 21 px dilation). Reports boxes, speed, IoU, clean-plate source | IoU first/last | Box is conservative: it can include the subject's floor reflection and some ghost |
| Shutter | 10–90% edge rise of moving edges vs static edges (lens softness) | measurable only if motion > 0.75 × static rise | ±20% on synthetic (149° for a true 180°). Slow movers → "indeterminate, assume 180°" |
| DOF | High/mid frequency energy per tile vs distance from the VP | far/near < 0.80 = far soft [rule] | Medium |
| CA | Phase correlation of R and B gradient tiles against G in the corners; constant chroma-siting offset removed | > 0.5 px [rule] | High |
| Bloom | Radial profile around clipped areas and practicals: r50, r10 | "near" ratio | Medium |
| Ghosts | Mirror-position test through frame center | skips sources near the center | Low |
| Flicker | Static pixels in a 6×4 tile grid. Global factor = median tile. **Flicker** = frame-to-frame wobble around a 7-frame average. **Exposure change** = start vs end and swing. **Local light change** = tiles that move against the global factor | flicker > 1% [rule]; exposure > 3%; local > 5% | High. Beats slower than ~1 Hz read as exposure change, not flicker |

## 3. Signal → recommendation rules
- **Rec.709-tagged video, graded** → 01 Strategy A (display-linear), ACEScg working space, 32 bpc, round-trip test.
- **Sub-blacks or super-whites present** → keep them. 32 bpc preserves them. Never clamp the plate. Ask production whether the export is a legal-range grade with excursions or full range mis-tagged as legal. Interpret it per the answer and rerun the round-trip test.
- **Locked** → no track. **2D drift ≤ 4 px, no parallax** → 2D track (Mocha Pro planar, fallback AE Track Motion or King Pin) applied to the CG precomp. **Parallax** → 3D solve (Mocha Pro, fallback AE 3D Camera Tracker or SynthEyes).
- **1-VP + vertical VP** → build the C4D camera from the measured focal and pitch. Verify with a proxy box against the floor and wall lines. Ask for the lens and sensor to confirm.
- **Distortion likely** → undistort for line-up, redistort the CG (Lens Distortion Matcher; fallback Optics Compensation or STMapper with an ST map), render 5–10% overscan. If `note` says one line carries it, confirm on a second edge first.
- **Clipped region** → never use it as the energy reference. Use the brightest **unclipped emitter** from the candidates (not a specular). Glow and halo above the clip need care under Strategy A (06 soft rolloff).
- **GLOSSY** → reflection catcher on the floor proxy is mandatory. Start GGX roughness ~0.1–0.25 [rule], tune until the CG streak aspect matches the measured one.
- **Dark glass panels** → separate low-roughness reflection proxies, ~4% at normal incidence (Fresnel of glass).
- **Moving subject near the CG** → holdout (Object Matte → Mocha Pro fixes; fallback Roto Brush), person proxy in C4D for shadows and reflections, reverse light wrap.
- **IoU high (subject never leaves its area)** → no clean plate from the plate itself. Plan around it: CG stays in front, or paint a clean plate.
- **Haze** → depth fog on the CG matched to the measured lift. Optional Redshift volume for glow in air.
- **Grain** → degrain (Neat Video; fallback Magic Bullet Denoiser III) → per-channel regrain to the measured σ per band (Magic Bullet Renoiser; fallback Add Grain). Blue usually needs the most.
- **Bloom on clipped practicals** → match glow radius to the measured r50/r10 at equal brightness. No bloom → restrain the glow.
- **CA > 0.5 px** → radial CA on the CG and glow only. None → add none.
- **No ghosts** → no flares.
- **Far soft** → match the CG's defocus to plate objects at the same depth. Defocused emitter → render DOF in Redshift.
- **Shutter indeterminate** → 180° (Redshift shutter 0.5 frame) until the camera report says otherwise. Rotating CG → transformation steps ≥ 3.
- **Exposure change or local light change** → the CG's light and the plate's light must change together: animate the CG exposure to the measured curve, or key the interactive-light pass to the changing region. Static CG on a changing plate is a tell.
- **Flicker** → match it on the CG (expression from the measured per-frame factor), or deflicker the plate first.
- **Black floor below legal** → CG blacks may reach the plate's floor, not deeper.
- **Cool cast / low saturation** → desaturate halos toward the plate palette; let cores roll to white.

## 4. Known limits
- Energy candidates include speculars. Read the overlay.
- Unpaired floor streaks can be carpet weave, rails or door edges. Only paired streaks prove gloss.
- Distortion needs long straight edges near the frame edge. On dark plates it often finds none and says so (`not detected` ≠ no distortion).
- Shutter is rarely measurable on slow walk-aways. Treat 180° as the default, not a measurement.
- Temporal grain is invalid on 8-bit H.264 when noise is below 1 code. Use the spatial figure and the eye.
- The subject box includes the floor reflection and can include median-background ghost on slow, self-overlapping movers.
- Haze from one surface can be confused with that surface's lighting gradient.
- Scene-linear EXR plates are out of scope for the energy numbers.

## 5. Report format
Emit these sections in order. Each line of the shot read carries its measured value and a trust word (measured / estimated / assumed).
1. **Shot read**: format and range, camera, perspective and focal, lens, light references (ceiling, emitter), black floor, palette, surfaces (gloss, glass), haze, grain, subject, shutter, DOF, CA, bloom, flicker and light changes.
2. **Risks and tells** for this plate (from 08), ranked.
3. **Pipeline**: OCIO strategy, config and view names, bit depth, EXR specs.
4. **C4D/Redshift**: camera, proxies, light groups, Takes, AOVs, render settings with values.
5. **AE stack**: layer order, one tool per step with its starting settings and a fallback (native or Red Giant).
6. **QC checklist** tailored to the shot.
7. **Questions for production and open items**: camera report, lens, sensor, shutter, range of the export, anything the script could not measure.
