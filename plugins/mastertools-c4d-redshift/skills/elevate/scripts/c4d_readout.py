"""c4d_readout.py: read-only scene readout for /elevate (Cinema 4D 2026, Python 3).

Run one of these ways:
  - Extensions > Script Manager: open this file and Execute.
  - Through the Maxon Cinema 4D MCP server's Python tool.
It reads the active document and prints JSON. If the document has been saved, it also
writes <document>_elevate_readout.json next to the .c4d file. It never modifies the scene:
no parameter writes, no inserts, no undo steps.

Parameters are read generically from each object's description (name -> value), so the
dump survives version differences without hard-coded parameter IDs.

Limits (stated in the JSON "notes"):
  - Redshift node-material graphs are not traversed. Node materials are listed with
    node_based=true; send a screenshot of the node editor or read them through the MCP.
  - Redshift AOVs live in the Redshift video post and are not expanded.
"""
import json
import os

import c4d

VERSION = "1.0"
MAX_PARAMS = 200          # per object / material / tag
MAX_OBJECTS = 400         # objects of interest
NODE_SPACE_RS = "com.redshift3d.redshift4c4d.class.nodespace"   # [T] confirm on the user's install
RS_LIGHT_ID = 1036751                                            # [T] Redshift Light object ID
KEYWORDS = ("Camera", "Light", "Extrude", "Text", "Sweep", "Lathe")


def _const(name, default=None):
    return getattr(c4d, name, default)


def safe_value(v):
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return round(v, 5) if isinstance(v, float) else v
    if isinstance(v, str):
        return v[:200]
    if isinstance(v, c4d.Vector):
        return [round(v.x, 4), round(v.y, 4), round(v.z, 4)]
    if isinstance(v, c4d.BaseTime):
        return {"seconds": round(v.Get(), 4)}
    return None


def dump_params(bl):
    """name -> simple value for every readable parameter in bl's description."""
    out = {}
    try:
        desc = bl.GetDescription(_const("DESCFLAGS_DESC_NONE", 0))
    except Exception as exc:
        return {"_error": "description unavailable: %s" % exc}
    count = 0
    for bc, paramid, _group in desc:
        if count >= MAX_PARAMS:
            out["_truncated"] = True
            break
        try:
            name = bc[_const("DESC_NAME", 1)]
        except Exception:
            name = None
        if not name:
            continue
        try:
            value = bl[paramid]
        except Exception:
            continue
        simple = safe_value(value)
        if simple is None:
            continue
        key = name
        if key in out:
            try:
                key = "%s [%s]" % (name, paramid[0].id)
            except Exception:
                key = "%s [%d]" % (name, count)
        out[key] = simple
        count += 1
    return out


def matrix_info(op):
    try:
        mg = op.GetMg()
        return {"position": safe_value(mg.off), "forward_axis": safe_value(mg.v3)}
    except Exception:
        return {}


def material_tags(op):
    names = []
    ttex = _const("Ttexture")
    tag = op.GetFirstTag()
    while tag:
        try:
            if ttex is not None and tag.GetType() == ttex:
                mat = tag.GetMaterial()
                names.append(mat.GetName() if mat else None)
        except Exception:
            pass
        tag = tag.GetNext()
    return names


def related_tags(op):
    """Redshift or camera-related tags on a camera (DOF often lives there)."""
    out = []
    tag = op.GetFirstTag()
    while tag:
        try:
            tname = tag.GetTypeName() or ""
            if "Redshift" in tname or "Camera" in tname:
                out.append({"tag": tname, "params": dump_params(tag)})
        except Exception:
            pass
        tag = tag.GetNext()
    return out


def classify(op):
    t = op.GetType()
    tname = op.GetTypeName() or ""
    if t == _const("Ocamera") or "Camera" in tname:
        return "camera"
    if t in (_const("Olight"), RS_LIGHT_ID) or "Light" in tname:
        return "light"
    if t in (_const("Oextrude"), _const("Osplinetext")) or any(k in tname for k in ("Extrude", "Text")):
        return "geometry"
    if any(k in tname for k in KEYWORDS):
        return "geometry"
    return None


