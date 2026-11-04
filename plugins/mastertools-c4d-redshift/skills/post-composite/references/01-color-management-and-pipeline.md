# 01: Color management and pipeline

## Facts by version [doc]
- AE: Project Settings → Color → Color Engine = **OCIO color managed**. Then set the OCIO config, Working Color Space and Display Color Space. Media color space is set per footage item (Interpret Footage).
- AE 26.5: OCIO library 2.5.1 with native ACES 2.0. AE lists the configs as **ACES 2.0 CG v4.0** and **ACES 2.0 Studio v4.0**. Upstream they are `cg-config-v4.0.0_aces-v2.0_ocio-v2.5` and `studio-config-v4.0.0_aces-v2.0_ocio-v2.5`; the exact filenames AE bundles were not confirmed [checked 2026-10-23].
- Names in those configs [checked 2026-10-23]:
  - Input colorspaces: "Gamma 2.4 Encoded Rec.709" (aliases `g24_rec709`, `rec709_display`), "sRGB Encoded Rec.709 (sRGB)", "Linear Rec.709 (sRGB)", "ACEScg", "Raw".
  - Displays: "sRGB - Display", "Rec.1886 Rec.709 - Display".
  - Views: "ACES 2.0 - SDR 100 nits (Rec.709)", "Un-tone-mapped", "Video (colorimetric)", "Raw".
  - "Un-tone-mapped" is a **view**, not an input colorspace.
  - In AE, Interpret Footage → Color has a "Show all" option that reveals the full list.
- Native OCIO arrived in AE 23.x, so older projects may be on ACES 1.0.3/1.3 configs. Under OCIO, the legacy "Use Display Color Management" toggle is greyed out, so calibrate the OS/monitor chain separately.
- C4D/Redshift 2027.0: OCIO updated to ACES 2.0, which is now the C4D default.
- Redshift 2026.4.0: RenderView auto-detects the monitor profile. C4D 2027 has Monitor Profile enabled by default.

## Core rule: data vs view
- ACEScg linear pixel data is identical under ACES 1.x and 2.0. **Only the view transform differs.**
- Use the same config version **and** the same view in Redshift RenderView and in AE. If they differ, emissive highlight rolloff and hue will look different between the lighting and comp stages.

## Plate linearization: pick ONE strategy
### Strategy A: display-linear (DEFAULT for graded, final-look 709 plates)
- Interpret the plate as **"Gamma 2.4 Encoded Rec.709"** (Interpret Footage → Color, "Show all" on).
- Working space ACEScg (or linear Rec.709). Display "Rec.1886 Rec.709 - Display" (or "sRGB - Display" on a desktop monitor), view **"Un-tone-mapped"**.
- Output with the same encoding to get a **bit-exact round trip**. The grade, black level and clipped highlights are preserved.
- Trade-off: plate white is 1.0, so CG emission above 1.0 clips in view. Add a manual soft rolloff (06). Set Redshift RenderView to the same view.

### Strategy B: scene-linear via the inverse ACES output transform
- Interpret with the inverse ACES 2.0 SDR Rec.709 output transform and view with the forward one. This gives a shared filmic rolloff, so emission above 1.0 rolls off naturally.
- Risk: near-white plate pixels map to huge scene values, so any blur, glow or grade on the plate gets aggressive around clipped areas.
- Use it **only if** the round-trip test passes, and keep plate-touching operations minimal.

**Rule:** delivering to a colorist or client edit → A. You're final and want a heavy filmic glow → B (after the test passes).

## Round-trip test (mandatory)
1. New comp containing only the plate, no effects, OCIO on.
2. Render one frame to the delivery encoding.
3. Re-import, set Difference against the original, then boost exposure by +8 stops.
4. The result must be black (within 1 code value). Any structure means the input and output transforms don't match.

## Bit depth and range
- Project at **32 bpc** (required for emission above 1.0, additive rebuild and inverse transforms). 16 bpc clips at 1.0.
- ProRes 422 HQ is usually legal/video range. Check that 10-bit code values 64 and 940 map to black and white in the Info panel at 32 bpc.
- **Working space and ProRes** [measured 2026-10-27, AE Beta 27.1, evidence in `post-composite-workspace/prores-retest/`]:
  - AE decodes ProRes exactly (shadows within 0.1 level of ffmpeg) with no working space, at 16 or 32 bpc, and under OCIO at 32 bpc. Color tags and 422 vs 4444 change nothing.
  - **An sRGB working space darkens ProRes** by up to 12.6 levels (at level 24), because AE treats ProRes as Rec.709 Gamma 2.4 and converts it. This is the "ProRes shadow crush" in older notes. Never use an sRGB working space with ProRes plates.
  - A Rec.709 Gamma 2.4 working space keeps the plate exact but lifts sRGB graphics (PNG logos) by up to 13 levels.
  - Default for graphics into graded Rec.709 footage: **no working space** (or OCIO pass-through), so plate and graphic code values both pass unchanged.
  - Scripting: `workingSpace` is settable in Adobe mode, reads `None` under OCIO. An invalid profile name raises a modal.
- **Excursions:** graded plates often carry sub-blacks (below code 64) and super-whites (above 940). At 32 bpc they survive as values below 0 and above 1. Never clamp them. If a large share sits below legal black (the 2026-10-23 test plate had 4.3%), ask production whether the export is legal range with excursions or full range mis-tagged as legal. Interpret per the answer, then rerun the round-trip test.
- 4:2:2 chroma has half horizontal resolution, so pull mattes from luma and expect soft chroma edges.

## Redshift output formats [doc]
| AOV class | Depth | Compression |
|---|---|---|
| Beauty, light groups, emission, diffuse/spec/reflection, GI, volume | Half | DWAA (≈45 is "perceptibly lossless" per Maxon) or ZIP/PIZ |
| Z, P, N, motion vectors | **Full float** | **ZIP/ZIP1/PIZ (lossless)** |
| Cryptomatte | **Full float**, lossless | ZIP/PIZ, **Direct output, separate EXR** |
- Per-AOV Direct Output bit depth is 8-bit/Half/Float, and **Half is the default**. EXR compression options: zip scanline (default), none, rle, zip16, zip1, piz, pxr24, b44, dwaa, dwab.
- **Cryptomatte in Redshift for C4D works only through Direct output.** Through Multi-Pass it writes an empty-looking color layer.
- To merge the other AOVs into one layered EXR, point their Direct Output at the same file.

## AE multichannel EXR [doc]
- Since AE 17.0, layered EXR can be imported **as a composition**. The fnord EXtractoR, IDentifier and Cryptomatte effects are bundled.
- When imported as a comp, Cryptomatte is applied automatically with nothing selected. Duplicate the layer once per matte.
- If AE says "No Cryptomatte layers found", you loaded the beauty EXR instead of the crypto EXR, or the channels are misnamed (they must look like `CryptoMatte00.red`).

## Do / Don't
- DO set the plate's media colorspace explicitly, never "auto", and note it in the project.
- DO let OCIO handle the display transform. Never bake a viewing LUT into the comp stack.
- DON'T mix the Adobe (ICC) engine and OCIO in one chain.
- DON'T put 8/16-bpc-only effects on linear data. Check each plugin's bpc support.
- DON'T render data AOVs or Cryptomatte with DWAA, B44 or half float.
