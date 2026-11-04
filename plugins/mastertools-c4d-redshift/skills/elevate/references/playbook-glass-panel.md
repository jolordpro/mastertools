# PB-GLASS: glass panel

Panels are judged by their edges and by what shows through them.

## Check order
1. **Shading model:** thin or solid, chosen deliberately (MAT-08). Settings → RS.
2. **Edges:** the bevel catches a highlight (BEV-01, BEV-03); a rim separates the panel from the background (LGT-01).
3. **Behind the glass:** backplate value contrast so the refraction reads (CMP-03, CLR-01).
4. **Reflections:** designed cards or strips, not an HDRI smear (LGT-04, LGT-05).
5. **Type on or behind the glass:** hierarchy and legibility through refraction and blur (TYP-01, TYP-07).
6. **Finish:** grain, plus light wrap on comp layers (FIN-01, FIN-04).

Load `materials-texture.md` and `lighting.md`. Add `typography.md` if type sits on the panel.

## Likely failure modes (A: hypotheses to confirm at the dry run)
- The panel face is brighter than its edges, so it reads as a gray card.
- Refraction over a flat background shows nothing. Add structure behind it (CMP-03).
- Frosted glass hides the type. Raise the contrast behind the text, or move the type in front.

## Gold examples needed
At least 2: a clear panel over an environment, and a frosted panel with type.
