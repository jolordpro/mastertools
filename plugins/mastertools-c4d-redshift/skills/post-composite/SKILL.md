---
name: post-composite
description: Measures a live-action plate (camera drift and parallax, vanishing points and focal length, lens distortion, clipping, the brightest unclipped light, black floor, palette, glossy floors and glass, haze, grain per channel, moving subjects, shutter, DOF, CA, bloom, flicker and light changes) and writes a shot-specific plan for compositing Cinema 4D / Redshift CG into it in After Effects to feature-film standard. The plan covers the OCIO strategy, C4D/Redshift setup (proxies, light groups, Takes, AOVs, render settings), the AE layer stack with a tool and starting settings per step, risks, a QC checklist and questions for production. Use this whenever someone has footage or a plate and wants to put CG, a 3D element, a glowing or emissive object, a logo, light or VFX into it, asks how to make CG "sit in" or "match" a shot, asks for a comp plan, integration plan, plate analysis, matchmove or lens read, or asks why a comp looks fake. Use it even if they only attach a .mov/.mp4 and say "I want to add X to this shot".
---

If `~/.claude/overlays/post-composite/README.md` exists, read it first: the user's own picks, examples and paths. They win over this skill's defaults.

# Post composite

Turn a plate into measured facts, then into a plan someone can build from. Every recommendation traces back to a number from this plate or to a dated fact in `references/`.

## Inputs
- **Plate** (required): a video file or image sequence. ProRes, H.264/5, DNx or integer frames. Scene-linear EXR plates are out of scope for the energy numbers.
- **CG element** (optional): a description or a render. Example: "an emissive ring orbiting the subject".
- **Plugins owned**: ask once (below).

Needs `ffmpeg`/`ffprobe` and Python 3 with `numpy` and `opencv-python`.

## Workflow

### 1. Ask once about plugins
Ask in one short message, with a recommended answer, then move on without waiting if the user has said to proceed:

> Which of these do you own? Maxon One (includes Red Giant), Deep Glow 2, Mocha Pro, Sapphire, Neat Video, others?
> Recommended if unsure: "Maxon One only". I'll name third-party tools as optional upgrades.

Prefer what they own. For every third-party tool, also name a native AE or Red Giant fallback.

### 2. Measure
```
python3 scripts/analyze_plate.py "<plate>" --out "<folder>"
```
About 35 s for 5 s of 1080p. It prints a one-screen summary and writes `plate_analysis.json`, `contact_sheet.jpg`, `overlay.jpg` and `maps.jpg`. Use `--start`/`--dur` to analyze part of a long clip.

If the script was edited, run `python3 scripts/selftest.py` first. It must print 15/15.

### 3. Look at the frames yourself
Open `contact_sheet.jpg`, `overlay.jpg` and `maps.jpg`. The script proposes and the frames decide. Confirm at least:
- Which energy candidate is a **true emitter** and which is a specular (glass, metal).
- That **paired** floor streaks are reflections, and that unpaired ones aren't carpet, rails or door edges.
- That the subject box covers the person (and their reflection).
- What any flagged light change or flicker is (a light turning off, a moving source, an exposure ramp).
- Anything the script can't see: practicals off frame, motivated light direction, what the CG must pass behind.

When the frames contradict a number, say so in the plan and trust the frames. Pull extra frames with ffmpeg when needed.

### 4. Load references progressively
Read `references/README.md` first, then only what the shot needs. Never load all of them at once.

| Load | When |
|---|---|
| `10-scene-analysis-signals.md` | Always, to read the script's output: trust levels, rules, known limits, report format |
| `00-overview-and-decision-tree.md` | Always, for the decision tree |
| `01-color-management-and-pipeline.md` | Always for the pipeline section. Also when the plate has sub-blacks, super-whites or odd tags |
| `02-camera-matchmove-and-lens.md` | Drift, parallax, focal estimate or distortion found |
| `03-c4d-redshift-integration-and-aovs.md` | Writing the C4D/Redshift section |
| `04-ae-comp-rebuild-glow-and-light-interaction.md` | Writing the AE stack, glow and interactive light |
| `05-roto-holdouts-depth.md` | A moving subject or occluder |
| `11-harmonize.md` | Harmonize mode (below): an existing layer (logo, graphic, render, cutout) must match or blend into a shot. §1 method, §10 tested rules and limits |
| `12-placing-graphics.md` | A logo, sign, screen insert or type must be tracked onto a surface: tracker choice, failure fixes, rolling shutter, stabilize round trips, motion blur, perspective type |
| `13-occlusion-color-key.md` | People or objects pass in front of a graphic on a surface (a field, floor or wall logo) |
| `14-ae-compositing-toolbox.md` | Choosing native AE matte tools, blend modes in 32 bpc, precomp rules, shadow catchers, displacement, Content-Aware Fill, plate-driven expressions |
| `15-glossary.md` | A term is unclear or clashes between apps or skills (plate, tracking, key, occlusion, premultiplied, legal range) |
| `06-lens-artifacts-grain-finishing.md` | Grain, DOF, CA, bloom, shutter, final grade |
| `07-atmosphere-and-reflections.md` | Haze, glossy floor or glass found |
| `08-qc-checklist-and-tells.md` | Writing risks and the QC checklist |
| `09-tool-matrix.md` | Choosing tools against what the user owns |

