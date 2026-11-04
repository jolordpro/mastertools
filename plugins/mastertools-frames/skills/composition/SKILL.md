---
name: composition
description: >-
  Use this skill for any question about how a frame, image or layout is composed, even when the word composition is never
  used: feedback or notes on a frame, "why does this feel off", comparing two versions or layouts (A vs B, "which is
  stronger"), where the subject, title, logo or score bug should go, crops and reframes (16:9, 9:16, 1:1, 4:5, safe
  areas), layout options for a graphic, poster or social post, focal point, hierarchy, balance, value, lines, depth,
  negative space, or how to push a frame from solid to world-class. Covers photos, 3D brand frames and styleframes,
  broadcast graphics (lower thirds, full-screens, score bugs, matchup boards), athlete key art, posters, social verticals,
  thumbnails, logos and marks, and film frames. Measures frames with scripts and renders fixes. Not for C4D/AE lighting, material and bevel
  polish (elevate), animation timing (motion-critique), render settings (redshift), web or app UI (design-taste), or
  delivery QC (shakedown).
---

If `~/.claude/overlays/composition/README.md` exists, read it first: the user's own picks, examples and paths. They win over this skill's defaults.

# Composition

Judge and build frames the way a senior art director would, with measurements behind every note. Known weaknesses of AI critics, measured: they describe well but locate problems poorly, they flatter, they invent reasons when unsure, and their A-vs-B picks flip with left/right order. Every rule below exists to counter one of those.

## Laws

1. **Evidence before opinion.** Name the mechanism, not the rule ("subject faces out with no lead room", never "breaks thirds"). Tags in `references/01-evidence-legend.md`; a number from `look.py`, `value_plan.py` or our own render is `[Measured]`, and its meaning takes the tag of the threshold it is checked against. The user's own words are `[A (user)]` and outrank every tag. Never mark work down for missing a `[Lore]` rule (rule of thirds, golden ratio or spiral).
2. **Ground every note** to a frame and grid cell (`F1·B3`: columns A–D left to right, rows 1–4 top to bottom) or to coordinates. Before output, re-check each note against its mark and the numbers; drop or relabel any that fail.
3. **Check everything, report only what holds.** Run every rubric criterion. Report a problem only with a location, a mechanism and a measurement or visible mark. "Leave it" is a valid verdict when the checks are shown.
4. **Show, don't tell.** When scripts can run, lead with the board: the annotated original beside the best fix.
5. **Never trust one order.** Every A-vs-B runs with A on the left and again with A on the right; only agreeing verdicts count. Never grade your own fix by eye alone (see Improve).
6. **Unsure means measure.** Low confidence triggers a measurement or "can't tell from this frame". Never write an invented reason ("slightly crisper") to fill the gap.
7. **Aim at the ceiling.** Removing flaws reaches "solid". Each critique also names the one push move, from the canon, that would make the frame exceptional, unless it already is.

## Surfaces

Check what this session can do; take the first row that fits.

| Available | How to see | Fix rendering |
|---|---|---|
| Shell on macOS | `python3 scripts/look.py IMG --out DIR` (Apple Vision + OpenCV); for dark abstract frames add `scripts/value_plan.py` (dark share, light event, title zone) | `python3 scripts/fix.py IMG plan.json --out DIR` |
| Shell without macOS (claude.ai code execution) | `look.py --no-vision` (OpenCV only; faces, pose, text, masks are null) | `fix.py` works |
| No shell | Imagined 4×4 grid on the raw frame; lower confidence one step; ask for 1:1 crops of small type and edges | Describe fixes with values; say the rendered board needs a session with a shell |

If `cv2` is missing in a sandbox, try `pip install opencv-python-headless`; if that fails, use the no-shell row.

If `report.json` says "Apple Vision models did not load", Bash is sandboxed. Rerun that one `look.py` command with the sandbox off if the host allows it; otherwise go on with the OpenCV fallback and list faces, pose and text under Can't judge.

## Workflow

1. **Classify.** Medium, job type, delivery format and ratio, stage (exploring or shipping). Infer from the frame and state the assumption in one line. Ask only if the answer would flip the verdict.
2. **See.** Run `look.py`. Read `board.jpg` first (grayscale, notan, 10% thumbnail, saliency, lines, grid, safe areas, delivery crops, colour-blind view), then `report.json`, then the original at full size. Crop small type and edges 1:1.
   Reading the report: a tilt from the lines detector alone (Apple horizon absent) is unconfirmed; perspective on boards, sets and architecture reads as tilt. Apple's attention map has a centre prior, so a central peak is weak evidence by itself. Facing is null when no face or pose is found; judge it by eye and say so. All thresholds in the report are `[Infer]` starting points.
3. **Ask in stages.** (a) What is the subject? (b) What competes with it? (c) What single change fixes the most?
4. **Check.** Every criterion in `references/critique/rubric.md`, the job checklist in `references/critique/genre-checklists.md`, and the hard gates (text inside graphics safe; text contrast ≥ 4.5:1 at its worst background pixel, 3:1 for large text; nothing covering play-critical areas; correct spelling).
5. **Reach for the ceiling.** Load the matching canon file. Name the frame's rung on each dimension. Pick the push move that lifts the weakest high-impact dimension (`references/push-moves.md`).
6. **Verify.** Re-check every note against its cell and the report numbers. Drop what doesn't hold. Inspect your own output images up close, one at a time (gaps, cut-offs, uneven size and placement), before presenting any as good.
7. **Output** (contract below). In Improve and Build modes, render first.

