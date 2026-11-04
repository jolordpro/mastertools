---
id: attention-saliency
title: Attention, saliency and eye movements
type: science
aliases: [saliency, salience, where people look, eye tracking, scanpath, fixations, eye path, gaze, visual attention, bottom-up attention, top-down attention, Yarbus, Buswell]
tags: [smith, mital, deepgaze, umsi, eye-tracking, evidence-strong, measurable]
related: [hierarchy-focal-point, clutter-peripheral, continuity-attention, line-direction, tools-models, metric-recipes]
evidence: strong. Task shapes static viewing; motion and cuts synchronize gaze in video.
updated: 2026-10-20
---

# Attention and saliency

## Quick answer
- In stills, where people look depends on their task and spreads out over time. `[E-strong]`
- Faces, eyes and people grab attention fast. `[E-strong]` `[Unverified: "regardless of size" was not checked]`
- Text also draws early looks, but the effect depends on task and layout. `[E-mixed]`
- In edited video, motion, contrast and flicker pull many viewers to the same spot at the same time, most strongly right after a cut. `[E-strong]`
- The top saliency peak should be the intended focal point.

## Definition
- **Saliency**: how strongly a region pulls attention.
- **Bottom-up**: driven by contrast, color, motion, flicker, faces.
- **Top-down**: driven by the viewer's task, expectation, meaning.
- **Fixation / saccade / scanpath**: a pause, a jump, the ordered sequence.
- **Viewing center bias**: fixations cluster near frame center for any content (distinct from aesthetic center bias).
- **Attentional synchrony**: many viewers fixating the same place at once.

## Evidence
- Buswell 1935; Yarbus 1967: the same picture yields different scanpaths for different tasks. `[E-mixed]` `[Unverified: the task effect on scanpaths is real but its strength is contested; Yarbus's single-subject method is weak]`
- Mital, Smith, Hill & Henderson 2011: gaze clustering in moving scenes (video) is predicted by motion. Gaze resets toward center after cuts. `[E-strong]`
- Smith & Mital 2013: synchrony is far greater in moving (video) than static scenes; peaks shortly after onset; correlates with contrast, motion and flicker. `[E-strong]`
- DeepGaze IIE (Tübingen, 2021) leads the MIT/Tübingen Saliency Benchmark (AUC 88.3%, sAUC 79.4%, CC 82.4%). `[E-strong]`
- UMSI (MIT + Adobe, 2020) predicts importance in graphic designs (posters, infographics, UIs, ads) and saliency in photos. Retraining on UI eye-tracking data (UEyes) raised AUC from 0.778 to 0.878: domain data matters. `[E-strong]`
- UIGaze (2026): VLMs sometimes approximate human gaze on UIs; dedicated saliency models remain the reference. `[E-mixed]`

## Attention magnets `[Practice, mostly consistent with evidence]`
- Faces and eyes; then hands, text, animals.
- Highest local contrast (value first, then saturation).
- Motion onset and sudden change.
- Isolation in empty space.
- Convergence of lines and gazes.
- Sharp focus against blur.
- Anomaly in a repeated pattern.

## By medium
- Photography: brightest-contrast junction and faces win; check that a background highlight doesn't steal the eye.
- Design: text is read before images are studied; headlines and numbers act as magnets.
- Film: put the next shot's focal point where the eye already is at the cut (see `continuity-attention`).
- Broadcast and motion: any movement in a secondary graphic competes with the main action. Keep secondary elements still while the main read happens.

## How to measure
- Saliency map (DeepGaze IIE for photos, UMSI for graphics; check licenses) or Claude's own judgment plus clutter maps.
- Face and text detectors as attention boosts.
- Peak ratio: strength of top peak / second peak. `[Infer]` Target > 1.5 for a clear focal point.
- Overlap of top peak with intended subject mask (IoU or % of peak mass inside mask).
- Video: optical-flow magnitude per region; cut detection; expect a central reset after each cut.

## Failure modes
- Bright background highlight or sign stealing focus.
- Two faces of equal size and contrast splitting attention.
- Moving secondary graphic pulling eyes off live action.
- Text in a photo outranking the subject.

## Critique questions
- What is seen first, second, third?
- Is the first look the intended subject?
- Does anything move that shouldn't?

## Terms
- saliency, importance map, fixation, saccade, scanpath, bottom-up, top-down, attentional synchrony, center bias (viewing), AUC, NSS, CC

## Sources
- Buswell 1935; Yarbus 1967; Mital et al. 2011; Smith & Mital 2013; Linardos et al. 2021 (DeepGaze IIE); Fosco et al. 2020 (UMSI); UIGaze 2026.
