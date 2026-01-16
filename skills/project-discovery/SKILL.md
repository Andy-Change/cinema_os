---
name: project-discovery
description: Systematic data gathering for new season initialization. Use to define narrative, commercial, and technical DNA before production starts.
---

# Project Discovery Skill

This skill acts as the bridge between initialization and production. It ensures all agents work from a unified "Source of Truth" (Discovery Report).

## Core Workflow

1.  **Context Audit**:
    - Scan available files, links, and previous session context.
    - Extract entities, themes, and commercial requirements.

2.  **The Interview (Interactive Dialogue)**:
    - **Step-by-Step Questioning**: Don't dump all questions at once. Ask one, wait for the answer.
    - **Proactive Suggestions**: If the user is unsure ("не знаю", "предложи сам"), provide 3 distinct cinematic directions (e.g., Cyberpunk Noir, Solar-punk, Clinical Hard Sci-Fi).
    - **File/URL Extraction**: Automatically digest any uploaded data and use it to populate the report.

3.  **Synthesis**:
    - Compile findings into `blueprints/discovery_report.md`.
    - Generate a visual `meaning_map.md` (Theme -> Visual Arc).

## Principles
- **Accuracy Over Speed**: One vague parameter in Discovery ruins 100 frames of production.
- **Narrative First**: Commercial integrations must fit the narrative axis defined in Step 1.
