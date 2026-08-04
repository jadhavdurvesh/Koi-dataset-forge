import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "configs" / "scenarios.json", encoding="utf-8") as f:
    SCENARIOS = json.load(f)


def generate_scenario():
    scenario = random.choice(SCENARIOS)

    return {
        "emotion": scenario["emotion"],
        "situation": scenario["situation"],
        "input": random.choice(scenario["examples"])
    }