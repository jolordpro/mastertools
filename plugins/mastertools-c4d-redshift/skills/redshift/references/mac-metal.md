# MAC AND METAL — Apple Silicon Constraints

## 1. Unified memory is not VRAM

Apple Silicon shares one physical memory pool between CPU and GPU. Do not model
two independent pools, and never say a 64 GB Mac gives Redshift 64 GB of VRAM.
It does not.

The number that governs a render is **physical unified memory remaining under
the combined load** of macOS, Cinema 4D, Redshift, geometry, textures, caches,
AOV buffers, and whatever else is open. Chrome with forty tabs is a render
setting on this platform.

Heavy consumers, in rough order of how often they cause trouble:

- High-resolution textures and UDIM sets
- Texture Displacement baked maps
- Geometry-heavy scenes
- High deformation and motion-blur step counts
- Volumes
- Large AOV sets
- Other applications

Severe memory pressure triggers swapping, and swapping costs far more
performance than any quality setting saves. The render does not fail. It just
gets slow in a way that looks like the scene is hard.

Maxon documents both **Dealing with Out-Of-VRAM situations** and **Dealing with
Out-Of-RAM situations** in the current tree. On unified memory these converge.

## 2. Hardware ray tracing

Hardware ray tracing accelerates compatible ray-traced operations on supported
Apple Silicon generations, M3-class and newer.

**It does not accelerate everything.** Irradiance Cache and Irradiance Point
Cloud are documented as not benefiting the way brute-force tracing does.
*(This row is inherited, not freshly fetched — re-verify against Globals —
Production before building presets on it.)*

So this inference is wrong:

> "M3 or M4 plus HWRT means every Redshift scene renders faster."

Likely to benefit: glossy reflections, refractions and glass, brute-force GI,
other ray-traced effects. Less likely: cache and point-cloud GI.

Benchmark HWRT on and off **by scene class**, not once for the machine.

### HWRT release history — all [V], 2026-08-20

| Version | Change |
|---|---|
| 2026.2.0 | Hardware Ray Tracing back-ends updated for better interactivity |
| 2026.4 | Fixed texture displacement causing holes in meshes when using HWRT |
| 2026.5 | Improved render startup in high-primitive-count scenes with HWRT |
| 2026.8 | Fixed poor interactivity when HWRT fails to initialise from out-of-memory |

That 2026.8 fix is worth knowing about. Before it, an HWRT initialisation
failure from memory pressure degraded interactivity without announcing itself,
which reads exactly like "the scene got heavy."

## 3. macOS

| Fact | Label | Date |
|---|---|---|
| 2026.1.0 added precompiled Metal kernels for macOS Tahoe, reducing startup time | **[V]** | 2026-08-20 |
| Known rendering artifacts remain on Tahoe for **Intel CPU + AMD GPU** systems | **[V]** | 2026-08-20 |
| Apple Silicon is not named in that artifact note | **[V]** | 2026-08-20 |

Metal-specific fixes appear in most releases. On a Mac, staying current is
worth more than it is on Windows, because the Metal path receives ongoing
correction rather than incremental features.

## 4. System requirements

Prior research recorded Apple Silicon M1+ with 16 GB as the compatibility
baseline, M3+ with 16 GB+ in the Redshift Mac recommendations, and a higher
macOS and hardware bar for Redshift Live than for ordinary rendering.

**Status: [V-carry], not freshly verified. Re-fetch System Requirements on the
`/r3d/cinema/` tree before quoting to anyone making a purchase.**

Whatever the numbers say, they are compatibility floors. They are not
production-performance guarantees, and treating a stated minimum as a working
configuration is how a 16 GB machine ends up swapping through a broadcast
deadline.

## 5. Memory-constrained preset logic

When memory is tight, spend in this order. The list is ordered so that
perceptual quality survives longest.

1. Reduce texture resolution before sacrificing render sampling
2. Cut Texture Displacement bake resolution
3. Reduce background geometry and detail
4. Drop AOVs that will not be used
5. Reduce motion-blur and deformation steps where the visual change is small
6. Close other memory-heavy applications
7. Test HWRT if the scene is ray-trace-heavy
8. Do not assume cache-based GI gains from HWRT
9. Profile memory before raising any quality setting

### By machine class

**16 GB** — low texture footprint, minimal displacement baking, restrained
geometry, careful AOV selection, Live with upsampling for interaction. This
configuration runs Redshift. It does not comfortably run a stacked-glass
broadcast package at 4K with a full AOV master.

**32 GB** — most single-shot sports work fits. Watch UDIM sets and displacement
bakes.

**64 GB and above** — higher complexity is practical, and headroom should still
be measured rather than assumed. The failure mode at this tier is a scene that
fits on the workstation and does not fit wherever it renders next.

## 6. What to record when something goes wrong

Memory problems on unified architecture are hard to reproduce without context.
Capture: Mac model and chip, GPU core count if known, total unified memory,
macOS version, Redshift build, C4D version, what else was running, resolution,
AOV count, peak memory, and whether the machine swapped.

Without the last two the report is a feeling, not a measurement.
