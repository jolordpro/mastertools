# /elevate evals (v1)

Run these once the dry run supplies real frames. Record results in `evals/results/<YYYY-MM-DD>.md`. When moving to skill-creator benchmarking, port the cases to its evals.json schema.

## Pass/fail bar (approved)
- In blind A/B against plain Claude given the same frames, /elevate wins at least 8 of 10 scenes, judged by the user and one teammate.
- At least 4 of the top 5 ideas are usable without edits.
- At least 90% of notes point at the right mark.
- Zero Redshift values appear without an evidence label (zero values at all is the target).
- On 3 real projects, 2 of 3 reviewers prefer the revised render blind.

## Scene cases
| # | Shot type | Inputs | Must do | Fails if |
|---|---|---|---|---|
| E01 | PB-LOGO, metal mark (C4D) | 4 frames + MCP readout | Uses the readout flags. Raises edge catch (BEV-01/02) and reflection lighting (LGT-04) when present. FIX ranks first | States a Redshift value; any generic "add contrast" note |
| E02 | PB-LOGO, painted mark | Frames + readout | Covers coat and roughness (MAT-06, MAT-01). Respects TYP-14 | Suggests altering the letterforms |
| E03 | PB-LOGO, already strong | Frames + readout | Leads with S→W. "Keep" names the real strengths | Pads the list with FIX-tier fundamentals |
| E04 | PB-GLASS, clear panel over an environment | Frames + readout | Hands thin-vs-solid (MAT-08) to RS. Edge catch (BEV-01) | Judges grain or banding from an 8-bit preview |
| E05 | PB-GLASS, frosted panel with type | Frames + readout | Type legibility through glass (TYP-01/07), correctly located | Type note points at the wrong mark |
| E06 | AE type piece, default eases | Frames + AE readout | MOT-01 from the ease totals. Every motion note ends "verify in playback" | Claims timing quality from stills alone |
| E07 | AE type piece, no readout | Frames only | Asks once for the readout and lowers confidence | Asks repeatedly; invents parameter values |
| E08 | Player cutout (stub) | Frames | Uses the stub and says its rules await gold examples | Presents stub moves as established |
| E09 | Arena environment (stub) | Frames + readout | Motivated light (LGT-07/15). MAT-S1 restraint for hockey | Proposes a full frozen world |
| E10 | Revision round | Before and after frames + previous notes | Marks each note resolved, partly done or open, then proposes the next rung | Repeats resolved notes |
| E11 | Any shot, notes built on our own numbers and the user's words | Frames + readout + a note from the user | Labels a measured value or readout key M with its frame or key; labels the user's words A (user); keeps the move's own label beside M | Labels its own measurement V, or the user's words D |

## Surface cases
| # | Surface | Setup | Must do | Fails if |
|---|---|---|---|---|
| S01 | Claude Desktop + Maxon C4D MCP | No attachments; scene open in C4D | Renders the camera view through the MCP, reads the scene through read tools (or `c4d_readout.py` contents via Python), grounds to the imagined grid | Asks the user to export what the MCP can fetch; writes to the scene |
| S02 | claude.ai or Desktop, code execution on | Attached PNG frames + readout JSON | Runs `frame_prep.py`, cites overlay cells; any gold draft goes out as a downloadable file | Tries to write into the read-only skill folder |
| S03 | Claude Code in the repo | Frame paths + JSON path given | Reads from disk; runs `frame_prep.py`, or explains the Pillow install; writes gold drafts to the user's overlay `examples/gold/` (else the skill's `examples/gold/`) | Asks the user to upload files it can read locally |
| S04 | No shell, no MCP | Attached frames only | Imagined grid, confidence lowered, asks once for the readout | Claims overlay or crop precision it can't have |

## Trigger cases
- **Should trigger:**
  - "/elevate this resolve" (with frames)
  - "elevate this C4D glass panel shot"
  - "push this AE type piece to agency level"
- **Should not trigger:**
  - "make me a slide deck" (a slide or UI design skill)
  - "QC this render for broadcast-legal levels" (plan-review:shakedown)
  - "what sampling should glass use in Redshift" (c4d-redshift:redshift)
  - "red-team my plan" (plan-review:challenger)

## Grading per note
Pass or fail on each of:
- specific (a location and a concrete change)
- actionable
- justified (label plus source)
- right label ("Which label" in `references/README.md`: own measurements M, the user's words A (user))
- correct location
- correct hand-off
- no leaked render value
