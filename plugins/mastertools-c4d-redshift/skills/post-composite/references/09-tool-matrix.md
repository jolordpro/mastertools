# 09: Tool matrix (status as of 2026-10-23)

Rows marked [checked 2026-10-23] were web-checked on that date. Recheck versions and host support at the start of each job.

License: **Native** = ships with AE or C4D. **RG** = Red Giant, included in Maxon One. **3P** = paid third-party. **Free** = free or open source.

| Tool | Vendor | License | Best for | 2026 status | Notes |
|---|---|---|---|---|---|
| OCIO color management | Adobe | Native | ACEScg working space, plate IDT, output | AE 26.5: OCIO 2.5.1, ACES 2.0 CG/Studio v4.0 | Match the config to C4D |
| Layered EXR import, EXtractoR, IDentifier, Cryptomatte | fnord (bundled) | Native | Multipass EXR, mattes | Since AE 17.0 | Redshift crypto = separate Direct EXR |
| Object Matte (incl. Quick Selection) | Adobe | Native | AI subject holdout | 26.2 (Apr 2026); disk cache 26.5 [checked 2026-10-23] | Old Roto Brush versions selectable |
| Mask Tracker | Adobe | Native | Tracking hand masks | 26.3 (June 2026) up to 5× faster [checked 2026-10-23] | |
| Advanced 3D renderer | Adobe | Native | AE-side 3D helpers (shadows 26.0, DOF 26.3) | 26.x | Not a substitute for Redshift passes |
| Glow | Adobe | Native | Small accents | Long-standing | Linear-looking falloff |
| Camera Lens Blur, Optics Compensation, Pixel Motion Blur, Match/Add Grain | Adobe | Native | Depth blur, mild distortion, plate blur, grain | Long-standing | Camera Lens Blur 32 bpc; Match/Add Grain **8/16 only** [checked 2026-10-27]. Full list in 11 |
| Remove Grain | Adobe | Native | n/a | Long-standing | **8/16 bpc only** [checked 2026-10-27]. Prefer Neat Video |
| 3D Camera Tracker | Adobe | Native | Parallax solves | Long-standing | Weak on static shots |
| Unmult | Adobe | Native | Stock elements on black | 26.0 (Jan 2026) [checked 2026-10-23] | Not for real-alpha EXR |
| Cineware / C4D Lite | Maxon/Adobe | Native | Camera/scene exchange | Still shipped | Not for Redshift finals |
| Cinema 4D + Redshift | Maxon | Maxon One / C4D sub | CG, proxies, AOVs, light groups, matte/shadow | 2027.0 (Oct 14 2026); ACES 2.0 default; Auto Focus | Redshift included with C4D sub |
| Supercomp | Red Giant | RG | Light wrap, reverse wrap, haze, glow | Current; AE-only | 17 GPU context-aware tools |
| Scene Light | Red Giant | RG | AI depth/normal relight; accepts Redshift passes | New 2027.0; RG hosts AE 2025 and 2026 [checked 2026-10-23] | Known issues at release: Edge Smoothing broken; light buttons can freeze AE in non-English languages |
| Depth Generator | Red Giant | RG | AI depth | 2026.1+; AE-only | Render-to-Comp crash noted |
| Lens Distortion Matcher | Red Giant | RG | Undistort/redistort | AE-only | |
| Reflection / Shadow | Red Giant | RG | 2D floor reflection / cast shadow | AE-only; not WinARM | Fallback only |
| King Pin Tracker / Spot Clone Tracker | Red Giant | RG | Planar track / cleanup | AE-only | |
| Optical Glow | Red Giant | RG | Hero glow alternative | Current | |
| Real Lens Flares | Red Giant | RG | Ray-traced flares | 2026.5 zoom/aspherical; 2027.0 Schmutz + LED/fluorescent | Only if motivated |
| Knoll Light Factory | Red Giant | RG | Flares | **Discontinued March 2023** (last in VFX 2023.2.0) [checked 2026-10-23] | Use Real Lens Flares |
| Chromatic Displacement | Red Giant | RG | CA/fringing | Current | |
| Trapcode Particular / Form / Shine / Starglow | Red Giant | RG | Motes, rays, streaks | Particular perf 2026.5 | Use with depth |
| Universe (Glow, Bokeh, Maxon Noise) | Red Giant | RG | Secondary glow, bokeh, noise | Installer merged 2026.2; Maxon Noise 2027.0 | |
| Magic Bullet Looks / Colorista / Film / Renoiser / Denoiser III | Red Giant | RG | Grade, grain, denoise | Current | |
| Deep Glow 2 | Plugin Everything (aescripts) | 3P | **Hero glow** | v1.1.1 (Dec 4 2025); AE 2025–2027; 32 bpc, GPU, MFR [checked 2026-10-23] | Inverse-square falloff. Native Apple Silicon not stated |
| Mocha Pro 2026 | Boris FX | 3P | Planar roto/track, 3D solve, Matte Refine ML | 2026.5 (June 12 2026). AE 2026 host support **unconfirmed**: host page listed AE 2025 and earlier [checked 2026-10-23] | Test in your AE before a job. Fallback: Mocha AE (bundled) |
| Sapphire 2026.5 | Boris FX | 3P | S_Glare, S_AdvancedDefocus, S_LensFlare, S_Glow, S_Grain | May 21 2026. AE 2026 host support **unconfirmed** [checked 2026-10-23] | Test in your AE before a job |
| Silhouette | Boris FX | 3P | Hero roto/paint | Current | |
| Neat Video 6 | ABSoft | 3P | Degrain | 6.1.x supports AE 2026 [checked 2026-10-23] | Profile on a flat area |
| Frischluft Lenscare | Frischluft | 3P | Depth lens blur | AE 26.x **unconfirmed**; last news 2025, Mac builds rolled back 2023 [checked 2026-10-23] | Fallback: Camera Lens Blur |
| Optical Flares / Element 3D | Video Copilot | 3P | Flares | AE 26.x **unconfirmed**; Element 3D last updated 2022 [checked 2026-10-23] | Sparingly. Fallback: Real Lens Flares |
| ReelSmart Motion Blur Pro | RE:Vision | 3P | Vector blur from motion vectors | 7.0.0, AE 2022–2026 [checked 2026-10-23] | Prefer rendered 3D blur for rotation |
| ft-UVPass / ft-PPass2Matte | François Tarlier (aescripts) | Free | P-pass mattes, UV remap | 6.1.0, AE 2026, Apple Silicon [checked 2026-10-23] | |
| STMapper | aescripts | 3P | Exact distortion round trip from an ST map | 1.0 (Jul 2026), AE 2025/2026, Universal; needs 32 bpc [checked 2026-10-23] | |
| fSpy | Stuffmatic | Free | Still camera matching | 1.0.3 | 1-VP needs known focal length; Blender importer only |
| SynthEyes / PFTrack | Boris FX / Foundry | 3P | Hard solves | Current | FBX/Alembic to C4D |
