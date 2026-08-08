import argparse
import sys
from pathlib import Path

# Allow running this file directly as `python3 pipeline/generate.py`
# (not just `python3 -m pipeline.generate`) by putting generator/ on
# sys.path so the builders/engines/core packages resolve either way.
GENERATOR_DIR = Path(__file__).resolve().parent.parent
if str(GENERATOR_DIR) not in sys.path:
    sys.path.insert(0, str(GENERATOR_DIR))

from builders.template_builder import random_template
from builders.blueprint_engine import build_blueprint
from engines.scenario_engine import generate_scenario
from engines.response_engine import generate_response
from engines.life_engine import generate_person

from core.validator import validate
from core.exporter import save_sample
from core.id_generator import generate_id
from core.diversity import is_duplicate, remember
from core.stats import record, show


def main():
    parser = argparse.ArgumentParser(description="KOI Hearts Dataset Generator")
    parser.add_argument(
        "--count", type=int, default=1,
        help="Target number of valid, unique samples to SAVE (not attempts).",
    )
    args = parser.parse_args()

    saved = 0
    skipped_duplicates = 0
    rejected = 0
    attempts = 0
    # Safety cap: if the target is unreachable (vocab exhausted), stop
    # instead of looping forever. 8x the target is generous headroom.
    max_attempts = max(args.count * 8, 100)
    # For large runs, printing every single line is unusable — report
    # progress periodically instead, but always print every line for small
    # runs so nothing feels silent.
    report_every = max(1, args.count // 20) if args.count > 50 else 1

    while saved < args.count and attempts < max_attempts:
        attempts += 1
        person = generate_person()
        template = random_template()
        scenario = generate_scenario()

        # The blueprint is built from the scenario's emotion (not the
        # template's) so that need/intent/style stay consistent with the
        # emotion that actually drove the situation and input text.
        blueprint = build_blueprint(scenario["emotion"])

        sample = {
            "id": generate_id(),
            "person": person,
            "emotion": scenario["emotion"],
            "emotion_description": scenario["emotion_description"],
            "situation": scenario["situation"],
            "style": template["style"],
            "intensity": template["intensity"],
            "input": scenario["input"],
            **blueprint,
            "response": generate_response(
                scenario["emotion"], need=blueprint["need"], intent=blueprint["intent"]
            ),
        }

        if is_duplicate(sample):
            skipped_duplicates += 1
            continue

        valid, message = validate(sample)

        if not valid:
            rejected += 1
            if args.count <= 50:
                print(f"❌ Validation failed: {message}")
            continue

        save_sample(sample)
        record(sample)
        remember(sample)
        saved += 1

        if args.count <= 50:
            print(f"✅ {sample['id']} saved successfully.")
        elif saved % report_every == 0:
            print(f"... {saved}/{args.count} saved | {attempts} attempts | {skipped_duplicates} duplicates | {rejected} rejected")

    show()
    if saved < args.count:
        print(
            f"\n⚠️  Stopped early: only {saved}/{args.count} unique samples were reachable "
            f"after {attempts} attempts (vocabulary pool exhausted). "
            f"Add more entries to configs/scenario_parts/ to raise the ceiling."
        )
    print(f"\n{saved}/{args.count} saved | {rejected} rejected | {skipped_duplicates} duplicates skipped | {attempts} total attempts.")


if __name__ == "__main__":
    main()
