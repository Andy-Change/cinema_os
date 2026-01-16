# OS Cinema: Global Agent Guidelines (SOP)

This document serves as the primary operational protocol for all agents within the Cinema OS environment. Adherence to these guidelines ensures system integrity and narrative consistency.

## 1. Worktree & Branching Protocol
To prevent context pollution and file lock conflicts, **direct edits to the root directory are prohibited during production cycles.**

- **Initialization**: Before starting any task, use the `git-ops` skill to create a fresh worktree.
  - `python lib/git_manager.py create --agent <your-name> --task <task-slug>`
- **Isolation**: All work must be performed strictly within the path returned by the command.
- **Completion**: Once the task is approved, use the merge protocol to integrate changes and remove the worktree.
  - `python lib/git_manager.py merge --task <task-slug>`

## 2. Post-Production Report Format (`walkthrough.md`)
Every major task completion must be documented in a `walkthrough.md` file within the task's output directory.

**Structure:**
- **Summary**: 1-2 sentences on what was achieved.
- **Changes**: Bulleted list of created/modified files (Narrative, Scripts, Assets).
- **Verification**: Evidence of quality (e.g., "Screenplay format verified against templates.md").
- **Agent Hand-off**: Who should review this next? (e.g., "Visual Ctrl for aesthetic pass").

## 3. Pre-Completion Checklist
Before marking a task as "Ready for Review", you MUST verify:

- [ ] **Formatting Check**: Use the `scene-drafting` skill for screenplay standards.
- [ ] **Integration Check**: Verify that `brand-integration` rules were followed (if applicable).
- [ ] **Season Alignment**: Confirm that the scene doesn't contradict `season_dna.yaml`.
- [ ] **Clean Git State**: Ensure all new files are added to the worktree staging.
- [ ] **UTF-8 Integrity**: Confirm all text files use UTF-8 encoding without BOM.

## 4. Language Protocol (RU/EN)
**Russian (RU) is the primary language for all user-facing interactions, narrative drafts, and discovery interviews.**

- **User Communication**: Always respond in Russian unless explicitly asked otherwise.
- **Narrative Content**: Screenplays, themes, and subtext must be drafted in Russian.
- **Prompt Engineering**: Technical prompts for AI models (Layer 2 Control, MJ/SD prompts) stay in English.

## 5. Season Management
- **Single Season Lock**: To maintain focus, only one active season is allowed per workspace (`os_cinema`).
- **Initialization**: `/film-init` will fail if a season already exists in `output/seasons`.

---
*Note: This is a living document. Updates must be cleared by the Chief Orchestrator.*
