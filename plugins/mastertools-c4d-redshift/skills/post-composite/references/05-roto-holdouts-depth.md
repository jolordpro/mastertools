# 05: Roto, holdouts and depth

## Tools (2026) [doc]
- **AE Object Matte** (native, 26.2+, Apr 2026): one-click AI subject selection with propagation. The classic Roto Brush now lives inside it as "Quick Selection", alongside the Selection Brush and Refine Edge. Older Roto Brush versions can still be selected in Effect Controls. Works in the Layer panel only. 26.5 caches propagation to disk. 26.2.1 fixed aerender with Object Matte. **First pass.**
- **Mocha Pro 2026** (Boris FX, paid): planar-tracked spline roto, Matte Refine ML (hair and motion-blur edges), Object Brush ML / Matte Assist ML. Use it to lock frames where the AI matte chatters.
- **AE Mask Tracker** (26.3: up to 5× faster, can start from the Timeline panel).
- **Boris FX Silhouette** (paid): hero roto and paint.
- **Red Giant Depth Generator** (2026.1+, AE-only): local AI monocular depth. Outputs grayscale depth (MP4 or PNG sequence through Render to Comp) that feeds Bokeh and Particular's ZBuffer. Known issue: Render to Comp can crash AE on completion (2027.0.0 notes).
- Red Giant **Primatte Keyer**: chroma keying only. Useless without a backing color.
- AE **Unmult** (26.0): for stock emissive elements on black. Not for EXRs that have real alpha.

## Subject holdout procedure
1. Run Object Matte on the **degrained** plate. Click the subject on a middle frame and propagate both ways.
2. Review the soft-edge frames at 200%: feet, swinging limbs, hair against bright backgrounds.
3. Fix problem frames in Mocha Pro (planar splines per body part) or with the Selection Brush.
4. Motion-blurred edges: either Refine Edge / Matte Refine ML with decontamination, **or** roto the sharp core and add vector motion blur to the matte (e.g. RSMB driven by plate motion).
5. Export a **hard matte** (core) and a **soft matte** (with blurred edge).
6. When the CG is behind the subject, CG alpha × (1 − soft matte). When it's in front, no holdout, but add CG light onto the subject (env-light on the proxy, or Scene Light).
7. Backlit silhouettes: when an emitter passes behind, add a slight bright fringe (reverse light wrap, 04).

## Depth
- For the CG: Redshift Depth AOV (full float, unfiltered).
- For the plate: depth from the **proxy geometry render** for the environment, plus the subject's depth (proxy, or AI Depth Generator) merged in through the subject matte.
- AI depth is relative, non-metric and can flicker. Use it only where no proxy exists.

## Do / Don't
- DO QC mattes over bright red and with exaggerated exposure, **in motion**. Chatter is a worse tell than slightly soft edges.
- DON'T use a binary hard matte on a motion-blurred subject. It reads as a cut-out.
