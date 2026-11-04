import numpy as np
"""Known-positive / known-negative checks for look.py. run_all() -> list of (name, status, detail).
status is PASS, FAIL or SKIP (SKIP only when Apple Vision is not available on this machine)."""
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
import cv2  # noqa: E402
import look  # noqa: E402
import synth  # noqa: E402


def _run(img, tmp, name, no_vision):
    p = os.path.join(tmp, name + ".png")
    cv2.imwrite(p, img)
    out = os.path.join(tmp, name + ("_nv" if no_vision else "_v"))
    rc = look.run(p, "auto", out, no_vision)
    if rc != 0:
        raise RuntimeError("look.run returned %s" % rc)
    return json.load(open(os.path.join(out, "report.json")))


def _vision_available(tmp):
    rep = _run(synth.flat_scene(320, 180), tmp, "probe", False)
    return rep["vision"]


def run_all():
    res = []
    tmp = tempfile.mkdtemp(prefix="comp_selftest_")

    def check(name, cond, detail=""):
        res.append((name, "PASS" if cond else "FAIL", detail))

    def skip(name, why):
        res.append((name, "SKIP", why))

    try:
        vis_ok = _vision_available(tmp)

        # 1 tilt 2 deg vs 0 deg (lines detector, no Vision needed)
        t2 = _run(synth.horizon(2.0), tmp, "tilt2", True)["metrics"]["horizon"]
        t0 = _run(synth.horizon(0.0), tmp, "tilt0", True)["metrics"]["horizon"]
        v2 = t2.get("value") or {}
        check("horizon lines: 2 deg tilt read as +2 and flagged", abs((v2.get("tilt_deg") or 99) - 2.0) < 0.6 and v2.get("accidental_tilt_flag") is True, str(v2.get("tilt_deg")))
        v0 = t0.get("value") or {}
        check("horizon lines: 0 deg not flagged", v0.get("accidental_tilt_flag") is False and abs(v0.get("tilt_deg", 99)) < 0.5, str(v0.get("tilt_deg")))
        if vis_ok:
            a2 = _run(synth.horizon(2.0), tmp, "tilt2", False)["metrics"]["horizon"].get("value") or {}
            a0 = _run(synth.horizon(0.0), tmp, "tilt0", False)["metrics"]["horizon"].get("value") or {}
            check("horizon apple+lines: 2 deg flagged, agrees, sign matches lines", a2.get("accidental_tilt_flag") is True and a2.get("cross_check_agrees") is True and abs(a2.get("tilt_deg", 99) - 2.0) < 0.8, json.dumps(a2)[:160])
            check("horizon apple+lines: 0 deg not flagged", a0.get("accidental_tilt_flag") is False, json.dumps(a0)[:160])
        else:
            skip("horizon apple+lines", "no Vision")

        # 2 corner highlight vs none; flat frame must not crash and must say why
        for nv in ([False, True] if vis_ok else [True]):
            tag = "vision" if not nv else "no-vision approx"
            rp = _run(synth.corner_highlight(), tmp, "corner", nv)["metrics"]["saliency"]
            pk = ((rp.get("value") or {}).get("peaks") or [{}])[0]
            check("saliency (%s): corner highlight peak lands in D1" % tag, pk.get("x", 0) > 0.75 and pk.get("y", 1) < 0.3 and pk.get("cell") == "D1", str(pk))
            rf = _run(synth.flat_scene(), tmp, "flat", nv)["metrics"]["saliency"]
            check("saliency (%s): flat frame gives null + reason, no crash" % tag, rf.get("confidence") is None and bool(rf.get("reason")), str(rf)[:120])

        # 3 low vs high contrast text (direct on a known box, then end to end via OCR)
        lo, box = synth.text_frame((140, 140, 140), (128, 128, 128))
        hi, boxh = synth.text_frame((255, 255, 255), (0, 0, 0))
        tl, th = look.text_contrast(lo, box), look.text_contrast(hi, boxh)
        check("text contrast: low-contrast text fails 3.0", tl is not None and tl["pass_3_0"] is False and tl["contrast_worst"] < 1.5, str(tl))
        check("text contrast: white-on-black passes 4.5", th is not None and th["pass_4_5"] is True and th["contrast_worst"] > 15, str(th))
        mid, boxm = synth.text_frame((255, 255, 255), (140, 140, 140))   # known ratio about 3.4
        tm = look.text_contrast(mid, boxm)
        check("text contrast: ratio ~3.4 passes 3.0 and fails 4.5", tm is not None and tm["pass_3_0"] and not tm["pass_4_5"], str(tm))
        if vis_ok:
            rh = _run(hi, tmp, "text_hi", False)["metrics"]["text"]
            bx = (rh.get("value") or {}).get("boxes") or []
            check("text e2e: OCR reads white-on-black and passes 4.5", bool(bx) and bx[0].get("pass_4_5") is True and "MATCH" in bx[0]["text"].upper(), str(bx[:1])[:200])
        else:
            skip("text e2e", "no Vision")

        # 4 subject crowded at edge facing out vs centred (metric functions on a known mask and facing)
        facing = (0.7, 0.9)   # nose right of eye midpoint
        bbox_out, c_out = [0.84, 0.3, 0.14, 0.4], (0.91, 0.5)
        m_out = look.facing_metrics(bbox_out, c_out, facing, "test")["value"]
        check("facing: crowded at right edge facing right -> inward -1, outward_near_edge flag", m_out["inward_score"] == -1 and m_out["outward_near_edge_flag"] is True and m_out["space_ratio_front_back"] < 0.2, str(m_out))
        bbox_in, c_in = [0.15, 0.3, 0.2, 0.4], (0.25, 0.5)
        m_in = look.facing_metrics(bbox_in, c_in, facing, "test")["value"]
        check("facing: left of centre facing right -> inward +1, no flag", m_in["inward_score"] == 1 and m_in["outward_near_edge_flag"] is False and m_in["space_ratio_front_back"] > 2, str(m_in))
        m_c = look.facing_metrics([0.4, 0.3, 0.2, 0.4], (0.5, 0.5), facing, "test")["value"]
        check("facing: centred -> inward 0, no flag", m_c["inward_score"] == 0 and m_c["outward_near_edge_flag"] is False, str(m_c))
        fr = look.facing_metrics(bbox_in, c_in, (0.05, 1.0), "test")
        check("facing: frontal face gives null + reason", fr["confidence"] is None and "faces the camera" in fr["reason"], str(fr))
        ff = look.facing_from_face({"left_eye": {"x": 0.45, "y": 0.4}, "right_eye": {"x": 0.55, "y": 0.4}, "nose": {"x": 0.56, "y": 0.45}, "confidence": 1})
        fl = look.facing_from_face({"left_eye": {"x": 0.45, "y": 0.4}, "right_eye": {"x": 0.55, "y": 0.4}, "nose": {"x": 0.44, "y": 0.45}, "confidence": 1})
        check("facing_from_face: nose right of eyes = +, left = -", ff[0] > 0.2 and fl[0] < -0.2, "%s %s" % (ff, fl))
        e_edge = look.edge_distances(synth.subject_mask(0.5, 0.5, 0.99, 0.5))
        e_mid = look.edge_distances(synth.subject_mask(0.5, 0.5, 0.4, 0.4))
        check("tangent: mask 0.5% from the edge flagged, centred not", e_edge["tangent_flag"] is True and e_mid["tangent_flag"] is False, str((e_edge["per_side"], e_mid["tangent_flag"])))
        e_cut = look.edge_distances(synth.subject_mask(0.5, 0.5, 1.2, 0.5))
        check("tangent: mask crossing the edge is 'touches', not tangent", e_cut["tangent_flag"] is False and "left" in e_cut["touches_edge_sides"], str(e_cut["touches_edge_sides"]))
        jc_hit = look.joint_crop({"joints": {"left_hand_joint": {"x": 0.015, "y": 0.5, "confidence": 0.9}}})
        jc_ok = look.joint_crop({"joints": {"left_hand_joint": {"x": 0.3, "y": 0.5, "confidence": 0.9}}})
        check("joint crop: wrist at 1.5% flagged, wrist at 30% not", len(jc_hit) == 1 and jc_ok == [], str(jc_hit))

        # 5 flattened vs full tonal range
        tf = look.tone_metrics(look.to_lab(synth.value_range(True))[..., 0])
        tq = look.tone_metrics(look.to_lab(synth.value_range(False))[..., 0])
        check("tone: full range not flat, spread > 70", tf["flat_flag"] is False and tf["L_spread_p5_p95"] > 70, str(tf["L_spread_p5_p95"]))
        check("tone: flattened range flagged, spread < 25", tq["flat_flag"] is True and tq["L_spread_p5_p95"] < 25, str(tq["L_spread_p5_p95"]))

        # 6 text outside vs inside graphics safe
        rects = look.safe_rects("16:9")
        check("safe area: box at 1% outside, box at 30% inside",
              not look.box_inside({"x": 0.01, "y": 0.4, "w": 0.3, "h": 0.1}, rects["graphics"]) and look.box_inside({"x": 0.3, "y": 0.4, "w": 0.3, "h": 0.1}, rects["graphics"]), "")
        # regression: low-contrast text on a small plate over bright ice. The old measure padded past the
        # plate and read the ice, giving ~3.5:1 on a true ~1.5:1 caption.
        from PIL import Image as _I, ImageDraw as _D, ImageFont as _F
        im = _I.new("RGB", (960, 540), (235, 238, 240))
        d = _D.Draw(im)
        d.rectangle([630, 395, 865, 472], fill=(119, 145, 131))
        f = _F.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 33)
        d.text((646, 405), "THIS WEEK", font=f, fill=(108, 109, 127))
        tb = d.textbbox((646, 405), "THIS WEEK", font=f)
        bgr_p = np.asarray(im)[..., ::-1].copy()
        tc = look.text_contrast(bgr_p, {"x": tb[0] / 960, "y": tb[1] / 540, "w": (tb[2] - tb[0]) / 960, "h": (tb[3] - tb[1]) / 540})
        check("text contrast: faint caption on a plate over bright ice reads under 2:1 (true ~1.5)",
              tc is not None and tc["contrast_worst"] < 2.0, str(tc))
        r9 = look.safe_rects("9:16")
        check("safe area 9:16: box at 5% outside the 9:16 hard box", not look.box_inside({"x": 0.05, "y": 0.4, "w": 0.3, "h": 0.05}, r9["graphics"]), str(r9["graphics"]))
        check("safe area 9:16: caption-band box (y 1300-1400 px) outside, mid box inside",
              not look.box_inside({"x": 0.3, "y": 1300 / 1920, "w": 0.3, "h": 100 / 1920}, r9["graphics"])
              and look.box_inside({"x": 0.3, "y": 0.4, "w": 0.3, "h": 0.05}, r9["graphics"]), str(r9["graphics"]))
        if vis_ok:
            out_img, _ = synth.text_frame((255, 255, 255), (0, 0, 0), xy=(0.01, 0.4), size=110)
            in_img, _ = synth.text_frame((255, 255, 255), (0, 0, 0), xy=(0.2, 0.4), size=110)
            ro = _run(out_img, tmp, "txt_out", False)["metrics"]["text_outside_graphics_safe"]
            ri = _run(in_img, tmp, "txt_in", False)["metrics"]["text_outside_graphics_safe"]
            check("safe area e2e: OCR text at 1% flagged, text at 20% not",
                  (ro.get("value") or {}).get("flag") is True and (ri.get("value") or {}).get("flag") is False, "%s | %s" % (str(ro)[:100], str(ri)[:100]))
        else:
            skip("safe area e2e", "no Vision")

        # 7 no-vision run: honest nulls, flag, fallback saliency
        nv = _run(synth.corner_highlight(), tmp, "nvcheck", True)
        m = nv["metrics"]
        check("no-vision: report says vision false", nv["vision"] is False, str(nv["vision_reason_off"]))
        need = ["subject", "subject_delta_L", "subject_capture", "facing", "joint_crop", "text", "text_outside_graphics_safe", "edge_distance", "tangent", "objectness", "aesthetics"]
        bad = [k for k in need if not (m[k]["confidence"] is None and "no-vision" in m[k].get("reason", ""))]
        check("no-vision: every Vision-only metric is null with reason 'no-vision'", not bad, str(bad))
        check("no-vision: approximate saliency, balance and thumbnail still reported", m["saliency"]["confidence"] and m["balance"]["confidence"] and m["thumbnail_survival"]["confidence"], "")
        check("no-vision: board.jpg long edge <= 2576", max(nv["board_size"]) <= 2576, str(nv["board_size"]))
        # every metric dict carries confidence number or null+reason
        broken = []
        for k, v in m.items():
            if isinstance(v, dict) and "confidence" in v and v["confidence"] is None and not v.get("reason"):
                broken.append(k)
            if isinstance(v, dict) and "confidence" not in v and k not in ("safe_area",):
                broken.append(k)
        check("every metric has a confidence or a null reason", not broken, str(broken))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return res
