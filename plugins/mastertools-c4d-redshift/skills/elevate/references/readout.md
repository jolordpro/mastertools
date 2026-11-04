# Scene readout

The readout supplies what pixels can't: exact lens, light, bevel and material parameters. /elevate reads values to diagnose. It never judges or recommends Redshift values; those go to `redshift`.

## C4D, path A: Maxon Cinema 4D MCP server (primary)
- Requires C4D 2026.4 or later.
- Off by default. Enable it in Preferences → MCP. It needs an adapter token and keeps a local audit log.
- Grant only the read and render groups. Fewer tools means better tool choice (Maxon FAQ).
- It can render the viewport or a camera view. Use that for fresh frames at a known resolution.
- Claude Desktop is officially supported. Claude Code works by copying the generated client entry, but isn't officially supported.
- Not available in Commandline, Team Render, c4dpy, Cineware or Lite.
- Tool names aren't published, so field mapping gets confirmed at the dry run.
- If the server offers only a Python execution tool, send the contents of `scripts/c4d_readout.py` as the code. It reads only.
- Redshift node materials probably need the Python tool. Python access can also write, so keep /elevate's scripts read-only by construction and check the audit log.
- Don't run Maxon's server alongside third-party C4D MCP servers; their Python tools overlap.

## C4D, path B: read-only Python dump (fallback; Claude Code)
Run from the Script Manager or through the MCP Python tool. It prints JSON and writes nothing to the scene.
- **Chat apps:** the user attaches the JSON that is saved next to the .c4d.
- **Claude Code:** read it from the path the user gives.

## C4D fields
| Group | Fields |
|---|---|
| Render | Resolution, fps, frame range, color management/view transform, motion blur on/off, AOV list, takes |
| Camera (per key frame) | Focal length, sensor/film width, DOF on/off, f-stop, focus distance/target, position, height above floor, target, rig/parent |
| Lights | Type, size (w×h), intensity/exposure, color/temperature, visible in reflections, shadows on/off, include/exclude, angle off the camera axis |
| Objects | Hierarchy; Extrude depth, caps, bevel size/segments/profile/miter; phong angle; rounded-corner shader present |
| Materials | Assignment, base color, metalness, roughness (constant or mapped), IOR, thin-walled, anisotropy, coat, sheen, bump/normal/displacement present, texture resolution |

## AE: ExtendScript comp dump (follows the after-effects-engineering skill's conventions)
| Group | Fields |
|---|---|
| Comp | Size, fps, duration, project bit depth, color settings |
| Layers | Name, type, 3D, blending mode, parent, in/out points |
| Effects | matchName plus key parameters per effect |
| Text | Font, size, tracking, leading, animators |
| Keys | Times plus temporal ease (speed, influence) per animated property; count of default eases |
| Camera | Zoom, DOF, focus distance, aperture |

The user runs `ae_readout.jsx` via File ▸ Scripts ▸ Run Script File…. In the chat apps, the user attaches the JSON; in Claude Code, read it from the path the user gives.
AE MCP or UXP readout paths in 2026: not verified.

## Readout → likely moves (thresholds are T)
- The same roughness constant on every material → MAT-01
- Metalness between 0 and 1 on clean metal → MAT-09
- Colored specular on dielectrics → MAT-04
- Key within ~15° of the camera axis → LGT-02
- Bevel size 0, or below what reads at delivery size → BEV-01
- Rounded-corner shader on a hero close-up → BEV-03
- Focal length under ~35 mm on a hero close-up → CAM-01
- DOF off in a deep scene with a foreground → CAM-03, CAM-04
- Most eases at default → MOT-01
- 8 bpc project with large gradients → AE-04, FIN-06

Sources: MAXON-MCP.
