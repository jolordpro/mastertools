# 12: Placing graphics in moving footage

Research snapshot: **2026-10-27**. Scope: tracking, pinning and blurring a logo, sign, screen insert or type so it sticks to a surface in the plate. AE first.

Already covered elsewhere, not repeated here:
- Lock-off check, 3D solve tools, undistort/redistort, STMaps (02).
- Affine and corner-pin math.
- Measured shutter and drift thresholds from `analyze_plate.py` (10).
- Making the graphic match the light, softness and grain (11).
- Things passing in front of the graphic (13).

## 1. Pick the tracker by shot
Rank by what the surface does, not by habit.

| Shot | Tracker, in order |
|---|---|
| Locked (drift < 0.25 px, file 10) | None. Place it by hand |
| A flat surface moves, no parallax across it | 1. **Mocha AE** planar track, Perspective on. 2. AE point tracker, **Perspective Corner Pin** (4 points) |
| A flat surface with four clean corners (a screen, a sign) | 1. Mocha AE. 2. Point tracker on the corners, if they stay visible all shot |
| Several surfaces, or the graphic must sit in 3D depth | 1. **AE 3D Camera Tracker**, attach to a plane of solved points. 2. Mocha Pro or SynthEyes solve (02) |
| A bending surface (shirt, flag, skin) | Mocha Pro **PowerMesh**. Not in Mocha AE |
| Shaky handheld, graphic is a fix or paint | Stabilize, place, unstabilize (§4) |

