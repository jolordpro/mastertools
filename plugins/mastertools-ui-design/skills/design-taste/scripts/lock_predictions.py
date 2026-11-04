"""Lock a round's prediction file before the user sees the round.

Checks every pair has all four sources (a source may abstain with null), makes the file
read-only and appends its sha256 to DT/predictions/LOCK.log. Refuses to lock twice.
"""
import hashlib, json, os, sys
from datetime import datetime, timezone

SOURCES = ("profile", "frontend_design", "convention", "jury")

def main(path):
    data = json.load(open(path))
    for p in data["pairs"]:
        missing = [s for s in SOURCES if s not in p["predictions"]]
        if missing:
            sys.exit(f"refused: pair {p['id']} lacks {missing}")
        for s, v in p["predictions"].items():
            if v is not None and v["pick"] not in ("A", "B"):
                sys.exit(f"refused: pair {p['id']} source {s} pick must be A, B or null")
    log = os.path.join(os.path.dirname(path), "LOCK.log")
    name = os.path.basename(path)
    if os.path.exists(log) and any(l.split(" ")[1] == name for l in open(log) if l.strip()):
        sys.exit(f"refused: {name} is already locked")
    digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
    os.chmod(path, 0o444)
    with open(log, "a") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {name} sha256={digest} pairs={len(data['pairs'])}\n")
    print(f"locked {name}: sha256 {digest}")

if __name__ == "__main__":
    main(sys.argv[1])
