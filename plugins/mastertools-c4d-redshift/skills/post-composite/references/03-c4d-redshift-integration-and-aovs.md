# 03: C4D + Redshift integration and AOVs

## Proxy environment
- Use simple geometry for every surface the CG lights or reflects in: floor, walls, ceiling, end wall/window, door insets (boxes), rails (cylinders), glass panels as separate polys, practical lights (for example the LED strip as a thin box).
- **Person/object proxy:** a low-poly capsule or mannequin keyframed to follow the roto silhouette (size, distance). It both **receives** CG light and **casts** occlusion.
- **Plate projection:** project the linearized (ACEScg) plate from the shot camera (C4D Camera Mapping or a Redshift camera-projection node), so CG bounce and reflections pick up the real local colors.

## Matte / shadow [doc]
- Redshift Object tag → **Matte** tab → Override.
  - **Matte** is a camera-ray holdout (alpha 0). It can still show the material's reflections, refractions or GI for secondary rays.
  - **Shadow** is a shadow catcher for back-plates.
  - **Apply to Secondary Rays** keeps mattes consistent in reflections and GI.
- The old **Matte Shadow Catcher shader is deprecated**. Use the object-tag options.
- Use Redshift **≥2026.4.0** if you rely on matte reflections (it fixed bucket-mode artifacts).

## Emitters as lights
- Make emissive geometry a **Redshift Light set to Mesh** (or parent a mesh light to it). An emission-only material lights the scene noisily through GI and won't separate into light groups.
- Give each emitter its own group, e.g. `LG_ringA`, `LG_ringB`. Plate-matching fill or dome goes in `LG_env`.
- A dome from a plate-derived lat-long or set HDRI is **only for reflections on the CG object itself**. Keep it out of the env-light pass.

## Matching the floor gloss [rule]
- Put a test light at the position of a plate practical, then tune the floor proxy roughness until its reflection streak matches the plate's (length and blur falloff). GGX roughness of ~0.1–0.25 at grazing angles is a typical start. Reuse that roughness in the reflection pass.

## Takes (one file, multiple passes)
| Take | Renders | Setup | Comp use |
|---|---|---|---|
| `T_ring_beauty` | CG element only | All proxies + person = Matte | Main CG, already held out |
| `T_env_light` | Proxies lit only by `LG_ring*`, black background, no dome | Proxies not matte; CG element invisible to camera | **Add** onto plate (interactive light) |
| `T_env_refl` | Floor/glass reflections of the CG only | Diffuse 0, reflection on (matched roughness/Fresnel); CG invisible to camera but visible in reflections | **Add** (reflections) |
| `T_shadow_occ` | Occlusion/shadow from the person proxy | Matte + Shadow on floor/walls | **Multiply** |
| `T_utility` | Z, P, N, motion vectors, Cryptomatte | Full float, lossless | Defocus, fog, relight, mattes |

**Env-light material:**
- Projected-plate diffuse gives roughly albedo × irradiance, so you can Add it directly. It over-brightens where the plate is already bright.
- **White/18% grey diffuse (preferred for hero shots)** gives pure irradiance. In AE, multiply it by an albedo proxy (the degrained plate, slightly desaturated, highlights clamped to ~0.8), then Add.

## AOV list (Redshift for C4D names) [doc]
- Beauty, **Emission** (glow source), Diffuse Lighting, Specular Lighting, Reflections, Refractions (only if glass), Global Illumination, Volume Lighting (only if in-render fog).
- **Light Groups:** "All Light Groups", or list them explicitly. **RAW AOVs are incompatible with light groups.**
- **Depth** (`Z`, full float, unfiltered for defocus; render a filtered version too if needed), World Position, Normals (world space), optionally Bump Normals.
- **Motion Vectors:** enabling it **disables Redshift motion blur in the beauty**, so render a separate beauty Take with true 3D blur.
- **Cryptomatte** (object and material), Direct output, separate EXR. Puzzle Mattes as a backup. Optional AO for contact darkening.

## Render settings starting points
- Match the plate's resolution and fps (plus overscan if redistorting).
- Shutter matched to the plate (assume 180° = 0.5 frame unless the camera report says otherwise). Estimate it from the moving subject's blur length vs per-frame displacement.
- Motion blur on in the beauty Take. **Transformation steps ≥3** for fast rotation or orbits (otherwise the blur on curved paths goes straight). Deformation blur off unless the mesh deforms.
- Denoiser: fine on env-light passes. **Never on data AOVs.** Be careful on thin bright emitters, which smear.

## Do / Don't
- DO give each emitter its own light group.
- DON'T render Redshift final frames through Cineware in AE. Render EXRs from C4D.
- DON'T forget the person proxy has to receive light, or the subject never reacts.
