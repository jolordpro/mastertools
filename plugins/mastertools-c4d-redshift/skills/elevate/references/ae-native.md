# After Effects native (AE)

Sourcing is thin here. Video Copilot, Ben Marriott, Jake in Motion and ECAbrams haven't been reviewed yet (open).
Taught in: SOM Animation Bootcamp, Advanced Motion Methods, VFX for Motion.

## Read
- **R:** Effect matchNames and key parameters; blend modes; bit depth; 3D renderer; text animators.

## Moves
| ID | If you see | Try | Why | Lbl | Src | Rung | → |
|---|---|---|---|---|---|---|---|
| AE-01 | Default Glow look | A stacked, thresholded glow at restrained intensity | Defaults read as stock | P | — | C→S | AE |
| AE-02 | Vector and CG layers don't sit together | One grain pass over everything, plus subtle light wrap (no native light wrap; native grain stops at 16 bpc: see `finishing.md` › AE tools) | Shared texture and light | P | BRK:13; WRT:14; PC-HARM | C→S | AE |
| AE-03 | Linear keys on type | Spacing set in the graph editor | Spacing carries weight | P | WIL | FIX | AE |
| AE-04 | 8-bit gradient banding | 16 or 32 bpc; dither before delivery | A bit-depth artifact | P | WRT:1.8.1.1 | FIX | SD |
| AE-05 | Stock Bevel & Emboss standing in for 3D | Real 3D (C4D or AE 3D), or a crafted multi-layer bevel | Stock styles read cheap | A | — | C→S | — |
| AE-06 | Reflective type with no light motion | Animate a glint pass across the type, on the beat | The glint as a reveal | P | ADB-REF | C→S | AE |
| AE-07 | Uneven shape-layer strokes | Consistent weights; round joins and caps on curves | Vector craft | A | — | FIX | — |
