import argparse

from engines.templates import random_template
from engines.scenario_generator import generate_scenario
from engines.response_generator import generate_response
from engines.blueprint_engine import build_blueprint

from core.validator import validate
from core.exporter import save_sample
from core.id_generator import generate_id
from engines.scenario_forge import create_message

from core.stats import record, show


parser = argparse.ArgumentParser(
    description="KOI Hearts Dataset Generator"
)

parser.add_argument(
    "--count",
    type=int,
    default=1,
    help="Number of samples to generate"
)

args = parser.parse_args()

for _ in range(args.count):

    template = random_template()
    scenario = generate_scenario()
    blueprint = build_blueprint()

    sample = {
        "id": generate_id(),

        **template,
        **scenario,
        **blueprint,

        "response": generate_response(scenario["emotion"])
    }

    valid, message = validate(sample)

    if valid:
        save_sample(sample)
        print(f"✅ {sample['id']} saved successfully.")
    else:
        print(f"❌ Validation failed: {message}")

record(sample)
show()
