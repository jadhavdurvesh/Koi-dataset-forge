from builders.blueprint_engine import EMOTION_BLUEPRINT

REQUIRED_FIELDS = [
    "id", "emotion", "situation", "intensity",
    "input", "response", "need", "intent",
    "communication_style", "response_style",
]


def validate(sample):
    """
    Validate a generated sample. Checks structural completeness AND
    emotional consistency — a sample where the 'need' doesn't belong to the
    emotion's Emotion Blueprint is rejected, since that's exactly the kind
    of "emotion mismatch" Milestone 5 (Validator v2) is meant to catch.
    """
    for field in REQUIRED_FIELDS:
        if field not in sample:
            return False, f"Missing field: {field}"
        if not str(sample[field]).strip():
            return False, f"Empty field: {field}"

    if len(sample["input"]) < 10:
        return False, "Input is too short."

    if len(sample["response"]) < 15:
        return False, "Response is too short."

    if not (1 <= sample["intensity"] <= 5):
        return False, "Intensity out of range (1-5)."

    allowed = EMOTION_BLUEPRINT.get(sample["emotion"])
    if allowed and sample["need"] not in allowed.get("needs", []):
        return False, (
            f"Emotion mismatch: '{sample['need']}' is not a plausible "
            f"need for '{sample['emotion']}'."
        )

    return True, "Valid"
