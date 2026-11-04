# CG-into-plate integration reference: index

Research snapshot: **2026-10-23**. Scope: compositing C4D/Redshift CG (especially emissive/glowing elements) into live-action plates in After Effects, to feature-film standard.

## Version snapshot (pin these before starting a job)
- After Effects **26.5** (Sept 2026): OCIO 2.5.1, native ACES 2.0, ships the configs "ACES 2.0 CG v4.0" and "ACES 2.0 Studio v4.0".
- Cinema 4D / Redshift / Red Giant **2027.0** (Oct 14 2026): ACES 2.0 OCIO is the default in C4D.
- Red Giant 2027.0 hosts AE 2025 and 2026.
- Projects already running on 2026.x should stay on 2026.x. Match AE's OCIO config to whatever C4D/Redshift is using.
- Third-party status (Deep Glow 2, Mocha Pro, Sapphire, Neat Video, Lenscare, flares, STMapper) was web-checked on 2026-10-23. See 09. Mocha Pro and Sapphire host support for AE 2026 was **not confirmed**.

## File map: load only what the task needs
| File | Load when |
|---|---|
| `00-overview-and-decision-tree.md` | Always first. It covers how to read a shot and the decision branches. |
| `01-color-management-and-pipeline.md` | Setting up OCIO/ACES, interpreting the plate, choosing EXR formats, or when the round-trip fails |
| `02-camera-matchmove-and-lens.md` | Checking for lock-off, camera layout/solve, focal length, lens distortion |
| `03-c4d-redshift-integration-and-aovs.md` | Building proxy geometry, matte/shadow, light groups, Takes, AOV list, render settings |
| `04-ae-comp-rebuild-glow-and-light-interaction.md` | Layer order, beauty rebuild, glow, interactive light, light wrap |
| `05-roto-holdouts-depth.md` | Isolating people/objects, holdouts, depth maps |
| `06-lens-artifacts-grain-finishing.md` | Defocus, chromatic aberration, flares, halation, motion blur, grain, final grade |
| `07-atmosphere-and-reflections.md` | Haze/fog, volumetrics, floor/glass reflections |
| `08-qc-checklist-and-tells.md` | Review passes and diagnosing why a comp "looks fake" |
| `09-tool-matrix.md` | Choosing a tool by vendor or license, and its 2026 status |
| `10-scene-analysis-signals.md` | Reading `analyze_plate.py` output: what each number means, its trust level, the rule it triggers, known limits, report format |
| `11-harmonize.md` | Making an existing layer (logo, graphic, render, cutout, video element) belong in a shot: the match method, paths to rank, AE and Photoshop tools with bit depth (research 2026-10-27; mode not built yet) |
| `12-placing-graphics.md` | Tracking a graphic onto a surface: which tracker per shot, how each one fails and the fix, rolling shutter, stabilize-place-unstabilize, motion blur on pinned graphics, type in perspective (research 2026-10-27) |
| `13-occlusion-color-key.md` | People or objects passing in front of a graphic on a surface: the broadcast color-key method, an AE version, keyer bit depths, shadows on the graphic (research 2026-10-27) |
| `14-ae-compositing-toolbox.md` | Native AE matte and alpha tools, blend modes in 32-bpc linear, precomp and render-order rules, shadow catchers, displacement, Content-Aware Fill, a `sampleImage()` recipe (research 2026-10-27) |
| `15-glossary.md` | Plain-word compositing terms with each app's name (AE, PS, Nuke, C4D/RS), and words that clash between skills: plate, tracking, key, occlusion (research 2026-10-27) |

## Non-negotiables (apply to every shot)
1. Work in a **32-bpc linear** project under OCIO. Use the **same config version and view** in AE and Redshift.
2. Untouched plate pixels must **round-trip bit-exact**. Run the difference test in 01.
3. CG light must **touch the set**: interactive light pass, reflections in glossy surfaces, occlusion.
4. Build glow from the **Emission AOV**, not from the beauty or the plate.
5. Never let CG blacks go deeper than the plate's black floor. Desaturate halos toward the plate's palette.
6. **Degrain → comp → regrain**, matched per channel.
7. Lens effects (CA, flares, halation, defocus) only **if the plate itself shows them**.
8. Combine light in linear with **Add**, never Screen.
9. Data AOVs (Z, P, N, motion vectors, Cryptomatte) must be **full float and lossless**.
10. Treat AI tools (Object Matte, Depth Generator, Scene Light) as first passes that still need hand fixes.

## Confidence key used in these files
- **[doc]**: from vendor docs or release notes.
- **[rule]**: practitioner rule of thumb. Tune it against the plate.
- **[verify]**: version or compatibility claim not confirmed. Check before relying on it.
- **[checked YYYY-MM-DD]**: web-checked on that date. Recheck if the job starts much later.
