"""Daily backup of the user's taste decisions.

Copies the irreplaceable files (decisions.jsonl, usage.jsonl, .project-salt, rounds/, predictions/,
scores/, test-set/, grids/, library/inventory.csv, library/dial.csv, library/awards.json) into one gzip JSON
archive in two places: DT/backups/ and ~/.config/mastertools/design-taste-backups/ (outside DT, so one
mishap can't take both; DESIGN_TASTE_BACKUP_DIR overrides it). Keeps the newest 7 in each.
`--drill` restores the newest archive into a temp folder and compares every file byte for byte.
"""
import base64, glob, gzip, hashlib, json, os, sys, tempfile
from datetime import datetime, timezone
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dt import DT, ready

KEEP = 7
LOCAL = os.environ.get("DESIGN_TASTE_BACKUP_DIR") or os.path.expanduser("~/.config/mastertools/design-taste-backups")
# .project-salt keeps project hashes stable after a restore; without it old and new uses look like different projects.
PATTERNS = ["decisions.jsonl", "usage.jsonl", ".project-salt", "rounds/*", "predictions/*", "scores/*", "test-set/*", "grids/*",
            "library/inventory.csv", "library/dial.csv", "library/awards.json"]

def collect():
    files = {}
    for pat in PATTERNS:
        for p in sorted(glob.glob(os.path.join(DT, pat))):
            if os.path.isfile(p):
                files[os.path.relpath(p, DT)] = base64.b64encode(open(p, "rb").read()).decode()
    return files

def backup():
    if not ready():
        sys.exit("not backed up: the Design Taste folder is not reachable from here")
    files = collect()
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    blob = gzip.compress(json.dumps({"at": stamp, "files": files}).encode())
    for d in (os.path.join(DT, "backups"), LOCAL):
        os.makedirs(d, exist_ok=True)
        tmp = os.path.join(d, f".tmp-{stamp}")
        open(tmp, "wb").write(blob)
        os.replace(tmp, os.path.join(d, f"taste-{stamp}.json.gz"))
        for old in sorted(glob.glob(os.path.join(d, "taste-*.json.gz")))[:-KEEP]:
            os.remove(old)
    print(f"backed up {len(files)} files ({len(blob)} bytes) to DT/backups and {LOCAL}")

def drill():
    newest = sorted(glob.glob(os.path.join(LOCAL, "taste-*.json.gz")))[-1]
    snap = json.loads(gzip.decompress(open(newest, "rb").read()))
    live = collect()
    with tempfile.TemporaryDirectory() as t:
        for rel, b64 in snap["files"].items():
            p = os.path.join(t, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "wb").write(base64.b64decode(b64))
        missing = [r for r in live if r not in snap["files"]]
        changed = [r for r in snap["files"] if r in live and hashlib.sha256(open(os.path.join(t, r), "rb").read()).hexdigest() != hashlib.sha256(base64.b64decode(live[r])).hexdigest()]
    print(f"drill {os.path.basename(newest)}: {len(snap['files'])} restored, {len(missing)} missing, {len(changed)} changed since backup")
    return 0 if not missing and not changed else 1

if __name__ == "__main__":
    sys.exit(drill() if "--drill" in sys.argv else backup())
