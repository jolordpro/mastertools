# 15: Compositing glossary

Research snapshot: **2026-10-27**. Plain-word definitions, with each app's name for the same thing. App key: **AE** After Effects · **PS** Photoshop · **Nuke** Foundry Nuke (the industry's reference vocabulary) · **C4D/RS** Cinema 4D and Redshift.

Names for C4D/RS and Photoshop are pointers only; those toolboxes (areas 4 and 5) aren't researched yet. [verify] marks those.

## 0. Words that clash between skills
Say which meaning you mean. These four cause real mistakes.

| Word | Meanings |
|---|---|
| **Plate** | Here: the live-action footage the comp is built on. In the composition skill: a type backing panel behind text |
| **Tracking** | Here: following motion in footage. In typography: letter spacing. In 12 both appear; write "motion track" and "letter tracking" |
| **Key** | Here: pulling a matte by color (keying). In lighting: the key light, the main source. Write "keying" and "key light" |
| **Occlusion** | Here: something in front hides the graphic (a holdout). In lighting and depth: ambient occlusion, or occlusion as a depth cue. Write "holdout" for the comp meaning |
| Mask | AE: a vector path on a layer. PS: a raster layer mask. Nuke: an input that limits a node. All limit where something applies |
| Screen | A blend mode (§4), or the colored backing (green screen) |
| Add | A blend mode (plus), or AE's default mask mode (masks combine) |
| Matte | Any image that defines transparency. In C4D/RS, a "matte" object is a holdout that renders as a hole [verify] |

## 1. Mattes
| Term | Meaning · names |
|---|---|
| **Matte** | A grayscale image that says where a layer is opaque (white) or clear (black). AE: track matte, Set Matte. Nuke: matte or mask input |
| **Alpha** | The matte stored as a layer's fourth channel. AE, Nuke, PS: alpha channel |
| **Garbage matte** | A rough shape that throws away everything that is surely not foreground (rigs, stands, screen edges). Keylight: **Outside Mask**. AE: a loose Subtract mask |
| **Core matte** | A hard, choked inside matte that makes the solid middle of the subject fully opaque. Keylight: **Inside Mask**. Supercomp: Core Matte |
| **Edge matte** | The thin soft band of the key, worked on separately for hair and blur, then combined with the core |
| **Holdout matte** | A matte that cuts a hole in something behind a foreground object, so the object stays in front. Used for CG behind people (05) and graphics behind players (13). C4D/RS: matte or holdout options [verify] |
| **Traveling matte** | A matte that moves or changes over time. AE: any animated track matte |
| **Luma matte** | Transparency from brightness, not alpha. AE: Luma Matte |
| **Inverted matte** | Black and white swapped. AE: Inverted toggle |

