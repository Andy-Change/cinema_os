# OS Cinema: AI-Native Production Operating System

[![System Status](https://img.shields.io/badge/System-Online-success)](https://github.com/Andy-Change/cinema_os)
[![Version](https://img.shields.io/badge/Version-0.3.0-blue)](https://github.com/Andy-Change/cinema_os)
[![Architecture](https://img.shields.io/badge/Architecture-Claude%20Plugin-indigo)](https://anthropic.com)

**OS Cinema** is a headless, agentic operating system designed to orchestrate the end-to-end production of episodic cinematic content. Built as a native plugin for Claude Code, it leverages a sophisticated multi-agent architecture to handle everything from aesthetic direction to distribution strategy.

---

## 🏗 System Architecture

The system mimics a professional film studio structure, divided into specialized departments overseen by a central orchestration layer.

### Departments

| Code | Department | Responsibility | Key Agents |
|------|------------|----------------|------------|
| **[A]** | **Aesthetics & Meaning** | Creative Direction, Scriptwriting | `Meaning Owner`, `Visual Ctrl`, `Writer` |
| **[D]** | **Distribution** | Market Fit, Transmedia, Branding | `Brand Integrator`, `Social Manager` |
| **[I]** | **Intelligence** | Research, Data Analysis | `Analyst`, `Researcher` |
| **[O]** | **Operations** | System Integrity, Pipeline Management | `Orchestrator` |

---

## 🔧 Core Mechanics

### 1. Git-Native Production Flow
Every season and episode is treated as a software release branch. The system utilizes `git worktrees` to allow multiple agents to work on different narrative threads simultaneously without context pollution.

### 2. Protocol-First Interaction
OS Cinema is designed to be "headless" but observable. Interfacing is done through a native CLI wrapper (`orchestrator.py`) or widely integrated Slash Commands in Claude Code.

### 3. "Golden Template" State
This repository represents the **Golden Template** — a pristine, self-contained environment ready for cloning. It includes self-replication and update capabilities.

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
1.  Verify your Python environment.
2.  Create a strict virtual environment (`venv`).
3.  Install core dependencies (if available).
4.  Perform a system integrity check.

### Manual Update
To pull the latest logic updates from the core repository:

```bash
/film-update
```

---

## 🎬 CLI Commands

Once inside the environment (or using Claude Code), you have access to the following directives:

*   `/film-status` — Display the agent roster and system health.
*   `/film-init --season <ID>` — Initialize a new Season context (scaffolding).
*   `/film-reflect` — Trigger an "Idea-to-Action" (I2A) reflection cycle for agents.
*   `/film-update` — Self-update the system core.

---

## 📂 Project Structure

```text
os_cinema/
├── .agent/             # Claude Code workflow definitions
├── .claude-plugin/     # Plugin manifest
├── agents/             # Agent prompts & personas (Markdown)
├── commands/           # Batch wrappers for CLI
├── lib/                # Python core logic
├── output/             # Generated Content (Seasons/Episodes)
├── skills/             # Specialized capabilities (Git, etc.)
└── setup.bat           # Universal Installer
```

---

## 📄 License

Proprietary Software. Internal Use Only.
Copyright © 2026 OS Cinema Core.
