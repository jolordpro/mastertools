# /elevate references — v2 (Oct 2026)

Knowledge base for /elevate: elevation ideas for a mostly built C4D or AE scene, from frames plus a scene readout. Built for model use: terse rows, stable IDs, load only what the shot needs. Claude already knows the fundamentals; these files exist for IDs, labels, sources, priority, hand-offs and house-specific rules. Never expand a row into a tutorial in output.

## Load order (per run)
1. `vision-protocol.md`: always.
2. `readout.md`: when a readout is present.
3. One playbook for the shot type (`playbook-*.md`). Unknown type → `playbooks-stub.md`.
4. At most two principle files named by the playbook. At clay stage, add `clay-detail.md` (CLY moves).
5. `ladders.md`: to name the next rung.
6. 2–4 gold examples matched by shot type (`gold-examples.md` explains selection).
`sources.md` and `moments.md` are for citing and calibration. Load them only when citing.

## Move row schema
`| ID | If you see | Try | Why | Lbl | Src | Rung | → |`

**ID**
- Stable. Never renumber. Retire with ~~strike~~.

**Lbl** (evidence label)
- **V:** stated in an authoritative primary source read in full.
- **P:** practitioner or teaching practice. Book table-of-contents matches land here.
- **D:** derived from a V fact.
- **A:** art direction, a draft until the user approves.
- **T:** test range; render and judge.
- **M:** measured in our own render, readout or test frame. Name the frame or key it came from (`q1r3a L* p5–p95`, `BLOCKCH 0.02`). True for that scene only.
- Combined labels such as V/D mean the parameter is V and the application is D.

**Which label** (first that fits):
1. A primary source read in full says it → V.
2. Arithmetic or logic from a V fact → D. D always needs a V fact; the user's words or our own numbers alone are not one.
3. A number we read or measured from this project's frames, readout or test renders → M. A pattern drawn from such numbers is not M (see M rules).
4. The user said it (a note, a ruling, a reference they chose) → A (user).
5. A look nobody has approved yet → A.
6. A range to bracket and judge → T.
7. Practitioner or teaching practice → P.

**M rules**
- M describes the scene; the move still carries its own label. Write both when they differ: `M · q1r3a` for the finding, then the move's label (`MAT-17 · T`).
- M never becomes V. A pattern measured in one scene is T until it holds in another scene, then P.
- A move whose only source is one scene's measurements is T or A, never D or V (MAT-14 to MAT-17 follow this).

**Across skills.** The same evidence carries these labels in the sibling skills. When a note cites one, translate it; never mix systems in one note.