### 5. Write the plan
Use the report format in `10-scene-analysis-signals.md` §5:
1. **Shot read**: each line with its measured value and a trust word (measured / estimated / assumed).
2. **Risks and tells** for this plate, ranked.
3. **Pipeline**: OCIO strategy, exact config, colorspace and view names, bit depth, EXR specs.
4. **C4D/Redshift**: camera (focal, pitch, roll, drift handling), proxies, light groups, Takes, AOVs, render settings with values.
5. **AE stack**: layer order, one tool per step with starting settings, plus a fallback.
6. **QC checklist** tailored to this shot.
7. **Questions for production and open items**.

Save it as a file (Markdown or HTML) next to the analysis outputs. Show it as a **draft** before calling it final.

## Harmonize mode
When someone brings a layer and a shot ("harmonize this logo into the shot", "make this graphic look like it's in the room", "why does this look pasted on?").
1. **Ask what the layer is in the world**, as one poll with the best guess first: painted or printed on a surface, a physical object, emitting light (screen, sign), projected light, or floating (title, lower third). Never guess silently; it decides which steps apply.
2. **For painted and object layers, ask the surface's paint** if it isn't obvious (default: wall albedo 0.6). It is a brightness dial only: a ×0.75 or ×1.33 miss moves brightness 0.4 stop and leaves color alone.
3. **Place the layer at plate size** (tracking and placement: `12-placing-graphics.md`), saved as an RGBA PNG or TIFF with straight alpha.
4. **Run:**
   ```
   python3 scripts/harmonize.py "<plate>" "<layer.png>" --kind <kind> --at <seconds> --out "<folder>"
   ```
   If `harmonize_core.py` or `harmonize.py` was edited, run `python3 scripts/selftest_harmonize.py` first. It must print 10/10.
5. **Look before you report:**
   - `black_reference.jpg`: what was taken as black for the glare floor. A shadow or a dark-painted surface marked magenta means the floor is wrong; rerun with `--black-reflectance` set to that surface's value, or treat the floor as zero.
   - `squint.jpg`: paste vs harmonized as brightness only, each channel, heavy blur and edges at 200%. Brightness and blur rows first.
   - `before_after.jpg`.
6. **Hand over `plan.md` as a draft** with the files. Say which values are measured and which are dials. Projected and emitting kinds have no ground-truth test yet; say so.

## Defaults and rules
- **Strategy A** (display-linear: plate interpreted as "Gamma 2.4 Encoded Rec.709", view "Un-tone-mapped") is the default for graded Rec.709 plates. Strategy B only after the round-trip test passes and the user wants a filmic glow (01).
- **Sub-blacks and super-whites**: keep them (32 bpc). Never clamp the plate. When more than ~1% of pixels sit below legal black, ask production about the export range (01).
- **Energy reference** = the brightest *unclipped* emitter. A clipped window or LED core carries no energy information.
- **Don't invent settings.** Every value is either measured, from a [doc] reference, or labeled a starting point. Rules of thumb say "starting point" in the plan.
- **Dated facts.** Version and compatibility claims carry the date they were checked. If that date is more than about three months old, or the job depends on it (a plugin's host support, for example), web-check it again and say so.
- **Lens effects only when the plate shows them**: no flares without ghosts, no CA without measured CA.
- Write the plan in plain words: short lines, values in a consistent unit, one tool per step.

## Files
- `scripts/analyze_plate.py`: the measurement script. All thresholds sit in its `TH` table with [rule] tags.
- `scripts/selftest.py`: builds two synthetic plates with known answers and checks 15 measurements.
- `scripts/harmonize.py`: Harmonize mode. Writes the harmonized frame, the layer alone, the squint board, the black reference, a cast LUT, `harmonize.json` and `plan.md`.
- `scripts/harmonize_core.py`: the light match, glare floor and camera traits it uses. Tested against C4D/Redshift ground truth (2026-10-27).
- `scripts/selftest_harmonize.py`: a synthetic painted wall with a known answer. 10 checks.
- `references/`: 00–15 plus README. Facts are tagged [doc], [rule], [verify] or [checked date].
