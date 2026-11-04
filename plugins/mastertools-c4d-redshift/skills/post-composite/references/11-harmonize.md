# 11: Harmonize: make an existing layer belong in a shot

Research snapshot: **2026-10-27**. Scope: a logo, graphic, 3D render, photo cutout or video element placed over a plate or photo, finished in After Effects (first) or Photoshop. Pairs with 04 (layer order, light wrap), 06 (defocus, grain), 07 (haze, reflections) and 09 (tool status).

Status: built as `scripts/harmonize.py` v1 (2026-10-27). Tested on C4D/Redshift ground truth, a synthetic self-test and the Jack plate (§10, §11).

**v1 scope (locked 2026-10-27):** the top 7 in `HARMONIZE-IDEAS.md` §7.
1. Ask what the layer is in the world.
2. Work in the §7/§8 priority order.
3. Squint board with every preview.
4. Softness, grain by brightness and compression, from existing measures.
5. Local black floor with glare, and shadow density from the plate's shadows.
6. Texture transfer for painted or printed layers.
7. Illuminant shift by Bradford adaptation, baked into the LUT.

Out of v1: automatic scorers, Depth Generator, gloss reflections.

## 1. The core rule: match the light, not the content
**Upgraded by §8:** match shadows, mids and highlights as three zones, with measured human tolerances.

