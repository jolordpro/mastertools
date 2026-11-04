# 07: Atmosphere and reflections

## Atmosphere
- **Measure the plate first.** Backlit deep spaces usually show veiling glare or haze that lifts the blacks with distance. The CG's blacks must lift the same way. **Depth-matched haze is the #1 integration fix for deep sets.**
- **Depth fog in AE:** drive a fog layer with the merged proxy and CG depth. Sample the fog color from the plate's far haze and ramp opacity with depth. Apply it to the **CG** to match the haze already in the plate. Don't add fog to the plate unless it's a creative ask.
- **Emitter glow in air** (sells "light in air"; scale it with distance):
  - **Redshift volume:** homogeneous fog box, with the light groups contributing to the volume, gives a Volume Lighting AOV per group. Most accurate, and occluded by proxies.
  - **AE 2.5D:** Trapcode Shine or CC Light Rays from the Emission pass, masked by depth. Supercomp Volume Fog. Fractal/Turbulent Noise or Universe **Maxon Noise** (2027.0) for inhomogeneity, kept **very low contrast and slow**.
  - **Trapcode Particular** dust motes lit by the emitter, using a ZBuffer (Depth Generator or Redshift Z) so they pass behind subjects. Only if the plate shows motes.

## Reflections
- **Rendered (preferred):** `T_env_refl` from floor and glass proxies with matched roughness and Fresnel. You get correct stretching, mirrored parallax and occlusion.
- **2D fake (fallback):** duplicate the CG precomp and flip it around the element's **projected floor contact point** (not the frame center), offset for perspective. Blur vertically **2–4× more than horizontally**, lower the opacity and mask by the floor matte. **Red Giant Reflection** (AE-only, not WinARM) automates this with falloff.
- **Fresnel:** reflection gets stronger at grazing angles (far floor stronger, near floor weaker). For 2D fakes, multiply by a gradient that increases toward the VP.
- **Streak matching:** measure the length:width aspect of a plate practical's floor streak and stretch the CG reflection to match.
- **Dark glass:** sharper (low roughness) and weaker (~4% at normal incidence, higher at grazing), tinted by the glass. Add a double image only if the plate's glass shows one.
