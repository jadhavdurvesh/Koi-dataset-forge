import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SEEN_FILE = BASE_DIR / "generator" / ".seen_hashes"

_seen = None


def _load_seen():
    global _seen
    if _seen is None:
        _seen = set()
        if SEEN_FILE.exists():
            with open(SEEN_FILE, "r", encoding="utf-8") as f:
                _seen = {line.strip() for line in f if line.strip()}
    return _seen


def _hash_sample(sample):
    key = f"{sample.get('emotion', '')}|{sample.get('input', '')}|{sample.get('response', '')}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()


def is_duplicate(sample):
    """True if a sample with this emotion+input was already saved before."""
    return _hash_sample(sample) in _load_seen()


def remember(sample):
    """Record a saved sample so future runs can detect repeats of it."""
    seen = _load_seen()
    h = _hash_sample(sample)
    seen.add(h)
    SEEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SEEN_FILE, "a", encoding="utf-8") as f:
        f.write(h + "\n")
