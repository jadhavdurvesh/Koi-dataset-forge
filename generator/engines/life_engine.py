import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

PARTS = BASE_DIR / "configs" / "scenario_parts"


def load(name):
    with open(PARTS / name, encoding="utf-8") as f:
        return json.load(f)


people = load("people.json")
events = load("events.json")
places = load("places.json")
thoughts = load("thoughts.json")


def create_message():

    person = random.choice(people)
    event = random.choice(events)
    place = random.choice(places)
    thought = random.choice(thoughts)

    return f"{person} {event} {place}. {thought}"