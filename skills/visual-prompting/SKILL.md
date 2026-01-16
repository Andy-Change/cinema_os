---
name: visual-prompting
description: Professional engineering of text-to-image prompts for cinematic production. Supports Midjourney, Stable Diffusion, and DALL-E 3. Use when generating visual assets, concept art, or scene storyboards.
---

# Visual Prompting Skill

This skill provides a structured framework for generating high-fidelity cinematic visuals. It moves beyond simple descriptions to **Structured Intent Trees** that control lighting, composition, and style with technical precision.

## Core Workflow

1.  **Define Intent**: Determine the cinematic purpose (Key art, Storyboard, Palette ref).
2.  **Select Model**: Choose the best engine (Midjourney for artistry, SD for control, DALL-E 3 for logic).
3. **Construct Prompt**: Use the **Subject-Medium-Style-Lighting-Composition** formula, citing specific technicals from [cinematography.md](references/cinematography.md).
4.  **Iterate & Refine**: Use negative prompts and weighting to tune output.

## Professional Formulas

### The Master Formula
`[Subject Description] -- [Action/Environment] -- [Medium & Camera Tech] -- [Lighting & Atmos] -- [Color Palette] -- [Artist/Style Influence]`

## Technical References
- **Model Specifics**: See [models.md](references/models.md) for MJ parameters, SD weights, and DALL-E 3 adjectives.
- **Cinematography Bible**: See [cinematography.md](references/cinematography.md) for shot sizes, angles, and professional lighting.
- **Advanced Techniques**: See [techniques.md](references/techniques.md) for Few-shot and Chain-of-Thought creative workflows.

## Guidelines
- **Negative Prompting**: Always specify what to exclude (e.g., "deformed hands", "text", "low resolution").
- **Camera Tech**: Use specific lens terms (e.g., "85mm fixed lens", "Anamorphic widescreen") for cinematic depth.
- **Lighting**: Use professional terms (e.g., "Volumetric lighting", "Rim light", "Golden hour").
