import argparse
import sys
import os
import json
from datetime import datetime

# Force UTF-8 encoding for standard output
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def print_banner():
    # Single-line banner - Gemini CLI Style
    # Simple and clean, works everywhere
    print()
    print("\033[38;5;63m▸ CINEMA OS\033[0m")
    print("\033[38;5;244m  Director's Operating System v0.3.0\033[0m")
    print()

def cmd_status(args):
    print_banner()
    
    # Detect Latest Season
    seasons_dir = os.path.join("output", "seasons")
    active_season = "None"
    if os.path.exists(seasons_dir):
        seasons = [d for d in os.listdir(seasons_dir) if os.path.isdir(os.path.join(seasons_dir, d))]
        if seasons:
            active_season = sorted(seasons)[-1]

    # System Status
    print("\033[38;5;63m●\033[0m System \033[32mOnline\033[0m")
    print(f"  Season: \033[36m{active_season}\033[0m")
    print()

    # Active Agents
    # ... (remaining agent scanning code)
    agents_root = "agents"
    found_agents = []
    dept_map = {
        "DEPT-A": ("[A]", "Aesthetics & Meaning", "\033[38;5;166m"),
        "DEPT-D": ("[D]", "Distribution", "\033[38;5;118m"),
        "DEPT-I": ("[I]", "Intelligence", "\033[38;5;039m"),
        "DEPT-O": ("[O]", "Operations", "\033[38;5;63m"),
    }
    
    for root, dirs, files in os.walk(agents_root):
        dept_key = os.path.basename(root).upper()
        if dept_key in dept_map:
            for file in files:
                if file.endswith(".md") and file != "orchestrator.md":
                    display_name = file.replace(".md", "").replace("-", " ").title()
                    found_agents.append((dept_key, display_name))
    
    agents_by_dept = {}
    for dept_key, name in found_agents:
        if dept_key not in agents_by_dept: 
            agents_by_dept[dept_key] = []
        agents_by_dept[dept_key].append(name)

    for dept_key in sorted(agents_by_dept.keys()):
        label, dept_name, color = dept_map[dept_key]
        print(f"{color}{label}\033[0m {dept_name}")
        for agent in sorted(agents_by_dept[dept_key]):
            print(f"  - {agent}")
        print()
            
    print("\033[38;5;250mAvailable Commands:\033[0m")
    print("  - \033[38;5;63m/film-init\033[0m     Initialize new season")
    print("  - \033[38;5;63m/film-discovery\033[0m Launch discovery phase")
    print("  - \033[38;5;63m/film-status\033[0m   Check agent status")
    print("  - \033[38;5;63m/film-reflect\033[0m  Launch I2A reflection cycle")
    print("  - \033[38;5;63m/film-update\033[0m   Pull latest system updates")
    print()

def cmd_init(args):
    # Strict Limit: One season per project
    seasons_dir = os.path.join("output", "seasons")
    if os.path.exists(seasons_dir):
        existing = [d for d in os.listdir(seasons_dir) if os.path.isdir(os.path.join(seasons_dir, d))]
        if existing:
            print(f"\033[31m✘ Ошибка:\033[0m Сезон уже существует: \033[36m{existing[0]}\033[0m.")
            print("  В данный момент разрешен только один активный сезон на проект.")
            return

    season_name = args.season or f"Season-01-{datetime.now().strftime('%Y%m')}"
    season_path = os.path.join("output", "seasons", season_name)
    
    os.makedirs(os.path.join(season_path, "blueprints"))
    os.makedirs(os.path.join(season_path, "production"))
    os.makedirs(os.path.join(season_path, "distribution"))
    
    # Create Season DNA Stub
    with open(os.path.join(season_path, "blueprints", "season_dna.yaml"), "w", encoding='utf-8') as f:
        f.write(f"season_id: {season_name}\nstatus: planning\ncreated_at: {datetime.now().isoformat()}")

    print(f"\033[32m✓\033[0m Инициализирован новый сезон: {season_path}")

def cmd_update(args):
    print("\033[38;5;244m> Проверка обновлений...\033[0m")
    try:
        # Simple git pull
        result = os.popen("git pull").read()
        print(f"\033[32m{result}\033[0m")
        print("\033[32m✓\033[0m Система обновлена.")
    except Exception as e:
        print(f"\033[31m✘ Ошибка обновления: {e}\033[0m")

def cmd_discovery(args):
    print_banner()
    
    # Detect Season
    seasons_dir = os.path.join("output", "seasons")
    if not os.path.exists(seasons_dir):
        print("\033[31m✘ Ошибка:\033[0m Директория 'output/seasons' не найдена.")
        print("  \033[38;5;250mДействие:\033[0m Пожалуйста, запустите '\033[38;5;63mpython lib/orchestrator.py init\033[0m'.")
        return
        
    seasons = [d for d in os.listdir(seasons_dir) if os.path.isdir(os.path.join(seasons_dir, d))]
    production_seasons = [d for d in seasons if d != "Season-00-Genesis"]
    
    if not production_seasons:
        print("\033[31m✘ Ошибка:\033[0m Активный сезон не найден.")
        print("  \033[38;5;250mДействие:\033[0m Запустите '\033[38;5;63mpython lib/orchestrator.py init\033[0m'.")
        return
        
    active_season = sorted(production_seasons)[-1]
    print(f"\033[38;5;63m▸ Режим Discovery для {active_season} активен.\033[0m")
    print()
    print("  \033[38;5;250mСледующий шаг:\033[0m")
    print("  Пожалуйста, начните свободный диалог с агентом \033[36mMeaning Owner\033[0m.")
    print("  Он проведет вас через интервью и поможет собрать данные для Эпизода 01.")
    print()
    print("\033[32m✓\033[0m Окружение готово.")

def main():
    parser = argparse.ArgumentParser(description="os_cinema Orchestrator CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Command: status
    parser_status = subparsers.add_parser("status", help="Check system status")
    
    # Command: init
    parser_init = subparsers.add_parser("init", help="Initialize a new season")
    parser_init.add_argument("--season", type=str, help="Season identifier")

    # Command: update
    parser_update = subparsers.add_parser("update", help="Update the system")

    # Command: discovery
    parser_discovery = subparsers.add_parser("discovery", help="Launch post-init discovery phase")

    args = parser.parse_args()
    
    if args.command == "status":
        cmd_status(args)
    elif args.command == "init":
        cmd_init(args)
    elif args.command == "update":
        cmd_update(args)
    elif args.command == "discovery":
        cmd_discovery(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
