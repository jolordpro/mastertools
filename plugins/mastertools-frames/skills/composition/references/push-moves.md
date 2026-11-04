---
id: push-moves
title: Push moves, by weakest dimension
type: playbook
aliases: [push move, how to make it exceptional, next level, world-class move, what would make this great, ceiling, S→W, C→S]
tags: [playbook, push, rungs, improve, build]
related: [canon-3d-brand-frame, canon-broadcast-graphics, canon-sports-photo-key-art, canon-poster-social-vertical, textbook-methods, rubric, protocol, metric-recipes, value-contrast, hierarchy-focal-point, clutter-peripheral, negative-space, depth-space, color, framing-cropping, reframing, broadcast-standards]
evidence: moves are distilled from the canon exemplars (DOC or RETRO) and the textbook methods [Practice]. Start values marked [Infer] are starting points chosen here, not figures from a source.
updated: 2026-10-20
---

# Push moves

Removing flaws gets a frame to solid. These moves take it further. Each row is one change, with a start value, the canon frames that show it working, and the `look.py` number that should move.

## How to pick one

1. Rate each dimension FIX, C→S or S→W (codes in `SKILL.md`). FIX items are notes, not push moves; fix them first.
2. Pick the weakest dimension that carries the job (job weights below). One push move per critique.
3. Take the row that matches the symptom and the job. Name the exemplar ID so the reader can look it up in the canon file.
4. In Improve or Build, render the move and confirm the Check number moves. If it does not, the move did not land; say so.
5. If every high-weight dimension is already S→W, write "Push: none, this is at the ceiling" with the checks that show it.

**Which dimensions carry each job** `[Practice]`, from the canon "what separates" rankings:

| Job | Carry first | Then |
|---|---|---|
| 3D brand frame, logo resolve | VAL, FOC | COL, DEP, EDG (room for type and bug) |
| Broadcast graphic (bug, lower third, full-screen) | GLN, FOC | EDG (anchors, safe), COL (second cue) |
| Sports action photo | FOC, PLC | GLN (strip the stage), VAL |
| Athlete key art | FOC, VAL | EDG (planned split), GLN |
| Poster, 9:16 social, thumbnail | GLN, FOC | EDG (safe box, crops), COL |
| Film or promo frame | VAL, PLC | DEP, MOT |

Canon IDs: `BF` 3D brand frame · `BG` broadcast graphics · `SP` sports photo and key art · `PS` poster and social. Methods: `textbook-methods.md` procedure numbers (M1 to M12).

## FOC: focal point and hierarchy

| ID | Move | When | How (start value) | Rung | Exemplars | Check |
|---|---|---|---|---|---|---|
| PM-01 | One light event | Mark or subject is lit like everything else | Hold the field in a narrow low band; bring one rim or beam onto the subject so it is the brightest, most saturated area. Subject at least 2 stops over the field `[Infer]` | C→S | BF-01, BF-02, BF-29 | `subject` ΔL* up; top `saliency` peak on the subject |
| PM-02 | Strip to one hero | Two or more peaks compete | Remove or mute all but subject, one line of type, one number | C→S | PS-11, PS-13, SP-01 | `saliency` second peak weaker; `edge_density` down outside subject |
| PM-03 | Pick the beat after the play | Choosing among burst frames | Take the reaction, extension or contact frame over the release; accept a little less sharpness | C→S | SP-03, SP-04, SP-10 | `facing` and face found; judge pick in both orders |
| PM-04 | Mark the player, not the field | Analytics or telestration | One ring per meaning, on the player; add a second cue beyond hue | S→W | BG-18 | Ring cell matches the player's cell |
| PM-05 | Draw the invisible | Data graphic restates what viewers see | Ask what the viewer cannot see; make one graphic for that variable | S→W | BG-19, BG-20 | Judge only; no metric |
| PM-06 | Remove the headline | The story is already known | Let the frame run alone or with one small mark | S→W | SP-04, SP-25 | `text` count down; `thumbnail_survival` holds |
| PM-07 | Type as the picture, or near nothing | Medium type next to a medium image | Either set the headline at 40%+ of the frame as the image, or shrink it so the image owns the frame | S→W | PS-06, PS-08, PS-14, PS-17, PS-03, PS-11 | Text box share of frame |

