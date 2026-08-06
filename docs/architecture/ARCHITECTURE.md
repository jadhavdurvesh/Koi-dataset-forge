# 🌸 KOI Dataset Forge Architecture

> **Every heart has a story worth understanding.**

This document describes the internal architecture of KOI Dataset Forge and explains how every generated conversation is created.

---

# Vision

KOI Dataset Forge is not a random prompt generator.

It is a human-centered dataset generation framework designed to create emotionally rich training data for the KOI Emotional Intelligence Language Model.

Every dataset sample begins with a person, not an emotion.

---

# Core Philosophy

Instead of asking:

> "What should the AI say?"

KOI asks:

> "Who is the person behind these words?"

Every conversation is generated from a complete emotional context.

---

# Generation Pipeline

```
Person
    │
    ▼
Life Engine
    │
    ▼
Scenario Engine
    │
    ▼
Blueprint Engine
    │
    ▼
Response Engine
    │
    ▼
Validator
    │
    ▼
Exporter
    │
    ▼
KOI Hearts Dataset
```

---

# Engine Responsibilities

## 🧬 Life Engine

Creates a believable person.

Example:

- Age
- Age Group
- Education
- Occupation
- Living Situation
- Personality
- Relationship Status
- Support System
- Current Life Event

Output:

```json
{
  "age": 18,
  "education": "Diploma Student",
  "occupation": "Student",
  "personality": "Empathetic"
}
```

---

## 🎭 Scenario Engine

Uses the generated life profile to create a realistic situation.

Example:

```
An 18-year-old diploma student is worried about final exams.
```

---

## ❤️ Blueprint Engine

Builds the emotional metadata.

Generates:

- Emotion
- Secondary Emotion
- Trigger
- Need
- Intent
- Communication Style
- Response Style
- Emotional Intensity

---

## 💬 Response Engine

Creates a compassionate response that matches the person's emotional context.

The response should be:

- Emotionally aware
- Context sensitive
- Non-judgmental
- Supportive
- Natural

---

## ✅ Validator

Checks dataset quality.

Responsibilities include:

- Required fields
- Empty values
- Invalid metadata
- Duplicate detection
- Length checks
- Schema validation

---

## 📦 Exporter

Stores validated conversations inside KOI Hearts.

Dataset versions are archived automatically.

---

# Dataset Schema

Every conversation follows the same structure.

```json
{
  "id": "KH-V1-000001",

  "person": {
    "age": 18,
    "education": "Diploma Student",
    "occupation": "Student",
    "personality": "Empathetic"
  },

  "life_event": "Preparing for final exams",

  "emotion": "anxiety",

  "need": "Reassurance",

  "intent": "Seeking Support",

  "communication_style": "Hesitant",

  "input": "...",

  "response": "..."
}
```

---

# Project Structure

```
generator/
│
├── pipeline/
│
├── engines/
│   ├── life_engine.py
│   ├── scenario_engine.py
│   ├── blueprint_engine.py
│   ├── response_engine.py
│
├── managers/
│   ├── id_generator.py
│   ├── stats.py
│
├── core/
│   ├── validator.py
│   ├── exporter.py
│
└── utils/
```

---

# Future Engines

Planned additions include:

- Emotion Engine
- Personality Engine
- Relationship Engine
- Memory Engine
- Dialogue Engine
- Conversation Flow Engine
- Quality Scoring Engine

---

# Long-Term Goal

Generate millions of emotionally diverse, high-quality conversations while maintaining realistic human context.

Every conversation should feel as though it came from a believable person living through a believable moment.

---

# KOI Philosophy

> Every heart has a story worth understanding.

KOI does not begin with an emotion.

It begins with a person.

Understanding the person leads to understanding the emotion.

Understanding the emotion leads to understanding the response.