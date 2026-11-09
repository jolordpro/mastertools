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
| BEV-12 | Logo's main mass reads flat or uniformly puffy; no ridges | Shape the mass as a roof: Extrude, cap bevel type Curve, size ~9% of the mass width, depth ~0.36 (tune on the real shape with its holes), on a wall about half the ridge height; remesh to even quads after | Straight ramps meeting at ridges give a crisp light line along each region's spine; a uniform puff gives one blurry highlight | T | TD-1105 §2 (M+T: profile within 0.2 units) | C→S | — |
| BEV-13 | Seams between stacked colour layers show dark lines, false rounded edges or flicker | Run a thin metal strip (Sweep of a rectangle ~1.1 x 7.9 at this scale) along every seam, top ~0.3 above the neighbouring faces | Maxon: hidden or near-coplanar polygons make Round Corners draw false edges; fix by deleting them or a boolean. The strip is this scene's workaround: it covers the seam and adds the edge highlight | T | MAXON-RC (cause, V); TD-1105 §2 (strip) | FIX | — |
| BEV-14 | Inset parts look stuck on top of the mass | Sit them about 7 units under the mass's wall top (scale-relative: ~1.3% of logo width), flat tops, Round Corners for the edge glint | Parts set into valleys read carved; parts on top read as stickers | T | TD-1105 §2 | C→S | — |
| BEV-15 | Backplate edge reads soft and toy-like | One-segment Round bevel (a chamfer) on the backplate, smooth Curve bevels only on hero parts | A hard chamfer frames the soft hero; soft-on-soft muddies the silhouette | T | TD-1105 §2 | C→S | — |
