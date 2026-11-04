# DECISION ENGINE — Scene Classes and Levers

How to get from "this shot looks wrong" to "change this one setting."

## Contents

1. Renderer mode selection
2. Scene classes
3. Symptom to first lever
4. What to change first, what to change last
5. Setting interactions
6. Glass and transparent panels
7. Motion blur
8. Depth of field
9. Displacement and bump
10. AOVs and compositing
11. Starting configurations

---

## 1. Renderer mode selection

Three engines, not three quality levels. They compute differently.

**Production Bucket** — final renders, broadcast masters, AOV-heavy output.
Full unified sampling, per-effect sample controls, point-based GI, photon
mapping and caustics, complete AOV behaviour. Everything delivered goes
through here.

**Production Progressive** — fast confirmation when the missing features do
not matter. Progressive substitutes or disables a meaningful list, including
unified sampling controls and filtering, point-based SSS, photon mapping,
Irradiance Cache, Irradiance Point Cloud, and per-effect sample counts for
DOF, glossy reflection and refraction, and area lights. Quality is driven by
Progressive Passes instead. *(Feature list inherited, not freshly verified —
see ledger §11.)*

**Redshift Live** — interactive lookdev, layout, rapid material and lighting
decisions. Fastest by a wide margin. Check the Live feature-parity table in
`version-timeline.md` before trusting any Live preview of glass, refraction,
transparent shadows or depth of field, because several of those arrived only
in the last two releases.

| Intent | Mode |
|---|---|
| Instant material and camera feedback | Live |
| Interactive test needing Production features | Production Progressive |
| Quick review animation | Bucket at relaxed quality, or Progressive if the limits are acceptable |
| Final broadcast render | Bucket |
| Hero still | Bucket |
| AOV compositing master | Bucket |
| Caustics or photon mapping | Bucket |
| Cache-based GI | Bucket |

---

## 2. Scene classification — base type plus pathology tags

A shot is not one category. `Glass + fast flip + DOF + hot specular + 4K` is a
single normal Tuesday, and forcing it into one bucket loses most of what makes
it hard.

So classify in two moves:

**Base type** — what the shot *is*. One of the six below. This picks the
starting configuration.

**Pathology tags** — what makes it *hard*. Any number, and they compose. Each
tag carries its own levers, and tags stack rather than override.

### Pathology tags

| Tag | Trigger | Owns |
|---|---|---|
| `REFRACTIVE` | Light must physically bend | Refraction + combined depth. §6 |
| `STACKED` | More than one transmissive surface in the path | Interface arithmetic. Multiplies `REFRACTIVE` |
| `GLOSSY` | Chrome, clearcoat, polished metal | Reflection depth, reflection sampling |
| `HOT-SPEC` | Small bright emitters, strip lights, dark background | Max Subsample Intensity, Max Secondary Ray Intensity. §3 |
| `DOF` | Shallow focus | Min/max samples. **Conflicts with `HOT-SPEC`** |
| `MOTION` | Transformation or deformation blur | Steps + min samples |
| `TEMPORAL` | Anything animated that will be scrutinised | Denoiser and GI stability |
| `THIN-EDGE` | Fine typography, bevel highlights, thin glass edges | Filtering, not sampling |
| `AOV-MASTER` | Passes will be graded independently | Importance optimisation. §10 |
| `DISPLACED` | Real surface relief | Bake resolution, Auto Bump, memory |
| `MEM-TIGHT` | 16 GB, or 4K+ with a heavy scene | Overrides quality decisions. `mac-metal.md` |
| `4K-PLUS` | Above 1080p delivery | 4× pixels per 2× linear. Rebenchmark |

### The tag conflicts that actually bite

Tags do not merely add. Some pull against each other, and these three are
where good settings go wrong:

**`HOT-SPEC` + `DOF`** — the important one. Clamping to kill fireflies weakens
the bokeh highlights, and bright specular circles in the blur are usually the
shot. Resolve toward the bokeh and fix fireflies at the light instead.

**`TEMPORAL` + any noise fix** — denoising and cache GI both buy cleanliness
with temporal risk. A clean frame in a flickering sequence is a failure.
`TEMPORAL` wins.

**`MEM-TIGHT` + everything** — memory is not a quality dial, it is a ceiling.
When it is on, it resolves first and the rest fit underneath.

