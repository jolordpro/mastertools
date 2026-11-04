# Bevels and edges (BEV)

Bevel values are geometry, not render settings. Test them [T], and never put them in the redshift ledger.
Taught in: SOM R21 Caps & Bevels (EJ Hassenfratz) · GSG Rounded Corners · SCAD MOME 713. No curriculum teaches bevel scale as a design rule.

## Read
- **C:** An edge highlight that is present and wider than a pixel at delivery size; pinching at corners; layer separation on marks.
- **R:** Extrude depth; caps; bevel size, segments, profile and miter; phong angle; whether a rounded-corner shader is in use.

## Moves
| ID | If you see | Try | Why | Lbl | Src | Rung | → |
|---|---|---|---|---|---|---|---|
| BEV-01 | Edge highlight hairline or missing | Widen the bevel until the highlight clearly reads at delivery size | Rounded bevels catch light on reflective materials | P | SOM-BEV | FIX | — |
| BEV-02 | Same bevel on every edge | A structural bevel on the silhouette, small catch bevels on secondary edges; start from macro 2–5%, meso 0.5–2%, micro 0.1–0.5% of object size | Reads as manufactured, not procedural | P/T | NOV | C→S | — |
| BEV-03 | Rounded-corner shader on a hero close-up | Model the bevel; keep the shader for distant edges | The shader doesn't change the silhouette | P | NOV | C→S | RS |
| BEV-04 | Pinching at multi-edge corners | Change the miter or corner mode; test under a bright area light | Clean highlights need clean corners | P | NOV | FIX | — |
| BEV-05 | Layers of a mark merge | Give each layer its own extrusion depth and bevel profile so each catches its own highlight | Layered marks stay readable at distance | A | — | S→W | — |
| BEV-06 | Badge or engraved look reads flat | Stepped (stair) bevel profile | The profile carries character | P | SOM-BEV | S→W | — |
| BEV-07 | Bevel inflated or bubbly | A smaller size, or a chamfer instead of a full round | Over-rounding reads soft | A | — | FIX | — |
| BEV-08 | Fine details smeared | A smaller bevel on small details, or model them separately | Bevels eat thin strokes first | P | — | FIX | — |
| BEV-09 | Thin extrusion reads like cardboard | More depth, or a backplate or ring so the sides catch light; corporate marks may want modest depth, so judge per brand | The sides give the light something to hit | A | NOV | C→S | — |
| BEV-10 | Chrome type in a thin weight | A wider, heavier weight | More surface for glints | P | ADB-REF | C→S | — |
| BEV-11 | Hero's outer edge or side band facing camera reads raw: hard corner, broken highlight, no finish | A polished piped edge: rounded welt with one continuous crest highlight, crisp groove where it meets the face, optional fine seam at constant offset (reference photos in the user's overlay, when present) | Art director's note: "these kinds of polished details are important" when a surface faces camera in a hero shot | A | AD-1028 | C→S | RS |
