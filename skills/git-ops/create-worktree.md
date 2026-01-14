---
name: git-create-worktree
description: Создает изолированное рабочее пространство (Git Worktree) для выполнения задачи агентом.
input_schema:
  type: object
  properties:
    agent_name:
      type: string
      description: Имя агента (например, dept-a-writer)
    task_slug:
      type: string
      description: Краткое название задачи (например, ep01-scene03)
  required: ["agent_name", "task_slug"]
---

Этот навык используется, когда агенту нужно начать новую задачу, не мешая основной ветке.
Он создает "песочницу", где агент может безопасно создавать файлы.

Для выполнения:
Вызови `python lib/git_manager.py create --agent {agent_name} --task {task_slug}`
Верни пользователю путь к созданной директории.
