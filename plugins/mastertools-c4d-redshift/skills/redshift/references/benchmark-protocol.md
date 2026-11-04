# BENCHMARK PROTOCOL — Turning [T] Into Measurement

The ledger is roughly two-thirds verified facts and one-third test ranges. This
file is how a **[T]** range becomes a number worth typing into a broadcast
master.

## The rule that keeps it honest

**The model never generates a number.** Render times come from timestamps.
Quality scores come from the user's eyes. This skill computes and records. Same rule
as `timecard` (`ledgers:timecard`), same reason: a benchmark that a model estimated is not a
benchmark, it is a prediction with a table around it.

## Definition of done

The prior research proposed twelve benchmark scenes with no pass criteria, no
time budget and no owner. That programme will not get run, and an unrun
benchmark programme is worse than none because it licenses the belief that the
numbers are about to be verified.

So: **each benchmark is done when it produces one row in the ledger that moves
a [T] to a measured value, or it is not done.**

A benchmark that produces "interesting observations" produced nothing.

## Sequencing — do these three first

Ordered by how much of the user's actual work they unblock. If only one afternoon
exists, do BM-01.

### BM-01 — Glass topology ladder
**Unblocks:** every Class B shot, which is most of the package.

Single pane, double pane, four stacked, eight stacked. For each, find the
minimum refraction depth at which the render is complete, and confirm combined
depth is not capping. Then find the minimum that is visually complete, which
may be lower than the physically complete one.

**Produces:** a topology-to-depth table, replacing the inherited 8-panes-16
example with measured values for the user's actual panel construction.

### BM-02 — Firefly and bokeh tradeoff
**Unblocks:** Class B and F, and the failure nobody diagnoses.

Chrome logo, dark background, bright strip light, shallow DOF. Sweep Max
Subsample Intensity across 1 / 2 / 4 / 8 / 16 / 128. At each stop record:
fireflies present, bokeh highlight strength, apparent overall exposure.

**Produces:** the value where fireflies stop without the bokeh going flat.
This is a single number with high leverage and it does not currently exist.

### BM-03 — Threshold response curve
**Unblocks:** every quality-band decision in the ledger.

One representative shot. Threshold 0.1 / 0.05 / 0.01 / 0.005 / 0.003 / 0.001.
Record render time and note where visible improvement stops.

**Produces:** the user's own curve, replacing Maxon's example-scene timings. Maxon's
numbers describe Maxon's scene. They were never portable.

## The rest of the suite

Run when the work calls for them, not as a programme.

| ID | Scene | Answers |
|---|---|---|
| BM-04 | Extruded logo, bevels, glossy, strong key | Filter choice, reflection sampling, bevel aliasing |
| BM-05 | Fast flip | Where the transformation-step ladder stops improving |
| BM-06 | Slow hero flip | Denoiser chatter and temporal stability at delivery length |
| BM-07 | Camera pan | Filter shimmer on thin typography |
| BM-08 | HWRT on/off by GI engine | Whether cache GI really sees no benefit — closes a ledger hole |
| BM-09 | AOV master | Importance optimisation on/off, dark contributions brightened in comp |
| BM-10 | Resolution scaling 1080 / 2160 / 4320 | Time and memory scaling on the user's hardware |
| BM-11 | Memory stress | Where the machine starts swapping |
| BM-12 | GI method comparison | BF+BF vs BF+IPC for temporal quality per unit time |

## What every run records

Without this block a result cannot be compared to another result.

```
DATE
MAC MODEL / CHIP / GPU CORES / UNIFIED MEMORY
MACOS VERSION
REDSHIFT BUILD / C4D VERSION
SCENE FILE + VERSION
RENDERER MODE
RESOLUTION / FPS / FRAME RANGE
THRESHOLD / AUTOMATIC ON-OFF / MIN / MAX
GI PRIMARY / SECONDARY / BOUNCES
TRACE DEPTHS (refl / refr / transp / combined)
MOTION BLUR MODE / SHUTTER / STEPS
DENOISER / ENGINE / QUALITY
AOV SET
TEXTURE + DISPLACEMENT FOOTPRINT
BUCKET SIZE
HWRT STATE
---
RENDER TIME (from timestamps, not estimated)
PEAK MEMORY
SWAP OCCURRED Y/N
```

## Scoring quality

One quality number hides the thing you needed to know. Score separately, 1–5:

noise · edge and aliasing · reflection · refraction · motion blur · temporal
stability · AOV integrity · highlight and firefly · detail preservation

A setting that improves noise and degrades temporal stability is a bad setting
for animation and a fine one for a still. A single score cannot say that.

## Promoting a result to the ledger

When a benchmark answers something, write the row:

```
| <fact> | **[V-measured]** | <date> | BM-NN, <hardware>, <scene> |
```

**[V-measured]** is distinct from **[V]**. [V] means Maxon documents it. [V-measured]
means the user measured it on their hardware with their scenes. For their own work
[V-measured] outranks [V], because Maxon's number describes a general case and
the user's number describes their case. For anything that leaves the building, cite
[V].

## Preset metadata

A preset without this block is a guess with a filename.

```
preset_name · redshift_version · c4d_version · hardware_profile
renderer_mode · scene_class · production_intent
still_or_animation · resolution · fps
threshold · automatic_sampling · samples_min · samples_max
GI_primary · GI_secondary · GI_bounces · GI_trace_depth
reflection_depth · refraction_depth · transparency_depth · combined_depth
motion_blur_mode · shutter · transformation_steps · deformation_steps
max_subsample_intensity · max_secondary_ray_intensity
denoiser · importance_optimizations · AOV_set
texture_filter · bucket_size · HWRT
displacement_mode · bake_resolution · auto_bump
color_config · output_format · bit_depth
---
validation_status: UNMEASURED | MEASURED (BM-NN) | IN PRODUCTION USE
known_risks
evidence_label_per_nondefault_value
```

`validation_status` is the field that matters. A preset marked UNMEASURED
should not render a master.

## Preset families to build, after measurement

`LIVE_FAST` · `LIVE_LOOKDEV` · `PROG_REVIEW` · `MOGRAPH_DRAFT` ·
`BROADCAST_BALANCED` · `BROADCAST_HIGH` · `BROADCAST_HERO` · `GLASS_BALANCED` ·
`GLASS_HERO` · `FAST_FLIP` · `SLOW_FLIP` · `CAMERA_PAN` · `AOV_MASTER` ·
`STILL_HERO` · `MEMORY_16GB` · `MEMORY_32GB` · `MEMORY_64GB_PLUS`

Seventeen presets is a lot to maintain and most of them will turn out to be
three presets with variations. Build the three that BM-01 through BM-03
support, use them for a month, and let the rest earn their existence.
