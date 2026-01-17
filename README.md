# OS Cinema: Director's Operating System

[![System Status](https://img.shields.io/badge/System-Online-success)](https://github.com/Andy-Change/cinema_os)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue)](https://github.com/Andy-Change/cinema_os)
[![Architecture](https://img.shields.io/badge/Architecture-Claude%20Plugin-indigo)](https://anthropic.com)

**OS Cinema** is a headless, agentic operating system designed to orchestrate the end-to-end production of episodic cinematic content. It fuses the cinematic philosophies of **Denis Villeneuve** and **Christopher Nolan** into a powerful AI-native production engine.

---

## 🏗 System Architecture

The system mimics a professional film studio structure, divided into specialized departments overseen by a central orchestration layer.

### Departments

| Code | Department | Responsibility | Key Agents |
|------|------------|----------------|------------|
| **[A]** | **Aesthetics & Meaning** | Creative Direction, Scriptwriting | `Meaning Owner`, `Visual Ctrl`, `Writer` |
| **[D]** | **Distribution** | Market Fit, Transmedia, Branding | `Brand Integrator`, `Social Manager` |
| **[I]** | **Intelligence** | Research, Data Analysis | `Analyst`, `Researcher` |
| **[O]** | **Operations** | System Integrity, Pipeline Management | `Orchestrator`, `First AD` |

---

## 🌟 Key Features (v1.0)

### 1. Hybrid Cinematic Engine
*   **Villeneuve Codex**: Atmosphere, scale, minimal dialogue.
*   **Nolan Protocol**: Temporal architecture, IMAX optimization, practical effects priority.
*   **Dune Dynamics**: Witness camera, motivated motion.

### 2. Unified Context Brain 🧠
*   The system maintains a **`project_bible.json`** — a persistent memory file that tracks theme, visual style, and script decisions across all agent interactions.

### 3. One-Click Production Book 📚
*   Automated generation of a professional production report (`/film-export`) summarizing the entire season's creative and strategic decisions.

### 4. Self-Healing Diagnostics 🏥
*   Built-in **Doctor** (`/film-doctor`) to verify system integrity and fix configuration issues.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   Git

### Quick Installation
We provide a unified installer for Windows environments.

```bash
setup.bat
```

This will:
1.  Verify your Python/Git environment.
2.  Create a strict virtual environment (`venv`).
3.  Install core dependencies.
4.  Perform a system integrity check.

---

## 🎬 CLI Commands

Once inside the environment (or using Claude Code), you have access to the following directives:

| Command | Description |
|---------|-------------|
| `/film-init` | Initialize a new Season context (scaffolding). |
| `/film-discovery` | Launch the interactive Discovery Interview with `Meaning Owner`. |
| `/film-export` | **[NEW]** Generate a PDF/MD Production Book from the Project Bible. |
| `/film-doctor` | **[NEW]** Run system diagnostics and health check. |
| `/film-status` | Display the agent roster and system health. |
| `/film-update` | Self-update the system core (Git Pull). |

---

## 📂 Project Structure

```text
os_cinema/
├── .agent/             # Claude Code workflow definitions
├── .claude-plugin/     # Plugin manifest
├── agents/             # Agent prompts & personas (Markdown)
├── lib/                # Python core logic (Orchestrator)
├── output/             # Generated Content (Seasons/Episodes)
├── skills/             # Specialized capabilities (Context, Visuals, etc.)
└── setup.bat           # Universal Installer
```

---

## 📄 License

Proprietary Software. Internal Use Only.
Copyright © 2026 OS Cinema Core.