## VAL: value structure

| ID | Move | When | How (start value) | Rung | Exemplars | Check |
|---|---|---|---|---|---|---|
| PM-10 | Two or three masses | Mid-key mush; squint shows no plan | Write the 2 to 4 value masses before lighting or grading (M4, M7, M9); merge small darks into one mass | C→S | BF-27, BF-28, BF-23 | `notan_k3` reads as a design; largest mass share clear |
| PM-11 | Value flip at the finish | A dark open needs a payoff | Run the body dark and low chroma, then cut to a lit environment for the lockup | S→W | BF-01 | Final frame mean L* well above the body's |
| PM-12 | Pre-light the surround | Busy or bright crowd behind the subject | Mask: crowd down 1 to 2 stops, desaturate, cool slightly; lift the subject's edge. `fix.py`: `burn_region`, `desaturate_outside`, `vignette` | C→S | SP-01, SP-13, SP-07 | `subject` ΔL* from under 10 to 20+ `[Infer]` |
| PM-13 | Lightest light against darkest dark at the focus | Highest contrast junction sits off subject | Move or relight so the extreme pair touches at the focus cell (M4, M6) | C→S | BF-29, BF-25 | Max local contrast cell = subject cell |
| PM-14 | Tone-on-tone relief | Field needs brand voice without a second value | Emboss type or pattern into the field in the same hue; light from the side | C→S | BF-29 | `tone` range of field stays narrow |

## GLN: glanceability and clutter

| ID | Move | When | How (start value) | Rung | Exemplars | Check |
|---|---|---|---|---|---|---|
| PM-20 | Strip the stage | Boards, ads, screens behind the athlete | Crop them out; else mask-darken 1 to 2 stops, desaturate, blur to match the crowd. Never blur the ground at the feet | FIX | SP-01, SP-13, SP-18 | `edge_density` in those cells down; `saliency` off the boards |
| PM-21 | 10% and tile test | Before any delivery | Downscale to 10% and to about 130 px wide; message and focal peak must survive | FIX | PS-01, PS-04, BG-04 | `thumbnail_survival` |
| PM-22 | Detail budget | Texture competes with the mark | Keep the busiest texture away from the mark, or soften it there | C→S | BF-29, BF-25 | `edge_density` lowest ring around the mark |
| PM-23 | Silhouette check | Hero pose or shape | Blur to about 20 px (or fill black, M8); the pose must still read | C→S | SP-16, SP-09, PS-01 | Judge on the blurred view |
| PM-24 | Neighbourhood list | Long tables, leaderboards | Show the subject plus nearest items, not the whole order | C→S | BG-16, BG-21 | Rows on screen down |
| PM-25 | One datum per cell | Dense full-screens | One datum per cell; size set by the worst screen | C→S | BG-21 | Min text height at phone size |
| PM-26 | Silhouette plus hidden second read | Hero poster or Story cover reads once and stops | Build the subject as one shape; put a detail in the negative space | S→W | PS-01, PS-10, PS-22 | Judge only |

## PLC: placement and direction

| ID | Move | When | How (start value) | Rung | Exemplars | Check |
|---|---|---|---|---|---|---|
| PM-30 | Lead room by crop | Subject faces a tight edge or sits dead centre with motion | Recrop so space opens ahead of the gaze or motion. Never mirror: numbers and names flip | FIX | SP-03, SP-06 | `facing` side has more room; `edge_distance` |
| PM-31 | Crowd as gaze lines | Reaction or goal frame cropped tight | Keep a wider crop so many gazes aim at the subject | S→W | SP-06 | Judge; faces found pointing to subject |
| PM-32 | Sport supplies the geometry | Layout feels arbitrary | Build the frame or transition from the sport's own shape: home plate, bases, track outline | S→W | BF-17, BF-27, BF-03 | Judge only |
| PM-33 | Seam as versus device | Matchup or head-to-head | Split the frame; warm against cool; mark on each side at equal size | C→S | BF-28, BF-19 | `balance` near centre; equal subject areas |
| PM-34 | Radial break pattern | The mark needs impact | Shatter, ripple or fan lines out from the mark, darkest mass at the centre | C→S | BF-23 | `line_orientation` diagonal share up; lines converge on mark |

