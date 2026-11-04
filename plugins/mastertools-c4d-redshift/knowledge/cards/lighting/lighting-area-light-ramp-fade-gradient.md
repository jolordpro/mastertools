---
id: lighting-area-light-ramp-fade-gradient
title: Fade or colour an area light by adding a light shader graph with a Ramp into its colour (black means no light)
domain: lighting
tags: [area light, ramp, gradient, fade out, light shader, node editor, spread]
applies_to: Cinema 4D 2025 + Redshift
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KnfiJy2ND2o, src:yt-transcripts, https://www.youtube.com/watch?v=Gfz0jfx0EmM]
feeds: [lookdev sheet, coach]
conflicts: none
---
Reduce Spread first so the strip is visible; Spread 1 is 180 degrees, lower focuses the light and makes it more intense [06:36]. Add Graph on the area light creates an area-light material; connect a Ramp to Color [07:41-08:43]. Black in the ramp is zero light, so a vertical or horizontal ramp makes a fade; black-white-black gives soft edges [09:14-09:45]. Coloured ramp stops give a colour gradient [10:17]. Cmd-click the port dot to add the input.

**Use it:** Teach the coach order: spread, then graph, then ramp stops; remember spread changes intensity.
Transcript support: Same ramp-in-light-shader method in Redshift: spread to 0 for a projected beam, black ramp stops at the edges to fade it softly, orange tones in the middle; lower the intensity first so the gradient is easier to see. (https://www.youtube.com/watch?v=Gfz0jfx0EmM [02:00-03:15])
