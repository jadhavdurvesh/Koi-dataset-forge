def validate(sample):
    """
    Validate a KOI Hearts sample.
    Returns (True, "Valid") or (False, "Reason")
    """

    required_fields = [
        "id",
        "emotion",
        "situation",
        "intensity",
        "input",
        "response",
    ]

    # Check required fields
    for field in required_fields:
        if field not in sample:
            return False, f"Missing field: {field}"

    # Check empty values
    for field in required_fields:
        if not str(sample[field]).strip():
            return False, f"Empty field: {field}"

    # Input length
    if len(sample["input"]) < 10:
        return False, "Input is too short."

    # Response length
    if len(sample["response"]) < 20:
        return False, "Response is too short."

    return True, "Valid"