## 2. Keying (green and blue screen)
| Term | Meaning · names |
|---|---|
| **Keying** | Making a matte from a color or brightness. AE: Keylight, Linear Color Key and others (13) |
| **Key color / screen color** | The backing color to remove. Keylight: Screen Colour ([Foundry](https://learn.foundry.com/nuke/content/reference_guide/keyer_nodes/keylight.html)) |
| **Screen gain** | How much of the screen color gets removed. "Increasing this value keys more" (Keylight) |
| **Screen balance** | Keylight's balance point. Typical: about 0.95 for blue screens, 0.5 for green (Foundry) |
| **Clip black / clip white** | Cutoffs that force near-black matte values to 0 and near-white to 1. Cleans the matte; too much hardens the edge |
| **Screen matte** | The raw matte from the screen color, before core and garbage mattes (Keylight) |
| **Spill** | Screen color bounced onto the subject: green on skin, hair, edges |
| **Despill** | Removing spill. Common method: limit green to no more than the larger of red and blue (FaceSizer notes). It also shifts skin and yellows, so check them. Keylight: Despill Bias |
| **Clean plate** | The same shot with no subject: an empty screen or set. Used for Difference Matte, screen correction and cleanup |
| **Screen correction** | Evening out an unevenly lit screen before keying, often using the clean plate |
| **Difference matte** | A matte from what differs between the shot and its clean plate. Locked camera only. AE: Difference Matte |

## 3. Alpha and edges
| Term | Meaning · names |
|---|---|
| **Premultiplied** | Color already multiplied by alpha, so edge pixels carry the background color (usually black). AE Interpret Footage: Premultiplied – Matted With Color. Nuke: Premult |
| **Straight (unpremultiplied)** | Color stored apart from alpha. More accurate color; fewer programs read it right. AE: Straight – Unmatted. Nuke: Unpremult |
| **Wrong interpretation** | Premultiplied read as straight gives a dark halo; the reverse gives bright fringes ([Adobe manual](https://www.manualsdir.com/manuals/753844/adobe-after-effects.html?page=98)) |
| **Grade unpremultiplied** | [rule] Unpremultiply before a color change and premultiply after, or edges shift. Nuke does this explicitly |
| **Choke** | Shrink a matte's edge inward. AE: Simple Choker (positive), Matte Choker. Opposite: **spread** (negative) |
| **Erode** | Nuke's name for choking by a pixel radius. AE: Minimax (Minimum). Supercomp: Edge Erode |
| **Feather** | Soften an edge by blurring it. AE Mask Feather is Gaussian (14) |
| **Edge decontamination** | Replacing the background color left in semi-clear edge pixels with nearby foreground color. AE: Refine Soft Matte > Decontaminate Edge Colors. PS: Select and Mask > Decontaminate Colors [verify] |
| **Light wrap** | Background light bleeding a few pixels over the foreground edge. Recipe in 11 §8. AE has no native tool; Supercomp has one (04) |
| **Edge blend** | Blending a layer's edge pixels with what's behind. Supercomp: Edge Blend |
| **Unmult** | Building alpha from brightness, for elements shot on black. Not the same as unpremultiplying. AE: Unmult (26.0) |

## 4. Comp operations
Formulas from [Foundry Merge](https://learn.foundry.com/nuke/content/reference_guide/merge_nodes/merge.html) [doc]. A, B = color of the top and bottom image; a, b = their alphas.

| Operation | Meaning · formula · names |
|---|---|
| **Over** | A on top of B by A's alpha. `A + B(1−a)`. AE: Normal mode, layer order. PS: Normal |
| **Under** | B on top of A. `A(1−b) + B`. AE: move the layer below |
| **Plus** | Adds light. `A + B`; can exceed 1.0. AE: **Add**. PS: Linear Dodge (Add) |
| **Screen** | `A + B − AB` for 0–1 values. Nuke switches to `max(A,B)` above 1; AE's handling above 1 is unconfirmed (14 §2). Use Plus for light |
| **Multiply** | `AB`. Darkens; for shadows and printed color. AE, PS: Multiply |
| **In / Out** | A only inside B's alpha (`Ab`), or only outside (`A(1−b)`). AE: track matte, inverted track matte |
| **Atop** | A shown only where B is. AE: Preserve Underlying Transparency. PS: clipping mask |
| **Stencil / Mask** | B shown outside / inside A's alpha. AE: Silhouette / Stencil blend modes |
| **Difference** | `abs(A−B)`. Alignment and QC: matched pixels go black |
| **Merge** | Nuke's node that does all of the above. AE has no node; the layer stack is a chain of Overs |

## 5. Footage and shot work
| Term | Meaning |
|---|---|
| **Plate** | The live-action footage. **BG / MG / FG plate** = background, midground, foreground pieces |
| **Element** | Any separate piece added to the comp: a CG render, a graphic, smoke, a keyed person |
| **Matchmove** | Rebuilding the real camera's move so CG or graphics follow it |
| **Track** | Following a feature or plane over time: point, planar (Mocha), or 3D (camera solve) |
| **Solve** | The computed 3D camera (and points) from a track. Its quality reads as average error in px |
| **Corner pin** | Mapping a flat image onto four tracked corners. AE: Corner Pin, CC Power Pin |
| **Stabilize** | Removing camera motion, often reversibly so work can be added then the shake put back (12 §4) |
| **Roto** | Drawing animated shapes by hand to make a matte. AE: masks, Object Matte. Mocha: splines |
| **Paint / cleanup** | Removing unwanted things: rigs, marks, wires. AE: Clone Stamp, Content-Aware Fill (14) |
| **Degrain / regrain** | Remove grain for clean work, then add matched grain back at the end (06) |
| **Overscan** | Rendering past the frame edge so distortion and moves don't expose empty pixels (02) |
| **Proxy** | A lighter stand-in file for speed |

## 6. Color
| Term | Meaning |
|---|---|
| **Scene-referred** | Values say how much light reached the camera ([OpenEXR](https://openexr.com/en/latest/SceneLinear.html)). Also "input-referred" |
| **Display-referred** | Values say how much light the screen should emit. Also "output-referred" (OpenEXR) |
| **Scene-linear** | Scene-referred and linear, scaled so an 18% gray card reads 0.18 (OpenEXR). Light adds correctly here. ACEScg is one (01) |
| **Display-linear** | Linear light measured from a display. Strategy A works in it (01) ([OCIO](https://opencolorio.readthedocs.io/en/latest/guides/authoring/colorspaces.html)) |
| **Log** | Scene-referred, roughly proportional to the log of brightness: ACEScct, ARRI LogC (OCIO) |
| **Legal (narrow) range** | Broadcast video uses 16–235 in 8-bit and 64–940 in 10-bit for black to white (EBU R 103's "Expected Range"). **Full range** is 0–255 |
| **Tolerance** | EBU R 103 allows ±5% beyond the legal range, about 5–246 in 8-bit ([EBU R 103](https://tech.ebu.ch/publications/r103); figures via a QC vendor summary, PDF not opened). [verify] Delivery rules belong to area 9 |
| **Superwhites / sub-blacks** | Values above legal white or below legal black. Keep them in 32 bpc; never clamp the plate (01) |
| **Linear blending** | Mixing in linear light, so blurs and glows behave like real light. AE: linearized working space, or Blend Colors Using 1.0 Gamma |
| **Over-range** | Values above 1.0. Exist only in 32-bpc (float) work |
