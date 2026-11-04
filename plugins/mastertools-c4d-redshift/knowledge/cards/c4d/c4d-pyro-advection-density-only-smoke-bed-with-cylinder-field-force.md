---
id: c4d-pyro-advection-density-only-smoke-bed-with-cylinder-field-force
title: Pyro advection that does not fall apart late in the sim: a flat box of density-only smoke, no gravity, no temperature, vorticity 0, stirred by a cylinder-field force
domain: c4d
tags: [pyro, pyro advection, field force, cylinder field, density dissipation, vorticity, voxel size, smoke bed, sketchy visuals, deep-read]
applies_to: Cinema 4D 2025 pyro with particles (Sketchy Visuals, uploaded Dec 2025)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vrE2wrqq0TM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Sketchy Visuals (Cinema 4D 2025, recorded 2025). The problem he fixes: in earlier tries the pyro dissolved after a certain frame count and particles flew off in odd directions [04:45]. His cure is a constant bed of density-only smoke that swirls in set patterns [00:37-05:16].
Settings [01:08-04:45]: source cube 1000 x 5 x 700 cm (thin is better); pyro emitter tag set to Volume; gravity off in the simulation scene; temperature off; density about 2; velocity off; noise off (optional); voxel size 3; relative density dissipation 20% so it stays light; vorticity strength 0 for smoother smoke (a little is fine).
Stir it with a Field Force holding a tall Cylinder field: strength 500, later 2000. Radius 65 gave a clean X pattern; a larger inner offset makes the pattern sharper, a smaller one wilder [03:14-05:47]. Random field on Overlay at 50% adds irregularity; a field driver on the radius (55 to 90 over a time field) or a flickering random driver also work, but returns diminish unless precise [06:19-08:56]. The values are very sensitive to tiny changes [28:10].

**Use it:** A stable, repeatable pyro base for particle advection in an energy or reveal open; expect long tuning of the cylinder field.
