# Prompt Hierarchy & Frame=Act Architecture

This standard defines the 5-Level Prompt Hierarchy and the "Frame as Act" production unit.

## The Hierarchy (Rigid Inheritance)
1.  **TYPE 01 — GLOBAL STYLE (Invariant)**: Fixed DNA (Villeneuve/Wachowski, grounding).
2.  **TYPE 02 — SEASON PROMPT (World Context)**: Theme, emotional axis, world state.
3.  **TYPE 03 — EPISODE PROMPT (Narrative Core)**: Central conflict, emotional path.
4.  **TYPE 04 — FRAME PROMPT (Production Unit)**: The atomic unit of automation (State A + State B).
5.  **TYPE 05 — TRANSITION PROMPT**: Deep description of A -> B motion.

## The "Frame = Act" Standard
We do not generate static images. We generate **Acts**.

```text
FRAME N (ACT)
├── IMAGE A (Start State) — 4K Visual Anchor
├── IMAGE B (End State) — Result of Micro-action
└── ANIMATION (A → B) — 8-10s Semantic Motion
```

### Transition Logic
The bridge between frames is an Act itself:
`TRANSITION ACT = IMAGE B (Frame N) → IMAGE A (Frame N+1)`

## Layered Production Model
1.  **LAYER 1 (Narrative)**: Text, Human-first, Meaning.
2.  **LAYER 2 (Control)**: JSON Schema, Machine-first, Consistency.
3.  **LAYER 3 (References)**: Visual Anchors, Stability.

## JSON Control Schema (Layer 2)
The output of Visual Ctrl must be a valid JSON object:
```json
{
  "frame_id": "EP01_ACT01_FRAME01",
  "type": "frame_act",
  "narrative": {
    "intent": "...",
    "subtext": "..."
  },
  "state_a": {
    "camera": "...",
    "subject_pose": "...",
    "lighting": "..."
  },
  "state_b": {
    "change": "...",
    "new_focus": "..."
  },
  "technical": {
    "aspect_ratio": "16:9",
    "resolution": "4K"
  }
}
```
