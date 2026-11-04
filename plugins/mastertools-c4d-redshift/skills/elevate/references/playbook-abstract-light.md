# PB-ABSTRACT: abstract light and line art

Strands, ribbons, waveforms, fans of light, particles, type laid on paths. No logo or product to light: the light *is* the subject.
Added 2026-10-23 (DRAFT) from an abstract-light project's rounds (BW-3D in `sources.md`): 9 delivery rounds, ~150 draft stills, art-director notes.

## Check order
1. **Value plan first.** Dark share and one light event (CLR-01, CLR-14). The art director's references ran 70-95% black with one bright edge,
   streak or convergence point. Mid-key gold everywhere was the most common miss.
2. **Colour along the length.** One colour end to end reads flat; a ramp (hot core, body, darker tails) reads as depth (CLR-10).
   Give each strand its own change point or the shared cut shows as a seam; in a mirror floor even staggered steps stair-step.
3. **Brand colour through the view.** Check the hero colour as displayed, not as typed (CLR-12). Glow and dim edges drift
   hue under ACES: judge the full-strength pixels, then the halo separately.
4. **Depth of field and macro physics** (CAM-14). Close-ups wash out into colour fog when the aperture is wider than the field.
5. **Shape quality.** Curves round, never pointy or creased; viewing straight down a curve flattens arches into walls (re-angle 3/4).
6. **Set consistency** across frames of one package: hue, black level, glow (CLR-13, `scripts/set_hue.py`).
7. **Thumbnail and title room.** Hand the placement pass to `composition` once the light works.

Load `color.md` and `camera-lens.md`. Add `composition.md` for the title room.

## Likely failure modes (seen, not hypotheses)
- Wall-to-wall gold: no dark field, no light event (fix: pull back or go longer, thin the count, dim the non-hero lines).
- Gold reads khaki or orange: the brand colour was fed in before the view transform (CLR-12).
- Macro fog: wide aperture at close focus (CAM-14).
- Type on paths that tumbles or repeats reads as a caption or noise; ordered tracked caps read as design.

## Gold examples needed
At least 2: a wide light event (fan or horizon) and a macro with type or particles. The user's own corrected rounds
are the first candidates.
