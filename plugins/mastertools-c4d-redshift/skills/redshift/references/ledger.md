# LEDGER — Verified Redshift Facts

**Every row carries a label and a date. A number without both is not usable.**

Labels: **[V]** verified against Maxon docs on the stated date · **[D]** derived
from a [V] fact · **[P]** practitioner practice · **[T]** test range, unmeasured ·
**[R]** recalled, do not use.

Canonical documentation tree: `https://help.maxon.net/r3d/cinema/en-us/`

Source shorthand: **R/** = `https://help.maxon.net/r3d/cinema/en-us/Content/html/`
(pages carry no version stamp; the release notes run to 2027.0.1, so read them as
2027 docs). **C27** = `https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/`.

Updated 2026-10-31 from an approved knowledge-base ledger proposal. Rows dated
2026-10-30 or 2026-10-31 came in then.

## Contents

1. Version baseline
2. Sampling and threshold
3. Redshift Live — denoising and upsampling
4. Progressive passes
5. Trace depth
6. Global illumination
7. Fireflies and hot highlights
8. Colour management
9. Mac and Metal
10. Recalled entries
11. Open holes
12. Lights, visibility, displacement and materials

---

## 1. Version baseline

| Fact | Label | Date | Source |
|---|---|---|---|
| Redshift 2027.0 (2026.10) and 2027.0.1 (2026.10) released. **2027.0.1 is the current patch** | **[V]** | 2026-10-31 | R/Release+Notes+Latest.html |
| Redshift 2027.0 adds a new device memory architecture: less memory, faster time to first pixel | **[V]** | 2026-10-31 | R/Release+Notes+Latest.html |
| Redshift 2026.9 (2026.09): OCIO updated to 2.5.2; fixed wrong monitor name for a display profile. Day not stated | **[V]** | 2026-10-31 | R/Release+Notes+Latest.html |
| Redshift 2026.8.1 (2026.08) released 12 Aug 2026. Was the current patch on 2026-08-20; superseded | **[V]** | 2026-08-20 | Maxon release-notes index |
| Redshift 2026.8.0 (2026.07) released 22 Jul 2026. Was the feature baseline on 2026-08-20 | **[V]** | 2026-08-20 | Maxon release-notes index |
| Redshift 2026.8 raises minimum to **Cinema 4D 2026.3** | **[V]** | 2026-08-20 | Release Notes (Latest), 2026.8, marked \*\*\*IMPORTANT\*\*\* |
| Redshift 2026.5 raised minimum to **Cinema 4D 2026.2** | **[V]** | 2026-08-20 | Release Notes (Latest), 2026.5 |
| Cinema 4D 2026.3.4 released 5 Aug 2026. Was the current C4D on 2026-08-20; 2027 not yet checked | **[V]** | 2026-08-20 | Maxon knowledge base |
| Cinema 4D 2026.2.0 (15 Apr 2026) bundles **Redshift 2026.5.0** | **[V]** | 2026-08-20 | C4D 2026.2.0 release article |
| Cinema 4D 2026.3.x bundles **Redshift 2026.7.0**; 2026.8.x is a separate manual update | **[V]** | 2026-08-20 | C4D 2026.3.x release articles |
| Cinema 4D 2026.1.4 (17 Mar 2026) bundles **Redshift 2026.2.0** | **[V]** | 2026-08-20 | C4D 2026.1.4 release article |
| Redshift 2026.5.0 released 15 Apr 2026, same day as C4D 2026.2.0 | **[V]** | 2026-08-20 | Maxon release-notes index |
| Cinema 4D 2026.0 requires macOS 14.0 or later | **[V-carry]** | 2026-08-20 | Secondary source, re-verify |
| Redshift 2026.0.0 dropped support for Cinema 4D R25 and S26 | **[V]** | 2026-08-20 | Release Notes (Latest), 2026.0.0 |

**Baseline re-check, 2026-10-31.** The 2026-08-20 "current" rows are history now.
Which Redshift C4D 2027 bundles, and the minimum C4D version for Redshift 2027,
are not verified yet (§11). Do not infer either from the version numbers (Law 5).

**Consequence of the 2026.0.0 row:** any documentation URL containing `/c4d/s26/`
describes a Cinema 4D version this renderer no longer supports. Such URLs
cannot carry a 2026 fact even when the number they contain is right.

---

## 2. Sampling and threshold

| Fact | Label | Date | Source |
|---|---|---|---|
| Threshold is the Adaptive Error Threshold. Lower detects noise more aggressively, shoots more rays per pixel, less visible noise | **[V]** | 2026-08-20 | Sampling — Production |
| Default 0.01 works for a wide variety of scenes | **[V]** | 2026-08-20 | Maxon sampling guidance |
| Production quality: Maxon recommends lower settings such as **0.003** | **[V]** | 2026-08-20 | Maxon sampling guidance |
| With DOF or motion blur, use at least **8–16 min samples** | **[V]** | 2026-08-20 | Unified Sampling |
| Strong DOF or long motion blur may require **256+ max samples** | **[V]** | 2026-08-20 | Unified Sampling |
| Automatic Sampling: threshold is the only parameter affecting sample count. Min/Max are hidden | **[V]** | 2026-08-20 | Sampling — Production |
| Disabling Automatic Sampling reveals Samples Min and Max; threshold still operates inside those bounds | **[V]** | 2026-08-20 | Sampling — Production |
| Automatic Sampling has no effect on point-cloud rendering | **[V]** | 2026-08-20 | Unified Sampling |
| Basic quality presets map to threshold: Low 0.100 / Medium 0.010 / High 0.005 / Very High 0.001 | **[V]** | 2026-10-31 | C27 Render Settings — Basic (was [V-carry]) |
| Maxon example timings on one scene: 0:44 / 3:20 / 7:53 / 22:50 for 0.1 / 0.01 / 0.005 / 0.001. Shows threshold cost, not a time to expect | **[V]** | 2026-10-31 | C27 Render Settings — Basic (was [V-carry]) |
| Show Samples: all-white pixels mean Max Samples was reached. Look before changing sampling | **[V]** | 2026-10-30 | C27 Unified Sampling; Sampling Advanced |
| Per-ray sample overrides replace or scale the counts; they work only with Automatic Sampling off | **[V]** | 2026-10-30 | C27 Sampling Advanced |
| Automatically Reduce Samples of Other Effects is **on by default**. Maxon does not recommend disabling it | **[V]** | 2026-10-31 | R/System+-+Advanced.html |
| Image filter: Gauss is the default, size 2–3; Mitchell 3–5; sharper filters need a larger size | **[V]** | 2026-10-30 | C27 Sampling Advanced |
| Bucket size 512 vs the default 128 cut one frame from 3:24 to 2:02 with the same look. One test; GPU noted in the KB card | **[P]** | 2026-10-30 | https://www.youtube.com/watch?v=wnJGABcUCh0 |

**[V-carry]** means: the claim is plausible and internally consistent, was
carried in from prior research, but its citation does not meet Law 1. Treat as
[T] for any delivery decision until re-verified. Do not quote it as Maxon's
position without the caveat.

### Threshold intent bands

The ladder above is the anchor. These bands are the working interpretation.

| Intent | Threshold | Label |
|---|---:|---|
| Fast layout preview | 0.05–0.10 | **[T]** |
| Lookdev / draft | 0.01–0.02 | **[T]**, anchored on 0.01 default |
| General production | 0.005–0.01 | **[T]** |
| Broadcast final | 0.003–0.007 | **[T]**, anchored on Maxon's 0.003 |
| Hero still / critical frame | 0.001–0.003 | **[T]** |
| Below 0.001 | — | Only if a side-by-side shows a visible gain |

Threshold response is not linear and not scene-portable. Two shots in the same
package can want different values.

### Manual min/max test ranges — all [T]

| Scene | Min | Max |
|---|---:|---:|
| Simple still | 4–8 | 32–128 |
| General motion graphics | 8–16 | 64–256 |
| Strong DOF | 8–16 | 128–512 |
| Long motion blur | 8–16 | 128–512 |
| Pathological / hero | 16–32 | 512–1024+ |

Only the 8–16 min and 256+ max figures are [V]. Everything else in this table
is a bracket for measurement.

---

## 3. Redshift Live — denoising and upsampling

| Fact | Label | Date | Source |
|---|---|---|---|
| **Native** engine uses machine learning to upsample from a lower internal resolution | **[V]** | 2026-08-20 | Sampling — Live |
| Native uses **DLSS** on Windows with NVIDIA hardware | **[V]** | 2026-08-20 | Sampling — Live |
| Native uses **MetalFX** on Mac with Apple hardware | **[V]** | 2026-08-20 | Sampling — Live |
| Live does not render (Maxon's full list of 12): subsurface scattering (SSS), hair, point clouds, texture displacement (tessellation-free), AO, volumes, the Ray Switch node, Trace Sets, light linking, soft shadows, motion blur, AOVs. The list may predate 2027 additions to Live | **[V]** | 2026-10-31 | R/Redshift+Live.html, Limitations |
| **OIDN** denoises with no upscaling, compatible with all hardware | **[V]** | 2026-08-20 | Sampling — Live |
| Upsampling Mode — Quality **44%** of target resolution | **[V]** | 2026-08-20 | Sampling — Live |
| Upsampling Mode — Balanced **33%** | **[V]** | 2026-08-20 | Sampling — Live |
| Upsampling Mode — Performance **25%** | **[V]** | 2026-08-20 | Sampling — Live |
| Upsampling Mode — Ultra Performance **11%** | **[V]** | 2026-08-20 | Sampling — Live |
| Upsampling Mode is only available with the Native engine | **[V]** | 2026-08-20 | Sampling — Live |
| OIDN has its own Quality control: High / Balanced / Fast | **[V]** | 2026-08-20 | Sampling — Live |
| OIDN High prioritises quality, best for final; Fast prioritises speed | **[V]** | 2026-08-20 | Sampling — Live |
| OIDN results can differ across hardware architectures at all three quality levels | **[V]** | 2026-08-20 | Sampling — Live |
| Static Frame Denoising applies OIDN after a set number of passes | **[V]** | 2026-08-20 | Sampling — Live |
| Threshold # Passes sets how many passes before Static Frame Denoising engages | **[V]** | 2026-08-20 | Sampling — Live |

### The percentage trap

Those percentages are **of target resolution by pixel count, not by linear
dimension**. Performance at 25% renders at half the width and half the height,
which is a quarter of the pixels. **[D]** from the [V] figures: √0.25 = 0.5.

The full derivation, which also explains why the numbers look like DLSS:

| Mode | Pixels | Linear scale **[D]** | 3840×2160 renders at **[D]** |
|---|---:|---:|---|
| Quality | 44% | ~66% | ~2560×1440 |
| Balanced | 33% | ~58% | ~2216×1247 |
| Performance | 25% | 50% | 1920×1080 |
| Ultra Performance | 11% | ~33% | ~1280×720 |

Reading these as linear scale factors overstates the internal resolution by
roughly 2×. That mistake makes Live previews look more trustworthy than they are.

### Final-frame denoising (production)

| Fact | Label | Date | Source |
|---|---|---|---|
| The denoiser is a finisher: it can oversmooth, leave brush-stroke artifacts, and fail on very noisy input | **[V]** | 2026-10-30 | C27 Denoising |
| Altus single and dual pass work in bucket mode only. OptiX is NVIDIA only, so not on a Mac | **[V]** | 2026-10-30 | C27 Denoising |
| Denoise overhead defaults: 10% bucket, 100% progressive. 0 means one denoise at the end | **[V]** | 2026-10-30 | C27 Denoising |
| Randomize Pattern on Each Frame **off** for denoised animation, to cut flicker | **[V]** | 2026-10-30 | C27 Denoising; Sampling Advanced |
| OIDN and OptiX need the Diffuse Albedo and Bump Normals AOVs; Automatically Create AOVs adds them | **[V]** | 2026-10-31 | C27 Denoising |

---

## 4. Progressive passes

| Fact | Label | Date | Source |
|---|---|---|---|
| Progressive Passes applies to Production Progressive and Live only | **[V]** | 2026-08-20 | Sampling — Live |
| Controls the maximum number of passes reachable | **[V]** | 2026-08-20 | Sampling — Live |
| **Interactive:** only reaches max passes if left undisturbed between edits. Any scene edit restarts the climb | **[V]** | 2026-08-20 | Sampling — Live |
| **Final rendering:** always reaches exactly the max pass count, no more and no fewer, then moves to the next frame | **[V]** | 2026-08-20 | Sampling — Live |

**Why this matters for animation.** In final progressive rendering the pass
count is a fixed per-frame budget, so every frame gets identical sampling
effort regardless of difficulty. That is good for temporal consistency and bad
for a sequence where a few frames are much harder than the rest — those frames
get no extra effort and will be the noisy ones. Bucket mode with adaptive
threshold spends where the noise is. This is one concrete reason final
delivery goes through Bucket.

### Progressive pass test bands — all [T]

| Intent | Passes |
|---|---:|
| Instant feedback | 8–16 |
| Lookdev | 16–32 |
| Material approval | 32–64 |
| Technical review | 64–128 |
| Final-equivalent check | higher, still validate in Bucket |

Do not map production threshold values onto Live. They are different controls
on different architectures.

---

## 5. Trace depth

| Fact | Label | Date | Source |
|---|---|---|---|
| Combined Depth caps GI, reflection, refraction and volume depth | **[V]** | 2026-10-31 | R/Globals+-+Advanced.html (upgraded from [V-carry]) |
| Transparency depth is **not** limited by Combined depth. It goes deeper and renders faster than refraction. Materials can override depths | **[V]** | 2026-10-31 | R/Globals+-+Advanced.html |
| Eight thick glass panes need a refraction trace depth of at least 16 to see through all of them (2 per pane; Maxon's test scene, Basic page: "until the refraction trace depth is high enough") | **[V]** | 2026-10-31 | C27 Render Settings — Basic (was [V-carry], originally `/s26/`) |
| Redshift 2026.8 added Combined, Reflection and Refraction trace depths to Live | **[V]** | 2026-08-20 | Release Notes, 2026.8 |
| Redshift 2026.8 added **refraction support** to Live | **[V]** | 2026-08-20 | Release Notes, 2026.8 |
| Redshift 2026.8 added **transparent shadows** to Live | **[V]** | 2026-08-20 | Release Notes, 2026.8 |

### The interface arithmetic — [D]

A thick refractive pane presents two interfaces to a camera ray: entry and
exit. So:

- 1 pane = 2 interfaces
- 2 stacked panes = 4
- 4 stacked panes = 8
- 8 stacked panes = 16

This derivation reproduces Maxon's own 8-panes-needs-16 example exactly, which
is why the carried claim is credible. Set refraction depth to the interface
count, then confirm combined depth is at least that high.

**Transparency is not refraction.** Alpha-style transparency uses Transparency
Depth and costs far less than physical transmission. Before reaching for
refraction on a sports panel, ask whether the design needs light to bend at
all. Frequently it wants the look of glass, not the physics of glass.

---

## 6. Global illumination

| Fact | Label | Date | Source |
|---|---|---|---|
| Brute Force: high accuracy, stable in animation, noisier and slower | **[V-carry]** | inherited | GI docs |
| Irradiance Cache: faster on large smooth surfaces, can flicker or splotch in animation | **[V-carry]** | inherited | GI docs |
| Irradiance Point Cloud: efficient secondary engine, needs storage, can leak light at detailed corners | **[V-carry]** | inherited | GI docs |
| Brute Force primary + IPC secondary is a documented general starting point when more than one bounce is needed | **[V-carry]** | inherited | GI docs |
| With Irradiance Cache primary, 1–2 secondary bounces often suffice | **[V-carry]** | inherited | GI docs |
| With Brute Force primary, 2–3 bounces often suffice | **[V-carry]** | inherited | GI docs |
| Irradiance Cache: rays 500–1000 (2000–4000 for interiors). Draft Max Rate −1 / Min Detail 4–8; final 0 / 0; Min Rate −4 or −5 at 4K | **[V]** | 2026-10-30 | C27 GI Advanced; Irradiance Cache engine |
| Secondary GI default is Irradiance Point Cloud. Volumes force Brute Force with any point-based engine | **[V]** | 2026-10-30 | C27 GI Advanced |

The first six GI rows are inherited rather than freshly fetched. It is stable,
long-standing Redshift behaviour and unlikely to have changed, but it has not
been checked against a current page. Re-verify before it anchors a delivery
decision.

**For animation:** cache-based GI trades render time for temporal risk. A
sequence that flickers is worse than a sequence that took longer. Test the
cache method across a moving range, never on one frame.

---

## 7. Fireflies and hot highlights

| Fact | Label | Date | Source |
|---|---|---|---|
| Max Subsample Intensity limits the maximum intensity of each individual sample | **[V]** | 2026-08-20 | Sampling — Live |
| Higher values make antialiasing harder; a single very bright sample dominates the pixel | **[V]** | 2026-08-20 | Sampling — Live |
| Maxon's illustration: 128 leaves an emissive ring visibly aliased, 4.0 improves it, 1.0 renders it smoothly | **[V]** | 2026-08-20 | Sampling — Live |
| Drawback 1: in HDR output, bright pixels clamp to that value, limiting post bloom | **[V]** | 2026-08-20 | Sampling — Live |
| Drawback 2: clamping loses light energy, appearing as darkening, worse at high sample counts | **[V]** | 2026-08-20 | Sampling — Live |
| Energy loss is **especially apparent in depth of field** — Maxon's own example shows weak bokeh highlights at 1.0 and strong ones at 4.0 | **[V]** | 2026-08-20 | Sampling — Live |
| The only fix for both drawbacks is raising the value, which reintroduces harsh edges | **[V]** | 2026-08-20 | Sampling — Live |

**This is the single most important firefly fact for broadcast sports work.** A dark
background, a chrome logo, a bright strip light and shallow depth of field is
the exact scene where clamping quietly kills the bokeh. The bright specular
circles in the blur are the shot. Clamp them and the frame goes flat, and
nobody diagnoses it as a sampling setting because it does not look like noise.

Order of investigation for fireflies:

1. Is the source a hot primary sample or a hot secondary ray? They have
   different controls.
2. Inspect the light and material intensities first. A firefly is often a
   lighting mistake wearing a sampling costume.
3. Max Subsample Intensity — and check the bokeh after every change.
4. Max Secondary Ray Intensity, for hot contributions arriving through glossy
   reflection or glass.
5. Only then increase sampling on whichever effect legitimately needs it.

---

## 8. Colour management

| Fact | Label | Date | Source |
|---|---|---|---|
| Redshift 2026.8 added OCIO config **`maxon-cg-v1.0_ocio-v2.4.ocio`** with ACES v2.0 support, improved file rules and v2.4 profile support | **[V]** | 2026-08-20 | Release Notes, 2026.8 |
| Redshift 2025.6.0 upgraded OpenColorIO to 2.4.2 | **[V]** | 2026-08-20 | Release Notes, 2025.6.0 |
| 2026.4 added RenderView automatic detection of the monitor's display profile (OCIO) | **[V]** | 2026-08-20 | Release Notes, 2026.4 |
| Redshift 2027 ships **`maxon-cg-v1.1_ocio-v2.4.ocio`** (ACES 2 default view transform, ACEScg render space). The legacy `config.ocio` still ships. Which file is the default is not stated | **[V]** | 2026-10-31 | R/Color+Management+-+OCIO+ACES.html |
| Use the same OCIO config at every stage, comp included. Pass EXR between apps | **[V]** | 2026-10-30 | R/Color+Management+-+OCIO+ACES.html |
| Apply Color Processing (view transform, tone mapping, gamma) is on by default only for lighting AOVs: diffuse, specular, SSS, reflection, refraction, emission, GI, caustics, volume, translucency | **[V]** | 2026-10-31 | R/Intro+to+AOVs.html |

Never say "ACES" without naming the config and the role. Four distinct things
get flattened into that one word:

- **Rendering / working space** — what the renderer computes in
- **Texture colour space** — how each input map is interpreted
- **View transform** — what the display shows
- **Output encoding** — what lands in the file

A wrong texture interpretation produces a viewport-to-render mismatch that no
sampling setting will ever fix. Albedo and base colour take a display-referred
space. Normal, bump, roughness, metalness and mask data take Raw or the
non-colour data role. Never gamma-correct a data map.

---

## 9. Mac and Metal

Full treatment in `mac-metal.md`. Ledger rows only here.

| Fact | Label | Date | Source |
|---|---|---|---|
| 2026.1.0 added precompiled Metal kernels for macOS Tahoe to reduce startup time | **[V]** | 2026-08-20 | Release Notes, 2026.1.0 |
| Known rendering artifacts remain on **Intel CPU + AMD GPU** systems on Tahoe. Apple Silicon is not implicated | **[V]** | 2026-08-20 | Release Notes, 2026.1.0 |
| OIDN 2.3.0 (Redshift 2025.2.0) brought GPU denoising on Metal for Apple Silicon; 2025.5.0 moved to OIDN 2.3.3. Maxon's notes name no OIDN 2.5 | **[V]** | 2026-10-31 | Release Notes, 2025.2.0 and 2025.5.0 |
| `redshiftUsdCmdLine` renders .usd files to disk, Mac included. Added in 2025.2.0 (not new in 2027). Built for SideFX Solaris scenes; scenes from other DCCs are supported only once those DCCs support the complete Redshift USD pipeline, so don't assume a C4D USD export renders. Its page gives no look-change warning | **[V]** | 2026-10-31 | R/USD+Command+Line.html; Release Notes, 2025.2.0 |
| 2026.2.0 updated Hardware Ray Tracing back-ends for better interactivity | **[V]** | 2026-08-20 | Release Notes, 2026.2.0 |
| 2026.5 improved render startup performance in high-primitive-count scenes when using Hardware Ray Tracing | **[V]** | 2026-08-20 | Release Notes, 2026.5 |
| 2026.8 fixed poor interactivity when HWRT fails to initialise due to out-of-memory | **[V]** | 2026-08-20 | Release Notes, 2026.8 |
| Irradiance Cache and Irradiance Point Cloud do not benefit from hardware ray tracing the way brute-force tracing does | **[V-carry]** | inherited, re-verify | Globals — Advanced |
| Apple Silicon uses unified memory shared between CPU and GPU | **[V]** | general platform fact | Apple |
| Redshift reserves 90% of free GPU memory by default; above 90% risks instability; memory is released after 10 s idle. Recheck against 2027's new memory architecture | **[V]** | 2026-10-31 | R/System+-+Advanced.html |
| Volumes are not handled by out-of-core. Baked displacement textures cannot go out of core. The log's GPU Memory figures show out-of-core use | **[V]** | 2026-10-31 | R/System+-+Advanced.html; Volume Object; Tessellation and Displacement; Log Files |
| A Redshift log prints texture lines only on a texture cache miss: a warm run of the same scene prints none. Texture lines never identify a scene | **[T]** | 2026-10-31 | 6,666 GPU render logs on an M1 Max Mac: 6,024 have no texture lines |
| The log's "Breakdown:: Geo: N MB, Tex: N MB" line is the scene's own GPU memory. The "Allocated" total is mostly ray buffer, which grows into whatever memory is free, so it overstates what a scene needs | **[T]** | 2026-10-31 | One production shot's log: Geo + Tex 1,122 MB, Allocated 14,479 MB |
| Hardware RT has a 5–10 s ramp-up, so 20–40 s frames gain little. M3 and later only | **[P]** | 2026-10-30 | https://www.youtube.com/watch?v=L4riSkE7FwA |

That HWRT-versus-GI row is load-bearing for Mac preset design and it is
inherited rather than fetched. Re-verify it against **Globals — Production**
before building presets on it.

---

## 10. Recalled entries

Errors are kept, not deleted. A deleted error comes back.

### [R] "Redshift Live was introduced earlier in the 2026 cycle, not 2026.4"

**Recalled 2026-08-20. This is false.**

The 2026.4 release notes state: *"[All] Added Redshift Live render mode (and
discontinued Redshift RT)."* Live shipped in **Redshift 2026.4 (2026.03)**.

**Root cause, diagnosed 2026-08-20.** Cinema 4D 2026.2's feature documentation
does describe Live, which looks like a contradiction and is not one. C4D 2026.2
shipped on 15 April 2026 bundling **Redshift 2026.5.0**, by which point Live had
existed for a full release. Reading "Live is in C4D 2026.2" as "Live shipped in
Redshift 2026.2" crosses two unrelated version lines.

There is no conflict between Maxon's documents. There is a version-number
collision between two products on different cadences, and it is now Law 5.

This remains the most instructive entry in the ledger. A confident correction,
repeated in three places for emphasis, that inverted a verifiable fact — and the
mechanism was a single unexamined cross-product inference.

Corollary: **Redshift RT was discontinued in 2026.4.** Any tutorial referring
to RT predates Live and its settings do not transfer directly.

### [R] `/c4d/s26/` documentation citations

**Recalled 2026-08-20.** Cinema 4D S26 support was dropped in Redshift 2026.0.0.
Four of the prior research's thirteen primary sources pointed at that tree,
including the two carrying the most load: the Basic quality ladder and the
refraction-depth example. The figures may survive re-verification. The
citations do not.

**Update 2026-10-31:** the Basic quality ladder and its example timings
re-verified on the C4D 2027 Render Settings — Basic page; both rows in §2 are
[V] again. The refraction-depth example is still open (§11).

### [R] Three card errors caught by the Maxon check, 2026-10-31

Found in knowledge-base cards, not in this ledger. Kept here so they do not
come back. Each card now carries a correction line and `conflicts: [maxon-docs]`.

- A summary said Maxon advises against Automatically Reduce Samples of Other
  Effects. **Maxon says keep it on** (§2).
- A tutorial said displacement needs an Object tag override. **Not since 3.6.04**:
  Automatic Displacement needs no tag (§12).
- An Octane card said Redshift lights have a visible-to-camera switch and a
  "tube" shape. **Redshift has a Camera contribution slider and a Cylinder shape** (§12).

### [R] Dual evidence-label systems

**Recalled 2026-08-20.** The prior document ran a seven-label system in its
body and a separate five-tier A–E confidence system in its preset schema, with
no mapping between them. Replaced by the single five-label system in Law 2.

---

## 11. Open holes

Named, so they do not get filled with guesses.

| Hole | What would close it |
|---|---|
| ~~Basic quality ladder, current citation~~ | **Closed 2026-10-31**: C27 Render Settings — Basic (§2) |
| Refraction depth 16 / 8 panes example | Same page |
| HWRT versus Irradiance Cache and IPC | Fetch **Globals — Production** |
| Production Progressive disabled-feature list | Fetch **Sampling — Production** in full |
| ~~"Automatically Reduce Samples of Other Effects" default state and current guidance~~ | **Closed 2026-10-31**: on by default, keep it on (§2) |
| Current Mac system requirements, and Live's higher bar | Fetch **System Requirements** on the `/r3d/cinema/` tree. Maxon's article refused the fetch (403) on 2026-10-31; open it in a browser |
| Image filter: the Gaussian-for-animation guidance | **Narrowed 2026-10-31**: filter types and sizes are in §2. Still open: the animation guidance |
| Which Redshift C4D 2027 bundles, and Redshift 2027's minimum C4D | Fetch the C4D 2027 release articles and the 2027.0 release notes |
| Which OCIO config file is the 2027 default | A Maxon page that names it, or a fresh 2027 install's settings |
| Does the 90% GPU memory default hold under 2027's new memory architecture | Fetch **System — Advanced** for 2027 again, or the 2027.0 notes in full |
| AOV importance-optimisation interaction | Fetch **AOV — Production** and **Optimization — Production** |
| GPU licence per machine; licences for Team Render and command-line nodes | Maxon support articles refused the fetch (403) on 2026-10-31. Open them in a browser |

Each of these is one scout run. On 2026-10-31 two holes closed and one
narrowed; three opened with the 2027 release and one (licensing) from a 403.

---

## 12. Lights, visibility, displacement and materials

Added 2026-10-31 from the Maxon check of knowledge-base cards.

| Fact | Label | Date | Source |
|---|---|---|---|
| Area light shapes: Rectangle, Disc, Sphere, Cylinder | **[V]** | 2026-10-31 | R/Redshift_C4D_Light.html |
| Per-light contribution sliders Diffuse and Reflection, range 0–2 | **[V]** | 2026-10-31 | R/Common+Redshift+Light+Parameters.html |
| No visible-to-camera switch on lights. Area and dome lights have a Camera contribution slider, 0–2 | **[V]** | 2026-10-31 | R/Common+Redshift+Light+Parameters.html |
| Normalize Intensity keeps intensity constant when the light is resized | **[V]** | 2026-10-31 | R/Redshift_C4D_Light.html |
| Object tag: Primary Ray Visible off hides the object from camera. It still shows in shadows, reflections, refraction and GI | **[V]** | 2026-10-31 | R/Visibility.html |
| GI visibility toggles are Visible to Non-Photon GI and Visible to GI Photons | **[V]** | 2026-10-31 | R/Visibility.html |
| Automatic Displacement (3.6.04+): a material with a Displacement shader and texture displaces with no Object tag. Vector maps still need Max Displacement. Tag settings win | **[V]** | 2026-10-31 | R/Displacement.html |
| Texture displacement Bake Resolution runs 64 to 16k. It is capped at the source size only with Smart Bake on | **[V]** | 2026-10-31 | R/Tessellation+And+Displacement.html |
| Displacement Blender blends up to 4 displacement shaders | **[V]** | 2026-10-31 | R/Displacement+Blender.html |
| IOR To Metal Tints (Utility › Conversion) outputs Facing and Edge Tint, used with Metalness 1 | **[V]** | 2026-10-31 | `https://help.maxon.net/c4d/2027/en-us/Content/html/COM_REDSHIFT3D_REDSHIFT4C4D_NODES_CORE_IORTOMETALTINTS.html`; R/IOR_To_Metal_Tints.html |
| Window glass: Standard Material with Thin Walled. Shadows through it via Fresnel Affects Shadow and Shadow Opacity | **[V]** | 2026-10-31 | R/Standard_Material.html |
| Standard Material has a Metalness slider and no Fresnel Type menu. Fresnel "Metalness" belongs to the legacy RS Material | **[V]** | 2026-10-31 | R/Standard_Material.html; R/Material.html |
| OpenPBR is the default for new Redshift materials in **Cinema 4D** since 2026.2 (a C4D version, not a Redshift one) | **[V]** | 2026-10-31 | `https://help.maxon.net/c4d/en-us/Content/html/COM_REDSHIFT3D_REDSHIFT4C4D_NODES_CORE_OPENPBRMATERIAL.html` (OpenPBR Material node) |

