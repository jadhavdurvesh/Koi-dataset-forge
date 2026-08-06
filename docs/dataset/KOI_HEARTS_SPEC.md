# ❤️ KOI Hearts Specification

> **Every heart has a story worth understanding.**

Version: **1.0 Draft**

---

# Purpose

KOI Hearts is the official emotional conversation dataset developed for the **KOI Emotional Intelligence Language Model**.

Its objective is to teach AI how to understand the emotional context behind human conversations rather than simply generating text.

Every sample should represent a believable person experiencing a believable moment in life.

---

# Design Principles

Every dataset sample must satisfy four principles:

- Human First
- Emotionally Consistent
- Context Aware
- Compassionate

KOI Hearts does not generate random prompts.

It generates emotionally grounded human stories.

---

# Dataset Pipeline

```
Person
    ↓
Life Profile
    ↓
Current Situation
    ↓
Emotion
    ↓
Need
    ↓
Intent
    ↓
Conversation
    ↓
Response
```

---

# Dataset Schema

Every sample follows the same structure.

```json
{
  "id": "KH-V1-000001",

  "person": {
    "age": 18,
    "age_group": "teen",
    "education": "Diploma Student",
    "occupation": "Student",
    "personality": "Empathetic",
    "living_situation": "Lives with parents",
    "support_system": "Moderate"
  },

  "life_event": "Preparing for final exams",

  "emotion": "anxiety",

  "secondary_emotion": "hope",

  "need": "Reassurance",

  "intent": "Seeking Support",

  "communication_style": "Hesitant",

  "response_style": "Gentle",

  "intensity": 4,

  "input": "...",

  "response": "..."
}
```

---

# Required Fields

Every dataset sample must include:

| Field | Required |
|--------|----------|
| id | ✅ |
| person | ✅ |
| life_event | ✅ |
| emotion | ✅ |
| need | ✅ |
| intent | ✅ |
| communication_style | ✅ |
| response_style | ✅ |
| intensity | ✅ |
| input | ✅ |
| response | ✅ |

---

# Emotion Categories

Current supported emotions include:

- Joy
- Gratitude
- Hope
- Excitement
- Love

- Anxiety
- Fear
- Stress
- Confusion

- Loneliness
- Sadness
- Grief
- Disappointment

- Anger
- Frustration
- Guilt
- Shame

Future versions will expand this list.

---

# Intensity Scale

| Level | Meaning |
|--------|---------|
| 1 | Very Mild |
| 2 | Mild |
| 3 | Moderate |
| 4 | Strong |
| 5 | Extremely Intense |

---

# Response Principles

Every response should be:

- Compassionate
- Respectful
- Context Aware
- Emotionally Appropriate
- Non-Judgmental
- Natural
- Honest

Responses should avoid:

- Shaming
- Blaming
- Mocking
- Dismissing feelings
- Unrealistic promises
- Manipulation

---

# Quality Rules

A dataset sample should be rejected if:

- Required fields are missing.
- Context is inconsistent.
- Emotion does not match the situation.
- Response ignores the user's emotion.
- Duplicate conversation.
- Empty response.
- Invalid metadata.

---

# Dataset Versioning

Format:

```
KH-V<major>-<sample_number>
```

Example:

```
KH-V1-000001
KH-V1-000002
KH-V1-000003
```

Major dataset revisions increase the version.

Example:

```
KH-V2-000001
```

---

# Naming Convention

Dataset

```
KOI Hearts
```

Generator

```
KOI Dataset Forge
```

Model

```
KOI
```

---

# Long-Term Vision

The goal of KOI Hearts is to become one of the world's highest-quality open emotional conversation datasets.

Rather than collecting isolated prompts, KOI Hearts seeks to capture realistic human experiences with consistent emotional context.

---

# Motto

> **Every heart has a story worth understanding.**