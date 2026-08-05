import json
import random
from pathlib import Path

from pathlib import Path
import json
import random

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = BASE_DIR / "configs"


def load_json(filename):
    with open(CONFIG_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


emotions = load_json("emotions.json")
situations = load_json("situations.json")
styles = load_json("styles.json")


def random_template():
    emotion = random.choice(emotions)

    return {
        "emotion": emotion["name"],
        "emotion_description": emotion["description"],
        "situation": random.choice(situations),
        "style": random.choice(styles),
        "intensity": random.randint(1, 5)
    }