---
id: broadcast-standards
title: Broadcast composition standards (safe areas, lower thirds, bugs, glanceability)
type: domain
aliases: [safe areas, action safe, title safe, graphics safe, EBU R95, SMPTE ST 2046, lower third, L3, chyron, super, name strap, score bug, network bug, DOG, ticker, full screen graphic, glanceability, on-air graphics, sports graphics package]
tags: [broadcast, standards, motion, nesn, standard]
related: [clutter-peripheral, accessibility-legibility, motion-principles, reframing, framing-cropping, hierarchy-focal-point, typography, sports-action]
evidence: standards for safe areas; practice and clutter evidence for glanceability.
updated: 2026-10-20
---

# Broadcast standards

## Quick answer
- 16:9 HD: action safe = 93% of frame, graphics/title safe = 90%. `[Standard]`
- Every on-air graphic must read in one glance while the viewer watches something else. `[Practice; clutter evidence E-strong]`
- Live action is primary; graphics are secondary except in dedicated full-screens. `[Practice]`

## Safe areas `[Standard]`
- EBU R 95 v1.1 (2017): action safe margin 3.5% and graphics safe margin 5% on each of top, bottom, left, right. Totals 7% and 10%, so 93% and 90% of frame.
- SMPTE ST 2046-1:2009 (via NAB TV TechCheck 2010): Safe Action 93%, Safe Title 90%.
- SMPTE RP 2046-2: 90% for 4:3 protection when a center-cut feed is needed.
- Legacy: RP 8 (1961) title safe 80%; RP 13 (1963) action safe 90%. CEA-708 captions still use the 80% window.
- Ignore third-party "88% title safe" figures; they contradict EBU.

## HDR graphics white `[Standard]`
- ITU-R BT.2408 ("Operational practices in HDR television production") defines HDR Reference White as the nominal level from a 100% reflectance white card: 203 cd/m2 on a PQ display, or on an HLG display with a 1000 cd/m2 peak. Signal levels: about 58% for PQ, 75% for HLG. Graphics and diffuse white are set at this reference level, not at peak. Checked live 2026-10-20 through secondary sources (BBC engineer post, Unreal Engine docs, forum quotes of the report); the report's own graphics-white wording was not read. `[Unverified: exact graphics-white wording in the current BT.2408 edition]`
- Practice: setting graphics at reference white keeps SDR-converted and HDR-to-SDR downmixes consistent. Peak-white graphics (100% signal) read as glaring in HDR and clip in downconversion. `[Practice]`
- Some productions use other diffuse-white levels; film and episodic HDR often do. Follow the show's HDR spec first.
- Check the current edition and the broadcaster's delivery spec before delivery.

## Glanceability `[Practice + Infer]`
- One idea per graphic.
- High value contrast (ΔL*), not only hue contrast. Use a plate or edge treatment over unpredictable video.
- Few elements, consistent positions across the package so viewers learn where to look.
- Text hold `[Infer heuristic]`: at least 3 s for short text; longer for multi-line. Read the copy aloud twice as a rough test.
- Numbers larger than labels in stat graphics.

## Lower thirds `[Practice]`
- Sit inside graphics safe, below the talent's chin, not covering the mouth.
- Name larger and heavier than title.
- Side placement agrees with talent's look room (graphic on the side the talent is not facing, or below).
- Animate on and off with clear staging; avoid motion while the viewer needs to read.

## Score bugs and persistent graphics `[Practice]`
- Constant position; never cover play-critical areas (ball path, goal, plate).
- Minimize animation; persistent motion competes with live action (motion captures gaze; Smith & Mital 2013).
- Account for their weight when composing camera framing and other graphics.
- Clutter budget: count simultaneous on-screen graphics (bug + score + ticker + sponsor + L3). `[Infer]` Above 3 at once, review.

## Full-screen graphics `[Practice]`
- Grid-based layout (see `grids-layout`), strong hierarchy, one focal stat.
- Background motion low-contrast and slow so foreground reads.

## Play-critical zones by sport `[Practice]`
Where graphics must not sit while play is live. These are working conventions from broadcast practice, not published rules (a search for an official NHL or league guide found none, 2026-10-20). Confirm with the show's director.
- Hockey: puck carrier and the puck, the net areas, the faceoff circles at a faceoff. Wide-camera boards and glass strips carry the action; keep bugs high and to a corner.
- Baseball: the pitcher-batter line from the center-field camera (the strike zone area), the baserunner and the ball during a play. Keep the lower-third zone free of the batter's box on the tight shot.
- Football: the line of scrimmage and the snap area, the ball carrier and the receiver's route; the down-and-distance and yard lines in the lower area. Do not cover the first-down line.
- Basketball: the ball handler, the basket and paint area on both ends; the court is fully live, so keep persistent graphics small and at an edge.
- Soccer: the ball, the penalty areas and goals, the player on the ball and the offside line when drawn. Wide shots put the action center-frame; keep bugs in a top corner.
- General rule: one persistent bug in one corner; moving graphics only when the ball or puck is dead. `[Practice]`

## Team-colour pairs and colour vision `[Practice]`
- Red-green deficiency affects about 8% of men and 0.5% of women (a color scientist's figure in press; population rates vary). Red vs green is the classic failure. `[E-mixed]`
- Documented case: the 2015 NFL Color Rush game with all-red Bills vs all-green Jets confused many viewers; the NFL said its TV test had not accounted for color blindness. Broadcast reproduction made the two colours closer. `[Practice]`
- Pairs likely to fail for red-green viewers: red vs green, red vs brown, orange vs green, green vs brown, green vs yellow-olive, purple vs blue, pink vs grey. When a matchup has such a pair, separate by value (light vs dark) and add a shape, number or position cue; do not rely on hue alone.
- Run the frame through a deuteranopia / protanopia simulator before delivery; see `accessibility-legibility`.

## Color and brand `[Practice]`
- Team colors are fixed; manage value contrast and use neutral plates.
- Check graphics on broadcast-legal levels and on phones (small screen).

## How to measure
- Element bounding boxes vs 90% and 93% rectangles.
- ΔL* between text and immediate background; WCAG contrast ratio as a proxy (see `accessibility-legibility`).
- Count of simultaneous graphics; motion magnitude in graphic regions.
- Overlap of graphics with salient regions of the live video (occlusion metric).

## Failure modes
- Text outside graphics safe.
- Graphic covering the ball, puck, face or scoreboard of play.
- Low contrast over bright ice, snow or sky.
- Busy animated backgrounds behind stats.

## Critique questions
- Can a fan read this in one glance while watching play?
- Is anything outside safe or covering key action?
- How many graphics are competing right now?

## Terms
- action safe, title safe, graphics safe, protection, center cut, lower third, chyron, super, bug, DOG, ticker, crawl, full screen, plate, legal levels

## Sources
- ITU-R BT.2408 (HDR operational practices); EBU R 95 v1.1 (2017); SMPTE ST 2046-1:2009; NAB TV TechCheck 2010; Smith & Mital 2013; Rosenholtz 2016; Ward.
