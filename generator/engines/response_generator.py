import random

RESPONSES = {
    "loneliness": [
        "Feeling alone can be incredibly difficult. Your feelings matter, and meaningful connections often take time to grow.",
        "It's painful to feel left out. Even if it doesn't feel that way now, this moment doesn't define your future relationships.",
        "Wanting to be understood is something many people experience. You deserve kindness, including from yourself."
    ],

    "joy": [
        "That's wonderful to hear. Moments like these are worth appreciating and remembering.",
        "Happiness has a way of spreading. I hope you take a moment to enjoy what you've achieved.",
        "It's great that something made today brighter for you."
    ],

    "anxiety": [
        "Feeling anxious doesn't mean you're weak. It often means something is important to you.",
        "Try taking one step at a time. You don't have to solve everything all at once.",
        "It's okay to feel uncertain. Many challenges become easier once they're broken into smaller pieces."
    ],

    "hope": [
        "Holding onto hope can make difficult times feel a little more manageable.",
        "Every small step forward counts, even if progress feels slow.",
        "Sometimes hope begins with believing tomorrow can be different from today."
    ]
}


def generate_response(emotion):
    if emotion in RESPONSES:
        return random.choice(RESPONSES[emotion])

    return "Thank you for sharing how you're feeling."