# Vision protocol

Pixels are /elevate's weakest evidence. Ground every note to a mark, and say when something can't be judged.

## Frame prep
- **Key frames:** send 3–5. For logo work that means approach, mid, resolve and hold; otherwise the hero frame plus one frame before and one after.
- **Size:** long edge ≤ 2576 px. Anthropic's API docs list this high-resolution tier for Claude 4.7+; other models cap near 1568 px. The claude.ai apps may downscale differently (not verified), so never rely on sub-pixel detail.
- **Crops:** add 1:1 crops (no scaling) of the main bevel or edge, the smallest type, the brightest highlight, and any large gradient.
- **Grid:** overlay a labelled grid (columns A–D, rows 1–4) on each frame with `scripts/frame_prep.py`. Keep an unmarked copy.
- **No overlay possible** (no shell, or MCP-rendered images that can't be saved): cite cells of an imagined 4×4 grid on the raw frame (A–D left to right, 1–4 top to bottom). Lower confidence one step. If an edge or small type matters, ask for a 1:1 crop.

## Whole-frame defect sweep (before the mark)
- Cut 4x crops of every large surface in the frame, not only the mark: set pieces, floor, background rock or ice.
- Look for square or straight-edged patches of a second texture (MAT-14), texture patches bigger than the hero's details (MAT-15), seams and overlaps.
- Why: on one carved-ice logo shot (2026-10-30) the critique checked only the logos. The art director found snow squares and oversized frost by eye. A defect the user finds first is a miss.

## Note grounding
- Every note cites a frame and grid cell ("F3·C2") or a crop ID.
- Before output, run a second pass: re-check each note against its mark. Drop any note whose location doesn't hold, or relabel it.
- When the readout and the pixels disagree on a parameter, trust the readout and say so.

## Not judgeable from stills (flag X; don't guess)
- Grain structure
- Banding in 8-bit previews
- Sub-pixel aliasing
- Motion blur quality
- Easing and timing (ask for the ease readout or a frame strip)
- Flicker

## Confidence
- **High:** visible in both frame and readout.
- **Medium:** frame only.
- **Low:** inferred. Phrase it as a question.

Sources: SETMARK, DUAN24, ANT-VIS (see `sources.md`).
