# Lighting (LGT)

Taught in: SOM Lights, Camera, Render m03 · SCAD VFX 752, MOME 758, MOME 360 · Gnomon Lighting & Rendering 1–4 · Gnomon Workshop Vallecilla Vol. 1.

## Read
- **F:** Key direction agrees across shading and shadows; the silhouette separates from the background; the brightest value sits at the focus; the shadow side has shape.
- **C:** Specular shapes on metal and glass (designed cards, or an HDRI smear).
- **R:** Light count, type and size; key angle against the camera axis; key:fill:rim intensity; color temperatures; light-linking; reflection-only cards; what the HDRI is doing; volumes.

## Moves
| ID | If you see | Try | Why | Lbl | Src | Rung | → |
|---|---|---|---|---|---|---|---|
| LGT-01 | Hero edge merges with bg | Rim/kicker opposite the key; check in grayscale | Separation comes from edge value | P | BRN:13 | C→S | RS |
| LGT-02 | Key near the camera axis; flat form | Move the key off-axis/upstage; let fill shape the shadow side | Flat front light kills form | P | BRN:13 | C→S | RS |
| LGT-03 | Lights at similar strength | Dominant key, lower fill, rim as an accent | Hierarchy directs the eye | P | BIR:5 | C→S | RS |
| LGT-04 | Metal reads gray or murky | Light what it reflects: camera-invisible cards or strips along the form | Metal shows its surroundings | P | GSG-PL | C→S | RS |
| LGT-05 | Generic HDRI look on the hero | HDRI as ambient only; a designed key and cards place the hero highlights | Highlight placement should be designed | P | GSG-PL | S→W | RS |
| LGT-06 | Shadows from several directions | One key direction; demote the rivals | Conflicting shadows read as CG | P | BIR:1; BIR:3 | FIX | RS |
| LGT-07 | Lights with no source in an environment | Tie key and accents to world sources: rigs, ribbon boards, scoreboard | Motivation sells the space | P | BIR:1 | C→S | — |
| LGT-08 | Neutral white everywhere | Warm/cool split, or team color in the rim only | Temperature contrast adds depth | P | GUR | C→S | RS |
| LGT-09 | No depth cue | Atmosphere that thickens with distance; lower background contrast | Atmospheric perspective | P | GUR; BRN:2 | C→S | RS |
| LGT-10 | Shadow edges wrong for the mood | Larger source for softer shadows, smaller for harder | Source size relative to distance | D | BRN:13 | C→S | RS |
| LGT-11 | Volumetric rays with no source | Reveal the source or remove the rays | Volumes need motivation | P | BIR:4 | FIX | RS |
| LGT-12 | Shadow side crushed | Bounce or fill, or negative fill chosen on purpose | Keep detail in key shadows | P | BRN:13 | C→S | RS |
| LGT-13 | Sweep wanders | One glint per beat, travelling the bevel, landing on the settle | Light as the reveal | A | IF-CBS | S→W | RS |
| LGT-14 | Solid but static highlights on holds | Drift one card or light slowly through the hold | Live speculars read premium | A | — | S→W | RS |
| LGT-15 | Arena lit evenly from nowhere | Put practicals in frame (LED ribbons, overhead rig) that also motivate the key | Visible, motivated sources | A | — | S→W | — |
| LGT-16 | Soft key still leaves a hot spot on glossy type or a face | Book light: aim the key into a large white card hidden from camera so only its bounce lights the hero (GI on) | Double diffusion wraps softly but keeps one direction | P | THY:4 | C→S | RS |
| LGT-17 | Bright, high-key frame with no shape | One large soft source from above or one side; a black card hidden from camera on the shadow side as negative fill; keep its spill off the background | High key without losing contrast | P | THY:8; THY:9 | C→S | RS |
| LGT-18 | Background is a flat, empty wall or void | Hard light through a cutout (window frame, truss, grille) into thin haze, so shaped shafts cross behind the hero | Shaped shafts add depth and a motivated source (keep the cutout readable: LGT-11) | P | THY:7 | S→W | RS |
| LGT-19 | Hype shot lit clean but flat in energy | Soft key on the hero, a little off-axis so the face keeps shape (LGT-02); two hard backlights in frame aimed at camera, in light haze, flaring in post | Visible sources and flare add energy; hype only, not clean brand frames | P | THY:5 | S→W | RS |
| LGT-20 | A light setup or HDRI about to be built from scratch | When the user has an asset library with light rigs or HDRIs (for example Greyscalegorilla studio HDRIs and Light Kit Pro rigs), search it first with the user's own library tools. Light Kit Pro rigs need the GSG Light Kit Pro plugin in the C4D that runs them (untested headless: check the rig loads whole). The library is the start: LGT-04 and LGT-05 still place the hero highlights. Headless renders of library HDRIs: as MAT-18 (pre-convert maps, then confirm the first frame) | A tested rig starts closer to the look and saves build time | A | — | C→S | — |

## Sports notes
- Team colors work as rim or accent, not as the key.
- The brightest moment lands on the mark at the resolve.
- Rink boards and turf act as reflectors.
- Glass is judged at its edges (see PB-GLASS).
- Named setups by job: book light (LGT-16) or soft source with negative fill (LGT-17) for brand resolves and athlete portraits; flaring backlights (LGT-19) for player intros and hype opens.
