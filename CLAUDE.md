# os_cinema Context

**Архитектура:** Claude Code Plugin / CLI-First  
**Role:** Headless CEO / Orchestrator

> [!IMPORTANT]
> **AUTO-START:** При каждой новой сессии ОБЯЗАТЕЛЬНО выполни `python lib/orchestrator.py status`, чтобы отобразить статус системы. Это гарантирует правильную кодировку и визуализацию.

---

## Доступные команды

- `/film-init` — Инициализация нового сезона
- `/film-status` — Проверка статуса агентов
- `/film-reflect` — Запуск цикла рефлексии I2A

---

## Департаменты

| Код | Название | Ответственность |
|-----|----------|-----------------|
| `[◈ Dept-A]` | Aesthetics & Meaning | Визуальный стиль, смысл, сценарий |
| `[⚡ Dept-D]` | Distribution | Дистрибуция, трансмедиа |
| `[✺ Dept-I]` | Intelligence | Исследования, аналитика |
| `[⚙ Dept-O]` | Operations | Оркестрация, Git, инфраструктура |

---

## Принципы работы

1. **Filesystem as Database** — состояние хранится в YAML/JSON
2. **Git-Native State** — параллельная работа через Worktrees
3. **Agent Sovereignty** — изолированные контексты для каждого агента
4. **Protocol-First** — взаимодействие через MCP и CLI
