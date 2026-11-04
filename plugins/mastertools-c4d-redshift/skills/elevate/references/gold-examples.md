# Gold examples

**Why:** in UI critique, few-shot examples chosen by task and visual similarity, combined with visual prompting, improved LLM feedback by 55% over zero-shot (UICRIT). Targeted selection beat random selection. Transfer to 3D motion is plausible but unproven; the dry run tests it.

## Rules
- **Author:** the user or a teammate, writing from real scenes in their own work. An AI draft isn't gold until the user edits it.
- **Set size:** the v1 minimum is 6 (2 × PB-LOGO, 2 × PB-GLASS, 2 × AE type piece). Target 8–12.
- **Storage:** the user's overlay, `~/.claude/overlays/elevate/examples/gold/<shot-type>-<nn>.md`, when present; else `examples/gold/<shot-type>-<nn>.md`. Keep the marked frames beside it, referenced by filename. Gold examples are optional, and this skill ships with none.
- **Selection at runtime:** 2–4 examples. Match shot type first, then the dimensions in play. Never random.

## Template
```
---
id: logo-01
shot_type: PB-LOGO
dimensions: [BEV, LGT, MOT]
app: C4D
rung_before: {LGT: C, BEV: C, MOT: S}
---
Read: one line on what the piece is and where it sits.
Notes (ranked by visual payoff, max 5):
1. [F2·B3] Diagnosis → Why → Try (move ID) → Hand-off → Rung lifted
Keep: what's working (1–2 lines).
After: what changed in the revision, if known.
```

## Format illustration (NOT gold)
1. [F3·C2] The ring and the inner field merge. Both carry the same bevel and roughness, so one highlight spans both.
   - **Why:** layered marks need a separate catch per layer.
   - **Try:** a deeper extrusion and a stepped profile on the ring (BEV-05, BEV-06), plus a roughness split between the layers.
   - **Hand-off:** RS for the material values.
   - **Rung:** C→S.
