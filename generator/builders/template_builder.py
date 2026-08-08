import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = BASE_DIR / "configs"
KNOWLEDGE_DIR = BASE_DIR / "knowledge"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# emotions.json lives in the knowledge layer, not configs/
# (configs/emotions.json never existed — this was a dead path).
emotions = load_json(KNOWLEDGE_DIR / "psychology" / "emotions.json")
situations = load_json(CONFIG_DIR / "situations.json")
styles = load_json(CONFIG_DIR / "styles.json")


def random_template():
    emotion = random.choice(emotions)

    return {
        "emotion": emotion["name"],
        "emotion_description": emotion["description"],
        "situation": random.choice(situations),
        "style": random.choice(styles),
        "intensity": random.randint(1, 5),
    }
