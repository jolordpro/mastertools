# 02: Camera, matchmove and lens

## Lock-off check
1. Hold frame 1 (Time Remap), set Difference against the live plate and boost exposure. Static areas should stay black. Ghosted edges mean drift.
2. Track 3–4 static features (AE Track Motion, or a Mocha planar track on the far wall or floor). Read the X/Y curves (Mocha Pro 2026 has a rebuilt Curve Editor).
3. Thresholds (see 00): under 0.25 px means locked. Sub-px to a few px means apply the 2D planar drift to the CG precomp. Parallax means a 3D solve.

## Static layout, one-point perspective
- **Pitch/roll:** the VP sits on the horizon. VP at vertical frame center ≈ 0° pitch. Roll comes from the transverse edges, which should be level.
- **Focal length:** one VP can't determine it. fSpy's 1-VP mode needs a known focal length, with the principal point at the VP. Sources, in order:
  1. Camera report or metadata (best).
  2. Fit a C4D proxy box with plausible real dimensions and adjust focal length plus camera height until the **spacing of features along depth** (door spacing) matches. Width and height alone only fix the ratio of distance to focal length. [rule] Typical dimensions: institutional corridor 1.8–2.4 m wide, ceiling 2.7–3.0 m, doors 0.9×2.1 m, handrails 0.85–0.95 m.
  3. C4D **Camera Calibrator** tag, or fSpy using any second VP (open door leaves, angled signage). fSpy's importer is Blender-only, so either enter the values manually or go Blender → FBX/Alembic.
- **Sensor:** set the C4D sensor width to the production camera's (Super 35 ≈ 24.9 mm). If unknown, keep the horizontal FOV consistent instead.
- **Camera height** [rule]: 1.2–1.7 m for sticks or handheld. Objects at lens height sit on the VP's horizontal line, which is a quick sanity check.

## 3D solve, when needed
- **Mocha Pro 2026** (Boris FX, paid): planar-driven camera solve (SynthEyes-derived). **Refine Solve** deletes unstable features and recalibrates without re-solving. The "Locked Shot" option (2025) solves moving objects on a static camera. Exports to AE/C4D.
- **AE 3D Camera Tracker** (native): fine with clear parallax, weak on near-static shots. Mask out moving people.
- SynthEyes, PFTrack or Blender for hard solves, handed off to C4D via FBX/Alembic.
- **AE → C4D:** File → Export → MAXON Cinema 4D Exporter (.c4d) [verify on build], or FBX from Mocha/SynthEyes.
- **C4D → AE:** Redshift EXRs carry no camera. Use "Save Project for Cineware" (.aec) or the Cineware camera/null extract so AE 3D layers (fog cards, flares) line up.

## Lens distortion
- Keep the original plate pixels untouched. Undistort only for solving and layout, render the CG undistorted with **5–10% overscan**, then **redistort the CG** and crop back.
- **Red Giant Lens Distortion Matcher** (AE-only, Maxon One): grid- or line-based analysis, apply or remove.
- **AE Optics Compensation** (native): single-parameter FOV model, fine for mild barrel distortion. Tick "Reverse Lens Distortion" to invert.
- **STMap:** the most exact option when a lens grid or SynthEyes/3DE solve exists. In AE use **STMapper** 1.0 (aescripts, Jul 2026; AE 2025/2026, needs 32 bpc) [checked 2026-10-23].
- Overscan in Redshift: raise the resolution and film back proportionally.

## Focal length from a single frame
- One VP alone gives pitch and roll, not focal length.
- If the camera tilts so that verticals converge, their meeting point is a second VP. Then f² = −(v1 − c)·(v2 − c) in pixels, with c the frame center. `analyze_plate.py` does this and reports hFOV plus mm for S35 and full frame. Treat it as an estimate until the camera report confirms the lens and sensor.

## Do / Don't
- DO render a wireframe of the proxy over the plate and scrub. Edges must stick.
- DON'T trust a solved focal length on a near-static shot. Use the camera report value.
- DON'T leave the delivered plate distorted or resampled.
