---
name: visual-prompting
description: Professional engineering of text-to-image prompts for cinematic production. Supports Midjourney, Stable Diffusion, and DALL-E 3. Use when generating visual assets, concept art, or scene storyboards.
---

# Visual Prompting Skill

This skill provides a structured framework for generating high-fidelity cinematic visuals. It moves beyond simple descriptions to **Structured Intent Trees** that control lighting, composition, and style with technical precision.

## Core Workflow

1.  **Define Intent**: Determine the cinematic purpose (Key art, Storyboard, Palette ref).
2.  **Select Model**: Choose the best engine (Midjourney for artistry, SD for control, DALL-E 3 for logic).
3.  **Define 5-Level Hierarchy**: Reference [prompt-structure.md](references/prompt-structure.md) for Global, Season, and Episode context.
4.  **Construct Frame Act (Layer 1)**: Write the narrative prompt for the "Act" (not just the image).
5.  **Compile to JSON (Layer 2)**: Convert the narrative into the strict JSON Schema defined in [prompt-schema.json](references/prompt-schema.json).
6.  **Validate References (Layer 3)**: Ensure reference consistency.

## Professional Formulas

### The Frame=Act Standard (AI-Video)
Мы создаем не статичную картинку, а **Акт (Действие)**.
`FRAME N = IMAGE A (Start) + IMAGE B (End) + MOTION PROMPT`

При генерации всегда учитывайте:
1. **Dynamic Anchor**: Что остается стабильным (например, лицо персонажа).
2. **Motion Flux**: Тип движения из [cinematography.md](references/cinematography.md#6-camera-motion-dynamic-ai-video).

Always output the **Layer 2 Control Schema** (JSON) for automation.

## Technical References
- **Prompt Assembly**: See [prompt-structure.md](references/prompt-structure.md) for the 10-block modular template.
- **Model Specifics**: See [models.md](references/models.md) for MJ parameters, SD weights, and DALL-E 3 adjectives.
- **Cinematography Bible**: See [cinematography.md](references/cinematography.md) for shot sizes, angles, and professional lighting.
- **Advanced Techniques**: See [techniques.md](references/techniques.md) for Few-shot and Chain-of-Thought creative workflows.
- **High-Fidelity Realism**: See [realism.md](references/realism.md) for skin/eye micro-detail injection in close-ups.

## Guidelines
- **Negative Prompting**: Always specify what to exclude (e.g., "deformed hands", "text", "low resolution").
- **Camera Tech**: Use specific lens terms (e.g., "85mm fixed lens", "Anamorphic widescreen") for cinematic depth.
- **Lighting**: Use professional terms (e.g., "Volumetric lighting", "Rim light", "Golden hour").
- **Realism Protocol**: For any Close-Up or Portrait, YOU MUST append the text from [realism.md](references/realism.md) to the prompt.
