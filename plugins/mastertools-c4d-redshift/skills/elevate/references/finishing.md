# Finishing (FIN)

Taught in: SOM VFX for Motion (Mark Christiansen) · SCAD VFX 715, 758, 420, 437 · Gnomon Art of Compositing.

## Read
- **C:** Highlight roll-off; where glow sits; light-wrap edges.
- **X:** Grain structure and banding can't be judged in 8-bit previews; ask for the delivered file or a 16-bit frame.
- **R:** Available AOVs; the AE stack (grade, glow, grain); bit depth; color settings.

## Moves
| ID | If you see | Try | Why | Lbl | Src | Rung | → |
|---|---|---|---|---|---|---|---|
| FIN-01 | Clean CG with no unifying texture | Matched, subtle grain over the final comp (32 bpc: see AE tools) | Grain unifies CG | P | BRK:13; WRT:14.8; PC-HARM | C→S | AE |
| FIN-02 | Glow on everything | Glow only on true hot sources, with a high threshold | Bloom should behave like light | A | — | FIX | AE |
| FIN-03 | Highlights clip harshly | Roll them off in the grade; halation on the hottest sources | A film-like response | A | — | S→W | — |
| FIN-04 | A comp element looks pasted on | Light wrap (no native AE effect: see AE tools); match blacks and color | Integration | P | BRK:13; WRT:14.3; PC-HARM | FIX | AE |
| FIN-05 | No depth haze | Let the depth pass drive subtle haze with distance | Atmospheric haze | P | WRT:14.6 | C→S | RS |
| FIN-06 | Banding in gradients | Higher bit depth; grain or dither before delivery | Banding is a bit-depth artifact | P | WRT:1.8.1.1 | FIX | SD |
| FIN-07 | Grade drifts | Lock a reference frame; match each shot to it | Scene continuity | P | BRK | C→S | — |
| FIN-08 | Lens effects stacked from several plugins | One lens character, applied consistently | Restraint reads as intent | A | — | FIX | — |
| FIN-09 | Hero looks flat after the grade | Dodge and burn: lift the hero's highlights, deepen the darks around it | Guides the eye | P | CB | C→S | AE |
| FIN-10 | Missing passes for comp control | Render light groups and depth for finishing | Control without re-rendering | P | BIR | C→S | RS |
| FIN-11 | Clean pipeline, still a CG look | Color-managed, band-free, per-shot matched grain: the studio standard | Top studios credit a color role | A | ELASTIC-NHL | S→W | RS |

## AE tools (checked 2026-10-27; PC-HARM)
- **Light wrap:** AE has no native light-wrap effect. Adobe's feature request for one is still open. Use Supercomp **Light Wrap**
  (part of Maxon One), or build it by hand: blurred background × a 2–8 px edge band × a brightness gate (background > 0.2),
  added (screen or plus) in linear. Turn it off where the layer meets a surface it sits on.
- **Grain:** Add Grain, Match Grain and Remove Grain are 8/16 bpc only. They drop a 32-bpc chain on that layer. In 32 bpc, use Noise
  or Magic Bullet Renoiser. Renoiser's bit depth is [verify].

## Delivery
- ProRes 4444: check grain and dither on the delivered file.
- Broadcast-legal levels go to SD.
