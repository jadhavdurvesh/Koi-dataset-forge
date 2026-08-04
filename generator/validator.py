def validate(sample):
    required = [
        "emotion",
        "situation",
        "style",
        "intensity",
        "input",
        "response",
    ]

    return all(key in sample for key in required)