### Worked example

> `Glass + fast flip + DOF + bright rim light + 4K`

Base type **C — fast flip**. Tags: `REFRACTIVE`, `GLOSSY`, `HOT-SPEC`, `DOF`,
`MOTION`, `TEMPORAL`, `4K-PLUS`.

Resolution order: interface count first (`REFRACTIVE`), then confirm combined
depth is not capping, then transformation steps for the arc (`MOTION`), then
min samples serving both `MOTION` and `DOF`, then the `HOT-SPEC` + `DOF`
conflict with the bokeh as the tiebreak, then denoise judged across the whole
flip (`TEMPORAL`), and threshold last. Rebenchmark at 4K rather than scaling
the 1080p numbers.

Seven tags, one order, and threshold — the setting most people reach for first
— arrives last.

### Base types

Six recurring shapes. Each sets a starting configuration; the tags modify it.

### A — Extruded logo or typography
Rigid geometry, bevels, glossy and specular surfaces, strong lights, small
high-importance edges.
**Risks:** bevel aliasing, hot speculars, reflection noise, edge instability
under motion blur.
**Watch:** image filtering more than sampling. A bevel highlight one pixel wide
is a frequency problem.

### B — Glass or transparent panel
Transmission, refraction, reflection, stacked surfaces, bright edge lighting.
**Risks:** insufficient trace depth, noisy refraction, fireflies, AOV noise.
**Watch:** topology before sampling, always. See §6.

### C — Fast flip
High angular velocity, large screen-space movement, motion blur, often glass
or chrome.
**Risks:** motion-blur sample starvation, undersampled trajectories, temporal
denoise artifacts, blurred highlights turning noisy.
**Watch:** transformation steps and min samples, not threshold.

### D — Slow flip or hero reveal
Long readable periods, subtle motion, high scrutiny.
**Risks:** temporal flicker, denoiser chatter, reflections shifting frame to
frame.
**Watch:** anything that changes between frames. This class punishes cache GI
and aggressive denoising harder than any other.

### E — Camera pan or sweep
Object static, camera moving. Thin edges and background detail sweep through
frame.
**Risks:** filter shimmer, temporal denoise instability, background aliasing.
**Watch:** filtering and texture frequency. More samples will not stop shimmer.

### F — Hero still
Maximum scrutiny, no temporal constraint, extensive comp.
**Risks:** residual noise, fireflies, AOV reconstruction, DOF.
**Watch:** this is the one class where escalating global quality is often the
right answer, because there is no temporal budget to protect.

---

## 3. Symptom to first lever

| Symptom | What it is | First lever |
|---|---|---|
| Whole frame uniformly grainy | Global sampling error | Threshold |
| One glossy object noisy | Local reflection problem | That material, that light, reflection sampling |
| Glass black or inner objects missing | Ray terminated early | Refraction depth, then combined depth |
| Glass grainy but complete | Refraction noise | Refraction and glossy sampling, after topology is confirmed |
| Bright single-pixel speckles | Hot rays | Max Secondary Ray Intensity, Max Subsample Intensity, light setup |
| DOF noisy | Lens sampling | Min and max samples, then threshold |
| Bokeh highlights look weak and flat | Clamping ate the energy | **Raise** Max Subsample Intensity |
| Motion blur noisy | Motion and lens sampling | Min/max plus transformation steps |
| Sequence flickers, stills are clean | Temporal reconstruction | Denoiser, GI method, filter, sampling stability |
| GI splotches | GI engine | Retrace, IPC, IC or BF strategy |
| GI flickers in animation | Cache method | Move toward brute force |
| AOV noisy only after a comp grade | Importance optimisation dropped dim samples | Disable importance optimisation for the master |
| Thin lines shimmer | Filtering | Filter choice, texture frequency |
| Displacement too soft | Representation | Auto Bump, bake resolution, tessellation |
| Displacement crushing memory | Scene footprint | Lower bake resolution, Auto Bump, change representation |
| Live looks different from final | Feature parity | Validate in Bucket, check the parity table |
| Render out of memory | Scene footprint | Textures, displacement, AOVs, motion-blur steps |

---

## 4. What to change first, what to change last

**First:**
1. Renderer mode, if it is wrong for the job
2. Material and geometry representation
3. Ray depths needed for the paths that are actually visible
4. GI method
5. The specific secondary effect causing the noise
6. Motion blur or DOF settings, if they are the source

