---
id: reframing
title: Reframing for multiple aspect ratios (16:9 to 9:16 and beyond)
type: domain
aliases: [reframing, auto reframe, smart crop, cutdowns, social cutdowns, vertical video, 9:16, 4:5, 1:1, multi-format delivery, protection zones, AutoFlip, saliency-based cropping, aspect ratio conversion]
tags: [broadcast, social, motion, tools, practice]
related: [framing-cropping, broadcast-standards, attention-saliency, generation-loop, tools-models, sports-action]
evidence: practice; saliency-tracking tools are mature research code.
updated: 2026-10-20
---

# Reframing

## Quick answer
- Design for every delivery format at the start: a central protection zone that holds subject and key text in 16:9, 1:1, 4:5 and 9:16. `[Practice]`
- For footage, track the subject (saliency, faces, ball), not the frame center. `[Practice; tools exist]`
- Vertical is not a crop of horizontal: re-stack graphics vertically and resize type. `[Practice]`

## Planning `[Practice]`
- Draw safe rectangles for each target ratio over the master composition.
- Keep subject, faces and primary text inside the intersection of all targets.
- Put secondary elements in zones that may be cut.
- In vertical, reserve top and bottom bands for platform UI (captions, buttons, handles).
- Shoot or render wider than needed when possible to give reframing room.

## Vertical 9:16 default safe zone `[Practice]`
Sources disagree and no official organic-post figures were found (checked 2026-10-20). Use a conservative default:
- Canvas 1080x1920. Keep anything that must be read (faces, headline, score, logo) inside the hard box **x 120 to 888, y 288 to 1248** (768 wide, 960 tall). It is the union of the largest margin on each edge in TikTok, Reels and Shorts ad guidance, so it is safe on all three.
- Treat the lower-right quadrant (x > 850, y > 1150) as button territory.
- Keep the bottom 25 to 35% (about 480 to 670 px) clear of key content: captions, handles, buttons and ad call-to-action sit there. Ad-template guidance runs as high as about 660 to 670 px on TikTok, Reels and Shorts.
- Keep about 15% (about 290 px) clear at the top and 10 to 15% at the sides; the TikTok action column sits on the right edge.
- Older guides cite a centred 900x1400 or 880x1420 box. Both reach below y 1600, into the caption band, so they are not used here. Source table: `canon/poster-social-vertical.md`, "Phone-size and safe zones".
- Check the platform live before delivery: preview the upload in each app; UI layouts change without notice.

## Footage reframing methods
- Saliency and object tracking with smoothing (Google AutoFlip, 2020, MediaPipe; now unmaintained; pyautoflip is a maintained Python re-implementation). `[Tools]`
- UMSI-style importance maps for graphics reflow (research-only license). `[Tools]`
- Composition-aware cropping research: GAIC, CACNet, Venus (see `tools-models`).
- Manual keyframing remains the quality bar for hero assets.

## Graphics reflow `[Practice]`
- Re-stack horizontal layouts into vertical columns.
- Increase type size for phone viewing; reduce line count.
- Keep brand elements in consistent relative positions across formats.

## How to measure
- For each target crop: % of subject mask inside, % of text boxes inside, whether faces are cut.
- Crop path smoothness over time (avoid jitter).
- Saliency mass retained after crop.

## Failure modes
- Center crop cutting off the speaker or the ball.
- Jittery tracking crops.
- Horizontal text layout shrunk into vertical, unreadable.
- Captions covered by platform UI.

## Critique questions
- Does the story survive in every format?
- Does anything key sit in the bottom 25 to 35% or the right edge on 9:16?
- Are faces and key text inside every crop?

## Terms
- reframing, smart crop, auto reframe, protection zone, safe rectangle, cutdown, reflow, crop path smoothing

## Sources
- Google AutoFlip blog (2020); pyautoflip on PyPI; Fosco et al. 2020 (UMSI); cropping literature in `tools-models`.
