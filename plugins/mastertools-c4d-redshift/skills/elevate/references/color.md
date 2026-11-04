# Color (CLR)

Taught in: SOM Design Bootcamp (Mike Frederick) · SOM 30 Days of AE, day 14 (Korenman) · SCAD MOME 720, VFX 752 · Gnomon Visual Structure.

## Read
- **F:** Squint test for 3–5 value groups; where the saturation sits; light versus shadow temperature.
- **C:** Buzzing edges between saturated hues.
- **R:** Albedo values (brand colors entered at full value are a flag); light colors; the AE grade stack; project color settings (→ RS).

## Moves
| ID | If you see | Try | Why | Lbl | Src | Rung | → |
|---|---|---|---|---|---|---|---|
| CLR-01 | Mid-gray values; nothing pops | Put the value extremes at the focus; compress the background range | Value carries contrast | P | SOM-VAL | C→S | — |
| CLR-02 | A saturated rainbow | One dominant family plus one accent; desaturate the rest | An accent pulls the eye | P | GUR | C→S | — |
| CLR-03 | Brand color right on flat art, wrong once lit | Tune albedo and light until the rendered mark reads on-brand | Color is relative to light and surroundings | P | ALB:IV | FIX | RS |
| CLR-04 | Team colors at full strength everywhere | Hero color on the mark and accents; tints and shades in the environment | Hue affinity, saturation contrast | P | BLK:6 | C→S | — |
| CLR-05 | Light and shadow at the same temperature | Warm light with cool shadow (or the reverse), consistently | Reads as natural light | P | GUR | C→S | RS |
| CLR-06 | Adjacent hues buzz | A value step or a neutral between them, or shift one hue | Vibrating edges hurt reading | P | KOR | FIX | — |
| CLR-07 | Grade drifts from shot to shot | Lock a reference frame; match blacks and highlights first | Package consistency | P | BRK | C→S | — |
| CLR-08 | Hot spots tint the frame | Roll hot sources toward white with a tinted halo | Highlights desaturate as they brighten | P | GUR | S→W | — |
| CLR-09 | Muddy dark palette | Lift accent values; keep the darks neutral | Dark palettes need value anchors | A | — | C→S | — |
| CLR-10 | Colors picked element by element | Build from one base color plus a harmony rule; test in grayscale | A system beats one-off picks | P | KOR | C→S | — |
| CLR-11 | Correct but flat palette | Save one controlled complementary accent for the resolve | A contrast spike at the climax | A | BLK:2 | S→W | — |
| CLR-12 | Brand colour right as a number, wrong on screen (khaki, orange) | Solve the colour through the display view (ACES): feed the value that *shows* as the brand colour. Lit metal needs only part of that correction; dim glow needs its own solve at low level | The view's tone curve dulls saturated colour and its toe pushes dim colours red | D | KIT-CP; BW-3D | FIX | RS |
| CLR-13 | Frames of one package drift in hue | Measure median hue of the bright, saturated pixels per frame against a reference frame (`scripts/set_hue.py`); bring each within 3 deg | "Doesn't match" becomes a number; catches overshoot too | P | BRK; BW-3D | FIX | — |
| CLR-14 | Dark frame, but nothing reads as the light | Make one element at least two stops above everything else (one light event); dim or thin the rest | A dark field only works with a clear source; dark-and-dim reads as murky | P | SOM-VAL; BW-3D | C→S | — |

## Notes
- A network's house looks live in the user's own style guides, not here.
- In dark arenas, the mark keeps the value extreme.
