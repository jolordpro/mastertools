# 14: After Effects compositing toolbox

Research snapshot: **2026-10-27**, from Adobe's effect and workflow pages unless tagged. Scope: native AE tools for mattes, blending, precomps, shadow catchers, displacement, cleanup and plate-driven expressions.

Already covered elsewhere, not repeated here:
- Bit depth of color, blur, grain, generate and LUT effects (11 §4).
- Track matte scripting traps, `setTrackMatte()`, bit-depth defaults for scripts (ae-extendscript skill, `api-gotchas.md`).
- Light wrap and Supercomp tools (04, 11).
- Keying in depth (green screen, areas 6–7, not researched yet). The keyer bit-depth table is in 13.

## 1. Mattes and alpha
Bit depth per effect [checked 2026-10-27]: [channel](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/channel-effects.html), [matte](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/matte-effects.html), [keying](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/work-with-keying-effects/keying-effects.html) pages.

| Tool | Bit depth · what it's for |
|---|---|
| **Track Matte** (layer menu) | n/a · Any layer in the stack can be the source, and many layers can share one. Alpha, Luma, and an Inverted toggle for each |
| **Set Matte** | 8, 16, 32 (since CS6) · Legacy, but useful: the matte layer can sit anywhere; **Composite Matte With Original** intersects the new matte with the current alpha |
| **Preserve Underlying Transparency** (T switch) | n/a · The layer shows only over opaque pixels below it. AE's version of a Photoshop clipping mask |
| **Stencil / Silhouette** (Alpha or Luma) blend modes | n/a · Cut through or punch a hole in **all** layers below. Precompose to limit their reach |
| **Alpha Add** blend mode | n/a · Fixes seams where two anti-aliased edges meet. Normal over gives 50% + 50% = 75% opaque; Alpha Add gives 100% |
| **Luminescent Premul** blend mode | n/a · Keeps over-range color from premultiplied light elements (flares). Interpret the source as Straight first |
| **Simple Choker** | 8, 16, 32 · Small choke or spread. Negative spreads, positive chokes |
| **Matte Choker** | 8, 16 only · Spread then choke, repeated (Iterations) to close holes. Gray Level Softness 100% = a pure alpha blur |
| **Minimax** | 8, 16, 32 · Min/Max per channel by radius. Radius 1 Minimum shrinks a matte 1 px |
| **Refine Soft Matte** | not listed [verify] · After a key: Calculate Edge Details (hair, blur), Chatter Reduction, More Motion Blur, Decontaminate Edge Colors |
| Refine Hard Matte | not checked [verify] |
| **Channel Combiner** | 32 · From Min RGB / Max RGB / Lightness to **Alpha Only**; quick mattes from a channel |
| **Shift Channels**, **Set Channels** | 8, 16, 32 · Route any channel (or another layer's) into alpha |
| Calculations | 8, 16 only · Photoshop-style channel math between layers |
| **Remove Color Matting** | 8, 16, 32 · Unpremultiplies a matted edge against a background color. Turn off Clip HDR Values in 32 bpc. Formerly "Unmultiply"; not the same as Unmult |
| **Unmult** (26.0) | 8, 16, 32 · Builds alpha from black or white. For stock elements on black (05) |
| **Invert** (Alpha) | 8, 16, 32 · Flip a matte |

Notes [doc]:
- Matte Choker and Calculations drop a layer to 16 bpc. Fine inside a matte precomp, since a matte is 0–1 data [rule].
- Track mattes and Preserve Underlying Transparency are siblings: one takes transparency from a chosen layer, the other from everything below ([Adobe, track mattes](https://helpx.adobe.com/after-effects/desktop/work-with-transparency-and-compositing/work-with-track-mattes-and-traveling-mattes/track-mattes-and-traveling-mattes.html)).
  - That page's intro says "pixels with higher values are more transparent," which contradicts its own toggle list ("Opaque when … 100%"). Trust the toggles.
- To move a matte with its layer, parent the matte to it (same page).
- Mask Feather is a Gaussian falloff, not linear, and only works inside the layer's bounds. Keep feathered masks away from the layer edge ([Adobe, masks](https://helpx.adobe.com/after-effects/desktop/work-with-transparency-and-compositing/work-with-alpha-channels-and-masks/alpha-channels-masks-mattes.html)).

## 2. Blend modes in a 32-bpc linear project
Adobe [doc] ([blending modes](https://helpx.adobe.com/after-effects/desktop/work-with-layers/work-with-layer-blending-modes/blending-modes-layer-styles.html), [color basics](https://helpx.adobe.com/after-effects/desktop/adjust-colors/color-basics/color-basics.html)) [checked 2026-10-27]:
- Glows, blurs and "some blending modes" behave differently in 32 bpc than in 8 or 16 bpc. Adobe doesn't list which modes.
- **Multiply** divides by the project's max value. **Subtract** can go below 0 and **Divide** above 1.0 in 32 bpc.
- Blend modes can't be keyframed. Split the layer, or use Compound Arithmetic (8 bpc only).
- **Advanced Blending** (inside Layer Styles > Blending Options) turns R, G or B off for blending, and can be animated.
- In a project without OCIO, **Blend Colors Using 1.0 Gamma** gives linear blending.
- AE blends 8 modes in 32 bpc on the GPU when the layer has motion blur: Screen, Multiply, Add, Overlay, Hard Light, Classic Difference, Lighten, Darken.

**Why Screen fails above 1.0** [rule, worked from Adobe's formula]:
- Screen = 1 − (1 − A)(1 − B). It assumes both inputs are 0–1.
- A = 2.0, B = 0.5 → 1.5. Add gives 2.5. The light lost a stop.
- A = 2.0, B = 2.0 → 0.0. Two bright lights screen to **black**.
- Nuke avoids this: its screen uses the formula only when both inputs are 0–1, "otherwise max(A,B)" ([Foundry Merge](https://learn.foundry.com/nuke/content/reference_guide/merge_nodes/merge.html)). What AE does above 1.0 wasn't confirmed. [verify by test]

**Which mode for which job** [rule]:

| Job | Mode in 32-bpc linear |
|---|---|
| Light, glow, flare, interactive spill | **Add** (04) |
| Shadow, dirt, a printed or dyed graphic on a surface | **Multiply** |
| Overlay, Soft Light, Hard Light, Linear Light, Vivid Light | Pivot on 50% gray, defined for 0–1. Use only on display-range layers (a gradient, a texture), or inside a precomp converted to display space |
| Classic Color Dodge, Classic Color Burn, Classic Difference | Legacy (AE 5.0 behavior). Use only to match old projects |
| Hue, Saturation, Color, Luminosity | Use with care on over-range values [verify by test] |
| Difference | Alignment and QC: matched pixels go black |

## 3. Precomps, adjustment layers and render order
From [Adobe, precomposing](https://helpx.adobe.com/after-effects/desktop/work-with-compositions/precomposing-and-nesting/precomposing-nesting-pre-rendering.html) [checked 2026-10-27]:
- **Render order per layer:** masks → effects → transforms → layer styles. Use the Transform effect to transform earlier in the effect stack.
- Some effects ignore masks on their own layer. Precompose the masked layer, then apply the effect.
- **Collapse Transformations:** the nested comp's transforms combine with the parent's, so scaling down then up loses nothing.
  - 3D layers in a **non**-collapsed precomp render flat through the default camera. They can't intersect, cast or receive shadows, or follow the parent's camera and lights.
  - Collapsed, they do all of that.
  - An **adjustment layer inside** a collapsed precomp forces it to flatten and crop.
  - A mask, layer style or effect **on** a collapsed precomp renders its layers first. Their blend modes then stop reaching layers in the parent, and 3D layers above and below can't interact.
- **No clipping masks in AE.** Clip an adjustment by: a mask on the adjustment layer; a track matte on it; or putting it in a precomp with only the layers it should touch.
- Layer styles block 3D interaction: a layer with a style can't intersect or trade shadows with other 3D layers ([Adobe, blending modes](https://helpx.adobe.com/after-effects/desktop/work-with-layers/work-with-layer-blending-modes/blending-modes-layer-styles.html)).

## 4. Shadow catchers in AE 3D
From [Adobe, shadow catchers](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/cast-and-accept-shadows/shadow-catchers.html) and [3D Camera Tracker](https://helpx.adobe.com/after-effects/desktop/work-with-3d-composition/3d-camera-tracker-effect/tracking-3d-camera-movement.html) [checked 2026-10-27]:
1. A 3D solid aligned to the floor or wall, under the object.
2. Material Options > **Accepts Shadows: Only**. The layer turns invisible and keeps only shadows.
3. The caster needs **Casts Shadows** on, and a light that casts shadows.
4. **Shadow Color** (default black) tints the shadow. Set it from the plate's own shadows, never black (11 §7).
5. The 3D Camera Tracker's **Create Shadow Catcher** makes one in place, and adds a light if none exists.
- Shadow catchers and Shadow Color work with the **Advanced 3D** renderer ([Adobe Community, beta notes](https://community.adobe.com/t5/after-effects-beta-discussions/new-in-beta-shadow-catchers-and-shadow-colors/m-p/14552288); seen in search results). [verify]
- For hero shadows, render a shadow pass from Redshift instead (03). The AE catcher is for quick or 2.5D work.

## 5. Displacement and surface
From [Adobe, distort effects](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/distort-effects.html) [checked 2026-10-27]:

| Effect | Bit depth · note |
|---|---|
| **Displacement Map** | 8, 16, 32 · Reads the map layer's source **without its effects or masks**. Precompose the map first. Mid-gray (128 of 255) = no shift; 0 and 255 = full shift each way |
| **Turbulent Displace** | 8, 16, 32 · Fractal warp: heat haze, water, flags. Cycle Evolution makes a loop |
| Optics Compensation | 8, 16, 32 · Lens distortion add or remove (02) |
| Corner Pin | 8, 16, 32 · See 12 for motion blur |
| Bezier Warp, Mesh Warp, Bulge, Liquify, Ripple, Wave Warp, Warp, Mirror, Offset, Spherize | 8, 16 only |
| Transform | 8, 16 only · Own shutter angle |
| CC Glass, Bevel Alpha, CC Power Pin | not checked [verify] |

- For a graphic that follows a textured wall: Displacement Map driven by the wall's most contrasty channel (11 §7).
- A displacement map is data. In a 32-bpc linear project, check that mid-gray in the map is 0.5 in the working space, or the graphic shifts everywhere [rule, verify by test].

## 6. Cleanup: Content-Aware Fill
From [Adobe, Content-Aware Fill](https://helpx.adobe.com/after-effects/desktop/remove-objects-from-your-videos/content-aware-fill.html) [checked 2026-10-27]:
- Make a hole with any method (a Subtract mask, Roto Brush, a key), then Window > Content-Aware Fill > **Generate Fill Layer**.
- **Fill Method:**
  - **Object**: a moving object; uses motion behind it.
  - **Surface**: a static, flat surface (a sign on a wall).
  - **Edge Blend**: textureless areas; fastest.
- **Lighting Correction** (Subtle, Moderate, Strong) for shots whose light changes. Start Strong, step down if it flickers. Not needed for Edge Blend.
- **Reference Frame:** paints one frame in Photoshop (clone, patch) and the fill copies from it. Add more at lighting or angle changes. Save in place, not Save As.
- **Output Depth** follows the project. 32 bpc writes EXR sequences; 8/16 writes PNG.
- **Alpha Expansion** grows the hole; a loose mask often fills better than a tight one.
- A feathered mask blends the fill by its alpha.
- Remove an object and its shadow in separate passes.
- Uses a lot of disk. Water and mixed light and texture are weak spots.

## 7. Expressions that read the plate
**`sampleImage()`** [doc] ([docsforadobe](https://ae-expressions.docsforadobe.dev/layer/general/)) [checked 2026-10-27]:
- `layer.sampleImage(point, radius=[0.5,0.5], postEffect=true, t=time)` returns `[r, g, b, a]`, the alpha-weighted average inside the radius.
- `point` is in **that layer's space**; `[0,0]` is the center of the top-left pixel. Convert with `fromComp()` when layers aren't comp-sized.
- `postEffect=true` reads after the layer's own masks and effects. Adjustment layers above are never included.
- It "no longer disables multiprocessing."
- From probes: it reads OCIO float values exactly, including over 1.0. Run from a script with no render, it returns zeros.

**Recipe: follow a light change on the plate** [rule]
Put it on an **Exposure** effect's Exposure value on the graphic. It moves the graphic by the same number of stops as the plate patch under it.
```
// Exposure (stops) that tracks the plate's brightness at the graphic
var plate = thisComp.layer("PLATE");                     // the plate layer
var c = thisComp.layer("TRACK_NULL").toComp([0,0,0]);    // tracked spot
var p = plate.fromComp(c);
var r = [12, 12];                                        // big enough to average out grain
function Y(t){ var s = plate.sampleImage(p, r, true, t);
  return 0.2126*s[0] + 0.7152*s[1] + 0.0722*s[2]; }      // Rec.709 luma weights, linear
var ref = Y(thisLayer.inPoint);                          // the frame the look was set on
value + Math.log(Math.max(Y(time),1e-6) / Math.max(ref,1e-6)) / Math.LN2;  // keeps the hand-set offset
```
- The luma weights are Rec.709's, correct only in linear. Under Strategy A (display-linear, 01) the plate is linear in the working space, so they apply.
- Sample a **flat patch** next to the graphic, not under it, so the graphic itself never feeds back [rule].
- If grain flickers the result, average three times (`time - thisComp.frameDuration`, `time`, `+`) or bake the curve to keyframes, then smooth [rule].
- Same pattern drives a tint (per-channel ratios) or a shadow layer's opacity.

## Open
- [verify by test] AE Screen and HSL modes above 1.0; a 32-bpc displacement map's neutral value.
- [verify] Refine Soft/Hard Matte, CC Glass, Bevel Alpha, CC Power Pin bit depths; shadow catcher renderer limits.