## DEP: depth

| ID | Move | When | How (start value) | Rung | Exemplars | Check |
|---|---|---|---|---|---|---|
| PM-40 | Four planes | Centred and flat, no depth cue | Foreground occluder or particles, the subject, a set piece, a hazy deep field. Haze lowers contrast with distance | C→S | BF-03, BF-02, BF-28, BF-16 | Contrast falls from foreground to back cells |
| PM-41 | Horizon staging | A calm, large title frame | Low silhouette at the horizon, light behind the mark, calm sky for title and bug, a tiny figure for scale | C→S | BF-02 | `horizon` low; quiet sky cells for type |
| PM-42 | Outlined type as a plane | A figure or car needs a stage | Huge outline-only type behind the subject; light the subject in front | C→S | BF-03 | Subject ΔL* over the type plane |
| PM-43 | Compression and symbol stack | A crest, banner or trophy sits behind the athlete | Tight crop from a long lens or high-res frame; keep the symbol as the second level | S→W | SP-14, SP-07 | Judge; symbol readable at 10% |
| PM-44 | Background-only motion blur | Skating or running frame with a still background | Path blur on the background behind a clean mask; face stays sharp; blur by distance | C→S | SP-10 | Halo check on the mask edge (trap 8 in SP canon) |
| PM-45 | Change the vantage | A new shoot or render is possible | Overhead, floor level, remote, far-side long lens | S→W | SP-02, SP-13, SP-11 | Judge only |

## COL: colour

| ID | Move | When | How (start value) | Rung | Exemplars | Check |
|---|---|---|---|---|---|---|
| PM-50 | One accent over a mono field | Every colour at full strength | Mute the field to neutral or tonal; one saturated hue on the mark and key accents | C→S | BF-07, BF-21, BF-29, BG-08 | `palette` chroma: accent high, rest low |
| PM-51 | Second cue beyond hue | Meaning carried by red vs green | Add shape, arrow or a value step of at least 3:1 `[Infer]` | FIX | BG-18, BG-22 | Deuteranopia view still separates them |
| PM-52 | Fixed medallion | Team colours vary by kit | One container for every logo; flat swatch; test the three lowest-contrast kits before animating | C→S | BG-02, BF-06 | Text contrast ≥ 4.5:1 on each kit |
| PM-53 | Signal colour per game | A series looks like brand paint | One colour per game from a fixed spectrum, off the team palette | S→W | PS-07 | Judge only |
| PM-54 | Stage colour ladder | Tournament rounds | Encode round in a tone (silver to gold) that never changes layout | C→S | BG-10 | Layout boxes identical across rounds |
| PM-55 | Colour-field ground | Hero art on plain ice or floor | Grade the ground to one hue chosen against the jersey; keep contact and cast shadow | S→W | SP-15 | `palette` ground hue opposite jersey |
| PM-56 | Relativity check | Brand colour looks wrong on some grounds | View on light, dark, warm, cool grounds; fix the ground, edge or value, not the swatch (M10) | C→S | BG-12 | Judge across grounds |

## EDG: framing, edges, safe areas

| ID | Move | When | How (start value) | Rung | Exemplars | Check |
|---|---|---|---|---|---|---|
| PM-60 | Safe-box and crop pass | Any 9:16 or cover | Hard box x 120-888, y 288-1248 on 1080x1920; then 4:5 and 3:4 centre crops over the master | FIX | PS-16 | `text_outside_graphics_safe` false; `format_survival` |
| PM-61 | Rebuild vertically | A 16:9 asset must go vertical | Re-stack into a column, raise type, subject upper-middle; never scale the 16:9 down | FIX | PS-23, PS-19 | `subject_capture` in 9:16 crop |
| PM-62 | Lock the anchors | Bug or package redesign | Keep every fixed position and reading order; change type and plate only; test at 10% | FIX | BG-05, BG-01, BG-22 | Box positions match the old package |
| PM-63 | Planned room for type and bug | Hero frame built without its overlays | Comp the real title, bug and lower third on the frame; keep a calm zone where they land | C→S | BF-02, BF-25, SP-22 | `edge_density` low in the type cells |
| PM-64 | Planned split | Portrait plus a line of type | Fix the portrait and type blocks first, then crop to suit; face fills its block | C→S | SP-22, SP-21 | Text box and face box do not overlap |
| PM-65 | Crop past the frame, then resolve small | You need a scale beat and a clean lockup | Open with the mark huge and cropped at the edges; settle at about a quarter of the width in an almost empty field | S→W | BF-25 | Final mark width about 25% |
| PM-66 | Clear the edge fragments | Teammate, stick or heads cut at the border | Recrop past them or clone out; or lean in and make the second figure a full foreground frame | FIX | SP canon trap 6 | `tangent`, `joint_crop` clear |

