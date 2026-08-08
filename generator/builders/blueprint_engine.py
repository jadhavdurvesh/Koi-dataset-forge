import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"


def load(*parts):
    with open(KNOWLEDGE_DIR.joinpath(*parts), "r", encoding="utf-8") as f:
        return json.load(f)


# The rules: for each primary emotion, which needs / intents / communication
# styles / response styles are actually plausible. This is what makes the
# generator produce psychologically coherent samples instead of randomly
# pairing e.g. "joy" with "processing_loss".
EMOTION_BLUEPRINT = load("koi", "emotion_blueprint.json")

# Fallback vocabularies, used only for an emotion with no blueprint entry.
ALL_NEEDS = load("psychology", "needs.json")
ALL_INTENTS = load("koi", "intents.json")
ALL_STYLES = load("koi", "communication_styles.json")
ALL_RESPONSE_STYLES = load("koi", "response_styles.json")


def build_blueprint(emotion):
    """
    Build a psychologically consistent blueprint for a given primary emotion:

        emotion -> need -> intent -> communication style -> response style

    Rather than picking each field independently at random, this looks up
    the plausible options for the given emotion (from emotion_blueprint.json)
    and picks among those, so every generated sample stays emotionally
    coherent. Falls back to the full vocabulary for any emotion that doesn't
    have an entry yet, so new emotions never crash the pipeline.
    """
    rules = EMOTION_BLUEPRINT.get(emotion, {})

    return {
        "need": random.choice(rules.get("needs") or ALL_NEEDS),
        "intent": random.choice(rules.get("intents") or ALL_INTENTS),
        "communication_style": random.choice(rules.get("communication_styles") or ALL_STYLES),
        "response_style": random.choice(rules.get("response_styles") or ALL_RESPONSE_STYLES),
        "secondary_emotion": random.choice(rules.get("secondary_emotions") or ["none"]),
    }


if __name__ == "__main__":
    print(build_blueprint("loneliness"))
