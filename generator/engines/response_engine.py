import random

# Core empathetic response per primary emotion. Previously only 4 emotions
# were covered (joy/sadness/anxiety/fear-ish); this now covers every emotion
# in knowledge/psychology/emotions.json.
CORE_RESPONSES = {
    "joy": [
        "That's wonderful to hear.",
        "Moments like these are worth appreciating and remembering.",
        "It's great that something made today brighter for you.",
    ],
    "sadness": [
        "I'm sorry you're carrying this right now.",
        "It makes sense to feel this way given what you're going through.",
        "What you're feeling is valid, and it's okay to sit with it for a while.",
    ],
    "loneliness": [
        "Feeling alone can be incredibly difficult.",
        "It's painful to feel left out, even if that's not how others see you.",
        "Wanting to be understood is something a lot of people go through.",
    ],
    "love": [
        "It sounds like this connection means a lot to you.",
        "That kind of care is worth holding onto.",
        "It's clear you feel deeply about this.",
    ],
    "hope": [
        "Holding onto hope can make difficult times feel more manageable.",
        "Every small step forward counts, even if progress feels slow.",
        "Sometimes hope starts with believing tomorrow can be different from today.",
    ],
    "anxiety": [
        "Feeling anxious doesn't mean something is wrong with you — it often means something matters to you.",
        "You don't have to solve everything at once; one step at a time is enough.",
        "It's okay to feel uncertain. Big worries often get smaller once broken into pieces.",
    ],
    "grief": [
        "I'm so sorry for what you've lost.",
        "Grief doesn't move on a schedule, and there's no wrong way to feel it.",
        "Whatever you're feeling right now is a natural part of losing someone or something important.",
    ],
    "fear": [
        "It's okay to feel scared — that reaction makes sense.",
        "Fear often shows up around things that really matter to us.",
        "You don't have to face this all at once.",
    ],
}

# A closing line shaped by what the person actually needs, not just their
# emotion — this is what makes the Emotion Blueprint (need/intent) actually
# change the output, instead of the blueprint fields being generated but
# never used.
NEED_CLOSERS = {
    "connection": "You're not as alone in this as it might feel.",
    "understanding": "I hear you, and what you're saying makes sense.",
    "encouragement": "You're capable of getting through this, even if it doesn't feel that way right now.",
    "validation": "Your feelings are valid, exactly as they are.",
    "comfort": "Be gentle with yourself while you work through this.",
    "guidance": "Taking it one small step at a time can help.",
    "hope": "Things can look different than they do right now.",
    "forgiveness": "It's okay to forgive yourself, or others, in your own time.",
    "acceptance": "You don't have to have it all figured out to be okay.",
    "belonging": "You deserve people around you who truly see you.",
}


def generate_response(emotion, need=None, intent=None):
    core = random.choice(
        CORE_RESPONSES.get(emotion, ["Thank you for sharing how you're feeling."])
    )
    closer = NEED_CLOSERS.get(need, "")
    return f"{core} {closer}".strip()


if __name__ == "__main__":
    print(generate_response("loneliness", need="belonging"))
