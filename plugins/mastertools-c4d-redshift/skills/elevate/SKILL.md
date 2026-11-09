---
name: elevate
description: Diagnoses a mostly built Cinema 4D or After Effects motion graphics scene from rendered frames plus a scene readout, and proposes ranked, evidence-labelled elevation ideas that lift it toward world-class broadcast polish across lighting, color, materials, bevels, camera, composition, typography, motion and finishing. Use only when the user runs /elevate or explicitly asks to elevate, level up or push a specific C4D or AE shot, styleframe, logo resolve, glass panel or type piece toward agency quality. Not for defect audits or broadcast-legal checks (plan-review:shakedown), render settings or Redshift values (c4d-redshift:redshift), UI, slide or document design, plan-level critique (plan-review:challenger), or creating visuals from scratch.
---

# /elevate

If `~/.claude/overlays/elevate/README.md` exists, read it first: the user's own picks, examples and paths. They win over this skill's defaults.

/elevate turns a mostly built C4D or AE scene into a short, ranked list of elevation ideas. Each idea is grounded to a spot in the frame, justified by a labelled source, and handed to the right skill to implement. It is calibrated for broadcast sports graphics.

## Laws

1. **Diagnose; never set render values.** Any Redshift number goes to `c4d-redshift:redshift`, whose ledger outranks everything here.
2. **Ground every note.** Each note cites a frame mark or crop, and the verification pass runs before output (`references/vision-protocol.md`).
3. **Label every claim** with the move's evidence label (V/P/D/A/T). [A] is draft art direction until the user approves it. A finding measured in this project's frames or readout is M, written beside the move's label (`M · q1r3a`), never as V; the user's own words are A (user), never D (`references/README.md`, "Which label").
4. **Lead with what the user doesn't already know.** No lectures on fundamentals. Five ideas at most.
5. **Say what can't be judged.** Flag X items and ask for the readout or a frame strip rather than guessing.
6. **Never alter brand marks.** Elevate the light, material and motion around them (TYP-14).
7. **Taste hierarchy:** gold examples outrank the reference files, and the user's notes outrank both.
8. **Hero surfaces are polished.** On a hero shot, crop every camera-facing surface at 4x, side walls and outer bevels included. Texture is wanted; streaks, smears or stray lines are a defect even when faint (MAT-13, BEV-11; reference photos from the user's overlay, when present).
9. **Asset library first, when the user has one.** When an idea needs a material, model, light rig or HDRI and the user has a texture or asset library (for example Greyscalegorilla or KitBash3D), propose a library asset first: search it with the user's own library tools and name the asset, its path and its label. Build from scratch only when nothing fits or the library is the wrong look, and say which (MAT-18, LGT-20). Flag licence status when the library's licence may not cover the work; the user decides.
10. **Prove a Try's direction before naming it.** Read the knob's code or probe it once before saying "more" or "less" (a lift that raises camera and aim together adds headroom). A cause stays a hypothesis until a same-frame A/B moves the measure, and first check the test changed pixels at all; a tag that never applied makes the test void.

## Inputs

- **Frames:** 3–5 key frames (approach, mid, resolve, hold), plus 1:1 crops of edges, the smallest type and the brightest highlight. When raw renders arrive and a shell is available, run `scripts/frame_prep.py`.
- **Scene readout (strongly preferred):**
  - C4D: the Maxon Cinema 4D MCP server with read and render groups only, or `scripts/c4d_readout.py`.
  - AE: `scripts/ae_readout.jsx`.
- **No readout:** proceed from frames at Medium/Low confidence and ask for the readout once.
- **Optional north star:** a moment from `references/moments.md` or one the user names.

How frames and readouts arrive depends on the surface. See Surfaces.

## Surfaces

Check what this session can actually do, then take the first row that fits. Never assume a tool exists.

| What's available | Frames | Readout | Grounding |
|---|---|---|---|
| Cinema 4D MCP tools are listed (Claude Desktop with Maxon's server; Claude Code works but is unofficial) | Render the viewport or shot camera through the MCP, or use attached frames | The server's read tools. If it only offers Python execution, send the contents of `scripts/c4d_readout.py` as the code (it only reads) | MCP images arrive as images, not files. Use the imagined grid unless they can be saved and run through `frame_prep.py` |
| A shell or code execution (claude.ai, Claude Desktop, Claude Code) | Run `scripts/frame_prep.py` on attached or local frames. If Pillow is missing, install it or fall back to the imagined grid | Read the attached readout JSON, or in Claude Code read it from the path the user gives | Grid overlay from `frame_prep.py` |
| The scene is built by a script (a build file plus data, often headless c4dpy) | Render drafts from the script, or use its output frames | The build data is the readout: cameras, lights, materials and counts are known exactly. Read the saved .c4d with `scripts/c4d_readout.py` through c4dpy if needed. Confidence High | Grid overlay from `frame_prep.py` |
| Neither | Work on the attached frames | Ask once for the JSON. The user runs `c4d_readout.py` in C4D's Script Manager or `ae_readout.jsx` via Run Script File | Imagined 4×4 grid: columns A–D left to right, rows 1–4 top to bottom; confidence one step lower |

- Scripts that run inside C4D or AE are run by the user, unless an MCP tool can run them.
- The installed skill folder is read-only in the chat apps. Anything /elevate writes there, such as a gold-example draft, goes out as a downloadable file. In Claude Code, write it to the user's overlay (`~/.claude/overlays/elevate/examples/gold/`) when it exists, else to `examples/gold/`.

## Workflow

**Plan stage (reference frames only, nothing built yet).** Read the reference first: a measured read on 1:1 crops, lifted when the frame is dark (`vision-protocol.md`, Frame prep), or the reference-read lane once it exists. Feed that read into the plan, then run elevate at the first clay or draft frames. For a remake, offer deep mode here, not only after a built shot stalls (T: in one remake study, the blind reviewer at plan stage found the mark's edge profile and that the brand red couldn't reach the reference's value).

1. **Prep.** Frames become F1…Fn with grid cells A–D × 1–4 and crops K1…Kn.
2. **Classify the shot:** PB-LOGO, PB-GLASS, PB-ABSTRACT (strands, ribbons, waveforms, type on paths), AE type piece, or a stub type. If unsure, state the assumption in one line.
3. **Load**, following `references/README.md`:
   - always: vision-protocol
   - readout.md, if a readout exists
   - one playbook, plus at most two principle files it names
   - ladders
   - 2–4 gold examples matched by shot type
4. **Apply the readout flags first** (`references/readout.md`). They give High-confidence candidates.
5. **Read the frames** in the playbook's check order, using each file's Read section and judgeability flags. On the first read also check:
   - **Repeats and primitives:** tile repeat at hero-surface scale, straight-walled prisms, flat tops where the real thing is irregular. Perspective hides repeat on far surfaces, so a low repeat score there proves nothing; crop near.
   - **Speed jumps:** a sudden drop into slow motion can read as a glitch, not slow motion (T: one shot went 1.0 to 0.29 in 4 frames and the viewer read it as a glitch). Flag it and verify in playback.
6. **Rank** FIX before C→S before S→W. If the scene is already strong, lead with S→W instead. Within a tier, rank by visual payoff against the time it costs.
   - **Remakes, sketches and boards:** say how far to push (the target rung), include at least one remix move beyond polish (a new idea, not a cleaner version of the old one), and say what stays.
7. **Verify.** Re-check every note against its mark, drop or relabel the failures, and confirm no Redshift value leaked.
8. **Output** using the contract below.

## Output contract

```
Read: <shot type> · <where it sits, one line> · rungs: LGT C · BEV C · MOT S …
1. [F2·B3] <diagnosis> — <why> (<Lbl> · <Src>[; M · <frame or key>]) → Try <ID>: <specific change> [hold: <what must not drop>] → <hand-off> · <rung>
2. …                                   (max 5, ranked by visual payoff)
Also flagged: <ID — 2–4 word reason; …>   (only when there are more than 5 findings)
Keep: <1–2 things that work; don't break them>
Can't judge from these frames: <X items> → send <what>
Questions for the user: <keep reversals, taste picks; only when there are any>
Next rung: <one S→W idea for the strongest dimension>
Calibration: <no gold examples yet | matched gold: <ids>>
```

- Keep it terse: one line per idea where possible, no tutorials.
- Cite sources by key (`BRN:13`). Give links only when asked; they are in `references/sources.md`.
- Never drop a finding silently. Anything past the top 5 goes on the Also flagged line.
- End every motion note with "verify in playback".
- **hold:** on any Try that could undo an earlier win, name the measure that must not drop (metal base colour, wave amplitude at the hem, black level). On round 2 and later, every Try carries one.
- If an [A] move leads the list, mark it "(draft art direction)".
- When the user has an asset library, a material, model, light or HDRI idea names the library asset (law 9): `Try MAT-18: <asset name> [<library pack>] · <path> (<Lbl>)`. When nothing fits, say `library: none fits "<words searched>"` before the from-scratch move.


## Iterating

**Notes before renders, every round.** Loading this skill is not doing it.
- **The user's words first.** Before choosing a change, look up what their words mean for this shot: the gold examples, the round ledger, their rulings. A word may already be defined there (T: one shot built "etched" as sandblasted frost, though its gold example defined it for that shot as a clear skin around white ice).
- **Pass steps line** before any draft: `Pass steps: prep · crops · gold <ids or none fit> · library · Redshift`, each marked done or n/a with its reason. Then write the notes (output contract) to a file and show them with the board. Let the notes pick 2–3 drafts that differ in kind (construction, light placement), not strengths of one value.
- **Probes are looking.** Light solos and close-ups (one light at a time, a close camera on the part in question) may run before the notes; they answer what makes the good side work.
- **Hold renders until the notes exist.** Write the contract's `Read:` and `Calibration:` lines to a file before any C4D or AE render. Lines already in a file from an earlier round don't count. The user's "render now" lifts this until their next ask.

When the user sends revised frames ("again", "round 2"):
- Compare them against the previous notes and mark each note resolved, partly done or open.
- Then propose the next rung.
- Never repeat a resolved note.
- **Check each fix for overshoot and undershoot** before calling it resolved. Measure the changed part against its neighbour: a fix that flips the value hierarchy (body brighter than its letters) is an over-correction; one the eye can't see at the delivery crop is an under-correction. Mark it "partly done" and say which way it missed. Log both kinds with the reason in the project's `LESSONS.md`.
  - A fix limited to a band or region: crop the rows just outside it too.
  - A flag that fires on some frames: crop every frame it fires on before calling it an artefact.
  - A printed or flat mark that reads wrong: check the material's emission before judging its colour.
  - A defect that could come from several stages (sim, deform, shader, comp): test each stage alone before blaming one.
  - A measure is evidence of direction, not a bar to hit. Edge energy, for example, rises with the artwork's own complexity, so matching another scene's number is not the goal; judge the final at delivery size.
- **Re-sweep the whole frame** each round (`vision-protocol.md`), not only the areas the user named.
- **Keep a round ledger** for the shot in the project (`elevate/ROUNDS.md`, or the project's PROGRESS.md): one line per note with what it changed, the measure that moved, and what the user approved as **keep**. Before proposing a note, check it against every keep line. A note that would reverse one is flagged "reverses round N keep" and goes on the Questions for the user line, not as a Try.
- **If the read didn't move, change the layer.** When the user's complaint repeats after a round ("still looks too CGI"), the next round works on a different layer of cause, not more of the same. For a CGI read, follow the ladder in `vision-protocol.md` (light behaviour first), then offer deep mode.
  - **After two rounds with the same complaint**, the next round must be a construction change or a probe test (light solos, a side-by-side 4x crop against the part that works). Strength-only variants of one value are not a round (T: one shot went through about 25 drafts of one value each, and the part kept reading as the same flat plate).
  - Your own measures rising is not the read moving. Check the crop against the reference side, not the score.

## Deep mode

Offer it at plan stage for remakes, after the first pass when the shot still sits below S, when the read didn't move between rounds, or when the user asks to go deeper. A blind second reviewer reads the frames, every finding is re-checked against pixels, and each idea line carries its origin tag after the ID: `[Claude]`, `[Reviewer]`, `[Both]` or `[Pixel]`. Steps and the fallback when no helper can start: `vision-protocol.md`, "Deep mode".

## Set mode (4 or more frames of one package)

- Output one line per frame (`F3: <main note> → <ID>`), then up to 5 set-wide moves, then one **consistency line**:
  hue (`scripts/set_hue.py`), black level and glow across the set. A frame that doesn't match the others is a FIX.
- Rank set-wide moves the same way (FIX before C→S before S→W).
- When the user has to pick between versions, show them as labelled strips (A, B, C), one strip per option across the same frames, so the pick is one look.

## Hand-offs

| Need | Skill |
|---|---|
| Any render value, sampling, AOV setup or color management | `c4d-redshift:redshift` |
| AE automation, comp templates or timing math | `after-effects:after-effects-engineering`, when installed |
| Defects, broadcast-legal levels or delivery QC | `plan-review:shakedown`, when installed |
| A full composition pass: placement, crops and reframes, safe areas, hierarchy, comparing layouts, push moves with grid-cell notes | `frames:composition`, when installed |
| Concept- or plan-level pushback | `plan-review:challenger`, when installed |
| Audio, music edits, beat sync or level dips | `motion-craft:motion-critique`, when installed (or the project's music-join check); /elevate doesn't judge sound |
| Time saved by a script or automation | `ledgers:timecard`, when installed |
| Finding or loading a library asset (materials, models, HDRIs, light rigs) | The user's own library tools or C4D setup notes, when they have them; otherwise the library's own browser |

## Reference map

| File | Read when |
|---|---|
| `references/README.md` | First run in a session: schema, labels, load order |
| `references/vision-protocol.md` | Always |
| `references/readout.md` | A readout is present, or you are asking for one |
| `references/playbook-logo-resolve.md` | Extruded logo or type resolve |
| `references/playbook-glass-panel.md` | Glass panels |
| `references/playbook-abstract-light.md` | Strands, ribbons, waveforms, light fans, particles, type on paths |
| `references/playbooks-stub.md` | Player cutout, stat graphic, arena, AE type piece, or an unknown shot type |
| `references/lighting.md`, `color.md`, `materials-texture.md`, `bevels-edges.md`, `camera-lens.md`, `composition.md`, `typography.md`, `motion-timing.md`, `finishing.md`, `ae-native.md` | Only the two the playbook names, plus any a readout flag points to |
| `references/ladders.md` | Naming rungs and the next-rung idea |
| `references/clay-detail.md` | Clay or geometry-stage frames: set scale, repeats, construction detail, cloth folds (CLY moves) |
| `references/moments.md` | Anchoring a world-class idea in a published reference |
| `references/sources.md` | The user asks for a source, or a citation needs more than its key |
| `references/gold-examples.md` | Selecting or writing gold examples |

## Gold examples

- **Optional.** Gold examples come from the user's overlay (`~/.claude/overlays/elevate/examples/gold/`) when present, else `examples/gold/`. Select 2–4, matching shot type first and dimensions second. Never pick at random.
- **This skill ships with none.** Until some exist, run without them and print "Calibration: no gold examples yet".
- **Prompt at the end of every round the user corrected:** "You corrected this run: save it as a gold draft?" (offer once per round).
- **Growing the set:** when the user corrects a run, offer to save the corrected critique as a draft using `examples/gold/_template.md`. It goes out as a downloadable file in the chat apps, or into the user's overlay (else `examples/gold/`) in Claude Code. It becomes gold only after the user edits and approves it.

## Scripts

| Script | Runs in | What it does | Writes |
|---|---|---|---|
| `scripts/frame_prep.py` | Any shell with Python 3 + Pillow (`pip install pillow`). Don't run it with `python3 -I`: isolated mode hides a user-installed Pillow. Or use `uv run --with pillow python scripts/frame_prep.py …` | Resizes to a long edge, adds grid marks, cuts 1:1 crops, writes a manifest | The `--out` folder |
| `scripts/c4d_readout.py` | C4D 2026 Script Manager, or the MCP Python tool | Read-only dump: render settings, cameras, lights, extrudes and text, materials, takes | JSON next to the saved .c4d, plus stdout |
| `scripts/ae_readout.jsx` | AE: File ▸ Scripts ▸ Run Script File… | Read-only dump: comp, layers, effects, text, key eases, cameras, lights | JSON next to the saved .aep |
| `scripts/set_hue.py` | Python 3 + OpenCV + numpy | Median hue of bright gold/brand pixels per frame vs a reference frame; flags drift over 3 deg (`--selftest` runs its known miss) | stdout |

```
python3 scripts/frame_prep.py F1.png F2.png --out prep --crop "K1=F1:1200,400,600,400"
```

The AE script needs Preferences ▸ Scripting & Expressions ▸ Allow Scripts to Write Files and Access Network. Neither readout script changes the scene.

## Unattended runs

When no one can answer (an overnight batch of stills): pick the recommended reversible move on each frame and pass it to its hand-off skill; never set render values (law 1). List every idea skipped with a one-line reason, and put anything the user must judge (taste picks, brand marks, keep reversals) on the Questions for the user line. Never stop to wait.

## Evals and maintenance

- **Lessons for this skill:** when a run teaches something elevate should know, write it in the project's `LESSONS.md` tagged `[elevate-skill]`, and propose the change to whoever maintains the installed skill. Never edit the installed skill from a project thread.

- The eval cases (evals/evals.md: scene, surface and trigger cases plus the pass/fail bar) ship in the repo bundle, not the installed skill. Run them once the dry run supplies real frames.
- **[V] rule:** V needs a full-text or primary-document read. A table-of-contents match stays P. Log each new source in `references/sources.md` with its read status and date.
- **Volatile files** (re-check yearly): `sources.md`, `moments.md`, `readout.md`.
- **IDs are stable.** Add new moves at the end of a file, and retire old ones with ~~strike~~.
