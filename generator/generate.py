from templates import random_template
from validator import validate
from exporter import save_sample
from id_generator import generate_id

template = random_template()

sample = {
    **template,
    "input": "I feel like nobody understands me.",
    "response": "Feeling misunderstood can be painful. Your feelings deserve to be heard, and it's okay to seek someone who listens with care."
}
from scenario_generator import generate_scenario

scenario = generate_scenario()

sample = {

    "id": generate_id(),
    **template,
    **scenario,
    "response": "Placeholder response"
}

if validate(sample):
    save_sample(sample)
    print("Dataset sample saved.")
else:
    print("Invalid sample.")