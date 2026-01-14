---
name: git-merge-worktree
description: Применяет изменения из ворк-три агента в основную ветку.
input_schema:
  type: object
  properties:
    worktree_path:
      type: string
      description: Путь к директории ворк-три
    branch_name:
      type: string
      description: Имя ветки (если известно)
  required: ["worktree_path"]
---

Этот навык используется, когда агент завершил задачу и пользователь одобрил результат.
Он выполняет слияние ветки и удаляет временное ворк-три.

Для выполнения:
1. Убедитесь, что мы в корне проекта.
2. Выполните `python lib/git_manager.py cleanup --path {worktree_path}` (упрощенная логика для прототипа, в реальности нужен merge).