| Kind of evidence | elevate | composition | redshift |
|---|---|---|---|
| Primary source or published standard, read in full | V | `[E-strong]`, `[Standard]` | `[V]` (dated Maxon page) |
| Derived from a primary fact | D | `[Infer]` (reasoning from a tagged source) | `[D]` |
| Measured in our own render or frame | M | `[Measured]` | none yet |
| Practitioner or teaching practice | P | `[Practice]`; `[Unverified]` until checked | `[P]` |
| Contested or single-study research | P (say "mixed") | `[E-mixed]` | none |
| Test range or starting threshold | T | `[Infer]` (software thresholds) | `[T]` |
| Art direction, or the user's call | A, A (user) | `[A (user)]` for the user's words; an unapproved look has no tag | `[A]` |
| Popular but refuted | none (don't cite) | `[Lore]` | none |
| Asserted, then failed checking | none | none | `[R]` (never use) |

**Src**
- A key in `sources.md`, optionally with a chapter or section (`BRN:13`).
- "—" means no source.

**Rung**
- **FIX:** below competent.
- **C→S:** competent to strong.
- **S→W:** strong to world-class. Use these for scenes that are already solid.

**→** (hand-off)
- **RS:** `c4d-redshift:redshift`. Any render value goes here.
- **AE:** `after-effects:after-effects-engineering`, when installed.
- **SD:** `plan-review:shakedown`, when installed. Defects and legal levels.
- **—:** no hand-off.

## Judgeability flags (the "Read" sections)
- **F:** frame.
- **C:** needs a 1:1 crop.
- **R:** needs the readout.
- **X:** not judgeable from stills. Say so, then ask for the readout or a frame strip.

## Hard rules
- Never state a Redshift value. Hand it to RS.
- A table-of-contents match never makes a move V.
- Gold examples outrank these files on taste. The user's notes outrank both.

## Files
| File | Contents |
|---|---|
| vision-protocol.md | Frame prep, crops, marks, verification pass, unjudgeable list |
| readout.md | C4D (Maxon MCP, Python fallback) and AE fields; read-only rules; readout-to-move flags |
| playbook-logo-resolve.md | PB-LOGO: extruded logo or type resolve |
| playbook-glass-panel.md | PB-GLASS: glass panel |
| playbooks-stub.md | Player cutout, stat graphic, arena, AE type piece |
| lighting.md | LGT-01–20 |
| color.md | CLR-01–14 |
| materials-texture.md | MAT-01–18, MAT-S1–S3 |
| bevels-edges.md | BEV-01–11 |
| camera-lens.md | CAM-01–14 |
| composition.md | CMP-01–11, ASP-01–03 |
| typography.md | TYP-01–15 |
| motion-timing.md | MOT-01–11 |
| finishing.md | FIN-01–11 |
| ae-native.md | AE-01–07 |
| ladders.md | Competent / strong / world-class per dimension (draft A) |
| gold-examples.md | Why, rules, template, runtime selection |
| sources.md | Source registry with read status |
| moments.md | Dated reference moments from published breakdowns |

## Change log
- **2026-10-31:** MAT-18 says to save the scene before pre-converting library maps, so saved scenes keep library paths, and states the proof: with pre-converted maps, the scenes rendered with no conversions. No label changed.
- **2026-10-31:** law 9 gains the licence flag. MAT-18 and LGT-20 gain the headless step: pre-convert library maps before rendering, then confirm the first frame, because headless Redshift 2027.0.1 hung converting library maps and pre-converted maps rendered clean. No label changed.
- **2026-10-31 (art-director ruling):** added SKILL.md law 9 (asset library first), MAT-18 (materials and models) and LGT-20 (light rigs and HDRIs), an output-contract line that names the library asset and its path, and a Hand-offs row for asset-library tools. Fixed the Files table: materials-texture.md listed MAT-01–13 but held MAT-01–17. No existing row changed. MAT-12 (rebuild a stock hero material from photo reference) and LGT-04/05 (designed key and cards place the hero highlights) still apply on top of a library asset.
- **2026-10-31:** added label M (measured in our own render, readout or test frame), a "which label" order, M rules, and a table that maps these labels to composition's tags and redshift's labels. No existing row changed label. Why: QC notes labelled their own measurements V and the art director's words D, and the scheme had no right label for either.
- **2026-10-30 (art-director note, round 2 of a carved-ice logo shot):** added MAT-14 (blocky texture patches from per-face placement), MAT-15 (texture scale against the hero), MAT-16 (thin clear parts go dark), MAT-17 ("X% see-through" is a look, not a slider), CMP-12 (mark sits in its surface), a whole-frame defect sweep in `vision-protocol.md`, a step 0 in the logo playbook, an overshoot check in SKILL.md Iterating, and source AD-1030. MAT-14 labelled A, MAT-16 and MAT-17 labelled T: their only source is one scene's measurements, not a V fact.
- **2026-10-28 (art-director note):** added BEV-11 (polished piped edge) and MAT-13 (no streaks on camera-facing hero surfaces), SKILL.md law 8, and source AD-1028.
- **v2 (Oct 2026):**
  - Re-labelled after research round 2: Brown 4th ed. is the lead source for lighting and camera, and Burley 2012/2015 are V for materials.
  - Added IDs, rungs, hand-offs, playbooks, ladders, readout spec, vision protocol, gold-example template, source registry and moments.
  - Dropped citations to pirate-hosted book copies.
- **v1 (Oct 19, 2026):** 99 moves. Retired.