- **Pro method** [doc]: define the target's black point, white point and neutral first, then map the foreground's tonal range onto them.
  - Nuke's Grade node does this with four controls. **blackpoint**/**whitepoint** are sampled on the layer being changed. **lift**/**gain** are sampled on the image it must match. Gamma follows for the mids. Foundry says the node is used "for matching foreground plates to background plates." ([Foundry Grade](https://learn.foundry.com/nuke/content/reference_guide/color_nodes/grade.html))
  - Steve Wright's *Digital Compositing for Film and Video* covers black and white point matching, grayscale balancing, midtone matching and the "Constant Green" method under "Matching the Light Space" ([Routledge, 5th ed. 2024](https://www.routledge.com/Digital-Compositing-for-Film-and-Video-Production-Workflows-and-Techniques/Wright/p/book/9781032417998)). Only the section titles were checked; the book's text was not read. [verify]
  - Two more rules: contrast before color, since the eye is "much more sensitive to subtleties of contrast than of color." And judge one channel at a time. ([Frame.io](https://blog.frame.io/2016/08/25/first-essential-vfx-compositing-matching/))
- **Why not match histograms or averages.** Statistics-based matchers assume both images hold similar colors in similar amounts. Nuke's MatchGrade, for example, needs "the same proportion of colored pixels" in source and target ([Lynda](https://origin-www.lynda.com/Nuke-tutorials/MatchGrade-node-Matching-two-clips/5005078/5024125-4.html), [Foundry MatchGrade](https://learn.foundry.com/NUKE/CONTENT/reference_guide/color_nodes/matchgrade.html)). A red logo on a gray wall breaks that assumption, so a stats match drags the logo toward gray and flattens it.
  - A still-comp grade (mean + covariance) is right for a **render vs a reference of the same scene**. It is not right for different content.
- **What to map** [rule]:
  - The layer's darkest *intended* black goes to the plate's black at that spot. Use the black floor from `analyze_plate.py`, read locally, never deeper than the plate's floor.
    - The plate's black means a **black object's** level (glare plus the camera's floor). It is never the dimmest patch of a lit wall. With no black object near the spot, use zero glare. Measured 2026-10-27, §10.
  - The layer's brightest *intended* white goes to what a white surface at that spot would read. Use the brightest unclipped diffuse surface near the spot, not a practical light or a clipped area.
  - The layer's neutrals go to the plate's gray balance at that depth. Take it from neutral surfaces near the spot (walls, concrete, paper). Without one, use the median chroma of low-saturation pixels, flagged lower confidence.
  - The layer's own hues are kept. Only the tone curve's ends and the neutral axis move.
- **"Constant green" in practice** [rule]: set overall brightness on luma first. Then move only red and blue lift and gain to remove the cast, so brightness barely shifts while color is fixed.

## 2. Reading the light from one frame: what's reliable
- Estimating light from a single image is "highly ill-posed" ([Eurographics 2013](https://diglib.eg.org/handle/10.1111/v32i8pp170-182)). The open problem is still the full HDR environment from casual footage ([summary](https://www.emergentmind.com/open-problems/inferring-hdr-environment-lighting-from-casual-images-or-video)).
- **Measure with confidence** only from a flat, plain surface near the spot (a wall, floor or panel). Its brightness slope gives the light's direction across the frame and its falloff gives the softness. A shadow edge, if visible, gives softness directly.
- **Low confidence** on busy textures, multiple light sources, or when the slope is under the grain level. Then ask the user one question (left, right, above, behind camera, frontal), and say the answer was supplied, not measured.
- **Research-grade methods** (for context, none used in v1):
  - Intrinsic Harmonization (SIGGRAPH Asia 2023) splits albedo from shading and fits a simple light model to the background ([arXiv](https://arxiv.org/html/2312.03698v2)). Its authors note that most learned harmonizers only reverse global color edits and miss real lighting mismatches.
  - Relightful Harmonization (CVPR 2024, Adobe/NYU) relights portraits with a diffusion model and environment-map priors ([CVPR](https://openaccess.thecvf.com/content/CVPR2024/papers/Ren_Relightful_Harmonization_Lighting-aware_Portrait_Background_Replacement_CVPR_2024_paper.pdf)).
  - IC-Light (background-conditioned relighting) is the common open baseline ([GitHub](https://github.com/lllyasviel/IC-Light)). 2025 tests found it lacked convincing backlight and was unstable from frame to frame on video ([AnyPortal](https://arxiv.org/pdf/2509.07472)), and that it struggles with complex light transport ([HumanOLAT](https://arxiv.org/pdf/2508.09137)). Its default background remover is non-commercial only.
  - **Rule for motion work** [rule]: AI relighters are look-finding tools for one frame. Rebuild their result as measured, keyframable values before using it across a shot.
- **libcom** (BCMI Lab) bundles open harmonization, shadow generation and composite-quality scoring ([PyPI](https://pypi.org/project/libcom/0.0.2), [survey](https://arxiv.org/html/2106.14490v8)). Its Mac support, license and speed are unchecked. [verify]

## 3. The paths to rank (per layer type)
Rank by realism for this shot, then cost. Always name what would move a path up.

| Layer | Paths, usual rank |
|---|---|
| Flat logo / graphic on a surface | 1. AE stack (below). 2. Rebuild in C4D when light must wrap depth or reflect (03). 3. Photoshop Harmonize on one frame as a look target |
| 3D render (C4D/Redshift) | 1. Re-render with the plate's light: light groups, shadow catcher (03, 04). 2. AE stack on the beauty |
| Photo cutout | 1. Neutralize its own light first, then the AE stack. 2. Scene Light to relight it in AE. 3. Photoshop Harmonize for stills |
| Video element (second plate) | 1. AE stack plus matching its grain, blur and camera move (02, 06). 2. Rebuild or reshoot when the lights point different ways |

- **Different light directions can't be graded away.** A match works "as long as their source lighting doesn't go in different directions" ([Frame.io](https://blog.frame.io/2016/08/25/first-essential-vfx-compositing-matching/)). When the layer's baked light opposes the plate's, say so and rank relight, rebuild or a new source above any grade.

## 4. The polish stack: tools by step, with bit depth
**Workflow note.** In a **32-bpc linear** project, do the tone steps with **Exposure** and per-channel gain and offset, not Levels or Curves gamma (04: "Avoid Curves/Levels on linear data"). Levels and Curves fit display-referred projects and Photoshop.

AE bit depth was read from Adobe's effect pages on 2026-10-27 [checked 2026-10-27]:

| Effect (AE native) | Bit depth |
|---|---|
| Levels, Levels (Individual Controls), Curves, Exposure, Hue/Saturation, Lumetri Color, Tint, Tritone, Brightness & Contrast | 8, 16, 32 |
| Color Balance, Channel Mixer, Selective Color, Shadow/Highlight, Vibrance, Change to Color | 8, 16 only |
| Gradient Ramp, Fill, Drop Shadow | 32 |
| 4-Color Gradient | 8, 16 only |
| Camera Lens Blur, Gaussian Blur, Directional Blur, Compound Blur, Bilateral Blur, Box Blur | 8, 16, 32 |
| **Add Grain, Match Grain, Remove Grain** | **8, 16 only** |
| Noise, Fractal Noise, Turbulent Noise | 8, 16, 32 |
| Apply Color LUT (.cube, .3dl, .look, .csp; up to 64 points per axis) | 8, 16, 32 |

Sources: Adobe's [color correction](https://helpx.adobe.com/after-effects/desktop/adjust-colors/work-with-color-correction-effects/color-correction-effects.html), [noise and grain](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/noise-grain-effects.html), [blur](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/blur-sharpen-effects.html), [generate](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/generate-effects.html), [perspective](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/perspective-effects.html) and [utility](https://helpx.adobe.com/en/after-effects/using/utility-effects.html) effect pages.

**Consequence.** Native grain tools drop a 32-bpc project to 16 bpc on that layer. In 32 bpc, use Magic Bullet Renoiser (Maxon One) or Noise, or put grain in an 8/16-bpc finishing comp. Renoiser's bit depth was not checked. [verify]

| Step | AE (native · Maxon One) · Photoshop |
|---|---|
| 1. Black and white points | Exposure + offset per channel (linear) or Levels (Individual Controls) · Supercomp Color Correction "Match Background" · PS Levels, clipped |
| 2. Gray balance | Curves per channel, Lumetri · Colorista 3-way · PS Curves, clipped |
| 3. Contrast, saturation | Lumetri, Hue/Saturation · Colorista · PS Curves, Hue/Saturation |
| 4. Undo baked-in light | Gradient Ramp in a blend mode, against the baked direction · PS gradient fill layer |
| 5. Key light | Gradient Ramp, Soft Light / Overlay · **Scene Light** (relights with AE lights) · PS gradient fill in Soft Light |
| 6. Room bounce | Fill in a blend mode, masked to the side away from the light · PS color fill layer |
| 7. Haze | Exposure offset toward the haze color · Supercomp **Haze**, **Volume Fog** · PS fill layer, low opacity |
| 8. Softness | Camera Lens Blur, Directional Blur, Pixel Motion Blur · PS Lens Blur, Motion Blur |
| 9. Edges | Supercomp **Light Wrap**, **Edge Blend**, **Core Matte** · PS blurred plate copy clipped inside the edge |
| 10. Shadow, reflection | Drop Shadow or a blurred, skewed matte · VFX **Shadow**, VFX **Reflection** · PS by hand |
| 11. Lens | Optical Glow, Chromatic Aberration, Lens Distortion Matcher, only if the plate shows them (06) · PS Camera Raw lens panel |
| 12. Grain | Renoiser (32 bpc) or Match Grain (16 bpc) · PS Add Noise per channel |

### Red Giant facts used above [checked 2026-10-27]
- **Supercomp's Color Correction > Match Background** (Normal layers) sets the layer's black and white points to the image behind it. **BP** and **WP** percentages set how far, from 0% (kept) to 100% (full match). It can be keyframed each time the button is clicked. **Optimize Black Point** does the same for Additive layers. ([Supercomp Layer Effects](https://help.maxon.net/rg/en-us/Content/html/06-Supercomp_layer-effects.html))
  - This is a built-in black/white point match that the user may already own. Use it as the quick path, and as a cross-check on the measured values.
  - It matches whatever sits behind the layer. A dark logo over a bright window gets the wrong points; the measured path reads the spot's surroundings instead.
- **Supercomp's layer effect names:** Blur Behind, Color Correction, Core Matte, Diffusion, Displacement, Edge Blend, Edge Erode, Haze, Heat Blur, Layer Glow, Light Wrap, Optical Glow, Reverse Light Wrap, **Volume Fog**. Files 04 and 07 were corrected to this name on 2026-10-27.
- **Scene Light** relights a 2D footage or image layer with AE point and spot lights. Two local AI models estimate depth and surface direction. Its "My Footage Is" control sets Video, Log (ACEScct) or Linear. Maxon says the models "aren't as accurate as the largest models available." ([Using Scene Light](https://help.maxon.net/rg/en-us/Content/html/01-Scene-Light.html)) Whether it holds steady from frame to frame on video is unchecked. [verify]
- **Universe** has no light wrap, relight or color-match tool. Its fits are Grain 16, Chromatic Aberration, Glow/Chromatic Glow/Edge Glow and Long Shadow (stylized). ([Universe Tools Locator](https://help.maxon.net/rg/en-us/Content/html/universe-tools-locator.html))

### Photoshop facts [checked 2026-10-27]
- **Clipping masks** let each adjustment touch only the layer below. Photoshop has them; After Effects doesn't.
- **Color Lookup** adjustment layers load .cube 3D LUTs (Properties > 3DLUT File > Load 3D LUT). Strength comes from the layer's opacity. ([bwillcreative](https://bwillcreative.com/how-to-use-and-create-luts-in-photoshop/), [SparkleStock](https://sparklestock.com/docs/load-photoshop-luts)) Loading one through a script (batchPlay) reportedly fails silently ([Adobe Community, 2025](https://community.adobe.com/questions-712/applying-3d-lut-cube-file-to-color-lookup-adjustment-layer-via-batchplay-is-there-any-working-m-1179564)), so load it by hand.
  - **One LUT for both apps:** the same .cube drives AE Apply Color LUT and PS Color Lookup.
- **Match Color** (Image > Adjustments) is still documented by users. It is destructive (no adjustment layer or Smart Filter) and works in RGB only ([JP Caponigro](https://www.johnpaulcaponigro.com/blog/17772/photoshops-match-color-may-change-way-see/)). It is a stats matcher, so it has the weakness in §1. No 2026 deprecation was found. [verify]
- **Harmonize** shipped in Photoshop **27.0** (Oct 2025) from the Project Perfect Blend demo ([Digital Production](https://digitalproduction.com/2025/10/29/photoshop-27-0-now-with-harmonise-upscale-firefly-video/), [CG Channel](https://www.cgchannel.com/2025/10/adobe-releases-photoshop-27-0/)).
  - It works on **pixel layers only**: no Smart Objects, text or adjustment layers. It returns variations to pick from ([Adobe](https://helpx.adobe.com/photoshop/desktop/repair-retouch/remove-objects-fill-space/blend-subjects-with-harmonize.html)).
  - Credit cost conflicts between Adobe's pages: 5 per generation on desktop, 1 on the web beta. [verify]
  - Known issues: Generate goes unavailable when layers sit between the Harmonize layer and the subject ([Adobe known issues](https://helpx.adobe.com/ch_it/photoshop/kb/known-issues.html)). Users in 2026 report no-change results ([Adobe Community](https://community.adobe.com/questions-700/harmonize-not-working-button-is-present-photoshop-thinks-while-processing-then-provides-three-options-of-the-exact-same-image-with-no-harmonization-applied-1555491)). No fix was confirmed.
  - Role here: a one-frame look target, path 3. Its result gets measured and rebuilt as values.

## 5. Over time
- When the plate's exposure or local light changes (flags `exposure_change`, `local_light_change` in 10), keyframe the light steps (1, 5, 6) from the per-frame curve. A fixed grade drifts visibly. Example: Hall shot 1 falls 13% start to end.
- Supercomp's Match Background can be re-clicked and keyframed at points through the shot [doc]. Check between the keys.

## 6. QC for a harmonized layer [rule]
- **Squint and desaturate.** The layer's darkest and brightest values sit inside the plate's range at that spot.
- **Check each channel.** Its blacks carry the same cast as nearby blacks.
- **Direction.** Its bright side faces the plate's light.
- **Edges.** At 200%, they're as soft as nearby edges at that depth, with light wrap only where the background is brighter.
- **Grain.** On a flat area of the layer it matches the plate per channel, and it moves.
- **Over time.** The first, middle and last frames all hold.

## 7. More findings (research 2026-10-27, second pass)
Ranked ideas live in `HARMONIZE-IDEAS.md` in the project folder. Facts only here.
- **Perception.** People catch wrong shadow or light direction poorly: inconsistent shadow scenes were judged wrong 46% of the time ([Nightingale & Farid 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6856028/)). Outdoors, people noticed once the sun's direction was off by about 30° ([Lopez-Moreno et al.](https://www.researchgate.net/publication/283019683_The_Perception_of_Lighting_Inconsistencies_in_Composite_Outdoor_Scenes)). Contrast is seen more keenly than color ([Frame.io](https://blog.frame.io/2016/08/25/first-essential-vfx-compositing-matching/)).
  - [rule] Fix blacks, contrast, edges and grain before light direction. Fix direction when it is clearly off.
- **Layer type sets the stack** [rule]:
  - printed/painted on a surface;
  - a physical object;
  - emitting light (04, 07);
  - projected light (Add only, can't darken);
  - a floating graphic (camera traits only).
  Ask which one before building the stack.
- **Softness.** Edge rise distance (10–90%) is a standard sharpness measure, and MTF50 the usual summary ([Imatest](https://www.imatest.com/wp-content/uploads/2019/02/EI_2019_Compensating_MTF_paper.pdf)). `analyze_plate.py` already computes rise width (`_rise_width`, `RISE_PER_BLUR`). Reuse it for the layer's blur.
- **Grain by brightness.** Grain strength depends on exposure. Pros match about three points per channel across shadows, mids and highs ([Logik forum](https://forum.logik.tv/t/the-impeccable-4k-exr-add-noise-workflow/5634), [DVO Regrain RGB](https://filmworkz.com/wp-content/uploads/2025/06/DVO-Regrain-RGB-User-Guide.pdf)).
- **Compression.** 4:2:0 plates smear color edges, so clean graphics show crisp color boundaries the plate can't have. Simulate the subsampling on the layer ([DVXuser](https://www.dvxuser.com/threads/compositing-into-4-2-0.248705/)). Extends 06's ~1 px chroma blur for 4:2:2. 4:2:0 needs both axes [rule].
- **Veiling glare** lifts shadows near bright sources. It is added light, uneven across the frame ([RawDigger](https://rawdigger.com/node/329), [Imatest](https://www.imatest.com/support/docs/5-2/veilingglare/)). Read the black floor at the spot.
- **Shadows** darken the background toward a shadow color, never to black. Existing plate shadows give the density to match ([Chuang et al., SIGGRAPH 2003](https://www.csie.ntu.edu.tw/~cyy/projects/matting/papers/sig2003.pdf), [Autodesk Matte Shadow](https://download.autodesk.com/global/docs/softimage2014/en_us/files/mat-mentalimages_shaders_MatteShadow.htm)).
- **Texture transfer.** AE Displacement Map, driven by the wall's most contrasty channel, makes a graphic follow the surface. Size both layers the same first ([ProVideo Coalition](https://www.provideocoalition.com/2d_texture_mapping/)).
- **Color cast.** Linear Bradford is the ICC-recommended chromatic adaptation and tested as well as CAT16 ([NTNU CCIW](https://ntnuopen.ntnu.no/ntnu-xmlui/bitstream/handle/11250/2626317/CCIW-23.pdf?sequence=1)). Use it for illuminant shifts in linear, baked into the LUT.
- **Photoshop Neural Filters > Harmonization** (beta) is separate from Harmonize. It matches a layer's color and tone to a chosen reference layer, with sliders, and can output a Smart Filter ([CreativePro](https://creativepro.com/how-to-use-photoshops-harmonization-filter/), [Adobe FAQ](https://helpx.adobe.com/photoshop/using/neural-filters-list-and-faq.html)). It is stats-style, so the §1 trap applies.
- **After Effects 26.x:** Object Matte (26.2) and an AI Assistant beta (26.5) ([CG Channel](https://www.cgchannel.com/2026/09/adobe-releases-after-effects-26-5-and-new-ai-assistant-in-beta/)). There's still no native light wrap ([Adobe feature request](https://community.adobe.com/feature-requests-530/native-light-wrap-in-after-effects-layer-1215067)).
- **Automatic scorers** (not used yet):
  - HarmonyIQA (2025) predicts human preference for harmonized images; its release status is unknown ([arXiv](https://arxiv.org/html/2501.01116v1)).
  - BCMI Composite-Image-Evaluation compares light codes of the layer and background ([GitHub](https://github.com/bcmi/Composite-Image-Evaluation)).

## 8. Prior research: realism checklist (researched 2026-07-19, reused 2026-10-27)
It was researched for garment composites against the perception literature and the compositing canon (Wright, Brinkmann, VES Handbook, Nuke). Its findings apply to any layer over footage. They **refine §1 and §6; where they differ, this section wins.**

**What drives perceived realism, in order** (Xue, Agarwala, Dorsey, Rushmeier, *Understanding and Improving the Realism of Image Composites*, SIGGRAPH 2012):
1. Luminance.
2. Color temperature.
3. Saturation.
4. Local contrast.

- **Match zones, not averages.** Match shadows, mids and highlights separately, per channel, in log2 luminance. Leave clipped pixels out. This upgrades §1's black/white/neutral mapping into three zones.
- **Measured human tolerance.** Perceived realism drops 40% at about **2.99 stops** of luminance error, **64.9 mired** of color temperature, or **0.97 stops** of saturation. By equal annoyance, 1 stop of luminance ≈ 22 mired ≈ 0.3 stop of saturation.
- **Working targets for zone deltas** [rule, from the checklist]: ≤ 0.5 stop luminance, ≤ 10–15 mired, ≤ 0.15 stop saturation.

**Light direction tolerance** (Lopez-Moreno et al., APGV 2010; Tan et al., ACM TAP 2015):
- Mismatches of 20–40° mostly go unseen; detection was 68% vs 50% chance.
- Azimuth (left/right) errors matter more than elevation errors. Texture masks the cue.
- **A flipped key, or the wrong elevation sign, is always seen.** Rule: never let the layer's bright side face away from the plate's light. Under 20° is fine; over 35° fails.
- Attached objects are judged by local boundary-intensity relations: the light and dark at the seam.

**Pass order** (stable across Wright, Brinkmann, VES and Nuke practice): color/zone match → interactive light and spill → edges and light wrap → defocus match → lens artifacts → **grain last** → quantize once at export.
- Grain before blur makes mush. This confirms the stack order in §4.

**Edge softness, measured** (Zhuo & Sim, *Pattern Recognition* 2011, gradient-ratio defocus):
- Reblur the image with σ₀ = 1.0 and take the ratio R of the edge gradients. Then σ_edge = σ₀ / √(R² − 1).
- Measure σ on the plate's own edges near the spot and on the layer's edges.
- Add blur of √(σ_plate² − σ_layer²) to the layer. Target |Δσ| < 0.3 px.
- Complements §7's rise-width measure; both should agree.

**Light wrap recipe:** wrap = blur(background, σ_w) × edge band (2–8 px) × brightness gate (background > 0.2), added (screen or plus) in linear. Turn it off where the layer meets a surface it sits on.

**Material response** [rule]:
- Saturation should fall as brightness rises, fitted to the plate's own saturation-vs-brightness slope: S′ = S · (1 − k · smoothstep(Y)).
- A flat logo that keeps full saturation in its highlights reads as a "vinyl decal".

**Float and quantize once:** stay in float from decode to export, with no 8-bit round trips mid-stack. Quantize once at the end; plate-matched grain doubles as dither.

**A numeric "looks fake" check** (non-circular QC oracle):
1. Tan's χ² boundary-histogram score, layer vs surround. It correlates with human detection (r ≈ 0.46–0.64).
2. Zone-delta asserts on the final export.
3. An edge-σ assert.
4. A shading-direction delta ≤ 35°.
5. Exposure sweep: recompute zones at ±2 stops, and the match should hold.
6. A banding detector.

These turn the squint board (HARMONIZE-IDEAS §5) into numbers.

## 9. Spike result (2026-10-27, one test frame)
Evidence: `post-composite-workspace/harmonize-spike/README.md`.
- **Light match beats a stats match and a paste** for a painted logo. It passes 9 of 9 checks; the stats match fails on content (red hue 34° off, 22% chroma left), and the paste fails on light, edges and grain.
- **Painted layer recipe that worked:**
  - Layer colors are reflectance (white paint 0.85).
  - Light = smoothed wall luminance ÷ wall albedo.
  - Illuminant from nearby low-saturation pixels, by Bradford.
  - Plus the local glare floor. **Wrong as built; see §10.**
  - Then defocus → the plate's own grain rescaled by brightness → 4:2:2 chroma.
- **Floating graphic:** camera traits only. Colors untouched.
- **Rules learned** [rule]:
  - For graphics, judge the **white (highs) zone and the black floor**, not shadow or mid zones. A designed dark color is not a light error.
  - Check color cast with **Δuv as well as mired**. Green-magenta casts are off the mired axis (this plate: plain white passed mired but failed Δuv 0.011).
  - **Wall albedo is the key input.** It passed at 0.6 and 0.8 and failed at 0.4 and 0.95. Ask the user, or measure from a known white or gray in the shot.
  - Grain checks need flat areas well away from color edges, or edges read as grain.

## 10. Ground-truth test (2026-10-27, C4D/Redshift renders)
Evidence: `post-composite-workspace/harmonize-gt/README.md`. Four lit cases (neutral, warm/cool split, teal, hot spot), pass bar fixed before rendering. An exact-answer oracle passes every case, so the scenes and scorer are sound.
- **The spike's light match failed all four cases** (+1.3 to +2.0 stops, median ΔE 20 to 29). The cause is the glare floor: the darkest 0.5% near the logo was the wall's own dim patch, not glare. Adding it lifts dark paint toward the wall.
- **With the floor at zero (true for these renders) it passes every case**: luminance within 0.04 stop, median ΔE under 0.7, Δuv ≤ 0.0014. The split light and the steep hot spot did not break it.
- **Rules** [rule]:
  - The relight core holds: layer reflectance × (plate ÷ wall albedo), one Bradford neutral per spot.
  - Glare floor only from a real black reference: a dark object near the spot, the analyzer's floor only when it rests on near-black pixels of real size, or a user mark. Otherwise zero.
  - Wall albedo is a brightness dial only. A miss of ×0.75 or ×1.33 costs 0.4 stop; color stays right.
  - A check must not reuse the method's own estimate. The spike's "not below the local floor" check agreed with the method by construction and hid this.
- **Veil test of the black-reference floor** (same day; `harmonize-gt/README.md`, second part):
  - Rule: black objects are pixels under 25% of their local mean, in patches ≥ 0.01% of the frame, within 600 px. Floor v = (B − a·S/ρ)/(1 − a/ρ), with B the black's dark level, S its surround, a its reflectance (default 0.03). None found: 0.
  - Black reflectance right: 19 of 20 runs pass, glare 1–5%. The miss is uneven glare with the black far from the logo.
  - Black reflectance half or double: 0.1 to 0.27 stop of error in the darks. **a is a dial**, like wall albedo.
  - No floor: 1% glare already fails; 5% leaves the darks half a stop low. Whites and color hold.
  - Jack rerun: floor 0 (its blacks are crushed by the grade). Every non-circular check still passes; red hue and contrast improved.
- [rule] Glare floor = `black_floor()`. Show what it picked as black and the floor value in the plan, so a shadow taken for a black object gets caught.

## 11. Build notes (2026-10-27, `harmonize.py` v1)
Evidence: `post-composite-workspace/harmonize-build/README.md`. All checks pass: C4D truth 8/8, self-test 10/10, Jack painted and floating.
- [rule] **Blur and composite in linear.** Blurring code values darkens bright-to-dark edges (luminance P90 0.46 stop vs 0.10 in linear). In AE this means a linear working space for the softness step.
- [rule] **Measure edge blur near the layer only.** Far edges sit at other depths, and soft light boundaries read as lens blur. Too few edges near the layer: add none, set by eye.
- [rule] **Cast: matrix first, LUT second.** The Bradford matrix is exact as a Channel Mixer in a linear project. A 65-point LUT matches within 1/255 on normal colors but can miss very dark ones.
- **Clean alpha matters more in linear.** An alpha of 0.996 inside lets 0.4% of a bright wall through dark paint.

## Still open
- ~~Test §1 against the C4D ground-truth set.~~ Done, §10.
- ~~Glare floor from a black reference, veil test, Jack rerun.~~ Done, §10.
- [verify] Renoiser bit depth, Scene Light frame-to-frame stability, Photoshop Harmonize credit cost, libcom.
- Wright's chapter text for midtone and gray balancing details.
