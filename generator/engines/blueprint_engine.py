import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIGS = BASE_DIR / "configs"


def load(name):
    with open(CONFIGS / name, encoding="utf-8") as f:
        return json.load(f)


needs = load("needs.json")
intents = load("intents.json")
styles = load("communication_styles.json")


def build_blueprint():

    return {
        "secondary_emotion": random.choice([
            "hope",
            "fear",
            "gratitude",
            "confusion",
            "none"
        ]),

        "intent": random.choice(intents),

        "need": random.choice(needs),

        "communication_style": random.choice(styles),

        "response_style": random.choice([
            "gentle",
            "reflective",
            "warm",
            "encouraging"
        ])
    }