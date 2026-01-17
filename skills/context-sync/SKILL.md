---
name: context-sync
description: Навык для чтения и записи в единый файл истины (Project Bible).
version: 1.0.0
---

# Context Sync Skill 🧠

Этот навык позволяет агентам сохранять контекст между сессиями и обмениваться данными через единый JSON-файл.

## 1. Концепция
`project_bible.json` — это "мозг" проекта. 
- **Meaning Owner** пишет в `core_identity` и `script_bible`.
- **Visual Controller** читает `core_identity` и пишет в `visual_language`.
- **Dept-D** читает всё и пишет в `distribution_strategy`.

## 2. Использование (Python)

```python
import json
import os

BIBLE_PATH = "output/seasons/<active_season>/blueprints/project_bible.json"

def load_bible():
    if not os.path.exists(BIBLE_PATH):
        return {}
    with open(BIBLE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def update_section(section, data):
    bible = load_bible()
    bible[section] = data
    with open(BIBLE_PATH, 'w', encoding='utf-8') as f:
        json.dump(bible, f, indent=2, ensure_ascii=False)
```

## 3. Протокол для Агентов
1.  **ПЕРЕД** генерацией ответа: Прочитай `project_bible.json`, чтобы понять контекст (жанр, стиль, герой).
2.  **ПОСЛЕ** утверждения пользователем: Запиши новые факты в соответствующую секцию Библии.