## GRP and BAL: grouping and balance

| ID | Move | When | How (start value) | Rung | Exemplars | Check |
|---|---|---|---|---|---|---|
| PM-70 | Reserved secondary zone | Records, stats or ads crowd the score | A separate area beside the main block so the main read is never touched | C→S | BG-02, BG-04 | Main block boxes unchanged |
| PM-71 | Shape echo break | Hero and background repeat one silhouette | Change the background shape or offset it (M8) | C→S | M8 | Judge on the black-fill view |
| PM-72 | Steelyard check | Frame feels lopsided with no intent | Name the stem (M5); balance a big near mass with a small far one, not with a centred mass | C→S | M5 | `balance` centroid; judge |

## Systems (a package, a season, a roster)

| ID | Move | When | How (start value) | Rung | Exemplars | Check |
|---|---|---|---|---|---|---|
| PM-80 | Worst case first | Leagues, multi-team packages | Build for the longest name, the worst logo and the most teams before the hero shot | C→S | BG-09, BF-06 | Longest-name test passes safe and contrast |
| PM-81 | Constant framing, changing material | One system, many venues or teams | Fix the layout and motion logic; vary texture and colour per place | S→W | BF-12, BF-06 | Layout boxes identical across members |
| PM-82 | Two-tier output | A season of posts | Locked template for volume; one hand-built piece per week | C→S | PS-21, PS-18 | Judge only |
| PM-83 | Toolkit-first open | A launch film must also feed bumpers | Design every scene as a cut-out element with its own start and end | C→S | BG-11, BF-09, BF-17 | Each scene holds as a still |
| PM-84 | Roster template | A set of media-day portraits | One light, one crop height, one grade; vary expression only | C→S | SP-19, SP-23 | Face height share equal within 5% `[Infer]` |
| PM-85 | Sport skin as the field | The frame feels generic | Use the real surface (leather, mesh, ice, marble) as the field, with raking light; let the mark share it | C→S | BF-22, BF-25, BF-23, BF-20 | Judge only |

## MOT: motion (stills of a sequence)

Timing and easing go to `motion-critique`. These are composition moves across holds.

| ID | Move | When | How (start value) | Rung | Exemplars | Check |
|---|---|---|---|---|---|---|
| PM-90 | Bug leaves the play | Fixed play window | Fade or slide the bug out at the snap (6 to 10 frames `[Infer]`), restore on the dead ball | S→W | BG-06 | Hold at the snap shows no bug |
| PM-91 | Hold one component back | Open or promo peaks too early | Graph intensity and the seven components (M3); keep one at affinity until the climax | S→W | M3 | Contact sheet: the held component changes only at the peak |
| PM-92 | Two-frame beat | A Story set explains everything at once | Frame 1 image only; frame 2 one fact | C→S | PS-23 | Text count per frame |
| PM-93 | Derive motion from the sport | Package motion feels generic | Watch footage; write four behaviours (speed, inertia, impact, agility); use only those | S→W | BG-24 | Judge only |
| PM-94 | Test at delivery scale | Motion tuned on one monitor | Review at the largest and smallest delivery size | FIX | BG-27 | Judge at both sizes |

## Traps when pushing

- One move per critique. Two pushes at once hide which one worked.
- A push must not break a Keep item. If it does, pick the next row.
- Do not credit composition for the event itself (Leifer, SP-01). A great moment with average composition is still average composition.
- A deliberate low-key or high-key range is a choice, not a VAL failure (M7 caution).
- Judge-only rows have no metric. In Improve mode they still go through the blind both-order judge.
