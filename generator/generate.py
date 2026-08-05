from engines.templates import random_template
from engines.scenario_generator import generate_scenario
from engines.response_generator import generate_response
from engines.blueprint_engine import build_blueprint

from core.validator import validate
from core.exporter import save_sample
from core.id_generator import generate_id
from engines.scenario_forge import create_message

template = random_template()

sample = {
    **template,
    "input": "I feel like nobody understands me.",
    "response": "Feeling misunderstood can be painful. Your feelings deserve to be heard, and it's okay to seek someone who listens with care."
}


scenario = generate_scenario()
blueprint = build_blueprint()

sample = {
    "id": generate_id(),

    **template,

    **scenario,
    "input": create_message(),

    **blueprint,

    "response": generate_response(scenario["emotion"])
}
if validate(sample):
    save_sample(sample)
    print("Dataset sample saved.")
else:
    print("Invalid sample.")