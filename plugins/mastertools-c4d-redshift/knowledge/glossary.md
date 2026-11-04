# Glossary: the creative post-production pipeline, brief to delivery


## How to use it

- Terms are grouped by stage, in the order a job moves. Alphabetical inside each group.
- Each row has two cells: the term, then what it means.
- The meaning ends with two tags:
  - **Dept:** who owns it.
  - **Platform:** where it shows up.
    - `check` = an automatic check or gate
    - `coach` = a tooltip or plain-words explanation
    - `report` = a field in a report or hand-off sheet
    - `none` = good to know, nothing to build
- Definitions are plain restatements of common industry use, checked against the interview
  talks in `research-pro-interviews.md` where noted (S-numbers match that file's source list).
  Studios differ. Where a term varies by shop, the entry says so.
- Slang is in its own group near the end. Some of it is rude. It is here so the coach can
  recognise it when a note or a message uses it.
- Not edited into cards or INDEX. Search with `grep -i term glossary.md`.

---

## 1. Brief and pitch

| Term | Meaning |
|---|---|
| Award (a shot) | Give a bid shot to a vendor, who then owns it. A 40-shot bid may split between two vendors (S1). **Dept:** production. **Platform:** report (who owns which shot). |
| Bid | A price and schedule offered before work starts. It rests on a breakdown of the work. **Dept:** production. **Platform:** report (bid versus actual render hours). |
| Brief | The client's written ask: goal, audience, length, deliverables, deadline. **Dept:** client, creative. **Platform:** report field "brief version"; coach (judge work against it). |
| Budget | The money available. Not the same as a bid. **Dept:** production. **Platform:** report. |
| Chemistry call | Early talk to see if the client and studio fit. **Dept:** production. **Platform:** none. |
| Concept | The core idea in one or two lines, before design. **Dept:** creative. **Platform:** none. |
| Deck | The slide file used to pitch. Often holds mood, frames and a plan. **Dept:** creative. **Platform:** none. |
| Fit check | Can we do this, on this date, with these people? Done before saying yes. **Dept:** producer. **Platform:** coach (render hours against deadline). |
| Kickoff | The first meeting after the job is won. Sets roles, dates, who gives notes. **Dept:** producer. **Platform:** report field "single voice for notes". |
| Mood board | Collected images that set feeling, colour and tone. Usually approved first. **Dept:** creative. **Platform:** none. |
| NDA | A non-disclosure agreement. No sharing the work or the project. **Dept:** legal, producer. **Platform:** check (watermark and private link on review files). |
| Pitch | A competitive presentation to win the job. Often unpaid or part-paid. **Dept:** creative, producer. **Platform:** none. |
| Rate card | The studio's list of prices by role or service. **Dept:** production. **Platform:** none. |
| Reference (ref) | Any image or clip that shows the look or move wanted. **Dept:** creative. **Platform:** report (ref list with the job). |
| Revision count | How many rounds of changes the price includes. **Dept:** producer. **Platform:** report (round counter); coach (warn at the last included round). |
| Scope | What the job includes. Anything outside it is a change. **Dept:** producer. **Platform:** report. |
| SOW | Statement of work. The written scope, dates and price. **Dept:** producer, legal. **Platform:** report. |
| Spec work | Free creative work done to win a job. **Dept:** creative. **Platform:** none. |
| Treatment | A written plan of the idea: story, look, music, how it will move. Common in director and commercial pitches. **Dept:** creative. **Platform:** none. |

## 2. Creative development: boards, style frames, animatic

| Term | Meaning |
|---|---|
| Animatic | Boards cut to timing and sound, with rough moves. Proves pacing before full work. **Dept:** creative, edit. **Platform:** check (final length matches animatic length). |
| Art direction | The person or work that sets the look and keeps it steady. **Dept:** creative. **Platform:** none. |
| Boards (storyboards) | A set of drawn or composed frames that lay out the story shot by shot. **Dept:** creative. **Platform:** report (board number on each shot). |
| Colour script | A strip of colour keys across the piece, showing how colour changes over time. **Dept:** creative. **Platform:** check (shot colour against colour script). |
| Comp (design comp) | A finished-looking still of the design. Not the same as a composite. **Dept:** creative. **Platform:** coach (word clash with "comp"). |
| Concept art | Paintings or frames that explore a look. **Dept:** creative. **Platform:** none. |
| Design phase | The stage where looks are explored and locked before animation. **Dept:** creative. **Platform:** coach (phase names). |
| Hero frame | The single best frame of the look, used as the target. **Dept:** creative. **Platform:** check (draft compared to locked frame). |
| Look lock | Client approves the look. Later changes are scope. **Dept:** creative, producer. **Platform:** check (frame fingerprint); report. |
| Style frame | A finished still, 2D or 3D, that shows the look of a motion piece. Often three to four are shown (S24, S26). **Dept:** creative. **Platform:** check (locked frame); coach. |
| Thumbnail | A tiny rough sketch of a frame. Many are made fast. **Dept:** creative. **Platform:** none. |
| Tone | The feeling the piece should give. **Dept:** creative. **Platform:** none. |
| Typography (type) | Choice and treatment of letters. **Dept:** design. **Platform:** check (type size and safe areas for broadcast). |

## 3. Previz and layout

| Term | Meaning |
|---|---|
| Blocking | Placing objects and camera roughly, before detail. **Dept:** layout, animation. **Platform:** coach (block timing first). |
| Camera move | How the camera travels: push, pan, orbit, crane. **Dept:** layout, animation. **Platform:** coach; check (jerk and dead stops). |
| Layout | Stage and camera set-up for each shot, matched to the cut. **Dept:** layout. **Platform:** report (camera and frame range per shot). |
| Postvis | Rough temp comps made after the shoot to show what a shot will be (S1). **Dept:** edit, VFX. **Platform:** none. |
| Previs | Rough 3D made before the shoot to plan shots. Also used in motion design to plan choreography. **Dept:** previs, layout. **Platform:** coach; report. |
| Proxy (low-poly stand-in) | Light model used for speed, swapped for the high-res version later. **Dept:** layout, 3D. **Platform:** check (proxy swapped before final). |
| Scratch track | Temporary sound used to time the piece. **Dept:** edit, sound. **Platform:** check (audio cut matches animatic). |
| Techvis | Planning the shoot with real camera, lens and rig numbers. **Dept:** previs. **Platform:** none. |

## 4. Asset build, look-dev and lighting set-up

| Term | Meaning |
|---|---|
| Albedo | The base colour of a surface without light. **Dept:** look-dev. **Platform:** check (value range). |
| Asset | A reusable item: model, material, rig, scene. **Dept:** 3D. **Platform:** report (asset version). |
| Bevel | A small rounded edge that catches light. Without it, edges vanish. **Dept:** modelling. **Platform:** check (bevel presence). |
| Chrome ball, grey ball | Balls held at the camera on set to record light direction and shadow (S1). **Dept:** on-set data, lighting. **Platform:** report (ref present). |
| Clay render | A render in plain grey material to judge light and form first. **Dept:** lighting. **Platform:** coach; check. |
| Colour chart | A card with known colours shot at the start of a take. **Dept:** DP, colour. **Platform:** check (chart in plate set). |
| Displacement | A map that moves surface detail in real geometry. **Dept:** look-dev. **Platform:** coach (cost warning). |
| HDRI | A 360 image holding real light levels, used to light a scene. **Dept:** lighting. **Platform:** check (HDRI range and health). |
| Hero asset | The object in focus. Gets the most detail. **Dept:** 3D. **Platform:** report. |
| Lens grid | A chart shot per lens (per serial number) so 3D can match lens warp (S1). **Dept:** on-set data, comp. **Platform:** report. |
| Look-dev (lookdev) | Building and testing materials and light to set how things look. **Dept:** look-dev. **Platform:** check (neutral rig test, white furnace). |
| Metalness / F0 | How metal-like a surface is, and how much it reflects head-on. **Dept:** look-dev. **Platform:** check. |
| Neutral rig | A fixed light set-up for comparing materials. **Dept:** look-dev. **Platform:** check. |
| Normal map | An image that fakes small surface bumps. **Dept:** texture. **Platform:** check (map is not inverted). |
| Proxy (render proxy) | A file that loads heavy geometry only at render time. **Dept:** 3D. **Platform:** check (path exists on farm). |
| Rig | The controls that move a model. Also a light or camera set-up. **Dept:** rigging, lighting. **Platform:** none. |
| Texel density | How many texture pixels cover a unit of surface. **Dept:** texture. **Platform:** check (on-screen density). |
| Texture | An image applied to a surface. **Dept:** texture. **Platform:** check (missing, wrong colour space). |
| Turntable | A render of the asset spinning on a plain background to inspect it. **Dept:** look-dev. **Platform:** check; coach. |
| UV | The flat map that tells a texture where to sit on a model. **Dept:** modelling. **Platform:** none. |
| White furnace test | Render in an even white world. Material should vanish if energy is right. **Dept:** look-dev. **Platform:** check. |

## 5. Lighting and rendering

| Term | Meaning |
|---|---|
| AOV | A separate image layer from one render: diffuse, reflection, depth, and so on. **Dept:** lighting, comp. **Platform:** check (sums to beauty). |
| Beauty | The full finished render pass. **Dept:** lighting. **Platform:** check. |
| Bucket | A tile of the image rendered at a time. **Dept:** lighting. **Platform:** coach. |
| Cryptomatte | Auto-made masks by object or material, for fixes in comp. **Dept:** lighting, comp. **Platform:** check. |
| Denoise | Software that removes grain noise from a render. **Dept:** lighting. **Platform:** check (finisher only; flicker). |
| Depth of field (DOF) | Focus blur by distance. **Dept:** lighting, comp. **Platform:** coach. |
| Farm (render farm) | Many machines that render frames in parallel. **Dept:** pipeline, IT. **Platform:** check (preflight); report. |
| Firefly | A bright stray pixel in a render. **Dept:** lighting. **Platform:** check. |
| Frame range | First to last frame to render. Includes handles when needed. **Dept:** lighting, edit. **Platform:** check. |
| GI (global illumination) | Light that bounces between surfaces. **Dept:** lighting. **Platform:** coach. |
| Job (render job) | One submission to the farm. **Dept:** render. **Platform:** report. |
| Light group | A render layer that holds the effect of one light or set. Lets lights be rebalanced in comp. **Dept:** lighting. **Platform:** check (groups sum to beauty). |
| Light ratio | How much brighter the key is than the fill, in stops. **Dept:** lighting. **Platform:** check. |
| Motion blur | Smear on moving objects, set by shutter. **Dept:** lighting. **Platform:** check; coach (180 degree rule). |
| Noise | Grain from too few samples. **Dept:** lighting. **Platform:** check. |
| Pass | One layer rendered for later combining. **Dept:** lighting. **Platform:** check. |
| Preflight | Checks run before sending to the farm. **Dept:** pipeline. **Platform:** check. |
| Render wrangler | The person who watches the farm, requeues failed frames, sets priorities (S28). **Dept:** pipeline, production. **Platform:** report. |
| Requeue | Send a failed frame or job back to the farm. **Dept:** wrangler. **Platform:** report. |
| Samples | How many light rays per pixel. More means cleaner, slower. **Dept:** lighting. **Platform:** coach. |
| Sequence (render sequence) | A numbered stack of frame images. **Dept:** render. **Platform:** check (naming, gaps). |
| Shutter angle | How long the virtual shutter is open per frame. 180 degrees is the usual baseline. **Dept:** lighting, camera. **Platform:** check. |
| Take (C4D) | A saved variant of a scene, with its own settings or objects. **Dept:** 3D. **Platform:** check. |
| Test render | A small, fast render to judge one thing. **Dept:** lighting. **Platform:** coach. |
| Trace depth | How many bounces a ray may take. **Dept:** lighting. **Platform:** check. |
| Wedge | A set of renders with one setting changed in steps, to compare. **Dept:** lighting, FX. **Platform:** coach (test matrix). |

## 6. Animation and FX

| Term | Meaning |
|---|---|
| Cache | Saved sim or animation data. **Dept:** FX. **Platform:** check (path on farm). |
| Ease | A change of speed at the start or end of a move. **Dept:** animation. **Platform:** check (curve metrics). |
| Hold | A pose kept still. **Dept:** animation. **Platform:** check (dead-stop test). |
| Overlap | Parts of an object finishing at different times. Makes motion feel alive. **Dept:** animation. **Platform:** coach. |
| Retime | Change the speed of a clip or a move. **Dept:** edit, animation. **Platform:** check. |
| Rough (rough animation) | Early motion to approve timing. **Dept:** animation. **Platform:** report (stage). |
| Sim (simulation) | Software-run physics: cloth, fluid, smoke, bodies. **Dept:** FX. **Platform:** check (cache present). |
| Spacing | Distance between positions in neighbouring frames. Sets the feel of speed. **Dept:** animation. **Platform:** none. |
| Timing | When things happen, in frames. **Dept:** animation. **Platform:** coach. |

## 7. Compositing and colour

| Term | Meaning |
|---|---|
| ACES | A colour system that keeps one working space from camera to display. **Dept:** colour. **Platform:** check (same config at every stage). |
| Alpha | The transparency channel of an image. **Dept:** comp. **Platform:** check (straight or premultiplied). |
| CDL | A small set of colour numbers (slope, offset, power, saturation) passed with a shot. **Dept:** colour. **Platform:** report (S1). |
| Clean plate | A shot of the scene without the thing to remove. **Dept:** comp. **Platform:** none. |
| Colour pipeline | The chain of colour spaces and conversions from source to display. **Dept:** colour. **Platform:** check. |
| Colour space | The rules that give numbers their colour meaning. **Dept:** colour. **Platform:** check. |
| Comp / composite | Combine images and layers into one. **Dept:** comp. **Platform:** coach. |
| Conform (colour) | Match graded and VFX shots to the final cut in the grade. **Dept:** colour, edit. **Platform:** check. |
| Despill | Remove green or blue light that bounced onto the subject. **Dept:** comp. **Platform:** none. |
| DI (digital intermediate) | The final colour and finishing stage for film. **Dept:** colour. **Platform:** none. |
| Difference check | Subtract one image from another to see only what changed. Used old versus new (S3). **Dept:** comp. **Platform:** check. |
| Grade | Set the final colour and contrast. **Dept:** colour. **Platform:** check. |
| Grain | Film-like noise added to match plates. **Dept:** comp. **Platform:** coach (match by area, S3). |
| Integration checklist | Six checks to make a CG element sit in a plate: context, perspective, tracking, colour, sharpness, grain (S3). **Dept:** comp. **Platform:** coach. |
| Key (keying) | Pull a matte from green or blue, or from a colour or brightness. **Dept:** comp. **Platform:** none. |
| LUT | A lookup table that maps colours from one look or space to another. **Dept:** colour. **Platform:** check. |
| Matte | A black and white mask. **Dept:** comp. **Platform:** check. |
| Output transform | The step that turns working colours into what the screen shows. **Dept:** colour. **Platform:** check. |
| Premultiplied | An image whose colour is already multiplied by its alpha. **Dept:** comp. **Platform:** check. |
| Roto | Trace a mask frame by frame. **Dept:** roto, comp. **Platform:** none. |
| Tech check | A pass that checks files, not taste: format, colour, range, naming (S3, S4). **Dept:** comp, QC. **Platform:** check. |
| Tone mapper | Compresses bright values to fit a display. **Dept:** colour. **Platform:** check. |
| Z-depth | An image of distance from camera. Used for focus and haze. **Dept:** comp. **Platform:** check. |

## 8. Editorial and conform

| Term | Meaning |
|---|---|
| AAF, EDL | Files that carry the edit decisions so another tool can rebuild the cut. **Dept:** edit. **Platform:** report (S2). |
| Assistant editor (AE) | Edit-team member who preps media, logs and turns over (S2). **Dept:** edit. **Platform:** none. |
| Bidding QuickTime | A clip of one shot, no context, no sound, watermarked, sent so vendors can price it (S1). **Dept:** VFX edit. **Platform:** none. |
| Conform | Rebuild the final cut from the original, high-quality media. **Dept:** edit, finishing. **Platform:** check. |
| Count sheet | A list of each shot with frames in handle and in cut (S1). **Dept:** VFX edit. **Platform:** report. |
| Cut | The current edited version of the piece. **Dept:** edit. **Platform:** report (cut version). |
| Cutback | One long take is worked as one VFX shot, then cut into two on return (S1). **Dept:** VFX edit. **Platform:** coach. |
| FFOC / LFOC | First and last frame of cut (S1). **Dept:** edit. **Platform:** report. |
| Handles | Extra frames before and after the cut that give room for edits. **Dept:** edit, VFX. **Platform:** check (handles after lock). |
| Hero plate | The main plate of a shot (S1). **Dept:** VFX edit. **Platform:** report. |
| Lineup | A chart showing which frames of which elements make up a shot (S1). **Dept:** VFX edit. **Platform:** report. |
| Lock (picture lock) | The cut is final. Only agreed changes after this. **Dept:** edit. **Platform:** check. |
| Offline | The working cut in light media. **Dept:** edit. **Platform:** none. |
| Online | The final cut rebuilt in full quality. **Dept:** finishing. **Platform:** none. |
| Plate | Any shot image used as a base for VFX. Usually filmed footage. **Dept:** edit, VFX. **Platform:** check (naming, S1). |
| Pull (a plate) | Cut a plate from source media with handles. **Dept:** VFX edit, lab. **Platform:** report. |
| Reconcile | Compare the new cut to the old for each VFX shot: extended, trimmed, omitted, added (S1). **Dept:** VFX edit. **Platform:** check. |
| Temp (temp comp, temp VFX) | A rough stand-in used in the cut until the final arrives. **Dept:** edit, VFX. **Platform:** report (temp or final flag). |
| Timecode (TC) | Hours:minutes:seconds:frames. **Dept:** edit. **Platform:** check. |
| Turnover | The package given to a vendor: plates, references, data, lists (S2). **Dept:** VFX edit. **Platform:** report. |
| Turnover (re-turnover) | A repeat hand-over after the cut changed. **Dept:** VFX edit. **Platform:** check. |
| Version (edit) | Numbered save of the cut. **Dept:** edit. **Platform:** report. |
| VFX editor | Edit-team role that preps shots, makes temps and tracks the cut (S1). **Dept:** edit. **Platform:** none. |
| VFX spreadsheet | Shared list of every VFX shot and its status and plate data (S2). **Dept:** VFX edit. **Platform:** report. |

## 9. Review: dailies, notes, status codes

| Term | Meaning |
|---|---|
| Approved (apr) | Passed the current review. May still need the next review. **Dept:** review. **Platform:** report. |
| Client review | Review by the paying side, usually after internal approval (S34). **Dept:** producer. **Platform:** report. |
| Dailies | Daily session where the latest shot versions are watched together and notes taken (S33). **Dept:** all. **Platform:** report. |
| Draw-over (paint-over) | Notes drawn on the frame. **Dept:** review. **Platform:** coach. |
| Final (finaled, fin) | Approved by the one who signs off. Ends the cycle (S33). **Dept:** review. **Platform:** report. |
| Hold (hld) | Work paused by supervisor or client. **Dept:** production. **Platform:** report. |
| Internal review | Review inside the studio before the client sees it. **Dept:** supervisor. **Platform:** report. |
| Kickback | A shot sent back to an earlier stage after review (S6). **Dept:** review. **Platform:** report (stage sent back to). |
| Note | A requested change. Best written with the shot number and a frame (S33). **Dept:** review. **Platform:** report. |
| Note coordinator | The person who writes notes live and sends them clean (S33). **Dept:** coordination. **Platform:** none. |
| Omit (omt) | Shot or element removed from the job. **Dept:** production. **Platform:** report. |
| Ready to start (rdy) | All inputs in. Work can begin. **Dept:** production. **Platform:** report. |
| Review round | One pass of notes and response. **Dept:** producer. **Platform:** report (round counter). |
| Shot code | Unique name for a shot, such as SEQ_010_SHOT_0040_v012 (S33). **Dept:** production. **Platform:** check. |
| Sign-off | The named person's yes. **Dept:** all. **Platform:** report (who, when). |
| Status (shot status) | A short label of where a shot stands. Common set: waiting, ready, in progress, review, approved, final, on hold, omit. ShotGrid defaults differ (S36). **Dept:** production. **Platform:** report. |
| Tech check (status) | The stage after internal approval where files are checked (S34). **Dept:** QC. **Platform:** check. |
| Version (shot) | One numbered submission of a shot (v001, v002). **Dept:** all. **Platform:** check (naming). |
| Waiting to start (wtg) | Blocked until inputs arrive. **Dept:** production. **Platform:** report. |
| WIP | Work in progress. Not ready to show. **Dept:** all. **Platform:** report. |

## 10. Delivery and QC

| Term | Meaning |
|---|---|
| Alpha delivery | Delivering with transparency, usually fill and key or a file with alpha. **Dept:** finishing. **Platform:** check. |
| Burn-in | Text burned onto review video: shot name, frame, timecode. **Dept:** review. **Platform:** check. |
| Codec | The way video is compressed. **Dept:** finishing. **Platform:** check. |
| Deliverables | The list of files promised. **Dept:** producer. **Platform:** report. |
| Delivery spec | The client's written rules for format, size, frame rate, colour, audio, naming. **Dept:** finishing. **Platform:** check (delivery profile as a file). |
| Dropped frame | A missing frame in a sequence. **Dept:** QC. **Platform:** check. |
| EXR | A high-range image format used for renders and plates. **Dept:** render, comp. **Platform:** check. |
| Frame rate (fps) | Frames per second. **Dept:** all. **Platform:** check. |
| Handoff | The moment one department or party takes over (S1, S2). **Dept:** all. **Platform:** check; report. |
| IMF | A mastering package format used by streamers. **Dept:** finishing. **Platform:** check. |
| Master | The approved top-quality file all copies come from. **Dept:** finishing. **Platform:** report. |
| Naming convention | Written rule for file and shot names. Example: bg01 v2 (S1). **Dept:** pipeline. **Platform:** check. |
| ProRes | A common mastering video codec. **Dept:** finishing. **Platform:** check. |
| QC (quality control) | A final technical check against the spec. **Dept:** QC. **Platform:** check. |
| Safe area | The part of the frame guaranteed visible on screens. **Dept:** design, finishing. **Platform:** check. |
| Slate | Info card at the start of a file: title, version, date. **Dept:** finishing. **Platform:** report. |
| Stems | Separate parts of the mix (voice, music, effects). Also separate picture elements. **Dept:** sound, finishing. **Platform:** report. |
| Versioning | Saving each change as a new numbered file. **Dept:** all. **Platform:** check. |
| Watermark | A mark over review video to deter leaks. **Dept:** review. **Platform:** check. |

## 11. Broadcast terms

| Term | Meaning |
|---|---|
| Bug (score bug) | The small score or logo box left on screen. **Dept:** graphics. **Platform:** check (safe area). |
| Chyron | A graphics system and brand for on-air text and graphics. Used as a generic word too. **Dept:** broadcast graphics. **Platform:** coach. |
| Fill and key | Two signals for broadcast graphics: the colour picture (fill) and the cut-out (key). **Dept:** graphics, playout. **Platform:** check. |
| Game package | The set of graphics for the live match: score, lower thirds, transitions. **Dept:** broadcast graphics. **Platform:** report. |
| Interstitial | A short graphic between pieces of programme. **Dept:** graphics. **Platform:** none. |
| Legal levels (broadcast safe) | Video values inside the allowed range, such as EBU R103. **Dept:** QC. **Platform:** check. |
| Loudness | Audio level measure, such as EBU R128. **Dept:** sound, QC. **Platform:** check. |
| Lower third | Name or info bar in the lower part of the screen. **Dept:** graphics. **Platform:** check (safe area, legibility). |
| On-air graphics | Graphics that appear in live or recorded programmes. **Dept:** broadcast. **Platform:** none. |
| Open (show open) | The opening animation for a show or game. **Dept:** graphics. **Platform:** none. |
| Playout | Sending the programme or graphics to air. **Dept:** broadcast ops. **Platform:** check. |
| Real-time graphics | Graphics rendered live by a game engine or a broadcast engine. **Dept:** broadcast graphics. **Platform:** check (repeat-run test, S5). |
| Sponsor plate | A card or element carrying a sponsor name inside a package (S5). **Dept:** graphics, sales. **Platform:** report. |
| Stinger | A short animated transition covering a cut. **Dept:** graphics. **Platform:** none. |
| Template (data-driven) | A graphic that takes names and numbers from data at air time. **Dept:** broadcast graphics. **Platform:** check. |
| Truck rehearsal | Practice in the mobile production truck before air (S29). **Dept:** broadcast. **Platform:** report (rehearsal days). |
| Vizrt, Unreal | A broadcast graphics engine, and a game engine used for broadcast. **Dept:** broadcast graphics. **Platform:** coach (S5). |

## 12. Production roles and producer terms

| Term | Meaning |
|---|---|
| Art director | Leads the look of one project and its designers (S25). **Dept:** creative. **Platform:** none. |
| Broadcast graphics director | Leads on-air look and graphics for a network or show. **Dept:** broadcast. **Platform:** none. |
| CG supervisor | Leads 3D across shots: pipeline, lighting, look. **Dept:** CG. **Platform:** none. |
| Change order | Written record of changed scope: what, schedule effect, price effect, sign-off date (S35). **Dept:** producer. **Platform:** report. |
| Colourist | Sets the final grade. **Dept:** colour. **Platform:** none. |
| Compositing supervisor | Leads comp and gives internal approval before delivery. **Dept:** comp. **Platform:** none. |
| Coordinator (VFX / production) | Tracks shots, notes and deliveries. **Dept:** production. **Platform:** report. |
| Creative director | Oversees the creative of many projects and the client voice. **Dept:** creative. **Platform:** none. |
| Executive producer (EP) | Owns sales, contracts and the client relationship (S23). **Dept:** production. **Platform:** none. |
| Lighting lead | Leads the lighters on a sequence. **Dept:** lighting. **Platform:** none. |
| Look-dev lead | Sets materials and look for the show. **Dept:** look-dev. **Platform:** none. |
| Overage | Cost above the bid. **Dept:** producer. **Platform:** report. |
| Pipeline TD | Builds the tools and checks that move work between departments. **Dept:** pipeline. **Platform:** none. |
| Producer | Day-to-day owner of schedule, budget and client contact (S23). **Dept:** production. **Platform:** none. |
| Profit line | A visible profit amount in a bid. **Dept:** producer. **Platform:** none. |
| Rebid | A new price after scope changes. **Dept:** producer. **Platform:** report. |
| Technical director (TD) | A technical problem-solver in a department. **Dept:** varies. **Platform:** none. |
| Vendor | An outside company doing part of the work. **Dept:** production. **Platform:** report. |
| VFX producer | Runs VFX budget, bids, vendors and schedule. **Dept:** production. **Platform:** none. |
| VFX supervisor | Leads the visual effects creative and technical result. **Dept:** VFX. **Platform:** none. |

## 13. Slang and shorthand

| Term | Meaning |
|---|---|
| Baking | Locking a live effect or setting into a fixed result (a cache, a map). **Dept:** all 3D. **Platform:** coach. |
| Beauty pass | See Beauty. **Dept:** lighting. **Platform:** none. |
| Cheat | Place or shape something to look right in camera, even if it breaks real space. **Dept:** layout, lighting, comp. **Platform:** coach (log cheats, as they break on a new angle). |
| Crunch | A hard stretch of long hours before a deadline. **Dept:** all. **Platform:** none. |
| Final final | The last real version, after others were called final. Used with dry humour. Best practice is to name versions so this is never needed. **Dept:** all. **Platform:** check (version names). |
| Finalling | Getting a shot approved as final. **Dept:** review. **Platform:** none. |
| Fix it in post | Leave a problem for comp or edit. Often costs more later. **Dept:** all. **Platform:** coach. |
| Hero | The thing that matters most in the shot or the best-looking version. **Dept:** all. **Platform:** none. |
| Kick it back | Send work to an earlier stage (S6). **Dept:** review. **Platform:** report. |
| Kick it to comp | Leave a fix for the compositor rather than re-render. **Dept:** lighting. **Platform:** coach (what can be fixed in comp). |
| Lock it down | Stop changes. **Dept:** all. **Platform:** check. |
| Notes round | A review that ends in new notes. **Dept:** review. **Platform:** report. |
| Pixel f*cking | Judging or fixing tiny details that no viewer will see. Also the careful polish that finishes a shot. Meaning depends on who says it. **Dept:** comp, design. **Platform:** coach (set a stop rule: when does polish end?). |
| Plate (slang use) | Any shot you build on. See Plate. **Dept:** all. **Platform:** none. |
| Pull (a key, a matte) | Create a key. Also: pull a plate from source. **Dept:** comp, edit. **Platform:** none. |
| Slap comp | A very rough, quick composite to see if the idea works (S38). **Dept:** comp. **Platform:** coach. |
| Temp | Placeholder. Anything marked temp must be replaced. **Dept:** all. **Platform:** report (temp flag). |
| Tweak mode | The stage where everything looks fine and only small changes are asked (S18). **Dept:** review. **Platform:** coach. |
| V0 | The first return of an untouched plate, to prove colour and frame range before work (S1). **Dept:** VFX, colour. **Platform:** check. |
| Wedge | See Wedge in rendering. **Dept:** lighting. **Platform:** coach. |
| WIP it | Show unfinished work to get early input. **Dept:** all. **Platform:** none. |
| Wrap | The shoot or job is finished. **Dept:** production. **Platform:** none. |

## Added by the deep read (2026-10-30)

Terms heard in the interview and talk transcripts, grouped by stage as the speakers used them. Each meaning ends with where it was heard. Dept and Platform tags are still to be added.


### animation

| Term | Meaning |
|---|---|
| **Layout blocking** | A first pass of set, character positions and camera using plain shapes. (heard: dMaRyOuMpRM [08:54]) |
| **prop animation** | technical animation of objects such as swords or vehicles rather than characters (heard: 4Z6s5-9o7W0 [1:04:11]) |
| **rotomation** | animating a CG stand-in to follow a filmed object or person (heard: 4Z6s5-9o7W0 [1:04:41]) |
| **rubber hose limb** | A limb with no joints that bends along a path; quick to build and render (heard: 2ivlXc9yrWI [47:34]) |
| **Secondary action** | Motion that follows the main action, such as hair or clothes, also called overlap or follow-through. (heard: dMaRyOuMpRM [09:26]) |
| **super rig** | One master character rig reused for most shots; Yond covered about 80% of the main character with it (heard: 2ivlXc9yrWI [32:02]) |

### any

| Term | Meaning |
|---|---|
| **exploded view** | CAD-style diagram or animation where parts separate along paths to show assembly order (heard: ysIL6NORGIo [1:02:20]) |

### any (AI skills)

| Term | Meaning |
|---|---|
| **hill climbing** | repeatedly adjusting an agent skill and re-testing it until the output improves (heard: ysIL6NORGIo [1:03:22]) |

### brief and pitch

| Term | Meaning |
|---|---|
| **Cost consultant** | A client-side person who caps the day rates an agency may pay, often around $800 in 2018. (heard: U3-_dDDKIgA [1:12:23]) |
| **MSA** | Master service agreement: umbrella contract between a studio and a client or agency, so later SOWs only cover one job. (heard: U3-_dDDKIgA [15:35]) |

### business

| Term | Meaning |
|---|---|
| **four A's funnel** | Awareness, attraction, action, advocacy: Hayley Akins' staging for marketing and client follow-up (heard: 5brpZYU-OzY [14:38]) |
| **Line of credit** | A bank's agreement to lend up to a limit when needed; easiest to open while billing is strong. (heard: U3-_dDDKIgA [47:19]) |
| **Monthly nut** | A studio's fixed monthly overhead that must be covered before any profit. (heard: U3-_dDDKIgA [35:17]) |
| **productized service** | A service with fixed time, price and deliverable, unlike custom work (heard: 5brpZYU-OzY [04:11]) |
| **three lists of freedom** | Lists of what you can't do, don't like doing and shouldn't do, to define a hire; credited to Chris Ducker (heard: 5brpZYU-OzY [57:16]) |
| **Zero-hour contract** | UK contract where the artist is booked but paid only for days actually called in. (heard: pKfKsUYpk4w [37:43]) |

### c4d

| Term | Meaning |
|---|---|
| **Auto Take** | Cinema 4D Takes mode that records changed values into the active take (heard: Cf9t-bPQkb0 [26:28]) |
| **Enhanced OpenGL** | Hardware preview renderer options (shadows, depth of field) for quick animatics (heard: Cf9t-bPQkb0 [40:22]) |
| **place tool** | C4D tool that drops a selected object onto a surface and aligns it to the surface; used for lights (heard: nwBpkCPFG0s [27:33]) |

### c4d lights

| Term | Meaning |
|---|---|
| **Preview intensity** | per-light setting that dims a light in the viewport only (heard: le17-h6tUD0 [40:00]) |

### c4d liquid

| Term | Meaning |
|---|---|
| **Age threshold / speed threshold** | frame or speed a source particle must reach before it produces secondary liquid (heard: FmaKhqSITFQ [27:31]) |
| **Trapped air / wave crest** | emitter inputs that estimate bubbles from turbulence and foam from surface curvature (heard: FmaKhqSITFQ [29:05]) |

### c4d mograph

| Term | Meaning |
|---|---|
| **Scatter tag** | tag that overrides distribution, variation, filter or probability for one item in a Scatter (heard: FmaKhqSITFQ [11:28]) |

### c4d viewport

| Term | Meaning |
|---|---|
| **Gouraud shading** | the shaded viewport mode where lights can look burnt out; Quick Shading is the plain alternative (heard: le17-h6tUD0 [39:35]) |

### camera

| Term | Meaning |
|---|---|
| **no-parallax point (entrance pupil)** | the lens position a CG pinhole camera must match (heard: Aa7UvqgMDKM [33:43]) |
| **open gate** | recording the full sensor area so any frame can be cropped later (heard: Aa7UvqgMDKM [48:45]) |

### career

| Term | Meaning |
|---|---|
| **lighting breakdown (reel)** | a separate PDF or video of passes per shot, kept off the main reel (heard: gjgAZ0x29ag [43:14]) |

### colour

| Term | Meaning |
|---|---|
| **ACES 2065** | the very wide archival ACES space that holds every visible colour (heard: 7uY4-bPvRKs [04:11]) |
| **Fake ACES** | using the ACES view transform while picking colours by eye, without converting textures and HDRIs (heard: 7uY4-bPvRKs [30:54]) |
| **Utility Raw** | OCIO input space that leaves values as they are (heard: 7uY4-bPvRKs [34:34]) |
| **View transform** | the display step that maps scene-linear values to a monitor, for example ACEScg to sRGB (heard: 7uY4-bPvRKs [02:39]) |

### comp

| Term | Meaning |
|---|---|
| **ADX** | Academy Density Exchange, a density encoding of film scans used for film-process colour work (heard: -g6JTD8cge4 [12:07]) |
| **AMF** | ACES Metadata File, records which ACES transforms were applied to a clip (heard: -g6JTD8cge4 [16:20]) |
| **beauty work** | 2D touch-up of faces and skin (heard: 4Z6s5-9o7W0 [1:23:03]) |
| **CLF** | Common LUT Format, an open file format for portable colour transforms (heard: -g6JTD8cge4 [12:39]) |
| **concatenate** | consecutive colour grade nodes combine into one maths operation, so adding a reverse grade returns the original with no loss (heard: yl28HkA-qyo [30:16]) |
| **Deep compositing** | Comp from renders that carry many depth samples per pixel, so edge and depth problems do not appear. (heard: pKfKsUYpk4w [47:41]) |
| **difference key** | key from the difference between before and after images, used to isolate what a comp changed (heard: yl28HkA-qyo [37:33]) |
| **Edge extend** | Growing the colour or depth values past an object's edge so a defocus or blur sampling the edge does not pick up wrong values. (heard: pKfKsUYpk4w [46:07]) |
| **Flop (a shot)** | Mirror a shot horizontally to test whether its composition still works. (heard: _Y17791HioY [18:40]) |
| **high/low frequency separation** | split an image into fine detail (edges, text) and smooth tone/colour so detail can be restored without changing lighting (heard: sMMYSmDHAY8 [32:31]) |
| **key mix** | node that blends two images through a mask, used to bring changed pixels over an untouched plate (heard: yl28HkA-qyo [37:33]) |
| **prep artist** | person who prepares plates (roto, clean-up) before the compositor; some studios treat it as a rung below junior comp (heard: yl28HkA-qyo [58:57]) |

### creative development

| Term | Meaning |
|---|---|
| **boardamatic** | A slideshow of storyboard frames cut to the voiceover to approve timing, before the animatic (heard: 2ivlXc9yrWI [58:30]) |

### creature vfx

| Term | Meaning |
|---|---|
| **puppet methodology** | using a physical stand-in on set as the reference and as real footage where possible (heard: Fg9_-ssGcbg [05:44]) |

### delivery

| Term | Meaning |
|---|---|
| **Net 30 / net 90** | Payment due 30 or 90 days after the invoice; long terms are offset by taking most of the fee at signing. (heard: U3-_dDDKIgA [50:24]) |

### design

| Term | Meaning |
|---|---|
| **acrylic (Fluent Design)** | Microsoft's name for the glass-like translucent panels in its UI language (heard: J76-IxN7pVI [05:56]) |

### editorial

| Term | Meaning |
|---|---|
| **decompose (Avid)** | tool that makes sub clips from a timeline with handles (heard: MoR7ncjN9Ds [15:37]) |

### finishing

| Term | Meaning |
|---|---|
| **last looks** | The final review week before a piece is called done (heard: 2ivlXc9yrWI [1:05:43]) |

### fluid sim

| Term | Meaning |
|---|---|
| **Flowline** | Scanline's in-house fluid simulation system that divides sims across a network for hundreds of millions of particles (heard: dAL6U1nZpcA [14:06]) |

### grade

| Term | Meaning |
|---|---|
| **digital gaffer** | A colorist seen as the cinematographer's lighting assistant after the shoot: emphasises the shot, does not author it (heard: yvvXW_fLB6c [09:49]) |
| **full print emulation (FPE)** | A look-up table that mimics a film print so the digital picture matches a print side by side (heard: yvvXW_fLB6c [28:30]) |
| **hero shot** | The shot where the lead delivers the key line; the first shot graded in a scene to set the scene look (heard: yvvXW_fLB6c [53:31]) |
| **interpositive** | An intermediate film element made from the negative; a telecine scan from it lacks the print look (heard: yvvXW_fLB6c [30:06]) |
| **metameric failure** | Two viewers or two devices disagree on a colour match because narrow-band light hits each eye's response differently (heard: yvvXW_fLB6c [36:22]) |
| **printer lights** | Offsets that raise or lower overall exposure in steps, mimicking opening the lens or changing lights; used for the first scene balance (heard: yvvXW_fLB6c [54:34]) |
| **scene pass** | A grading block that holds corrections for a whole scene, separate from the single-shot balance and the film-wide look (heard: yvvXW_fLB6c [1:04:28]) |

### ideation

| Term | Meaning |
|---|---|
| **open mode / closed mode** | open mode is idea generation with no judgement; closed mode is executing the chosen idea (from John Cleese's creativity talk) (heard: wbkmPYViTlw [19:13]) |

### lighting

| Term | Meaning |
|---|---|
| **IBL (image-based lighting)** | Yann Dupont's preferred term for HDRI, to avoid confusion with Photoshop HDR blending (heard: gjgAZ0x29ag [10:25]) |
| **light cookie** | texture projected from a light to shape or fake shadows (heard: r2PXd6l7kBg [23:20]) |
| **master shot (lighting)** | a lead-prepared first lighting and comp setup of a sequence that other artists copy (heard: I17wB0Mn940 [04:10]) |
| **Rembrandt lighting** | triangle of light on the shadow-side cheek that gives a face volume (heard: I17wB0Mn940 [37:33]) |
| **set photography** | photos taken on set as lighting and look reference (heard: 4Z6s5-9o7W0 [40:17]) |
| **shot lighting vs sequence setup** | Sequence setup is the lead's look and rig for a sequence; shot lighting is when other lighters join and tune each shot (heard: GcPlNw9kFVk [20:56]) |

### look dev

| Term | Meaning |
|---|---|
| **Natural shaders** | A procedural material set (rock, snow, ice, water) controlled by masks and sliders. (heard: Fa7z8RgPhA4 [24:26]) |

### look development

| Term | Meaning |
|---|---|
| **photo bashing** | Building an image by layering photo textures and renders in Photoshop (heard: J76-IxN7pVI [18:35]) |

### motion

| Term | Meaning |
|---|---|
| **breakdown key** | a key between two extremes that carries the most information about the move and is slid to test timing (heard: E-sF_1FgpJw [01:34]) |
| **eye trace (I trace)** | Making a moving element guide the viewer's eye from one beat to the next (heard: -R-Nuds6Bd0 [12:11]) |
| **maintain scale (expression)** | A parent-null expression that keeps strokes or dots at a fixed size while a parent null scales (heard: -R-Nuds6Bd0 [47:40]) |
| **on twos** | a new drawing/pose every two frames (heard: E-sF_1FgpJw [09:49]) |
| **overshoot** | An element passes its target slightly and settles back; a few frames of it add life (heard: -R-Nuds6Bd0 [12:44]) |
| **storytelling pose** | one of the poses that alone tells the audience what happens, like a comic-book version of the shot (heard: E-sF_1FgpJw [05:42]) |

### notes

| Term | Meaning |
|---|---|
| **American sandwich** | Slang for praising, then giving the problem, then praising again; this guest asks for the problem stated plainly (heard: yvvXW_fLB6c [1:27:52]) |

### on-set data

| Term | Meaning |
|---|---|
| **reference spheres** | chrome and gray balls shot in the plate to match CG light and reflection (heard: gjgAZ0x29ag [08:21]) |

### on-set vfx

| Term | Meaning |
|---|---|
| **clean pass** | take repeating the action without the stand-in or prop so CG can be added over a clean plate (heard: Fg9_-ssGcbg [07:18]) |

### pipeline

| Term | Meaning |
|---|---|
| **Arras** | MoonRay's distributed compute framework that sends interactive work to a cluster and streams results back (heard: fQUnq6drevw [05:29]) |
| **cookbook** | an artist's own saved set of reusable procedures and tool groups (heard: yl28HkA-qyo [42:16]) |
| **data IO** | team moving client media and archives in and out of a studio (heard: eb0QFXD3AaA [03:36]) |
| **Hydra delegate** | adapter that lets a renderer draw inside USD's Hydra viewport framework (heard: fQUnq6drevw [16:27]) |
| **Iterate and render** | Greyscalegorilla script that saves the next scene version and starts a Team Render (heard: aheTC8N2xQg [37:15]) |
| **minimum viable product (MVP)** | the first version that meets the stated ask, shown before polish (heard: qlNn8Gim3qU [15:35]) |
| **Parsec** | remote-desktop tool for logging into a render PC from another machine (heard: aheTC8N2xQg [21:03]) |
| **PC over IP** | remote desktop compression so a workstation in a server room is used at home (heard: dAL6U1nZpcA [50:16]) |
| **plate (VFX)** | one layer of a shot, such as foreground or background, turned over to a vendor (heard: MoR7ncjN9Ds [08:23]) |
| **pull package** | EDL, AAF and reference sent to the lab so it can cut plates from source (heard: MoR7ncjN9Ds [39:11]) |
| **tape shucking** | loading and unloading backup tape cartridges (heard: eb0QFXD3AaA [06:42]) |
| **tech art** | role bridging art and engineering, tools and look (heard: r2PXd6l7kBg [12:20]) |
| **version zero (v0)** | vendor's first return that only proves frames and format, no effects (heard: MoR7ncjN9Ds [49:08]) |
| **working range / working duration** | shot length minus handles (heard: MoR7ncjN9Ds [58:28]) |

### pitch

| Term | Meaning |
|---|---|
| **style shots** | Single polished frames that show the look of key moments; Italian Giants' wording for style frames (heard: Cf9t-bPQkb0 [36:25]) |

### production

| Term | Meaning |
|---|---|
| **Circle take** | A take marked as a good one during recording, later assembled into the selects. (heard: dMaRyOuMpRM [07:17]) |
| **Digital tap / video tap** | A small digital video feed on a film camera so the crew can see the shot. (heard: _Y17791HioY [33:44]) |
| **Head of Nuke** | Department lead for Nuke compositors in a studio pipeline. (heard: pKfKsUYpk4w [06:21]) |
| **Post-vis** | Rough but fairly good-looking CG added to filmed plates during editing, to show the finished shot idea; Cangelosi says higher quality than previz. (heard: Fa7z8RgPhA4 [19:14]) |
| **Soup to nuts** | One vendor handling every part (writer, VO, sound, animation) so the client passes on nearly all of the budget. (heard: U3-_dDDKIgA [44:11]) |

### real-time

| Term | Meaning |
|---|---|
| **spherical harmonics (SH) lighting** | low-order baked indirect lighting; good for indirect, poor for direct light shaping (heard: r2PXd6l7kBg [21:46]) |

### redshift

| Term | Meaning |
|---|---|
| **Principled Hair** | physically based hair shader (melanin, albedo mix) used on procedural fur (heard: FmaKhqSITFQ [46:59]) |

### rendering

| Term | Meaning |
|---|---|
| **random walk SSS 2** | newer ray-traced subsurface scattering algorithm described as more accurate in thin areas, first in Arnold (heard: gjgAZ0x29ag [1:18:39]) |

### review

| Term | Meaning |
|---|---|
| **bonus round** | list of extra client ideas parked for the end of the project, done only if time remains (heard: qlNn8Gim3qU [21:19]) |
| **contact sheet (VFX review)** | all matching shots laid out at once to spot the odd one (heard: 4Z6s5-9o7W0 [36:05]) |
| **keystone shot** | one agreed-good shot loaded next to others to compare a look (heard: 4Z6s5-9o7W0 [35:03]) |
| **paint-over** | A note given by painting directly on a rendered frame to show the intended look (heard: GcPlNw9kFVk [21:37]) |
| **paper doll status** | Characters that slide around the frame without real animation yet; tell clients in a status round (heard: 2ivlXc9yrWI [1:03:41]) |
| **RV** | flipbook player used for shared remote review sessions (heard: dAL6U1nZpcA [49:15]) |
| **throw it over the fence** | send a presentable, not perfect, version for client notes at the internal cutoff (heard: qlNn8Gim3qU [18:42]) |

### styleframe

| Term | Meaning |
|---|---|
| **thumbnails (design)** | tiny rough sketches of many compositions, done before refining (heard: wbkmPYViTlw [18:43]) |

### tool

| Term | Meaning |
|---|---|
| **Recolor (Illustrator)** | edit-recolor colour wheel with randomise to try palettes fast (heard: wbkmPYViTlw [52:22]) |

### VFX

| Term | Meaning |
|---|---|
| **2D sup** | The 2D supervisor, who leads compositing on a show (heard: DVkwpF9ddhQ [13:48]) |

### vfx

| Term | Meaning |
|---|---|
| **bubbles** | Quick A-over-B environment mockups given to editorial before the full 3D build (heard: bU6IJNM7QUY [38:22]) |
| **invisible effects** | work the audience never notices was done (heard: 4Z6s5-9o7W0 [12:17]) |

### VFX

| Term | Meaning |
|---|---|
| **light probe** | On-set reference (chrome or grey ball, HDR capture) used to rebuild the lighting in CG (heard: Cj4SuW4lnlY [09:30]) |

### vfx

| Term | Meaning |
|---|---|
| **livery** | A racing car's paint and sponsor scheme, which changes between races (heard: bU6IJNM7QUY [22:16]) |

### VFX

| Term | Meaning |
|---|---|
| **lockdown shot** | A locked-off camera shot with no parallax, so it cannot be 3D tracked (heard: Cj4SuW4lnlY [21:33]) |

### vfx

| Term | Meaning |
|---|---|
| **matchimation** | Hand-animated match to a filmed object's motion, used as reference and replacement (heard: bU6IJNM7QUY [29:32]) |
| **picture car** | A real vehicle used on camera, as opposed to a stand-in or CG one (heard: bU6IJNM7QUY [24:52]) |
| **postviz** | quick temp comps made by the editorial team after shooting (heard: Qft4VRn_WaY [13:51]) |
| **reskin** | Swap the livery or body of a real filmed car (or object) for a digital one, tracking the original's performance (heard: bU6IJNM7QUY [28:30]) |
| **rooster tail** | The plume of spray thrown up behind a fast vehicle on a wet surface (heard: bU6IJNM7QUY [33:11]) |
| **witness cameras** | extra cameras on set recording the shot for later reconstruction (heard: ZcXhMm3eXTs [07:30]) |

### vfx (Loki)

| Term | Meaning |
|---|---|
| **time slipping** | effect where a character is stretched through time using performance passes and digital double (heard: ZcXhMm3eXTs [13:43]) |

### vfx review

| Term | Meaning |
|---|---|
| **Spidey sense** | A trained gut feeling that a shot is fake before you can say why. (heard: _Y17791HioY [08:22]) |

### vfx turnover

| Term | Meaning |
|---|---|
| **awarded** | a bid shot handed to a specific vendor to do (heard: Qft4VRn_WaY [10:33]) |
| **reconcile (differential, cut count check)** | checking every VFX shot for extended, trimmed, omitted or added changes after a cut change (heard: Qft4VRn_WaY [15:59]) |

### virtual production

| Term | Meaning |
|---|---|
| **outside-in / inside-out tracking** | cameras around the room track markers on the object, versus a camera on the object tracking markers on the ceiling (heard: Aa7UvqgMDKM [30:37]) |
| **Simulcam** | live composite of the camera feed with CG so the set extension is visible while shooting (heard: Aa7UvqgMDKM [10:24]) |
| **spectator view** | stabilised camera view of a VR user shown to others (heard: Aa7UvqgMDKM [16:37]) |
| **volume (LED volume)** | stage walled with LED panels showing real-time background (heard: Fg9_-ssGcbg [02:38]) |

## Added by the polish page read (2026-10-30)

Terms from the full text of interviews and articles with the polish roster. Each meaning ends with where it was read.


### agencies

| Term | Meaning |
|---|---|
| **Experience design** | Imaginary Forces' name for designing brands, spaces and sponsored sensation together rather than a single medium. (read: suckerpunch frankfurt §6) |

### animation

| Term | Meaning |
|---|---|
| **Cel (animation)** | Hand-drawn frames; Gunner mixed cel and 3D. (read: gunner mesh §2) |

### brief

| Term | Meaning |
|---|---|
| **Eye candy** | Alderson's plain word for crafted, engaging imagery that needs no big story behind it (read: cleverpodcast ep164 [§30, §32]) |
| **Ice shot / consumption shot** | The formula beats a drinks spot must tick (Pepsi example) before the studio plays (read: cleverpodcast ep164 [§30]) |

### broadcast

| Term | Meaning |
|---|---|
| **Duet breakdown** | Fox term for graphics generated live on site on Chyron Duet character generators (read: tvtechnology §1) |
| **NEWstalgia** | reviving an old era's iconography inside a current-feeling package (read: SVG GFX forum §2) |
| **tape breakdown** | Fox term for the pre-rendered stock graphics (openers, closers, interstitials, bumpers, bugs) made at HQ and distributed to shows (read: tvtechnology §1) |
| **transition logic** | a graphics system moving from one graphic to the next on the same video input without separate cueing (read: tvtechnology §2) |

### cinematography

| Term | Meaning |
|---|---|
| **CineFade** | lens iris synced to a motorised polarizer so depth of field changes with no visible exposure change (read: motionpictures-mank-p2 §3) |
| **day-for-night** | night scene shot in daylight with the exposure closed down; needs heavy fill on faces (read: motionpictures-mank-p2 §4) |
| **swing/tilt lens** | lens system that shifts the focal plane so only part of a subject, e.g. one eye, is sharp (read: motionpictures-mank-p2 §3) |

### color

| Term | Meaning |
|---|---|
| **Scene Based Image Manipulation** | perceptual approach (2002) that lets one grade convert automatically for more than one display (read: business-punk §2) |

### comp

| Term | Meaning |
|---|---|
| **DI theatre** | digital intermediate theatre where versions are compared side by side (read: motionpictures Volpatto §4) |
| **Optical signature** | Winquist's phrase for the look of a lens that rendered elements must match. (read: yahoo winquist §2) |
| **show LUT** | a look-up table built early with the DP for each period or world of a film (read: Company 3 Flamin' Hot §1) |

### comp review

| Term | Meaning |
|---|---|
| **shot ping pong** | two compositors swap the first five things each notices before dailies (read: benmcewan §5) |

### comp/CG

| Term | Meaning |
|---|---|
| **Deep Shapes** | Weta FX machine-learning tool adding subtle wrinkling and tissue detail over artist-made facial animation. (read: yahoo winquist §1) |

### concept

| Term | Meaning |
|---|---|
| **Post-rationalising** | Writing the idea after the visual exists so it reads as having led it; Alderson treats it as a core skill (read: cleverpodcast ep164 [§19-§20]) |

### education

| Term | Meaning |
|---|---|
| **Robustness** | How broadly a method holds across shots, genres and cameras; the broader, the better the technique. (read: ccd7f3b8 §2) |

### grade

| Term | Meaning |
|---|---|
| **Hero shot workflow** | Pulling a small set (best, worst, important, about 15-20) to settle looks with the approver early (read: premiumbeat Inhofer [§5]) |
| **Three-pass workflow** | Fix each shot, match across shots, then apply the look (read: premiumbeat Inhofer [§2-§3]) |

### grading

| Term | Meaning |
|---|---|
| **Colour wash look** | A bold colour treatment that should feel organic to the shot rather than a filter. (read: dvresolve §1) |
| **Compensation loop** | Using a tool that fixes a problem but creates another that needs a second fix. (read: 9cee63c0 §22) |
| **Etalonaje** | Spanish word for colour grading. (read: panorama §1) |
| **Hue vs curves** | Resolve custom curves used to harmonise colours across shots. (read: dvresolve §1) |
| **Printer points** | Printer-light style grading control the hosts say was all the rage 7-8 years ago; the page does not define it. (read: 9cee63c0 §22) |
| **Refinement (grade)** | Sonnenfeld's word for grading footage whose look was set on set. (read: panorama §1) |

### lighting

| Term | Meaning |
|---|---|
| **caustics** | ribbons of light, like on a pool bottom, made by sun bending through surface ripples (read: english-video §4) |
| **fog beams** | underwater light shafts that give colour depth cues and show which way is up (read: english-video §4) |
| **key colour (colour key)** | Pixar colour key: a painted colour study per sequence that the master lighter follows (read: fxguide Inside Out §2) |
| **Last light** | Final light of the day, a shooting window that a Volume can hold for hours. (read: nfs fraser-deakins §2) |
| **master lighter / shot lighter** | master lighter sets the sequence's main lights; shot lighters take them into each shot (read: fxguide Inside Out §1-2) |
| **negative fill** | black material that removes bounce so shadows stay deeper (read: fstoppers Young §2; rogerdeakins day exterior §2) |
| **Pools of light** | Hudson River School device of lit areas that lead the eye around a big landscape. (read: cgchannel cole §4) |
| **Pre-lighting** | Lighting key angles of a digital set with the DP before the shoot to fix time of day, angles and ratios (read: fxguide Jungle Book [§6]) |
| **Rated at 640 / lower rating** | Setting the camera's exposure index lower than usual so a scene needs more light and gets more shape (read: nofilmschool Messerschmidt [§4]) |
| **theatrical fadeout** | stage lights on plate dimmers fading selectively so part of the frame lingers (read: motionpictures-mank-p2 §2) |

### look

| Term | Meaning |
|---|---|
| **Surrealist naturalism** | Messerschmidt's phrase for practicals, allowed darkness and silhouettes with motivated sources (read: nofilmschool Messerschmidt [§4]) |

### lookdev

| Term | Meaning |
|---|---|
| **camera projection** | projecting a still onto low-res geometry so a camera can move through it (read: maxon Marks §2) |
| **damage map** | a map assigning wounds and damage states to each shot so look variants match (read: artofvfx §4) |
| **De-rez** | Hand-degrading a photo into coarse blocks for a digital-decay look (read: artofthetitle Halt and Catch Fire [§4]) |
| **EbSynth** | Tool that carries one painted style frame across an unstylised animation sequence (read: artofthetitle Peripheral [§4]) |
| **Fractal sense of detail** | Wall's phrase for detail that continues at every scale, such as cogs under the surface (read: artofthetitle Game of Thrones [§4]) |
| **gate weave** | slight frame wobble of film; added to dissolves to imitate optical printing (read: motionpictures-mank-p2 §2) |
| **look book** | a set of reference images sent to a director to find the film's visual vocabulary (read: motionpictures-mank-p1 §1) |
| **medulla** | central core of an animal hair fibre, now modelled in Weta's hair shading (read: artofvfx §3) |
| **Pixel sorting** | Glitch technique that re-orders pixels by a value; used with distortion layers on Peripheral (read: artofthetitle Peripheral [§4]) |
| **Ptex (per-face texturing)** | RenderMan texture method used so the CG team avoided UV mapping on building models (read: artofvfx Inception [§1]) |
| **Unbiased renderer** | Renders light physically without shortcuts and does not flicker, historically slow; Marks says Octane uses the GPU to fix the speed. (read: semi-permanent §5) |
| **Waldo control suit** | mechanical telemetry suit that translates operator motion to a robot's joints (read: gizmodo Avatar §3) |

### motion

| Term | Meaning |
|---|---|
| **board-o-matic** | an animatic cut from storyboards (read: artofthetitle §3) |
| **cinemagraph** | still photo with subtle looping movement (read: provideocoalition §2) |
| **Previs (map shots)** | Moving blockout used here instead of storyboards so camera moves can be judged (read: artofthetitle Game of Thrones [§1, §4]) |
| **signpost (title design)** | one recognisable element kept between seasons while the rest changes (read: stash Clair §1) |

### pipeline

| Term | Meaning |
|---|---|
| **Element in pipe** | Published status for an internally approved file that failed tech checks: usable downstream, not for the client. (read: caveacademy statuses §5) |
| **Proposed final** | Status when an element is on its way to the client for sign-off. (read: caveacademy statuses §6) |
| **sg_status_list** | the Flow Production Tracking field holding an entity's status (read: shotgrid §1) |

### practical effects

| Term | Meaning |
|---|---|
| **Air mortar** | Device that blasts lightweight debris, used in camera for the Paris café explosions (read: artofvfx Inception [§2]) |

### pre-production

| Term | Meaning |
|---|---|
| **Boardomatic** | Boards timed to a track, used before a full animatic; here an animatic was needed far sooner (read: artofthetitle Halt and Catch Fire [§3]) |

### process

| Term | Meaning |
|---|---|
| **Charrette** | A compressed, shotgun-style design sprint; the six-week WTC competition is Frankfurt's example. (read: suckerpunch frankfurt §3) |
| **funnel (creative process)** | start broad with big movements and get more specific; from Austin Shaw's Design for Motion (read: Ordinary Folk §17) |
| **verbal ideation** | word-association lists before sketching (read: designboom Hische §3) |

### production design

| Term | Meaning |
|---|---|
| **Vibranium roads** | Hidden practical detail: roads that look like dirt but let cars maglev. (read: premiumbeat beachler §5) |
| **West Wing me** | Beachler's name for a fast walk-and-decide pass through department work. (read: premiumbeat beachler §5) |

### review

| Term | Meaning |
|---|---|
| **finaling a shot** | lighting DP approves a shot as final before the director sees it (read: fxguide Inside Out §3) |
| **hero shots** | representative frames chosen with the DP to set the look for a sequence (read: motionpictures Volpatto §2) |
| **Seeing through the client's eyes** | Inhofer's name for learning what a client's eye likes in skin tone, sky, brightness, light pools and vignette (read: premiumbeat Inhofer [§5]) |

### rigging

| Term | Meaning |
|---|---|
| **profile movers** | Pixar method where a drawn profile line drives the mouth or shape and the computer solves the points (read: looper §2-§3) |

### title design

| Term | Meaning |
|---|---|
| **Hosts / newcomers** | Westworld's terms for the robots and the human guests. (read: artofthetitle westworld §1) |
| **Main-on-end** | Main title sequence placed at the end of the film. (read: Eye §3 (Across the Universe)) |
| **Milk bath** | The vat in Westworld's title where hosts are formed; the redundant-host idea returns there. (read: artofthetitle westworld §4) |
| **Prologue (film)** | First scene of a film; Cooper named his company for it, taking the idea from Henry V's opening. (read: Eye §1) |

### titles

| Term | Meaning |
|---|---|
| **Multiplane** | Disney's layered-glass camera technique, imitated here with cells and a CG camera (read: fxguide Jungle Book [§11]) |

### typography

| Term | Meaning |
|---|---|
| **Din Mittel** | Medium weight of a DIN face, based on 1931 DIN 1451. (read: semi-permanent §6) |

### vfx

| Term | Meaning |
|---|---|
| **lighting proxy** | a physical stand-in of a creature part shot on set to match lighting reference (read: artofvfx §4) |
| **Tissue** | Weta's finite-element muscle and skin simulation system (read: artofvfx §2) |

### vfx review

| Term | Meaning |
|---|---|
| **draw-over** | annotated frame (circles, arrows, sketched shapes) attached to a VFX note (read: whatsafterthemovie §1) |
| **finaled** | a shot approved by the director; a finaled shot can still come back (read: whatsafterthemovie §1; benmcewan §3) |

### virtual production

| Term | Meaning |
|---|---|
| **Inverse square law (Volume)** | Light from a nearby LED wall falls off faster than distant sky or sun, so exposure and fall-off differ. (read: nfs fraser-deakins §1) |

## Added from discover transcripts (2026-10-30)

Terms heard in the 158 search-picked talks and tutorials. Each meaning ends with where it was heard.


### 3D to AI

| Term | Meaning |
|---|---|
| **Style transfer (grey box)** | render a rough grey 3D shot, then restyle it with a generative video model, keeping camera and timing (heard: dsYggO4lsSo [31:09]) |

### after effects

| Term | Meaning |
|---|---|
| **roving keyframes** | keys that AE spaces automatically along a path to keep motion even (heard: HpVtzOtaHlg [09:20]) |

### agencies

| Term | Meaning |
|---|---|
| **hub and spoke (project)** | a studio at the centre coordinating other agencies and artists across a large campaign (heard: A2EIfXMPmSg [09:29]) |
| **membrane (not silo)** | BUCK's name for departments that give people a home base without walling off work (heard: A2EIfXMPmSg [43:48]) |

### AI VFX

| Term | Meaning |
|---|---|
| **Pixel / frame / shot / multi-shot control** | Beeble's four control levels: what stays, how a frame looks, motion within a shot, matching across shots (heard: weXc-JGwewo [06:21]) |

### ai-models

| Term | Meaning |
|---|---|
| **4DGS / dynamic Gaussian splatting** | splats over time from many synchronised cameras, like video (heard: KZqv3Z5rRg8 [57:06]) |
| **Driving video strength** | how strictly an AI video model follows the control video; lower is freer (heard: 7J7hi-Hxpac [15:31]) |
| **Halo rig** | ten-action-camera capture rig said to be used to train an actor avatar on Sinners (heard: KZqv3Z5rRg8 [51:22]) |
| **NVFP4** | NVIDIA 4-bit float format for 50-series tensor cores, smaller and faster than FP8 (heard: 7J7hi-Hxpac [12:57]) |
| **spherical harmonics degree** | per-splat view-dependent colour order; lowering it saves a lot of VRAM on non-reflective subjects (heard: QW8ec3qquHA [24:47]) |
| **SSIM** | structural similarity index, a score of how closely a trained splat matches the source images (heard: QW8ec3qquHA [23:13]) |
| **unscented transform (3DGUT)** | method that lets splatting handle non-pinhole lenses and secondary lighting (heard: KZqv3Z5rRg8 [25:47]) |

### animation

| Term | Meaning |
|---|---|
| **Baked animation clip** | Animation baked from a rig into a clip with version data, used in the main edit instead of live constraints. (heard: hc6xf-3uDX8 [26:21]) |
| **Playblast** | a viewport preview render of a shot used for review (heard: jiXB5X1S1AI [19:19]) |
| **Pre-roll / post-roll** | Extra animated frames before and after a shot's cut so later edit changes still work. (heard: hc6xf-3uDX8 [20:39]) |
| **Shot sculpt** | A morph target sculpted for particular frames of one shot to fix a deformation problem. (heard: hc6xf-3uDX8 [38:47]) |

### animation/layout

| Term | Meaning |
|---|---|
| **ground contact** | keeping a character's feet on the changing set surface throughout production (heard: aR3yNNGK_sc [19:08]) |

### art direction

| Term | Meaning |
|---|---|
| **color script** | strip of colour/lighting paintings per beat that syncs everyone's imagination of the film (heard: Vj2OAptTQD4 [03:44]) |

### brief and pitch

| Term | Meaning |
|---|---|
| **Fast / first / final pixel** | Ryan Summers' three uses of AI: quick iteration, a story-setting first frame, the shipped frame (heard: dsYggO4lsSo [34:14]) |

### broadcast

| Term | Meaning |
|---|---|
| **3:2 pulldown** | uneven repeat of 24 fps frames (3, 2, 3, 2) on a 60 Hz display, causes judder (heard: oEOkjYnsTMs [00:34]) |
| **3D fullframe** | full-frame graphic floating in 3D space (heard: 2DoF-oYNQgU [16:13]) |
| **3Play** | Vizrt instant-replay system, 8 channels in and 2 out (heard: bp5L3VpHYD0 [21:07]) |
| **Cable cam** | camera flown on cables over the field via X, Y and Z winch motors, controlled with a joystick, with a roll axis for the horizon (heard: u_V8IlitveE [02:40]) |
| **Colour chips** | The set of team colour swatches that feed every element; the only source of colour in the toolkit. (heard: YiMh6bEebIs [20:15]) |
| **Controller (Remote Control)** | An integer with conditions that sets a few allowed options on a scene, e.g. 0 red, 1 green. (heard: XAtjoawRN_Y [29:00]) |
| **Data Link (Unreal)** | pulls external data (sheet, HTTP, table) into graphics fields (heard: QWT8IAUfWSk [32:58]) |
| **Digital twin (stadium)** | full-scale 3D model of a venue used to test AR graphics and tracked cameras (heard: 2DoF-oYNQgU [11:00]) |
| **Directors (sub-timelines)** | Broadcast graphics term for several timelines inside one graphic, giving options within it. (heard: XAtjoawRN_Y [27:50]) |
| **EVS** | live replay server; operators call plays back within seconds of the whistle (heard: u_V8IlitveE [06:49]) |
| **field ID** | key that binds a remote-control property to a rundown slot (E101...) (heard: QWT8IAUfWSk [35:15]) |
| **Ghost frame** | Technique that lets several live cameras each see their own perspective on one LED wall; the 'secret sauce' of Fox's studio. (heard: XAtjoawRN_Y [04:57]) |
| **Hype chamber** | Rocket League's swappable pre-match graphic environment rebuilt in Unreal as a downloadable sample. (heard: XAtjoawRN_Y [11:53]) |
| **K-zone** | ESPN's tracked strike-zone box graphic (heard: qkWWcjeL_zM [05:23]) |
| **Layer alias** | A graphic's layer type (full screen, slab, lower third) that tells the rundown what to remove when it comes in. (heard: YiMh6bEebIs [1:31:40]) |
| **media profile (Unreal)** | asset that holds SDI input/output and genlock settings (heard: bcL001ZFHBQ [44:32]) |
| **micro-judder** | small stutter from frames dropped by a TV's de-judder processing (heard: oEOkjYnsTMs [03:43]) |
| **Path behavior** | Unreal remote-control behavior that builds a content path from inputs (sport, league, team code) to swap assets by name. (heard: YiMh6bEebIs [1:12:21]) |
| **RC (remote control) controller** | Unreal object that gives an exposed property a field ID for rundown pages (heard: QWT8IAUfWSk [45:11]) |
| **Ready one, take one** | director's live call: ready cue then cut to camera one (heard: u_V8IlitveE [04:15]) |
| **reverse pulldown (inverse telecine)** | a TV detecting the 3:2 pattern in a 60 Hz signal to show the original 24 frames (heard: CuEZIJDEQyo [02:12]) |
| **Rundown** | The run-of-show list of graphics page templates that the operator previews and takes to air. (heard: YiMh6bEebIs [24:26]) |
| **Scene rig** | A shared sublevel of lights (and sometimes camera) used by many graphic levels to avoid light pops between them. (heard: YiMh6bEebIs [1:40:27]) |
| **scene state (Unreal)** | state-machine system for score bugs and tickers (heard: QWT8IAUfWSk [28:44]) |
| **Slab** | A side-panel style broadcast graphic (player bio or stats) that sits beside the action. (heard: YiMh6bEebIs [47:52]) |
| **Stop point / continue** | Cue marks on a live graphic's timeline: play to a point, hold, then continue on an operator's cue. (heard: XAtjoawRN_Y [27:20]) |
| **sublayer (broadcast graphics)** | an on-air element such as header, ticker or footnote with its own in and out animation inside one scene (heard: 5P-sO_2aiwU [24:50]) |
| **Timed Data Monitor** | Unreal panel that shows genlock/timecode timing (heard: bcL001ZFHBQ [46:36]) |
| **transition logic (Unreal)** | layer-based system that animates only the changed region of a graphic (heard: QWT8IAUfWSk [16:03]) |
| **Translucent sort priority** | Unreal modifier that stacks 2D layers on one plane by layer order, avoiding small depth offsets. (heard: YiMh6bEebIs [56:08]) |
| **tricode** | three-letter team code used as the row key for a team's data (heard: bcL001ZFHBQ [17:35]) |

### business

| Term | Meaning |
|---|---|
| **Jevons paradox** | When a costly thing gets cheaper to make, total demand for it grows instead of shrinking. (heard: 0Uxq1IEKpFE [03:05]) |

### comp

| Term | Meaning |
|---|---|
| **ACES-compliant EXR** | One frame per file, 16-bit half, compressed, ACES2065-1, no baked look, ACES metadata flag set. (heard: Y2mcVM8c7cA [25:09]) |
| **ACEScc / ACEScct** | Log ACES spaces meant for colourists, not for compositing. (heard: Y2mcVM8c7cA [11:36]) |
| **AP0 / ACES2065-1** | ACES primaries wide enough to hold every visible colour; the exchange and archive space and the space of compliant EXRs. (heard: Y2mcVM8c7cA [08:58]) |
| **AP1 / ACEScg** | Smaller ACES primaries made for VFX and CG; the linear working space (Nuke's 'scene linear' under the ACES config). (heard: Y2mcVM8c7cA [09:31]) |
| **beauty rebuild passes** | passes (material AOVs, light groups) that add up to the beauty (heard: UCUXhXKDnWQ [00:30]) |
| **CLF (Common LUT Format)** | Academy XML format for a chain of simple LUT and matrix operators (heard: 7e0SSka8Ar8 [15:12]) |
| **ContactSheetAuto** | Nuke gizmo that arranges connected inputs into a grid automatically (heard: UCUXhXKDnWQ [12:02]) |
| **CTF** | OCIO extension of CLF that can store every OCIO operator (heard: 7e0SSka8Ar8 [52:21]) |
| **data passes** | helper passes (utilities and IDs) used for effects, not rebuilds (heard: UCUXhXKDnWQ [01:01]) |
| **Deep holdout** | Using depth-aware data to hide one element behind another in comp, e.g. fog held out by a foreground. (heard: ETV1VTV0vNg [31:42]) |
| **Deflicker** | Removing frame-to-frame brightness or detail flicker from AI-made passes, e.g. with a CopyCat network. (heard: NaCJiquNnYY [26:04]) |
| **display color space (AE)** | view-only transform in After Effects ACES; never applied to exports (heard: x2sx-P5f-iM [04:41]) |
| **file rules / viewing rules** | OCIO v2 rules that pick default colour space by path and suggest views (heard: 7e0SSka8Ar8 [16:45]) |
| **First light** | The colourist's initial base grade applied before creative looks. (heard: Y2mcVM8c7cA [20:01]) |
| **Fog glow** | A glare type that gives a soft wide bloom rather than streaks. (heard: Jwl48psPrxU [05:10]) |
| **Frequency separation** | splitting an image into fine detail and smooth tone so detail can be restored without changing lighting (heard: weXc-JGwewo [26:48]) |
| **Glow under/over, blur under/over** | DillonGoo's two-letter naming telling a script where an FX pass sits relative to the character (heard: aDsyNfISVLA [35:04]) |
| **IDT (input device transform)** | The ACES step that moves a camera, scan or other image into the ACES space; every source has its own. (heard: Y2mcVM8c7cA [14:12]) |
| **Light pass** | A render of one light's effect that is added into the diffuse of its AOV, not placed over the beauty. (heard: NaCJiquNnYY [22:23]) |
| **LMT** | Look Modification Transform: ACES term for a show look that changes the starting point of the pipeline (heard: uaynELBZdSE [01:43]) |
| **LMT (look modification transform)** | The ACES step between IDT and ODT that carries the creative look: CDL, first-light grade, presets, trim. (heard: Y2mcVM8c7cA [17:18]) |
| **Look ID** | a tag grouping shots that share a grade and effects, so they can be comped together (heard: aDsyNfISVLA [32:27]) |
| **Look-LUT** | a LUT applied in ACEScct that stands in for an ACES LMT because Resolve cannot export a true LMT (heard: uaynELBZdSE [02:18]) |
| **Merged AOVs** | all passes written into one multi-layer EXR per frame (heard: xwD_UPqbmCU [01:36]) |
| **ODT (output device transform)** | The ACES step that maps the working image to a display such as sRGB, Rec.709, Rec.2020 or P3. (heard: Y2mcVM8c7cA [16:20]) |
| **Pixel fudging** | Debating details nobody will see in a review. (heard: FW942ZgK8Ic [26:26]) |
| **Post comp** | Hugo Guerra's joke name for the small grade comp built on a pre-rendered float EXR of the full comp. (heard: FW942ZgK8Ic [40:58]) |
| **Pref (reference position)** | A per-pixel rest-pose position that stays fixed as the object moves, for stable masks. (heard: NNUtKYRmcjY [13:01]) |
| **Reference Gamut Compress** | ACES 1.3 option that pulls out-of-gamut saturated colours back inside the working space (heard: drEi66Xj5Hg [08:49]) |
| **scene-referred** | footage (raw, log) that keeps scene light values; display-referred discards them for viewing (heard: aJF2sAjRsy0 [06:16]) |
| **Shader rebuild** | Recombining separate light passes into the beauty so each part can be graded alone. (heard: ETV1VTV0vNg [02:03]) |
| **tetrahedral interpolation** | more accurate 3D LUT interpolation than trilinear; GPU-supported in OCIO v2 (heard: 7e0SSka8Ar8 [40:50]) |
| **TMI (Nuke colour picker)** | Temperature, magenta, intensity sliders; change colour without changing brightness. (heard: ZrOiwMSGmIw [35:15]) |
| **Trim pass** | A final adjustment layered after converting a grade from HDR to SDR, treated as one more look transform. (heard: Y2mcVM8c7cA [21:34]) |
| **view transform (OCIO v2)** | step from scene-linear to a display reference space, before the display colour space (heard: 7e0SSka8Ar8 [17:46]) |
| **Viewer process (input process)** | A node chain shown only in the viewer (named viewer_input in Nuke) that previews a look without changing pixel values. (heard: Y2mcVM8c7cA [48:33]) |
| **ZDefocus** | Nuke's depth-driven blur, focused by picking a depth point. (heard: ETV1VTV0vNg [38:43]) |

### edit

| Term | Meaning |
|---|---|
| **eye fix** | where the viewer's eye sits at the start of a shot compared with the end of the last; good cuts keep them close (heard: Vj2OAptTQD4 [26:47]) |

### education

| Term | Meaning |
|---|---|
| **AI slop** | Output made when judgement and taste are delegated to the model. (heard: SCQt6B96DSs [27:10]) |

### finishing

| Term | Meaning |
|---|---|
| **image finaling** | final cleanup of popping, buzzing and smudge artefacts in rendered frames (heard: ru0tQRJ4qKs [13:46]) |

### layout

| Term | Meaning |
|---|---|
| **anim prep** | step that swaps proxy characters for high-res versions and sets start poses before animation (heard: ru0tQRJ4qKs [07:52]) |

### layout/previz

| Term | Meaning |
|---|---|
| **alts** | alternate camera or staging setups pitched for the same shot (heard: Vj2OAptTQD4 [10:05]) |

### lighting

| Term | Meaning |
|---|---|
| **Bank** | A group of lamps on one circuit in a multi-lamp unit, e.g. six bubbles to a bank. (heard: 2gaibYk1Cro [08:57]) |
| **Bubble** | One lamp of a multi-lamp unit such as a Maxi Brute or Dino; 'turn off two bubbles' dims the unit in steps. (heard: 2gaibYk1Cro [07:23]) |
| **Burger / chip / grenade** | New grip slang: cheeseborough clamp, quarter-round speed-rail piece that protects a square pipe, and speed-rail starter. (heard: 2gaibYk1Cro [17:18]) |
| **Cookie (cucoloris)** | patterned board in front of a light to cast dappled shadow (heard: r2nD_knsNrc [12:24]) |
| **Cup block / candlestick** | Rigging parts: a steel pipe fitting that takes a light's pin, and a notched block that stops it kicking out in a lift basket. (heard: 2gaibYk1Cro [13:34]) |
| **Digital diffusion** | Lens filter that softens skin and gently blooms highlights without a visible halo; graded 1 to 7 by lens width. (heard: 2gaibYk1Cro [21:36]) |
| **EV (exposure value)** | A scale of camera exposure; a noon sun pairs with about EV 14. (heard: nlbJwMoj1Dg [12:29]) |
| **Frustum** | The camera-matched window an LED volume renders in correct perspective; the rest of the wall shows ambient light. (heard: aKRcGoc_osQ [22:18]) |
| **key plus fill to fill ratio** | the more accurate key-to-fill ratio, since fill also reaches the key side (heard: 0CEVwgxs5XY [22:20]) |
| **Local exposure** | Tone-mapper control that lifts or lowers only the shadows or highlights, not the whole image. (heard: nlbJwMoj1Dg [15:41]) |
| **low key / high key (cinematography)** | defined by background exposure, not the subject (heard: p7X4PTImbZ4 [02:45]) |
| **Lux** | Light arriving on a surface, one lumen per square metre. (heard: nlbJwMoj1Dg [04:14]) |
| **Mimic** | RGBW LED panel (400 W) that plays low-res video as interactive light. (heard: aKRcGoc_osQ [25:55]) |
| **Moire (LED wall)** | Shimmering pattern when camera sensor grid aligns with the screen's pixel grid; avoid by defocusing the wall. (heard: aKRcGoc_osQ [20:40]) |
| **Multiple importance sampling** | sampling both light and surface to cut variance; on by default for lamps (heard: 0amlKMClE4s [12:43]) |
| **outside / inside lighting** | light between subject and background (mysterious) versus between subject and camera (revealing) (heard: si7UAgvBd4Y [09:26]) |
| **Portal light** | a window-shaped light that tells the renderer to sample the world there, not the light itself (heard: 0amlKMClE4s [13:15]) |
| **Ray reconstruction** | Nvidia's AI denoiser for path-traced frames, bundled with DLSS 3.7. (heard: zD9kS1nOuyU [32:17]) |
| **ReSTIR** | Reservoir-based sampling that reuses light samples from neighbour pixels and earlier frames. (heard: zD9kS1nOuyU [04:15]) |
| **sequence lighting** | lights applied to every shot of a sequence, with shot lighting added on top as a sublayer (heard: CpiumJctktM [22:11]) |
| **sider** | a flag at the side of a key light to limit spill on the background (heard: 0CEVwgxs5XY [25:03]) |
| **Smart side / short side** | lighting the side of the face turned away from the camera, for a more dramatic look (heard: r2nD_knsNrc [08:05]) |
| **Sunny-side-up flare** | Hurlbut's name for the Kowa flare: golden centre inside a whitish-yellow halo. (heard: 2gaibYk1Cro [26:24]) |
| **Toe / shoulder** | The low (shadow) and high (highlight) ends of a tone-mapping curve. (heard: nlbJwMoj1Dg [14:37]) |
| **topper** | a flag or net on a high front light that cuts the beam hitting the background without affecting the subject (heard: 0CEVwgxs5XY [03:17]) |
| **umbra / penumbra** | the dark core of a shadow and its fuzzy edge; soft light has mostly penumbra (heard: 0CEVwgxs5XY [12:09]) |
| **Upstage lighting** | key light placed behind the eyeline (180 line) away from the camera side, giving Rembrandt-style modelling (heard: jAz4Lb93gwY [14:27]) |

### lookdev

| Term | Meaning |
|---|---|
| **Blast furnace look** | Slang for gold reflecting gold until a set looks burnt. (heard: NNUtKYRmcjY [15:36]) |
| **chatoyance** | stretched shimmering highlight from fibre structure, as in some woods (heard: UjThhVMuV18 [00:00]) |
| **Curvature mask** | A mask from surface bend: convex picks edges, concave picks crevices. (heard: -lpj38Cql4c [19:48]) |
| **Edge tint** | The colour a metal shows at grazing angles, different from its face-on colour. (heard: -lpj38Cql4c [03:46]) |
| **Light mixer / snapshot** | One panel for all lights in a stage; and a saved copy of the whole network plus render to revert to. (heard: cE-Bbdspu_8 [2:18:36]) |
| **LPE tag (light path expression)** | A tag on a light that splits the beauty pass per light for re-balancing in comp. (heard: cE-Bbdspu_8 [2:33:32]) |
| **nested dielectric** | overlapping solids of different IOR (glass and liquid) resolved by the renderer (heard: Bbj18-933Vg [06:14]) |
| **Start node** | In the Redshift node graph, the group whose controls show when its preset is applied. (heard: -lpj38Cql4c [40:44]) |
| **VDF / EDF** | MaterialX volume slots: absorption/scattering for smoke, and emission for fire. (heard: cE-Bbdspu_8 [2:14:01]) |

### motion

| Term | Meaning |
|---|---|
| **avars** | animation variables, the hinges and controls on a Pixar character rig (up to about 1000) (heard: fT_LdcWFHkA [07:47]) |
| **Boil** | the shimmer of a rough cutout edge re-randomised each frame or few frames, imitating hand animation (heard: pfapONWRaHc [09:22]) |
| **free placement cloner** | Unreal cloner where hand-placed actors pop into place (heard: QWT8IAUfWSk [23:18]) |
| **geometry mask (Unreal)** | modifier that cuts or reveals through layers with animated geometric shapes, like After Effects shape masks (heard: 5P-sO_2aiwU [27:25]) |
| **judder** | uneven frame time (for example 3:2 pulldown), distinct from stutter (heard: CuEZIJDEQyo [00:08]) |
| **media texture (Unreal)** | video clip played as a live texture inside a material (heard: 5P-sO_2aiwU [15:42]) |
| **Multiples** | Duplicate limbs offset on a fast move to sell speed, like a smear built from extra geometry. (heard: hc6xf-3uDX8 [32:29]) |
| **Optical printer** | machine that rephotographs film strips onto another to layer elements; slow, errors force a restart (heard: pfapONWRaHc [03:46]) |
| **Protron** | Unreal media option that makes ProRes scrub accurately (heard: QWT8IAUfWSk [37:21]) |
| **Rostrum camera** | camera over a flat table photographing artwork frame by frame; classic title-sequence method (heard: pfapONWRaHc [03:14]) |
| **Separate dimensions** | After Effects option that splits position into X, Y and Z properties so each gets its own curve (heard: AG19fyRcOkA [08:46]) |
| **Speed graph vs value graph** | After Effects' two graph editors: curve height as speed, versus height as value (steepness is speed) (heard: AG19fyRcOkA [06:31]) |

### pipeline

| Term | Meaning |
|---|---|
| **animation bank** | character facial expressions and cycles built once and reused in shot animation (heard: AiRjt7nWcZc [20:45]) |
| **Asset resolver** | A USD plugin that turns asset-path strings into real file locations; the one part that needs compiled code. (heard: VSE7ayrRStg [26:47]) |
| **Blacklist (farm node)** | Excluding a misbehaving machine from receiving jobs. (heard: FNhUnPWzVaw [41:55]) |
| **Breakdown list** | production list of the assets each shot needs, used to populate shot files (heard: 4R8PduY_vV4 [20:28]) |
| **Cache placer crowd** | Background crowd made from a few pre-simulated agents scattered with variants, with no per-shot simulation. (heard: jpbMbafS9FY [30:37]) |
| **casting (Milk)** | listing the placeholders a shot needs before any version exists (heard: XfMp13jOSxE [14:30]) |
| **Chunk size** | How many frames a farm node renders before asking the master for more. (heard: FNhUnPWzVaw [45:05]) |
| **Class prim** | USD prim that assets inherit from, so edits made there reach every instance later. (heard: TLJPDt4YpYM [21:22]) |
| **collection (USD)** | a named group of prims stored in the USD file, recalled with a percent sign (heard: hBYSHFRnFlo [50:24]) |
| **Component builder** | a Houdini node that makes a best-practice USD asset with geometry, material and variants (heard: bwkCfp6G-F8 [19:33]) |
| **composition arcs** | USD layering tools: sublayers, references, payloads, inherits, specializes, variants (heard: XfMp13jOSxE [14:30]) |
| **Concurrent tasks** | In Deadline, how many tasks one worker runs at the same time. (heard: v083eMXSwXw [22:23]) |
| **Context playblast** | a playblast joined with the neighbouring shots so timing and continuity can be judged (heard: aDsyNfISVLA [22:21]) |
| **department layer** | one USD file written by one department (modeling, layout, animation, FX, lighting) and referenced by a container (heard: CpiumJctktM [03:08]) |
| **Editor Utility Widget** | small in-editor tool built like a UI widget, used here to batch queue renders (heard: bcL001ZFHBQ [39:44]) |
| **Frame-change handler** | A script that runs on every frame change, e.g. to apply keyed custom properties. (heard: W01lQrcCz9s [24:55]) |
| **Frames per task** | In Deadline, how many frames one task renders; very high for simulations so they run in one go. (heard: v083eMXSwXw [21:18]) |
| **Genlock** | Sync signal locking camera sensor, render nodes and screens to the same frame timing to prevent tearing. (heard: aKRcGoc_osQ [16:27]) |
| **Graph state variable** | Katana variable that switches lighting or material setups so several variations can be rendered or viewed (heard: xCk4BO4WoTI [12:39]) |
| **hero version** | the single published latest version of an asset that shots link to, so a new publish updates every shot (heard: AiRjt7nWcZc [27:06]) |
| **husk** | Houdini's command-line renderer for USD files; usdrecord is a second command-line option. (heard: TLJPDt4YpYM [51:15]) |
| **Hydra** | USD's viewport and render abstraction that lets one scene be shown by many renderers (Storm, RenderMan). (heard: TLJPDt4YpYM [06:49]) |
| **Impostor card** | camera-facing plane with a shader that shows an object from many angles; a cheap LOD for distant objects (heard: ofTjypijLEU [00:00]) |
| **Instanceable reference** | USD instancing mode where each copy can be edited, at a memory cost compared with point instancing. (heard: cE-Bbdspu_8 [1:26:30]) |
| **Kind (USD)** | Cheap metadata on a prim used to filter and select quickly; studios add their own kinds in JSON. (heard: VSE7ayrRStg [25:13]) |
| **Kind: component / assembly / group** | USD tags for a finished asset, components combined, and an arbitrary set. (heard: cE-Bbdspu_8 [28:05]) |
| **Layer break** | A Houdini LOPs step that starts a new USD layer so edits stay fast and branches do not load content twice. (heard: VSE7ayrRStg [51:25]) |
| **Library override** | Blender's way to edit a linked asset (like a rig) without breaking the link (heard: aDsyNfISVLA [08:42]) |
| **Load shot node** | Solaris node that brings in everything pushed for a shot (camera, layout, animation, FX) in layer-department order. (heard: jpbMbafS9FY [24:03]) |
| **LOPs** | Houdini node type that composes a USD stage inside Solaris (heard: hBYSHFRnFlo [00:31]) |
| **Manifest** | Union VFX's name for the versioned USD description of a shot or sequence (others say bundle or package). (heard: nUXfEdZ-7Xs [12:01]) |
| **master version** | a published copy that always equals the highest version so imports need no repointing (heard: CpiumJctktM [07:46]) |
| **MaterialX** | Renderer-neutral shader standard, 'USD for materials'. (heard: cE-Bbdspu_8 [34:44]) |
| **MBrew** | Milk's API over ShotGrid for casting published USD (heard: XfMp13jOSxE [16:02]) |
| **media playlist** | list of versions queued for a daily or client review (heard: GE6Af6hjYfI [17:20]) |
| **Meta strip** | a Blender sequencer strip that wraps shot clips and carries the shot's name and length to the tracker (heard: jiXB5X1S1AI [12:02]) |
| **MPC (Material Parameter Collection)** | shared colour/vector store that every material in Unreal can read (heard: bcL001ZFHBQ [11:15]) |
| **Multi-prop** | An asset package built from instanced references of other props (a pile of crates) with its own variants. (heard: jpbMbafS9FY [20:19]) |
| **packed USD** | USD geometry held as one point carrying all data to save memory (heard: hBYSHFRnFlo [07:48]) |
| **Payload (USD)** | A file in an asset that stores a bounding box so the asset can be unloaded from the scene. (heard: cE-Bbdspu_8 [1:05:53]) |
| **Pipeline log (push/pull)** | a file recording who pushed or pulled each pipeline file and when, used to warn others (heard: aDsyNfISVLA [18:05]) |
| **Point instancer** | USD's copy-to-points: arrays of positions, orientations and scales plus a list of prototype prims. (heard: VSE7ayrRStg [42:45]) |
| **pre-roll (sim)** | extra frames before the shot starts so a simulation settles; Spring starts files at 101 (heard: aR3yNNGK_sc [24:27]) |
| **Prim** | A node in a USD scene hierarchy at a path; holds properties (attributes and relationships). (heard: VSE7ayrRStg [08:56]) |
| **prim (primitive)** | any thing in a USD scene: geometry, light, camera, shader, render settings (heard: USD Basics hBYSHFRnFlo [02:05]) |
| **Prim (USD primitive)** | Any element of a USD stage: mesh, light, camera, material scope, group. (heard: cE-Bbdspu_8 [26:32]) |
| **Primvar** | A variable stored on a USD prim: colour, normals, UVs, velocity or a custom mask; Houdini calls it an attribute. (heard: cE-Bbdspu_8 [1:50:16]) |
| **Principal shot** | A never-rendered scene linked to many shots; edits made there are pushed to all connected shots, with shot switches for per-shot exceptions. (heard: jpbMbafS9FY [25:58]) |
| **publish area** | folder where released asset versions are copied apart from artists' working files (heard: AiRjt7nWcZc [29:13]) |
| **Purpose (USD)** | A tag (render, proxy, guide) so a viewport can load a light stand-in while rendering uses the full-res version. (heard: TLJPDt4YpYM [37:48]) |
| **push / pull (asset update)** | push: shots auto-update when an asset is published; pull: each shot repoints to a new version by hand (heard: AiRjt7nWcZc [26:02]) |
| **Push pipeline** | Assets and shots update automatically in downstream scenes when a department publishes, as opposed to pull (artist chooses to update). (heard: jpbMbafS9FY [09:04]) |
| **Rez** | Open-source tool that resolves a package list into a runtime environment per shot. (heard: HuV0_AbDgYk [20:03]) |
| **sandbox (folder)** | shared temporary folder inside a project for stray files (heard: MtFYQx3Jq5E [07:20]) |
| **Scene Capture camera** | engine camera that renders a hidden space to a texture used on screens (heard: bcL001ZFHBQ [08:07]) |
| **Scene description** | The renderer-specific file between a scene and its picture (.ifd, .rib); USD replaces them with one shared form. (heard: cE-Bbdspu_8 [12:29]) |
| **Show / sequence / shot / task** | Method Studios' work hierarchy: project, a story chunk, one camera move, and the type of work on a shot. (heard: HuV0_AbDgYk [02:43]) |
| **SLAM scanner** | handheld multi-camera/lidar scanner that maps a space as you walk (heard: KZqv3Z5rRg8 [11:37]) |
| **software pipeline** | which apps, versions and file formats connect departments (heard: MtFYQx3Jq5E [19:13]) |
| **spherical harmonics (splat)** | coefficients (0 to 3) letting a splat's colour change with view angle (heard: ERuRMOVO58Q [07:47]) |
| **stage** | the composed USD scene context where LOPs nodes are laid down (heard: hBYSHFRnFlo [00:31]) |
| **Stage Manager** | Houdini Solaris node that gathers and tidies assets into one USD scene (heard: bwkCfp6G-F8 [23:42]) |
| **Storm (Hydra Storm)** | Pixar's built-in real-time Hydra renderer used for viewports (heard: GE6Af6hjYfI [34:24]) |
| **story reel** | storyboards cut into an animatic with scratch sound and temporary dialogue (heard: fT_LdcWFHkA [00:35]) |
| **structure from motion (SfM)** | step that solves where each camera was, the skeleton for splat or photogrammetry reconstruction (heard: KZqv3Z5rRg8 [10:35]) |
| **Take (Houdini)** | A saved set of parameter overrides for rendering variants. (heard: NNUtKYRmcjY [17:10]) |
| **take letter** | trailing letter on a shot name marking an alternate version of the shot (heard: aR3yNNGK_sc [22:15]) |
| **task layer (live/locked)** | Blender Studio asset data domain that is updated by publishes (live) or frozen for old versions (locked) (heard: IBTEBhAouKc [11:01]) |
| **Time-dependent node** | A node that must recook each frame; USD time samples let it be avoided by caching the whole range. (heard: VSE7ayrRStg [36:53]) |
| **USD container** | the USD file for an asset or shot that references all its department layers (heard: CpiumJctktM [03:08]) |
| **USDA / USDC** | Text (readable) and binary (small, fast) forms of a USD file. (heard: cE-Bbdspu_8 [18:08]) |
| **usdc / crate** | binary USD format: faster, smaller, not readable (heard: hBYSHFRnFlo [10:58]) |
| **usdcat** | USD command-line tool; can flip a .usd between ASCII and binary (heard: hBYSHFRnFlo [13:59]) |
| **USDZ** | Zip-style package holding a USD file and its textures for transport. (heard: nUXfEdZ-7Xs [13:02]) |
| **value clips (USD)** | stitched time-varying data resolved at render via manifest and template (heard: XfMp13jOSxE [26:24]) |
| **Variant set** | Alternatives stored inside one USD asset (geometry, material, light) that you switch in the scene graph. (heard: cE-Bbdspu_8 [57:36]) |
| **VFX round trip** | test pull of show footage through every vendor/post hop before real work starts (heard: qlqiBNsqNps [00:18]) |
| **work vs publish** | editable version vs the stable file other departments reference (heard: MtFYQx3Jq5E [09:56]) |
| **Xform / scope** | USD prim types: a movable parent, and a non-moving parent used for materials. (heard: cE-Bbdspu_8 [27:34]) |

### pitch

| Term | Meaning |
|---|---|
| **Rip-o-matic** | A pitch edit made from clips of other films and ads to sell an idea before shooting. (heard: 0Uxq1IEKpFE [40:13]) |

### production

| Term | Meaning |
|---|---|
| **Fake UI** | Invented screen graphics for film and TV, now sometimes run live on the set screen. (heard: 0Uxq1IEKpFE [30:12]) |
| **Showrunner** | A creative lead who directs the directors across many episodes. (heard: W01lQrcCz9s [02:52]) |

### redshift

| Term | Meaning |
|---|---|
| **temporal noise** | noise that differs between consecutive frames, causing flicker even after spatial denoise (heard: jyGQIKOPwGA [00:32]) |

### render

| Term | Meaning |
|---|---|
| **Blue noise sampling** | a noise pattern arranged so denoisers can clear it better (heard: 0amlKMClE4s [23:20]) |
| **Lightspeed** | Pixar team that makes shots render faster without changing the intent (heard: Vj2OAptTQD4 [24:09]) |
| **sample merging** | render a small chunk of samples, check, then render more samples with an offset and merge the passes on the farm (heard: aR3yNNGK_sc [33:40]) |
| **Sample-count pass** | a pass showing how many samples each pixel took before the noise threshold stopped it (heard: 0amlKMClE4s [30:46]) |

### story

| Term | Meaning |
|---|---|
| **fishbowl** | Pixar story room where boards are pitched with voices (heard: Vj2OAptTQD4 [02:07]) |

## Added from polish videos (2026-10-30)

Terms heard in talks and interviews by the polish roster. Each meaning ends with where it was heard.


### agencies

| Term | Meaning |
|---|---|
| **Agency of record** | The single main agency a brand hires for its marketing; tech companies dropped it and hired makers directly. (heard: C1kd07_lR-4 [18:19]) |
| **Buckers** | Staff of Buck, used for counting artists on a job. (heard: NzwG2h_cbrk [38:08]) |
| **Spotted soldiers** | Cooper's Henry V image: a team of flawed people, so the idea must work with them rather than with an ideal crew. (heard: d9pT_zab-MA [20:57]) |
| **Tone meeting** | A pre-production meeting where department heads agree the look and are told to flag anything off-look (heard: DZM-0voWWtw [1:12:07]) |
| **Variety show approach** | Buck's way of starting a passion project: each creative director pitches a technique to try, then a script is built from the best cores. (heard: NzwG2h_cbrk [16:06]) |
| **Visioning** | Early work imagining what a client's product could look like and do in about five years. (heard: C1kd07_lR-4 [14:54]) |

### agency practice

| Term | Meaning |
|---|---|
| **Applied AI studio** | Erlingsson's term for a studio that builds tools and pipelines around models for clients, not only deliverables. (heard: XnaT-aJQZM0 [1:25:53]) |
| **Buckyback** | Buck's weekly vote on hashtagged Instagram work from outside artists; top picks are featured. (heard: 0GInMbR0khg [36:09]) |
| **Scamping** | A quick rough sketch of an idea to show direction before real production. (heard: wog1-B9W1Js [25:54]) |
| **Spark deck** | Buck's shared deck where anyone adds ideas, reviewed in a weekly meeting. (heard: 0GInMbR0khg [13:41]) |

### AI

| Term | Meaning |
|---|---|
| **LoRA** | A small add-on trained on top of a model to teach it one specific behaviour or style. (heard: XnaT-aJQZM0 [46:16]) |

### AI / motion

| Term | Meaning |
|---|---|
| **Seamless morph transition** | A generated clip that moves from one still to another without a cut, used as a keyframe-pair effect. (heard: XnaT-aJQZM0 [49:50]) |

### ai-models

| Term | Meaning |
|---|---|
| **Captioning strategy** | Choice of how much text goes with each training clip (none, short, essay) (heard: https://www.youtube.com/watch?v=ktSEt_8T9MA [52:52]) |
| **Moondream** | Open vision model that finds named objects in an image and returns boxes (heard: https://www.youtube.com/watch?v=4xS4LOn3CTE [54:38]) |
| **Trigger word** | Word in training captions that makes a LoRA switch on whatever the captions left unnamed (heard: https://www.youtube.com/watch?v=ktSEt_8T9MA [57:28]) |

### any

| Term | Meaning |
|---|---|
| **reverse justification** | after an intuitive reaction, work backwards to why it feels that way (heard: tLLqE6Ia8-U [30:07]) |

### bid

| Term | Meaning |
|---|---|
| **price bracketing** | quote a range with the high figure first so the client anchors on it (heard: m_pGpH_kt4w [05:49]) |

### broadcast

| Term | Meaning |
|---|---|
| **Ident** | A short branded clip a channel plays between shows. (heard: njXzShJ5Dws [04:34]) |
| **Motion smoothing** | A TV frame-interpolation setting; colourists want it off (heard: cMBsxg1hVls [05:21]) |

### business

| Term | Meaning |
|---|---|
| **Color finish house** | A post facility focused on final colour and finishing rather than offline edit. (heard: EqeLzIczV3w [16:34]) |

### c4d

| Term | Meaning |
|---|---|
| **Pin material tag** | Cinema 4D tag that lets a texture follow a deformer such as a twist (heard: y71sbUExVTQ [08:57]) |

### camera

| Term | Meaning |
|---|---|
| **Detachable lens block** | A camera head separated from the body by a cable so the lens and sensor can go into tight spaces. (heard: qYPhjUHTZ9M [24:28]) |
| **Remote head** | Motorised camera head operated at a distance; non-stabilised ones pass vibration to the picture (heard: https://www.youtube.com/watch?v=NmCnE-SL1tU [01:35]) |
| **Ronin gimbal** | A handheld stabiliser used to keep a moving camera steady when track cannot be level. (heard: SljMXrUxylE [10:30]) |
| **Undercranking** | Shooting at fewer frames per second so playback looks faster than real speed (heard: https://www.youtube.com/watch?v=NmCnE-SL1tU [01:05]) |

### capture

| Term | Meaning |
|---|---|
| **MTF** | Modulation transfer function: how much contrast a lens or sensor keeps at fine detail; it caps how far a crop can be pushed. (heard: mtAmXRWXTx0 [16:14]) |
| **Optical low-pass filter** | A deliberate blur in front of a sensor that prevents moire. (heard: mtAmXRWXTx0 [17:15]) |
| **Photosite** | One light-measuring cell on a sensor; larger photosites collect more light and are less noisy. (heard: mtAmXRWXTx0 [22:28]) |

### colour

| Term | Meaning |
|---|---|
| **Creative color science** | Building custom tools, transforms and looks for colorists, as opposed to using stock grading tools. (heard: lt21nZbgkbM [23:23]) |
| **Virtual colours** | Values inside a camera or gamut triangle that lie outside the real spectral locus; they are data with no meaning to the eye. (heard: lt21nZbgkbM [56:43]) |

### colour / finishing

| Term | Meaning |
|---|---|
| **Creative LUT** | A LUT that changes look only, staying in the same colour space (no space conversion). (heard: dSYTWErq0Vw [23:00]) |
| **DCTL** | A small code tool in DaVinci Resolve that computes each pixel exactly instead of using a baked LUT. (heard: dSYTWErq0Vw [59:14]) |
| **Hybrid LUT** | A LUT that adds a look and converts colour space in one file (for example a film print look to Rec.709). (heard: dSYTWErq0Vw [24:31]) |
| **Scene-referred vs display-referred** | Scene-referred: image values tied to light in the scene (wide range). Display-referred: tied to a specific screen (limited range, like a film print). (heard: dSYTWErq0Vw [53:09]) |
| **Technical LUT** | A LUT that only converts between colour spaces, with no look. (heard: dSYTWErq0Vw [22:26]) |

### comp

| Term | Meaning |
|---|---|
| **50/50 look** | Blend of an Alexa-normal LUT and a film-print LUT, giving some filmic tone but not all (heard: yvvXW_fLB6c [29:34]) |
| **Ball Action** | After Effects CC Ball Action: turns pixels into 3D balls; a colour channel can drive its twist (heard: https://www.youtube.com/watch?v=5KYo8zFy1Ew [07:57]) |
| **bloomed blacks** | Defocusing the dark areas a little to mimic duped black-and-white stock (heard: levHA7MwQrA [25:51]) |
| **Colour appearance model** | A model that predicts how colours are perceived so grading controls act perceptually evenly. (heard: 4gQt4PVybPU [39:31]) |
| **colour timer** | Photochemical-era grader who set printer lights; many top colorists trained under one (heard: yvvXW_fLB6c [16:56]) |
| **Knee and shoulder** | The low-mid and high-mid regions of a contrast curve; knee darkens for density, shoulder pushes highlights. (heard: RnSQq3OCNjY [02:03]) |
| **Light wrap** | Background light bleeding onto the edge of a keyed subject. (heard: gNh9r-VbSVg [46:58]) |
| **luminance key** | Matte pulled from brightness instead of colour; used when a colour key is impossible, for example on a black-and-white camera (heard: dqMpPsAGuvw [37:54]) |
| **Power Pin** | After Effects CC Power Pin: a corner pin with an unstretch option, used to flatten and later restore perspective (heard: https://www.youtube.com/watch?v=5KYo8zFy1Ew [13:40]) |
| **Print black** | A black point set slightly above zero so shadows never clip and the image has depth. (heard: RnSQq3OCNjY [04:08]) |
| **Print stock** | The film stock a negative is printed onto, which defines the final colour response. (heard: 4gQt4PVybPU [06:52]) |
| **printer point** | One step of printer-light exposure in photochemical timing; a point of green was a coarse bucket (heard: PcFUgVjswxE [01:33]) |
| **SDR trim of HDR** | Shooting and monitoring wide range, then deriving the SDR version as a trim (heard: dqMpPsAGuvw [45:38]) |
| **split screen (take join)** | Joining parts of two takes in one frame to fix continuity or speed the pace without a cut (heard: GoLrVjL4wgo [40:05]) |
| **The 10 percent** | Kramer's name for small final changes (dust, exposure, curves) that decide whether a composite sells. (heard: Yv4H8Ll1vcc [14:31]) |

### concepting

| Term | Meaning |
|---|---|
| **Mock frames** | Rough collaged frames made to win agreement on an approach, even if the art never ships. (heard: wywwAFOKXug [58:15]) |

### delivery

| Term | Meaning |
|---|---|
| **Film out** | Delivering a finished piece by recording it back to film. (heard: wywwAFOKXug [1:22:07]) |
| **Photochemical finish** | Finishing and timing a film on film stock with no digital intermediate (heard: As2k69rYoN4 [46:28]) |
| **Rec 2020 limited to P3** | Deliverable stored in a Rec 2020 container but graded and clipped inside P3 primaries. (heard: upUAulx7sGI [28:04]) |

### design

| Term | Meaning |
|---|---|
| **stake in the ground** | a fixed style decision that every other element must follow (heard: rwGczakB8w4 [08:57]) |

### edit

| Term | Meaning |
|---|---|
| **Temp track** | Placeholder music used while cutting, which can end up as the final track. (heard: 3_s9du9sDZ4 [18:13]) |
| **Wet clay (film)** | Saying that a film's content stays changeable until very late, so titles made early may need to change. (heard: NqO-PCErlas [29:03]) |

### education

| Term | Meaning |
|---|---|
| **above the fold** | The first screenful a viewer sees before scrolling; portfolio projects must win there (heard: y1QzpLFgtqA [07:48]) |
| **Grade-along** | A training format where the learner grades the same footage as the trainer and sends the project for critique (heard: dPlHag9ilqQ [12:33]) |
| **Insight** | Mixing Light's name for a short single-thought lesson (article, podcast or video). (heard: _xMqdSER7PU [31:54]) |

### film

| Term | Meaning |
|---|---|
| **Pre-flash** | Pre-exposing film to lift shadows and lower contrast; used to match underwater light falloff. (heard: y8Owkb8VreI [28:43]) |

### grade

| Term | Meaning |
|---|---|
| **Creamy vs pingy** | Kelly's scale for highlight roll-off: creamy is a soft shoulder, pingy is hard, near one-to-one bright speculars. (heard: upUAulx7sGI [04:20]) |
| **FPE (film print emulation)** | A setting that limits colour to what a real film print could show. (heard: bpZ3Zuhop5s [13:09, 32:50]) |
| **Gamut limit** | An early input stage that reduces extremely saturated sources such as LED lights. (heard: bpZ3Zuhop5s [07:21]) |
| **Gen 1 / Gen 2 print** | A calculated generic print versus a second-generation print with richer colour and gamut. (heard: bpZ3Zuhop5s [28:45, 31:49]) |
| **Macro beats micro** | Kelly's rule that a fix applying across all shots is better than a shot-level fix. (heard: upUAulx7sGI [13:49, 50:54]) |
| **MPF (Motion Picture Film target)** | Codex target values used to specify and check manufactured film. (heard: bpZ3Zuhop5s [30:47]) |
| **output blanking** | forces legal (16-235) output range so reference and result compare equally (heard: KE085zdpi_I [03:17]) |
| **Skip bleach / ENR** | A bleach-bypass style post process; ENR is a caption spelling and may be wrong. (heard: bpZ3Zuhop5s [13:09, 26:40]) |
| **Subtractive saturation** | Colour richness from a denser negative (exposing down), as opposed to brightness-driven saturation (heard: -7OEzmPfSi0 [58:04]) |
| **Sweet spot (grading)** | The point on the exposure or colour balance control where the image is clearly right and an inch either way is not. (heard: lt21nZbgkbM [1:12:21]) |
| **Toe and shoulder** | The gentle roll-off at the bottom and top of a tone curve. (heard: mtAmXRWXTx0 [29:15]) |

### grade/lens

| Term | Meaning |
|---|---|
| **MTF (modulation transfer function)** | how much contrast a lens keeps as detail gets finer; used to dial lens softness (heard: KE085zdpi_I [42:20]) |

### grading

| Term | Meaning |
|---|---|
| **Unified visual timeline** | Goal that the whole cut looks like one set of eyes saw it, whatever the camera. (heard: KWQCkjr6KuI [25:49]) |

### lighting

| Term | Meaning |
|---|---|
| **Cobra head** | An old-style street light fixture on a bracket; the period source the Mindhunter team matched with sodium colour (heard: DZM-0voWWtw [50:42]) |
| **day for night** | Shooting daylight and treating it dark in post; needs back or side sun to look right (heard: dqMpPsAGuvw [36:21]) |
| **Depron strip** | Thin foam sheet used to soften small LED dots so they photograph well inside a prop or helmet. (heard: N3Pqj1RcpoM [06:56]) |
| **diffraction softness** | Loss of sharpness when a lens iris is closed very far (e.g. T11 to T16); worse in blue light (heard: levHA7MwQrA [19:38]) |
| **Dummy (a light effect)** | Faking the look of a light source, such as a flame, with hidden sources. (heard: ZUg1j3NT3i4 [02:17]) |
| **EL Zone** | Ed Lachman's exposure-zone system used as an alternative to false colour. (heard: GXX7YZPOz7Y [01:33]) |
| **Eyelight** | A small frontal light that puts a bright highlight in the eyes; lets a face sit under-exposed (heard: DZM-0voWWtw [1:17:17]) |
| **Floater panel** | An LED panel on wheels or a stand, moved around the set to fill reflections with plate content (heard: DZM-0voWWtw [17:59]) |
| **follow spot** | Hand-aimed spotlight that tracks a person; used on stages (heard: levHA7MwQrA [52:13]) |
| **Foot-candle** | A unit of light level on a surface; Mindhunter ran about 12 to 15 on the floor (heard: DZM-0voWWtw [28:29]) |
| **fringe (shadow)** | handmade-looking broken texture added at shadow edges (heard: rwGczakB8w4 [29:45]) |
| **Gaffer slash** | A quick strip of light from a gobo'd source that enlivens a background. (heard: ea3-sMoV5EE [08:48]) |
| **Gobo** | Goes before optics: a pattern placed in front of a light to throw shadows (blinds, branches, caustics); in Redshift a map on a spotlight. (heard: mDT94FHPg9c [00:02]) |
| **London Fog diffusion** | A diffusion material placed about four inches in front of LED panels to blur the individual pixels in reflections (heard: DZM-0voWWtw [22:10]) |
| **modeled light** | Light shaped to sculpt a face with falloff; historically read as glamour (heard: GoLrVjL4wgo [1:00:19]) |
| **Puck (light)** | The small soft eyelight unit, the size of a hockey puck, that the Mindhunter gaffer built (heard: DZM-0voWWtw [1:17:17]) |
| **Soft sun** | A very large HMI soft source used to stand in for or boost the sun. (heard: MKZEwJD9wRo [03:33]) |
| **top light** | Key light mostly from overhead (fluorescent tubes); gives unflattering, institutional shape and keeps a moving camera free of relighting (heard: GoLrVjL4wgo [59:47]) |

### look development

| Term | Meaning |
|---|---|
| **North Star (look test)** | A reference test, such as a real film camera test graded to taste, that all later matching aims at. (heard: X4lYIBDnunE [15:09]) |
| **Print stock (as a look)** | Kelly's term for a macro-level creative transform: one fixed rendering applied to every shot, with local adjustments beneath it. (heard: lt21nZbgkbM [28:05]) |
| **Recipe (look)** | A short fixed set of capture settings plus a fixed transform, found by test shoots, so the DP shoots freely and the grade starts from it. (heard: X4lYIBDnunE [12:32]) |

### lookdev

| Term | Meaning |
|---|---|
| **deep focus** | Both near and far planes sharp through a very small aperture; used here instead of colour to separate depth in monochrome (heard: dqMpPsAGuvw [43:03]) |
| **Fantasy within the limits** | Cameron-school design rule: fantasy bounded by real conditions (weather, load, biology), used as both inspiration and technical limit. (heard: UbsXJxFZcJ0 [02:14]) |
| **Marui** | Avatar 2 name for the small huts of the Metkayina village. (heard: bup0Nbg07Xk [34:53]) |
| **ring flare (halo)** | Defined circular halo around highlights from simple 1940s lenses; modern lenses suppress it, so it is added in post (heard: dqMpPsAGuvw [34:09]) |

### motion

| Term | Meaning |
|---|---|
| **aha moment** | The payoff beat in a title or transition where a read flips and surprises the viewer (heard: D-i9yPcEW28 [33:08]) |
| **Airlock (title sequence)** | Clair's term for a title's first job: a transition between daily life and the show's world. (heard: 8MBLqyxPV0o [00:36]) |
| **Daily (Beeple sense)** | A finished piece made every day, here since 2007. (heard: DVJOZzRzlGg [20:27]) |
| **Emotion-to-time chart** | A chart of where the story's big moments, troughs and normal beats fall, used while designing boards. (heard: YHUBasYeDD8 [44:27]) |
| **logotype** | The typographic part of a logo (name as typeface or lettering), as opposed to an icon (heard: SUCIjMrn1KQ [00:00]) |
| **Machine vision (title design)** | The machine's point-of-view imagery, historically red-tinted with grids and code, here updated from depth-camera tech. (heard: _bw6CTAh4i0 [01:15]) |
| **Slit-scan** | Effect that slices an image into strips and offsets each strip in time (heard: https://www.youtube.com/watch?v=4xS4LOn3CTE [51:00]) |

### pipeline

| Term | Meaning |
|---|---|
| **Front projection** | Projecting content from the camera side onto a screen behind the set; sharper and brighter than rear projection (heard: As2k69rYoN4 [1:03:35]) |
| **head of story** | Lead of the story department who runs sketch reels and story notes before layout (heard: PVvRlrKUq7o [05:15]) |
| **motion-capture volume** | Stage where performers in suits drive a virtual set so a crew can scout and shoot it live (heard: PVvRlrKUq7o [06:16]) |
| **Process trailer** | A towed platform carrying a vehicle for driving shots; the stage-and-plates method replaces it (heard: DZM-0voWWtw [10:09]) |
| **Viewing LUT (VFX)** | A LUT made from the colour pipeline plus the look so VFX vendors judge shots as they will look in the grade. (heard: upUAulx7sGI [49:20]) |

### pre-production

| Term | Meaning |
|---|---|
| **protect (an element)** | agree that a chosen real-world element stays in the plan and keeps its budget (heard: CWKJM3oqGOk [41:14]) |

### previs

| Term | Meaning |
|---|---|
| **Lipstick camera** | A tiny video camera, used to shoot a model with real lenses for previs. (heard: y8Owkb8VreI [15:16]) |
| **Prop wash** | Air blast behind a propeller that makes standing on a wing impossible; used to test previs (heard: As2k69rYoN4 [21:57]) |

### process

| Term | Meaning |
|---|---|
| **fix it in prep** | Solve staging, coverage and look in rehearsal and prep so the shoot day only executes (heard: GoLrVjL4wgo [55:06]) |
| **Next indicated action** | Cooper's phrase for doing only the next concrete step on a problem (look at the letter spacing now) instead of trying to hold everything. (heard: d9pT_zab-MA [27:42]) |
| **run-and-gun** | Small crew, fast, self-shot filming without a big production (heard: D-i9yPcEW28 [50:40]) |
| **shot diagram** | Overhead sketch of camera positions and lenses per setup, used to match complementary reverses across days (heard: GoLrVjL4wgo [53:01]) |
| **tabletop (shoot)** | Small objects shot on a table with controlled light, common in title work (heard: D-i9yPcEW28 [50:40]) |

### production

| Term | Meaning |
|---|---|
| **Ape school** | Weeks of prep in which performers learn the creature's movement language before capture (heard: https://www.youtube.com/watch?v=elMnAhsXwuM [10:56]) |
| **Biscuit rig** | A drivable platform carrying the picture car, steered by a precision driver so the cast and camera crew ride safely. (heard: qYPhjUHTZ9M [23:56]) |
| **Found light** | Light available on location with little setup, as in a travel show. (heard: KWQCkjr6KuI [02:59]) |
| **Second unit** | A separate crew shooting action or inserts apart from the main cast scenes. (heard: qYPhjUHTZ9M [34:19]) |
| **Super take** | A combined performance-capture take with all animation that the director can film repeatedly with virtual cameras. (heard: bup0Nbg07Xk [32:45]) |
| **Virtual scout** | A walkthrough of a digital set on the capture stage with the director to block and choose angles. (heard: bup0Nbg07Xk [30:43]) |
| **Weir wall** | Wall in a water tank that forces a controlled rush of water past actors. (heard: LvDFT3kxDb4 [06:48]) |

### production design

| Term | Meaning |
|---|---|
| **Chip chart** | Paint or colour chip sheets shown behind a performer to test wall colour against skin and light. (heard: 3dZrhpQSAnY [43:13]) |

### production/post

| Term | Meaning |
|---|---|
| **special effects vs visual effects** | special effects = physical, on set, shot live; visual effects = post work on filmed plates plus CG; separate budgets (heard: CWKJM3oqGOk [34:59]) |

### redshift

| Term | Meaning |
|---|---|
| **bokeh image map** | Texture used as the aperture shape of the bokeh in Redshift's camera tag (heard: aWkfAAJgiJ0 [02:36]) |
| **bokeh normalization mode** | Camera tag option (none, unit intensity, white colour sum) that rebalances the bokeh image's brightness and tint (heard: aWkfAAJgiJ0 [03:37]) |

### review

| Term | Meaning |
|---|---|
| **Playdown** | Playing a reel start to end without pausing or comment so the room notes what to change. (heard: lt21nZbgkbM [1:09:13]) |
| **Temp love** | Client attachment to a temporary version (temp music, log rendering) that makes the finished one feel wrong. (heard: upUAulx7sGI [39:25]) |

### role

| Term | Meaning |
|---|---|
| **Finisher** | Colourist who also assembles final deliverables and adds VFX plates after the grade; role boundaries are still debated. (heard: KWQCkjr6KuI [43:57]) |

### security

| Term | Meaning |
|---|---|
| **Double black** | Sonnenfeld's term for a secret client reveal run under strict secrecy (Apple's first iPhone). (heard: EqeLzIczV3w [28:35]) |

### still/motion

| Term | Meaning |
|---|---|
| **Drag (photography)** | Blur trail from a long exposure that shows movement in time within a still frame. (heard: 3dZrhpQSAnY [12:37]) |

### story

| Term | Meaning |
|---|---|
| **Soft reboot** | A sequel set far after earlier films, with new characters, that still honours the old story (heard: https://www.youtube.com/watch?v=elMnAhsXwuM [02:08]) |

### style

| Term | Meaning |
|---|---|
| **Lead drawing** | The one drawing or style frame finished and coloured first so palette and rules can be set. (heard: wywwAFOKXug [1:01:23]) |

### title history

| Term | Meaning |
|---|---|
| **Bipack** | Old optical technique of running two film strips together to burn type onto negative; Fong shot titles this way on an animation stand early in her career. (heard: wywwAFOKXug [1:22:07]) |

### titles

| Term | Meaning |
|---|---|
| **Main on end** | Main title placed at the end of a film instead of the start. (heard: NqO-PCErlas [31:40]) |
| **Skip intro button** | The streaming control that lets viewers skip a main title. (heard: H_bwUkS4scM [13:28]) |

### titles and credits

| Term | Meaning |
|---|---|
| **Above the title** | Billing position for the top names, shown before the film title appears. (heard: NqO-PCErlas [37:54]) |
| **Style sheet (crawl)** | Fixed rules for type size, speed and spacing of an end-credit crawl. (heard: NqO-PCErlas [36:20]) |

### titles and music

| Term | Meaning |
|---|---|
| **Clip track** | Temporary or mood music used to cut a title sequence before the final score exists. (heard: NqO-PCErlas [44:10]) |

### type

| Term | Meaning |
|---|---|
| **Master (type)** | A fully drawn extreme weight from which in-between weights are interpolated (heard: https://www.youtube.com/watch?v=jWCUeBYapkI [51:08]) |
| **Tracking (type)** | Even letterspacing across a run of text, as opposed to kerning a single pair (heard: https://www.youtube.com/watch?v=jWCUeBYapkI [40:17]) |
| **Wobbly face** | Typeface with irregular outlines drawn to look pre-worn for letterpress (heard: https://www.youtube.com/watch?v=jWCUeBYapkI [07:51]) |

### VFX

| Term | Meaning |
|---|---|
| **Hanging miniature** | A model hung close to camera so it reads as a distant large object. (heard: y8Owkb8VreI [29:15]) |
| **Witness camera** | A second camera beside the main one that records depth and parallax data. (heard: gNh9r-VbSVg [1:15:53]) |

### VFX elements

| Term | Meaning |
|---|---|
| **Dirt charge** | An air-compression charge that throws up dirt safely indoors for filming. (heard: gNh9r-VbSVg [02:16]) |

## Added from round S (2026-10-31, unsorted)
client direct | agencies | selling to the brand itself instead of through an ad agency | lhZLvNQgB7w [28:37]
media buy | agencies | agency purchase of ad time or space, the old main earner for agencies | lhZLvNQgB7w [20:32]
financial runway | agencies | how many months a studio or freelancer can survive without income | lhZLvNQgB7w [37:41]
toolbox (of elements) | broadcast | a library of reusable graphic pieces built by vendors for a package | tWVq7hQCwzo [01:38]
phantom / storm / venom | broadcast | ESPN's MNF names for the black-on-black, white-on-white and third main colour looks | tWVq7hQCwzo [03:12]
battle mesh | broadcast | ESPN's name for a tough fabric-like texture used for MNF logo alternates | tWVq7hQCwzo [06:27]
surface brightness | lighting | Octane light option that ties power to light area | J5KwV7GfbEQ [09:23]
delta EV | lighting | light-meter function that shows the stop difference between a stored and a new reading | ksIsFd2F4Uk [08:36]
camera-referred / scene-referred / display-referred grading | comp | which colour space the grade is applied in: the camera's, a wide scene space, or the display's | w0ubDSzEEYg [10:57]
position camera pass | comp | a render pass with each pixel's position in camera space, usable as depth in scene units | tB5-Oe7pTUs [11:15]
tent poles (story) | lighting | the few emotional beats expected to survive story changes, lit first | CIFN7k8H3Gw [04:47]
barbules | lookdev | tiny hairs on feather barbs that make feathers soft; absent in Houdini's feather procedural | 4D9GDZsCzy0 [23:08]
condensed feathers | lookdev | Houdini feather mode storing barbs as vectors on the shaft, generated at render time | 4D9GDZsCzy0 [22:07]
execution graph | pipeline | Prism's node-based tool for automating pipeline steps (project creation, archiving, publishing), nodes are JSON and TD-extendable | jfH7JpjDO_w [04:42]
slap comp | comp | rough fast comp used to judge a render before final comp (here in Houdini Copernicus) | jfH7JpjDO_w [45:01]
Look deck | look development | A PDF for the client with hero frame, reference stills, palette and the graded scene, used to approve a look remotely. | JWa0YpS98-w [32:38]
Omer (look suffix) | look development | Code word added to a look's name meaning "first look, not yet approved"; removed on sign-off. | JWa0YpS98-w [25:04]
Printer lights | grade | Trim controls from film printing; in the tool 8 points equal one stop, 4 a half stop. | JWa0YpS98-w [26:46]
Scene-referred cube | grade | A LUT that keeps camera log in and out so the display transform is applied later by colour management. | JWa0YpS98-w [43:05]
Money shot (VFX/animation) | production | A shot flagged early as technically, creatively or computationally expensive, such as hair, crowds or light through water. | JR6cmASjuuI [12:06]
Exposure zones (Ansel Adams) | look development | Five bands of exposure around a skin-tone middle zone used to compute a look's palette. | JWa0YpS98-w [36:14]
Test-driven pipeline | pipeline | Testing each small part of a production problem alone before using it on set. | 8tW77BsgtPY [05:00]
Cel (hand-drawn accent) | motion | Hand-drawn frame-by-frame line layer drawn over a render for stylised effect. | ENbEafUSac0 [04:15]
chain of title | delivery | auditable record of every input, model and setting behind a generated image | bWvxBu_vVes [1:37:00]
FID | ai | Frechet inception distance; 100+ between image sets means distinct populations | bWvxBu_vVes [1:32:14]
conditioning | ai | feeding a model human-made inputs (depth, LoRA, mask) besides a text prompt | bWvxBu_vVes [1:29:36]
probabilistic renderer | ai | Stellar's term for AI video driven by proxy animation | bWvxBu_vVes [1:44:52]
kodalith | motion | very high-contrast film used to shoot light through title letters for optical flaws | _a1lp_ygGB4 [02:07]
PQ (ST 2084) | broadcast | absolute-brightness signal encoding; Unreal maps 1.0 to 100 nits | bh5wD1YapJo [05:15]
ICVFX | broadcast | in-camera visual effects on an LED volume | bh5wD1YapJo [00:02]
interstitial | broadcast | a transition graphic between two TV segments, such as news handing to sports | WLdmYnkFoK4 [38:32]
bumper | broadcast | a short loop at the top or end of a segment with a logo or sponsor | WLdmYnkFoK4 [38:32]
stitch | comp | a visual effect that joins two takes so they read as one continuous shot | Pok6EN3cfA4 [12:32]
paintout | comp | removing an object from a frame | Pok6EN3cfA4 [06:34]
garbage matte | comp | a rough first-pass mask, now often made by AI roto, refined later | d5uP3wjc3Tc [08:52]
clean plate | comp | footage of the same angle and camera move without actors or moving props, used to paint out or reveal | d5uP3wjc3Tc [02:11]
take next | broadcast | send the queued item in the rundown to air (versus preview, which plays only in the editor) | lZpiYHbHgR8 [03:44]
rundown | broadcast | an ordered list of graphics a playout operator takes to air one by one | lZpiYHbHgR8 [00:01]
bundle (unapproved/approved) | pipeline | a packaged work-in-progress shot version sent for review; approval lets the next department pull it | cID-j-f3Mj8 [1:00:50]
BG prep | pipeline | background prep, entry-level roto and paint cleanup department | cID-j-f3Mj8 [21:20]
planckian locus | comp | the curve of colours an incandescent black body takes as temperature changes; white points lie near it | Hlj5ep-85ys [26:40]
line of purples | comp | the straight edge of the CIE diagram: colours that exist but have no single wavelength | Hlj5ep-85ys [17:10]
cyc (cyclorama) wall | lighting | backdrop wall with a rounded corner so floor and wall blend with no seam | k5ArlhNwGFU [5:12]
bumper | broadcast | Short (about 5 s) transition from a program to a break and back, reminding viewers what they watch | VkkG-_oUGwg [03:10]
play off / play on | broadcast | Bumper variants placed before the break (play off) and before the return (play on) | VkkG-_oUGwg [03:10]
bug | broadcast | Channel logo kept in a screen corner, static or animated | VkkG-_oUGwg [03:41]
snipe | broadcast | Lower-screen box announcing what airs next or schedule information | VkkG-_oUGwg [03:41]
swipe | broadcast | Transition between two segments of a program, e.g. into a replay | VkkG-_oUGwg [04:12]
cluster buster | broadcast | Group of transitions and boxes bridging segments, loosely defined by the speaker | VkkG-_oUGwg [04:12]
mortise | broadcast | Composition showing a small picture inside the screen with its information | VkkG-_oUGwg [04:47]
packshot | broadcast | Closing card with the next showing's time and date | VkkG-_oUGwg [05:17]
billboard | broadcast | Sponsor card ("brought to you by") after a promo or program | VkkG-_oUGwg [05:17]
classification | broadcast | Animation showing a program's age rating | VkkG-_oUGwg [05:48]
manifest (USD) | pipeline | Master USD per entity that gathers every department's published USD | Dd1eYWpgpkw [04:09]
asset instance | pipeline | Hari's entity for an asset prepared for use in shots, starting from the asset's manifest | Dd1eYWpgpkw [04:40]
shot group | pipeline | Entity for multi-shot lighting and layout across a sequence | Dd1eYWpgpkw [05:13]
fake hierarchy | pipeline | Prim paths recreated without types, kinds or properties so thousands of prims load free for light linking | Dd1eYWpgpkw [21:40]
point deform | houdini | Moves a high-res or original-UV mesh with deformed points, preferred over remeshing for sim-to-geo | JCUks81cBtw [35:20]
lock list | ai-models | The list of things in a clip an AI edit prompt must leave unchanged | Yte-UGhYkPQ [02:49]
copy pre-mult setup | comp | Unpremult, correct, copy alpha back, premult chain used around CG corrections in Nuke | fxfuhl8Q7ys [06:46]
handles | pipeline | extra frames at head and tail of a VFX shot (8, 10, 16 or 24) beyond the edit | 5_FxVWwShws [51:37]
VFX editor | pipeline | person in the cutting room who syncs editorial and the VFX house, tracks versions and timecodes | 5_FxVWwShws [50:06]
temp comp / postvis | pipeline | rough early composite or animation put in the edit before final shots | 5_FxVWwShws [54:18]
DMP | comp | digital matte painting, often projected on simple 3D | 5_FxVWwShws [05:42]
LOD (asset budget) | pipeline | level of detail needed for how large an asset appears on screen, drives cost | 5_FxVWwShws [39:12]
data wrangler | pipeline | on-set person capturing balls, charts, clean plates, HDRs for VFX | 5_FxVWwShws [49:01]
back to beauty | comp | rebuild the beauty from split passes so each can be graded | evwUXSqbysQ [02:28]
is shadow ray (light path) | lookdev | Cycles output that lets a shader go transparent only for shadow rays, letting light through glass | dLZEmfqob7k [03:49]
light portal | lighting | rectangular area light on an opening that focuses sampling through it | dLZEmfqob7k [02:16]
Stage object | c4d | C4D object that keys which camera is active, for cuts in one render | wAVOwrxLHcA [46:53]
tone curve (Unreal MRQ) | comp | baked display curve in Movie Render Queue output; off gives linear sRGB | 2Q3CybANHKE [03:56]
CC Force Motion Blur | comp | AE effect on an adjustment layer to fake blur where Advanced 3D has none | ks9TXSxSUGs [04:50]

## Added from round U (2026-10-31, unsorted)
Eye ding | lighting | small highlight reflection in a character's eye, often kept at a set clock position on the key side | cP3AELeZf6o [09:22]
Hall of fame (critique) | education | the Academy's gallery of finished student pieces approved by their artist | cP3AELeZf6o [23:39]
Focus triangle | lighting | the area of face and neck where the critic wants the light kept, with the chest and edges darker | cP3AELeZf6o [42:41]
Reveal (roto paint) | comp | painting away a top layer through a Roto Paint node to show a second input underneath | sTCeHUto1IM [17:55]
Protected region | motion | After Effects work-area section marked so it keeps its timing when the layer is stretched | bnFRXVbi0ZA [36:00]
Time remapping (as "which frame am I on") | motion | keyframing the source frame number so beats can stretch or compress | bnFRXVbi0ZA [31:10]
Render and Replace / Restore Unrendered | pipeline | Premiere commands that render a linked comp and later restore the editable one | bnFRXVbi0ZA [25:00]
Real ID | pipeline | Scratch metadata column that keeps the original source clip name | pWT2nk1vCt8 [01:39]
Locator (Avid) | pipeline | marker on a clip in an Avid EDL, here holding the VFX shot name | pWT2nk1vCt8 [01:05]
Look file / show LUT trigger | broadcast | per-performance colour profile loaded onto live cameras | e7rE79Dp4rg [07:30]
Vision engineer / shader | broadcast | person who matches and exposes live cameras from the truck | e7rE79Dp4rg [10:36]
Follow me (lighting) | broadcast | desk function that points a light at a tracked performer position | e7rE79Dp4rg [20:31]
PSN data | broadcast | PosiStageNet protocol sending positions of moving objects such as winches to the desk (term heard as "PSN"; spelling unverified) | e7rE79Dp4rg [22:04]
Infinity screen | broadcast | curved LED piece blending an upstage wall into the LED floor | e7rE79Dp4rg [23:07]
Peekaboo lift | broadcast | LED floor section on a stage lift that rises about 8 m, tracked so masks follow it | e7rE79Dp4rg [23:39]
Rotation (wireless audio) | broadcast | pool of wireless devices cycled between acts, six on stage at a time | e7rE79Dp4rg [31:30]
IBC | broadcast | international broadcast centre where the world feed is assembled | oM5SF5PyCVE [09:18]
Motion language | motion | framework of decisions on how and why things move, matched to the design | Jno5NiYoolM [03:40]
Ownability | motion | a motion style specific enough to be the brand's own | Jno5NiYoolM [11:44]
Functional animation | motion | plain A-to-B movement with no brand-specific style | Jno5NiYoolM [11:11]
Motion test / motion diagram | motion | stripped-down animation of a feeling, made before design to guide the team | Jno5NiYoolM [20:35]
Sanity check (pipeline) | pipeline | automatic test run on a task's output before handing it on | 4R8PduY_vV4 [20:49]
Virtual slate | pipeline | clip name and timecode burnt into a proxy | gqpVdX8k2xU [04:31]
ray epsilon | render (Octane) | Octane slider that offsets ray start points; lowering it clears artifacts where surfaces nearly touch | 8zCqKpeF5Uc [05:19]
hot pixel removal | render (Octane) | camera imager setting that suppresses single bright pixels (fireflies) after the render | 8zCqKpeF5Uc [03:43]
GI clamp | render (Octane) | cap on how bright indirect light samples can get; default is huge, lowering it reduces fireflies and speeds up | 8zCqKpeF5Uc [03:10]
light pass ID | lighting (Octane) | number on a light that lets objects opt in or out of its light via their object tag | 8zCqKpeF5Uc [00:34]
falloff map (distribution) | lighting (Octane) | light distribution whose angle sets how soft the beam edge is; 90 degrees used for softbox feel | mNcq8GD1mfI [05:19]
feature-based lighting | lighting | lighting each part of a product with its own light, starting from black | pdOppPMGuIU [02:08]
boundary fill | modelling (Fusion) | command that makes a closed body from the space between surfaces, such as liquid in a cup | 9yZCElLDRH4 [01:13]
coincident faces | modelling | two surfaces in exactly the same place; ray tracers cannot decide which material applies | 9yZCElLDRH4 [00:42]
Render Perfect | modelling (C4D) | primitive object option that keeps the shape mathematically round and ignores displacement | p-XJG8bLKBM [06:46]
Chaos Cosmos | lookdev (V-Ray) | Chaos browser of ready-made materials and assets | i6zQmQD_auA [07:23]
Blend node | lookdev (V-Ray) | node that combines a base material and a coat material under a texture mask | i6zQmQD_auA [10:37]
Local Slave Controls | pipeline (Deadline) | Deadline Monitor panel for the machine you are sitting at | QY5odtFbs5M [01:37]
Stop Slave After Current Task Completion | pipeline (Deadline) | command that lets the current frame finish and then takes the machine off the farm | QY5odtFbs5M [02:08]
PCG | pipeline (Unreal) | procedural content generation framework: rules that build meshes such as a stadium and crowd | crMTfD5XVkA [01:03]
pixel coded texture | motion (Unreal) | texture chosen by a code typed into remote control, used to swap team colours | Ty6etYkvaC8 [06:47]
CBB (could be better) | education | shorthand for optional small improvements on work that is already good, offered if there is time | RCCaQmwxNB4 [02:55]
FML frames | pipeline | first, middle and last frames rendered as a quick check before a full range | RCCaQmwxNB4 [20:33]
Helper light | lighting | a cheated extra light added for one moment of a shot | ETgt9YXSaeg [13:14]
Eye shine | lookdev | the reflective glow of an eye in dark light, matched as reflection not emission | TdTxV_ACVhU [04:18]
Dappled light | lighting | patchy light broken by leaves, made with a gobo; used to calm bright items | ETgt9YXSaeg [22:23]
Soft split | comp | a visible soft seam where two images were blended instead of one continuous surface | u7p4RnOuaNQ [19:13]
Tooth (of ground) | comp | fine surface texture that makes a ground plane read as real under shadows | u7p4RnOuaNQ [18:42]
Kicker | lighting | a rim or wrap light on the face that helps its sculpting | ETgt9YXSaeg [05:43]
Grey shader scene | pipeline | the scene rendered with one plain default shader on everything, to audit light only | 55eY1-LlY3k [43:42]
Store Color To AOV | redshift | node that writes a colour or texture into a named custom AOV; sits between shader and output | ARykOD6lG3c [19:19]
custom AOV | redshift, comp | a user-named pass fed from any texture or node, not a shader; takes colour, integer or float | ARykOD6lG3c [16:10]
Object ID pass (integer) | redshift, comp | per-object whole-number channel read in comp to pick one object; no anti-aliasing | ARykOD6lG3c [27:38]
clown pass | comp | colour-per-object ID render; here replaced by an integer ID channel | ARykOD6lG3c [27:38]
Lenscare | comp | post depth-of-field plugin used with a depth AOV (heard as "lens care") | ARykOD6lG3c [38:15]
Uber shader | redshift | the old name for the main Redshift Material in 2017 | LcxjkHFS-2k [13:59]
sample filtering (clamp) | redshift | old-UI output clamp that caps sample brightness against fireflies | LcxjkHFS-2k [59:07]
dome Back Plate | redshift | dome light slot for a visible background image that does not light the scene | RpiCCLHjlWQ [28:17]
Normalize Intensity | redshift | area light option that removes the light-size effect on brightness | RpiCCLHjlWQ [41:53]
Height Scale | redshift | strength of a Bump node's height; 1 is strong, about 0.2 subtle | RpiCCLHjlWQ [38:51]
Redshift proxy | stage: layout, render | baked mesh file Redshift loads at render time; bounding box in viewport, like Arnold .ass | MuVzbVhMUvI [00:32]
Add Proxy to Scene | stage: layout | export option that replaces the selected mesh with its proxy in one step | MuVzbVhMUvI [03:10]
Sample mode | stage: tuning | Redshift view showing where samples are spent per pixel (max bright, min dark) | MuVzbVhMUvI [20:52]
Shader Switch | stage: lookdev | Redshift node that picks an input by integer selector, used with object ID | MuVzbVhMUvI [53:11]
Smart bake | stage: lookdev | Redshift lowers a texture-displacement bake to the source texture's resolution | Xh8A767yA1U [45:02]
Delete Without Children | stage: modeling | C4D command that removes an object and keeps its children | TonSU8Ljm5c [08:35]
Cannonball distribution | stage: layout | advanced MoGraph distribution that piles clones as pyramids, scale-aware | Xh8A767yA1U [08:11]
EZ Matte | comp | Cheap Tricks name for a footage-plus-depth pre-comp with exposed Brightness and Contrast sliders used as a depth-sliced matte | -32g9bYyZuc [06:21]
Contact glow | comp | a squashed, blurred, additive duplicate of a fire layer at low opacity that fakes ground light | -32g9bYyZuc [40:41]
Blur Behind | comp | Supercomp option that blurs the layers below a layer by a chosen amount | -32g9bYyZuc [22:16]
Match Background (Supercomp) | comp | colour correction option that tints a layer toward a reference layer under the stack | -32g9bYyZuc [33:46]
Z buffer layer (Particular) | comp | Visibility setting that hides particles behind a depth pass, with Z at black and Z at white limits | -32g9bYyZuc [44:33]
Breaker (collider) | c4d | Boyts' name for an oversized hidden collision shape on a character that clears dynamics shards | 27b5cFk-Pjk [20:35]
Cloth NURBS | c4d | object that gives thickness to flat mesh pieces, used to thicken glass shards | 27b5cFk-Pjk [20:01]
PSR Reset | c4d | R21 command that zeroes position, scale and rotation | 0Zg4lpwZGe0 [08:22]
Scroll to First Active | c4d | Object Manager command that jumps to the selected object in a long hierarchy | 0Zg4lpwZGe0 [34:31]
2.5D logo | broadcast | a flat logo with a plain extrude and no contour or volume work | 0Zg4lpwZGe0 [13:37]
Create Outline | c4d | spline command that offsets a spline in or out, used for trims and faceplates | 0Zg4lpwZGe0 [16:13]
Puzzle Matte (Redshift AOV) | redshift | AOV that outputs a mask by material or object ID; Say sets Material ID 1 on an emissive material | 0Zg4lpwZGe0 [42:26]
Barn door (CG lighting) | lighting | narrow strip of light made with a slim area light and minimal spread | oANXbk9OUbI [07:22]
Digi-double | pipeline | digital double of an actor, matched to filmed plates | yDcjIk7L-0Y [39:33]
Render wrangler | pipeline | person who watches the farm and fixes broken jobs | yDcjIk7L-0Y [46:47]
disposable file system | gpu-cloud | a render file system launched from a template per project and deleted after outputs sync back to object storage | cm4sPe1nLjU [10:00]
AppStream (SDX protocol) | gpu-cloud | AWS service that streams a GPU Windows desktop or app as H.264 over UDP | cm4sPe1nLjU [22:29]
Direct Connect | gpu-cloud | dedicated network link from an office to AWS | cm4sPe1nLjU [06:21]
ORBX | gpu-cloud | OTOY's packaged scene file holding animation, plugins and textures for Octane | MghPaVl9aM0 [02:06]
render credits | gpu-cloud | prepaid balance for Render Network jobs, bought with card or PayPal, unlike crypto tokens | MghPaVl9aM0 [18:54]
economy tier | gpu-cloud | cheaper, slower farm priority that shares resources with other users | MghPaVl9aM0 [18:22]
OctaneBench | gpu-cloud | OTOY's benchmark score used as the billing and estimating unit for Octane cloud work | yc6Mfxt9bCc [10:30]
capsule | motion | Maxon Studio's comp-aware template that adapts to frame rate and size | -7-foJ3thiU [01:34]
data burn-in | pipeline | text such as timecode and clip name printed onto dailies | rgZjL2e8yEg [10:22]
inverse-normals sphere | lighting | Unreal's built-in sphere with flipped normals used as an HDRI dome | dT4Vl3PGe08 [03:05]
source soft angle | lighting | Unreal sun setting the speaker ties to reflection softness, next to source angle for diffuse softness | dT4Vl3PGe08 [08:18]
tracer fire | lighting | fake bullet streak made of a tube-length light plus an emissive cylinder | dT4Vl3PGe08 [14:30]
Start New Layer / Configure Layer | pipeline | same Solaris node; begins a new USD layer with its own save path | XUsleR7wJhk [05:20]
strip layer above layer breaks | pipeline | USD ROP option that drops everything before a layer break from the export | XUsleR7wJhk [13:33]
output processors | pipeline | ordered list of USD ROP steps such as copy assets and relative paths | XUsleR7wJhk [17:09]
context engineering | ai-models | managing what goes into an AI agent's context window | 8kL1Ae9AWWs [04:39]
plan mode | ai-models | Claude Code mode (Shift+Tab) that writes a plan to review before editing | 8kL1Ae9AWWs [06:12]
incident reading | lighting | light-meter reading taken at the subject pointing at the light | 7UG1aBlH1lo [03:08]
flash lock | lighting | switching a TTL flash to manual so its power stays fixed after a good exposure | yALctlSEakE [02:46]
Fuzz (OpenPBR) | lookdev | Topmost layer in OpenPBR for microfibre reflection (hair, dust, textile); replaces Sheen | ieWk4U63EBw [12:28]
Coat darkening | lookdev | OpenPBR control for how much a coat darkens layers beneath; 1 is physical | ieWk4U63EBw [11:17]
Tiled camera | pipeline | Old C4D Expresso setup rendering one still as N x N tile frames to be reassembled | 09hP2XAi0Rk [14:04]
Slash angle | broadcast | Low camera angled across the field from near the network stage, not straight on | 07waFGp9_M0 [07:09]
Field breakout box | broadcast | Sideline box that gathers camera, audio, IFB, talkback and data and sends them to the truck on one run | 07waFGp9_M0 [09:26]
Camera pylon | broadcast | Small cube camera inside an end-zone pylon for red-zone and goal-line angles | 07waFGp9_M0 [17:10]
IFB | broadcast | Interruptible foldback; the earpiece feed producers use to talk to on-air talent | 07waFGp9_M0 [09:26]
Dispersion weight | lookdev | OpenPBR scalar that blends dispersion in or out, separate from the Abbe value | ieWk4U63EBw [06:56]
core hour | gpu-cloud | cores used by a frame multiplied by hours it runs; unit for farm cost and capacity | FStbueCu1f8 [05:13]
render on tens | pipeline | test render of only every 10th frame to check a shot cheaply | FStbueCu1f8 [10:20]
fourth-quarter studio | agencies | a studio that shows its work to the client only late, which clients dislike | FStbueCu1f8 [15:33]
RFDK | gpu-cloud | AWS Render Farm Deployment Kit, open-source CDK constructs that deploy Deadline | kACWEs-XJcI [08:56]
TCC mode | gpu-cloud | NVIDIA driver mode that dedicates a card to compute and bypasses WDDM | kACWEs-XJcI [12:03]
usage-based licensing | gpu-cloud | licence billed by the minute only while a frame renders | kACWEs-XJcI [16:23]
GPU affinity (Deadline) | gpu-cloud | giving each concurrent frame on a node a subset of its GPUs | kACWEs-XJcI [21:16]
peer-to-peer asset distribution | pipeline | Team Render nodes share assets with each other instead of only pulling from a server | 1Gtp3BjlTjY [09:56]
step value | gpu-cloud | frame step so only every Nth frame renders, used to price a test | 6y4PSQOsJck [08:50]
Auto Submit (Render Beamer) | gpu-cloud | option that starts the farm job automatically on upload | 6y4PSQOsJck [03:11]
Economy / Priority tier | gpu-cloud | Render Network cost-vs-speed choices | hi_DDuUcGeA [03:19]
extra roughness (transmission) | lookdev | Redshift Standard control that blurs refraction inside without changing surface reflection | DmeiTnrqp3I [03:46]
transmission depth / scatter colour | lookdev | Redshift Standard controls for how deep light reaches and the colour it picks up inside | DmeiTnrqp3I [05:20]
shutter position (Redshift) | redshift | whether blur is centred on, ends at or starts at the frame time | tsx8Isq6m-s [01:41]
global caustics | redshift | scene switch that must be on for light caustic overrides to take effect (speaker) | FYq8sdCtsoY [01:36]
selection object | c4d | object that stores a selection and re-selects it when double-clicked | HlQhMbjrM6M [01:35]
timeline bookmark | c4d | saved set of isolated animation tracks | HlQhMbjrM6M [02:39]
spp | lookdev | samples per pixel | 3ornW8uKJpI [12:40]
Egress fee | gpu-cloud | charge for moving data out of a cloud provider | tzHZJU1rG3Y [29:24]
Boutique cloud | gpu-cloud | small provider that owns its hardware and supports clients personally, versus a hyperscaler | tzHZJU1rG3Y [11:23]
Minimum commit | gpu-cloud | floor of machines or spend a customer agrees to keep paying for | tzHZJU1rG3Y [32:30]
Loaded rate | agencies | day or hour rate bundling artist, machine and overhead into one price | -Ks7SSgeHGg [10:01]
Cost-plus (render) | agencies | passing on actual render cost with an agreed margin or allocation | -Ks7SSgeHGg [10:32]
Fleet (Deadline Cloud) | gpu-cloud | a group of cloud workers of one type that a queue can use | -Ks7SSgeHGg [09:00]
C node | pipeline | Vast compute node that runs the storage logic in front of shared flash | lCr3vIKUpwo [05:46]
DASE | pipeline | Vast's disaggregated shared-everything design: compute separate from flash, all nodes see all drives | lCr3vIKUpwo [04:45]
Similarity reduction | pipeline | Vast's data reduction that stores only the differences between near-identical blocks | lCr3vIKUpwo [08:53]
Forklift upgrade | pipeline | replacing a whole storage system instead of growing it | lCr3vIKUpwo [25:57]
Performance isolation | pipeline | giving groups of users separate slices of throughput on shared storage | lCr3vIKUpwo [30:08]

## Added from round X (2026-10-31, unsorted)
preemptible VM (pVM) | render | cloud machine sold cheap because the provider can take it back (Google: within 24 hours, about 70% cheaper in 2016) | https://www.youtube.com/watch?v=aAjOM-JqnHI [36:18]
spot instance | render | AWS spare-capacity machine, same hardware as on-demand, can be reclaimed with a two-minute warning | https://www.youtube.com/watch?v=Fl_FdVgp2E0 [10:21]
checkpoint (render) | render | periodic partial-result write so a task can resume on another machine after a preemption | https://www.youtube.com/watch?v=0gXT3sntiFg [21:19]
Cuebot | pipeline | OpenCue's central server that schedules jobs and hands work to render nodes | https://www.youtube.com/watch?v=0gXT3sntiFg [20:01]
RQD | pipeline | OpenCue's daemon on each render node; it registers the host with the Cuebot and runs tasks | https://www.youtube.com/watch?v=0gXT3sntiFg [20:01]
proc | pipeline | OpenCue work slot carved from a host (cores and RAM), not a processor | https://www.youtube.com/watch?v=0gXT3sntiFg [35:47]
allocation / subscription | pipeline | OpenCue buckets of hosts, and a show's claim on one or more buckets, used for fair share | https://www.youtube.com/watch?v=0gXT3sntiFg [36:56]
bin packing | render | fitting jobs into host slots so cores and RAM are used with the least waste | https://www.youtube.com/watch?v=0gXT3sntiFg [36:22]
wrangler (render wrangler) | render | person who watches the farm and fixes failed or slow jobs | https://www.youtube.com/watch?v=0gXT3sntiFg [41:48]
upload-only job | render | submit mode that syncs scene assets to cloud storage without rendering | https://www.youtube.com/watch?v=aAjOM-JqnHI [20:13]
repathing | pipeline | rewriting file paths between local and cloud locations so logs and scenes stay readable | https://www.youtube.com/watch?v=aAjOM-JqnHI [28:02]
frames per task | render | how many frames one cloud machine takes before returning; 1 limits loss on preemption | https://www.youtube.com/watch?v=aAjOM-JqnHI [23:19]
zero client | pipeline | small box at a monitor that only streams a remote desktop (Teradici style) | https://www.youtube.com/watch?v=Fl_FdVgp2E0 [48:40]
FSx for Lustre | render | AWS managed fast file system started per job for large parallel render fleets | https://www.youtube.com/watch?v=Fl_FdVgp2E0 [19:46]
hydrate (volume) | render | fill a cloud disk with the files a job needs before the nodes read it | https://www.youtube.com/watch?v=Fl_FdVgp2E0 [17:09]
live migration | render | Google Cloud feature that moves a running VM to another host without interrupting it | https://www.youtube.com/watch?v=aAjOM-JqnHI [36:18]
allocation vs utilization | render | machines assigned versus machines doing useful work | https://www.youtube.com/watch?v=hIxnygxsdmc [28:46]
studio in the cloud | pipeline | workstations, storage and rendering all hosted by one cloud vendor so no data moves between them | https://www.youtube.com/watch?v=hIxnygxsdmc [57:28]
queue budget | cloud | spend cap attached to a Deadline Cloud queue; can block the queue until set | PjafAJ0-6SA [13:56]
soft stop / hard stop (budget) | cloud | stop after current jobs finish vs stop immediately when the budget runs low | PjafAJ0-6SA [16:04]
customer-managed fleet | cloud | fleet whose instances and scaling groups you see in your own AWS account | PjafAJ0-6SA [07:04]
service-managed fleet | cloud | fleet AWS runs for you; instances are hidden and billed through the service | PjafAJ0-6SA [07:36]
preemptible VM | cloud | Google's spare-capacity VM, 24 hour cap, can be revoked | heDHOWmVMbU [26:28]
sustained use discount | cloud | automatic Google discount, up to 30 percent, for running a machine most of the month | heDHOWmVMbU [21:48]
pyoutline | farm | OpenCue Python library for building job files in code | fnbRcTeKirw [12:29]
outline file | farm | OpenCue job description (XML or YAML) listing layers, tasks and dependencies | fnbRcTeKirw [11:58]
layer (OpenCue) | farm | one stage of a job; layers can depend on each other | fnbRcTeKirw [13:35]
erasure coding | storage | protecting data across nodes at file level instead of RAID on disks | XSqzTroN_ec [02:42]
IFD | render | Mantra scene description file Houdini writes before rendering; big and meant to be deleted | XSqzTroN_ec [10:23]
cache hit rate | storage | share of reads served from flash instead of hard drives | XSqzTroN_ec [14:01]
Concierge (CoreWeave 2019) | cloud | web file manager tier of the Blender farm for bigger scenes | sh8UhQ1zofg [08:29]
pinned offline (LucidLink) | storage | marking files to keep a local copy for when the internet drops | em51SPDTJIE [04:11]
VDI | gpu-cloud | Virtual desktop infrastructure: a remote GPU workstation streamed to the artist. | me25mlhgERI [06:25]
PCI passthrough | gpu-cloud | Giving a whole physical GPU to a virtual machine, so no vGPU slicing. | me25mlhgERI [22:33]
Huge pages | gpu-cloud | Large memory blocks (1 GB here) reserved on a VM host for speed; hard to switch on and off at runtime. | me25mlhgERI [22:02]
Nearline storage | gpu-cloud | Cheap archive storage that returns a file in seconds, fast enough for restores but not for rendering. | _5tXiMbpKw0 [16:14]
Slow bake | gpu-cloud | A low-priority render job left on the farm while the artist is unsure of the look. | _5tXiMbpKw0 [11:01]
Burst rendering | gpu-cloud | Renting cloud nodes only for peak load while keeping a base farm on site. | F1KVCGox1TA [08:55]
Network volume (RunPod) | gpu-cloud | Persistent storage that survives when a rented GPU pod is deleted; can grow, not shrink. | FJrxD-BG0pg [02:36]
Farm, queue, fleet (Deadline Cloud) | gpu-cloud | Farm holds queues (where jobs go) and fleets (the worker machines). | kyaphnaCDEU [04:15-06:21]
Service-managed vs customer-managed fleet | gpu-cloud | AWS runs the worker images vs you build your own images and mount your own shares. | kyaphnaCDEU [00:03-01:04]
Client watch (Royal Render) | pipeline | Tray application that controls the background Royal Render client service. | HKLXU4do4Jc [06:55]
RLM | pipeline | Reprise License Manager: server software that hosts floating licences. | KUkjI7xprPM [00:04]
Teleportation (broadcast) | broadcast | keying a remote person on a small green backdrop into the studio, often behind a real desk | cE3jw6MO9kw [25:44]
Hybrid set | broadcast | studio mixing a real set, an LED wall, a virtual extension and a green zone | cE3jw6MO9kw [08:45]
Virtual extension | broadcast | graphic scenery added past the edge of a real set | cE3jw6MO9kw [17:32]
Take ID | broadcast | a numbered copy of a scene in XPression's sequencer, with its own data and settings | VZO7A0F7pZ0 [06:47]
Publish object | broadcast | XPression setting that lets the sequencer override an object's attributes per take | VZO7A0F7pZ0 [18:07]
Auto squeeze | broadcast | XPression text setting that condenses text to stay inside a set width | VZO7A0F7pZ0 [30:35]
Animation controller | broadcast | XPression keyframe-only clip inside a scene director | 71govSIChlQ [01:06]
Billboard (virtual set) | broadcast | flat keyed video of a person placed in a 3D set when there is no camera tracking | IWoq_ezCoTY [08:48]
Compound (Aximmetry) | broadcast | grouped node graph saved as a reusable module, optionally linked to its file | aiG_r6-uU54 [13:05]
Daisy-chaining controls | broadcast | passing Essential Graphics controls from a nested precomp up to its parent | E8gA_Is_gOM [02:46]
Cameo (Chyron CAMIO) | broadcast | Chyron asset-management server that holds templates and media and syncs them to devices | paB-GB70P2k [02:43]
Hub Drive | broadcast | Chyron sync service that copies uploaded content folders to all devices in a plant | paB-GB70P2k [03:14]
Lucy (Chyron) | broadcast | Plug-in inside a newsroom system where producers fill and preview Chyron templates | paB-GB70P2k [03:46]
ISQ | broadcast | Chyron control-room software that turns a newsroom rundown into per-channel playlists | paB-GB70P2k [09:30]
Workflow action | broadcast | Chyron ClickEffects rule that puts a scene on or off air or plays a named Prime keyframe action from a remote button | aphNW1vroXA [02:07]
Cook content (Aximmetry/Unreal) | broadcast | Unreal packaging step needed before Aximmetry can run an Unreal set | rhcwOVyKDlI [04:19]
Billboard (Aximmetry) | broadcast | Source layer that places a live-keyed talent feed inside the virtual set | rhcwOVyKDlI [08:43]
Tunnel (Aximmetry) | broadcast | Named invisible connection that passes a signal such as a mirror image between sub-compounds | leqVJhmy_zQ [02:06]
Clip plane (Aximmetry) | broadcast | Module that defines the plane about which a mirror camera reflects | leqVJhmy_zQ [00:02]
Mirror vs rough shader (Aximmetry) | broadcast | Mirror = planar real-time reflection; rough = environment-map reflection | leqVJhmy_zQ [03:40]
MOGRT | broadcast | Motion Graphics Template exported from After Effects for editing in Premiere Pro | qrMhd_D3yYU [00:40]
EasyTrack (Zero Density) | broadcast | Zero Density tracking hub that feeds camera and object tracking to multiple render engines | hN98GI8996w [08:31]
Portal window | broadcast | XR effect where virtual characters appear to step from a wall into the real set | hN98GI8996w [03:15]
Radiosity (Viz) | broadcast | Per-light setting that controls how much light colour bounces and bleeds onto surfaces in Viz real-time GI | zBeBgKY596k [01:08]
Asset View (Viz Artist 5) | broadcast | Viz Artist 5 window for browsing Graphic Hub assets by type tab | Yj_0Lg3Ljao [00:00]
Stage (Viz) | broadcast | Viz Artist window that holds animation and directors | GxEnE_UmzFA [06:20]
Continue reverse (Viz) | broadcast | Viz director command that plays an animation backwards from its start | i8J26rvFgnc [09:14]
Video Coder (XPression) | broadcast | Ross tool that converts media into formats XPression can play | KwxHdmv2HKw [17:03]
Quad (XPression) | broadcast | Basic rectangle object used as the fill of keys and lower thirds | KwxHdmv2HKw [00:38]
Field direction (Target effector) | c4d fields | Target effector mode where clones aim along the field's gradient, toward higher values, instead of at an object | cCCgPVurWjQ [44:51]
Subfield folder | c4d fields | Plus-button folder on a field parameter; any field inside drives that parameter | cCCgPVurWjQ [04:48]
Freeze field (Grow mode) | c4d fields | Layer that stores a selection and, in Grow mode, spreads it outward each frame | cCCgPVurWjQ [08:31]
MoGraph object into a field list | c4d fields | Dropping a matrix or cloner into a field list brings only its per-clone weights, no positions | cCCgPVurWjQ [31:09, 1:08:18]
Follow Position / Follow Rotation | c4d dynamics | Rigid Body tag force-tab values that let a moving parent or cloner steer a simulation | cCCgPVurWjQ [1:10:23]; _6toVWN7NMo [26:03]
Sleep / deactivation (rigid body) | c4d dynamics | A rigid body shown as black wireframe has gone to sleep and is not simulated until hit hard enough | _6toVWN7NMo [10:22]
Sleep Strength | c4d dynamics | Percent of the velocity thresholds a hit must exceed to wake a sleeping rigid body | _6toVWN7NMo [19:11]
Timer (rigid body) | c4d dynamics | New frames-below-threshold count before an object sleeps; 0 kills jitter but can freeze objects mid-air | _6toVWN7NMo [12:26]
Recoil (follow settings) | c4d dynamics | New springiness on Follow Position/Rotation; negative values smooth the blend | _6toVWN7NMo [28:40]
Scene Scale (simulation) | c4d dynamics | Project-setting value meant to equal the average size of dynamic objects | _6toVWN7NMo [03:39]
Cloth Surface | c4d cloth | Generator that adds thickness to a simulated cloth plane, parented with Cmd/Ctrl | dHQWVXWbsEM [06:49]
Smoothing iterations | c4d simulation | Project simulation setting that stops cloth and soft-body popping and jitter; too many stiffens cloth | dHQWVXWbsEM [14:04, 28:13]
Target Length (cloth) | c4d cloth | Cloth tag value; below 100 shrinks, above grows the cloth from its initial state | dHQWVXWbsEM [12:01]
Field Force | c4d simulation | Force that reads a field's vectors to attract or repel particles, cloth and pyro | dHQWVXWbsEM [19:19]; vrE2wrqq0TM [03:14]
Pyro advection (pyrovection) | c4d pyro | Particle modifier that makes particles follow a pyro simulation's velocity | vrE2wrqq0TM [15:10]
Data Mapper (particles) | c4d particles | Modifier mapping any particle value (age, speed) onto another (radius, colour); renamed by use, e.g. size by age | vrE2wrqq0TM [18:16]
Colour Mapper (particles) | c4d particles | Particle modifier colouring by age, distance traversed or velocity; colour acts as render data | vrE2wrqq0TM [20:24]
Seam selection tag | c4d uv | Special edge-selection tag that holds UV seams (2026.3), made via Mark as Seam | fsFbFDtLDT0 [20:06]
UV Weld tool | c4d uv | 2026.3 replacement for UV Terrace: hover shows arrows, click snaps an island back to its neighbour | fsFbFDtLDT0 [13:48]
Keep UV Connectivity | c4d uv | Default-on behaviour that keeps moved UV polygons attached; Control detaches | fsFbFDtLDT0 [09:35]
Ping back (particles) | c4d pyro | Particles snapping back after emission stops because the force is no longer holding them | vrE2wrqq0TM [39:33]
Pyro tag vs Pyro object | c4d | C4D 2023.1 Pyro makes both: the tag sets the emitter look (smoke, temperature, fuel), the object sets scene-wide behaviour (turbulence, dissipation, substeps) | TLlITrj5A_4 [02:36]
Voxel size (Pyro) | c4d | size of the 3D pixel of the sim grid; smaller is finer and much slower | TLlITrj5A_4 [06:14]
Vorticity strength | c4d | Pyro setting for the amount of chaotic swirl in smoke and fire | TLlITrj5A_4 [08:19]
Pyro Fuel tag | c4d | simulation tag on an object that burns or explodes when fire touches it | 2yaRgwWYoDg [08:35]
Simulation before generator | c4d | project setting that runs the sim before generators such as the Volume Mesher so meshes follow the sim | 2yaRgwWYoDg [12:14]
MoExtrude | c4d | MoGraph effector that extrudes every polygon of an object, steppable and layerable | 7-q1JKG8638 [01:03]
Memory node | c4d | scene-nodes node that stores a value or geometry for the next frame, the basis of a geometry solver | Iy2FAJbbyrY [04:49]
Geometry solver | c4d | frame-by-frame loop where last frame's geometry is changed and stored again, like a Houdini SOP solver | Iy2FAJbbyrY [00:33]
Loop Carve Value | c4d | scene-nodes loop node, run a set of operations a number of times set by a Range | jdBV7WrrIB8 [12:04]
Store Selection (node) | c4d | scene-nodes node that saves a selection as a tag so a material or other object can use it | 2z2pB3vIbk0 [08:37]
Datasmith (C4D importer) | pipeline | Unreal plugin that imports Cinema 4D scenes and native C4D materials | cut-ZBaB1b0 [07:51]
Geometry Cache (Unreal) | pipeline | import type for Alembic animation as playable vertex animation, marked experimental in UE 4.25 | cut-ZBaB1b0 [09:23]
Decay (field modifier layer) | c4d | C4D 2023.1 field layer that slows how fast affected clones return to rest after the field passes | tQbqZzk7Kc0 [01:35]
Freeze (field modifier layer) | c4d | C4D 2023.1 field layer that holds values; Grow mode spreads the selection outward by a radius | tQbqZzk7Kc0 [03:41]
Time field | c4d | Field that maps frame time to strength; with an offset it delays a Time effector start | mq2eMicxJZ4 [04:23]
Point-level animation (PLA) | c4d | Per-point animation baked onto a mesh, used to cache sims and hand them to engines | TEM9BU-Fp0E [02:35]
Cineware for Unreal | c4d | Maxon plugin that imports C4D scenes into Unreal via Datasmith, including geometry caches | TEM9BU-Fp0E [03:39]
Bake Objects | c4d | Timeline function that copies an object with its animation turned into keys | TEM9BU-Fp0E [02:35]
Cycle (cache node) | pipeline | Alembic playback mode beyond the last frame: hold, loop, reverse or bounce | jmjfqFuw0Sc [10:30]
tone map (Redshift Toon) | look-dev | Ramp that quantises diffuse, reflection or rim shading into steps | i3YczHKxtbo [02:03]
Tone Map Pattern | look-dev | Redshift node that turns tone-map steps into halftone dots, sine waves or a grid | i3YczHKxtbo [31:13]
matcap | look-dev | Image of a lit sphere used to shade an object by its normals, ignoring scene lights | rE_15TwtY5A [01:05]
bleed shell | look-dev | Blobby duplicate behind a model with a Fresnel-transparent material to fake paint spreading beyond edges | u6j9yrpgRhU [28:05]
Detect Separate Meshes | toon / lookdev | Redshift toon contour option that also draws lines where different meshes overlap or intersect, needed for a thick silhouette against a background object. | xaJ2pdIeLKA [03:46]
Change Range | lookdev | Node that remaps a value range (noise 0-1 to a new min and max, even negative), used to widen or cut toon line thickness and opacity. | 3Z6Td_LTpH0 [03:39]
Scalar User Data | lookdev | Node that reads a numeric user-data field per object so one material behaves differently for each object. | 3Z6Td_LTpH0 [08:49]
Contribution Scale (volume) | lighting | Per-light Redshift setting that sets how strongly the light scatters in a Redshift Environment volume; default 0 means no beams. | vnHKQmvKYH8 [01:39]
Phase (volume) | lighting | Redshift Environment control biasing scatter toward the camera when above 0 and away from it when below 0. | vnHKQmvKYH8 [05:04]
Horizon blur | lighting | Setting on Redshift height fog that softens the fog edge at the far horizon line. | vnHKQmvKYH8 [07:00]
Multi-Instance | c4d | C4D Cloner instance mode (R20) that keeps scenes with tens of millions of polygons responsive in the viewport. | cR5PCFKhVJc [02:39]
Sprite node | lookdev | Redshift node that renders cutout geometry such as leaves cheaply by using the opacity texture directly. | cR5PCFKhVJc [05:45]
Color Layer | lookdev | Redshift node that stacks colour inputs with Photoshop-like blend modes (subtract, multiply), used to build toon looks. | LWavn-Io1_o [06:27]
Set Driver / Set Driven (Absolute) | c4d | C4D expression pair that links one parameter to another; creates small Xpresso nulls that should be renamed. | eKG2QSWJYYM [14:38]
Chunk size (farm) | pipeline | Number of frames a worker renders before asking the supervisor for more work; 8 in the Qube demo. | p50NXgsMGiw [04:20]
Thin Wall | lookdev | Redshift standard material geometry option treating the object as infinitely thin so subsurface becomes simple translucency (leaves, paper). | a5BDzPkwlUM [06:29]
