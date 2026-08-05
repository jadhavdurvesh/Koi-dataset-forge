import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def save_sample(sample):
    emotion = sample["emotion"]

    folder = BASE_DIR / "datasets" / "raw" / "hearts"
    folder.mkdir(parents=True, exist_ok=True)

    filename = folder / f"{emotion}.jsonl"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(sample, ensure_ascii=False) + "\n")