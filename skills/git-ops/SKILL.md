---
name: git-ops
description: Comprehensive management of parallel production branches using Git worktrees. Use for creating isolated workspaces for agents, merging completed scenes, and maintaining pipeline integrity.
---

# Git Operations for Cinematic Production

This skill manages the parallel narrative production pipeline. Every creative task (scene drafting, research, brand integration) should happen in an isolated **Worktree** to ensure context safety and prevent file conflicts.

## Workflows

### 1. Creating an Isolated Workspace
When starting a new production task (e.g., writing a scene), initialize a new worktree.

**Pattern:**
`python lib/git_manager.py create --agent <agent_name> --task <task_slug>`

- `agent_name`: Directory-safe name (e.g., `dept-a-writer`)
- `task_slug`: Descriptive identifier (e.g., `s01-e01-intro`)

### 2. Merging & Synchronizing
Once a task is complete and verified, merge the worktree back into the main production branch and cleanup.

**Pattern:**
`python lib/git_manager.py merge --task <task_slug>`

## Core Principles
- **Conciseness**: Only use this skill when starting or finishing a multi-file creative cycle.
- **Isolation**: Never edit files in the root directory directly during a production season; always use a worktree.
- **Cleanup**: Always merge and remove the worktree once the agent's work is finished.

## Troubleshooting
If a worktree creation fails, check if a branch with the same name already exists: `git branch`.