**Later:**
7. Adaptive threshold
8. Manual max samples, if the automatic ceiling is genuinely the constraint
9. Denoiser
10. Aggressive clamping or optimisation

**Never raise blind:** combined depth, reflection depth, refraction depth, GI
bounces, samples everywhere, displacement bake resolution, motion-blur steps,
AOV count, 32-bit output. Each should answer an identified requirement.

---

## 5. Setting interactions

| A | B | How they interact | Decision |
|---|---|---|---|
| Threshold | Manual min/max | Threshold controls adaptive sensitivity inside the manual bounds | Manual only when explicit bounds are needed |
| Refraction depth | Combined depth | Combined caps refraction | Set combined for the topology first |
| Reflection depth | Combined depth | Combined caps recursive reflection | Never raise one without checking the other |
| Threshold | Refraction | Lower threshold gets expensive fast in glass | Confirm depth is right before lowering |
| GI depth | Secondary GI engine | Bounce count controls transport; engine controls method | Choose engine before raising bounces |
| GI | HWRT | Brute force benefits; cache methods reportedly do not | Benchmark by GI engine, not by scene |
| GI | Animation | Cache methods can flicker | Favour brute force when artifacts outweigh the saving |
| Importance optimisation | AOVs | Dim samples dropped from Beauty surface in a graded AOV | Consider disabling for the master |
| Max Subsample Intensity | DOF | Clamping weakens blurry specular highlights | Check bokeh after every change |
| Max Subsample Intensity | HDR post | Clamping caps values available to bloom | Do not clamp a plate destined for post glow |
| Denoise | Animation | Temporal artifacts appear even when a still is clean | Judge sequences |
| Denoise | Microdetail | Low-sample denoise erases fine detail | Compare against a clean high-sample reference |
| Motion steps | Memory | More steps cost resources | Use the minimum that preserves the arc |
| Texture displacement | Unified memory | Baked maps add pressure | Cap bake resolution to screen-space need |
| Auto Bump | Displacement | Preserves fine detail without heavy tessellation | Test before raising displacement resolution |
| Resolution | Threshold | 2× linear resolution is 4× the pixels | Benchmark each delivery resolution separately |

---

## 6. Glass and transparent panels

The highest-value class in this domain and the one most often solved wrong.

### Decision tree

1. Does the panel need light to physically bend, or does it need to look like
   glass? These are different renders at different prices.
2. Must the ray cross multiple thicknesses?
3. Are panels nested or stacked?
4. Is it reflective as well as refractive?
5. Is there strong DOF or motion blur?
6. Are there small bright lights making hot highlights?
7. Will reflection and refraction AOVs be graded separately?
8. Is it close enough to camera for subtle transmission to read?

### Fix order

1. Material mode and physical setup
2. Refraction depth for the actual interface count
3. Combined depth, confirmed not to be capping the path
4. Reflection depth, where recursive reflection is visible
5. Secondary sampling and noise
6. Hot-ray behaviour
7. Only now, global threshold

### The distinction that saves the most time

More samples cannot fix a depth problem. If the renderer terminates a refracted
ray before it reaches the object behind the glass, no number of samples will
create the missing path — the path does not exist. Equally, more depth cannot
fix Monte Carlo noise. Different failures, different levers, and confusing them
costs hours.

### Branch presets by topology

Single pane, double pane, three-plus stacked, pane with internal emissive
element, pane against a reflective background, pane with DOF, pane with motion
blur, pane with a hot edge light. One "Glass" preset across all eight is a
guess wearing a preset's clothing.

---

## 7. Motion blur

Three systems: camera, transformation (rigid), deformation.

For extruded text, logos and rigid panels, transformation blur is the one that
matters. Deformation blur is off by default, costs more memory, and is only
needed when the mesh itself deforms during the move.

**Shutter is a creative control, not a quality control.** All bands **[A]** —
art direction, nothing to verify:

| Look | Shutter |
|---|---:|
| Very crisp | 60–120° |
| Neutral baseline | 180° |
| Energetic | 200–270° |
| Exaggerated speed | 270–360° |

Do not let a shutter angle enter the benchmark queue. There is no measurement
that makes 180° more correct than 240°. Pick the one that matches the package.

