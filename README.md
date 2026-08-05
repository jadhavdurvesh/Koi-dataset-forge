# 🌸 KOI Dataset Forge

> **Every heart has a story worth understanding.**

**KOI Dataset Forge** is an open-source dataset generation framework created for **KOI**, an Emotional Intelligence Language Model developed by **DMJ Labs**.

Its mission is to build **KOI Hearts**—a carefully curated emotional conversation dataset that helps AI better understand human emotions, communication, empathy, and relationships.

Unlike traditional datasets that prioritize factual knowledge, KOI Hearts focuses on the emotional meaning behind conversations.

---

# ❤️ The Vision

Artificial Intelligence has become increasingly capable of solving technical problems, writing code, and answering factual questions.

Understanding people, however, requires something different.

KOI is built around a simple belief:

> **Before answering the question, understand the person asking it.**

Every conversation carries emotions, intentions, experiences, and context. KOI Dataset Forge exists to help AI recognize and respond to those human elements with care and consistency.

---

# 🌸 What is KOI?

**KOI** is an **Emotional Intelligence Language Model (EILM)** designed to understand feelings, communication styles, and emotional context.

Rather than competing with technical models, KOI specializes in conversations involving:

- ❤️ Emotional understanding
- 💬 Compassionate dialogue
- ✍️ Emotional writing
- 🤝 Relationship communication
- 🌱 Personal reflection
- 📖 Storytelling
- 🌍 Human-centered conversations

---

# ❤️ What is KOI Hearts?

**KOI Hearts** is the official emotional conversation dataset powering KOI.

Every dataset sample represents a realistic interaction between a person and an emotionally aware AI.

Each sample includes structured emotional metadata, allowing KOI to learn not just *what* people say, but *why* they say it.

Example:

```json
{
  "id": "KH-V1-000001",
  "emotion": "loneliness",
  "secondary_emotion": "hope",
  "situation": "friendship",
  "intensity": 4,
  "communication_style": "reserved",
  "input": "Nobody messages me unless I text first.",
  "response": "Feeling left out can be painful. Your feelings matter, and meaningful connections often take time to grow."
}
```

---

# 🔨 What is KOI Dataset Forge?

KOI Dataset Forge is the framework responsible for creating KOI Hearts.

It provides tools for:

- 🎭 Emotional scenario generation
- 💬 Response generation
- ✅ Dataset validation
- 🔍 Duplicate detection
- 📚 Dataset organization
- 📦 Exporting training-ready datasets
- 📊 Quality evaluation
- ❤️ Emotion metadata generation

The goal is to create one of the most comprehensive open emotional conversation datasets available.

---

# 🏗️ Project Architecture

KOI Dataset Forge is built using a modular pipeline architecture. Each component has a single responsibility, making the project easier to maintain, test, and extend.

```text
koi-dataset-forge/
│
├── configs/                 # Configuration files
│   ├── emotions/
│   ├── intents/
│   ├── needs/
│   ├── scenario_parts/
│   └── styles/
│
├── datasets/                # Generated datasets
│   ├── raw/
│   ├── reviewed/
│   ├── final/
│   ├── archive/
│   └── manifests/
│
├── docs/                    # Documentation
│   ├── architecture/
│   ├── dataset/
│   └── development/
│
├── generator/
│   ├── pipeline/            # Main generation workflow
│   ├── builders/            # Dataset builders
│   ├── engines/             # AI generation engines
│   ├── managers/            # Dataset & ID management
│   ├── core/                # Core utilities
│   └── utils/               # Shared helper functions
│
├── prompts/                 # Prompt templates
├── tests/                   # Unit tests
│
├── README.md
├── LICENSE
└── requirements.txt
```

---

## 📦 Module Overview

### Pipeline

The pipeline coordinates the complete dataset generation process.

Responsibilities:

- Start dataset generation
- Execute each engine in order
- Validate generated samples
- Export finished datasets

---

### Builders

Builders create structured metadata used throughout the generation process.

Examples:

- Emotional Blueprint Builder
- Template Builder
- Metadata Builder

---

### Engines

Engines generate the content of the dataset.

Current and planned engines include:

- Life Engine
- Scenario Engine
- Response Engine
- Emotion Engine
- Personality Engine

---

### Managers

Managers keep track of the project's internal state.

Examples:

- Dataset IDs
- Statistics
- Dataset versions
- Session management

---

### Core

Core contains reusable functionality shared across the project.

Examples:

- Exporter
- Validator
- Duplicate detection

---

### Utils

Utility functions that are shared by multiple modules.

Examples:

- JSON helpers
- File utilities
- Logging
- Formatting


# 🚀 Roadmap

## Phase 1 — Foundation
- [x] Project structure
- [x] Dataset generation pipeline
- [x] Emotion configuration
- [x] Scenario generation
- [x] Response generation

## Phase 2 — Emotional Intelligence
- [ ] Emotion Blueprint Engine
- [ ] Intent detection
- [ ] Emotional needs classification
- [ ] Conversation style generation
- [ ] Personality profiles

## Phase 3 — Dataset Quality
- [ ] Duplicate detection
- [ ] Diversity scoring
- [ ] Automatic validation
- [ ] Session management
- [ ] Metadata verification

## Phase 4 — KOI Hearts
- [ ] 10,000 reviewed conversations
- [ ] Multi-language support
- [ ] Community contributions
- [ ] KOI Hearts v1 Release

---

# 🌸 KOI Philosophy

> **Every heart has a story worth understanding.**

KOI believes that emotions do not exist in isolation.

Behind every emotion is an experience.

Behind every experience is a person.

Rather than generating isolated conversations, KOI Hearts generates emotionally grounded human stories.

Each dataset sample is built from a complete emotional context:

```
Person
    ↓
Life Profile
    ↓
Life Experience
    ↓
Current Situation
    ↓
Emotion
    ↓
Need
    ↓
Intent
    ↓
Communication Style
    ↓
Compassionate Response
```

This philosophy allows KOI to learn not only what people say, but why they say it and how thoughtful responses can be shaped by context.

---

# 🤝 Contributing

Contributions are welcome.

Whether you're improving conversation quality, expanding emotional coverage, fixing bugs, or proposing new ideas, every contribution helps make KOI Hearts more thoughtful and diverse.

---

# 📄 License

This project is licensed under The DMJ Community License (DCL)

---

# 🌌 DMJ Labs Ecosystem

KOI is part of the DMJ Labs family of AI models.

| Model | Purpose |
|--------|---------|
| 🌙 Saudade | Memory & Knowledge Language Model |
| 🏔️ Hiraeth | Technical Reasoning Language Model |
| 🌸 KOI | Emotional Intelligence Language Model |

---

# ❤️ Closing Words

Technology continues to evolve.

Knowledge can be memorized.

Logic can be learned.

But every conversation begins with a person.

**Every heart has a story worth understanding.**