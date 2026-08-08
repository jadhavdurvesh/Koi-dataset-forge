import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = BASE_DIR / "configs"
KNOWLEDGE_DIR = BASE_DIR / "knowledge"
PARTS_DIR = CONFIG_DIR / "scenario_parts"


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


CURATED_SCENARIOS = load(CONFIG_DIR / "scenarios.json")
SITUATIONS = load(CONFIG_DIR / "situations.json")
_EMOTION_ENTRIES = load(KNOWLEDGE_DIR / "psychology" / "emotions.json")
EMOTIONS = [e["name"] for e in _EMOTION_ENTRIES]
EMOTION_DESCRIPTIONS = {e["name"]: e["description"] for e in _EMOTION_ENTRIES}

PEOPLE = load(PARTS_DIR / "people.json")
PLACES = load(PARTS_DIR / "places.json")
EVENTS_POSITIVE = load(PARTS_DIR / "events_positive.json")
EVENTS_NEGATIVE = load(PARTS_DIR / "events_negative.json")
THOUGHTS_POSITIVE = load(PARTS_DIR / "thoughts_positive.json")
THOUGHTS_NEGATIVE = load(PARTS_DIR / "thoughts_negative.json")

# Which emotions are "positive-valence" vs "negative-valence" — this is what
# keeps compositional generation emotionally coherent. Without it you get
# nonsense like "joy" paired with the event "criticized me".
POSITIVE_EMOTIONS = {"joy", "love", "hope"}
# Everything else (sadness, loneliness, anxiety, grief, fear) is negative-valence.

# Index curated hand-written scenarios by emotion for quick lookup.
_CURATED_BY_EMOTION = {}
for s in CURATED_SCENARIOS:
    _CURATED_BY_EMOTION.setdefault(s["emotion"], []).append(s)


def _compose_input(emotion):
    """
    Combine person + event + place + thought into a fresh sentence, using
    the event/thought pool that actually matches the emotion's valence so
    the result stays emotionally coherent (e.g. "joy" only pairs with
    positive events like "praised me", never "criticized me").
    """
    if emotion in POSITIVE_EMOTIONS:
        event = random.choice(EVENTS_POSITIVE)
        thought = random.choice(THOUGHTS_POSITIVE)
    else:
        event = random.choice(EVENTS_NEGATIVE)
        thought = random.choice(THOUGHTS_NEGATIVE)

    person = random.choice(PEOPLE)
    place = random.choice(PLACES)
    sentence = f"{person} {event} {place}.".capitalize()
    return f"{sentence} {thought}"


def generate_scenario():
    """
    Pick a primary emotion and produce a matching situation + input.

    Uses a curated hand-written example when a good one exists (higher
    quality, more natural phrasing), and otherwise falls back to
    valence-aware compositional generation — which covers every emotion in
    knowledge/psychology/emotions.json, not just the 3 that happen to have
    curated scenarios today, while staying emotionally coherent.
    """
    emotion = random.choice(EMOTIONS)
    curated = _CURATED_BY_EMOTION.get(emotion)

    if curated and random.random() < 0.15:
        scenario = random.choice(curated)
        return {
            "emotion": emotion,
            "emotion_description": EMOTION_DESCRIPTIONS[emotion],
            "situation": scenario["situation"],
            "input": random.choice(scenario["examples"]),
        }

    return {
        "emotion": emotion,
        "emotion_description": EMOTION_DESCRIPTIONS[emotion],
        "situation": random.choice(SITUATIONS),
        "input": _compose_input(emotion),
    }


if __name__ == "__main__":
    print(generate_scenario())
