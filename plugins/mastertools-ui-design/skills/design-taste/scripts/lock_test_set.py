"""Lock a stratified random third of the specimen inventory as the test set.

Run once, before the user sees any specimen. Refuses to run again if a split exists.
Writes test-set/split.json (read-only) and appends a line to test-set/LOCK.log.
"""
import csv, hashlib, json, os, secrets, sys, random
from datetime import datetime, timezone

root = sys.argv[1]
inv_path = os.path.join(root, "library", "inventory.csv")
out = os.path.join(root, "test-set", "split.json")
if os.path.exists(out):
    sys.exit("split.json already exists; the test set is locked. Not overwriting.")

raw = open(inv_path, "rb").read()
rows = list(csv.DictReader(open(inv_path, newline="")))
seed = secrets.randbits(64)
rng = random.Random(seed)
test, train = [], []
for lane in ("proven", "crafted", "expressive"):
    ids = sorted(r["id"] for r in rows if r["lane"] == lane)
    k = round(len(ids) / 3)
    pick = set(rng.sample(ids, k))
    test += [i for i in ids if i in pick]
    train += [i for i in ids if i not in pick]

split = {
    "locked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "inventory_sha256": hashlib.sha256(raw).hexdigest(),
    "seed": seed,
    "rule": "Test ids never appear in a round, a grid or a draft shown to the user. Replace a test work only with another unseen work from the same lane, logged here.",
    "test": test,
    "train": train,
}
body = json.dumps(split, indent=2)
open(out, "w").write(body)
os.chmod(out, 0o444)
digest = hashlib.sha256(body.encode()).hexdigest()
with open(os.path.join(root, "test-set", "LOCK.log"), "a") as f:
    f.write(f"{split['locked_at']} split.json sha256={digest} test={len(test)} train={len(train)}\n")
print(f"locked {len(test)} test / {len(train)} train; split sha256 {digest}")
for lane in ("proven", "crafted", "expressive"):
    n = sum(1 for r in rows if r["lane"] == lane and r["id"] in test)
    print(f"  {lane}: {n} in test")
