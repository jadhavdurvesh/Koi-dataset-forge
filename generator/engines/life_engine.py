import json
import random
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Life configuration directory
LIFE_DIR = BASE_DIR / "configs" / "life"


def load(filename):
    """Load a JSON configuration file."""
    with open(LIFE_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


# Load configuration files
AGE_GROUPS = load("age_groups.json")
EDUCATION = load("education.json")
OCCUPATIONS = load("occupations.json")
PERSONALITIES = load("personalities.json")
RELATIONSHIPS = load("relationships.json")
LIFE_EVENTS = load("life_events.json")
LIVING_SITUATIONS = load("living_situations.json")
SUPPORT_SYSTEMS = load("support_systems.json")
RELATIONSHIP_STATUS = load("relationship_status.json")


def generate_person():
    """Generate a realistic life profile."""

    # Select an age group
    age_group = random.choice(AGE_GROUPS)
    group = age_group["group"]

    # Generate an age within that group
    age = random.randint(age_group["min"], age_group["max"])

    # Pick education and occupation that match the age group
    education = random.choice(EDUCATION[group])
    occupation = random.choice(OCCUPATIONS[group])

    return {
        "age": age,
        "age_group": group,

        "education": education,
        "occupation": occupation,

        "personality": random.choice(PERSONALITIES),

        "relationship": random.choice(RELATIONSHIPS),

        "relationship_status": random.choice(RELATIONSHIP_STATUS),

        "living_situation": random.choice(LIVING_SITUATIONS),

        "support_system": random.choice(SUPPORT_SYSTEMS),

        "life_event": random.choice(LIFE_EVENTS)
    }


if __name__ == "__main__":
    print(generate_person())