Facts behind the table [checked 2026-10-27]:
- AE ships **Mocha AE** from Boris FX. It is GPU-accelerated and supports Multi-Frame Rendering. Adobe recommends it for "shots with motion blur or objects that move off-screen." Apply it from Effect > Boris FX Mocha > Mocha AE ([Adobe, tracking](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/track-motion/tracking-stabilizing-motion-cs5.html)).
- The point tracker uses 1 point for position, 2 for scale and rotation, 4 for a corner pin. **Parallel Corner Pin** (3 points) keeps lines parallel and has no perspective. **Perspective Corner Pin** (4 points) adds perspective. All four feature regions must lie on one real plane (same page).
- Mocha Pro alone has the Lens, Insert, Remove, Stabilize and Reorient modules, plus PowerMesh ([Boris FX support](https://support.borisfx.com/hc/en-us/articles/10006962512909-What-is-Mocha-General-Mocha-Pro-and-Mocha-AE-information)). Whether Mocha AE has the 3D camera solver was not confirmed. [verify]
- Mocha AE shows only the planar tracking parameters; Mocha Pro shows more ([Mocha 2026.5 guide](https://borisfx.com/documentation/mocha/)).

## 2. When each tracker fails, and the fix

### AE point tracker
Source: [Adobe, tracking](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/track-motion/tracking-stabilizing-motion-cs5.html) [checked 2026-10-27].

| Fails when | Fix |
|---|---|
| The feature changes shape, light or angle over the shot | **Adapt Feature On Every Frame**, or "If Confidence Is Below → Adapt Feature". Track in sections |
| The feature leaves frame or is covered | Pick a different feature on the same plane and move the **Attach Point** offset. Or "Extrapolate Motion" for short gaps |
| Grain or noise | **Enhance Before Match**, blur 2–3 px. Tracking only; the plate isn't changed |
| The feature differs by color, not brightness | Channel: RGB (distinct color), Luminance (brightness), Saturation (strong color among similar hues) |
| Fast moves | Larger search region, offset toward the direction of travel |

- Set the confidence threshold from the data: track once, read the Confidence values on bad frames, then set the threshold slightly above the worst of them.

### Mocha (AE and Pro)
Source: [Mocha 2026.5 user guide](https://borisfx.com/documentation/mocha/) [checked 2026-10-27]. Mocha tracks texture inside a spline, not points.

| Fails when | Fix |
|---|---|
| "Large or continuous obstructions, extreme blur, low contrast details and sudden flashes" | Track what holds, then fix by hand with AdjustTrack. Don't tweak forever |
| Something enters the shape (an elbow, a bird, hair) | Draw an exclusion shape in the same layer, or a layer above. Layers above subtract from the tracking matte |
| Screens or reflective surfaces change inside the shape | Exclude the screen face; track the bezel or frame |
| Drift or slip | Raise **Min % Pixels Used**. Slower, but "usually a much more solid track" |
| Heavy noise | **Smoothing Level** blurs the clip before tracking (default 0) |
| Fast moves | Turn off the Auto search area and enter a larger value; give angle and zoom estimates |
| Motion blur | Raise Min % Pixels Used first, then fix drift in AdjustTrack |
| "Couldn't decompose motion matrix" | The plane went behind the camera in extreme perspective. Start tracking from the middle of the move |
| Wrong motion model | **Shear** for slight turning (a torso walking toward camera). **Perspective** for strong turns away (a truck front rounding a corner). Lower order (translation, rotation, scale) when the plane barely distorts |

- Not perfectly flat surfaces often track fine when parallax is low: distant backgrounds, faces around the eyes and nose, torsos, car bodies. "When in doubt, try quickly tracking an area."

### AE 3D Camera Tracker
Source: [Adobe, 3D camera movement](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/3d-camera-tracker-effect/tracking-3d-camera-movement.html) (updated Jan 19 2026) [checked 2026-10-27].

| Fails when | Fix |
|---|---|
| Moving objects (people, cars) pull the solve | Delete their points; **Auto-delete Points Across Time** removes them on every frame. Or give the layer an alpha that hides them |
| No parallax (pan on a tripod) | **Solve Method: Tripod Pan** |
| The scene is one flat plane | **Solve Method: Mostly Flat Scene** |
| Too few points | **Detailed Analysis** (slower, much larger data) |
| Zoom during the shot | **Shot Type: Variable Zoom**, or Specify Angle of View when the lens is known |

- Judge the solve by **Average Error** (px between 2D points and reprojected 3D points). Lower is better; compare changes against it.
- Set **Ground Plane and Origin** from selected points before creating content.
- Export to C4D: File > Export > Maxon Cinema 4D Exporter.

## 3. Rolling shutter
- CMOS sensors read one line at a time, so fast pans and vibration skew and wobble the frame ([Adobe](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/rolling-shutter-repair.html)).
- **AE Rolling Shutter Repair** [doc]: Rolling Shutter Rate is scan time as a percentage of the frame. "DSLRs seem to be in the 50-70% range, and iPhone is close to 100%." Adjust until skewed verticals stand straight. Methods: Warp (point tracking) or Pixel Motion (optical flow). Warp Stabilizer also has Rolling Shutter Ripple (Automatic or Enhanced Reduction), but only with Subspace Warp or Perspective.
- **Solves:** SynthEyes says rolling shutter "causes pervasive distortions on images and the resulting solves." It removes the effect from tracker data before solving, so the solve is an ideal camera. Inserts rendered from that camera "will not match the original imagery" where the plate wobbles ([SynthEyes guide](https://borisfx.com/documentation/syntheyes/SynthEyesUM_files/effects_of_rolling_shutter)).
- Whether Redshift's camera can render rolling shutter was not checked. [verify]

**Rules for graphics** [rule]:
1. A flat insert on a skewing plate: use a **Perspective** corner pin from Mocha. A skewed plane is still a four-sided shape each frame, so the pin follows most of the skew. Check the edges at 200% during the fastest move.
2. A 3D solve: solve on a repaired copy of the plate. Keep the delivered plate untouched (non-negotiable 2 in README). Expect the insert to drift by the residual wobble.
3. When the wobble is large, ask production whether the delivered plate may be the repaired one. That's their call, not a silent fix.

## 4. Stabilize, place, unstabilize
Use it when the graphic or fix is easier to build on a still frame: paint, cleanup, a hand-animated element.

| Tool | How |
|---|---|
| **Warp Stabilizer VFX** (native) | Two instances. The first with Objective **Reversible Stabilization**, the second with **Reverse Stabilization**. Work goes between them. Or **Apply Motion to Target** to move another layer with the shake |
| Mocha Pro Stabilize module | Track the area; stabilize translation, rotation, zoom, and even shear and perspective to flatten a plane, then restore. Pro only |
| AE point tracker | Stabilize Motion on a precomp, place the work, then apply the inverse with a null [rule] |

Facts [checked 2026-10-27, [Adobe](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/track-motion/tracking-stabilizing-motion-cs5.html)]:
- Warp Stabilizer's analysis ignores masks and effects on the same layer. Precompose them first.
- Methods fall back when tracking is thin: Subspace Warp → Perspective → Position, Scale, Rotation → Position. Subspace Warp can warp parts of the frame; Perspective can keystone. Pick a simpler method when that shows.
- Mocha's guide: track a static area with translation, scale and rotation only. Don't track a moving object for stabilization.

**Rule: never resample the plate twice** [rule]. Stabilize and unstabilize both resample. Keep the original plate at the bottom, untouched. Composite only the new pixels (the patch or graphic) from the round trip, through a matte.

## 5. Motion blur on tracked graphics
A sharp graphic on a blurred plate is the first tell in fast shots.

**Settings** [doc]:
- Comp **Shutter Angle**: match the plate. Use the camera report, or `analyze_plate.py`'s shutter (10). Default 180° when unmeasurable.
- **Shutter Phase = −½ × Shutter Angle** (−90° for 180°). Adobe: otherwise "the attached object may appear to lead or lag" ([Adobe, tracking](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/track-motion/tracking-stabilizing-motion-cs5.html)).
- Samples Per Frame is the minimum (3D and shape layers); Adaptive Sample Limit the maximum. Low limits echo on fast moves ([ProVideo Coalition](https://www.provideocoalition.com/?p=4194)). Current Adobe page not found. [verify]

**Which pin gets blur:**

| Setup | Blur |
|---|---|
| Corner Pin effect alone | Layer motion blur reads transform properties, so a pin animated only by its corners gets no blur. Reported by users for years ([Creative COW](https://creativecow.net/?p=23573)). [verify in 26.x] |
| Mocha export **"Corner Pin (Support Motion Blur)"** | Splits the track into position, scale and rotation plus a residual pin, so layer motion blur works ([Mocha guide](https://borisfx.com/documentation/mocha/)). A June 2025 user report describes jitter with this export on a null ([Adobe Community](https://community.adobe.com/questions-529/ae-tracker-mocha-tracking-is-jittery-when-applied-to-elements-60080), via search summary) [verify]. Compare it against the plain pin |
| 3D layer + solved camera | Real 3D motion blur from the camera move. Best for 3D Camera Tracker inserts |
| **Pixel Motion Blur** (native) | Optical-flow blur from the layer's own content, with its own Shutter Angle and Samples ([Adobe, time effects](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/time-effects.html)). Use on a precomp of the pinned graphic. Bit depth not listed. [verify] |
| CC Force Motion Blur on a precomp | Samples time; old reports call it slow and 8-bit ([Creative COW](https://creativecow.net/?p=1843182)). [verify] |
| Transform effect | Own shutter angle per layer, but 8/16 bpc only ([Adobe, distort](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/distort-effects.html)) |

- Corner Pin and Optics Compensation work in 32 bpc; CC Power Pin's bit depth wasn't checked [verify].
- **Check** [rule]: step to the fastest frame. The graphic's blur length and direction match a plate edge moving the same way. Compare with Difference at 200%.

## 6. Type and graphics in perspective
**Build** [rule unless tagged]:
- Design the graphic flat, in a precomp sized to the **largest size it reaches on screen**, then pin it. A pin resamples a precomp, so a small precomp goes soft when the pin enlarges it.
- Build the flat precomp at 2× when the graphic gets close to camera, then pin down.
- Text and shape layers are always continuously rasterized ([Adobe, precomposing](https://helpx.adobe.com/after-effects/desktop/work-with-compositions/precomposing-and-nesting/precomposing-nesting-pre-rendering.html)) [doc]. A 3D text layer under the solved camera stays sharp at any distance. Prefer it for 3D Camera Tracker inserts.
- Set tracking and kerning in the flat space. The pin keeps letter order and spacing ratios; never kern by eye in the perspective view.

**Legibility at an angle:**
- Foreshortening shrinks the depth axis. Road markings fight this by stretching letters along the line of sight. US practice is about **2.5:1** ([UW TOPS Lab](https://topslab.wisc.edu/research/tse/elongated-pavement-markings)); the MUTCD bases word markings on its standard alphabets "in elongated form" ([FHWA](https://mutcd.fhwa.dot.gov/resources/interim_approval/ia5rptcongress/ch2.htm)). A classic study found returns shrink as elongation grows ([TRID](https://trid.trb.org/View/139267)). These three were read from search summaries, not the full pages. [verify]
- Use elongation only when the graphic must read **from this camera**. A logo meant to look painted on the real surface keeps its true proportions.
- Keep the thinnest stroke at least ~2 px on screen at the far end, or it shimmers and aliases [rule]. Open tracking slightly for steep angles [rule].
- Then match softness and grain to the plate at that depth (11 §8). A graphic sharper than the surface it's printed on reads as a sticker.

## 7. QC for a placed graphic [rule]
- **Stick test.** At 200%, watch each corner over the full shot. Any slide against the surface texture is a fail.
- **Fastest frame.** Blur length and direction match the plate.
- **Wobble.** On rolling-shutter plates, check the edges during the fastest pan.
- **Edges and type.** No shimmer on thin strokes; no softness jump when the graphic scales.
- **Then** occlusion (13) and match (11).

## Open
- [verify] Mocha AE camera solver, Pixel Motion Blur and CC Force Motion Blur bit depth, CC Power Pin bit depth, whether Corner Pin still gets no layer blur in AE 26.x, Redshift rolling shutter.
- Test: a 10-frame fast pan with a pinned logo, comparing plain pin, "Support Motion Blur" pin and Pixel Motion Blur. Pass = blur length within 10% of a plate edge [rule].