def walk(doc):
    found = {"camera": [], "light": [], "geometry": []}
    total, truncated = 0, False
    stack = [doc.GetFirstObject()]
    while stack:
        op = stack.pop()
        while op:
            kind = classify(op)
            if kind:
                if total >= MAX_OBJECTS:
                    truncated = True
                else:
                    entry = {"name": op.GetName(), "type": op.GetTypeName(),
                             "type_id": op.GetType(), "params": dump_params(op)}
                    entry.update(matrix_info(op))
                    mats = material_tags(op)
                    if mats:
                        entry["materials"] = mats
                    if kind == "camera":
                        entry["tags"] = related_tags(op)
                    found[kind].append(entry)
                    total += 1
            child = op.GetDown()
            if child:
                stack.append(child)
            op = op.GetNext()
    return found, truncated


def node_based(mat):
    try:
        ref = mat.GetNodeMaterialReference()
        if ref is None:
            return False
        try:
            return bool(ref.HasSpace(NODE_SPACE_RS))
        except Exception:
            return "unknown"
    except Exception:
        return False


def materials(doc):
    out = []
    for mat in doc.GetMaterials():
        entry = {"name": mat.GetName(), "type": mat.GetTypeName(), "type_id": mat.GetType(),
                 "node_based": node_based(mat)}
        entry["params"] = dump_params(mat)
        out.append(entry)
    return out


def render_info(doc):
    rd = doc.GetActiveRenderData()
    fps = doc.GetFps()
    info = {"name": rd.GetName(), "fps_document": fps}
    fields = {"width": "RDATA_XRES", "height": "RDATA_YRES", "fps": "RDATA_FRAMERATE",
              "renderer_id": "RDATA_RENDERENGINE"}
    for key, const in fields.items():
        cid = _const(const)
        if cid is None:
            continue
        try:
            info[key] = safe_value(rd[cid])
        except Exception:
            pass
    for key, const in (("frame_from", "RDATA_FRAMEFROM"), ("frame_to", "RDATA_FRAMETO")):
        cid = _const(const)
        try:
            info[key] = rd[cid].GetFrame(fps)
        except Exception:
            pass
    posts = []
    vp = rd.GetFirstVideoPost()
    while vp:
        posts.append(vp.GetName())
        vp = vp.GetNext()
    info["video_posts"] = posts
    return info


def takes(doc):
    try:
        td = doc.GetTakeData()
        main = td.GetMainTake()
    except Exception:
        return {}
    names, stack = [], [main]
    while stack:
        tk = stack.pop()
        while tk:
            names.append(tk.GetName())
            if tk.GetDown():
                stack.append(tk.GetDown())
            tk = tk.GetNext()
    try:
        current = td.GetCurrentTake().GetName()
    except Exception:
        current = None
    return {"current": current, "all": names}


def main():
    doc = c4d.documents.GetActiveDocument()
    if doc is None:
        print(json.dumps({"error": "no active document"}))
        return
    found, truncated = walk(doc)
    data = {
        "tool": "elevate c4d_readout", "version": VERSION,
        "document": doc.GetDocumentName(),
        "render": render_info(doc),
        "cameras": found["camera"], "lights": found["light"], "geometry": found["geometry"],
        "materials": materials(doc),
        "takes": takes(doc),
        "notes": ["read-only dump; values are for diagnosis, never judged here (render values -> redshift skill)",
                  "Redshift node graphs not traversed; node_based materials need a node-editor screenshot or MCP read",
                  "Redshift AOVs not expanded (see video_posts)"],
    }
    if truncated:
        data["notes"].append("object list truncated at %d objects of interest" % MAX_OBJECTS)
    text = json.dumps(data, indent=1, ensure_ascii=False)
    print(text)
    folder = doc.GetDocumentPath()
    if folder:
        base = os.path.splitext(doc.GetDocumentName())[0]
        path = os.path.join(folder, base + "_elevate_readout.json")
        try:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
            print("elevate readout written: %s" % path)
        except Exception as exc:
            print("elevate readout: could not write file (%s); copy the JSON above instead" % exc)
    else:
        print("elevate readout: document not saved, so JSON was printed only")


if __name__ == "__main__":
    main()