## Modes

- **Critique** (default): one frame or layout.
- **Compare**: A vs B per criterion, then overall, in both orders. When a strong pair differs only in style, say so plainly; don't invent a winner. If the two differ only by compression, noise or a global brightness shift under about 2%, call them the same. Taste for designed work is the least shared kind of taste (Vessel et al. 2018).
- **Improve**: critique, then write a fix plan (JSON ops, see `scripts/fix.py --help`) for 2–3 variants and render them. Judge each variant against the original two ways: (a) the numbers move the right way in `look.py` (tilt toward 0°, competing peak weaker, subject ΔL* up, text contrast passes); (b) a fresh judge (a subagent that hasn't seen your reasoning) picks blind, in both orders. Keep a variant only if both agree; if they disagree keep the original and report both, and keep a variant that regresses on one metric while the others improve only with a flag. Run the judge with `scripts/ab_sheets.py` and `references/critique/judge-prompt.md`. **3D renders: re-frame with the camera, not by cropping** (ASP-03): move the camera so a key point lands at a screen position, then re-render; `fix.py` crops are for 2D frames. At most 3 rounds; stop when a round changes nothing material. Put geometry ops (rotate, reframe, crop) first; later ops use the new frame's coordinates. Rotate only with an explicit `deg` taken from the horizon reading in `report.json`, and only when a real horizon or dominant level line exists; never use `deg:"auto"` on frames without one (it reads rock or set edges as horizons).
- **Build**: from intent, format and required elements, propose 3–5 distinct compositions (crop plans, layout boxes as JSON, or HTML/SVG mocks), render, run hard gates first, then rank pairwise in both orders. Present the ranked board.
- **Sequence**: contact sheet of holds and cut points; treat every hold as a still; check where the eye lands across each cut (`references/cinematography/continuity-attention.md`). Timing and easing go to motion-critique.

## Output contract

```
Read: <job> · <format> · <assumption> · rungs: FOC S · VAL C · GLN S · PLC C · DEP S · COL S · EDG C
Verdict: <one line>   or   Leave it: <why, with the checks that passed>
Board: <path>   (when rendered)
1. [F1·B3] <problem> — <mechanism> (<evidence tag or metric>) → <fix with a value> · <rung>
2. …   (max 5, ranked by visual payoff)
Keep: <1–2 strengths the fix must protect>
Push: <one move toward world-class> (<canon exemplar ID>)
Can't judge: <items> → <what's needed>
```

- Dimension codes: FOC focal and hierarchy · VAL value structure · GLN glanceability and clutter · PLC placement and direction · DEP depth · GRP grouping · BAL balance · COL colour · EDG framing, edges and safe areas · MOT motion (video only).
- Rungs (shared with `elevate`): **FIX** below competent · **C→S** competent to strong · **S→W** strong to world-class.
- Fix values are specific: "move the logo 6% right", "burn the C1 window by 1 stop", "lift subject ΔL* from 9 to ≥ 20", "rotate −1.8°".
- One line per note. No tutorials on fundamentals; the reader is a senior designer.
- For apps or batch use, the JSON shape in `references/critique/rubric.md` replaces the text.

## References (load only what the job needs)

| File | Read when |
|---|---|
| `references/00-index.md` | First run: routes any question, maps file ids to paths |
| `references/01-evidence-legend.md` | Weighing or citing evidence |
| `references/critique/protocol.md`, `rubric.md` | Every critique |
| `references/critique/genre-checklists.md` | The job has a checklist (logo or mark, portrait, poster, lower third, stat graphic, bug, thumbnail, interview, title card) |
| `references/canon/3d-brand-frame.md` | 3D styleframes, logo resolves, show opens |
| `references/canon/broadcast-graphics.md` | Lower thirds, full-screens, bugs, matchup boards, packages |
| `references/canon/sports-photo-key-art.md` | Action photos, athlete portraits, campaign key art |
| `references/canon/poster-social-vertical.md` | Posters, 9:16 social, thumbnails |
| `references/canon/abstract-light-titles.md` | Abstract light, line or waveform frames, documentary title frames (DRAFT) |
| `references/canon/textbook-methods.md` | Running a named method (notan, Block contrast/affinity, Bang, Mateu-Mestre value plan, eye-path trace) |
| `references/push-moves.md` | Choosing the push move |
| facet and science files | Only those the rubric flags; paths in `00-index.md` |
| `references/broadcast-motion/*` | Safe areas, lower thirds, reframing, motion staging |
| `references/systems/metric-recipes.md` | Interpreting a `report.json` number |

## Hand-offs

| Need | Skill |
|---|---|
| Lighting, materials, bevels, finishing in a C4D/AE scene | `elevate` |
| Animation timing, easing, motion feel | `motion-critique` |
| Render settings and sampling | `redshift` |
| Web or app UI taste | `design-taste` |
| Delivery QC and broadcast-legal checks | `shakedown` |
| AE automation of a layout | `ae-extendscript` |

## Volatile facts

Vertical platform UI zones change often and sources disagree. Use the conservative default in `references/broadcast-motion/reframing.md` and say "check the platform's current preview before delivery". Benchmark numbers about AI critics date fast; cite them with their year.