**Transformation steps** approximate the trajectory. A straight move needs
few. An arc needs more. A fast flip is an arc.

Benchmark ladder **[T]**: 2 → 4 → 6 → 8 → 10 → 16.

The commonly repeated "4–10" is a practitioner band, not a standard. Find
where the ladder stops improving for the specific move and stop there.

---

## 8. Depth of field

DOF multiplies stochastic complexity, because the camera samples across the
lens rather than through a point.

Sequence:

1. Establish materials and lights with DOF off
2. Clean the secondary noise
3. Enable DOF
4. Set min and max samples for stable bokeh — **[V]** 8–16 min, 256+ max for
   difficult scenes
5. Threshold last, as the global error target

And check Max Subsample Intensity. It is the setting most likely to be quietly
destroying the bokeh highlights that justify the DOF in the first place.

---

## 9. Displacement and bump

**Vertex displacement** — most capable, modifies real vertices, supports vector
displacement, needs adequate tessellation, lower interactivity. Use when
silhouette, shadows or deep relief must be real.

**Texture displacement** — built for interactivity and large low-poly surfaces.
Carries a baked texture representation with UV requirements. On unified-memory
Macs the bake resolution is a memory decision before it is a quality decision.

**Auto Bump** — converts unresolved high-frequency displacement detail into
bump. Medium displacement for silhouette and large relief, Auto Bump for the
fine texture, is faster and lighter than forcing all microdetail into geometry.

The three-way choice:

| Need | Use |
|---|---|
| Detail affects shading only | Bump or normal |
| Detail affects silhouette, shadows, deep relief | Displacement |
| Fine detail on top of medium displacement | Auto Bump |

Do not bake at 8K or 16K by default. Test the smallest resolution that holds
the detail at final viewing distance.

---

## 10. AOVs and compositing

Beauty-only and AOV-master are different production modes, not one render with
extra outputs.

**Beauty-only:** importance-based optimisations can stay on. Nothing hidden
will later be pulled up.

**AOV master:** if reflection, refraction, specular or light-group passes get
brightened substantially in comp, importance optimisation may have discarded
samples that were too dim to matter to Beauty and are now visible. Maxon
documents this behaviour directly.

Typical sports set: Beauty, Diffuse, Specular, Reflection, Refraction,
Emission, GI, Depth, Motion Vector, Cryptomatte and ID utilities, Light Groups
where practical.

Some AOVs are not computed in Progressive mode. Do not approve an AOV master
from a Progressive preview because the Beauty looked right.

**Output:** OpenEXR. Half float unless the pipeline needs 32-bit. Preserve
scene-linear data. Keep the display transform separate rather than baking an
SDR look into the master. Align the exact EXR configuration with whoever
receives it.

---

## 11. Starting configurations

Starting points for measurement, not presets. Nothing here is [V] unless the
ledger says so.

### Fast preview
Live if the scene's features are supported, otherwise Production Progressive.
Passes 8–32 **[T]**. Native MetalFX or OIDN. Minimal trace depths. GI
simplified. Do not judge glass, refraction or motion-blur behaviour here.

### Lookdev
Live for material and camera work, Production Progressive for technical
confirmation. Target: stable enough to make lighting and material decisions.
Not final noise quality.

### Draft animation
Production Bucket. Threshold 0.01–0.02 **[T]**. Automatic sampling first;
manual 8–16 / 64–128 **[T]** for difficult motion blur. BF+IPC or BF-only
depending on temporal behaviour. Moderate denoise, validated across frames.

### Production broadcast
Production Bucket. Threshold 0.003–0.007 **[T]**, anchored on Maxon's 0.003
production recommendation **[V]**. Do not assume 0.003 is needed — inspect the
noise and the sample map first. GI: BF+IPC 2–3 bounces as a start, BF-heavy if
stability demands it. Motion blur: shutter creative, steps benchmarked.
Decide explicitly whether importance optimisations come off for the AOVs.

### Hero still
Production Bucket. Threshold 0.001–0.003 **[T]**. Manual min 16–32, max
256–1024+ **[T]** for severe DOF or motion blur. BF-heavy GI. Full AOV master
optimised for comp robustness. Denoise optional, validated against microdetail
and highlight structure.

### Memory-constrained Mac
See `mac-metal.md`.
